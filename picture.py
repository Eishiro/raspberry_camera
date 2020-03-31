from flask import Flask, render_template, send_file
from datetime import datetime
from time import sleep
from picamera import PiCamera

app = Flask(__name__)


@app.route('/')
def index():
    return 'there will be a picture in here'

@app.route('/takepicture')
def picture():

    try:
        #taking a picture
        camera = PiCamera()
        camera.resolution = (640,480)
        camera.start_preview()
        sleep(1)
        pic_name = datetime.now().strftime('%Y%m%d_%H%M%S') + '.jpg'
        camera.capture(pic_name)
        camera.close()
       # return render_template('index.html', pic_name =pic_name)
        return send_file(pic_name, mimetype = 'image/jpg')

    except:
        return 'there was an issue in takking picture'

@app.route('/getpicture')
def get_image():
    file_name = 'sample.jpg'
    return send_file(file_name, mimetype='image/jpg')

if __name__ == "__main__":
    app.run(debug = True)
