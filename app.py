from flask import Flask, request, render_template, jsonify
# from image_detection import detect_images_in_url  # assuming image detection function is stored in image_detection.py
from probability import *
from download import *
from detect_faces import *
from detect_gender import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_function', methods=['POST'])
def run_python_function():
    try:
        url = request.form['url']
        result = check_images(url)
        return jsonify(result=result)
    except Exception as e:
        print(e)
        return jsonify(result='Error: ' + str(e))

def check_images(url):
    print(url)
    try:
        image_path = url_to_image(url)
        probab = probability(image_path)
        gender = detect_gender(image_path)
        presence = detect_face(image_path)
        if presence:
            return f"There is {probab}% probability of presence of images on this page.\nThere is {gender}'s face present."
        else:
            return f"There is {probab}% probability of presence of images on this page.There is no face present."
    except Exception as e:
        print(e)
        return 'Error: ' + str(e)
# @app.route('/detect_faces', methods=['POST'])
# def detect_faces():
#     url = request.form['url']
#     image_path = url_to_image(url)
#     presence = detect_face(image_path)
#     if presence:
#         return f'There is face present.'
#     else:
#         return f'There is no face present.'


if __name__ == '__main__':
    app.run(debug=True)
