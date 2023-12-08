"""
GNU General Public License Version 3

Created by Noah Lobbe, November 2023
"""

#standard python libraries
import os
import json
import aiohttp
import datetime
import random as rand
import logging

#denpendencies
import discord
import discord.ext.commands
import discord.ext.tasks
from dotenv import load_dotenv


#other files
import h_functions


###Constants
DEBUG_MODE = True
VERBOSE_MODE = True #prints everything to another channel as well as printing to terminal
DAVE_MODE = True

JSON_INDENTS = 4
DATA_FILE = "data.json"

# trigger stuff
# Mon==0,...Sun==6 according to datetime.weekday() documentation. Tad messy for stringifying due to the conflict of strftime() and weekday()
DAYS_LEGEND = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6} 

TIMEZONE = datetime.timezone(datetime.timedelta(hours=10.5))  #Adelaide is 10.5 hours ahead of UTC
TRIGGER_TIME = datetime.time(hour=13, minute=55, tzinfo=TIMEZONE) 
TRIGGER_DAY_STR = "Friday" #"Saturday"
TRIGGER_DAY_NUM =   DAYS_LEGEND[TRIGGER_DAY_STR]
TRIGGER_SETUP_MSG = f"Deployment set for {TRIGGER_DAY_STR} @ {TRIGGER_TIME.strftime('%H:%M')}" 

#bot setup
BotIntents = discord.Intents.default()
BotIntents.message_content = True 
Bot = discord.ext.commands.Bot(command_prefix=".", intents=BotIntents)

CHANNEL = None #the channel to post messages into
PRIVILEGED_MEMBERS = set() #wanted something immutable
AUTHOR = None


### Secrets helper functions
def _getBotToken():
    """Returns str"""
    BOT_TOKEN = os.getenv("STRYPER_BOT_TOKEN")
    #assert BOT_TOKEN is not None
    logging.info("Bot token successfully obtained from secrets")
    return BOT_TOKEN


def _loadPrivilegedMembers():
    """Loads the usernames of discord members who have Bot privileges"""
    global PRIVILEGED_MEMBERS, AUTHOR
    ## general privileged
    privileged_member_names_str = os.getenv("PRIVILEGED_MEMBER_NAMES")
    #assert privileged_member_names_str is not None
    if privileged_member_names_str is not None:
        logging.info("Privileged member names successfully obtained from secrets")
    else:
        logging.debug("privileged_member_names_str is None")

    privileged_member_names = privileged_member_names_str.split(',')
    privileged_members_list = []
    
    for name in privileged_member_names:
        privileged_members_list.append(name)
    
    ## get author too.
    author_name = os.getenv("AUTHOR_NAME")
    #assert author_name is not None
    if author_name is not None:
        logging.info("Author name successfully obtained from secrets")
    else:
        logging.debug("author_name is None")

    if author_name not in privileged_members_list:
        privileged_members_list.append(author_name) #order doesn't matter as it wil be turned into a `set``

    PRIVILEGED_MEMBERS = set(privileged_members_list)
    AUTHOR = author_name

    logging.info("AUTHOR: '%s' | PRIVILEGED_MEMBERS: %s", AUTHOR, PRIVILEGED_MEMBERS)


async def _getChannel(debug_mode=True):
    """Returns a discord.py Channel object to be used"""
    if debug_mode:
        logging.info("Using debug mode channel")
        channel_id_str = os.getenv('DEBUG_CHANNEL_ID')
    else:
        channel_id_str = os.getenv('DEPLOYED_CHANNEL_ID')

    if channel_id_str.isdigit():
        channel_id = int(channel_id_str)
    
        channel = Bot.get_channel(channel_id)
        if channel is None:
            logging.debug("channel is None, ID from secrets is %s", channel_id)
        else:
            logging.info("channel successfully madet, %s", channel.name)
        return channel
    else:
        logging.debug("channel_id_str has been corrupted, fails .isdigit() test: %s", channel_id_str)
        return False


    




### Data file helper function(s)
def _doesDataFileExist():
    """Returns bool. True if already existed, and False if file had to be made"""
    if not os.path.exists(DATA_FILE):
        logging.info("Making '%s'", DATA_FILE)

        with open(DATA_FILE, "w+") as new_file:
            data = {
                "songs": [], 
                "templates":[]
                }
            json.dump(data, new_file, indent=JSON_INDENTS)
        return False
    return True


def _getData():
    """Returns JSON object of whole file"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)

def _writeData(new_data):
    with open(DATA_FILE, "w") as write_file:
        json.dump(new_data, write_file, indent=JSON_INDENTS)


### Templates helper functions
def _getTemplates():
    """Returns a list of templates"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)["templates"]
    

