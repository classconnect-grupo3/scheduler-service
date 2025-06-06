import logging
import sys
from typing import Optional


# ANSI color codes
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RESET = "\033[0m"


class ColoredFormatter(logging.Formatter):
    """Custom formatter that adds colors to log messages based on level"""

    def format(self, record):
        # Save the original format
        original_format = self._style._fmt

        # Add color based on level
        if record.levelno >= logging.ERROR:
            color = Colors.RED
        elif record.levelno >= logging.INFO:
            color = Colors.GREEN
        else:  # DEBUG
            color = Colors.BLUE

        # Add color to the format
        self._style._fmt = f"{color}{original_format}{Colors.RESET}"

        # Format the record
        result = super().format(record)

        # Restore the original format
        self._style._fmt = original_format

        return result


class ImmediateFlushHandler(logging.StreamHandler):
    """Custom handler that flushes after each emit"""

    def emit(self, record):
        super().emit(record)
        self.flush()


def setup_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Configure and return a logger with the specified name.
    If no name is provided, returns the root logger.

    Args:
        name: Optional name for the logger. If None, returns root logger.

    Returns:
        logging.Logger: Configured logger instance
    """
    # Create formatter
    formatter = ColoredFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create console handler with immediate flush
    console_handler = ImmediateFlushHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Get logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Show all levels including DEBUG

    # Remove existing handlers to avoid duplicates
    logger.handlers = []

    # Add handler
    logger.addHandler(console_handler)

    return logger
