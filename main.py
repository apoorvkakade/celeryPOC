from .scheduler import celery_obj
from flask import Flask
app = Flask(__name__)

@app.route('/send_task')
def fun():
    task_id = celery_obj.send_task('create_task', [1, 2])
    return str(task_id)