def _writeTemplates(new_template):
    """Writes templates to database"""
    current_database = _getData()
    current_templates_list = current_database["templates"]

    #with open(DATA_FILE, "w") as write_file:
    current_templates_list.append(new_template)
    _writeData(current_database)

        #json.dump(current_database, write_file, indent=JSON_INDENTS)

    
def _randomTemplate():
    """Returns str"""
    templates = _getTemplates()
    if len(templates) > 0:
        return rand.choice(_getTemplates())
    else:
        default = "***Hello everybody and WELCOME to Stryper Saturday!!!*** \nToday is the amazing song *{title}*, with a rating of {rating}/10: {url}" 
        _writeTemplates(default)
        return default


def _insertSongToTemplate(template, song):
    """Returns a str which has made o"""

    replacements = [
        ("{title}", song["title"]),
        ("{url}",song["url"]),
        ("{rating}", str(song['rating'])), #has to be a str for .replace(...)
        ("{notes}", song["notes"])
    ]

    new_string = template
    for replacement in replacements:
        new_string = new_string.replace(replacement[0], replacement[1])
    return new_string

        
def _isValidTemplate(raw_template):
    """Returns bool"""
    has_title = "{title}" in raw_template
    has_rating = "{rating}" in raw_template
    has_url = "{url}" in raw_template

    return (has_title and has_rating and has_url), (has_title, has_rating, has_url)


def _doesTemplateExist(templates_list, template):
    """Returns (bool, int). True if already exists, int of index if it exists, 0 otherwise."""
    for i, t in enumerate(templates_list):
        if (t == template):
            logging.info("Template exists in database!")
            return True, i
    return False, 0


def _addTemplate(new_template):
    """Returns bool. True if successful, False otherwise"""
    
    current_data_file = _getData()
    current_templates_list = current_data_file["templates"]

    template_already_exists, index = _doesTemplateExist(current_templates_list, new_template)
    if not template_already_exists:
        
        current_data_file["templates"].append(new_template)

        _writeData(current_data_file)
        #with open(DATA_FILE, "w") as write_file:    
            #json.dump(current_data_file, write_file, indent=JSON_INDENTS)
        
        return True
    return False





### songs helper functions
def _getSongs():
    """Returns list of songs"""
    with open(DATA_FILE, "r") as read_file:
        return json.load(read_file)["songs"]
    

def _songMessage(song):
    """Returns two strings based on the 'song' <dict>, the first is the main bit, 
    and the second is the notes to be posted afterwards"""
    '''
    intro = "***Hello everybody and WELCOME to Stryper Saturday!!!***" 
    description = f"\nToday is the amazing song *{song['title']}*, with a rating of {song['rating']}/10: "
    link = song["url"]
    notes = song["notes"]
    return (intro + description + link), notes
    '''
    if type(song["notes"]) != str:
        song["notes"] = " ".join(song["notes"]) #concatenate, otherwise a list of the notes will be inserted into template

    template = _randomTemplate()
    body = _insertSongToTemplate(template, song)
    notes = song["notes"]

    return body, notes
    



def _doesSongExist(songs_list, song_url):
    """Returns (bool, int). 
    Bool for the existence of song in database, and int of index of existing song.
    If song doesn't exist, then index is 0. Based on 'song_url' (str)"""
    print(f"in _doesSongExist(), song_url: {song_url} ")
    for i, s in enumerate(songs_list):
        if (song_url == s["url"]):
            logging.info("Song exists in database!")
            return True, i
    return False, 0

   
def _addSong(title, url, rating, notes):
    """Returns True if successful in adding the song to database or overwriting if""" ##################################finish
    new_song = {"title":title, "url":url, "rating":rating, "notes":notes}
    logging.debug("in addSong(), url: %s", new_song['url'])

    current_data_file = _getData()
    current_songs_list = current_data_file["songs"]

    song_already_exists, index_of_song = _doesSongExist(current_songs_list, new_song["url"])
    if not song_already_exists:
        current_songs_list.append(new_song) #add song to database
        _writeData(current_data_file)
        return True
    else:
        return False


