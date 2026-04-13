import streamlit as st
from src.model import train_model
from src.agents import financial_decision
from src.rag import load_knowledge, build_index, retrieve

# Train model once
train_model()

st.title("💼 AI Personal CFO - Financial Decision System")

income = st.number_input("Monthly Income", value=60000)
expenses = st.number_input("Monthly Expenses", value=30000)

query = st.text_input("Ask Financial Question")

if st.button("Analyze Finance"):
    
    savings, risk, advice = financial_decision(income, expenses)
    
    st.subheader("📊 Financial Analysis")
    st.write(f"Predicted Savings: {savings:.2f}")
    st.write(f"Risk Level: {risk}")
    st.write(f"Advice: {advice}")
    
    # RAG Insights
    docs = load_knowledge()
    index = build_index(docs)
    
    if query:
        insights = retrieve(query, docs, index)
        
        st.subheader("🔎 Financial Insights")
        for i in insights:
            st.write(i)