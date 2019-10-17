import cv2
import numpy as np
from app import app
from flask import render_template, Response


def video_generator():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imwrite('t.jpg', frame)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')


@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

@app.route("/stream/")
def video_stream():

    return Response(video_generator(),
            mimetype='multipart/x-mixed-replace; boundary=frame')