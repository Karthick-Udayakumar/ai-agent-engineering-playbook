# Enterprise base system message

Versioned behavioral contract for agents running on Amazon Bedrock.

| File | Layer | Who may change it |
|---|---|---|
| `base.md` | Shared enterprise base | Locked. Changes need a new version directory, a new hash and Governance approval. |
| `agent-layer.template.md` | Agent layer | Filled per agent from an agent JSON file. |
| `session-context.template.md` | Dynamic block | Filled at request time by your application. |

`{PLACEHOLDERS}` in the templates are filled by `scripts/compose_prompt.py`.
`{MAX_STEPS}` is a parameter inside the locked base: set it per agent in the agent JSON instead of editing `base.md`.
