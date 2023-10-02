import logging
import os
import time

class TimestampedRotatingLogger:
    def __init__(
        self,
        log_directory="log",
        log_level=logging.INFO,
        log_format="%(asctime)s - %(levelname)s - %(message)s",
        max_log_size_bytes=1048576,  # 1 MB by default
        create_if_not_exists=True
    ):
        self.log_directory = log_directory
        self.log_level = log_level
        self.log_format = log_format
        self.max_log_size_bytes = max_log_size_bytes
        self.create_if_not_exists = create_if_not_exists

        self.logger = self._create_logger()

    def _create_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        log_filename = self._get_timestamped_log_filename()
        file_handler = logging.FileHandler(log_filename, mode="a")
        formatter = logging.Formatter(self.log_format)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    def _get_timestamped_log_filename(self):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = os.path.join(self.log_directory, f"log_{timestamp}.log")

        if not os.path.exists("log/"):
            os.makedirs("log/")

        if not os.path.exists(log_filename) and self.create_if_not_exists:
            open(log_filename, 'a').close()

        return log_filename

    def rotate_logs(self):
        current_log_filename = self.logger.handlers[0].baseFilename
        if os.path.getsize(current_log_filename) > self.max_log_size_bytes:
            # Rename the current log file using the timestamp
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            new_log_filename = os.path.join(self.log_directory, f"log_{timestamp}.log")
            os.rename(current_log_filename, new_log_filename)

            # Create a new log file
            open(current_log_filename, 'a').close()

            self.logger.removeHandler(self.logger.handlers[0])
            new_file_handler = logging.FileHandler(current_log_filename, mode="a")
            formatter = logging.Formatter(self.log_format)
            new_file_handler.setFormatter(formatter)
            self.logger.addHandler(new_file_handler)
    
    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)