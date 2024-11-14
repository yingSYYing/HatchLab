import os
import re
import time 
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from openai import OpenAI
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="Roadmap", page_icon="")

load_dotenv()

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])



def loadingBar():
    

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

# inputted: industry, startup country, products, strength, target audience, timestamp, investor and fund availability

# Generated: Roadplan:
# Shortterm: according to timestamp
# Long term: 
# Business model: 
# Opps
# Marketing STrats
# Networking Suggestion

#examples
products = ["Furniture", "Woodworking", "Antiques"]
industry = "Furniture"
audience = "Adults"
timestamp = "6 months"
strength = "High durability and quality, eco-friendly"
investors = True
startup_fund = 50000 
country = "Norway"



# needed: products, industry, target audience
def genModel(products, industry, audience):
    busModel= f"""Create a business model consisting of its main four categories and relevant subcategories
                using the information known by the client startup: They plan to work with these products: {products},
                They work in {industry}, and their target audience is {audience}.
                                        
                Please generate in the format of the business model table, with these instructions: (Do not write the words Heading: and Content:, those are just for guidance of format)
                (in bullet points, straight to the point, short but concise)
                
                
                
                    
                                      
                Heading: [VALUE PROPOSITIONS] (no need rows or tables)
                Content: .............................................................................. 
                          
                (A VISIBLE SEPARATION LINE)
                                        
                Heading: REVENUE MODEL:  (Split in two columns) (ENSURE IT IS TABULAR)
                (For this one, display in two columns, and two rows)
                (First row are the headers, align centre)): COST STUCTURE, REVENUE STREAMS
                (second row are the contents in bullet points, align left, all contents for respective infrastructure will fit in one single column,  no need multiple rows)
                
                (A VISIBLE SEPARATION LINE)
                
                Heading: CUSTOMERS SEGMENT:  (Split in three columns) (ENSURE IT IS TABULAR)
                (For this one, display in three columns, and two rows)
                (First row are the headers, align center): CUSTOMER RELATIONSHIPS, CHANNELS, CUSTOMER SEGMENTS
                (second row are the contents in bullet points, align left, all contents for respective infrastructure will fit in one single column,  no need multiple rows)
                (still maintain a tabular format, contents for respective categories all stay in same column)
                
                (A VISIBLE SEPARATION LINE)
                               
                Heading: INFRASTRUCTURE:  (Split in three columns) (ENSURE IT IS TABULAR)
                (For this one, display in three columns, and two rows)
                (First row are the header, align center): PARTNERS, RESOURECES, ACTIVITIES
                (second row are the contents in bullet points, align left)
                                     
                
                                        
                Generate the business model in that table format above thank you. 
                                        
            """

    businessModel = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {"role": "system", "content":"You are a well-renowned consultant for businesses and startups and have incredibly prodigious business sense. "},
          {"role":"user", "content":busModel}
      ],
    )
    return businessModel.choices[0].message.content

