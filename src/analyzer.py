from collections import Counter


class Analyzer:

    def analyze(self, apps):

        auth_counter = Counter()

        category_counter = Counter()

        blocker_counter = Counter()

        buildability_counter = Counter()

        mcp_counter = Counter()

        confidence = []

        for app in apps:

            auth_counter[app.get("authentication", "Unknown")] += 1

            category_counter[app.get("category", "Unknown")] += 1

            blocker_counter[app.get("blocker", "Unknown")] += 1

            buildability_counter[app.get("buildability", "Unknown")] += 1

            mcp_counter[app.get("mcp_support", "Unknown")] += 1

            confidence.append(app.get("confidence", 0))

        avg = 0

        if confidence:

            avg = sum(confidence) / len(confidence)

        return {

            "total_apps": len(apps),

            "average_confidence": round(avg, 2),

            "authentication": dict(auth_counter),

            "categories": dict(category_counter),

            "blockers": dict(blocker_counter),

            "buildability": dict(buildability_counter),

            "mcp": dict(mcp_counter)

        }