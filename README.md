# Composio Research Agent

This project is an AI-powered research pipeline that collects, verifies, analyzes, and generates reports for SaaS applications.

## Features

- Researches SaaS applications using Groq LLM
- Scrapes product documentation
- Verifies extracted information using AI
- Generates analysis reports
- Creates an HTML report with summarized results

## Tech Stack

- Python 3.10+
- Groq API
- Jinja2
- Plotly
- Pandas
- BeautifulSoup4

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Rakshithabmsce/composio-research.git
cd composio-research
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

## Run the Research Agent

Execute:

```bash
python run.py
```

The pipeline performs:

1. Research
2. Documentation scraping
3. Verification
4. Analysis
5. HTML report generation

## Output

Generated files:

```
data/raw_results.json
data/verified_results.json
data/analysis.json
reports/report.html
```

Open:

```
reports/report.html
```

to view the generated report.

## Repository

https://github.com/Rakshithabmsce/composio-research
