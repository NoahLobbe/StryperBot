# StryperBot
A Discord bot made to automate Stryper Saturdays. Stryper Saturdays are when a Stryper song is posted on a Discord server for all to enjoy. However, sometimes someone forgets to post one, so automation is a solution.

"But what if I still want to do it myself?" you say. The answer is that StryperBot is intended to determine whether someone has already enacted Stryper Saturday, and if so, step down. However, if no-one has enacted Stryper Saturday then StryperBot will do so. The exact time the Discord members have till StryperBot posts is undetermined as of yet. ***Currently unsupported***

This code should be pretty easy to customise too, so it doesn't *have* to be a Stryper Saturdays bot :D

## Dependencies
Listed in [`requirements.txt`](requirements.txt)

## Testing Scripts
These files are probably not very easy to read, but were helpful in testing stuff quickly without the whole circus.

## Data Strucutre
`data.json` is the database file. The highest level entries (or keys) are currently `songs` and `templates`.
- `songs`: contains a `list` of each song 'object':
    - A song 'object' is a `dict` consisting of the keys `title`, `url`, `rating`, and `notes`. When adding a song to the database, `notes` is an optional part. `rating` is `int` while the rest are `str`.
- `templates`: contains a `list` of each template
    - A template is ...


## Deployment
# Adding Bot to server
It is recommended that a 'superuser'/'debug' server/guild or text channel is allocated to the Bot. This is so that the main server channel doesn't get cluttered with commands to the Bot.
***As for the instructions for adding the Bot to a server...I will get around to it :D***


# Secrects - Bot tokens, etc.
Without knowing an business/industry methods for storing secrets, the secrets should be stored in the environment/system variables of the machine the Bot is running on. However, if the Bot is being run off an external server, then a file accessible by the Bot is the 'best' next way. Currently, a `.env` file is being used for secrets, using `python-dotenv` library to make `os.getenv("token string")` read from a `.env` instead from system environment variables, easily.

Secrets:
- `STRYPER_BOT_TOKEN` (obviously)
- `DEBUG_CHANNEL_ID` is the separate debug channel.
- `DEPLOYED_CHANNEL_ID` is the channel to be active in.
- `AUTHOR_NAME` is the discord username of the author/owner of the Bot. Allows 'superuser' privileges, eg 'slash' commands.
- `PRIVILEGED_MEMBER_NAMES` is the list of members who have the privilege to use 'slash' commands. Example: `PRIVILEGED_MEMBER_NAMES=username1,username2`


# 'Slash' Commands
'Slash' commands can only be run by those in `PRIVILEGED_MEMBERS`, type is `set`, (which also contains `AUTHOR_NAME` for ease of use). Currently, it does not matter what channel the privileged member is to use any 'slash' command, it will respond in the same channel.

Commands:
- `alive`: post a message saying its alive. Basically a command (available to **everyone**) to check if it is running.
- `add`: adds a song to database. Has parameters `youtube_url` (`str`), `rating` (`int`, from 0 to 10), and `notes` (`str`) which can be contain in quotes or not (program currently doesn't care) and is just any additional thoughts on that song. Example (Discord channel): `.add https://www.youtube.com/watch?v=sG0zAn0dL2I 10 Surely one of the best ever Stryper has done!`
- ***...more to come...***

Slash command prefix is `.` instead of the default (?) `/`. Therefore, to trigger `alive`, post `.alive` in discord channel