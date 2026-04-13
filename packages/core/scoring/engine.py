from dataclasses import dataclass


@dataclass
class ScoringEnvelope:
    risk_score: float
    confidence_score: float
    impact_score: float
    reversibility_score: float

    def final_score(self) -> float:
        return round(
            (self.confidence_score * 0.4)
            + (self.impact_score * 0.2)
            + (self.reversibility_score * 0.2)
            - (self.risk_score * 0.2),
            4,
        )
