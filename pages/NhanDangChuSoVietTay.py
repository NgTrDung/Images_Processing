import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models, optimizers

# Suppress TensorFlow INFO and WARNING logs
tf.get_logger().setLevel('ERROR')

# Load model
model_architecture = r"C:/Users/dung8/Downloads/Giai-Nen/Image-Processing-Project/ModelNhanDangChuSoVietTay/digit_config.json"
model_weights = r"C:/Users/dung8/Downloads/Giai-Nen/Image-Processing-Project/ModelNhanDangChuSoVietTay/digit.weights.h5"
model = models.model_from_json(open(model_architecture).read())
model.load_weights(model_weights)
OPTIMIZER = tf.keras.optimizers.Adam()

model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,
              metrics=["accuracy"])

# Load MNIST data
(_, _), (X_test, _) = datasets.mnist.load_data()

# Custom CSS styles
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://t4.ftcdn.net/jpg/04/94/85/25/360_F_494852538_r8ylVApdAY0YuWYCkWIsg5pDZkboERYI.jpg");
    background-size: 100% 100%;
}

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

[data-testid="stForm"]{
    background-color: #77777745;
    backdrop-filter: blur(20px);
}

.st-emotion-cache-lrlib{
    padding-top: 44px;
}

[data-testid="stSidebar"] {
    background-color: #77777745;
    border-radius: 10px;
    margin-top: 115px;
    margin-left: 58px;
    backdrop-filter: blur(10px);
}

.header{
    background-color: rgba(113, 104, 119, 0.1);
    padding: 20px;
    border-radius: 6px;
    box-shadow: 17px 11px 53px -48px rgba(147, 0, 255, 0.45);
    backdrop-filter: blur(20px);
}

.header img{
    width: 100%;
    height: 250px;
    border-radius: 4px;
    box-shadow: 17px 11px 118px -38px rgba(147, 0, 255, 0.45);
    object-fit: cover;
}

.header-title{
    font-size: 44px;
    font-weight: 700;
    text-align: center;
    margin-top: 18px;
}

.header-malop{
    font-size: 32px;
    font-weight: 700;
    text-align: center;
}

.st-emotion-cache-1hdbmx1{
    border: 1px solid #fff;
}

.st-emotion-cache-1hgxyac{
    background-color: #fff;
}

.st-emotion-cache-1hgxyac svg{
    fill: #333;
}

.st-emotion-cache-1hgxyac:hover:enabled, .st-emotion-cache-1hgxyac:focus:enabled{
        background-color: rgb(242 242 242);
}

[data-testid="baseButton-secondaryFormSubmit"]{
    width: 100px;
    background-color: #ffffff33;
}

.st-emotion-cache-19rxjzo .ef3psqc6{
    float:right;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the Streamlit app
st.title("NHẬN DIỆN CHỮ VIẾT TAY")

# Button to trigger image generation and display
if st.button("Generate Images and Predictions"):
    # Sample some images for demonstration
    n_sample = 100
    index = np.random.randint(0, 9999, n_sample)
    sample = np.zeros((n_sample, 28, 28), np.uint8)

    for i in range(n_sample):
        sample[i] = X_test[index[i]]

    # Prepare images for display
    image = np.zeros((10*28, 10*28), np.uint8)
    k = 0
    for i in range(10):
        for j in range(10):
            image[i*28:(i+1)*28, j*28:(j+1)*28] = sample[k]
            k += 1

    # Normalize images for prediction
    sample = sample / 255.0
    sample = sample.astype('float32')
    sample = np.expand_dims(sample, axis=3)

    # Predict digits
    ket_qua = model.predict(sample, verbose=0)

    # Extract predicted digits
    chu_so = [np.argmax(ket_qua[i]) for i in range(n_sample)]

    # Display predicted digits in a grid
    st.image(image, caption='Sample MNIST Images', use_column_width=True)

    k = 0
    for i in range(10):
        row_text = ""
        for j in range(10):
            row_text += str(chu_so[k]) + " "
            k += 1
        st.write(row_text)
