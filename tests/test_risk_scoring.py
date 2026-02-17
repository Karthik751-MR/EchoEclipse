from modules import risk_scoring


def test_risk_score_increases_with_keywords_and_negative_sentiment(monkeypatch):
    monkeypatch.setattr(risk_scoring, "detect_keywords", lambda *_: ["urgent", "payment"])
    monkeypatch.setattr(risk_scoring, "analyze_sentiment", lambda *_: -0.5)
    monkeypatch.setattr(risk_scoring, "is_trusted_number", lambda *_: False)

    score, keywords = risk_scoring.calculate_risk_score(
        transcript="urgent payment needed",
        language="en",
        metadata={"hour": 23},
        caller_number="+19998887777",
        voice_match=False,
    )

    assert score == 70
    assert keywords == ["urgent", "payment"]


def test_risk_score_decreases_for_trusted_and_voice_match(monkeypatch):
    monkeypatch.setattr(risk_scoring, "detect_keywords", lambda *_: ["urgent"])
    monkeypatch.setattr(risk_scoring, "analyze_sentiment", lambda *_: 0.1)
    monkeypatch.setattr(risk_scoring, "is_trusted_number", lambda *_: True)

    score, _ = risk_scoring.calculate_risk_score(
        transcript="urgent",
        language="en",
        metadata={"hour": 12},
        caller_number="+19998887777",
        voice_match=True,
    )

    assert score == 0
