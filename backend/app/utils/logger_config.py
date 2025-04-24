import logging

def setup_logger(name=__name__):
    logger = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

    