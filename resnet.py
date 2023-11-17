# load_model_sample.py
from keras.models import load_model
import keras.utils as image
import matplotlib.pyplot as plt
import numpy as np
import os


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor


if __name__ == "__main__":

    model = load_model("C:/Users/windows.10/Desktop/ResNet50_ISIC_2019.h5")

    img_path = 'C:/Users/windows.10/Desktop/1.jpg'   
   

    # load a single image
    new_image = load_image(img_path)

    # check prediction
    pred = model.predict(new_image)