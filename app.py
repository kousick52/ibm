import streamlit as st

st.set_page_config(page_title="Watsonx Orchestrate Chat", layout="wide")

st.title("Watsonx Orchestrate Chat (Iframe Mode)")

iframe_code = """
<iframe
    src="https://au-syd.watson-orchestrate.cloud.ibm.com/wxochat/?agentId=d8730186-1a77-4834-8e84-524d160c2ad2&agentEnvironmentId=db284261-1a23-463d-9c41-79e17c837276&embed=true"
    width="100%"
    height="800"
    style="border: none;"
></iframe>
"""

st.components.v1.html(iframe_code, height=820)