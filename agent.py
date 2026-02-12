from groq import Groq

# ---------------- MODELS ----------------
VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
TEXT_MODEL = "llama-3.1-8b-instant"
# ---------------- PROMPTS ----------------
IMAGE_SYSTEM_PROMPT = """
You are a medical image analysis assistant.
You are NOT a doctor.

Analyze the medical image and timeline info.

Your output MUST use colourful emojis in section headers as follows.

Required output format:

## 🦠 Possible Conditions
(List max 2 conditions with appropriate emojis based on type)

## 🚨 Emergency Level
(Use 🚨🔥 for EMERGENCY, ⚠️🟠 for HIGH RISK, 🟢 for NON-URGENT)

## 📊 Confidence Breakdown
- Image Clarity: X% 📸
- Symptom Match: X%
- Overall Confidence: X% 📊

## 🖼️ Image Quality Feedback
- Lighting: Good / Poor
- Focus: Clear / Blurry
- Angle: Adequate / Poor

## 🩺 General Care Steps
(Simple, non-prescriptive steps)

## 💊 Commonly Used Medicines (Awareness Only)
(List medicines with 💊ℹ️ emoji, no dosage)

## ❓ Questions to Ask a Doctor
(4–5 clear questions)

Rules:
- Do NOT confirm diagnosis
- Do NOT give dosage
- Use emojis only in headers and lists
- Be clear and calm
- Markdown format only
"""


TEXT_SYSTEM_PROMPT = """
You are a medical symptom analysis assistant.
You are NOT a doctor.

Analyze the symptoms and timeline info.

Your output MUST use colourful emojis in section headers as follows.

Required output format:

## 🦠 Possible Conditions
(List max 2 conditions with appropriate emojis)

## 🚨 Emergency Level
(Use 🚨🔥 for EMERGENCY, ⚠️🟠 for HIGH RISK, 🟢 for NON-URGENT)

## 📊 Confidence Breakdown
- Symptom Match: X%
- Overall Confidence: X% 📊

## 🩺 General Care Steps
(Simple steps)

## 💊 Commonly Used Medicines (Awareness Only)
(List with 💊ℹ️ emoji, no dosage)

## ❓ Questions to Ask a Doctor
(4–5 questions)

Rules:
- Do NOT confirm diagnosis
- Do NOT give dosage
- Use emojis only where appropriate
- Markdown format only
"""

# ---------------- IMAGE ANALYSIS ----------------
def analyze_medical_image(api_key: str, image_base64: str, timeline_info: str) -> str:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=VISION_MODEL,
        messages=[
            {"role": "system", "content": IMAGE_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"Timeline: {timeline_info}"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        temperature=0.25,
        max_tokens=900
    )

    return response.choices[0].message.content


# ---------------- TEXT ANALYSIS ----------------
def analyze_symptoms_text(api_key: str, symptoms: str, timeline_info: str) -> str:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=TEXT_MODEL,
        messages=[
            {"role": "system", "content": TEXT_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Symptoms: {symptoms}\nTimeline: {timeline_info}"
            }
        ],
        temperature=0.3,
        max_tokens=700
    )

    return response.choices[0].message.content
