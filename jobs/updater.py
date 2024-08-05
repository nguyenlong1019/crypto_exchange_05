from datetime import datetime 
from apscheduler.schedulers.background import BackgroundScheduler 
from .tasks import * 


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_coin_price_vnd, 'interval', seconds=15)
    scheduler.start()
