# AI Autonomous Product Manager

## Overview

AI Autonomous Product Manager is an AI system that simulates the role of a Product Manager.

The system analyzes customer feedback, identifies product improvement opportunities, estimates business impact, and generates a product roadmap.

## Features

- User feedback analysis
- AI-generated product features
- Feature impact scoring
- Product roadmap generation
- Strategy report generation
- Streamlit interactive dashboard

## Tech Stack

Python  
CrewAI / Agent-based architecture  
Groq LLM (LLaMA 3)  
Pandas  
Streamlit  

## System Architecture

User Feedback → Feedback Analyzer → Feature Planner → Impact Estimator → Roadmap Planner → Strategy Report

## How to Run

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

## Example Output

The system generates:

• Feature improvement suggestions  
• Impact analysis  
• Product roadmap  
• Strategic product recommendations  

## Project Structure

agents/
feedback_agent.py  
feature_agent.py  
impact_agent.py  
roadmap_agent.py  

data/
sample_feedback.csv  

app.py  
main.py  
