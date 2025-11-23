import streamlit as st

st.title("Watsonx Orchestrate Embedded Chat")

embed_code = """
<div id="root" style="width:100%; height:700px;"></div>

<script>
  window.wxOConfiguration = {
    orchestrationID: "89fd1cc02bd2458cad21c01f2fbfd855_2b02d943-eeab-4874-aeb2-af5c046e113a",
    hostURL: "https://au-syd.watson-orchestrate.cloud.ibm.com",
    rootElementID: "root",
    deploymentPlatform: "ibmcloud",
    crn: "crn:v1:bluemix:public:watsonx-orchestrate:au-syd:a/89fd1cc02bd2458cad21c01f2fbfd855:2b02d943-eeab-4874-aeb2-af5c046e113a::",
    chatOptions: {
        agentId: "d8730186-1a77-4834-8e84-524d160c2ad2",
        agentEnvironmentId: "db284261-1a23-463d-9c41-79e17c837276"
    }
  };

  setTimeout(function () {
    const script = document.createElement('script');
    script.src = window.wxOConfiguration.hostURL + "/wxochat/wxoLoader.js?embed=true";
    script.addEventListener('load', function () {
        wxoLoader.init();
    });
    document.head.appendChild(script);
  }, 0);
</script>
"""

st.components.v1.html(embed_code, height=800, scrolling=True)