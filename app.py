import streamlit as st 
import pandas as pd 
import numpy as np 
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
emp0, con10, emp1 = st.columns( [0.1, 1.0, 0.1] )
emp0, tail0, emp1 = st.columns( [0.1, 1.0, 0.1] ) 
sbar = st.sidebar 

# 데이터 확인 
df0 = pd.read_csv("data/iris.csv") 
sr_variety = df0.variety.unique()

# 옵션 설정 
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
con10.dataframe(temp_df1) 

# 라디오  
my_rselect = list(df0.columns[:-1]) 
r_choice = sbar.radio("what is key column ?", my_rselect, horizontal=True) 

# 슬라이더 
slider_range = sbar.slider('choose range key column', 0.0, 10.0, (2.5, 7.5) )

# 버튼 
start_button = sbar.button('filter apply 📊') 



