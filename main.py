import numpy as np
import pandas as pd

from util.excelUtil import ExcelUtil
from util.OsUtil import OsUtil
from util.ZhongHuaUtil import ZhongHuaUtil
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


def tick2():
    print('Tick2! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour=16, minute=55)
    scheduler.add_job(tick2, 'cron', hour=16, minute=57)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
