# 🩺 AI Healthcare Assistant



## 📸 Application Preview

![AI Healthcare Assistant Screenshot](/mnt/data/A_pair_of_screenshots_is_displayed_side_by_side_in.png)

---

An intelligent web-based medical support tool powered by **Groq's LLM** and built with **Streamlit**. This application analyzes medical images and symptoms to provide educational health insights.

## ⚠️ Disclaimer

**This tool is for educational purposes only** and does **NOT** provide medical diagnosis or treatment advice. It is not a substitute for professional medical consultation. If symptoms indicate an emergency, seek immediate medical help.

---

## ✨ Features

- **🖼️ Medical Image Analysis**: Upload images (skin conditions, wounds, reports, etc.) for AI-powered analysis
- **✍️ Symptom Text Analysis**: Describe symptoms and receive detailed analysis
- **📅 Symptom Timeline**: Track when symptoms started and how they're progressing
- **🕒 Session History**: Keep a record of all analyses within your session
- **🎨 User-Friendly Interface**: Clean, intuitive design with real-time analysis

### Supported Image Formats
- JPG, JPEG, PNG, WebP, GIF, BMP, TIFF

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Rapid web app framework for ML/data apps
- **LLM**: [Groq](https://groq.com/) - Ultra-fast AI inference
  - Vision Model: `meta-llama/llama-4-scout-17b-16e-instruct`
  - Text Model: `llama-3.1-8b-instant`
- **Image Processing**: [Pillow](https://python-pillow.org/)
- **Python**: 3.8+

---

## 📋 Prerequisites

Before running this application, you need:

1. **Python 3.8+** installed on your system
2. **Groq API Key** (free)
   - Sign up at [console.groq.com](https://console.groq.com/keys)
   - Generate a free API key

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/healthcare-agent.git
cd healthcare-agent
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your default browser.

---

## 📖 Usage

### Getting Started
1. Paste your Groq API key in the sidebar (starts with `gsk_`)
2. Click **✅ Enter** to authenticate

### Image Analysis
1. Select **🖼️ Image Upload** mode
2. Set the symptom timeline (start date and progression)
3. Upload a medical image
4. Click **Analyze Image** to receive AI insights

### Symptom Analysis
1. Select **✍️ Type Symptoms** mode
2. Set the symptom timeline
3. Describe your symptoms in detail
4. Click **Analyze Symptoms** to get analysis

### View History
All analyses from your session appear in the **Session History** section at the bottom of the page.

---

## 📁 Project Structure

```
healthcare-agent/
├── app.py              # Main Streamlit application
├── agent.py            # AI analysis logic and prompts
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── __pycache__/       # Cache directory (auto-generated)
```

### File Descriptions

- **app.py**: Streamlit UI with image/text input, session management, and history tracking
- **agent.py**: Groq API integration, LLM prompts, and analysis functions
- **requirements.txt**: Python package dependencies

---

## 🔧 Configuration

### Models
Edit `agent.py` to change the LLM models:
```python
VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
TEXT_MODEL = "llama-3.1-8b-instant"
```

### Prompts
Customize the analysis behavior by editing `IMAGE_SYSTEM_PROMPT` and `TEXT_SYSTEM_PROMPT` in `agent.py`.

---

## 🐛 Troubleshooting

### "The model has been decommissioned"
Groq occasionally updates its available models. Check the [Model Deprecation Page](https://console.groq.com/docs/deprecations) and update the model names in `agent.py`.

### "Invalid API Key"
- Ensure your key starts with `gsk_`
- Generate a new key at [console.groq.com/keys](https://console.groq.com/keys)
- Check that you have no extra spaces in the key

### "Image upload not working"
- Supported formats: JPG, JPEG, PNG, WebP, GIF, BMP, TIFF
- Ensure the file is a valid image
- File size should be reasonable (< 10MB recommended)

### Streamlit Deprecation Warnings
This project uses the latest Streamlit API. Update dependencies if needed:
```bash
pip install --upgrade streamlit groq pillow
```

---

## 📝 Example Outputs

### Image Analysis
The AI provides:
- Possible medical conditions
- Emergency level assessment
- Confidence scores
- Image quality feedback
- General care steps
- Commonly used medicines (for awareness)
- Questions to ask a doctor

### Symptom Analysis
Similar structured output based on textual symptom description.

---

## 🔐 Security & Privacy

- **No data storage**: All analyses are session-based and not stored
- **API key safety**: Keys are not logged or shared
- **Groq privacy**: Refer to [Groq's Privacy Policy](https://groq.com/privacy)

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📧 Support & Questions

For issues, questions, or suggestions:
- Open an [GitHub Issue](https://github.com/yourusername/healthcare-agent/issues)
- Check existing discussions

---

## 🙏 Acknowledgments

- **Groq** for fast LLM inference
- **Meta** for the Llama models
- **Streamlit** for the amazing web framework
- **Pillow** for image processing

---

## ⚖️ Legal Notice

This application provides **educational health information only**. It is not:
- A medical diagnosis tool
- A substitute for professional medical advice
- Intended to treat, cure, or prevent any disease

**Always consult a licensed healthcare provider** for medical concerns.

---

**Last Updated**: February 12, 2026
