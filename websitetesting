import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
import numpy as np

st.header("Fish Weight Prediction App")
st.text_input("Enter your Name: ", key="name")

st.subheader("Please select relevant features of your fish!")


input_Length1 = st.slider('Vertical length(cm)', 0.0, 100.0, 1.0)
input_Length2 = st.slider('Diagonal length(cm)', 0.0, 100.0, 1.0)
input_Length3 = st.slider('Cross length(cm)', 0.0, 100.0, 1.0)
input_Height = st.slider('Height(cm)', 0.0, 100.0, 1.0)
input_Width = st.slider('Diagonal width(cm)', 0.0, 100.0, 1.0)
