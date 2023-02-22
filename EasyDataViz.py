#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title('Data Visualization Tool')

# Upload data
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Preview the data
    st.write('Preview of the data:')
    st.write(df.head())

    # Create visualizations
    st.subheader('Data visualizations')
    
    # Histogram
    hist_col = st.selectbox('Select a column for the histogram', df.columns)
    fig_hist = px.histogram(df, x=hist_col)
    st.plotly_chart(fig_hist)

    # Scatter plot
    scatter_cols = st.multiselect('Select two columns for the scatter plot', df.columns)
    if len(scatter_cols) == 2:
        fig_scatter = px.scatter(df, x=scatter_cols[0], y=scatter_cols[1])
        st.plotly_chart(fig_scatter)

    # Bar chart
    bar_col = st.selectbox('Select a column for the bar chart', df.columns)
    bar_agg = st.selectbox('Select an aggregation function', ['count', 'sum', 'avg', 'min', 'max'])
    if bar_agg == 'count':
        fig_bar = px.histogram(df, x=bar_col)
    else:
        fig_bar = px.bar(df, x=bar_col, y=bar_col, aggregation_function=bar_agg)
    st.plotly_chart(fig_bar)

    # Line chart
    line_cols = st.multiselect('Select one or more columns for the line chart', df.columns)
    if len(line_cols) > 0:
        fig_line = px.line(df, x='date', y=line_cols)
        st.plotly_chart(fig_line)


# In[ ]:




