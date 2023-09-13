from celery import Celery
from datetime import datetime
import json

BROKER = "amqp://guest:guest@localhost:5672/"

celery_obj = Celery('worker', broker=BROKER)

celery_obj.conf.task_routes = {
    'worker.create_task': {'queue': 'create_task'}
}

@celery_obj.task(bind=True, queue="create_task", name="create_task")
def create_task(self, a,b):
    print(f"Time: {datetime.now()} {a+b}")