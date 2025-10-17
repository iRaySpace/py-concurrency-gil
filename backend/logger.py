import logging
import time


class UTCFormatter(logging.Formatter):
    converter = time.gmtime
    def formatTime(self, record, datefmt=None):
        ct = time.gmtime(record.created)
        return time.strftime(datefmt, ct) if datefmt else time.strftime("%Y-%m-%d %H:%M:%S", ct)


def init_logger():
    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "utc": {
                "()": UTCFormatter,
                "fmt": "%(asctime)s [PID %(process)d] [%(threadName)s] %(levelname)s  %(message)s"
            }
        },
        "handlers": {
            "default": {
                "formatter": "utc",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "formatter": "utc",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "_fastapi.txt",
                "maxBytes": 10_000_000, # 10 MB
                "backupCount": 5,
                "encoding": "utf8",
            },
        },
        "loggers": {
            "uvicorn": {"handlers": ["default", "file"], "level": "INFO", "propagate": False},
            "uvicorn.error": {"handlers": ["default", "file"], "level": "INFO", "propagate": False},
            "uvicorn.access": {"handlers": ["default", "file"], "level": "INFO", "propagate": False},
            "fastapi": {"handlers": ["default", "file"], "level": "INFO", "propagate": False},
        },
    }
    logging.config.dictConfig(LOGGING_CONFIG)


def get_logger():
    return logging.getLogger("fastapi")