def _updateSong(song_url, new_rating, new_notes):
    """Updates song rating and notes in database if it exists. Returns bool of success/failure, messsage str"""    
    current_data_file = _getData()
    current_songs_list = current_data_file["songs"]

    song_already_exists, index_of_song = _doesSongExist(current_songs_list, song_url)

    if song_already_exists:
        rating_is_legit = h_functions._validateRating(new_rating)
        if rating_is_legit:
            #update song entry    
            current_songs_list[index_of_song]["rating"] = new_rating
            current_songs_list[index_of_song]["notes"] = new_notes

            _writeData(current_data_file)
            #with open(DATA_FILE, "w") as write_file:
                #json.dump(current_data_file, write_file, indent=JSON_INDENTS)
            return True, "success"
        return False, "invalid rating"
    return False, "doesn't exist"


def _getSong(index):
    """Returns a song dict of the given index in database"""
    songs_list = _getSongs()
    return songs_list[index]


def _getRandomSong():
    "Returns a song dict"
    songs_list = _getSongs()
    song_dict = rand.choice(songs_list)
    return song_dict

def _strSong(song, suppress_link=True):
    """Returns a nice string of the song"""
    link_str = (suppress_link * '<') + song['url'] + (suppress_link * '>')
    return f"{song['title']} ({link_str}) with rating {song['rating']}/10, {song['notes']}"


### both song and template helper functions
def _remove(key, raw_index):
    """Removes the item of index from database[key], and returns a msg string"""
    data = _getData()
    num_items = len(data[key])
    index = None
    if raw_index.isdigit(): #doesn't accept negative indices
        index = int(raw_index)

        if index < num_items:
            removed_item = data[key].pop(index)
            _writeData(data)
            if key == "songs":
                str_item = _strSong(removed_item)
            elif key == "templates":
                str_item = removed_item

            return f"'{str_item}' has been removed"
        
    return "index must be an integer from 0 to " + str(num_items-1)



### Bot functions (not 'slash' commands)
async def isMemberPrivileged(Context):
    """Returns bool"""
    ctx_message = Context.message
    return ctx_message.author.name in PRIVILEGED_MEMBERS


async def postSong(Context, song):
    """Uses the 'song' (dict) to make prettier text to post to 'Context'"""
    msg, note = _songMessage(song)
    await Context.send(msg)
    if note != "": await CHANNEL.send(note)


async def addSong(Context, title, url, rating, raw_notes):
    """Returns bool of success/failure"""
    #prep and add song to songs file        
    notes = ""
    if len(raw_notes) > 2:
        notes = " ".join(raw_notes[2:])
        
    is_success = _addSong(title, url, rating, notes)
    if is_success:
        await postSong(Context, _getSong(-1))
        logging.info("Adding song to database successful")
        return True
    else:
        error_msg = "Already added! Update entry using .update command"
        await Context.send(error_msg)
        logging.debug(error_msg)
        return False


