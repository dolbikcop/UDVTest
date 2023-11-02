import io

import loggers


@loggers.error_logger.catch
def write_report(**kwargs):
    with io.open("./static/template.html", mode="r", encoding="utf-8") as f:
        file = f.read().format_map(kwargs)
        loggers.info_logger.info(file)
        io.open("./results/report.html", mode="w").write(file)
        f.close()
