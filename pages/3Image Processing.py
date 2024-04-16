import streamlit as st
import cv2
import numpy as np

def main():
    select_image()

    operations = ['resize', 'grayscale', 'crop', 'rotation']
    selected_operation = st.sidebar.radio('Select an operation', operations)

    if selected_operation == 'resize':
        resize_image()
    elif selected_operation == 'grayscale':
        grayscale_image()
    elif selected_operation == 'crop':
        crop_image()
    elif selected_operation == 'rotation':
        rotate_image()


def grayscale_image():
    global selected_image
    image = cv2.imread(selected_image + ".jpg")
    image_copy = np.copy(image)  
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    if st.sidebar.button('Display Grayscale Image'):  
      st.image(gray_image, channels="GRAY")

def crop_image():
    global selected_image
    image = cv2.imread(selected_image + ".jpg")
    
    image_copy = np.copy(image)  

    height, width, _ = image_copy.shape
    left = st.sidebar.slider('Left', 0, width, 0)
    right = st.sidebar.slider('Right', 0, width, width)
    top = st.sidebar.slider('Top', 0, height, 0)
    bottom = st.sidebar.slider('Bottom', 0, height, height)

    if st.sidebar.button('Display Cropped Image'):
        cropped_image = image_copy[top:bottom, left:right]
        st.image(cropped_image, channels="BGR")

def rotate_image():
    global selected_image
    image = cv2.imread(selected_image + ".jpg")
    image_copy = np.copy(image)  

    angle = st.sidebar.slider('Angle', 0, 360, 0)

    if st.sidebar.button('Display Rotated Image'):
        M = cv2.getRotationMatrix2D((image_copy.shape[1] / 2, image_copy.shape[0] / 2), angle, 1)
        rotated_image = cv2.warpAffine(image_copy, M, (image_copy.shape[1], image_copy.shape[0]))
        st.image(rotated_image, channels="BGR")

def resize_image():
    global selected_image
    image = cv2.imread(selected_image + ".jpg")
    image_copy = np.copy(image)  

    width = st.sidebar.slider('Width', 0, image_copy.shape[1], image_copy.shape[1])
    height = st.sidebar.slider('Height', 0, image_copy.shape[0], image_copy.shape[0])

    if st.sidebar.button('Display Resized Image'):
        resized_image = cv2.resize(image_copy, (width, height))
        st.image(resized_image, channels="BGR")

def select_image():
    global selected_image  
    images = ['image1', 'image2', 'image3', 'image4']
    selected_image = st.sidebar.selectbox('Select an image', images)
    display_image(selected_image)

def display_image(image):
    st.image(image+".jpg")

if __name__=="__main__":
    st.title("Image Processing")
    main()
    