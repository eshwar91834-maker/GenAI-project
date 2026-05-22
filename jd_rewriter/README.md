# JD Rewriter

A Streamlit-powered web application that rewrites jargon-heavy job descriptions into clear, concise, and detailed versions using GPT-4.1-mini.

## Features

- Rewrites any job description into two distinct versions:
  - **Concise** — ~300 words, clear and to the point
  - **Detailed** — ~500 words, engaging and comprehensive
- Configurable temperature for creativity control
- Inclusivity-first prompts that avoid buzzwords and jargon
- Few-shot examples for consistent, high-quality output

## Project Structure

```
jd_rewriter/
├── app.py              # Streamlit web UI
├── jd_rewrited.py      # Core logic — OpenAI API calls
├── schema.py           # Pydantic response model
├── prompts.yaml        # System prompt, few-shot examples, and task prompts
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Before running the app, set your OpenAI API key in `jd_rewrited.py:13`:

```python
client = OpenAI(api_key="your_openai_api_key_here")
```

Alternatively, set it as an environment variable and update the code accordingly.

## Usage

```bash
streamlit run app.py
```

Then open the displayed local URL (usually `http://localhost:8501`) in your browser.

## How It Works

1. The Streamlit UI (`app.py`) accepts a job description string and a temperature value.
2. `jd_rewrited.py` loads system prompts and few-shot examples from `prompts.yaml`.
3. The job description is formatted into a **concise prompt** and a **detailed prompt**.
4. Both prompts are sent to `gpt-4.1-mini` via the OpenAI API.
5. The response is validated against `RewriteResponse` (a Pydantic model with `concise_version` and `detailed_version` fields) in `schema.py`.
6. Both rewritten versions are displayed in the web UI.

## Dependencies

| Package | Purpose |
|---|---|
| streamlit | Web UI framework |
| openai     | OpenAI API client |
| pydantic   | Response schema validation |
| PyYAML     | Load prompt configuration from YAML |
