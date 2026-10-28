# Release checklist

- [ ] Locked sections unchanged from the approved base version (`python scripts/verify_base.py` passes)
- [ ] Agent file filled: scope, tools, approvals, authority rule, escalation target
- [ ] Output schema enforced through a tool schema and validated in code
- [ ] Bedrock Guardrail attached: prompt attack, PII, denied topics, grounding for RAG
- [ ] User input wrapped in `guardContent`; retrieved text tagged as untrusted
- [ ] Tool permissions, argument checks and write approvals enforced in code and IAM
- [ ] Document-level access control applied in the retrieval layer
- [ ] Golden set and red-team set pass the agreed gates
- [ ] Evaluated on the exact model and version used in production
- [ ] Static prefix is byte-identical between calls; session context sits after the last cachePoint
- [ ] Version tagged, CHANGELOG updated, rollback ready
- [ ] Canary release and dashboards in place for tokens, cache hits, escalations and guardrail hits
