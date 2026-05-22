from pydantic import BaseModel

class RewriteResponse(BaseModel):
    concise_version: str
    detailed_version: str