def goals(timestamp, products, industry, startup_fund, investors, strength, audience):
    goal= f""" Create an interactive timeline dependent on the timestamp given, {timestamp}, and suggest and create goals and milestones.
               The timestamp is the timestamp of when the startup can successfully take off. 
               Suggested goals and/or milestones should include, but is not limited to: successful deployment, customer base milestone, etc you can think of. 
                Other variables you have and should consider when creating milestones to reach goals are: 
                The products/business they sell/develop: {products}
                The industry they are in: {industry}
                Whether or not they have a startup_fund or investors. If they have a startup_fund, it's {startup_fund}. 
                If they have investors: {investors}
                The strength of their product: {strength}
                And their target audience: {audience}
                
                Please create the goals in two ways: 
                First a Report, with each section separated by two new lines using this Format:
                
                (Make sure that when it is all generated, it is in a human readable form and looks readable)
                (HEADING 1 AND HEADING 2's ARE FORMATTING GUIDANCE)
                (UNDER NO CIRCUMSTANCES WILL YOU GENERATE ANY SORT OF CONCLUSION!)
                
                1. OVERALL GOAL AND TIMEFRAME (HEADING 1): 
                ( goal and timeframe )
                  
                
                2. MILESTONES AND GOALS (HEADING 1): (sort by ability to complete and urgency)
                    i) MILESTONE 1: (title, HEADING 2)
                    
                        Goal:
                        
                        Actions: (bullet points and by order)

                        Extra information:(To help achieve, if none, just type N/A)

                        Resources: (What is needed to be able to complete this milestone, such as budget, events to hold, finding investory etc etc, and/or anything else relevant)

                        Effects:(What accomplishing this milestone would benefit the startup)
                        
                        
                    ii) MILESTONE 2: (title, HEADING 2)
                    
                        (same as MILESTONE 1)
                        
                        
                    (Keep on generating milestones with numering using roman numerals, and formatted of each milestones following MILESTONE 1)
                
                (End each milestone section with a pretty line)
                
                    
                
            """

    goal = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {"role": "system", "content":"You are a well-renowned consultant for businesses and startups and have incredibly prodigious business sense, you also have incredibly acute future-sense and can be considered a prodigious actuarist. "},
          {"role":"user", "content":goal}
      ],
    )
    goal_timeline = goal.choices[0].message.content
    return goal_timeline
    
def Opportunities(products, industry, strength, audience, country): 
    steeple = f"""Conduct a STEEPLE analysis (Social, Technological, Economic, Environmental, Political, Legal, Ethical) to identify 
                  potential opportunities and risks for this startup in the {industry} industry, located in {country}. 
                  The startup's products are {products}, with the following strengths: {strength}. 
                  Their target audience includes {audience}, and the goal is to get products off the ground within {timestamp}.
                  
                  Consider how these factors could influence the startup's growth and success, color code them such that the headings displayed in colors relaying the urgency of each bullet point. 
                  Provide concise insights under each STEEPLE category, with actionable opportunities where possible. 
                  Highlight any trends, favorable policies, or technologies that the startup could leverage for competitive advantage.
                  (DO NOT WRITE A CONCLUSION, NO MATTER UNDER WHAT CIRCUMSTANCES, NO CONCLUSION AT THE END) 
                  (REMEMBER THAT PLACES WITH (NEWLINE) SHOULD BE REMEMBERED TO HAVE A NEW LINE)
                  
                  Formatting should be like this: 
                  (TITLE)
                  (Heading, this is format guidance, heading word should not be written out) SOCIAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                                 (NEWLINE) 
                                 
                  (Heading) TECHNOLOGICAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                               (NEWLINE)  
                                
                  (Heading) ECONOMICAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                                 (NEWLINE) 
                                 
                  (Heading) ENVIRONMENTAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                                 (NEWLINE) 
                                 
                  (Heading) POLITICAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                                 (NEWLINE) 
                                 
                  (Heading) LEGAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                                 (NEWLINE) 
                                 
                  (Heading) ETHICAL: 
                  (bullet points) Opportunities:
                                  (2 bullet points) (content)
                  
                  (bullet points) Risks:
                                  (2 bullet points) (content)
                  
                """

    Opp = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {"role": "system", "content":"You are a well-renowned consultant for businesses and startups and have incredibly prodigious business sense, you also have incredibly acute future-sense and can be considered a prodigious actuarist. "},
          {"role":"user", "content":steeple}
      ],
    )
    Steeple_opp = Opp.choices[0].message.content
    return Steeple_opp



# def Marketing(products, industry, strength, country, timestamp, audience):
    # strat = """Create a marketing strategy for a startup in the {industry} industry in {country}, focusing on the 4Ps: Product, Price, Place, and Promotion. 
    #           The startup's products include {products} with strengths like {strength}. Their target audience is {target audience}, and they aim to launch within {timestamp}.
    #               
    #               Outline specific strategies for each of the 4Ps:
    #               Product: Describe how the products should be positioned to highlight their unique strengths.
    #               Price: Suggest pricing strategies to appeal to the target audience.
    #               Place: Recommend distribution channels and regions that align with the audience demographics.
    #               Promotion: Propose effective promotional tactics that will resonate with the target audience, considering their preferences and media habits."""


