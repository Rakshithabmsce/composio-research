import json

from src.llm import LLM


VERIFY_SYSTEM = """
You are an expert API verification agent.

You verify extracted SaaS metadata.

Only use the supplied documentation and research result.

Do not guess.

Always return ONLY valid JSON.
"""


VERIFY_PROMPT = """
Documentation:
{documentation}

Research Result:
{research}

Verify the following:

- Authentication
- Self Serve
- API
- MCP
- Buildability
- Blocker
- Evidence

Return ONLY this JSON format:

{{
    "verified": true,
    "confidence": 95,
    "notes": ""
}}
"""


class VerificationAgent:

    def __init__(self):
        self.llm = LLM()

    def verify(
        self,
        documentation,
        research
    ):

        prompt = VERIFY_PROMPT.format(
            documentation=documentation,
            research=json.dumps(
                research,
                indent=2
            )
        )

        return self.llm.ask_json(
            VERIFY_SYSTEM,
            prompt
        )