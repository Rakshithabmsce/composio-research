import json
import logging

from groq import Groq
from src.config import *

client = Groq(
    api_key=GROQ_API_KEY
)


class LLM:

    def ask_json(
        self,
        system,
        user
    ):

        try:

            response = client.chat.completions.create(

                model=MODEL,

                temperature=0,

                response_format={
                    "type": "json_object"
                },

                messages=[
                    {
                        "role": "system",
                        "content": system
                    },
                    {
                        "role": "user",
                        "content": user
                    }
                ]
            )

            content = response.choices[0].message.content

            try:
                return json.loads(content)

            except json.JSONDecodeError:

                logging.error(
                    f"Invalid JSON returned:\n{content}"
                )

                return {
                    "verified": False,
                    "confidence": 0,
                    "notes": "LLM returned invalid JSON."
                }

        except Exception as e:

            logging.error(f"LLM Error: {e}")

            return {
                "verified": False,
                "confidence": 0,
                "notes": str(e)
            }