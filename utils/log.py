import logging
from logging.handlers import RotatingFileHandler


class RotatingLogger:
    def __init__(
        self,
        log_filename,
        log_level=logging.INFO,
        log_format="%(asctime)s - %(levelname)s - %(message)s",
        max_log_size_bytes=1048576,
        backup_count=3,
    ):
        self.log_filename = log_filename
        self.log_level = log_level
        self.log_format = log_format
        self.max_log_size_bytes = max_log_size_bytes
        self.backup_count = backup_count

        self.logger = self._create_logger()

    def _create_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        rotating_handler = RotatingFileHandler(
            self.log_filename,
            mode="a",
            maxBytes=self.max_log_size_bytes,
            backupCount=self.backup_count,
        )

        formatter = logging.Formatter(self.log_format)
        rotating_handler.setFormatter(formatter)

        logger.addHandler(rotating_handler)
        return logger

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
