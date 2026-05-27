#backend
import json
import yaml
from openai import OpenAI

from schema import CaseSheetSummary


with open("prompt.yaml", "r") as f:
    prompts = yaml.safe_load(f)

SUMMARY_PROMPT = prompts["SUMMARY_PROMPT"]

def summarize_case_sheet(case_sheet_text, api_key):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SUMMARY_PROMPT},
            {"role": "user", "content": case_sheet_text}
        ],
        temperature=0.2
    )
    summary = response.choices[0].message.content
    content = summary.strip()
    print("Raw Summary Output:", content)
    parsed_json = json.loads(content)
    print("Parsed JSON:", parsed_json)

    validated_summary = CaseSheetSummary(**parsed_json)

    return validated_summary