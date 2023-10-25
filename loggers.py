import loguru

info_logger = loguru.logger
info_logger.add('results/info.log', format='{time} {message}')

error_logger = loguru.logger
error_logger.add('results/error.log', level='ERROR', format='{time} {message} \n\n')
