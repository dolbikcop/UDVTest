import time
import schedule

from ssh_data import collect_data


def main():
    schedule.every(10).seconds.do(collect_data)
    # Включение регулярных задач
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
