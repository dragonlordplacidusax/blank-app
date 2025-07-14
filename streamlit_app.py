# app.py

import streamlit as st

# --- App Configuration ---
st.set_page_config(
    page_title="Climate Action AI | Your Guide to a Greener Planet",
    page_icon="🌍",
    layout="centered"  # Use centered layout for a cleaner feel on wide screens
)

# --- Custom CSS for subtle enhancements ---
st.markdown("""
<style>
    /* A more subtle background color */
    .stApp {
        background-color: #F7F7F7;
    }
    
    /* Custom title styling */
    h1 {
        color: #1a1a1a;
        font-weight: 700;
        text-align: center;
    }

    h2 {
        color: #333333;
    }

    /* Style for the containers */
    .st-emotion-cache-1jicfl2 {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --- Header ---
st.title("Climate Action AI 🌍")
st.markdown("<p style='text-align: center; color: #555;'>Your personal guide to making a tangible, positive impact on the environment.</p>", unsafe_allow_html=True)
st.divider()

# --- Main Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "💡 AI for Climate Action", 
    "📸 Eco-Scanner",
    "🏘️ Local Action Hub",
    "🏆 Collective Challenges"
])

# --- Tab 1: AI for Climate Action ---
with tab1:
    st.header("How AI Fuels Climate Solutions")
    st.write("Artificial Intelligence is a powerful tool in fighting climate change. It helps us understand complex systems, accelerate innovation, and build resilience.")
    
    with st.container(border=True):
        st.subheader("Optimizing Global Systems")
        st.write("""
        - **Energy Grids:** AI improves grid stability by forecasting power demand.
        - **Transportation:** AI-powered route planning reduces fuel consumption.
        - **Smart Agriculture:** AI helps optimize irrigation and reduce fertilizer use.
        """)
    
    st.write("") # Add some space

    with st.container(border=True):
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
    
    with st.container(border=True):
        st.subheader("📦 Product & Barcode Scanner")
        st.write("Scan a product's barcode to get a sustainability score and find eco-friendly alternatives.")
        barcode = st.text_input("Enter a product barcode:", key="barcode_scanner")
        if barcode:
            st.success(f"**Product Score (Barcode: {barcode}): 72/100**")
            st.info("Tip: Consider brands with fully recyclable packaging or refill options.")

    st.write("")

    with st.container(border=True):
        st.subheader("🧾 Utility Bill Analyzer")
        st.write("Upload a photo of your utility bill to get personalized savings tips.")
        uploaded_bill = st.file_uploader("Upload your bill (PNG, JPG)", type=["png", "jpg"], key="bill_uploader")
        if uploaded_bill:
            st.warning("**Analysis:** Your usage is 15% higher than similar homes. Consider unplugging devices on standby.")

# --- Tab 3: Local Climate Action Hub ---
with tab3:
    st.header("Hyper-Local Climate Action")
    st.write("Find local centers, volunteer events, and advocacy tools to make a difference in your community.")

    with st.container(border=True):
        st.subheader("📍 Interactive Action Map")
        st.write("Find local sustainable services (simulated list):")
        st.info("**Recycling Center:** 123 Green Way, M-F 9am-5pm")
        st.info("**Compost Drop-off:** City Park (Saturdays only)")

    st.write("")

    with st.container(border=True):
        st.subheader("🤝 Community Project Connector")
        st.write("Find and join local volunteer events:")
        st.checkbox("Tree Planting Day: July 20th", key="event1")
        st.checkbox("Park Clean-up Crew: August 5th", key="event2")
        if st.button("Join Selected Events", use_container_width=True):
            st.success("You've signed up! We'll send you a reminder.")

# --- Tab 4: Collective Challenges ---
with tab4:
    st.header("Collective Climate Challenges")
    st.write("Join with friends, participate in challenges, and track your collective impact.")

    with st.container(border=True):
        st.subheader("🎯 Team-Based Goals")
        team_name = st.text_input("Create or join a team:")
        if team_name:
            st.write(f"Welcome, **{team_name}**!")
            challenge = st.selectbox("Current Challenge:", ["Plastic-Free July", "Bike-to-Work Month", "Meatless Mondays"])
            progress_val = st.slider(f"Log your team's '{challenge}' progress:", 0, 100, 25)
            st.metric(label="Team Progress", value=f"{progress_val}%")

    st.write("")

    with st.container(border=True):
        st.subheader("🌳 Community Milestones")
        st.write("City-Wide Goal: **Plant 10,000 Trees**")
        st.progress(67, text="6,700 / 10,000 trees planted")
        st.write("Your actions contribute to a larger goal, making a real-world impact!")


# --- Footer ---
st.sidebar.header("About Climate Action AI")
st.sidebar.info("""
This app is a concept designed to empower individuals and communities to take meaningful climate action. By providing personalized insights and fostering local connections, we can build a more sustainable future together.
""")
