import streamlit as st
import requests

# Function to generate documentation using Replicate
def generate_documentation_with_replicate(title, code, insights, data_sources, methodology, results, conclusion, recommendations, references):
    api_url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": "r8_GYW7N0jnSLhjTuspToX1fzbvIdRJnBv4Jepfq",
        "Content-Type": "application/json"
    }
    payload = {
        "input": {
            "title": title,
            "code": code,
            "insights": insights,
            "data_sources": data_sources,
            "methodology": methodology,
            "results": results,
            "conclusion": conclusion,
            "recommendations": recommendations,
            "references": references
        },
        "model": "your-replicate-model-identifier"  # Replace with the actual model identifier
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("output", "No documentation generated")
    else:
        return "Error generating documentation"

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
        documentation = generate_documentation_with_replicate(title, code, insights, data_sources, methodology, results, conclusion, recommendations, references)
        st.markdown("### Generated Documentation")
        st.markdown(documentation)
    else:
        st.warning("Please fill in all fields to generate documentation.")