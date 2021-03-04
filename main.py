from util.Uiautomator2Util import DingTalk
from apscheduler.schedulers.blocking import BlockingScheduler


def punch_in():
    DingTalk.dingtalk()


def punch_out():
    DingTalk.dingtalk()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(punch_in, 'cron', hour=8, minute=50)
    scheduler.add_job(punch_out, 'cron', hour=21, minute=25)
    scheduler.start()
