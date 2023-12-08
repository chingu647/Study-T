import streamlit as st 
import plotly.express as px 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import time 
import os 
from datetime import datetime 
from collections import Counter 

from PIL import Image 


st.set_page_config(layout="wide")

st.markdown("#### Hello~~ Good Luck ^^ !!!")
st.markdown("""---""") 

# 컬럼 구성 
emp0, head0, emp1 = st.columns( [0.1, 1.0, 0.1] )
emp0, con10, con11, emp1 = st.columns( [0.1, 0.5, 0.5, 0.1] )
emp0, tail0, emp1 = st.columns( [0.1, 1.0, 0.1] ) 
sbar = st.sidebar 

# 데이터 확인 ==============================================
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

flag0 = True
if m_choice != '' and flag0==True: 
	con10.dataframe(temp_df1) 

# 라디오  
my_rselect = list(df0.columns[:-1]) 
state = sbar.radio("what is key column ?", my_rselect, horizontal=True) 
# 슬라이더 
slider_range = sbar.slider('choose range key column', 0.0, 10.0, (2.5, 7.5) )
# 버튼 
start_button = sbar.button('filter apply 📊') 
if start_button: 
	temp_df2 = df0[df0.variety.isin(m_choice)]
	temp_df2 = temp_df2[ ( temp_df2[state] >= slider_range[0] ) & ( temp_df2[state] <= slider_range[1]) ] 
	temp_df1 = temp_df2 
	
	flag0 = Falae 
	con10.dataframe(temp_df1) 
	sbar.success('Filter Applied') 
	sbar.balloons() 

# 그래프 
fig = px.scatter( df0.query("sepal_length >= 4.0" ),
	x='sepal_length',
	y='sepal_width',
	size='sepal_width', 
	color='variety', 
	hover_data =['sepal_width'],
) 
#fig.show() 
con11.plotly_chart(fig, theme="streamlit") #, use_container_width=True) 


# 지도 
base_position = [37.5073423, 127.0572734] 
map_data = pd.DataFrame(np.random.randn(5,1)/[20,20] + base_position,
	columns=['lat','lon'] 
	) 
#print(map_data) 
con11.code('con11.map(map_data)')
con11.map(map_data) 


# 프로그레스 바
latest_iteration = head0.empty() 
bar = head0.progress(0) 

for i in range(100):
	latest_iteration.text(f"Iteration {i+1}")
	bar.progress(i+1)
	time.sleep(0.05) 
head0.balloons() 




