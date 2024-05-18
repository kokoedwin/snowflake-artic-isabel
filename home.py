import streamlit as st

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