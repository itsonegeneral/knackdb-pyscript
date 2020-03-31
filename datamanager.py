import pyrebase
from datetime import datetime
import time

config = {
  "apiKey": "AIzaSyBQrLQYglhDTJ4LgNBKWfphbdrvyWjRViY",
  "authDomain": "knacktestmodule.firebaseapp.com",
  "databaseURL": "https://knacktestmodule.firebaseio.com/",
  "storageBucket": "knacktestmodule.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
datetime.now()
time_format = '%Y-%m-%d %H:%M:%S'


def upload_data(time_stamp):
    data = {
        "name": "rithik",
        "time": time_stamp
    }
    db.child('python').child(db.generate_key()).set(data)

def database_check():
    print('\nStarting Database Inspect')
    data = db.child('python').get()
    try:
        for user in data.each():
            k = user.val()
            data_time_stamp = datetime.strptime(k['time'],time_format)
            time_string = datetime.now().strftime(time_format);
            current_time_stamp = datetime.strptime(str(time_string),time_format)
            time_difference = current_time_stamp - data_time_stamp
            if(time_difference.seconds>600):
                print('Post older than 10 minute found deleting post id ' + user.key())
                db.child('python').child(user.key()).remove()
    except:
        print('No data found')        


while True:
    database_check()
    time.sleep(10)

def start_upload_process():
    x=0
    for x in range(100):
        print('Uploaded data with timestamp' + str(datetime.now()))
        upload_data(str(datetime.now().strftime(time_format)))
        time.sleep(2)
