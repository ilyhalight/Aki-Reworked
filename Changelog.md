Early Alpha 0.1 - (2020-11-05)
- Added new cog - utils.py
- Added command - $avatar [EU/RU]
- Added command - $random [EU/RU]
- Added command - $time [EU/RU]
- Added command - $wiki [EU/RU]
- Added custom python module - clock
- Added new dictionary - cogs_color, settings
- Added 'RANDOM COLOR' to the cogs_color dictionary
- Added 'RANDOM COLOR ERROR' to the cogs_color dictionary
- Added 'TIME COLOR' to the cogs_color dictionary
- Added 'WIKIPEDIA COLOR' to the cogs_color dictionary
- Added 'WIKIPEDIA COLOR ERROR' to the cogs_color dictionary
- Renamed 'NAME BOT' to 'BOT NAME' to the settings dictionary
- Added 'OWNER PING' to the settings dictionary

Early Alpha 0.1.1 - (2020-11-06)
- Added new cog - Owner.py
- Added command - $emoji [Owner Only]
- Added command - $del_emoji [Owner Only]
- Added command - $clear_emoji [Owner Only]
- Added command - $clear_all_emoji [Owner Only]
- Added command - $bot_status [Listen/Playing/Streaming/Watching] [Owner Only]
- Fixed bug in one of the options for displaying error $random
- Added new dictionary - quick_messages
- Added 'UNKNOWN ERROR LOG' to the quick_messages dictionary
- Added 'UNKNOWN ERROR' to the quick_messages dictionary
- Added 'COPYRIGHT RU' to the quick_messages dictionary
- Added 'COPYRIGHT EN' to the quick_messages dictionary
- Added 'BOT STATUS LOG' to the quick_messages dictionary

Early Alpha 0.1.2 - (2020-11-07)
- Fixed a small bug in the dictionaries config
- Added new cog - info.py
- Added command stub $help (Just a template)
- Added new dictionary - other_settings
- Added 'COMMAND VALUE' to the other_settings dictionary
- Added command - $ahelp [EU/RU] [Owner Only]

Early Alpha 0.1.3 - (2020-11-08)
- Added explanations for the commands $clear_all_emoji
- Added explanations for the commands $clear_emoji
- Added explanations for the commands $delete_emoji
- Added explanations for the commands $emoji
- Added command - $info [EU/RU]
- Added 'BOT INFO COLOR' to the cogs_color dictionary
- Added 'CURRENT PATCH' to the other_settings dictionary
- Added 'SPECIAL THANKS' to the settings dictionary

Early Alpha 0.1.4 - (2020-11-09)
- Small optimized code
- Fixed a bug with the lack of russification in the command - $хелп [No arguments]
- Deleted the variable 'unknown' from the info.py
- Deleted the variable 'unknown_log' from the info.py
- Fixed incorrect translation language in the error output logs for the command - $вики
- Added 'UNKNOWN ERROR ENGLISH' to the quick_messages dictionary
- Added new dictionary - fast_link
- Added 'TIME MSC' to the fast_link dictionary
- Fixed display of ValueError for the command $ранд
- Added 'TIME CET' to the fast_link dictionary
- Added 'THIRD PARTY SYM ERROR' to the fast_link dictionary
- Added 'THIRD PARTY SYM ERROR EN' to the fast_link dictionary
- Renamed 'UNKNOWN ERROR ENLISH' to 'UNKNOWN ERROR EN'
- Added 'THIRD PARTY SYM ERROR LOG' to the fast_link dictionary
- Fixed missing English translation in 'UNKNOWN ERROR EN'
- Added variable 'third_sym_log' to utils.py
- Added command - $server [EU/RU]
- Added 'SERVER INFO COLOR' to the cogs_color dictionary
- Small changes the text of the log output in the command $time [EU/RU]
- Added 'CURRENT VERSION' to the other_settings dictionary
- Added 'STREAM URL' to the fast_link dictionary
- Added 'WIKIPEDIA IMG' to the fast_link dictionary

Early Alpha 0.1.4.1 - (2020-11-10)
- Fixed 'OWNER PING' to the settings dictionary
- Added command - $achievement [EU/RU]
- Added 'MCACH' to the fast_link dictionary
- Added 'MCACH COLOR' to the cogs_color dictionary

Early Alpha 0.1.5 - (2020-11-11)
- Added command - $ping [EU/RU]
- Added command - $timeup [EU/RU]
- Added 'TIMEUP COLOR' to the cogs_color dictionary
- Added an alternative command for $bot [EU/RU]
- Added an alternative command for $server [EU/RU]
- Added an alternative command for $ahelp [EU/RU]

