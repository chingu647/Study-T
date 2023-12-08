import streamlit as st 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import time 
import os 
from datetime import datetime 
from collections import Counter 

from PIL import Image 
import plotly.express as px 

st.set_page_config(layout="wide")

st.markdown("#### Hello~~ Good Luck ^^ !!!")
st.markdown("""---""") 

# 컬럼 구성 
emp0, head0, emp1 = st.columns( [0.1, 1.0, 0.1] )
emp0, con10, con11, emp1 = st.columns( [0.1, 0.5, 0.5, 0.1] )
emp0, tail0, emp1 = st.columns( [0.1, 1.0, 0.1] ) 
sbar = st.sidebar 

# 데이터 확인 
df0 = pd.read_csv("data/iris.csv") 
df0.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'variety']
sr_variety = df0.variety.unique()

# 사이드 바 ================================================
sbar.title('Iris Species🌸') 

# 셀렉트 박스 
#my_select = list(sr_variety) 
#choice = sbar.selectbox('확인하고 싶은 종을 선택하세요', my_select) 

#temp_df = df0[df0.variety == choice]
#con10.dataframe(temp_df) 

# 멀티셀렉트 
my_mselect = list(sr_variety) 
m_choice = sbar.multiselect('확인하고 싶은 종은? (복수선택 가능)', my_mselect) 
temp_df1 = df0[df0.variety.isin(m_choice)] 
if not temp_df1.empty: 
    con10.dataframe(temp_df1) 

# 라디오  
my_rselect = list(df0.columns[:-1]) 
state = sbar.radio("what is key column ?", my_rselect, horizontal=True) 
# 슬라이더 
slider_range = sbar.slider('choose range key column', 0.0, 10.0, (2.5, 7.5) )
# 버튼 
start_button = sbar.button('filter apply 📊') 
if start_button: 
    temp_df1 = df0[df0.variety.isin(m_choice)]
    temp_df1 = temp_df1[ ( temp_df1[state] >= slider_range[0] ) & ( temp_df1[state] <= slider_range[1]) ] 

    con10.table(temp_df1) 
    sbar.success('Filter Applied') 
    sbar.balloons() 

# 그래프 
fig = px.scatter( df0, #.query(f"sepal_length >= 4.0" ),
	x='sepal_length',
	y='sepal_width',
#	size='pop', 
	color='continent', 
	log_x=True, 
	size_max=60 ) 
#fig.show() 


