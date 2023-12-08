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
st.dataframe(df0.columns)

# 옵션 설정 


