"""
This module will be used to log messages at agent side
the agent here is camrelaykar

"""
import logging
import logging.config
import logging.handlers


class BotLog(object):

    def __init__(self, log_file, logger_name, log_handler):
        self.log_file = log_file
        self.logger_name = logger_name
        self.log_handler = log_handler

    def main(self):
        self.config_initial = {
            'version': 1,
            'formatters': {
                'detailed': {
                    'class': 'logging.Formatter',
                    #'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
                    'format': '%(asctime)s - %(threadName)s:%(thread)d - %(levelname)s - %(name)s:%(module)s - %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'INFO',
                },
                'file': {
                    'class': 'logging.FileHandler',
                    'filename': self.log_file,
                    'mode': 'a',
                    'formatter': 'detailed',
                },
            },
            'loggers': {
                'root': {
                    'level': 'DEBUG',
                    'handlers': ['console']
                },
                self.logger_name: {
                    'level': 'DEBUG',
                    'handlers': ['file']
                },
            }
        }
        return self.config_initial
        # The worker process configuration is just a QueueHandler attached to the

    def get_logger(self):
        logging.config.dictConfig(BotLog.main(self))

        logger = logging.getLogger(self.logger_name)

        # logger.info("Program started")

        # result = otherMod2.add(7, 8)
        # logger.info("Done!")
        return logger

