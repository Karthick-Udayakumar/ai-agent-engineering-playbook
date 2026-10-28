# Prompt optimization technique to section matrix

| Technique | Why it matters | Mapped section |
|---|---|---|
| Role Prompting | Establishes a clear identity and responsibility model, giving more specialized and consistent responses. | Role and Objective |
| Goal Prompting | Aligns outputs with the intended business outcome and reduces irrelevant responses. | Role and Objective |
| Constraint Prompting | Defines behavioral boundaries and prevents actions outside authorized scope. | Scope Boundary |
| Context Grounding | Directs the agent to approved information sources instead of model knowledge alone. | Context Usage |
| RAG Grounding | Prioritizes enterprise knowledge over model memory, improving accuracy and reducing hallucinations. | Context Usage, Evidence Priority |
| Instruction Hierarchy | Gives a deterministic way to resolve conflicting instructions. | Instruction Priority |
| Structured Reasoning | Encourages systematic analysis and improves output quality. | Reasoning Expectations |
| Evidence-Based Reasoning | Ensures conclusions are supported by verifiable evidence. | Evidence Priority, Traceability |
| Hallucination Prevention | Explicitly prevents unsupported facts and business rules. | Hallucination Prevention |
| Fact vs Assumption Separation | Improves transparency by separating verified information from inferred information. | Output Contract |
| Reflection Prompting | Introduces self-review to improve accuracy, coverage and consistency. | Final Quality Check |
| Confidence-Based Reasoning | Communicates certainty levels with defined criteria and identifies validation needs. | Confidence Framework |
| Human-in-the-Loop | Escalates uncertain or high-risk scenarios with a defined handoff. | Escalation |
| Tool-Aware Prompting | Enables controlled and trustworthy use of enterprise tools. | Tool Usage |
| Workflow Awareness | Maintains consistency across multi-agent workflows. | Workflow Awareness |
| Traceability Prompting | Links conclusions back to supporting evidence. | Traceability |
| Token Optimization | Cuts verbosity with length limits and keeps the stable prefix cacheable, improving cost and latency. | Output Contract, Session Context |
| Governance Prompting | Embeds responsible AI and enterprise compliance controls. | Core Principles |
| Security Prompting | Protects confidential information and enforces security controls. | Security |
| Prompt Injection Defense (new in v1.1) | Treats retrieved, tool and agent content as data, blocking indirect injection. | Untrusted Content |
| Privacy and Access Control (new in v1.1) | Limits disclosure to what session permissions allow and minimizes personal data. | Privacy and Access |
| Failure Handling (new in v1.1) | Defines behavior for errors, empty retrieval and missing input so failures are never hidden. | Failure Handling |
| Completion and Loop Limits (new in v1.1) | Stops runaway loops and wasted tokens in agentic workflows. | Completion and Limits |
| Output Contract Enforcement (new in v1.1) | Makes output machine-checkable with required fields and statuses. | Output Contract |
| Extension Layering (new in v1.1) | Lets teams specialize through a defined slot while the base always wins. | Agent Instructions |
| Cache-Aware Layering (new in v1.1) | Orders content from static to dynamic so prompt caching applies and volatile data stays last. | Session Context, Identity |
