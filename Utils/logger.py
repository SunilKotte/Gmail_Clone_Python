import logging

def setup_logger():
    """
    Setup a logger to log application events to a file.
    """
    logger = logging.getLogger("gmail_clone")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("app.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
