# app.py

import streamlit as st

# --- App Configuration ---
st.set_page_config(
    page_title="F1's Race to Zero: The AI-Powered Climate Initiative",
    page_icon="🏎️",
    layout="wide"
)

# --- Header ---
st.title("F1's Race to Zero: The AI-Powered Climate Initiative 🏎️")
st.markdown("""
Welcome to the central hub for tracking the intersection of **Formula 1**, **Artificial Intelligence**, and **Climate Action**. 
This initiative showcases how cutting-edge technology from the racetrack can pioneer sustainable solutions for our planet.
""")

# --- Main Tabs ---
tab1, tab2, tab3 = st.tabs(["AI for Climate Action", "F1's Sustainability Journey", "The AI-F1 Tech Synergy"])

with tab1:
    st.header("How AI is Fueling Climate Solutions")
    st.markdown("""
    Artificial Intelligence is a powerful tool in the fight against climate change. It helps us understand complex environmental systems, accelerate innovation, and build resilience.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Optimizing Global Systems")
        st.write("""
        - **Energy Grids:** AI improves grid stability by forecasting power demand and optimizing the deployment of renewables like solar and wind.
        - **Transportation:** AI-powered route planning reduces fuel consumption and emissions.
        """)

    with col2:
        st.subheader("Accelerating Discovery & Resilience")
        st.write("""
        - **Innovation:** AI is used to discover new, sustainable materials and technologies required to meet net-zero goals.
        - **Early Warnings:** AI models process satellite imagery and sensor data to predict extreme weather events, enabling proactive disaster management.
        """)

with tab2:
    st.header("F1's Road to Net Zero")
    st.markdown("""
    Formula 1 has committed to being Net Zero Carbon by 2030. This ambitious goal relies on innovation in fuels, logistics, and operations.
    """)
    
    st.subheader("Key Milestones")
    st.write("""
    - **2026:** Introduction of 100% sustainable fuels for all F1 cars.
    - **Logistics Overhaul:** Reducing emissions from transport, which accounts for nearly half of F1's carbon footprint.
    - **Renewable Energy:** Promoting the use of renewable energy to power events.
    """)
    
    st.subheader("Carbon Footprint Reduction")
    st.write("F1 reduced its carbon footprint by 13% between 2018 and 2022.")
    st.progress(13, text="Progress towards 2030 Net-Zero Goal")

with tab3:
    st.header("The Tech Synergy: AI in F1")
    st.markdown("""
    AI is not just a future concept in F1; it's a critical part of modern racing, driving performance from the factory to the finish line.
    """)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("On-Track Strategy")
        st.write("""
        - **Real-Time Decisions:** AI analyzes live data to predict tire wear, fuel usage, and competitor strategies.
        - **Simulation Power:** Teams run thousands of race simulations using AI to map out strategies before the race starts.
        """)

    with col2:
        st.subheader("Car Design and Development")
        st.write("""
        - **Aerodynamic Perfection:** AI accelerates Computational Fluid Dynamics (CFD) simulations to perfect car design.
        - **Sustainable Engineering:** AI also helps optimize for sustainability by analyzing material use and fine-tuning energy recovery systems.
        """)

# --- Footer ---
st.sidebar.header("About the Initiative")
st.sidebar.info("""
This app is a concept for an initiative that believes the same spirit of innovation that makes an F1 car fast can also help us accelerate the race against climate change.
""")
