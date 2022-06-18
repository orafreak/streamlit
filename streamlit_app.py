import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.title('title')

st.header('header')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)


dict = {
    'col1': ['a', 'b', 'c', 'd', 'e'],
    'col2': [1,2,3,4,5]

}
st.header("Writing a dictionary")
st.write(dict)

df = pd.DataFrame(dict)

st.header("Writing a data frame")

st.write("on top of df", df, "at the bottm of df")

df2 = pd.DataFrame(
np.random.randn(200,3),  columns =['a','b','c']
)

st.header("Writing DF2")

# st.write("on top of df", df2, "at the bottm of df")

c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)