# StryperBot
A Discord bot made to automate Stryper Saturdays. Stryper Saturdays are when a Stryper song is posted on a Discord server for all to enjoy. However, sometimes someone forgets to post one, so automation is a solution.

"But what if I still want to do it myself?" you say. The answer is that StryperBot is intended to determine whether someone has already enacted Stryper Saturday, and if so, step down. However, if no-one has enacted Stryper Saturday then StryperBot will do so. The exact time the Discord members have till StryperBot posts is undetermined as of yet. ***Currently unsupported***

This code should be pretty easy to customise too, so it doesn't *have* to be a Stryper Saturdays bot :D



## Deployment
### Dependencies
Listed in [`requirements.txt`](requirements.txt)


### Adding Bot to server
It is recommended that a 'superuser'/'debug' server/guild or text channel is allocated to the Bot. This is so that the main server channel doesn't get cluttered with commands to the Bot.
***As for the instructions for adding the Bot to a server...I will get around to it :D***


### Operational Notes
The Bot checks these conditions to determine if Stryper Saturday has been enacted:
- 1 `stryper saturday` is contained in message
- 2 `rating` is contained in message
- 3 A link is contained, AND is an official Stryper youtube video 
- 4 The author of the above conditions has to be the same, and the messages (if several) have to be in an unbroken 'clump' or 'set' of messages (no other user 'interupting' with a message betwen them)

#### Dave Mode
Set with the flag `IS_DAVE_MODE`. It affects:
- Response to Stryper Saturday Enactor(s), changes to be more a humourous Dave's style response. **Not fully supported**


### Secrets
Without knowing a business/industry method for storing secrets, the secrets are stored in the environment/system variables of the machine the Bot is running on. However, if the Bot is being run off an external server, then a file accessible by the Bot is the 'best' next way. Currently, a `.env` file is being used for secrets, using `python-dotenv` library to make `os.getenv("token string")` read from a `.env` file, easily.

#### Secrets:
- `STRYPER_BOT_TOKEN` (obviously)
- `DEBUG_CHANNEL_ID` is the separate debug channel
- `DEPLOYED_CHANNEL_ID` is the channel to be active in
- `AUTHOR_NAME` is the discord username of the author/owner of the Bot. Allows 'superuser' privileges, more than just privileged members. ***None yet***
- `PRIVILEGED_MEMBER_NAMES` is the list of members who have the privilege to use 'slash' commands. Example: `PRIVILEGED_MEMBER_NAMES=username1,username2`



## 'Slash' Commands
'Slash' commands can only be run by those in `PRIVILEGED_MEMBERS`, type is `set`, (which also contains `AUTHOR_NAME` for ease of use). Currently, it does not matter what channel the privileged member is to use any 'slash' command, it will respond in the same channel.

#### Commands (slash prefix included):
- `.alive`: basically a command (available to **everyone**) to check if it is running, by replying with a message... :D
- `.add`: adds a song to database. Has parameters `youtube_url` (`str`), `rating` (`float`, from 0 to 10), and `notes` (`str`) which can be contain in quotes or not (script catches it). 
Additionally, suppression of links are also caught, e.g. `<url passed>`.
    - Example (Discord channel): `.add https://www.youtube.com/watch?v=sG0zAn0dL2I 10 Surely one of the best ever Stryper has done!`
- `.update`: updates a song in the database. Has the same parameters as `.add`. Overwrites the `rating` and `notes` of existing song in database.
- ...
- `.add_template`: adds the text after the command as a template for a Stryper Saturday post. **Must** contain template codes (see Data Structure section). Text can be inside quotes or not.
    - Example (Discord channel): `.add_template Greetings fans! \nToday's Stryper Saturday is the song {title}, with a rating of {rating}: {url}`



## Code Notes
### General
As of 2nd December 2023, all functions that are not Bot functions, now start with an underscore, `_`. E.g. 'Bot functions' mean any function that does has a discord/bot decorator and/or a `Context` parameter.

### Style guide:
- Variables are also in the `snake_case`
- Constant variables are in `SCREAMING_SNAKE_CASE`
- Slash commands are in the `snake_case` style for ease of Discord users
- Bot functions are `camelCase`
- Other 'helper' functions are in `_camelCase`, the underscore prefix notation to help indictate that they are helpers. Maybe there is a better method *shrug*; if so let me know!
- Class objects are in `PascalCase`
- `TIMEZONE`, `TRIGGER_TIME`, and `CHANNEL` are objects (from `datetime`) but I haven't figured out something better than `SCREAMING_SNAKE_CASE` as they are meant to be constant as well :D


### Data Strucutre
`data.json` is the database file. The highest level entries (or keys) are currently `songs` and `templates`.
- `songs`: contains a `list` of `dict`'s which represent a `song`
    - `song`: is a `dict` consisting of the keys `title`, `url`, `rating`, and `notes`. `rating` is an `float` (from 0 to 10) while the rest are `str`'s. When adding a song to the database, `notes` is optional. `url` is the property used to determine if a song exists already in the database or not.

- `templates`: contains a `list` of `str`'s which represent a `template`
    - `template`: a `str` containing codes that are reserved for replacement with `song` information. Codes:
        - `{title}` is replaced with song title
        - `{rating}` with song rating
        - `{url}` with song url
        - Song notes are always printed/posted after template, and thus don't have a code


### Other
#### Testing Scripts
These files are probably not very easy to read, but were helpful in testing stuff quickly without the whole circus.

    

## To Do
- Determine how to check for previous posts of Stryper Saturday.
- `.remove`: remove song from database. Not sure about this one
- Finish triggering.
- Catch legitimate non-youtube links when validating
- add a slash command to print song and template entries from database
- add the Dave feature; bot responds to Stryper Saturday Enactor
