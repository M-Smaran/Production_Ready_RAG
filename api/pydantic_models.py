from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    """Enum for model names."""
    GPT4_O = "gpt-4o"
    GPT4_O_MINI = "gpt-4o-mini"

class Queryinput(BaseModel):
    """Pydantic model for user query input."""
    session_id: str = Field(..., description="Unique identifier for the session")
    question: str = Field(..., description="User query")
    model: ModelName = Field(..., description="Model name to be used")
    

class QueryResponse(BaseModel):
    answer : str
    session_id : str
    model : ModelName

class DocumentInfo(BaseModel):
    id : int
    filename : str
    upload_timestamptp : datetime

class DeleteFileRequest(BaseModel):
    file_id : int 