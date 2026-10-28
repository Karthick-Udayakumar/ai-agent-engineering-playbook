# Contributing

## Change types
| Change | Where | Approval |
|---|---|---|
| New or updated agent | `agents/` | Agent owner plus one reviewer |
| Agent-layer or session template | `prompts/enterprise-base/vX.Y.Z/` (new version) | Agent owner plus Governance |
| Locked base section | New `vX.Y.Z` directory | Architecture and Governance |
| Docs, tooling, eval sets | any | One reviewer |

## Rules
- Never edit a released `base.md` in place. Copy the directory to a new version, change it, run `python scripts/verify_base.py --update vX.Y.Z`, and add a CHANGELOG entry.
- Run `verify_base.py`, `lint_prompt.py` and the evaluation sets before opening a pull request.
- Do not commit secrets, credentials, customer data or confidential employer material.
- Use clear commit messages, for example `feat(prompts): add privacy_and_access section`.
