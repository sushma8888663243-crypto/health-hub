import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Community Health Hub - Ambernath",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Glassmorphism Theme & UI Enhancement
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    .emergency-card {
        background: rgba(225, 29, 72, 0.2);
        border: 2px solid #f43f5e;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .role-badge {
        background: #0284c7;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION STATE INITIALIZATION (FIXED)
# ---------------------------------------------------------
if 'consultations' not in st.session_state:
    st.session_state.consultations = []
if 'feedbacks' not in st.session_state:
    st.session_state.feedbacks = []

# ---------------------------------------------------------
# 3. SIDEBAR - USER PROFILE & ROLE SELECTION
# ---------------------------------------------------------
with st.sidebar:
    st.title("👤 User Profile")
    user_name = st.text_input("Full Name", value="Prachi Gaikwad")
    user_age = st.number_input("Age", min_value=1, max_value=120, value=20)
    user_role = st.selectbox("Switch View Mode", ["Citizen", "Health Worker", "Admin"])
    st.markdown(f"Active View: <span class='role-badge'>{user_role}</span>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("📍 Location: Ambernath, Maharashtra")

# Top Navigation Bar
menu = ["🏠 Home", "🏥 Healthcare", "📅 Camps", "📱 Telemedicine", "💊 Medicines", "🤖 AI Assistant", "📊 Dashboard", "🚨 Emergency"]
choice = st.radio("Navigation Menu", menu, horizontal=True)

st.markdown("---")

# ---------------------------------------------------------
# MODULE 1: HOME
# ---------------------------------------------------------
if choice == "🏠 Home":
    st.title("🏥 Community Health Hub")
    st.subheader("Connecting communities with accessible healthcare.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🔍 Find Healthcare"): st.info("Navigate to 🏥 Healthcare section")
    with col2:
        if st.button("👨‍⚕️ Book Consultation"): st.info("Navigate to 📱 Telemedicine section")
    with col3:
        if st.button("📅 Health Camps"): st.info("Navigate to 📅 Camps section")
    with col4:
        if st.button("🚨 Emergency Help"): st.error("Emergency Section Triggered!")

    st.markdown("---")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Impact Overview")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("People Served", "1,248")
    m2.metric("Health Camps Held", "18")
    m3.metric("Consultations", "436")
    m4.metric("Communities Covered", "12")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 2: FIND HEALTHCARE
# ---------------------------------------------------------
elif choice == "🏥 Healthcare":
    st.title("🏥 Find Healthcare Facilities")
    search_q = st.text_input("Search Hospital, Doctor, or Pharmacy in Ambernath", placeholder="e.g., Primary Health Centre")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    hc1, hc2 = st.columns([3, 1])
    with hc1:
        st.markdown("### 🏥 Primary Health Centre (PHC)")
        st.markdown("📍 **Location:** Station Road, Ambernath West")
        st.markdown("🩺 **Services:** General Healthcare, Immunization, Maternal Care")
        st.markdown("🕐 **Timings:** 9:00 AM – 5:00 PM")
    with hc2:
        if st.button("View Details", key="phc1"):
            st.success("Facility Specs: 15 Beds, OPD Active, Emergency Response Unit")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    hc1, hc2 = st.columns([3, 1])
    with hc1:
        st.markdown("### 🏥 Central Municipal Hospital")
        st.markdown("📍 **Location:** Kansai Section, Ambernath East")
        st.markdown("🩺 **Services:** Emergency, Pediatrics, General Surgery")
        st.markdown("🕐 **Timings:** 24/7 Emergency Active")
    with hc2:
        if st.button("View Details", key="cmh1"):
            st.success("Facility Specs: 50 Beds, ICU Available, 2 Ambulances")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 3 & 5: CONSULTATION & TELEMEDICINE
# ---------------------------------------------------------
elif choice == "📱 Telemedicine":
    st.title("📱 Telemedicine & Online Consultations")
    st.caption("Need healthcare but can't travel?")
    
    t1, t2 = st.tabs(["👨‍⚕️ Book Consultation", "📤 Upload Reports"])
    
    with t1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        with st.form("book_form"):
            st.subheader("Consultation Booking Form")
            f_name = st.text_input("Name", value=user_name)
            f_age = st.number_input("Age", value=user_age)
            f_phone = st.text_input("Phone Number", "+91 ")
            f_service = st.selectbox("Select Service", ["General Physician", "Pediatrics", "Dermatology", "Gynaecology"])
            f_doctor = st.selectbox("Select Doctor/Health Worker", ["Dr. A. Sharma (General)", "Dr. P. Patil (Pediatrics)", "ASHA Supervisor Priya"])
            f_date = st.date_input("Preferred Date")
            f_time = st.time_input("Preferred Time")
            
            sub = st.form_submit_button("Submit Request")
            if sub:
                st.session_state.consultations.append({
                    "Name": f_name, "Age": f_age, "Phone": f_phone, "Service": f_service,
                    "Doctor": f_doctor, "Date": str(f_date), "Time": str(f_time)
                })
                st.success("✅ Consultation request submitted successfully.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with t2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Upload Clinical Diagnostic Reports")
        st.file_uploader("Upload Blood Test, X-Ray, or Prescription (PDF/PNG)", type=["pdf", "png", "jpg"])
        if st.button("Submit Report"):
            st.success("✅ Report uploaded and attached to your patient file.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 4: HEALTH CAMPS
# ---------------------------------------------------------
elif choice == "📅 Camps":
    st.title("📅 Upcoming Community Health Camps")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### Free Health Check-up Camp")
        st.markdown("📅 **Date:** 28 September 2026")
        st.markdown("📍 **Location:** Community Centre, Ambernath East")
        st.markdown("🩺 **Services:** BP check • Diabetes screening • General check-up")
        if st.button("Register for Camp 1"):
            st.success(f"✅ Registered {user_name} for Camp on 28 Sept 2026.")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### Maternal & Child Wellness Drive")
        st.markdown("📅 **Date:** 05 October 2026")
        st.markdown("📍 **Location:** Primary School Ground, Ambernath West")
        st.markdown("🩺 **Services:** Immunization • Nutrition counseling • Pediatric check")
        if st.button("Register for Camp 2"):
            st.success(f"✅ Registered {user_name} for Wellness Drive.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 6: MEDICINES
# ---------------------------------------------------------
elif choice == "💊 Medicines":
    st.title("💊 Nearby Pharmacies & Medicine Availability")
    st.caption("Sample availability records across local pharmacies.")
    
    med_data = pd.DataFrame({
        "Medicine": ["Paracetamol 500mg", "Amoxicillin 250mg", "Cetirizine 10mg", "ORSA Sachets", "Metformin 500mg"],
        "Availability": ["Available", "Limited", "Available", "Available", "Out of Stock"],
        "Pharmacy": ["ABC Pharmacy (West)", "XYZ Meds (East)", "Central Chemist", "ABC Pharmacy (West)", "Apex Pharma"],
        "Contact": ["+91 98220XXXXX", "+91 98330XXXXX", "+91 98110XXXXX", "+91 98220XXXXX", "+91 98440XXXXX"]
    })
    st.table(med_data)

# ---------------------------------------------------------
# MODULE 7: AI HEALTH ASSISTANT
# ---------------------------------------------------------
elif choice == "🤖 AI Assistant":
    st.title("🤖 AI Health Assistant")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("👋 Hello! How can I help you today?")
    q = st.text_input("Ask a question:", placeholder="e.g., When is the next health camp?")
    
    if q:
        q_lower = q.lower()
        if "camp" in q_lower:
            st.info("🤖 **AI:** The next Free Health Check-up Camp is on 28 September 2026 at Community Centre, Ambernath East.")
        elif "telemedicine" in q_lower:
            st.info("🤖 **AI:** Telemedicine allows you to consult certified doctors remotely via phone or video call without traveling.")
        elif "health centre" in q_lower or "nearby" in q_lower:
            st.info("🤖 **AI:** The primary health centre in Ambernath is located on Station Road, Ambernath West (Open 9 AM - 5 PM).")
        else:
            st.info("🤖 **AI:** I am here to help route you to healthcare services in Ambernath. Please visit the Healthcare or Camps section for full schedules.")
            
    st.caption("⚠️ *This assistant provides general information and does not replace professional medical advice.*")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 8: COMMUNITY DASHBOARD (ROLE-BASED VIEWS)
# ---------------------------------------------------------
elif choice == "📊 Dashboard":
    st.title(f"📊 Dashboard Mode: {user_role}")
    
    if user_role == "Citizen":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Your Personal Health Activity")
        st.write(f"**Citizen Name:** {user_name} | **Age:** {user_age}")
        st.write("• **Registered Camps:** Free Health Check-up Camp (28 Sept 2026)")
        st.write("• **Pending Consultations:** 1 Request Submitted")
        st.markdown('</div>', unsafe_allow_html=True)

    elif user_role == "Health Worker":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("👨‍⚕️ Health Worker Request Management")
        st.write("Manage incoming patient booking requests:")
        if st.session_state.consultations:
            st.dataframe(pd.DataFrame(st.session_state.consultations))
        else:
            st.info("No active consultation requests pending.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif user_role == "Admin":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🏛️ Central Management Analytics")
        
        months = ["May", "Jun", "Jul", "Aug", "Sep"]
        consults = [65, 80, 95, 110, 130]
        camps_att = [120, 180, 150, 210, 240]
        
        col1, col2 = st.columns(2)
        with col1:
            fig1 = px.line(x=months, y=consults, labels={'x':'Month', 'y':'Consultations'}, title="Monthly Consultations Trend")
            fig1.update_layout(template="plotly_dark", height=280)
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            fig2 = px.bar(x=months, y=camps_att, labels={'x':'Month', 'y':'Attendees'}, title="Health Camp Attendance")
            fig2.update_layout(template="plotly_dark", height=280)
            st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 9: EMERGENCY HELP
# ---------------------------------------------------------
elif choice == "🚨 Emergency":
    st.title("🚨 Emergency Assistance & Quick Contacts")
    
    st.markdown('<div class="emergency-card">', unsafe_allow_html=True)
    st.error("🚑 **AMBULANCE HELPLINE:** Dial 108 / 102")
    st.error("📞 **Ambernath Municipal Emergency Desk:** +91 0251-260XXXX")
    st.markdown("### Nearby Emergency Hospitals:")
    st.write("1. **Central Municipal Hospital** — Kansai Section (24/7 Open)")
    st.write("2. **Apex Critical Care Center** — West Station Road")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MODULE 10: FEEDBACK / REPORT ISSUE
# ---------------------------------------------------------
st.markdown("---")
with st.expander("📝 Report an Issue / Provide Feedback"):
    with st.form("feedback_form"):
        st.write(f"Submitting feedback as: **{user_name} (Age: {user_age})**")
        issue_type = st.multiselect("Issue Type:", ["Medicine unavailable", "Health centre issue", "Sanitation issue", "Request health camp", "Other"])
        desc = st.text_area("Description")
        fb_sub = st.form_submit_button("Submit Feedback")
        if fb_sub:
            st.session_state.feedbacks.append({"User": user_name, "Issues": issue_type, "Desc": desc})
            st.success("✅ Feedback submitted successfully.")