## Flask and Twilio includes and setup
from flask import Flask
from twilio.rest import Client

#### ADD YOUR TWILIO SECRETS HERE
account_sid = 'SECRET' 
auth_token = 'SECRET' 
client = Client(account_sid, auth_token)

from_number = '+12021111111' # put your twilio number here'
to_number = '+15101111111' # put your own phone number here


## Celery includes
from celery import Celery
from time import sleep
from datetime import datetime, timedelta

#### ADD YOUR CELERY BROKER HERE
# I enabled the Heroku add-on called cloudAMQP to use rabbitMQ as my broker
# Go to your heroku project Dashboard to find add ons.
# enable cloudAMPQ, then click on the info link to get the URL and paste it here.
app = Celery('tasks', broker='amqps://YOUR_STUFF_HERE')


# This will one ONCE in the future.
@app.task()
def hello():
    message = client.messages.create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_=from_number,
         to=to_number
     )
    return 'hello world'

in_a_minute = datetime.utcnow() + timedelta(minutes=1)
hello.apply_async(eta=in_a_minute)


# This will run at regular intervals.
@app.task
def check():
    print("I am checking your stuff")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    message = client.messages.create(
         body='Sent at '+dt_string,
         from_=from_number,
         to=to_number
    )
    return "check completed"

app.conf.beat_schedule = {
    "run-me-every-thirty-seconds": {
    "task": "tasks.check",
    "schedule": 30.0
     }
}



print("done")


# to start:
# heroku ps:scale worker=1
# heroku ps:scale beat=1

# to stop:
# heroku ps:scale worker=0
# heroku ps:scale beat=0
