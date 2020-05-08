from werkzeug.utils import secure_filename
import joblib
from flask import Flask, request, render_template
import cv2
import numpy as np

# Define a flask app
app = Flask(__name__)


def process_eval(imk):
    output1 = cv2.resize(imk, (30,30))
    output1 = output1.astype('float')
    output1 /= 255.0
    print(type(output1))
    output1 = np.array(output1).reshape(-1, 30, 30, 3)
    classifer = joblib.load("model.pk2")
    x = classifer.predict_classes(output1[[0], :])
    if x[0] == 0:
        result = "Speed limit (20km/h)"
    elif x[0] == 1:
        result = "Speed limit (30km/h)"
    elif x[0] == 2:
        result = "Speed limit (50km/h)"
    elif x[0] == 3:
        result = "Speed limit (60km/h)"
    elif x[0] == 4:
        result = "Speed limit (70km/h)"
    elif x[0] == 5:
        result = "Speed limit (80km/h)"
    elif x[0] == 6:
        result = "End of speed limit (80km/h)"
    elif x[0] == 7:
        result = "Speed limit (100km/h)"
    elif x[0] == 8:
        result = "Speed limit (120km/h)"
    elif x[0] == 9:
        result = "No passing"
    elif x[0] == 10:
        result = "No passing veh over 3.5 tons"
    elif x[0] == 11:
        result = "Right-of-way at intersection"
    elif x[0] == 12:
        result = "Priority road"
    elif x[0] == 13:
        result = "Yield"
    elif x[0] == 14:
        result = "Stop"
    elif x[0] == 15:
        result = "No vehicles"
    elif x[0] == 16:
        result = "Veh > 3.5 tons prohibited"
    elif x[0] == 17:
        result = "No entry"
    elif x[0] == 18:
        result = "General caution"
    elif x[0] == 19:
        result = "Dangerous curve left"
    elif x[0] == 20:
        result = "Dangerous curve right"
    elif x[0] == 21:
        result = "Double curve"
    elif x[0] == 22:
        result = "Bumpy road"
    elif x[0] == 23:
        result = "Slippery road"
    elif x[0] == 24:
        result = "Road narrows on the right"
    elif x[0] == 25:
        result = "Road work"
    elif x[0] == 26:
        result = "Traffic signals"
    elif x[0] == 27:
        result = "Pedestrians"
    elif x[0] == 28:
        result = "Children crossing"
    elif x[0] == 29:
        result = "Bicycles crossing"
    elif x[0] == 30:
        result = "Beware of ice/snow"
    elif x[0] == 31:
        result = "Wild animals crossing"
    elif x[0] == 32:
        result = "End speed + passing limits"
    elif x[0] == 33:
        result = "Turn right ahead"
    elif x[0] == 34:
        result = "Turn left ahead"
    elif x[0] == 35:
        result = "Ahead only"
    elif x[0] == 36:
        result = "Go straight or right"
    elif x[0] == 37:
        result = "Go straight or left"
    elif x[0] == 38:
        result = "Keep right"
    elif x[0] == 39:
        result = "Keep left"
    elif x[0] == 40:
        result = "Roundabout mandatory"
    elif x[0] == 41:
        result = "End of no passing"
    else:
        result = "End no passing veh > 3.5 tons"
    return result

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("bird.jpg"))
        im=cv2.imread("bird.jpg")
        result=process_eval(im)
        return render_template('index.html',result=result)

if __name__ == "__main__":
    app.run()