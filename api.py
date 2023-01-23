from flask import Flask
from flask import render_template
import os
from flask import request
from werkzeug.utils import secure_filename

# for prediction
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
import keras
import numpy as np
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator
from keras_preprocessing.image import img_to_array
from keras_preprocessing.image import load_img
import pathlib


app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    model = load_model('model_version3.hdf5')
    if request.method == 'POST':
        image_file = request.files["image"]
        if image_file:
            UPLOAD_FOLDER = './static/client_ctscan'
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            file_name = generate_custom_name(image_file.filename)
            image_file.save(os.path.join(UPLOAD_FOLDER, file_name))
            img_path = "./static/client_ctscan/check_cancer.png"
            image_shape = (305,430,3)
            N_CLASSES = 4
            BATCH_SIZE = 1
            test_path="./static/test"
            test_datagen = ImageDataGenerator(dtype='float32', rescale = 1.0/255.0)
            test_generator = test_datagen.flow_from_directory(test_path,
                                                            batch_size = BATCH_SIZE,
                                                            target_size = (305,430),
                                                            class_mode = 'categorical')
            class_names=list(test_generator.class_indices.keys())
            img = load_img(img_path, target_size=(460, 460))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, 0)

            prediction = model.predict(img_array)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            image_location = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            return render_template("index.html", prediction= "This image most likely belongs to {} with a {:.2f} percent confidence."
                .format(class_names[np.argmax(prediction)], 100 * np.max(prediction)), image=image_location)

    return render_template("index.html", prediction="Please Upload your CT Scan Report Image")


def generate_custom_name(original_file_name):
    return "check_cancer" + pathlib.Path(original_file_name).suffix


if __name__ == "__main__":
    app.run(port=12000, debug=True)
