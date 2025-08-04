type_mapping = {1: "mammal", 2:"bird", 3:"reptile", 4:"fish", 5:"amphibian", 6:"insect", 7:"invertbrate"}

import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("model.pkl", "rb") as p:
    model = pickle.load(p)

st.title("Animal Type Detection")


st.write ("Please Enter the required Values to predict the animal types")

hair = st.number_input("Enter the hair:", min_value = 0.0, format = "%.1f")
feathers = st.number_input("Enter the feathers:", min_value = 0.0, format = "%.1f")
eggs = st.number_input("Enter the eggs:", min_value = 0.0, format = "%.1f")
milk = st.number_input("Enter milk:", min_value = 0.000, format = "%.3f")
airborne = st.number_input("Enter airborne:", min_value = 0.000, format = "%.3f") 
aquatic = st.number_input("Enter the aquatic for the animal: ", min_value = 0.0, format = "%.1f")
predator = st.number_input("Enter the predator:", min_value = 0.0, format = "%.1f")
toothed = st.number_input("Enter the toothed:", min_value = 0.0, format = "%.1f")
backbone = st.number_input("Enter the backbone:", min_value = 0.0, format = "%.1f")
breathes = st.number_input("Enter breathes:", min_value = 0.000, format = "%.3f")
venomous = st.number_input("Enter venomous:", min_value = 0.000, format = "%.3f") 
fins = st.number_input("Enter the fins:", min_value = 0.0, format = "%.1f")
legs = st.number_input("Enter the legs:", min_value = 0.0, format = "%.1f")
tail = st.number_input("Enter the tail:", min_value = 0.0, format = "%.1f")
domestic = st.number_input("Enter domestic:", min_value = 0.000, format = "%.3f")
catsize = st.number_input("Enter catsize:", min_value = 0.000, format = "%.3f") 

if st.button("predict type"):
    columns = np.array([["hair", "feathers", "eggs", "milk", "airborne", "aquatic", "predator", "toothed", "backbone", "breathes", 
                          "venomous", "fins", "legs", "tail", "domestic", "catsize"]])
    features = np.array([[hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, 
                          venomous, fins, legs, tail, domestic, catsize]])
    
    predictions = model.predict(features)
    pred_string = type_mapping[predictions[0]]
    st.success(f"predicted type is:  {pred_string}")
    st.write("prediction output:", predictions)

