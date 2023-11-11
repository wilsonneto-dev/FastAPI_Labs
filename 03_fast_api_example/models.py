from typing import Optional
from pydantic import BaseModel

class Thread(BaseModel):
    id: Optional[str]
    title: str
    description: str
    
