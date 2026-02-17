# EchoEclipse

AI-assisted pipeline for scam/spam call analysis using speech-to-text, language detection, keyword/sentiment analysis, and rule-based risk scoring.

## Project Status
This repository currently provides a Python proof-of-concept pipeline and module-level utilities. It is not an Android app project in its present state.

## Repository Structure

- `main.py` – End-to-end call processing pipeline and CSV logging.
- `modules/` – Core components:
  - `speech_to_text.py` – Vosk transcription wrapper.
  - `language_detection.py` – Language detection using `langdetect`.
  - `nlp_analysis.py` – Keyword matching and sentiment analysis.
  - `risk_scoring.py` – Rule-based risk score computation.
  - `caller_verification.py` – Trusted-number checks from config JSON.
  - `alerting.py` – Alert channels (WhatsApp/SMS/Email).
  - `voice_biometrics.py` – Experimental voice feature extraction/comparison.
- `config/trusted_numbers.json` – Trusted caller whitelist.
- `audio/` – Sample call audio files.
- `tests/` – Unit tests.
- `models/` – Local speech model files.

## Quickstart

### 1) Create environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Optional: configure alerts

Create `.env` if you want email/SMS alert channels:

```env
ALERT_EMAIL=your_email@example.com
ALERT_EMAIL_PASSWORD=your_app_password
```

### 3) Run tests

```bash
python -m pytest -q
```

### 4) Run the pipeline

```bash
python main.py
```

## Notes

- Vosk models are expected under `models/`.
- `call_logs.csv` is treated as a runtime artifact and ignored by git.
- Alerting integrations may require external login/browser interaction.

## Development

- Formatting/lint config is defined in `pyproject.toml`.
- Test discovery is configured for the `tests/` directory.
