import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import pages.Profile_Form as p
from datetime import datetime

# Load environment variables
load_dotenv()

HISTORY_FILE = "history_records.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)

def delete_record(index):
    history = load_history()
    if 0 <= index < len(history):
        history.pop(index)
        save_history(history)
        st.session_state['history'] = history  # Update session state to reflect deletion


if 'history' not in st.session_state:
    st.session_state['history'] = load_history()
    
def save_record(record):
    history = load_history()
    history.append(record)
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)

client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])


def Trend(industry, participants, country, products, strength, target_audience, timestamp, investor, funds):
    user_prompt1 = f'''I am a startup owner who own a {industry} project, that the project products is working like this: {products}. I am working {participants}. 
    I estimated the project will be landed in {country}. This is the strength of the product: {strength}. The product is targeting to {target_audience} category. 
    I estimated the product will be landed in {timestamp} and I {investor}. The amount of funds for the project is {funds}. '''
    
    user_prompt2 = f'''This is our product: {products}, and here is its strength: {strength}, and we are targeting to the {target_audience}. We plan to take 
    {timestamp} to launch the product.'''

    taba, tabb = st.tabs(["Trend_Analysis", "History"])

    with taba:
        if st.button("Start Generate"):
            tab1, tab2 = st.tabs(["Project Analysis", "Product Trend Prediction"])
    
            with tab1:
                st.header("Project Analysis")
                projectT = project(user_prompt1)
                st.write(projectT)

            with tab2:
                st.header("Product Trend Prediction")
                productT, reportT = product(user_prompt2)

                for v in productT['prediction']:
                    plt.plot(productT['year'], v['data_points'], label=v['name'])
                
                plt.legend()
                plt.xticks(rotation = 20)
                st.pyplot(plt)
                with st.expander("Detailed Report"):
                    st.write(reportT)

            timestamp = datetime.now().isoformat()
            record = {
                "timestamp": timestamp,
                "projectT": projectT,
                "productT": productT,
                "reportT": reportT
            }
            save_record(record)

    with tabb:
        st.header("History")
        history = load_history()
        for i, record in enumerate(history):
            col1, col2 = st.columns([4, 1])  # Two columns for record and delete button
            with col1:
                if st.button(f"View Record {i + 1} - {record['timestamp']}"):
                    tab1, tab2 = st.tabs(["Project Analysis", "Product Trend Prediction"])
        
                    with tab1:
                        st.header("Project Analysis")
                        projectH = (record["projectT"])
                        st.write(projectH)

                    with tab2:
                        st.header("Product Trend Prediction")
                        productH = (record["productT"])
                        reportH = (record["reportT"])

                        for v in productH['prediction']:
                            plt.plot(productH['year'], v['data_points'], label=v['name'])
                        
                        plt.legend()
                        plt.xticks(rotation = 20)
                        st.pyplot(plt)
                        with st.expander("Detailed Report"):
                            st.write(reportH)

            with col2:
                if st.button("Delete", key=f"delete_{i}"):
                    delete_record(i)
                
        
def project(user_prompt):
    system_prompt = """You are an experienced senior analyst on startup projects. 
        The aspect below is how you should mark the likelihood of the project: 
            1. If the project have investor, they will have a high posibility to able to publish and get success in the market.
            2. From their industry type, compare their strength with the others published or known industry of the country. After 
            comparing, you will need to list out what is their passion  and weakness comparing to the other market company.
            3. If their strength has never been seen in the market and will bring big moves to the market their posibility to success 
            is high.
            4. Analyze and predict if the target audience fit with the product and if they need it and will buy it?
            5. Analyze if the time they used to invest is too short or long. If the technology already been publish in the market, but 
            they still need a long time will down their success rate, and vice versa.
            6. Analyze and see if their funds is enough for them to complete their project? If no, tell them, they maybe lack of funds 
            during the invention and suggest them to find an investor.
            7. Analyze if they have members or if he is working alone? if they have members to help they will be more posibility to sucess.

        The analyzed report should be a summary report based on the aspects, please make it organize and look good to read.
        
        The report should include:
            1. Market and Industry Analysis
            Industry Trends: Overview of current industry trends and the startup’s position within those trends.
            Market Demand: Analysis of market demand for the product/service, including projected growth rates and target market demographics.
            Competitive Landscape: Examination of direct and indirect competitors, their strengths and weaknesses, and the startup's competitive edge or unique selling point (USP).
            2. Product/Service Viability
            Value Proposition: Clarity of the value the startup brings to its customers and how it solves a specific problem or fills a gap.
            Innovation and Differentiation: Analysis of how innovative or unique the product/service is and whether it provides something new to the market.
            Product-Market Fit: Evaluation of how well the product meets the needs and desires of the target market and if there is room for product adjustments.
            3. Business Model and Revenue Streams
            Revenue Model: Analysis of how the startup plans to generate revenue (e.g., subscriptions, sales, ads).
            Pricing Strategy: Assessment of pricing strategy and whether it aligns with market standards and profitability goals.
            Scalability: Evaluation of the startup’s potential to scale (e.g., expand to new markets or increase user base without proportional increases in costs).
            4. Financial Projections and Funding Requirements
            Initial Funding and Runway: Assessment of initial capital, current funding, and the startup’s financial runway.
            Revenue and Profit Projections: Financial forecasts, including projected revenue, expenses, and profit over time.
            Break-Even Analysis: Determination of when the startup expects to reach break-even and start making a profit.
            Investor Appeal: Potential appeal to investors, including returns on investment (ROI) and exit opportunities.
            5. Team Composition and Capabilities
            Founders’ Backgrounds: Skills, experience, and track records of the founders in relevant fields.
            Key Team Members: Strengths and expertise of key personnel and whether their combined skill set covers essential areas (technology, marketing, operations).
            Team Structure and Gaps: Analysis of team structure and identification of any critical skill or resource gaps that might need addressing.
            6. Technology and Operational Feasibility
            Technology Stack: Suitability and sustainability of the chosen technology stack (for tech startups).
            Operational Model: Feasibility of the operations strategy and whether it aligns with business goals and scalability.
            Product Development Roadmap: Timelines, milestones, and feasibility of the product development plan.
            7. Market Entry and Growth Strategy
            Go-to-Market (GTM) Strategy: Details on how the startup plans to launch and establish its product/service in the market.
            Marketing and Sales Channels: Chosen channels for marketing and sales, and their alignment with the target audience’s preferences.
            Customer Acquisition Cost (CAC): Estimated cost to acquire a new customer and comparison to expected customer lifetime value (CLTV).
            8. Risk Assessment and Mitigation Strategies
            Market Risks: Potential market changes, economic downturns, or changes in customer preferences.
            Operational Risks: Production, supply chain, and technology-related risks, and backup plans.
            Financial Risks: Cash flow risks, especially related to revenue variability, funding challenges, and unexpected expenses.
            Compliance and Regulatory Risks: Any legal or regulatory compliance risks associated with the industry or market.
            9. Sustainability and Long-Term Vision
            Sustainability Practices: Environmental, social, and governance (ESG) factors, especially if they impact market perception.
            Long-Term Growth Vision: Founders’ vision for growth, including potential for international expansion, diversification, and market adaptability.
            Exit Strategy: If relevant, potential exit strategies, such as acquisition, merger, or IPO, to appeal to investors.

    The format of the output should look like this:
        
        Title (underline and bold)
        space
        subtitle 1: (bold)
        horizontal line
        body text
        space
        subtitle 2: (bold)
        horizontal line
        body text
        ...
        Conclusion:(bold and underline)
        body

        
        """

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt + " Generate a report on the project analysis."},
        ]
    )
    return response.choices[0].message.content

