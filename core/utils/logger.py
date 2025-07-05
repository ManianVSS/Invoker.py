import logging
import os
import time

# Create a logger
logger = logging.getLogger('invoker_logger')
logger.setLevel(logging.DEBUG)

# Create a formatter to define the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

os.makedirs("logs", exist_ok=True)
# Create a file handler to write logs to a file
file_name = 'logs/InvokerRun{}.log'.format(time.strftime("%Y_%m_%d-%H_%M_%S"))
file_handler = logging.FileHandler(file_name)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create a stream handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # You can set the desired log level for console output
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def gui_debug(message: str, gui=None):
    """
    Log a debug message and optionally emit it to a GUI console.
    """
    logger.debug(message)
    if gui:
        gui.consoleTextBox.emit(message)


def gui_info(message: str, gui=None):
    """
    Log an info message and optionally emit it to a GUI console.
    """
    logger.info(message)
    if gui:
        gui.consoleTextBox.emit(message)
