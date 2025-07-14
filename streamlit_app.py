# app.py

import streamlit as st

# --- App Configuration ---
st.set_page_config(
    page_title="Climate Action AI | Your Guide to a Greener Planet",
    page_icon="🌍",
    layout="wide"
)

# --- Custom CSS for a Modern UI ---
# Inspired by the clean, card-based layouts from easyui.pro
st.markdown("""
<style>
    /* Main container and text styling */
    .stApp {
        background-color: #F0F2F6;
    }
    
    /* Custom title styling */
    h1 {
        color: #1a1a1a;
        font-weight: 700;
    }

    /* Custom styling for tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF;
    }

    /* Card-like containers for features */
    .st-emotion-cache-1r4qj8v {
        border: 1px solid #E0E0E0;
        border-radius: 10px;
        padding: 20px;
        background-color: #FFFFFF;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: box-shadow 0.3s ease-in-out;
    }
    .st-emotion-cache-1r4qj8v:hover {
        box-shadow: 0 8px 12px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 8px;
        background-color: #0068C9;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0055A4;
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)


# --- Header ---
st.title("Climate Action AI 🌍")
st.markdown("Welcome to your personal guide for making a tangible impact. This app uses AI and community power to help you take meaningful steps towards a sustainable future.")


# --- Main Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "💡 AI for Climate Action", 
    "📸 Eco-Scanner",
    "🏘️ Local Action Hub",
    "🏆 Collective Challenges"
])

# --- Tab 1: AI for Climate Action ---
with tab1:
    st.header("How AI is Fueling Climate Solutions")
    st.markdown("Artificial Intelligence is a key tool in fighting climate change. It helps us understand complex systems, speed up innovation, and build resilience.")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.subheader("Optimizing Global Systems")
            st.write("""
            - **Energy Grids:** AI improves grid stability by forecasting power demand and optimizing renewable energy sources.
            - **Transportation:** AI-powered route planning reduces fuel consumption and emissions.
            - **Smart Agriculture:** AI helps optimize irrigation and reduce fertilizer use, lowering the food supply's carbon footprint.
            """)
    with col2:
        with st.container():
            st.subheader("Accelerating Discovery & Resilience")
            st.write("""
            - **Innovation:** AI is used to discover new, sustainable materials and technologies to meet net-zero goals.
            - **Early Warnings:** AI models predict extreme weather events, enabling better disaster management.
            - **Conservation:** AI analyzes drone and satellite imagery to monitor deforestation and protect endangered species.
            """)

# --- Tab 2: Eco-Scanner ---
with tab2:
    st.header("Eco-Scanner: AI-Powered Environmental Insights")
    st.markdown("Use your camera to get instant sustainability insights. *Note: This is a conceptual demo.*")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container():
            st.subheader("📦 Product Scanner")
            st.write("Scan a barcode for a sustainability score.")
            barcode = st.text_input("Enter a product barcode:", key="barcode_scanner")
            if barcode:
                st.success(f"Score: 72/100")
                st.info("Tip: Choose brands with recyclable packaging.")
    with col2:
        with st.container():
            st.subheader("🧾 Bill Analyzer")
            st.write("Upload a utility bill for savings tips.")
            uploaded_bill = st.file_uploader("Upload a photo of your utility bill", type=["png", "jpg"], key="bill_uploader")
            if uploaded_bill:
                st.warning("Analysis: Your usage is 15% above average. Unplug standby devices.")
    with col3:
        with st.container():
            st.subheader("🍎 Food Waste Assistant")
            st.write("Get recipes for leftover food items.")
            food_item = st.text_input("Enter a food item:", key="food_assistant")
            if food_item:
                st.success(f"Try roasted {food_item} or a {food_item} salad.")

# --- Tab 3: Local Climate Action Hub ---
with tab3:
    st.header("Hyper-Local Climate Action Hub")
    st.markdown("Find local centers, events, and tools to make a difference in your community.")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.subheader("📍 Interactive Action Map")
            st.write("Find local sustainable services (simulated):")
            st.info("**Recycling Center:** 123 Green Way, M-F 9am-5pm")
            st.info("**Compost Drop-off:** City Park (Saturdays only)")
            st.info("**Farmers' Market:** Town Square, Sundays 8am-1pm")
    with col2:
        with st.container():
            st.subheader("🤝 Community Project Connector")
            st.write("Find and join local volunteer events:")
            st.checkbox("Tree Planting Day: July 20th", key="event1")
            st.checkbox("Park Clean-up Crew: August 5th", key="event2")
            st.checkbox("Community Garden Workshop: August 15th", key="event3")
            
    with st.container():
        st.subheader("✍️ Local Policy Advocacy")
        st.write("Use this template to write to local representatives.")
        letter = st.text_area("Draft your letter:", "Dear Representative,\n\nI am writing to urge you to support stronger local policies for renewable energy and waste reduction.\n\nSincerely,\nA Concerned Citizen")
        if st.button("Send Letter (Simulated)"):
            st.success("Thank you for your advocacy!")

# --- Tab 4: Collective Challenges ---
with tab4:
    st.header("Collective Climate Challenges")
    st.markdown("Join with friends, participate in challenges, and track your collective impact.")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.subheader("🎯 Team-Based Goals")
            team_name = st.text_input("Create or join a team:")
            if team_name:
                st.write(f"Welcome, **{team_name}**!")
                challenge = st.selectbox("Current Challenge:", ["Plastic-Free July", "Bike-to-Work Month"])
                progress_val = st.slider(f"Log your team's '{challenge}' progress:", 0, 100, 25)
    with col2:
        with st.container():
            st.subheader("🌳 Community Milestones")
            st.write("City-Wide Goal: **Plant 10,000 Trees**")
            st.progress(67, text="6,700 / 10,000 trees planted")
            
    with st.container():
        st.subheader("AR Visualization (Concept)")
        st.write("Imagine pointing your phone at a park and seeing a virtual forest representing all the trees we've planted together!")
        st.image("https://i.imgur.com/8FPomi5.png", caption="AR feature would show the virtual trees your actions helped plant.")

# --- Footer ---
st.sidebar.header("About Climate Action AI")
st.sidebar.info("""
This app is a concept designed to empower individuals and communities to take meaningful climate action. By providing personalized insights and fostering local connections, we can build a more sustainable future together.
""")
