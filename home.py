import os
import streamlit as st
import replicate
#from dotenv import load_dotenv

# Load environment variables from .env file
#load_dotenv()

# Get the API key from environment variable
REPLICATE_API_KEY = "r8_GYW7N0jnSLhjTuspToX1fzbvIdRJnBv4Jepfq"

# Function to generate documentation using Replicate with streaming output
def generate_documentation_with_replicate(title, code, insights, data_sources, methodology, results, conclusion, recommendations, references):
    prompt = f"""
    Project Title: {title}
    Code Snippets: {code}
    Insights: {insights}
    Data Sources: {data_sources}
    Methodology: {methodology}
    Results: {results}
    Conclusion: {conclusion}
    Recommendations: {recommendations}
    References: {references}
    """
    
    # Setting up the streaming
    response = ""
    for event in replicate.stream(
        "snowflake/snowflake-arctic-instruct",
        input={
            "top_k": 50,
            "top_p": 0.9,
            "prompt": prompt,
            "temperature": 0.2,
            "max_new_tokens": 512,
            "min_new_tokens": 0,
            "stop_sequences": "",
            "prompt_template": "system\nYou're a helpful assistant\nuser\n{prompt}\n\nassistant\n",
            "presence_penalty": 1.15,
            "frequency_penalty": 0.2
        },
        api_token=REPLICATE_API_KEY
    ):
        response += str(event)
    
    return response

st.title("ISABEL: Documentation Generator for Analysts")

st.header("Create Documentation")

# Input fields for analysts
title = st.text_input("Project Title", placeholder="Enter the project title")
code = st.text_area("Code Snippets", placeholder="Enter your code snippets here")
insights = st.text_area("Insights", placeholder="Enter key findings and interpretations")
data_sources = st.text_area("Data Sources", placeholder="Describe the data sources used")
methodology = st.text_area("Methodology", placeholder="Describe the methods and techniques used")
results = st.text_area("Results", placeholder="Summarize the results of your analysis")
conclusion = st.text_area("Conclusion", placeholder="Summarize your conclusions")
recommendations = st.text_area("Recommendations", placeholder="Enter any actionable recommendations")
references = st.text_area("References", placeholder="List any references or citations")

if st.button("Generate Documentation"):
    if all([title, code, insights, data_sources, methodology, results, conclusion, recommendations, references]):
        with st.spinner('Generating documentation...'):
            documentation = generate_documentation_with_replicate(title, code, insights, data_sources, methodology, results, conclusion, recommendations, references)
            st.markdown("### Generated Documentation")
            st.markdown(documentation)
    else:
        st.warning("Please fill in all fields to generate documentation.")
