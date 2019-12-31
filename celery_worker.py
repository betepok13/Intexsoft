import os
from datetime import datetime

from celery import Celery
from celery.beat import Scheduler

from app import db
from app.models import Rate, Call

celery_app = Celery('tasks', broker='amqp://localhost//')
Scheduler.max_interval = 30


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(30, check_files_in_dir.s(), name='add every 30 sec')


@celery_app.task
def check_files_in_dir():
    list_files = os.listdir(os.path.abspath('files'))
    if list_files:

        rate_gsm_for_minute = Rate.query.filter_by(type_connect='GSM').first().price_per_minute
        rate_cdma_for_minute = Rate.query.filter_by(type_connect='CDMA').first().price_per_minute
        rate_lte_for_minute = Rate.query.filter_by(type_connect='LTE').first().price_per_minute

        for file in list_files:
            if file[-4:] == 'json':
                with open(os.path.abspath('files') + '/' + file) as file_handler:
                    line_list = file_handler.read().splitlines()
                    number_in, number_target, timestamp_start_call, timestamp_end_call, type_connect = line_list

                    dt_object_timestamp_start_call = datetime.fromtimestamp(float(timestamp_start_call))
                    dt_object_timestamp_end_call = datetime.fromtimestamp(float(timestamp_end_call))
                    count_minutes = (dt_object_timestamp_end_call - dt_object_timestamp_start_call).seconds / 60

                    if type_connect == 'GSM':
                        result_cost_call = count_minutes * rate_gsm_for_minute
                    elif type_connect == 'CDMA':
                        result_cost_call = count_minutes * rate_cdma_for_minute
                    elif type_connect == 'LTE':
                        result_cost_call = count_minutes * rate_lte_for_minute
                    else:
                        result_cost_call = 0

                    add_call = Call(number_in=number_in, number_target=number_target,
                                    timestamp_start_call=timestamp_start_call,
                                    timestamp_end_call=timestamp_end_call,
                                    cost_call=result_cost_call)

                    db.session.add(add_call)
                    db.session.commit()

                os.remove(os.path.abspath('files') + '/' + file)
