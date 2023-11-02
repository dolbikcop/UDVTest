import paramiko

from config import HOST, PORT, USERNAME, PASSWORD
from loggers import error_logger, info_logger
from report_writer import write_report

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


@error_logger.catch
def collect_data():
    try:
        # Подключение к коммутатору
        client.connect(HOST, PORT, USERNAME, PASSWORD)
    except Exception as e:
        error_logger.error(e)
        info_logger.info('Сбой подключения')
        return

    # Сбор данных
    version = execute_command(client, 'show version')
    start_config = execute_command(client, 'show startup-config')
    current_config = execute_command(client, 'show running-config')
    acls = execute_command(client, 'show access-lists')
    interfaces = execute_command(client, 'show interfaces')

    # Закрытие подключения
    client.close()

    # Сохранение данных в html-отчет
    write_report(version=version,
                 start_config=start_config,
                 current_config=current_config,
                 acls=acls,
                 interfaces=interfaces)


def execute_command(ssh, command):  # Обработка команд
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')
    return output
