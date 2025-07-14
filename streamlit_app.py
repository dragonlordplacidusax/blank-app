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
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "AI for Climate Action", 
    "F1's Sustainability Journey", 
    "The AI-F1 Tech Synergy",
    "Eco-Scanner",
    "Local Climate Action Hub",
    "Gamified Challenges"
])

# --- Original Tabs ---

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

# --- New Feature Tabs ---

# Tab 4: Eco-Scanner
with tab4:
    st.header("Eco-Scanner: AI-Powered Environmental Insights")
    st.markdown("""
    Use your camera or upload images to get instant sustainability insights about products, bills, and food waste. *Note: This is a conceptual demo.*
    """)
    
    st.subheader("Product and Barcode Scanning")
    st.write("Simulate scanning a product barcode to get a sustainability score and eco-friendly alternatives.")
    barcode = st.text_input("Enter a product barcode to simulate scanning:")
    if barcode:
        st.success(f"Product Score (Barcode: {barcode}): **72/100**")
        st.info("Eco-Friendly Alternatives: Consider a brand with recyclable packaging or a concentrated refill option.")

    st.subheader("Utility Bill Analyzer")
    uploaded_bill = st.file_uploader("Upload a photo of your utility bill", type=["png", "jpg", "jpeg"])
    if uploaded_bill:
        st.success("Bill uploaded successfully!")
        st.write("Analyzing your usage patterns...")
        st.warning("**Analysis Result:** Your electricity usage is 15% higher than similar homes in your area. Consider unplugging devices on standby to reduce phantom load.")

    st.subheader("Food Waste Assistant")
    food_item = st.text_input("Enter a food item you need to use up (e.g., 'carrots', 'chicken'):")
    if food_item:
        st.success(f"Here are some recipe ideas to use your {food_item}:")
        st.write(f"- Roasted {food_item} with herbs\n- {food_item} and ginger soup\n- Shredded {food_item} salad")

# Tab 5: Local Climate Action Hub
with tab5:
    st.header("Hyper-Local Climate Action Hub")
    st.markdown("""
    Find local recycling centers, volunteer events, and advocacy tools to make a difference in your community.
    """)
    
    st.subheader("Interactive Action Map")
    st.write("This map would show local sustainable services. Below is a simulated list for demonstration:")
    
    # In a real app, this would be an interactive map using st.map()
    locations = [
        "**Recycling Center:** 123 Green Way, open M-F 9am-5pm",
        "**Compost Drop-off:** City Park, near the main entrance (Saturdays only)",
        "**Farmers' Market:** Town Square, Sundays 8am-1pm"
    ]
    for loc in locations:
        st.info(loc)

    st.subheader("Community Project Connector")
    st.write("Find and join local volunteer events:")
    events = ["Tree Planting Day: July 20th", "Park Clean-up Crew: August 5th", "Community Garden Workshop: August 15th"]
    for event in events:
        st.checkbox(event, key=event)

    st.subheader("Local Policy Advocacy")
    st.write("Use this template to write to local representatives about important climate issues.")
    letter = st.text_area("Draft your letter:", "Dear Representative,\n\nI am writing to urge you to support stronger local policies for renewable energy and waste reduction. Our community's future depends on it.\n\nSincerely,\nA Concerned Citizen")
    if st.button("Send Letter (Simulated)"):
        st.success("Thank you for your advocacy! Your letter has been sent.")

# Tab 6: Gamified Collective Challenges
with tab6:
    st.header("Gamified Collective Challenges")
    st.markdown("""
    Join with friends, participate in challenges, and track your collective impact on climate action.
    """)
    
    st.subheader("Team-Based Goals")
    team_name = st.text_input("Create or join a team:")
    if team_name:
        st.write(f"Welcome, **{team_name}**!")
        challenge = st.selectbox("Current Challenge:", ["Plastic-Free July", "Bike-to-Work Month", "Meatless Mondays"])
        progress_val = st.slider(f"Log your team's '{challenge}' progress:", 0, 100, 25)
        st.write(f"Your team has completed **{progress_val}%** of the '{challenge}' goal!")

    st.subheader("Community Milestones")
    st.write("City-Wide Goal: **Plant 10,000 Trees**")
    # This value would update in real-time in a live app
    st.progress(67, text="6,700 / 10,000 trees planted")
    
    st.subheader("Augmented Reality (AR) Visualization")
    st.write("Visualize the impact of our collective actions!")
    if st.button("See Our Forest Grow (AR Simulation)"):
        st.success("Imagine pointing your phone at a local park and seeing a virtual forest representing all the trees we've planted together!")
        st.image("https://i.imgur.com/8FPomi5.png", caption="This AR feature would show the virtual trees your actions helped plant.")

# --- Footer ---
st.sidebar.header("About This Initiative")
st.sidebar.info("""
This app is a concept demonstrating how the same spirit of innovation that makes an F1 car fast can help us accelerate the race against climate change.
""")
