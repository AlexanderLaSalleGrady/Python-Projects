import logging


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    get_logger = logging.getLogger(logger_name)
    log_format = logging.Formatter('[ %(asctime)s ] [ %(levelname)-5s ] %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(log_format)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(log_format)

    get_logger.setLevel(level)
    get_logger.addHandler(fileHandler)
    get_logger.addHandler(streamHandler)


setup_logger('serviceLog', r'..\logs\service.log')
serviceLog = logging.getLogger('serviceLog')