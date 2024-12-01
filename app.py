import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Function to generate chart based on user input
def generate_chart(user_input, data):
    # Basic interpretation of user input for chart type
    if "trend" in user_input.lower() or "time" in user_input.lower():
        plt.figure(figsize=(10, 5))
        plt.plot(data['Date'], data['Sales'], marker='o')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        
    elif "compare" in user_input.lower() or "bar" in user_input.lower():
        plt.figure(figsize=(10, 5))
        plt.bar(data['Region'], data['Revenue'], color='skyblue')
        plt.title('Revenue by Region')
        plt.xlabel('Region')
        plt.ylabel('Revenue')

    else:
        st.warning("Sorry, I can't interpret that request. Please try something else.")

    # Show the plot
    st.pyplot(plt)
def interpret_request(user_input):
    # This function simulates calling an LLM API to get chart type.
    # Replace this with actual API call in production.
    if "trend" in user_input.lower() or "time" in user_input.lower():
        return {'chart_type': 'trend'}
    elif "compare" in user_input.lower() or "bar" in user_input.lower():
        return {'chart_type': 'comparison'}
    else:
        return {'chart_type': 'unknown'}
# Streamlit UI setup
st.title("Dynamic Chart Generator")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    # Create a sample dataset if no file is uploaded
    data = pd.DataFrame({
        'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01'],
        'Sales': [200, 220, 250, 275, 300],
        'Region': ['North', 'South', 'East', 'West', 'Central'],
        'Revenue': [1000, 1500, 800, 1200, 900]
    })

# User input for chart generation
user_input = st.text_input("Describe the graph or analysis you want:")

if st.button("Generate Chart"):
    if user_input:
        generate_chart(user_input, data)
    else:
        st.warning("Please enter a description for the graph.")