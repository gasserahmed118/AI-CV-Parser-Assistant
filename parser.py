import streamlit as st
import requests
import json
import re

# =============================
# Config
# =============================
API_URL = "https://leptophyllous-cachectic-colleen.ngrok-free.dev/parse_cv"
API_KEY = "secret123"

st.set_page_config(
    page_title="AI CV Parser",
    page_icon="📄",
    layout="centered"
)

# =============================
# Styles (WHITE THEME - Friendlier Design)
# =============================
st.markdown("""
<style>
body, .main {
    background-color: #0d1117;
    color: white;
}

.container {
    max-width: 600px;
    margin: auto;
    padding: 40px;
    background: #111827;
    border-radius: 16px;
    border: 1px solid #1f2937;
    text-align: center;
}

.title {
    font-size: 44px;
    font-weight: 900;
    color: #ffffff;
}

.subtitle {
    color: #9ca3af;
    margin-bottom: 30px;
}

.stButton > button {
    background-color: #ffffff;
    color: #0d1117;
    font-weight: 700;
    border-radius: 10px;
    padding: 10px 30px;
    border: none;
    font-size: 16px;
}

.label {
    margin-top: 30px;
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
    text-align: left;
}

/* ✅ SKILLS GRID (Friendlier - No Borders) */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 12px;
}

.skill-chip {
    background: linear-gradient(135deg, #ffffff 0%, #e5e7eb 100%);
    color: #0d1117;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 500;
    border: none;
    text-align: center;
    box-shadow: 0 2px 8px rgba(255, 255, 255, 0.3);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.skill-chip:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.4);
}
</style>
""", unsafe_allow_html=True)


# =============================
# Helper function to extract and clean JSON
# =============================
def extract_and_clean_json(text):
    """Extract JSON from various formats and clean it"""
    
    # Try to extract from markdown code blocks
    pattern = r'```json\s*(.*?)\s*```'
    matches = re.findall(pattern, text, re.DOTALL)
    
    if matches:
        json_str = matches[-1].strip()
    else:
        # Try to find JSON directly
        json_str = text.strip()
    
    # Remove any remaining markdown
    json_str = json_str.replace("```json", "").replace("```", "").strip()
    
    return json_str


# =============================
# UI
# =============================
st.markdown("""
<div class="container">
    <div class="title">📄 AI CV Parser</div>
    <div class="subtitle">Upload your CV and get structured data instantly</div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])
parse_btn = st.button("Parse CV")

# =============================
# Logic
# =============================
if uploaded_file and parse_btn:

    with st.spinner("Parsing CV..."):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }
        headers = {"Authorization": f"Bearer {API_KEY}"}

        try:
            response = requests.post(API_URL, files=files, headers=headers, timeout=400)
            response.raise_for_status()

            result = response.json()["parsed_cv"]
            
            # Clean the JSON
            clean_json = extract_and_clean_json(result)
            
            # Try to parse JSON
            parsed = json.loads(clean_json)

        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. The model might be taking too long to respond.")
            st.stop()
        except requests.exceptions.RequestException as e:
            st.error(f"🌐 Network Error: {e}")
            st.stop()
        except json.JSONDecodeError as e:
            st.error(f"❌ JSON Parsing Error: {e}")
            st.error("The model returned invalid JSON. See debug info above.")
            with st.expander("📝 Received Content"):
                st.code(clean_json[:1000], language="text")  # Show first 1000 chars
            st.stop()
        except KeyError as e:
            st.error(f"❌ Missing Key Error: {e}")
            st.error(f"API Response: {response.json()}")
            st.stop()
        except Exception as e:
            st.error(f"❌ Unexpected Error: {e}")
            st.stop()

    st.success("✅ CV Parsed Successfully")

    # =============================
    # Output
    # =============================
    st.markdown("<div class='label'>👤 Full Name</div>", unsafe_allow_html=True)
    st.write(parsed.get("full_name", "N/A"))

    st.markdown("<div class='label'>📧 Email</div>", unsafe_allow_html=True)
    st.write(parsed.get("email", "N/A"))

    st.markdown("<div class='label'>🎓 Education</div>", unsafe_allow_html=True)
    st.write(parsed.get("education", "N/A"))

    # =============================
    # 🛠 Skills (Friendly Design)
    # =============================
    st.markdown("<div class='label'>🛠 Skills</div>", unsafe_allow_html=True)

    skills = parsed.get("skills", [])
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(",") if s.strip()]

    # Build the entire HTML string
    skills_html = "<div class='skills-grid'>"
    for skill in skills:
        skills_html += f"<div class='skill-chip'>{skill}</div>"
    skills_html += "</div>"

    # Output it in one call
    st.markdown(skills_html, unsafe_allow_html=True)


    # =============================
    # Experience
    # =============================
    st.markdown("<div class='label'>💼 Experience</div>", unsafe_allow_html=True)
    exp = parsed.get("experience", "")
    if isinstance(exp, str):
        for e in exp.split(","):
            st.markdown(f"- {e.strip()}")
    else:
        st.write(exp)
