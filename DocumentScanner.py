
import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np


st.title("Document Scanner Application")
uploaded_image=st.file_uploader('Please upload an Image',type=['jpg','jpeg','png'])

# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def Extract_Text(img):
    text=pytesseract.image_to_string(img)
    return text

if uploaded_image is not None:
    img=Image.open(uploaded_image)
    image_array=np.array(img)
    st.image(image_array,'Uploaded Image...')

    with st.spinner('Extracting Text From Your Image...'):
        extracted_test=Extract_Text(image_array)
        st.subheader('Extracted Text:')
        text_list = extracted_test.splitlines()
        st.write(text_list)
        st.write('Organization Name: ', text_list[0] + ' ' + text_list[1])
        st.write('Education : ',text_list[4])
        st.write(text_list[5][:16])
        st.write('address : ',text_list[8]+' '+text_list[9])
