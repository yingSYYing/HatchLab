import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()   

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

import streamlit as st

pages = {
    "Hatch Lab": [
        st.Page("Hello.py", title="Hello!"),
    ],
    "Your business": [
        st.Page("Profile_Form.py", title= "Information Update"),
        st.Page("Business_profile.py", title="Business profile"),
    ],
    "Resources": [
        st.Page("3Roadplan.py", title="Roadmap"),
        st.Page("Trend_Analysis.py", title="Trend Analysis"),
    ],
}

pg = st.navigation(pages)
pg.run()