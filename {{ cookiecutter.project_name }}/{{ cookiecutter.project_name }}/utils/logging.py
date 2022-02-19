import logging

from colorama import Back, Fore, init

init(autoreset=True)


class ColorFormatter(logging.Formatter):
    BACK_COLORS = {
        "WARNING": Fore.BLACK + Back.YELLOW,
        "ERROR": Fore.BLACK + Back.RED,
        "DEBUG": Fore.BLACK + Back.GREEN,
        "INFO": Fore.BLACK + Back.BLUE,
        "CRITICAL": Fore.BLACK + Back.RED
    }

    FORE_COLORS = {
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "DEBUG": Fore.GREEN,
        "INFO": Fore.BLUE,
        "CRITICAL": Fore.RED
    }

    to_file = False

    def set_file(self, value):
        self.to_file = value

    def format(self, record):
        if not self.to_file:
            b_color = self.BACK_COLORS.get(record.levelname, "")
            f_color = self.FORE_COLORS.get(record.levelname, "")
            if b_color and f_color:
                record.levelname = b_color + record.levelname + Back.RESET + Fore.RESET
                record.msg = f_color + record.msg + Fore.RESET
        return logging.Formatter.format(self, record)


def get_logger(
        name: str,
        level: int = logging.WARNING,
        colored: bool = True,
        file: str = "",
        **kwargs) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = None
    if file:
        colored = False
        handler = logging.FileHandler(
            filename=file,
            mode=kwargs.get("mode", "a")
        )
        formatter = logging.Formatter("%(asctime)s | %(processName)s | %(pathname)s | %(lineno)d | [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)

    if colored:
        color_formatter = ColorFormatter("[%(levelname)s] %(message)s")
        color_formatter.set_file(True if file else False)
        if not handler:
            handler = logging.StreamHandler()
        handler.setFormatter(color_formatter)

    if handler:
        logger.addHandler(handler)
    return logger

