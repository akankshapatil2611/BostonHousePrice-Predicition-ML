#import yfinance as yf
#import streamlit as st
import pickle as pk

loaded_model = pk.load(open('C:/Users/Akanksha Patil/Documents/Data Science/Machine Learning/trained_model.sav', 'rb'))

m = loaded_model.predict([[1,2,0,1290,1,10]])
print(m)



