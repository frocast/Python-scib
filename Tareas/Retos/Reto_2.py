from flask import Flask, make_response
import datetime
app = Flask(__name__)

@app.route('/time')
def time():
    #now = datetime.datetime.now('%Y-%m-%d')
    now = datetime.datetime.now()
    time = ("%s:%s:%s" % (now.hour, now.minute, now.second))
    return "La hora actual es: " + time

if __name__ == "__main__":
    app.run()