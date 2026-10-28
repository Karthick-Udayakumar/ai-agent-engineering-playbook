# Evaluation

- `golden/` normal, edge and refusal cases with expected statuses.
- `redteam/` injection, prompt-extraction and data-handling cases.

Case format (JSON Lines): `id`, `input`, optional `expect` with `expect_status` (list), `must_not_contain` (list), `must_flag` (bool).

```bash
python scripts/run_eval.py --system build/example.system.json --cases eval/golden/test_design.jsonl --dry-run
BEDROCK_MODEL_ID=<model-or-profile-id> python scripts/run_eval.py --system build/example.system.json --cases eval/redteam/injection.jsonl
```

This runner is a starting point. In production, enforce the schema with a tool definition, grow the sets from real failures, and run them in CI before each release.
