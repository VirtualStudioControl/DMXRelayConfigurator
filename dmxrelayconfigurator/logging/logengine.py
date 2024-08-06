import logging
from logging import Logger
import sys

from typing import Dict, Optional


LOG_FORMAT_CONSOLE = '\033[96m[%(asctime)s]\033[91m[%(levelname)s]\033[0m %(message)s\033[94m at \033[93m%(pathname)s, \033[94mline \033[93m%(lineno)d, \033[94mFunction:\033[92m %(funcName)s \033[0m'
LOG_FORMAT = '[%(asctime)s][%(levelname)s] %(message)s at %(pathname)s, line %(lineno)d, Function: %(funcName)s'
LOG_TO_CONSOLE = True
LOG_TO_FILE = True
LOG_FILE = "virtualstudio.log"

LOG_LEVEL = logging.WARNING


def getLogger(name=None, level=None, isVerbose=False) -> Logger:
    if level is None:
        if isVerbose:
            log_level = logging.DEBUG
        else:
            log_level = LOG_LEVEL
    else:
        log_level = level

    log_format = logging.Formatter(LOG_FORMAT)
    log = logging.getLogger(name)
    log.setLevel(log_level)

    if not log.hasHandlers():
        if LOG_TO_FILE:
            # Writing to log file
            handler = logging.FileHandler(LOG_FILE)
            handler.setLevel(log_level)
            handler.setFormatter(log_format)
            log.addHandler(handler)

        if LOG_TO_CONSOLE:
            log_format_console = logging.Formatter(LOG_FORMAT_CONSOLE)
            # writing to stdout
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(log_level)
            handler.setFormatter(log_format_console)
            log.addHandler(handler)

    return log
