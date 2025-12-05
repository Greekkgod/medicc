import streamlit as st

def diagnose(symptoms):
    if not symptoms:
        return "No symptoms entered", "Low"
    symptoms_lower = symptoms.lower()
    patterns = {
        "Cardiac": ["chest pain", "shortness of breath", "heart"],
        "Respiratory": ["cough", "fever", "breath"],
        "Neurological": ["headache", "dizziness", "nausea"],
        "Gastrointestinal": ["vomiting", "diarrhea", "stomach"],
        "Musculoskeletal": ["joint pain", "back pain"]
    }
    for diagnosis, keywords in patterns.items():
        if any(keyword in symptoms_lower for keyword in keywords):
            return diagnosis, "High"
    return "General Checkup", "Low"

st.set_page_config(page_title="Medic.ai", page_icon="🏥", layout="wide")
st.title("🏥 Medic.ai")
st.markdown("**AI Symptom Analyzer**")

symptoms = st.text_area("Enter symptoms", height=120, placeholder="e.g., chest pain, shortness of breath")
if st.button("🔬 Diagnose", type="primary"):
    if symptoms.strip():
        diagnosis, risk = diagnose(symptoms)
        col1, col2 = st.columns(2)
        with col1: 
            st.error(f"**{diagnosis}**")
        with col2: 
            st.warning(f"**Risk: {risk}**")
    else:
        st.warning("Please enter symptoms first!")
        
st.caption("⚡ Powered by RTX 3050")
