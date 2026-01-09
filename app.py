# --- PAGE 2: FORECAST ---
elif page == "Sensory Forecast":
    data = load_data()
    st.title("📅 Venue Forecast")
    
    venue = st.selectbox("Select Venue", list(data.keys()))
    venue_data = data[venue]
    
    # 1. THE CHART
    times = list(venue_data.keys())
    crowd_levels = [d["crowd"] for d in venue_data.values()]
    
    st.subheader("Sensory Load Over Time")
    chart_data = pd.DataFrame({"Time": times, "Sensory Load": crowd_levels})
    st.area_chart(chart_data.set_index("Time"), color="#FF4B4B") # Red area chart looks more "medical/serious"
    
    # 2. THE DETAILS
    st.divider()
    st.subheader("🕒 Planning Assistant")
    time = st.select_slider("When do you want to visit?", options=times)
    details = venue_data[time]
    
    # Row 1: The Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Crowd Density", f"{details['crowd']}%")
    c2.metric("Noise Level", details['noise'])
    c3.metric("Lighting", details['light'])
    
    # Row 2: The Specifics (New Data)
    st.write("") # Spacer
    c4, c5 = st.columns(2)
    
    # Logic for Quiet Zones
    if details['quiet_zone'] != "None":
        c4.success(f"✅ **Quiet Zone Available:** {details['quiet_zone']}")
    else:
        c4.error("❌ **No Quiet Zones Available**")
        
    # Logic for Triggers
    if details['trigger'] != "None":
        c5.warning(f"⚠️ **Potential Trigger:** {details['trigger']}")
    else:
        c5.info("✨ No specific triggers predicted")

    # 3. THE VERDICT
    st.divider()
    if details['noise'] in ["High", "Very High", "Extreme"] or details['crowd'] > 70:
        st.error(f"🔴 **VERDICT: OVERWHELMING.** The {details['trigger']} causes high sensory stress.")
    else:
        st.success("🟢 **VERDICT: SAFE.** Good time to visit.")