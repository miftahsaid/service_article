from cgitb import text
from datetime import datetime, time
from typing import Literal, List
from pydantic import BaseModel, Field

class Post_(BaseModel):
    Title : str = Field(title="minimal 20 karakter",min_length=20)
    Content : str = Field(title="minimal 200 karakter",min_length=200)
    Category : str = Field(title="minimal 3 karakter",min_length=3)
    Created_date : datetime
    Updated_date : datetime
    Status : List[Literal["publish", "draft","trash"]] = Field(title="status : publish / draft / trash")



