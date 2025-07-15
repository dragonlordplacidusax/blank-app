# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- App Configuration ---
st.set_page_config(
    page_title="Project Evergreen | Your Guide to a Greener Planet",
    page_icon="🌍",
    layout="centered"
)

# --- Header ---
st.title("Project Evergreen 🌍")
st.subheader("AI for a Greener Tomorrow.")

st.markdown("""
**Project Evergreen** is a pioneering AI initiative dedicated to fostering a sustainable and resilient future. 
By harnessing the power of artificial intelligence, we translate complex climate data into clear, actionable insights for businesses, communities, and policymakers. 

Our mission is to cultivate a world that remains vibrant and thriving for generations to come, ensuring a green and prosperous planet for all.
""")
st.divider()

# --- Main Tabs ---
# Added a new tab for Citizen Science & Personal Tips
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 AI for a Greener Future", 
    "📸 Eco-Scanner",
    "🏘️ Local Action Hub",
    "📚 Sustainable Living Hub",
    "🔬 Citizen Science & Tips"
])

# --- Tab 1: AI for Climate Action ---
with tab1:
    st.header("How AI Fuels Climate Solutions")
    st.write("Artificial Intelligence is a powerful tool in fighting climate change. It helps us understand complex systems, accelerate innovation, and build resilience.")
    
    st.subheader("Optimizing Global Systems")
    st.write("""
    - **Energy Grids:** AI improves grid stability by forecasting power demand.
    - **Transportation:** AI-powered route planning reduces fuel consumption.
    - **Smart Agriculture:** AI helps optimize irrigation and reduce fertilizer use.
    """)
    
    st.subheader("Accelerating Discovery & Resilience")
    st.write("""
    - **Innovation:** AI is used to discover new, sustainable materials for net-zero goals.
    - **Early Warnings:** AI models predict extreme weather events for better disaster management.
    - **Conservation:** AI analyzes satellite imagery to monitor deforestation.
    """)

# --- Tab 2: Eco-Scanner ---
with tab2:
    st.header("Eco-Scanner: AI-Powered Insights")
    st.write("Use your camera to get instant sustainability insights. *Note: This is a conceptual demo.*")

    st.subheader("🍎 Food Waste Assistant")
    st.write("Get comprehensive recipe ideas to use up leftover food items and reduce waste.")
    food_item = st.text_input("Enter a food item (e.g., 'carrots', 'chicken', 'bread'):", key="food_assistant")
    
    if food_item.lower() == 'carrots':
        st.success("Recipe Idea: **Quick Carrot & Ginger Soup**")
        st.write("""
        - **Ingredients:** Leftover carrots, 1 onion, 1-inch piece of ginger, vegetable broth, olive oil.
        - **Method:** Sauté chopped onion and grated ginger in oil. Add chopped carrots and cover with broth. Simmer until carrots are soft, then blend until smooth. Season with salt and pepper.
        """)
    elif food_item.lower() == 'chicken':
        st.success("Recipe Idea: **Leftover Chicken Salad Sandwich**")
        st.write("""
        - **Ingredients:** Cooked chicken (shredded), mayonnaise or Greek yogurt, celery (chopped), salt, pepper, bread.
        - **Method:** Mix shredded chicken with mayo/yogurt and chopped celery. Season to taste. Serve on bread or with crackers.
        """)
    elif food_item.lower() == 'bread':
        st.success("Recipe Idea: **Simple Bread Pudding**")
        st.write("""
        - **Ingredients:** Stale bread (cubed), 2 eggs, 1 cup milk, 1/4 cup sugar, vanilla extract, cinnamon.
        - **Method:** Whisk eggs, milk, sugar, and vanilla. Pour over bread cubes in a baking dish. Sprinkle with cinnamon. Bake at 180°C (350°F) for 30-40 minutes until set.
        """)
    elif food_item:
        st.info(f"No specific recipe for '{food_item}' yet, but consider adding it to a general stir-fry, soup, or omelette!")

    st.subheader("📦 Product & Barcode Scanner")
    st.write("Scan a product's barcode to get a sustainability score.")
    barcode = st.text_input("Enter a product barcode:", key="barcode_scanner")
    if barcode:
        st.success(f"**Product Score (Barcode: {barcode}): 72/100**")
        st.info("Tip: Consider brands with fully recyclable packaging or refill options.")

# --- Tab 3: Local Action Hub ---
with tab3:
    st.header("Hyper-Local Climate Action")
    st.write("Find local centers, volunteer events, and advocacy tools to make a difference in your community.")

    st.subheader("🤝 Eco-Volunteering in Dubai")
    st.write("Find and join local environmental volunteer events. *Details are based on available information and may change.*")
    
    opportunities = {
        'Event/Opportunity': [
            "Sprint for Change: Ecyclex Recycling Facility",
            "Clean UAE Campaign",
            "UAE Dolphin Project Volunteering",
            "Emirates Nature-WWF Cleanups",
        ],
        'Date(s)': [
            "19 July 2025",
            "5-14 December 2025",
            "Ongoing",
            "Various",
        ],
        'Location': [
            "Dubai",
            "UAE-wide",
            "UAE",
            "UAE (various sites)",
        ],
        'Contact/Details': [
            "Visit leadersofchange.ae",
            "Register via Emirates Environmental Group",
            "Email: sighting@uaedolphinproject.org",
            "Visit emiratesnaturewwf.ae",
        ]
    }
    df = pd.DataFrame(opportunities)
    st.table(df)
    st.info("You can often find more opportunities on platforms like **Volunteers.ae**.")

