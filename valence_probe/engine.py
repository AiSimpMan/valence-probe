from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class WordTarget:
    text: str
    weight: float = 1.0

    def __post_init__(self) -> None:
        text = str(self.text).strip()
        if not text:
            raise ValueError("WordTarget.text cannot be empty")
        self.text = text
        if self.weight <= 0:
            raise ValueError("WordTarget.weight must be positive")


@dataclass
class SteeringConfig:
    name: str
    model: str | None = None
    prompt: str = ""
    strength: float = 1.0
    increase: list[WordTarget] = field(default_factory=list)
    decrease: list[WordTarget] = field(default_factory=list)
    neutral: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("name is required")
        if self.strength <= 0:
            raise ValueError("strength must be positive")

    @property
    def increase_terms(self) -> list[str]:
        return [item.text for item in self.increase]

    @property
    def decrease_terms(self) -> list[str]:
        return [item.text for item in self.decrease]

    @property
    def increase_weights(self) -> dict[str, float]:
        return {item.text: item.weight for item in self.increase}

    @property
    def decrease_weights(self) -> dict[str, float]:
        return {item.text: item.weight for item in self.decrease}


def _normalize_word_targets(entries: Any) -> list[WordTarget]:
    if entries is None:
        return []
    if not isinstance(entries, list):
        raise TypeError("Word list entries must be a list of mappings or strings")

    result: list[WordTarget] = []
    for entry in entries:
        if isinstance(entry, str):
            result.append(WordTarget(text=entry, weight=1.0))
        elif isinstance(entry, dict):
            if "text" not in entry:
                raise ValueError("Each word entry must include a 'text' field")
            result.append(
                WordTarget(
                    text=str(entry["text"]),
                    weight=float(entry.get("weight", 1.0)),
                )
            )
        else:
            raise TypeError("Unsupported word target format")
    return result


def load_config(path: str | Path) -> SteeringConfig:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}

    if not isinstance(data, dict):
        raise TypeError("Config file must contain a YAML mapping")

    config = SteeringConfig(
        name=str(data.get("name", "unnamed-direction")),
        model=data.get("model"),
        prompt=str(data.get("prompt", "")),
        strength=float(data.get("strength", 1.0)),
        increase=_normalize_word_targets(data.get("increase", [])),
        decrease=_normalize_word_targets(data.get("decrease", [])),
        neutral=[str(item) for item in data.get("neutral", [])],
    )

    if not config.increase and not config.decrease:
        raise ValueError("Config requires at least one increase or decrease target")

    return config
