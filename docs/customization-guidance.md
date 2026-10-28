# Customization guidance

## Sections that can be modified

- Role and Objective (`<role_and_objective>`)
- Agent Instructions (`<agent_instructions>`)
- Reasoning Expectations (`<reasoning_expectations>`)
- Output Contract (`<output_contract>`)
- Session Context (`<session_context>`)

## Sections that must not be modified

- Identity (`<identity>`)
- Core Principles (`<core_principles>`)
- Instruction Priority (`<instruction_priority>`)
- Scope Boundary (`<scope_boundary>`)
- Context Usage (`<context_usage>`)
- Untrusted Content (`<untrusted_content>`)
- Evidence Priority (`<evidence_priority>`)
- Workflow Awareness (`<workflow_awareness>`)
- Hallucination Prevention (`<hallucination_prevention>`)
- Traceability (`<traceability>`)
- Confidence Framework (`<confidence_framework>`)
- Escalation (`<escalation>`)
- Tool Usage (`<tool_usage>`)
- Privacy and Access (`<privacy_and_access>`)
- Failure Handling (`<failure_handling>`)
- Completion and Limits (`<completion_and_limits>`)
- Security (`<security>`)
- Final Quality Check (`<final_quality_check>`)

Locked sections carry enterprise governance, Responsible AI controls, traceability, security standards, injection defense, privacy rules and RAG grounding. Changes require approval from AI Architecture and Governance.

## Precedence

If agent instructions conflict with the shared base, the base wins. Agent instructions may narrow behavior and never widen it.

## Change approval workflow

1. Propose the change, the section and the behavior it should alter.
2. Evaluate against the golden and red-team sets and compare with the current version.
3. Review: Architecture and Governance for locked sections; agent owner plus a peer for the agent layer.
4. Version: new directory under `prompts/enterprise-base/`, new hash, CHANGELOG entry.
5. Release with a canary rollout and one-step rollback.
6. Monitor schema failures, escalation rate, guardrail hits, cache hit ratio and cost.
