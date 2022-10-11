import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA 
import numpy as np
import cv2
import pickle as pk
from PIL import Image 

loaded_model = pk.load(open('final_model.sav', 'rb'))
def prediction(image_name):
    img_list = list()
    image = cv2.imread(image_name)
    image = cv2.resize(image, (70, 70))
    image = image/255.0
    img_list.append(image)
    img = np.asarray(img_list)
    img = img.reshape(img.shape[0],img.shape[1]*img.shape[1]*img.shape[3])
    pca_reload = pk.load(open("pca.pkl",'rb'))
    img_pca=pca_reload.transform(img)
    y_pred = loaded_model.predict(img_pca)
    print("Prediction: {}".format(y_pred))
    print("Real label:", image_name)

st.header("Wavelength Prediction Application")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.write(image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = prediction(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))
