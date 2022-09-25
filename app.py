import jonlib
import streamlit as st

#load joblib model
model_nb= joblib.load('spam-ham')

st.title('SPAM HAM CLASSIFIER')
ip =st.text_input('Enter the text :')

op= model_nb.predict([ip])
if st.button('Predict'):
  st.title([op])
  
