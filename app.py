import streamlit as st
from PIL import Image

# Text/Title
st.title('Streamlit Dashboard')

# Header/Subheader
st.header('this is header')
st.subheader('this is Subheader')

# Text
st.text('Hello Streamlit text')

# Markdown
st.markdown('### This is Markdown')

#Error/Colorful text
st.success('Successful')

st.info('Information!')

st.warning('this is warning')

st.error('this is error msg')

st.exception("NameError('name three not defined')")

#Get Help Info about python
st.help(range)

#writing text/super fxn
st.write('Text with write')

st.write(range(10))

#image

img=Image.open('paraview.png')
st.header("Paraview is mainly created for 3d Graphs")
st.image(img,width=700,caption='Sample img')

#Video
st.header("Mask Detection Computer Vision Application")
vid_file=open("dhruvCV.mp4","rb").read()
#vid_bytes=vid_file.read()
st.video(vid_file)


#Widget
#Checkbox
if st.checkbox('Show/Hide'):
	st.text("Show/Hide Widget")

#Radio
status=st.radio("whats the status",("Active","Inactive"))

if status=="Active":
	st.success('You are Active')
else:
	st.warning('Inactive,Activate')

#SelectBox
occupation=st.selectbox("Your Occupation",("Data Scienctist","Data Engineer","PHP Developer"))
st.write("you selected this option",occupation)

#MultiSelection
location=st.multiselect("Preferred Location",("London","Paris","NYC","NCR Delhi"))
st.write("you selected",len(location),"locations")

#Slider
level=st.slider("what is your level",1,20)

#Button
st.button("Simple Button")

if st.button("About"):
	st.text("This is streamlit app created on python 3.7")

#Input
email=st.text_input("Enter your Email","Type here")
if st.button("Submit"):
	result=email.title()
	st.success(result)

#Text Area
message=st.text_area("Enter your query here","Type here...")
if st.button("Done"):
	result=message.title()
	st.success(result)

#Data Input
import datetime
today=st.date_input("Today is",datetime.datetime.now())

#Time
the_time=st.time_input('The time is',datetime.time())

#Display JSON
st.text("Display JSON")
st.json({'name':'dhruv','gender':'M'})

# Display Python Code
st.text('Display Raw Code')
st.code('import numpy as np')

#Display row code
with st.echo():
	#this will also show as comment
	import pandas as pd 
	df=pd.DataFrame

#Progress Bar
import time
my_bar=st.progress(0)
for p in range(10):
	my_bar.progress(p+1)

#Spinner
with st.spinner("Waiting..."):
	time.sleep(5)
st.success('Finished!')

#Ballons
#st.balloons()


#Side bars
st.sidebar.header("About")
st.sidebar.text("this is streamlit sidebar")
st.sidebar.button("sidebutton")

#Function
@st.cache
def run_fxn():
	return range(100)
st.write(run_fxn())

#Plot
#st.pyplot()

df=pd.read_csv(r'D:\Goles 101 data\Mock_Data\Data1.csv')

#DataFrame
#st.dataframe(df)

#Tables
st.table(df)

data2=pd.read_csv(r'D:\Goles 101 data\Mock_Data\Data2.csv')

#DataFrame
st.dataframe(data2.head())