# --- Tab 4: Sustainable Living Hub ---
with tab4:
    st.header("Sustainable Living Hub")
    st.write("Practical guides and information to help you adopt a more sustainable lifestyle.")

    st.subheader("♻️ How to Set Up a Home Recycling System")
    st.write("""
    1.  **Check Local Rules:** Find out what materials your local municipality collects for recycling.
    2.  **Designate a Spot:** Choose a convenient location, like the kitchen or garage, for your recycling bins.
    3.  **Use Clear Bins:** Use separate, clearly labeled bins for different materials (e.g., paper, plastic/metal, glass).
    4.  **Clean & Dry:** Rinse food containers and let them dry before placing them in the bin to avoid contamination.
    5.  **Know What to Exclude:** Keep non-recyclable items like plastic bags, food waste, and electronics out of your recycling bins.
    """)

    st.subheader("👣 Understanding Your Carbon Footprint")
    st.write("""
    Your carbon footprint is the total amount of greenhouse gases generated by your actions.
    - **Primary Footprint:** Direct emissions from energy consumption (e.g., electricity, transportation).
    - **Secondary Footprint:** Indirect emissions from the lifecycle of products you use.
    
    **To reduce it, focus on:**
    - **Energy:** Use energy-efficient appliances and reduce heating/cooling.
    - **Transport:** Walk, cycle, or use public transport instead of driving.
    - **Diet:** Reduce consumption of red meat, as it has a high carbon footprint.
    """)

# --- Tab 5: Citizen Science & Personal Tips ---
with tab5:
    st.header("Citizen Science & Personal Tips")
    st.write("Contribute to real scientific research and get personalized tips to reduce your carbon footprint.")

    st.subheader("🌿 Report Local Environmental Observations")
    st.write("Help scientists by reporting floods, tracking local wildlife, or monitoring air quality.")
    observation_type = st.selectbox("Select observation type:", ["Flood", "Local Plants & Animals", "Air Quality"])
    observation_details = st.text_area("Describe your observation (e.g., location, time, details):")
    if st.button("Submit Observation"):
        if observation_details.strip():
            st.success(f"Thank you for submitting your {observation_type.lower()} observation! Your data helps power real-world climate solutions.")
        else:
            st.error("Please enter a description for your observation.")

    st.divider()

    st.subheader("👣 Personal Tips & Progress Tracker")
    st.write("Answer a few questions about your lifestyle to receive tailored tips and track your positive impact over time.")

    # Lifestyle questions for personalization
    reusable_bottle = st.checkbox("I regularly use a reusable water bottle.")
    thermostat_adjusted = st.checkbox("I adjust my thermostat to save energy (e.g., a few degrees cooler in winter, warmer in summer).")
    waste_reduction = st.checkbox("I actively try to reduce my household waste (e.g., through recycling, composting).")

    # Calculate a simple progress score
    progress_score = sum([reusable_bottle, thermostat_adjusted, waste_reduction])

    # Provide personalized tips
    tips = []
    if not reusable_bottle:
        tips.append("Switch to a reusable water bottle to significantly cut down on single-use plastic.")
    if not thermostat_adjusted:
        tips.append("Adjusting your thermostat by just a few degrees can lead to major energy savings over a year.")
    if not waste_reduction:
        tips.append("Start a simple recycling system at home for paper, plastic, and glass to reduce landfill waste.")

    st.write("#### Your Progress")
    st.write(f"You're currently practicing **{progress_score} out of 3** key sustainable habits. See your progress below!")

    if tips:
        st.write("#### Your Next Steps")
        for tip in tips:
            st.info(f"**Tip:** {tip}")
    else:
        st.success("Amazing work! You're already practicing all the tracked sustainable habits. Keep it up!")

    # Display progress with a simple chart
    labels = ['Reusable Bottle', 'Thermostat Adjusted', 'Waste Reduction']
    values = [reusable_bottle, thermostat_adjusted, waste_reduction]

    fig, ax = plt.subplots()
    bar_colors = ['#28a745' if v else '#6c757d' for v in values] # Green for implemented, Gray for not
    ax.bar(labels, [1]*len(values), color=bar_colors, width=0.6)
    
    ax.set_yticks([])
    ax.set_title('Your Sustainable Habits Progress', pad=20)
    fig.set_facecolor('#0e1117') # Match Streamlit's dark theme background
    ax.set_facecolor('#0e1117')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='x', colors='white')

    st.pyplot(fig)
