


import imageio
import streamlit as st
st.set_page_config(layout="wide")



st.markdown("# IDL Project")



import matplotlib.image as mpimg
#if st.sidebar.checkbox("I want to explore the data first - EDA", True, key=1):
st.markdown("Lets look at the interactive outputs")
file1='sample//'
file2='out//'
l1=['id00017', 'id00061','id00081','id00154','id00419','id00562','id00812','id00817','id00866','id00926','id01000','id01041','id01066','id01106',  'id01224',  'id01228',  'id01298',  \
 'id01333',  'id01437',  'id01460']
l2=['00033.mp4', '00264.mp4', '00010.mp4', '00005.mp4', '00446.mp4', '00126.mp4', '00336.mp4', '00217.mp4', '00166.mp4', '00117.mp4', '00076.mp4', '00243.mp4', '00066.mp4', '00326.mp4',\
    '00467.mp4', '00301.mp4', '00497.mp4', '00082.mp4', '00019.mp4', '00206.mp4']
select_dept = st.sidebar.selectbox('Select an image', ('id00017', 'id00061','id00081','id00154','id00419','id00562','id00812','id00817','id00866','id00926','id01000','id01041','id01066',\
                                                       'id01106',  'id01224',  'id01228',  'id01298',  'id01333',  'id01437',  'id01460'))
if select_dept=='id00017':
  filename1='sample//id00017//00033.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename='out//id00017//00033.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
  

elif select_dept==l1[1]:
  filename1=file1+l1[1]+'//00264.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[1]+'//00264.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
  
elif select_dept==l1[2]:
  filename1=file1+l1[2]+'//00010.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[2]+'//00010.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[3]:
  filename1=file1+l1[3]+'//00005.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[3]+'//00005.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[4]:
  filename1=file1+l1[4]+'//00446.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[4]+'//00446.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[5]:
  filename1=file1+l1[5]+'//00126.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[5]+'//00126.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[6]:
  filename1=file1+l1[6]+'//00336.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[6]+'//00336.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[7]:
  filename1=file1+l1[7]+'//00217.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[7]+'//00217.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[8]:
  filename1=file1+l1[8]+'//00166.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[8]+'//00166.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[9]:
  filename1=file1+l1[9]+'//00117.mp4'
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[9]+'//00117.mp4'
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[10]:
  filename1=file1+l1[10]+'//'+l2[10]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[10]+'//'+l2[10]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[11]:
  filename1=file1+l1[11]+'//'+l2[11]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[11]+'//'+l2[11]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[12]:
  filename1=file1+l1[12]+'//'+l2[12]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[12]+'//'+l2[12]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[13]:
  filename1=file1+l1[13]+'//'+l2[13]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[13]+'//'+l2[13]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[14]:
  filename1=file1+l1[14]+'//'+l2[14]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[14]+'//'+l2[14]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[15]:
  filename1=file1+l1[15]+'//'+l2[15]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[15]+'//'+l2[15]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[16]:
  filename1=file1+l1[16]+'//'+l2[16]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[16]+'//'+l2[16]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[17]:
  filename1=file1+l1[17]+'//'+l2[17]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[17]+'//'+l2[17]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[18]:
  filename1=file1+l1[18]+'//'+l2[18]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[18]+'//'+l2[18]
  vid = open(filename,  'rb')
  st.video(vid)
elif select_dept==l1[19]:
  filename1=file1+l1[19]+'//'+l2[19]
  vid1 = open(filename1,  'rb')
  st.video(vid1)
  filename=file2+l1[19]+'//'+l2[19]
  vid = open(filename,  'rb')
  st.video(vid)
  