def product(user_prompt2):
    system_prompt = """You are an experienced trend analyst. Analyze the product given and generate a report focusing on:
    1. Market presence of similar products.
    2. Predict the 5-year trend for startup product and the similar product. (if there is no similar products, just provide the sample data points for the startup product.)
    Then provide sample data points as [0, year_1, year_2, year_3, year_4, year_5] format.
    Generate the sample data points in json format but dont mention json in the output.
    the json out put should look like this:
        {"year": [year01, year02, year03, year04, year05],
        "prediction":[
            {
            "name": "startup_product",
            "data_points": [200,150,300,xx,xx]
            }
            {
            "name": "similar_product",
            "data_points": [200,150,300,xx,xx]
            }
        ]
        }
    I only need the sample data output
    """

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt2 },
        ]
    )
    
    #st.write(response.choices[0].message.content)
    sample_data_points = json.loads(response.choices[0].message.content)

    
    sys_prompt2 = f"""You are an experienced actural scientist, help me to generate the report of product trend report.
        This is the prediction we made on the product together with the similar product we found on the market {sample_data_points}.
        The output should include:
        1. Market Viability and Demand Analysis
        Target Audience Fit: Evaluate if the product aligns with the needs and preferences of the target audience.
        Market Demand Trends: Analyze how similar products have performed historically and predict future demand.
        Competitive Advantage: Highlight any unique features that differentiate it from competitors, indicating potential for market penetration.
        2. Projected Profit Timeline
        Break-Even Analysis: Estimate when the product will start generating profit based on cost, pricing strategy, and sales volume.
        Revenue Forecasting: Use projections to determine expected revenue milestones over time.
        3. Threats and Risk Mitigation
        Market Risks: Identify risks from market changes, competition, and customer behavior.
        Financial Risks: Assess the adequacy of funds and project cash flow issues that might arise.
        Operational Risks: Consider supply chain, production, or scalability issues.
        Risk Mitigation Strategies: Propose strategies to mitigate each identified risk, such as securing additional funding, contingency planning, or alternative revenue streams.
        4. Predictive Analysis and Accuracy
        Data-Driven Insights: Provide an analysis of prediction trends, noting any potential accelerators or decelerators for product success.
        Success Probability: Generate an estimated success percentage based on factors like product fit, market demand, and innovation level.
        Confidence Interval: Provide a percentage accuracy or confidence level for predictions based on available data and comparable market case studies.
        5. Strategic Recommendations
        Based on all above insights, provide actionable recommendations, such as product adjustments, target audience refinement, or adjustments in marketing strategy to maximize success chances.
        
        
        The format of the output should look like this:
        
        Title (underline and bold)
        space
        subtitle 1: (bold)
        body text
        space
        subtitle 2: (bold)
        body text
        ...
        Conclusion:(bold and underline)
        body
        """
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": sys_prompt2},
            {"role": "user", "content": user_prompt2 },
        ]
    )
    trend_report = response.choices[0].message.content

    return sample_data_points, trend_report
    
industry_option = "Retail & Consumer Goods"
business_type = "sole trader"
location = "Sabah"
products = "a coffee place that is wheelchair accessible and disability-friendly"
strength_bus = "Unique Selling Point is niche market, with penetrative pricing"
demographics = "Single Individuals"
target_date = "10 months"
finance = 'looking for an investor'
initial_funds = "20000" 

trend_analysis = Trend(st.session_state.industry_option, st.session_state.business_type, st.session_state.location, product, st.session_state.strength_bus, 
                       st.session_state.demographics, st.session_state.target_date, st.session_state.finance, st.session_state.initial_funds)
