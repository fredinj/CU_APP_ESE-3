import cv2
import streamlit as st

selected_image = None

def main():

  select_image()
  


def select_image():
  images = ['image1', 'image2', 'image3', 'image4']

  selected_image = st.sidebar.selectbox('Select an image', images)

  display_image(selected_image)
  

def display_image(image):
  st.image(image+".jpg")
  

if __name__=="__main__":
  st.title("Image Processing")
  st.markdown("<br>", unsafe_allow_html=True)

  main()