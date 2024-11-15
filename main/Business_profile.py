import streamlit as st
import pages.Profile_Form as pf
st.title("Business Profile")

if 'business_type' not in st.session_state:
        st.session_state.business_type = "N/A"
if 'product' not in st.session_state:
        st.session_state.product = "N/A"
if 'industry_option' not in st.session_state:
        st.session_state.industry_option = "N/A"
if 'location' not in st.session_state:
        st.session_state.location = "N/A"
if 'demographics' not in st.session_state:
        st.session_state.demographics = "N/A"
if 'target_date' not in st.session_state:
        st.session_state.target_date = "N/A"
if 'strength_bus' not in st.session_state:
        st.session_state.strength_bus = "N/A"
if 'finance' not in st.session_state:
        st.session_state.finance = "N/A"
if 'initial_funds' not in st.session_state:
        st.session_state.initial_funds = 0

st.subheader("Business")
st.write(st.session_state.business_type)

st.subheader("Industry")
st.write(st.session_state.industry_option)

st.subheader("Products")
st.write(st.session_state.product)

st.subheader("Location")
st.write(st.session_state.location)

st.subheader("Demographics")
st.write(st.session_state.demographics)

st.subheader("Target Finish Date")
st.write(st.session_state.target_date)

st.subheader("Strengths")
st.write(st.session_state.strength_bus)

st.subheader("Finance")
st.write(st.session_state.finance)

st.subheader("Initial Funds")
st.write(st.session_state.initial_funds)
