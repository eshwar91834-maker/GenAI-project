import json
from openai import OpenAI
import os
from prompts import PROMPT_TEMPLATE
from dotenv import load_dotenv
from schema import MeetingMinutes
from jinja2 import Template

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_meeting_minutes(meeting_notes:str):
    template = Template(PROMPT_TEMPLATE)
    final_prompt = template.render(meeting_notes=meeting_notes)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You generate structured meeting minutes in JSON."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.2
    )

    raw_output = response.choices[0].message.content

    parsed_json = json.loads(raw_output)
    meeting_minutes = MeetingMinutes(**parsed_json)
    return {"success": True, "data": meeting_minutes}