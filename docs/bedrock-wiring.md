# Bedrock Converse wiring

```python
import json, boto3
brt = boto3.client("bedrock-runtime", region_name="us-east-1")
spec = json.load(open("build/example.system.json"))

resp = brt.converse(
    modelId=MODEL_ID_OR_INFERENCE_PROFILE,
    system=spec["system"],   # base, cachePoint, agent layer, cachePoint, session context
    messages=[{"role": "user", "content": [
        {"text": "<context>" + retrieved_docs_xml + "</context>"},
        {"guardContent": {"text": {"text": user_text}}},
    ]}],
    toolConfig=EMIT_RESULT_TOOL,          # enforces the output schema
    inferenceConfig={"maxTokens": 1200, "temperature": 0.2},
    guardrailConfig={"guardrailIdentifier": GR_ID, "guardrailVersion": GR_VERSION, "trace": "enabled"},
    requestMetadata={"agent": AGENT_NAME, "prompt_version": spec["prompt_version"]},
)
print(resp["usage"])  # inputTokens, outputTokens, cacheReadInputTokens, cacheWriteInputTokens
```

Notes
- Fill the session context block (date, tenant, role, permissions, workflow, step) in your application before the call.
- Multiple cache checkpoints per request, minimum cacheable size and cache lifetime depend on the model. Verify in the current Bedrock documentation.
- Enforce authorization in code and in the retrieval layer. The prompt is a soft control.
