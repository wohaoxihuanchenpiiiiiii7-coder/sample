import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and description
st.title('CSV Data Analysis Web App')
st.write('Upload a CSV file to view basic statistics and generate interactive charts.')

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display basic information about the dataset
    st.subheader('Dataset Overview')
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")
    
    # Display column names and data types
    st.subheader('Column Information')
    st.write(df.dtypes)
    
    # Display the first 10 rows of the dataset
    st.subheader('Sample Data (First 10 rows)')
    st.write(df.head(10))
    
    # Display descriptive statistics
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
    
    # Allow user to select columns for chart
    st.subheader('Interactive Chart')
    
    # Select x-axis column
    x_column = st.selectbox('Select X-axis column:', df.columns)
    
    # Select y-axis column (only numeric columns)
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    y_column = st.selectbox('Select Y-axis column:', numeric_columns)
    
    # Select chart type
    chart_type = st.radio('Select chart type:', ['Line Chart', 'Bar Chart', 'Scatter Plot'])
    
    # Generate chart based on user selection
    if st.button('Generate Chart'):
        if chart_type == 'Line Chart':
            fig = px.line(df, x=x_column, y=y_column, title=f'{y_column} vs {x_column}')
        elif chart_type == 'Bar Chart':
            fig = px.bar(df, x=x_column, y=y_column, title=f'{y_column} vs {x_column}')
        elif chart_type == 'Scatter Plot':
            fig = px.scatter(df, x=x_column, y=y_column, title=f'{y_column} vs {x_column}')
        
        # Display the chart
        st.plotly_chart(fig)

st.write('---')
st.write('Built with Streamlit for CSV data analysis')