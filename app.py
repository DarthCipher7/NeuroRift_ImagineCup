import streamlit as st
import json
import pandas as pd
import os

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Neuro Rift: Aura", 
    page_icon="🧠", 
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS to make it look cleaner (Hides default Streamlit menu)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {background-color: #fafafa;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOAD DATA ---
@st.cache_data # Caches data so it doesn't reload on every click
def load_data():
    try:
        # Looks for the file in data/mock_db.json
        with open(os.path.join("data", "mock_db.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ Error: 'data/mock_db.json' not found. Please check your folder structure.")
        return {}

data = load_data()

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("Neuro Rift: Aura 🧠")
st.sidebar.caption("Predictability = Peace")

page = st.sidebar.radio(
    "Navigate", 
    ["Home", "Sensory Forecast", "Live Scanner", "Profile & Settings"]
)

st.sidebar.divider()
st.sidebar.info("Developed for Microsoft Imagine Cup")

# --- PAGE 1: HOME ---
if page == "Home":
    st.title("Welcome to Aura")
    st.image("https://images.unsplash.com/photo-1493612276216-ee3925520721?w=800", caption="Find your quiet space.")
    
    st.markdown("""
    ### Predictability is Power.
    **Aura** empowers neurodivergent individuals to navigate the world with confidence.
    
    #### What would you like to do?
    * **📅 Plan Ahead:** Check the **Sensory Forecast** to avoid crowds.
    * **📷 Check Now:** Use the **Live Scanner** to analyze your current room.
    * **⚙️ Customize:** Set your triggers in **Profile**.
    """)
    
    if st.button("Start Planning Trip"):
        st.info("👈 Click 'Sensory Forecast' in the sidebar!")

# --- PAGE 2: FORECAST (The Core Feature) ---
elif page == "Sensory Forecast":
    st.title("📅 Venue Forecast")
    
    if not data:
        st.warning("No data found. Please add mock_db.json.")
    else:
        # Selection
        venue = st.selectbox("Select Venue", list(data.keys()))
        venue_data = data[venue]
        
        # 1. THE CHART
        times = list(venue_data.keys())
        crowd_levels = [d["crowd"] for d in venue_data.values()]
        
        st.subheader(f"Sensory Load: {venue}")
        chart_data = pd.DataFrame({"Time": times, "Sensory Load": crowd_levels})