import numpy as np
import streamlit as st
import pickle as pk

loaded_model = pk.load(open('C:/Users/Akanksha Patil/Documents/Data Science/Machine Learning/trained_model.sav', 'rb'))

# create a function for prediction

def propertyprediction(input_data):
    
    input_data_as_numpy_arrar = np.asarray(input_data).reshape(1,-1)
    input_data_as_numpy_arrar = input_data_as_numpy_arrar.astype(np.float)
    m = loaded_model.predict(input_data_as_numpy_arrar)
    return m


def main():

    # giving a title
    st.title("Boston House Price Prediction App")

    location = {
        'Whitefield', 
        'Bommanahalli'
    }
    # getting input data from user
    Location = st.selectbox("Location", location)
    BHK = st.text_input("BHK")
    Furnishing = st.text_input("Furnishing")
    Sq = st.text_input("Sq.ft")
    Old = st.text_input("Old(years)")
    Floor = st.text_input("Floor")

    if Location == "Bommanahalli":
        loc = 1
    else:
        loc = 0

    # code for prediction
    predict = ''

    # creating a button for prediciton
    if st.button("Predict Price"):
        predict = propertyprediction([loc, BHK, Furnishing, Sq, Old, Floor])
         

    st.success(predict)


if __name__ == "__main__":
    main()