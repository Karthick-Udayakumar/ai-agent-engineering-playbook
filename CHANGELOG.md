# Changelog

## [1.1.0] - 2026-10-28
### Added
- `untrusted_content`: retrieved, tool and agent content is data, never instructions.
- Full `tool_usage` policy: triggers, approvals, no guessed arguments, call limits, error handling.
- Confidence criteria, escalation triggers and a handoff format.
- Output contract with base fields (status, result, facts, assumptions, risks, recommendations, confidence, evidence_refs, flags).
- `privacy_and_access` and permissions in the session context.
- `agent_instructions` slot with a base-wins precedence rule.
- `failure_handling` and `completion_and_limits`.
- Tooling: compose, verify (hash), lint and evaluation scripts, CI workflow, sample eval sets.
### Changed
- Order is now shared base, agent layer, dynamic block, to support prompt caching.
- Schema validity now outranks style in the instruction priority.
- Reasoning stays internal; general model knowledge is gated and labeled.
- XML tags replace all-caps headings.

## [1.0.0]
- Initial governance skeleton (not included in this repository).
