# Agents

One JSON file per agent. `values` fills the agent layer and any parameters in the base (for example `MAX_STEPS`).
`session_example` is used only with `--with-example-session`, for local tests.

```bash
python scripts/compose_prompt.py --agent agents/example-test-design-agent.json --out build/example.system.json
```

Rules:
- Agent values may narrow behavior and never widen it. The base always wins on conflict.
- Do not put secrets, credentials or customer data in agent files.
