# Patient History Summarizer

A simple Streamlit web application that extracts text from patient case sheet PDFs and generates a structured medical summary using an OpenAI model.

## Features

- Upload a patient case sheet in PDF format
- Extract raw text from the PDF
- Send the text to an OpenAI model with a constrained prompt
- Validate and structure the response using Pydantic models
- Display:
  - Patient overview
  - Chief complaints
  - Diagnosis
  - Medications
  - Lab findings
  - Treatment given
  - Risks & alerts
  - Timeline of events
  - Doctor handoff summary

## Project Structure

- `app.py`: Streamlit frontend for uploading PDFs and displaying the summary
- `summarizer.py`: Backend logic for calling the OpenAI API and validating the response
- `prompt.yaml`: Prompt template that constrains the model output to a specific JSON schema
- `schema.py`: Pydantic models (`TimelineEvent`, `CaseSheetSummary`) describing the expected summary structure
- `utils.py`: Helper for extracting text from PDF files using PyMuPDF (`fitz`)
- `requirements.txt`: Python package dependencies

## Prerequisites

- Python 3.9+ (recommended)
- An OpenAI API key with access to the `gpt-4.1-mini` model (or update the model name in `summarizer.py`)

## Installation

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key. For example, using an environment variable:

   ```bash
   set OPENAI_API_KEY="your_api_key_here"  # On Windows (cmd)
   # or
   export OPENAI_API_KEY="your_api_key_here"  # On macOS/Linux
   ```

4. Update `app.py` / `summarizer.py` to read the key from the environment instead of hardcoding it, for example:

   ```python
   import os
   api_key = os.environ["OPENAI_API_KEY"]
   ```

## Running the App

From the project root directory:

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (typically `http://localhost:8501`).

## Usage

1. Open the Streamlit app in your browser.
2. Upload a patient case sheet as a PDF.
3. Review the extracted text preview.
4. Click **"Summarize Case Sheet"**.
5. Wait for the model to process and then review the structured summary sections.

## Notes & Limitations

- This tool is intended for assisting clinicians, not replacing them. Always verify the output against the original case sheet.
- The quality of the summary depends heavily on the quality and completeness of the input PDF.
- The current implementation expects the model to return valid JSON as specified in `prompt.yaml`. If the model output is malformed JSON, `json.loads` or Pydantic validation may raise an error.
- The API key is currently hardcoded in `app.py`; for production or sharing, move this to a secure configuration mechanism (environment variables, secrets manager, etc.).
