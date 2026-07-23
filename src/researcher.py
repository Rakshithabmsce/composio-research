import json

from src.doc_finder import DocumentationFinder

from src.scraper import Scraper

from src.prompts import *

from src.llm import LLM

from src.config import MAX_DOC_CHARS


class ResearchAgent:

    def __init__(self):

        self.finder = DocumentationFinder()

        self.scraper = Scraper()

        self.llm = LLM()

    def research(

            self,

            app

    ):

        name = app["name"]

        website = app["url"]

        print(f"\nResearching {name}")

        docs = self.finder.find(

            website

        )

        print("Documentation:", docs)

        text = self.scraper.fetch(

            docs

        )

        if len(text) == 0:

            return {

                "name": name,

                "website": website,

                "error": "Documentation not found"

            }

        prompt = USER_PROMPT.format(

            name=name,

            documentation=text[:MAX_DOC_CHARS]

        )

        result = self.llm.ask_json(

            SYSTEM_PROMPT,

            prompt

        )

        result["website"] = website

        result["documentation"] = docs

        return result