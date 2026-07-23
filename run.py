import json
import logging
import os
import time

from tqdm import tqdm

from src.researcher import ResearchAgent
from src.scraper import Scraper
from src.verifier import VerificationAgent
from src.analyzer import Analyzer
from src.html_generator import HTMLGenerator
from src.utils import save_json

# ----------------------------
# Logging Configuration
# ----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ----------------------------
# Load Apps
# ----------------------------

def load_apps():

    path = "data/apps.json"

    if not os.path.exists(path):
        raise FileNotFoundError(
            "data/apps.json not found!"
        )

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ----------------------------
# Research Stage
# ----------------------------

def research_apps(apps, researcher):

    logger.info("Starting research stage...")

    raw_results = []

    for app in tqdm(apps, desc="Researching"):

        try:

            result = researcher.research(app)

            raw_results.append(result)

        except Exception as e:

            logger.error(
                f"Research failed for {app.get('name')}: {e}"
            )

            raw_results.append({

                "name": app.get("name"),

                "website": app.get("url"),

                "error": str(e)

            })

    save_json(

        "data/raw_results.json",

        raw_results

    )

    logger.info("Raw research saved.")

    return raw_results


# ----------------------------
# Verification Stage
# ----------------------------

def verify_apps(raw_results, scraper, verifier):

    logger.info("Starting verification stage...")

    verified = []

    for result in tqdm(raw_results, desc="Verifying"):

        try:

            if "error" in result:

                verified.append(result)

                continue

            docs = result.get(

                "documentation",

                result.get("website")

            )

            documentation = scraper.fetch(

                docs

            )

            verification = verifier.verify(

                documentation,

                result

            )

            result["verified"] = verification.get(

                "verified",

                False

            )

            result["confidence"] = verification.get(

                "confidence",

                0

            )

            result["verification_notes"] = verification.get(

                "notes",

                ""

            )

            verified.append(result)

        except Exception as e:

            logger.error(

                f"Verification failed for {result.get('name')}: {e}"

            )

            result["verified"] = False

            result["confidence"] = 0

            result["verification_notes"] = str(e)

            verified.append(result)

    save_json(

        "data/verified_results.json",

        verified

    )

    logger.info("Verified results saved.")

    return verified


# ----------------------------
# Analysis Stage
# ----------------------------

def analyze_results(results):

    logger.info("Analyzing results...")

    analyzer = Analyzer()

    analysis = analyzer.analyze(results)

    save_json(

        "data/analysis.json",

        analysis

    )

    logger.info("Analysis saved.")

    return analysis


# ----------------------------
# HTML Report
# ----------------------------

def generate_report(analysis, results):

    logger.info("Generating HTML report...")

    generator = HTMLGenerator()

    generator.generate(

        analysis,

        results

    )

    logger.info("Report generated.")


# ----------------------------
# Main
# ----------------------------

def main():

    start = time.time()

    logger.info("Loading applications...")

    apps = load_apps()[:10]

    logger.info(f"{len(apps)} apps loaded.")

    researcher = ResearchAgent()

    scraper = Scraper()

    verifier = VerificationAgent()

    raw_results = research_apps(

        apps,

        researcher

    )

    verified_results = verify_apps(

        raw_results,

        scraper,

        verifier

    )

    analysis = analyze_results(

        verified_results

    )

    generate_report(

        analysis,

        verified_results

    )

    end = time.time()

    logger.info(

        f"Pipeline completed in {round(end-start,2)} seconds."

    )


if __name__ == "__main__":

    main()