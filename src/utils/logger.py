import logging

def get_logger(name: str = None):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | line %(lineno)d | %(message)s"
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
