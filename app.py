import streamlit as st 
import pandas as pd 
import numpy as np 
import time 
import os 
from datetime import datetime 
from collections import Counter 
from PIL import Image 

st.set_page_config(layout="wide")

st.markdown("#### Hello~~ Good Luck !!!")
st.markdown("""---""") 

# 컬럼 구성 
emp0, head0, emp1 = st.columns( [0.1, 1.0, 0.1] )
emp0, con10, emp1 = st.columns( [0.1, 1.0, 0.1] )
emp0, tail0, emp1 = st.columns( [0.1, 1.0, 0.1] ) 

# 데이터 확인 
df0 = pd.read_csv("data/iris.csv") 
sr_variety = df0.variety 

# 옵션 설정 
st.sidebar.title('Iris Species🌸') 

# 셀렉트 박스 
my_select = list(sr_variety) 
choice = st.selectbox('확인하고 싶은 종을 선택하세요', my_select) 

tmp_df = df0[df0.variety == choice]
con10.dataframe(tmp_df) 


