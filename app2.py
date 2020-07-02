import os 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use("Agg")

import plotly.express as px
import plotly
import plotly.graph_objects as gobj

def main():
	#Common ML EDA
	st.title("Demo on Streamlit Visualization")
	st.subheader("Goals101")

	html_temp="""
	<div style="background-color:tomato;"><p style="color:white;font-size:45px;"> DASHBOARD</p></div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	Path=st.text_input("Enter your Path here","Type...")
	if os.path.isdir(Path):
		st.success("You are into Directory:{}".format(Path))

		def file_selector(folder_path=Path):
			filenames=os.listdir(folder_path)
			selected_filename=st.selectbox("Select a file",filenames)
			return os.path.join(folder_path,selected_filename)

		filename=file_selector()
		st.info('you selected {}'.format(os.path.split(filename)[1]))


		#Read Data
		df=pd.read_csv(filename)
		#Show Dataset
		if st.checkbox("Show Dataset"):
			number=st.number_input("Number of Rows to View",5,1000)
			st.dataframe(df.head(number))
			#st.write(df.head(5))
		#Show Columns Name
		if st.checkbox("Column Names"):
			st.write(df.columns)
		#Show Subset based on selected columns
		if st.checkbox("Select Columns to show"):
			all_col=df.columns.tolist()
			selected_col=st.multiselect("Select",all_col)
			new_df=df[selected_col]
			st.dataframe(new_df)
		#Value counts of selected column
		colm=st.selectbox('Select a column',df.columns)
		if st.button("Value Counts"):
			st.text("Value counts  {}".format(colm))
			st.write(df[colm].value_counts())
		#Plots and Visualizations
		st.subheader('Data Visualization')
		#Custom plot
		st. subheader('Custom Plot')
		all_col=df.columns.tolist()
		type_of_plot=st.selectbox("Select the Type of Plot",['area','bar','line','hist','boxplot','kde'])
		selected_cols=st.multiselect("Select Columns",all_col)
		if st.button("Generate Plot"):
			st.success("Generate Custom plot of {} for {}".format(type_of_plot,selected_cols))

			#plot by Streamlit
			if type_of_plot=='area':
				df2=df[0:10000]
				cust_data=df2[selected_cols]
				st.dataframe(cust_data.head())
				st.area_chart(cust_data)
			elif type_of_plot=='line':
				df2=df[0:10000]
				cust_data=df2[selected_cols]
				st.dataframe(cust_data.head())
				st.line_chart(cust_data)
			elif type_of_plot=='bar':
				df2=df[0:10000]
				cust_data=df2[selected_cols]
				st.dataframe(cust_data.head())
				st.bar_chart(cust_data)
			#graph using simple python codiing
			elif type_of_plot=='boxplot':
				df2=df[0:1000]
				cust_data=df2[selected_cols]
				st.write(plt.boxplot(cust_data))
				st.pyplot()

			#graph using simple python codiing
			elif type_of_plot:
				df2=df[0:10000]
				cust_plot=df2[selected_cols].plot(kind=type_of_plot)
				st.write(cust_plot)
				st.pyplot()
				
		#Pie Chart
		if st.checkbox("Pie Plot"):
			all_col=df.columns.tolist()
			selected_col=st.selectbox("Select a columnn",all_col)
			if st.button("Generate Pie Plot"):
				st.success("Generating a Pie Chart")
				df2=df[0:10000]
				st.write(df[selected_col].value_counts().plot.pie(autopct="%1.1f%%"))
				st.pyplot()
		#Coorelation plot seaborn
		if st.checkbox("Correlation Plot['seaboarn']"):
			st.write(sns.heatmap(df.corr(),annot=True))
			st.pyplot()
		#Count Plot
		if st.checkbox("Count Plot"):
			st.text("Values counts by Categorical Variable")
			all_colm=df.columns.tolist()
			
			selected_cols_grpby=st.multiselect("Select few Columns",all_colm)
			groupby_col=st.selectbox("Group By",all_col)
			if st.button("Generate Count Plot"):
				st.success("Generating count plot...")
				if selected_cols_grpby:
					vc_plot=df.groupby(groupby_col)[selected_cols_grpby].count()
				st.table(vc_plot)
				st.write(vc_plot.plot(kind='bar'))
				st.pyplot()
		# few more visualisation using plotly
		df = df.replace(np.nan, 'Unknown Value', regex=True)
		#pie chart using plotly
		st.subheader("Pie Chart Using Plotly")
		st.write(px.pie(df, names='debit_txn_or_credit_txn'))

		# Line chart using plotly
		df['txn_date'] = pd.to_datetime(df['txn_date'], errors='coerce')
		df["txn_year"]=df['txn_date'].dt.year
		df["txn_month"]=df['txn_date'].dt.month

		df2=df[['txn_date','txn_month','txn_year']].groupby(by=['txn_year','txn_month']).count()
		df2.reset_index(level=0, inplace=True)
		df2.reset_index(level=0, inplace=True)

		fig2 = px.line(df2, x="txn_month",y="txn_date",color='txn_year')
		fig2.update_layout(title_text="Number of transaction over years")
		st.write(fig2)
	else:
		st.warning("You Entered wrong Path")


if __name__=='__main__':
	main()
