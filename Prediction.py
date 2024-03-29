import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA 
import numpy as np
import cv2
import pickle as pk
from PIL import Image 

loaded_model = pk.load(open('model_final.sav', 'rb'))

st.header("Wavelength Prediction Application")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png','jpeg'])
if uploaded_file is not None:
    imagedisplay = Image.open(uploaded_file)
    st.image(imagedisplay, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    
    image = Image.open(uploaded_file)
 
    image = image.resize((70,70))
    image = np.array(image)
    image = image.reshape(1,14700)
    image = image/255.0

    pca_reload = pk.load(open("pca_final.pkl",'rb'))
    img_pca=pca_reload.transform(image)
    
    y_pred = loaded_model.predict(img_pca)
    st.write("Loading result...")
    st.write("Prediction: ",y_pred[0])
    
    ###print("Real label:", image_name)
    
