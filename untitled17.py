# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F3DGx2E7rXuUZKljCJVPMb4fgRF5pHLB
"""



import streamlit as st
st.set_page_config(layout="wide")

import numpy as np
import pandas as pd
from io import BytesIO

import matplotlib.pyplot as plt 
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib
import seaborn as sns

st.markdown("# IDL Project")

!ls

import matplotlib.image as mpimg
if st.sidebar.checkbox("I want to explore the data first - EDA", True, key=1):
  st.markdown("Lets look at the interactive outputs")
  select_dept = st.sidebar.selectbox('Select an image', 'image1')
  img = mpimg.imread('vis_original_size.jpg')
  st.image(img)

