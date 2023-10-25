import paramiko
from paramiko.ssh_exception import SSHException

from config import HOST, PORT, USERNAME, PASSWORD
from loggers import error_logger, info_logger

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


@error_logger.catch
def collect_data():
    # try:
        # Подключение к коммутатору
    client.connect(HOST, PORT, USERNAME, PASSWORD)
    # except SSHException as e:
    #     error_logger.error(e)
    #     info_logger.info('Сбой подключения')
    #     return

    # Сбор данных
    version = execute_command(client, 'show version')
    start_config = execute_command(client, 'show startup-config')
    current_config = execute_command(client, 'show running-config')
    acls = execute_command(client, 'show access-lists')
    interfaces = execute_command(client, 'show interfaces')

    # Закрытие подключения
    client.close()

    info = f'Версия коммутатора:\n{version}\n' \
           f"Стартовая конфигурация коммутатора:\n{start_config}\n" \
           f"Текущая конфигурация коммутатора:\n{current_config}\n" \
           f'Сведения о списках контроля доступа (ACL) коммутатора:\n{acls}\n' \
           f'Сведения об интерфейсах коммутатора:\n{interfaces}\n'

    # Сохранение данных в логи
    info_logger.info(info)


def execute_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    return output


collect_data()
