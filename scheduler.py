from celery import Celery

BROKER = "pyamqp://guest:guest@localhost:5672/"

# scheduler is name of the celery_obj
celery_obj = Celery('scheduler', broker=BROKER)

# Declare the queue
celery_obj.conf.task_routes = {
    "scheduler.create_task": {'queue': 'create_task'}
}

@celery_obj.task(bind=True, queue='create_task', name='create_task')
def create_task(self, a, b):
    pass
