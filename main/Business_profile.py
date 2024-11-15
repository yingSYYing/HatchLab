import streamlit as st
import pages.Profile_Form as pf
st.title("Business Profile")

st.subheader("Business")
st.write(pf.business_type)

st.subheader("Industry")
st.write(pf.industry_option)

st.subheader("Products")
st.write(pf.product)

st.subheader("Location")
st.write(pf.updated_location)

st.subheader("Demographics")
st.write(pf.demographics)

st.subheader("Target Finish Date")
st.write(pf.target_date)

st.subheader("Strengths")
st.write(pf.strength_bus)

st.subheader("Finance")
st.write(pf.finance)

st.subheader("Initial Funds")
st.write(pf.intiial_funds)
