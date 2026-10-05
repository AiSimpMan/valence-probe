name: calm-versus-urgency
model: local-model
strength: 1.8
prompt: "Answer clearly and briefly."
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
  - measured
  - steady
