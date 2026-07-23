import requests

from bs4 import BeautifulSoup

from src.config import USER_AGENT


class Scraper:

    def fetch(self, url):

        try:

            r = requests.get(

                url,

                timeout=20,

                headers={
                    "User-Agent": USER_AGENT
                }
            )

            soup = BeautifulSoup(
                r.text,
                "lxml"
            )

            for tag in soup(
                    [
                        "script",
                        "style",
                        "svg",
                        "noscript"
                    ]
            ):
                tag.decompose()

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            return text

        except Exception:

            return ""