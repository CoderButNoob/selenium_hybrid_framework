# import logging
# import os
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\orangeHRMapp\\logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m%d%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
# customLogger.py
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Get the absolute path to the logs directory
        log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
        log_dir = os.path.abspath(log_dir)

        # Ensure the logs directory exists
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, 'automation.log')

        # Create logger
        logger = logging.getLogger("orangeHRMLogger")
        logger.setLevel(logging.INFO)

        # Avoid duplicate handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger


