from packages.core.scoring.engine import ScoringEnvelope


def test_scoring_envelope_final_score() -> None:
    scoring = ScoringEnvelope(
        risk_score=0.2,
        confidence_score=0.9,
        impact_score=0.8,
        reversibility_score=0.7,
    )

    assert scoring.final_score() > 0
