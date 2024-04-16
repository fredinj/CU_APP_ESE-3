import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import streamlit as st
import pandas as pd

df = pd.read_csv('WomensClothingE-CommerceReviews.csv')
df = df.dropna()
df = df.reset_index(drop=True)

def main():
    st.title("3d Plot Visualization")
    st.markdown("<br>", unsafe_allow_html=True)
    st.header('Dataset Visualisation')
    st.sidebar.title("Options")
    columns_to_display = st.sidebar.multiselect('Select columns to display', df.columns, default=df.columns.tolist())
    num_rows = st.sidebar.slider('Select number of rows to display', 10, len(df))

    st.dataframe(df[columns_to_display].head(num_rows))

    plot3d()

def plot3d():
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("Scatter Plot 3D")
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(df['Age'], df['Rating'], df['Positive Feedback Count'], c='skyblue', s=60)
    ax.view_init(35, 200, -3)

    ax.set_xlabel('Age')
    ax.set_ylabel('Rating')
    ax.set_zlabel('Positive Feedback Count')

    st.pyplot(fig)

if __name__=="__main__":
    main()