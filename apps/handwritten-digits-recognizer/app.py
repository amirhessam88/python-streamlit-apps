# Amirhessam Tahmassebi
# March-27-2021
# Handwritten Digits Recognizer

# loading libraries
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.models import load_model


# handling warnings
st.set_option("deprecation.showPyplotGlobalUse", False)

# title
st.markdown(
    "<h1 style='text-align: center; color: black;'>Handwritten Digits Recognizer</h1>",
    unsafe_allow_html=True,
)

HEADER_PATH = "apps/handwritten-digits-recognizer/assets/header.png"
st.image(HEADER_PATH, use_column_width=True)

# model types
model_type = st.selectbox("Choose Model", ("DNN", "CNN"))


# load trained model
def get_model(model_type):
    """
    Returns trained model
    """
    if model_type == "DNN":
        MODEL_PATH = "apps/handwritten-digits-recognizer/assets/model_dnn.h5"
    else:
        MODEL_PATH = "apps/handwritten-digits-recognizer/assets/model_cnn.h5"

    model = load_model(MODEL_PATH)

    return model


model = get_model(model_type)


def plot_model(model_type):
    """
    Plots model perf
    """
    if model_type == "DNN":
        PERF_PATH = "apps/handwritten-digits-recognizer/assets/performance_dnn.png"
        PARAMS_PATH = "apps/handwritten-digits-recognizer/assets/params_dnn.png"
    else:
        PERF_PATH = "apps/handwritten-digits-recognizer/assets/performance_cnn.png"
        PARAMS_PATH = "apps/handwritten-digits-recognizer/assets/params_cnn.png"

    st.write("Model Structure")
    st.image(PARAMS_PATH)

    st.write("Model Performance")
    st.image(PERF_PATH, use_column_width=True)


st.success(f"{model_type} is now loaded!")
plot_model(model_type)

st.header("Draw Your Digit")
SIZE = 192
canvas_result = st_canvas(
    fill_color="#000000",
    stroke_width=20,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=SIZE,
    height=SIZE,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))
    img = img.resize((28, 28))
    interpolated_img = img.resize((SIZE, SIZE), resample=Image.NEAREST)
    st.write("Model Input")
    st.image(interpolated_img)

if st.button("Predict"):

    if model_type == "DNN":
        X_test = img.convert(mode="L")
        y_pred_proba = model.predict(np.asarray(X_test).reshape(1, 28, 28))
        st.write(f"result: {np.argmax(y_pred_proba[0])}")
        st.bar_chart(pd.DataFrame({"Prediction": y_pred_proba[0]}))

    else:
        X_test = img.convert(mode="L")
        y_pred_proba = model.predict(np.asarray(X_test).reshape(1, 28, 28, 1))
        st.write(f"result: {np.argmax(y_pred_proba[0])}")
        st.bar_chart(pd.DataFrame({"Prediction": y_pred_proba[0]}))
