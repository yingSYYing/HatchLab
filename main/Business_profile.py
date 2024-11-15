import streamlit as st
import pages.Profile_Form as pf
st.title("Business Profile")

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
