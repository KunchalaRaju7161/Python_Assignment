import inspect
import logging


class LogDetails:
    @staticmethod
    def getLogger(file_path):
        # Get the name of the calling function from the stack
        logger_name = inspect.stack()[1][3]

        # Create a logger object with the name of the calling function
        logger = logging.getLogger(logger_name)

        # Create a file handler to log message to the specified file
        file_handler = logging.FileHandler(file_path)

        # Define a formatter for the log messages
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

        # Set the formatter for the file handler
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Set the log level for the logger to DEBUG, so it will log all messages
        logger.setLevel(logging.DEBUG)

        # Return the configured logger object
        return logger