@discord.ext.tasks.loop(time=TRIGGER_TIME)
async def trigger(channel):
    """'Triggers' everyday at a certain time, but only properly triggers if today is the correct day"""
    DateNow = datetime.datetime.now()
    day_num = DateNow.weekday()
    if day_num == TRIGGER_DAY_NUM:
        
        logging.info("Triggered")

        #"""
        #get messages from today
        year = DateNow.year
        month = DateNow.month
        day = DateNow.day
        tzinfo = TIMEZONE
        AfterDate = datetime.datetime(year=year, month=month, day=day, tzinfo=tzinfo)

        Msg_Iter = channel.history(after=AfterDate, oldest_first=False)
    
        enacted_bit_map = []

        msg_clumps = {}

        prev_author = ""

        i = 0
        async for Msg in Msg_Iter:
            if Msg.author == Bot.user:
                logging.debug("...skipping self...")
            else:
                #is SS enacted for Msg??
                logging.debug("\ti: %s, author: %s  | content: %s", i, Msg.author, Msg.content)
                yt_video_template_str = "https://www.youtube.com/watch?v="
                yt_video_id_len = 11 #may change in future depending on YouTube's system; not likely though :D

                            
                is_stryper_mentioned = "stryper saturday" in Msg.content.lower() 
                has_rating = "rating" in Msg.content.lower()
                yt_link_present = yt_video_template_str in Msg.content

                if yt_link_present:
                    #grab
                    slice_start = Msg.content.find(yt_video_template_str)
                    slice_end = slice_start + len(yt_video_template_str) + yt_video_id_len
                    yt_url = Msg.content[slice_start:slice_end]

                    logging.debug("\tstart: %s, end: %s, url: %s", slice_start, slice_end, yt_url)

                    is_valid_yt, _yt_title, _clean_url = h_functions._validateYoutubeURL(yt_url)

                    logging.debug("\tUrl validation: %s, title: %s, clean: %s", is_valid_yt, _yt_title, _clean_url)

                else:
                    is_valid_yt = False


                if is_stryper_mentioned or has_rating or is_valid_yt:
                    # add to list to check through
                    msg_conditions = [is_stryper_mentioned, has_rating, is_valid_yt] 
                    logging.debug("prev_author: %s, msg_clumps: %s", prev_author, msg_clumps)
                    if Msg.author == prev_author:
                        #make sure there is a list ready, otherwise KeyError
                        if prev_author not in msg_clumps:
                            msg_clumps[prev_author] = []

                        logging.info("...adding to existing clump...")
                        msg_clumps[prev_author].append(msg_conditions) # add to list to keep clump
                    else:
                        logging.info("...making new clump...")
                        msg_clumps[Msg.author] = [msg_conditions] # make a new clump

                    #msg_conditions_list.append(msg_conditions)
            prev_author = Msg.author
            i += 1

        logging.info("\nProcessing clumbs...")
        #go through each clump
        enactors = {}
        for author, msg_properties_list in msg_clumps.items():
            logging.debug("author: %s, msg_properties_list: \n%s", author, h_functions._str2DList(msg_properties_list))
            #msg_properties_list is a 2D list
            col_bitwise_or_results = []
            #bit-wise OR each column together
            num_cols = len(msg_properties_list[0])
            num_rows = len(msg_properties_list)

            for col in range(num_cols):
                col_bit_list = []
                for row in range(num_rows):
                    col_bit_list.append(msg_properties_list[row][col])

                OR_result = any(col_bit_list) 
                col_bitwise_or_results.append(OR_result)

                logging.debug("col:%s, col_bit_list: %s, OR_result: %s", col, col_bit_list, OR_result)


            stryper_saturday_enacted = all(col_bitwise_or_results)
            logging.info("col_bitwise_or_results: %s, stryper_saturday_enacted: %s", col_bitwise_or_results, stryper_saturday_enacted)

            if stryper_saturday_enacted:
                if author not in enactors: #add blank entry
                    enactors[author] = 0
                
                enactors[author] += 1

        logging.info("enactors: %s", enactors)

        #respone
        num_enactors = len(enactors.keys())
        if num_enactors > 1:
            msg = "Looks like Stryper central today, as my alogrithm is telling me *more than one* person is enacting Stryper Saturday!!!"

        elif num_enactors != 0:
            if DAVE_MODE:
                User = list(enactors.keys())[0]
                msg = f"{User.mention} grrrrrrrr"
            else:
                msg = "**Rock on!**"


            await channel.send(msg)
            logging.info(msg)
        else:
            logging.info("no enactors, so posting...")
            song = _getRandomSong()
            await postSong(channel, song)

        '''
        already_enacted = True in enacted_bit_map

        if not already_enacted:
            pass #enact
        else:
            pass #reply with a 'oo-rah!!!' kinda of message??? (REPLY @ ENACT-TOR)
        '''



        
        #"""
    else:
        day_str = h_functions._getDictKey(DAYS_LEGEND, day_num) 
        msg = f"Wrong day to trigger as today is {day_str} not {TRIGGER_DAY_STR} \n:("

        await CHANNEL.send(msg)
        logging.info(msg)



### 'slash' commands (prefix defined in Bot constructor)
@Bot.command()
async def alive(Context):
    """Simple test slash command to determine if Bot is operating. Anybody can call this."""
    msg = f"*I **AM** ALIVE!!!*"
    await Context.send(msg)
    logging.info(msg)



## song slash commands
@Bot.command()
async def random(Context):
    """Posts a random song from database, provided the member to call random has the privilege"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        song = _getRandomSong()
        await postSong(Context, song)
        logging.info("Random song is: %s", song)


@Bot.command()
async def add_s(Context, youtube_url, rating, *raw_notes):
    """Adds song to database. 'rating' needs to be a positive float (decimal) from 0 to 10,
    and 'raw_notes' is just in case someone adds song notes without quotes, as discord.py
    seems to split arguements by spaces."""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        logging.info("User inputted: '%s', '%s', and '%s'", youtube_url, rating, raw_notes)

        #validate user input
        url_is_legit, yt_title_or_error, clean_yt_url = h_functions._validateYoutubeURL(youtube_url)
        rating_is_legit, rating_error_msg = h_functions._validateRating(rating)
        
        #output stuff
        if url_is_legit and rating_is_legit:
            is_successful = await addSong(Context, yt_title_or_error, clean_yt_url, rating, raw_notes)
            if is_successful:
                msg = "Added!"
            else:
                msg = "Adding song to databse failed"
        else:    
            if url_is_legit and not rating_is_legit:
                msg = rating_error_msg

            elif not url_is_legit and rating_is_legit:
                msg = yt_title_or_error

            else:
                msg = yt_title_or_error + ", and " + rating_error_msg 
                
        logging.info(msg)
        await Context.send(msg)


@Bot.command()
async def update(Context, song_url, new_rating, *new_notes):
    """Updates database provided the song_url is in the database"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        url_is_legit, _, clean_url = h_functions._validateYoutubeURL(song_url)

        if url_is_legit:
            is_successful, status_msg = _updateSong(clean_url, new_rating, new_notes)

            if is_successful:
                msg = status_msg
            else:
                msg = f"ERROR: {status_msg}"  
        else:
            is_url_suppressed = ('<' in song_url) and ('>' in song_url)
            url = (is_url_suppressed * '<') + song_url + (is_url_suppressed * '>')
            msg = f"ERROR: invalid url passed, '{url}'"

        await Context.send(msg)
        logging.info(msg) 


@Bot.command()
async def remove_s(Context, raw_index):
    """Remove a song from database"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        msg = _remove("songs", raw_index)
        logging.info(msg)
        await Context.send(msg)


@Bot.command()
async def songs(Context):
    """Prints all the songs from database nicely"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        logging.info("printing song database...")
        msg = "Song database: \n"

        for i, song in enumerate(_getSongs()):
            raw_notes = song["notes"]
            if type(raw_notes) != str:
                notes = " ".join(song["notes"])
            else:
                notes = raw_notes
            msg += f"\t{i}: {song['title']}, <{song['url']}>, {song['rating']}/10, {notes} \n"

        await Context.send(msg)
        logging.info(msg)



##template slash commands
@Bot.command()
async def add_t(Context, *raw_new_template_parts):
    """Add a template string to database"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        #print(raw_new_template_parts)
        new_template = " ".join(raw_new_template_parts)
        is_valid, code_bools = _isValidTemplate(new_template)

        if is_valid:
            is_successful = _addTemplate(new_template)
            if is_successful:
                msg = "Success"
            else:
                msg = "Template already exists!"     
                
        else:
            msg = f"ERROR adding new template: '{new_template}':"
            #determine error message based on `code_bools`
            if not code_bools[0]:
                msg += "\n\tRequires title code '{title}'"
            if not code_bools[1]:
                msg += "\n\tRequires rating code '{rating}'"
            if not code_bools[2]:
                msg += "\n\tRequires url code '{url}'"
            
        await Context.send(msg)
        logging.info(msg)


@Bot.command()
async def remove_t(Context, raw_index):
    """Remove a template string from database"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        msg = _remove("templates", raw_index)
        logging.info(msg)
        await Context.send(msg)


@Bot.command()
async def templates(Context):
    """Prints all the templates from database nicely"""
    is_member_privileged = await isMemberPrivileged(Context) 
    if is_member_privileged:
        logging.info("printing template database...")
        msg = "Template database: \n"

        for i, template in enumerate(_getTemplates()):
            msg += f"\t{i}: {template} \n"

        await Context.send(msg)
        logging.info(msg)



###event commands
@Bot.event
async def on_ready():
    """Runs when Bot is ready, kind of like a class constructor/init/"""
    #setup variables
    global CHANNEL
    CHANNEL = await _getChannel(DEBUG_MODE) 

    _loadPrivilegedMembers()

    data_already_exists = _doesDataFileExist()

    logging.info(f"{Bot.user} has connected to Discord, into '{CHANNEL}' channel!")
    await CHANNEL.send(TRIGGER_SETUP_MSG)
    logging.info(TRIGGER_SETUP_MSG)

    if not data_already_exists:
        msg = "ERROR: database is empty, please fill..."
        await CHANNEL.send(msg)
        logging.debug(msg)

    #loop functions
    await trigger.start(CHANNEL)




if __name__ == "__main__":
    #make logging setup
    log_folder = "logs"
    if not os.path.isdir(log_folder):
        os.mkdir(log_folder) 

    log_file = log_folder + "/" + "verbose output " + datetime.datetime.now().strftime("%Y %b %d, %H;%M;%S") + ".log"
    logging.basicConfig(filename=log_file, encoding="utf-8", level=logging.DEBUG)

    load_dotenv()  #enable os.getenv() to actually get 'environment variables' from .env file

    try:
        logging.info("running...")
        Bot.run(_getBotToken())

    except aiohttp.client_exceptions.ClientConnectorError as e:
        logging.debug("...oops I caught a connection error running the bot: \n\t%s", e)
