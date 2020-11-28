# Early Alpha 0.1 - (2020-11-05)
- Added new cog - utils.py
- Added command - $avatar [EU/RU]
- Added command - $random [EU/RU]
- Added command - $time [EU/RU]
- Added command - $wiki [EU/RU]
- Added 'RANDOM COLOR' to the cogs_color dictionary
- Added 'RANDOM COLOR ERROR' to the cogs_color dictionary
- Added 'TIME COLOR' to the cogs_color dictionary
- Added 'WIKIPEDIA COLOR' to the cogs_color dictionary
- Added 'WIKIPEDIA COLOR ERROR' to the cogs_color dictionary
- Renamed 'NAME BOT' to 'BOT NAME' to the settings dictionary
- Added 'OWNER PING' to the settings dictionary

# Early Alpha 0.1.1 - (2020-11-06)
- Added new cog - owner.py
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

# Early Alpha 0.1.2 - (2020-11-07)
- Fixed a small bug in the dictionaries config
- Added new cog - info.py
- Added command stub $help (Just a template)
- Added new dictionary - other_settings
- Added 'COMMAND VALUE' to the other_settings dictionary
- Added command - $ahelp [EU/RU] [Owner Only]

# Early Alpha 0.1.3 - (2020-11-08)
- Added explanations for the commands $clear_all_emoji
- Added explanations for the commands $clear_emoji
- Added explanations for the commands $delete_emoji
- Added explanations for the commands $emoji
- Added command - $info [EU/RU]
- Added 'BOT INFO COLOR' to the cogs_color dictionary
- Added 'CURRENT PATCH' to the other_settings dictionary
- Added 'SPECIAL THANKS' to the settings dictionary

# Early Alpha 0.1.4 - (2020-11-09)
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
- Added 'THIRD PARTY SYM ERROR' to the quick_messages dictionary
- Added 'THIRD PARTY SYM ERROR EN' to the quick_messages dictionary
- Renamed 'UNKNOWN ERROR ENLISH' to 'UNKNOWN ERROR EN'
- Added 'THIRD PARTY SYM ERROR LOG' to the quick_messages dictionary
- Fixed missing English translation in 'UNKNOWN ERROR EN'
- Added command - $server [EU/RU]
- Added 'SERVER INFO COLOR' to the cogs_color dictionary
- Small changes the text of the log output in the command $time [EU/RU]
- Added 'CURRENT VERSION' to the other_settings dictionary
- Added 'STREAM URL' to the fast_link dictionary
- Added 'WIKIPEDIA IMG' to the fast_link dictionary

# Early Alpha 0.1.4.1 - (2020-11-10)
- Fixed 'OWNER PING' to the settings dictionary
- Added command - $achievement [EU/RU]
- Added 'MCACH' to the fast_link dictionary
- Added 'MCACH COLOR' to the cogs_color dictionary


# Early Alpha 0.1.5 - (2020-11-11)
- Added command - $ping [EU/RU]
- Added command - $timeup [EU/RU]
- Added 'TIMEUP COLOR' to the cogs_color dictionary
- Added an alternative command for $bot [EU/RU]
- Added an alternative command for $server [EU/RU]
-  Added an alternative command for $ahelp [EU/RU]

Early Alpha 0.1.6 - (2020-11-12)
- Created a new python module - useful
- Moved functionality from the "clock" module to the "useful" module
- Removed python module - clock
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

# Early Alpha 0.1.6.1 - (2020-11-14)
- Changed 'COMMAND VALUE' to 21 in the other_settings dictionary
- Moved the 'translit_abc' variable from the 'utils' cog to useful.py
- Moved the 'ru_layout' variable from the 'utils' cog to useful.py
- Fixed incorrect command in the log in the correct command $translit [EU/RU]

# Early Alpha 0.1.6.2 - (2020-11-27)
- Improved a $random [EU/RU]
- Fixed TypeError in the $random [EU/RU]
