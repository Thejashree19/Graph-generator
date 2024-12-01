# Graph-generator
A graph generator based on CSV file data

Key Components:
User Input Interpretation
The interpret_request function simulates how an LLM might interpret user input. In a real-world scenario, you would replace this with an API call to an LLM service (e.g., OpenAI's GPT models). The model would analyze the text and return structured information about what type of chart to create.

Chart Generation Logic
The generate_chart function uses the interpreted information to decide which type of chart to create. It handles two types of charts: trends over time and comparisons across categories.

Implementation Steps
1. Set Up Environment
Ensure you have the necessary libraries installed:

         pip install pandas matplotlib streamlit

2.. Running the Application
To run your Streamlit application, save your script as app.py and execute:

         streamlit run app.py

Future Scope :
Furthurly, working on real time application with OpenAI API key.
