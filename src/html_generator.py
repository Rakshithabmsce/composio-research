import os
import pandas as pd
import plotly.express as px
from jinja2 import Environment, FileSystemLoader


class HTMLGenerator:

    def generate(
        self,
        analysis,
        results,
        output="reports/report.html"
    ):

        os.makedirs("reports", exist_ok=True)

        df = pd.DataFrame(results)

        # Authentication chart
        auth = px.bar(
            x=list(analysis["authentication"].keys()),
            y=list(analysis["authentication"].values()),
            title="Authentication Methods"
        )

        # Category chart
        category = px.pie(
            names=list(analysis["categories"].keys()),
            values=list(analysis["categories"].values()),
            title="Categories"
        )

        # Load HTML template
        env = Environment(
            loader=FileSystemLoader("templates")
        )

        template = env.get_template(
            "report_template.html"
        )

        html = template.render(
            analysis=analysis,
            auth_chart=auth.to_html(
                include_plotlyjs="cdn",
                full_html=False
            ),
            category_chart=category.to_html(
                include_plotlyjs=False,
                full_html=False
            ),
            table=df.to_html(
                index=False,
                escape=False,
                classes="display"
            )
        )

        with open(
            output,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(html)

        print(f"HTML Report Generated: {output}")