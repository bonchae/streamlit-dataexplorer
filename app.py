import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title('Data Explorer')

st.image("https://www.akc.org/wp-content/uploads/2017/11/Pembroke-Welsh-Corgi-standing-outdoors-in-the-fall.jpg")

st.markdown("""
This app performs simple data visualization of the popular Titanic data!
* **Python libraries:** plotly, streamlit
""")



st.title('Predict Titanic Survival')

df = pd.read_csv('https://raw.githubusercontent.com/bonchae/data/master/titanic_train.csv') 

if st.checkbox('Show dataframe'):
    st.write(df)

if st.checkbox('Do you want to know the overall probability of survival?'):
    a = (df.groupby('Survived').size()/df.shape[0]).round(2).reset_index() 
    a.columns=['Survived','Probability']
    fig=px.bar(a,x='Survived',y='Probability',text='Probability')
    st.plotly_chart(fig)

st.subheader('Box plot')
feature = st.selectbox('Which feature?', ('Age','Embarked','Fare','Pclass','Sex'))
fig = px.box(df, y=feature, points='all', hover_name='Survived')
st.plotly_chart(fig)

st.subheader('Styled Box plot')
xfeature = st.selectbox('Which feature for X axis?', ('Embarked','Pclass','Sex','Survived'))
yfeature = st.selectbox('Which feature for Y axis?', ('Age','Fare'))
fig = px.violin(df, y=yfeature, x=xfeature, color="Survived", box=True, points="all", hover_data=df.columns)
st.plotly_chart(fig)

st.subheader('Scatter plot')
new_df = df[['Age','Fare','Survived']]
col1 = st.selectbox('Which feature on x?', new_df.columns)
col2 = st.selectbox('Which feature on y?', new_df.columns)
fig = px.scatter(df, x =col1,y=col2, color='Survived')
st.plotly_chart(fig)

st.subheader('Histogram')
feature = st.selectbox('Which feature for histogram?', ('Age','Embarked','Fare','Pclass','Sex'))
fig = px.histogram(df, x=feature, color="Survived", marginal="rug")
st.plotly_chart(fig)

st.markdown("## Party time!")
st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()
