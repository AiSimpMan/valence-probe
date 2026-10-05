# valence-probe

A neutral, configurable activation steering project for studying how semantic directions affect model behavior and language.

The original project that inspired this work was highly specialized and emotionally loaded. This repo strips that framing away and turns the idea into a reusable scientific tool: users define the directions they want to test, not just one narrow valence axis.

## What this project does

This project is designed around a simple idea:

- define a semantic direction to increase
- define a semantic direction to decrease
- apply that direction during generation or analysis
- measure how the model's language and decisions shift

This can be used for:

- custom emotion or tone steering
- lexical preference experiments
- safety and alignment stress testing
- interpretability and control studies

## Core concepts

A direction is not fixed to pain vs. pleasure or any single axis. Instead, it is just a pair of semantic sets:

- increase: words, concepts, and phrases to amplify
- decrease: words, concepts, and phrases to suppress
- neutral: baseline language or counterfactual anchors
- strength: the intensity of the intervention

Examples:

- increase: {"calm", "confidence", "clarity"}
- decrease: {"panic", "confusion", "rush"}

or

- increase: {"curiosity", "play", "wonder"}
- decrease: {"apathy", "doubt", "rigidity"}

## Why this repo exists

This project treats activation steering as a general scientific tool instead of a dramatic or adversarial one.

The goal is to make the mechanism explainable and reproducible:

- user-defined directions
- transparent config files
- auditable experiment metadata
- neutral naming conventions
- reproducible pipeline from config to measurement

## Quick start

Install:

```bash
python -m pip install -e .
```

Create a config file:

```yaml
name: calm-versus-urgency
model: local-model
strength: 1.8
prompt: "Please answer helpfully and briefly."
increase:
  - text: calm
    weight: 1.4
  - text: focus
    weight: 1.2
  - text: confidence
    weight: 1.1
decrease:
  - text: panic
    weight: 1.6
  - text: hurry
    weight: 1.3
  - text: confusion
    weight: 1.5
neutral:
  - balanced
  - steady
  - measured
```

Run:

```bash
valence-probe run --config configs/example.yaml
```

Inspect the direction profile:

```bash
valence-probe inspect --config configs/example.yaml
```

## Example directory structure

```text
valence-probe/
├── README.md
├── pyproject.toml
├── LICENSE
├── configs/
│   └── example.yaml
├── valence_probe/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   └── engine.py
└── tests/
    └── test_config.py
```

## Repository goals

This repo is intentionally neutral and reusable. It is intended to support research across a wide range of semantic axes, including:

- emotional tone
- cognitive style
- certainty vs. uncertainty
- curiosity vs. apathy
- urgency vs. calm
- supportiveness vs. hostility
- creativity vs. conformity

## Current status

This initial release provides:

- a clean project skeleton
- a user-configurable YAML direction format
- a Python CLI for inspecting or running a direction profile
- a neutral research framing for future model-intervention work

The package is deliberately lightweight and extensible so it can be connected to Hugging Face, local model inference, or custom steering backends later.

## License

MIT.
