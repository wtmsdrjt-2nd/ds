# ds < https://t.me/kastaid >
# Copyright (C) 2023-present kastaid
#
# This file is a part of < https://github.com/kastaid/ds/ >
# Please read the MIT License in
# < https://github.com/kastaid/ds/blob/main/LICENSE/ >.

import os
import sys
from typing import Union, List
from ds import PROJECT, Root


def time_formatter(ms: Union[int, float]) -> str:
    minutes, seconds = divmod(int(ms / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    time_units = (
        f"{weeks}w, " if weeks else "",
        f"{days}d, " if days else "",
        f"{hours}h, " if hours else "",
        f"{minutes}m, " if minutes else "",
        f"{seconds}s, " if seconds else "",
    )
    return "".join(time_units)[:-2] or "0s"


def get_terminal_logs() -> List[str]:
    return sorted(map(str, (Root / "logs").rglob("*.log")))


def restart() -> None:
    os.system("clear")
    try:
        import psutil

        proc = psutil.Process(os.getpid())
        for p in proc.open_files() + proc.connections():
            os.close(p.fd)
    except BaseException:
        pass
    reqs = Root / "requirements.txt"
    os.system(f"{sys.executable} -m pip install --disable-pip-version-check --default-timeout=100 -U -r {reqs}")
    os.execl(sys.executable, sys.executable, "-m", PROJECT)
