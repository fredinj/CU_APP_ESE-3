import streamlit as st

import pandas as pd
import nltk
from nltk.corpus import stopwords as sw
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stopwords = set(sw.words('english'))
df = pd.read_csv('WomensClothingE-CommerceReviews.csv')
df = df.dropna()
df = df.reset_index(drop=True)


def main():


  for i in range(len(df)):
      # df['Review Text'] = df['Review Text'].apply(preprocess_text)
      
      df.loc[i, 'Review Text'] = preprocess_text(df.loc[i, 'Review Text'])
      

  divisions = ['General', 'General Petite', 'Initmates']

  vectorizer = TfidfVectorizer()

  similar_reviews = {}

  for division in divisions:
      df_filtered = df[df['Division Name'] == division]

      tfidf_matrix = vectorizer.fit_transform(df_filtered['Review Text'])

      cosine_sim_matrix = cosine_similarity(tfidf_matrix)

      index = 0

      similar_indices = cosine_sim_matrix[index].argsort()[:-5:-1]

      similar_reviews[division] = df_filtered.iloc[similar_indices]['Review Text'].tolist()
      
  st.dataframe(df)
  
  st.markdown("<br>", unsafe_allow_html=True)
  st.header("Similar Reviews")
  
  for division, reviews in similar_reviews.items():
    st.header(division)
    for review in reviews:
        st.write(review)

  
  
def preprocess_text(text):
    text = text.lower()
    
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    words = nltk.word_tokenize(text)
    
    words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords]
    
    text = ' '.join(words)
    
    return text


if __name__ == "__main__":
  st.title('Text Analysis')
  main()