import streamlit as st
import nltk

def main():
  
  d = nltk.downloader.Downloader()

  for pkg in d.packages():
      if not d.is_installed(pkg.id):
          nltk.download('all')
          break
          
  st.write("Name: Fredin Johns")
  st.write("Roll No: 2347116")

    
if __name__ == "__main__":
  main()
  st.title('Home')
  st.write('Welcome to the home page!')