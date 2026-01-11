import sys
from loguru import logger

logger.remove()  # Remove the default logger
logger.add(sys.stdout, level="WARNING")  # Add a new logger with WARNING level (logging will only be performed at warning level and higher)
logger.add("my_log.log", level="DEBUG", rotation="100 MB") # Saving debug logging to file my_log.log

logger.info("This is an info message")
logger.debug("Check whether this script performs any logging...")
logger.warning("This script does not train any CNN!")
logger.error("No training parsed!")
logger.critical("Early stopping cannot be applied.")