import os
import streamlit as st
from openai import OpenAI


import streamlit as st

with st.form("my_form"):
    #Kind of business
    st.header("Business Structure")
    business_type = st.selectbox(
        "What kind of business will you be operating?",
        ("Soletrader", "Partnership", "Limited Partnership", "Medium-sized enterprise", "Large-scale enterprise", "Social enterprise"),
    )

    st.write("You selected:", business_type)
    st.divider()

   #Products sold by the business
    st.header("Products")
    product = st.text_input("What products are you selling?")
    st.divider()


    #industry the business will operate in
    st.header("Industry")
    industry_option = st.selectbox(
        "Which industry will you be working in?",
        ("Agriculture  &  Agribusiness", "Automotive", "Technology & IT", 
        "Healthcare & Life Sciences", "Energy", "Finance & Banking", 
        "Retail & Consumer Goods", "Construction & Real Estate", "Education", 
        "Transportation & Logistics", "Entertainment & Media", 
        "Manufacturing & Industrial Goods", "Hospitality & Tourism", 
        "Telecommunications", "Legal & Professional Services", "Government & Public Sector", 
        "Pharmaceuticals & Biotechnology", "Aerospace & Defense", "Environmental Services & Sustainability",
        "Arts & Culture"),
    )

    st.write("You selected:", industry_option)
    st.divider()

    #location of the business
    st.header("Location")
    location = st.selectbox(
        "Where will you be located?",
        ("Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", 
        "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", "Sarawak", 
        "Selangor", "Terengganu", "Wilayah Persekutuan Kuala Lumpur", 
        "Wilayah Persekutuan Labuan", "Wilayah Persekutuan Putrajaya"),
    )

    st.write("You selected:", location)
    st.divider()

    #demographics of target market
    st.header("Demographics")
    demographics = st.multiselect(
        "What is your target market?",
        (
        "Children & Teens", "Young Adults", "Middle-Aged Adults", 
        "Seniors/Older Adults", "Men", "Women", "Non-Binary/All Genders", 
        "Low-Income", "Middle-Income", "High-Income", "High School and College Students", 
        "College Graduates", "Professionals", "Blue-Collar Workers", 
        "Freelancers/Entrepreneurs", "Single Individuals", "Married Couples", 
        "Parents with Children", "Empty Nesters", "Urban Markets", "Suburban Markets", 
        "Rural Markets", "Regional Markets", "International Markets", "Health-Conscious Consumers", 
        "Eco-Conscious Consumers", "Tech-Savvy Consumers", "Environmentalists", 
        "Socially Conscious Consumers", "Religious Consumers", "Sports Enthusiasts", "Travelers", 
        "Gamers", "Loyal Customers", "Discount Shoppers", "Occasional Shoppers", "Heavy Users", 
        "Light Users", "Quality Seekers", "Convenience Seekers", "Price-Conscious Shoppers", "Small Businesses", 
        "Large Corporations", "Startups", "Patients", "Healthcare Providers", "Students", "Schools/Institutions", 
        "Homebuyers", "Renters", "Real Estate Investors", "Early Adopters", "Mass Market", "Pet Owners", "Vegan/Vegetarian Consumers", 
        "Luxury Consumers", "Adventure Travelers","Disabled"),
    )

    st.write("You selected:", demographics)
    st.divider()


    #by when the business can/will sell their products
    st.header("Target Finish Date")
    target_date = st.select_slider(
        "Select a target time to market your product",
        options=[
            "1 month", "2 months", "3 months",
            "4 months","5 months", "6 months",
            "7 months", "8 months","9 months",
            "10 months","11 months","1 year",
            "2 years","3 years","4 years",
            "5 years","6 years","7 years",
            "8 years", "9 years","10 years",
        ],
    )
    st.write("You selected ", target_date, "as your target date.")
    st.divider()

    #Strengths of the business
    st.header("Strengths")
    strength_bus = st.text_input("What are your strengths as a business?")
    st.divider()

    #Whether they have finance or not
    st.header("Finance")
    finance = st.radio(
        "Do you have your own finances or are you looking for investors?",
        ["Self-funded", "Looking for investors",],
        captions=[
            "I have my own funds or can get the money myself without help.",
            "I am looking for investors or ways to finance my business",
        ],
    )
    st.divider()

    #How much capital they have right now
    st.header("Initial Funds")
    intiial_funds = st.number_input(
        "What is your budget to start the business", value=None, placeholder="Type a number..."
    )
    st.write("The current number is ", intiial_funds)
    st.form_submit_button('Submit my picks')