# def Networking(products, investors, country, industry, startup_fund, audience):   


TabA, TabB, TabC = st.tabs(["Timeline", "Business Model", "Opportunities"])

with TabA: 
    generated_goals = goals(timestamp, products, industry, startup_fund, investors, strength, audience)
        
    st.write(generated_goals)
        
    milestones = generated_goals.split("\n\n")
    # if st.button("Generate Timeline"):
    #     generated_goals = goals(timestamp, products, industry, startup_fund, investors, strength, audience)
        
    #     st.write(generated_goals)
        
    #     milestones = generated_goals.split("\n\n")
        
    #     # Display Overall Goal and Timeframe
    #     # st.write("# Overall Goal and Timeframe")
    #     # st.write(milestones[0])
    #     # st.write(milestones[1])
    #     # st.write(milestones[2])

    #     # # Display each milestone in an expander for readability
    #     # # for i, milestone in enumerate(milestones[1:], start=3):  # Skip the first one which is the Overall Goal
    #     # #     with st.expander(f"Milestone {i} "):
    #     # #         st.write(milestone)
                
    #     # n = len(milestones)
        
    #     # for i in range(3, n, int((n-2)/7)): #start with index 3, across whole length, iterate every 6 indexes?
    #     #     milestone_title = f"Milestone {i//6 + 1}"  # Calculating milestone number i = 3
    #     #     print(i)
    #     #     print(len(milestones))
    #     #     with st.expander(milestone_title):
    #     #         for j in range(7): 
    #     #             st.write(milestones[j+i]) #j=1, i 
    #     #             print(j+i)
        
        
        
    #     #[3] = actions 

with TabB:
    progress_text = "Generating... Please wait."
    my_bar = st.progress(0, text=progress_text)

    loadingBar()
        
    business_model = (genModel(products, industry, audience))
        
    categories = business_model.split("\n\n")
        
    st.write(categories[0])
        # with st.expander(st.header("Value Propositions")):
        #     st.write(categories[0])

    with st.expander("Revenue Model"):
            st.write(categories[2])

    with st.expander("Customer Segment"):
            st.write(categories[4])

    with st.expander("Infrastructure"):
            st.write(categories[6])
    # if st.button("Generate"):
        
    #     progress_text = "Generating... Please wait."
    #     my_bar = st.progress(0, text=progress_text)

    #     loadingBar()
        
    #     business_model = (genModel(products, industry, audience))
        
    #     categories = business_model.split("\n\n")
        
    #     st.write(categories[0])
    #     # with st.expander(st.header("Value Propositions")):
    #     #     st.write(categories[0])

    #     with st.expander("Revenue Model"):
    #         st.write(categories[2])

    #     with st.expander("Customer Segment"):
    #         st.write(categories[4])

    #     with st.expander("Infrastructure"):
    #         st.write(categories[6])

with TabC: 
        opps = Opportunities(products, industry, strength, audience, country)
        # loadingBar()
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        
        # with st.spinner("Generating..."):
        #     time.sleep(2)
        
        steeple = opps.split("\n\n")
        
        # st.write(opps)
        

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["SOCIAL", "TECHNOLOGICAL", "ECONOMICAL", "ENVIRONMENTAL", "POLITICAL", "LEGAL", "ETHICAL"])
        
        
        with tab1:
            st.header("SOCIAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[1])
            container.write(steeple[2])
        
        with tab2:
            st.header("TECHNOLOGICAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[3])
            container.write(steeple[4])
            
        with tab3:
            st.header("ECONOMICAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[5])
            container.write(steeple[6])
            
        with tab4:
            st.header("ENVIRONMENTAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[7])
            container.write(steeple[8])
            
        with tab5:
            st.header("POLITICAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[9])
            container.write(steeple[10])
            
        with tab6:
            st.header("LEGAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[11])
            container.write(steeple[12])
            
        with tab7:
            st.header("ETHICAL")
            container = st.container(height = 500, border=True)
            container.write(steeple[13])
            container.write(steeple[14])



       






