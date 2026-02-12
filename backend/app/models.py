from typing import Optional
from sqlmodel import Field, SQLModel

class BookBase(SQLModel):
    title:str
    author:str
    description:Optional[str] = Field(default=None)

class BookDto(BookBase):
    pass

class Book(BookBase, table=True):#table=TrueでDBのテーブルになる
    id: Optional[int] = Field(default=None, primary_key=True)#これが自動採番のIDになる