import loguru

# логи на обработку исключений
error_logger = loguru.logger
error_logger.add('./results/error.log', level='ERROR', format='{time} {message} \n\n')

# логи на информирование
info_logger = loguru.logger
info_logger.add('./results/info.log', level='SUCCESS', format='{time} {message}')