Early Alpha 0.1.6 - (2020-11-12)
- Created a new custom python module - useful
- Moved functionality from the "clock" module to the "useful" module
- Removed custom python module - clock
- Removed unnecessary module imports in main.py, owner.py, utils.py, info.py
- Added command - $analytics [EU/RU]
- Filled in the command - $help info
- Added new dictionary - emoji
- Added 'ping_emoji' to the emoji dictionary
- Corrected command name from $timeup to $uptime
- Renamed 'TIMEUP COLOR' to 'UPTIME COLOR' to the cogs_color dictionary
- Added 'PING COLOR' to the cogs_color dictionary
- Added command - $reverse [EU/RU]
- Added 'REVERSE COLOR' to the cogs_color dictionary
- Added command - $translit [EU/RU]
- Added 'TRANSLIT COLOR EXAMPLE' to the cogs_color dictionary
- Renamed 'BOT COLOR ARG ERROR' to 'BOT COLOR EXAMPLE' to the cogs_color dictionary
- Renamed 'CLEAR ALL EMOJI COLOR ERROR' to 'CLEAR ALL EMOJI COLOR EXAMPLE' to the cogs_color dictionary
- Renamed 'CLEAR EMOJI COLOR ERROR' to 'CLEAR EMOJI COLOR EXAMPLE' to the cogs_color dictionary
- Renamed 'DELETE EMOJI COLOR ERROR' to 'DELETE EMOJI COLOR EXAMPLE' to the cogs_color dictionary
- Renamed 'ADD EMOJI COLOR ERROR' to 'ADD EMOJI COLOR EXAMPLE' to the cogs_color dictionary
- Fixed incorrect description of command usage - $delete_emoji
- Fixed a syntax error in the command usage description text - $clear_emoji [does not affect performance]
- Fixed a syntax error in the command usage description text - $clear_all_emoji [does not affect performance]
- Added 'TRANSLIT COLOR ERROR' to the cogs_color dictionary
- Added command - $ru_layout [EU/RU]
- Added 'LAYOUT COLOR EXAMPLE' to the cogs_color dictionary
- Added 'LAYOUT COLOR ERROR' to the cogs_color dictionary

Early Alpha 0.1.6.1 - (2020-11-12)
- Changed 'COMMAND VALUE' to 21 in the other_settings dictionary
- Moved the 'translit_abc' variable from the 'utils' cog to useful.py
- Moved the 'ru_layout' variable from the 'utils' cog to useful.py
- Fixed incorrect command in the log in the correct command $translit [EU/RU]

Early Alpha 0.1.6.2 - (2020-11-27)
- Improved a $random [EU/RU]
- Fixed TypeError in the $random [EU/RU]

Alpha 0.2 - (2020-12-)
- Fixed incorrect command in logs $random [EU/RU]
- Rewrote the main code
- Reworked the cog system (Commands are now separate cogs)
- Launched cogs are now written in the console
- Created a server to help with the bot (https://discord.gg/Vh3VcaEv23)
- Rewrote the bot's greeting in the console
- Added comments to the code
- Fixed incorrect localization of the command $help [info] [EU]
- Added an alternative command for $analytics [EU]
- Added more commands to $help [utils] [EU/RU]
- Added alternative command to $help [utils] [EU/RU]
- Added an additional alternative command to $help [utils] [EU/RU]
- Added a link to the server for a bug report
- Deleted info, owner, utils, main cogs
- Now the bot uses the variable "bot" instead of "client"
- Added and updated third-party сogs f*ck
- Moved the following commands to cogs: help, avatar, random, time, ahelp, info, server_info, emoji, del_emoji, clear_emoji, clear_all_emoji, temporary_bot_status, wiki, achievement, reverse_text, forgot_layout, translit
- Added 'ON GUILD JOIN LOG' to the cogs_color dictionary
- Added new dictionary - channels
- Added 'LOG JOIN CHANNEL' to the channels dictionary
- Added logs about the bot entering the server
- Added 'ON GUILD LEAVE LOG' to the cogs_color dictionary
- Added 'LOG LEAVE CHANNEL' to the channels dictionary
- Added logs about the bot leaving the server
- Added new cogs - uwutalk
- Now there are two versions of cogs: in Russian and English (You can install only 1 version of cog)
- Added 'FUCK U NOT USER' to the cogs_color dictionary
- Added 'FUCK U' to the cogs_color dictionary
- Added 'HELP COLOR' to the cogs_color dictionary
- Changed someone else's cog "PressF" for modern discord.py, And also reworked it to fit the style of my bot
- Added a nice bot launch menu (Use if you run on your pc / Dedicated Server) Special thanks: https://github.com/Wanderson-Magalhaes
- Frequently used variables have been moved to custom module useful.py  (prefix, copyright_ru, copyright_en)