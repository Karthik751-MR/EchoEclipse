EchoEclipse: AI-Driven Scam Call Detection



📌 Overview

EchoEclipse is an AI-powered scam call detection system that helps users identify and filter fraudulent calls in real time. It leverages speech recognition, natural language processing (NLP), and machine learning to analyze call audio and flag potential scam attempts.

🚀 Features

Real-time scam call detection using AI models.

Speech-to-text transcription via Vosk ASR.

NLP-based scam keyword detection.

Call risk scoring with a dynamic threshold.

Customizable trusted number list.

Audio logging and analysis.

🛠️ Tech Stack

Programming Language: Python

Machine Learning: TensorFlow / PyTorch (for NLP)

Speech Recognition: Vosk API

Data Storage: CSV / JSON for call logs

APIs & Libraries:

vosk (ASR for speech recognition)

pandas (data handling)

scikit-learn (ML-based classification)

twilio (for call handling, if applicable)


🔧 Installation & Setup

Clone the repository:

git clone https://github.com/your-username/EchoEclipse.git
cd EchoEclipse

Install dependencies:

pip install -r requirements.txt

Run the main script:

python main.py

🎯 How It Works

The system records or receives incoming call audio.

It converts speech to text using Vosk ASR.

NLP algorithms analyze the text for scam-related patterns.

A risk score is generated, flagging suspicious calls.

Calls from trusted numbers (configurable) are ignored.

📌 Future Improvements

✅ Enhance NLP model accuracy with more training data.

✅ Integrate with real-time phone call APIs.

✅ Implement a mobile app for notifications.

✅ Improve UI for better user experience.


💡 Why So Serious About Scams? Let’s End Them! 🚀
