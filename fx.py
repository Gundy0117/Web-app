from os import lchown
import pandas_datareader.data as pdr
import datetime
from matplotlib import pyplot as plt
import  seaborn as sns
import streamlit as st


#Get dates
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
first_day = today.replace(day=1)

#Get prices
data = pdr.get_data_yahoo('JPY=X',end=today ,start=first_day)
data = data[['High','Low']]

st.line_chart(data)