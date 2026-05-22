PROMPT_TEMPLATE = """
You are an expert business analyst.
Covert the following raw meeting notes into structures meeting minutes.

Requirements:
 - Extract agenda items
 - Extract decisions made
 - Extract action items with owner and due date
 - Create a concise summary of the meeting
 - Indentify next meeting details if available 

Retun ONLY valid JSON.

JSON Format:
{
  "meeting_title": "string",
  "summary": "string",
  "agenda_items": ["item1", "item2"],
  "decisions": [
    {
      "decision": "string",
      "owner": "string"
    }
  ],
  "action_items": [
    {
      "task": "string",
      "owner": "string",
      "due_date": "string"
    }
  ],
  "next_meeting": "string"
}

Meeting Notes:
{{meeting_notes}}
"""