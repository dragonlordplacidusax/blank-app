# app.py

import streamlit as st
import pandas as pd

# --- App Configuration ---
# The default theme will be used, which respects system settings (including dark mode).
st.set_page_config(
    page_title="Climate Action AI | Your Guide to a Greener Planet",
    page_icon="🌍",
    layout="centered"
)

# --- Header ---
st.title("Climate Action AI 🌍")
st.markdown("Your personal guide to making a tangible, positive impact on the environment.")
st.divider()

# --- Main Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "💡 AI for Climate Action", 
    "📸 Eco-Scanner",
    "🏘️ Local Action Hub",
    "📚 Sustainable Living Hub"
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
    
    # Corrected dictionary without syntax errors
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
    # Corrected st.info call without invalid characters
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

# --- Footer ---
st.sidebar.header("About Climate Action AI")
st.sidebar.info("""
This app is a concept designed to empower individuals and communities to take meaningful climate action. By providing personalized insights and fostering local connections, we can build a more sustainable future together.
""")
