import requests
from bs4 import BeautifulSoup

from src.config import USER_AGENT


class DocumentationFinder:

    COMMON_PATHS = [

        "/docs",

        "/developers",

        "/developer",

        "/api",

        "/api/docs",

        "/developer/docs",

        "/reference",

        "/docs/api",

        "/developer/reference",

        "/documentation"

    ]

    def __init__(self):

        self.headers = {
            "User-Agent": USER_AGENT
        }

    def exists(self, url):

        try:

            r = requests.get(
                url,
                timeout=10,
                headers=self.headers,
                allow_redirects=True
            )

            return r.status_code < 400

        except:

            return False

    def find(self, website):

        website = website.rstrip("/")

        if self.exists(website):

            soup = BeautifulSoup(

                requests.get(
                    website,
                    headers=self.headers
                ).text,

                "html.parser"
            )

            for a in soup.find_all("a", href=True):

                href = a["href"].lower()

                if any(

                        word in href

                        for word in [

                            "docs",

                            "developer",

                            "api"

                        ]

                ):

                    if href.startswith("http"):

                        return href

                    return website + href

        for path in self.COMMON_PATHS:

            candidate = website + path

            if self.exists(candidate):

                return candidate

        return website