import time
import numpy as np
import cv2 
from flask import Flask, render_template, Response,url_for, request, redirect

app=Flask(__name__,static_url_path='/templates')

@app.route('/',methods=['GET', 'POST'])

#app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    cap = cv2.VideoCapture(0)

    currentFrame = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

    # Handles the mirroring of the current frame
        frame = cv2.flip(frame,1)

    # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Saves image of the current frame in jpg file
    # name = 'frame' + str(currentFrame) + '.jpg'
    # cv2.imwrite(name, frame)

    # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # To stop duplicate images
        currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()
   
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    #app.jinja_env.auto_reload=True
    app.run(host="192.168.0.106",debug=True)
    