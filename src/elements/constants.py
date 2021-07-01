"""
Copyright 2021 Janrey "CodexLink" Licas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Classifications of constants of any kind. (limiters, choices, etc.) | constants.py
# Version dev.0.06232021


if __name__ == "__main__":
    from exceptions import IsolatedExecNotAllowed

    raise IsolatedExecNotAllowed

else:
    from datetime import timedelta as timeConstraint
    from typing import Any, Final, List
    from time import strftime
    from discord import Intents

    # # Classified Arguments Information
    ARG_CONSTANTS: Final[dict[str, str]] = {  # Cannot evaluate less.
        "ENTRY_PARSER_DESC": "An application that runs under workflow to evaluate User's Discord Activity Presence to Displayable Badge for their README.md.",
        "ENTRY_PARSER_EPILOG": "The use of arguments are intended for debugging purposes only. Please be careful.",
        "HELP_DESC_DRY_RUN": "Runs the whole script without commiting changes to external involved factors (ie. README.md)",
        "HELP_DESC_LOG_TO_CONSOLE": "Prints the log output to the console, whenever the case.",
        "HELP_DESC_NO_ALERT_USR": "Does not alert the user / developer from the possible crashes through Direct Messages (this also invokes the do-not-send logs.)",
        "HELP_DESC_NO_LOG_TO_FILE": "Disables logging to file but does not surpress outputting logs to console, if specified.",
    }

    # # Class Container Metadata
    ARG_PLAIN_CONTAINER_NAME: Final[str] = "ArgsContainer"
    ARG_PLAIN_DOC_INFO: Final[
        str
    ] = "This is a plain class to where the args has been living after being evaluated."

    # # Discord Client
    DISCORD_DATA_CONTAINER : Final[str] = "DiscUserCtxContainer"
    DISCORD_DATA_CONTAINER_ATTRS: Final[
        dict[str, Any]
    ] = {  # todo: Fill it up later. +  Ref: https://stackoverflow.com/questions/3603502/prevent-creating-new-attributes-outside-init
        "__usr__": {},  # Contains user's information, this excludes the Discord Rich Presence.
        "__guild__": {},  # Contains guild information.
        "__presence__": {},  # Contains user's presence activity.
    }
    DISCORD_ON_READY_MSG: Final[
        str
    ] = "Client (%s) is ready for evaluation of user's activity presence."

    # # Discord Client

    DISCORD_CLIENT_INTENTS : Intents = Intents.none() # todo: Make this one finalized later.
    DISCORD_CLIENT_INTENTS.presences = True

    # # Identification of Return Codes
    RET_DOTENV_NOT_FOUND : Final[int] = -1


    # # Message of Return Codes


    # # Logger Information
    ROOT_LOCATION: Final[str] = "../"
    ENV_FILENAME : Final[str] = ".env"
    LOGGER_FILENAME: Final[str] = ROOT_LOCATION + strftime("%m%d%Y-%H%M-") + "discord-activity-badge.log"
    LOGGER_OUTPUT_FORMAT: Final[
        str
    ] = "[%(relativeCreated)d ms, %(levelname)s\t]\tin %(module)s.py:%(lineno)d -> %(message)s"

    # # Required Parameters @ ENV
    REQUIRED_PARAMS_IN_ENV: List[str] = [""]  # todo...

    # # Pre-Condition Constraints
    ALLOWABLE_TIME_TO_COMMIT: Final[object] = timeConstraint(
        minutes=30
    )  # todo: Clarify this. This is connected from the workflow recommended refresh rate. Also rate-limits.
