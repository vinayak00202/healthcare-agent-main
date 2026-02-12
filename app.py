import streamlit as st
from PIL import Image
import base64
import io
from datetime import date

from agent import analyze_medical_image, analyze_symptoms_text

st.set_page_config(page_title="AI Healthcare Agent", page_icon="🩺")

# ---------------- SESSION STATE ----------------
if "groq_ok" not in st.session_state:
    st.session_state.groq_ok = False
if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ""
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔑 Groq API Configuration")

key_input = st.sidebar.text_input(
    "Groq API Key (starts with gsk_)",
    type="password"
)
enter_btn = st.sidebar.button("✅ Enter")

st.sidebar.caption("[Get a free key here](https://console.groq.com/keys)")

if enter_btn:
    if not key_input:
        st.sidebar.error("API key required.")
    elif not key_input.startswith("gsk_"):
        st.sidebar.error("Invalid Groq API key.")
    else:
        st.session_state.groq_api_key = key_input
        st.session_state.groq_ok = True
        st.sidebar.success("API key accepted!")

if not st.session_state.groq_ok:
    st.warning("Please enter your Groq API key to continue.")
    st.stop()

# ---------------- MAIN UI ----------------
st.title("🩺 AI Healthcare Assistant")

# ---------------- MODE SELECT ----------------
mode = st.radio(
    "Choose input method:",
    ["🖼️ Image Upload", "✍️ Type Symptoms"]
)

# ---------------- TIMELINE ----------------
st.subheader("📅 Symptom Timeline")

start_date = st.date_input("When did the symptoms start?", value=date.today())
progress = st.selectbox(
    "How are the symptoms changing?",
    ["Improving", "Worsening", "No Change"]
)

timeline_info = f"Started on {start_date}, symptoms are {progress.lower()}."

# ---------------- IMAGE MODE ----------------
if mode == "🖼️ Image Upload":
    uploaded_file = st.file_uploader(
        "Upload a medical image (skin, eye, wound, report, etc.)",
        type=["jpg", "jpeg", "png", "webp", "gif", "bmp", "tiff"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width="stretch")

        buf = io.BytesIO()
        image.save(buf, format="PNG")
        image_b64 = base64.b64encode(buf.getvalue()).decode()

        if st.button("Analyze Image"):
            with st.spinner("Analyzing image..."):
                result = analyze_medical_image(
                    api_key=st.session_state.groq_api_key,
                    image_base64=image_b64,
                    timeline_info=timeline_info
                )

                st.markdown(result)

                st.session_state.history.append({
                    "type": "Image",
                    "date": date.today(),
                    "result": result
                })

# ---------------- TEXT MODE ----------------
else:
    symptoms = st.text_area(
        "Describe symptoms (example: fever, headache, nausea):",
        height=120
    )

    if st.button("Analyze Symptoms"):
        if not symptoms.strip():
            st.error("Please enter symptoms.")
        else:
            with st.spinner("Analyzing symptoms..."):
                result = analyze_symptoms_text(
                    api_key=st.session_state.groq_api_key,
                    symptoms=symptoms,
                    timeline_info=timeline_info
                )

                st.markdown(result)

                st.session_state.history.append({
                    "type": "Text",
                    "date": date.today(),
                    "result": result
                })

# ---------------- HISTORY ----------------
if st.session_state.history:
    st.subheader("🕒 Session History")
    for i, h in enumerate(reversed(st.session_state.history), 1):
        with st.expander(f"{h['type']} Analysis {i} — {h['date']}"):
            st.markdown(h["result"])
