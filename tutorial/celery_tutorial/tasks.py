from celery import Celery
from celery import shared_task
#app = Celery('tasks', broker='amqp://localhost:5462')

app = Celery('tasks', broker='amqp://localhost//')

#@app.task
@shared_task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)