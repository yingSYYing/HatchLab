import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI




load_dotenv()   


client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])
st.set_page_config(
    page_title="HatchLab"
)


#logo = st.image("Pages\chick.png", width=100)

st.title("Hello, Hatchling!")
st.subheader("    Welcome to Hatch Lab Where Startups Learn to Thrive!")
st.markdown(
    """

At Hatch Lab, we believe great ideas deserve great marketing. 
We specialize in helping startups turn their vision into a brand that resonates. 
From building a strong digital presence to mastering customer acquisition, 
we guide you through the strategies that transform early-stage businesses into lasting success. 
Whether you're launching your first product or scaling your growth, 
Hatch Lab gives you the tools, knowledge, and expertise 
to market smarter, faster, and with confidence. 

Ready to hatch your next big idea? Let us get started🥚!
"""
)



st.page_link("Profile_Form.py", label="Let's Get Started!")




    
