# 🧠 Dyslexia Learning & Training Platform (ML-Powered)

A machine learning–powered web application designed to help individuals identify, understand, and improve dyslexia-related challenges through personalized training, reading assistance, and AI-driven feedback.

This project combines **Flask**, **Python**, **MongoDB**, and **Google Generative AI** to create an interactive learning system that adapts to users' reading and language patterns.

---

## 🚀 Features

- 📖 **Dyslexia Detection & Assistance**
  - ML-based analysis of reading and writing patterns
  - Text and speech evaluation for dyslexia indicators

- 🧠 **AI-Powered Learning Support**
  - Personalized recommendations using Google Generative AI
  - Adaptive exercises to improve reading fluency

- 🎤 **Speech & Audio Processing**
  - Speech-to-text using Whisper
  - Text-to-speech feedback using pyttsx3

- 🖼️ **Image & OCR Processing**
  - Extract text from images using EasyOCR and Tesseract
  - Enhance images for better text recognition

- ✍️ **Language Correction**
  - Grammar checking using LanguageTool
  - Real-time text improvement suggestions

- 📊 **User Progress Tracking**
  - Stores user data and learning progress in MongoDB
  - Session-based tracking and analytics

- 🔐 **Secure System**
  - Data encryption using cryptography
  - Secure session management

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- MongoDB

### AI / ML / NLP
- Google Generative AI (`google.generativeai`)
- Whisper (Speech Recognition)
- LanguageTool (`language_tool_python`)
- EasyOCR
- Tesseract OCR
- Pandas / NumPy

### Image Processing
- PIL (Pillow)
- ImageEnhance, ImageFilter

### Others
- pyttsx3 (Text-to-Speech)
- PyMongo
- Cryptography
- Regex (re)

---

## 📦 Installed Libraries

```python
whisper
language_tool_python
flask
os
pickle
pandas
tempfile
easyocr
PIL
datetime
pymongo
base64
cryptography
pytesseract
re
pyttsx3
random
google.generativeai
📁 Project Structure
dyslexia-ai-platform/
│
├── app.py                  # Main Flask application
├── models/                 # ML models & pickle files
├── templates/              # HTML templates (Jinja2)
├── static/                 # CSS, JS, images
├── utils/                  # Helper functions
├── ocr/                    # OCR processing modules
├── speech/                 # Speech recognition modules
├── database/               # MongoDB connection & schema
└── README.md
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/dyslexia-ai-platform.git
cd dyslexia-ai-platform
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
5. Open in browser
http://127.0.0.1:5000/
🧪 How It Works
User logs in / signs up
System analyzes input (text, speech, or image)
ML models detect patterns related to dyslexia
Google GenAI provides adaptive feedback
User receives personalized exercises and improvements
Progress is stored in MongoDB for tracking
🎯 Use Cases
Early dyslexia detection support
Reading and writing improvement training
Speech clarity enhancement
Educational assistance for students
AI-based personalized learning
🔐 Security Features
Encrypted user data storage
Secure session handling
Safe authentication flow
Protected API endpoints
🌟 Future Improvements
Mobile app version (Flutter / React Native)
Advanced deep learning dyslexia detection model
Multilingual support
Teacher/parent dashboard
Gamified learning system
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a new branch
Make changes
Submit a pull request
📜 License

This project is licensed under the MIT License.

💡 Acknowledgements
Google Generative AI
Open-source OCR & NLP libraries
Flask community
Medical & educational research inspirations on dyslexia support systems
❤️ Purpose

This project aims to make learning more accessible for individuals with dyslexia by combining AI, machine learning, and modern web technologies.
