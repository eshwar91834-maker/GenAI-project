from typing import List, Optional
from pydantic import BaseModel

class ActionItem(BaseModel):
    task: str
    owner: str
    due_date: Optional[str] = "Not specified"

class Decision(BaseModel):
    decision: str
    owner: Optional[str] = "Not specified"


class MeetingMinutes(BaseModel):
    meeting_title: str
    summary: str
    agenda_items: List[str]
    decisions: List[Decision]
    action_items: List[ActionItem]
    next_meeting: Optional[str] = "Not specified"