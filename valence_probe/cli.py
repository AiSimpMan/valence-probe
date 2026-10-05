from __future__ import annotations

from dataclasses import dataclass

from .config import SteeringConfig, WordTarget


@dataclass
class DirectionProfile:
    name: str
    strength: float
    increase: list[WordTarget]
    decrease: list[WordTarget]
    neutral: list[str]

    @property
    def total_increase_weight(self) -> float:
        return sum(item.weight for item in self.increase)

    @property
    def total_decrease_weight(self) -> float:
        return sum(item.weight for item in self.decrease)

    @property
    def net_bias(self) -> float:
        return self.total_increase_weight - self.total_decrease_weight

    def summary(self) -> dict[str, object]:
        return {
            "name": self.name,
            "strength": self.strength,
            "increase_terms": {item.text: item.weight for item in self.increase},
            "decrease_terms": {item.text: item.weight for item in self.decrease},
            "neutral_terms": self.neutral,
            "total_increase_weight": self.total_increase_weight,
            "total_decrease_weight": self.total_decrease_weight,
            "net_bias": self.net_bias,
        }


def build_direction_profile(config: SteeringConfig) -> DirectionProfile:
    return DirectionProfile(
        name=config.name,
        strength=config.strength,
        increase=config.increase,
        decrease=config.decrease,
        neutral=config.neutral,
    )


def recommend_prompt(profile: DirectionProfile) -> str:
    increase_phrase = ", ".join(item.text for item in profile.increase[:3])
    decrease_phrase = ", ".join(item.text for item in profile.decrease[:3])
    if not decrease_phrase:
        decrease_phrase = "none"
    return (
        f"Probe direction '{profile.name}' using a stronger emphasis on {increase_phrase} "
        f"and reduced emphasis on {decrease_phrase}."
    )
