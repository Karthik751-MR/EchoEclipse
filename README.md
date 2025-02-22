EchoEclipse - Real-Time Spam Call Detection



📌 Overview

EchoEclipse is an AI-powered spam call detection app that identifies spam calls in real-time and alerts users before they answer. Designed for privacy and efficiency, the app provides a seamless experience without compromising user security.

🔥 Features

✅ Real-time Spam Detection – Uses AI & external APIs to detect spam calls.
✅ Caller ID Lookup – Fetches caller details from trusted sources.
✅ Customizable Alerts – Visual & sound notifications for spam calls.
✅ Minimal UI – Simple, user-friendly interface for easy interaction.
✅ Battery Efficient – Optimized to run in the background without draining battery.

🚀 Tech Stack

Android Studio (Java) – Core development

Machine Learning Model – Spam detection

Caller ID API (NumLookup, Truecaller API, etc.)

Firebase (Optional) – Storing spam reports

AccessibilityService & CallScreeningService – Handling call detection

![image](https://github.com/user-attachments/assets/10b365f7-d0f9-4cd1-a31c-8c97c41685ea)



🛠️ Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/yourusername/EchoEclipse.git
cd EchoEclipse

2️⃣ Open in Android Studio

Open Android Studio → Open Project → Select the cloned folder.

3️⃣ Set Up Permissions

Grant required permissions for call screening & accessibility in settings.

4️⃣ Build & Run

Click Run ▶ in Android Studio or generate an APK.

🔗 API Integration

Ensure API keys are set in res/values/strings.xml.

Example (NumLookup API):

<string name="api_key">YOUR_API_KEY</string>

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

📜 License

This project is licensed under the MIT License.

🌟 Support & Feedback

Have suggestions or issues? Open an issue or contact us via LinkedIn.


