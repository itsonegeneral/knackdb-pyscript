import pyrebase
from datetime import datetime
from datetime import timedelta
import time

config = {
  "apiKey": "AIzaSyBAB3_BSepybVEPVR-PNcHxGC9aVOqT3uk",
  "authDomain": "knack-quiz-b57d5.firebaseapp.com",
  "databaseURL": "https://knack-quiz-b57d5.firebaseio.com/",
  "storageBucket": "knack-quiz-b57d5.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
time_format = '%c'
print(datetime.now().strftime(time_format))

def database_check():
    print('\nStarting Database Inspect')
    data = db.child('online_players').get()
    for contest in data.each():
        k = contest.val()
        start_time_db = datetime.strptime(k['lastOnline'],time_format)
        current_time = datetime.now().strftime(time_format)
        parsed = datetime.strptime(current_time,time_format)
        time_difference = parsed - start_time_db
        print(time_difference.seconds)
        if(time_difference.seconds>30):
            print('User older than 30 Second found deleting id ' + contest.key())
            db.child('online_players').child(contest.key()).remove() 

while True:
    database_check()
    time.sleep(5)


