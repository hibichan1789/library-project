from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..database import get_session
from ..models import Book, BookDto

router = APIRouter(prefix="/books", tags=["books"])
#prefix:エンドポイントのパスの始まりを決める,tagがswagger上の表示を決める

@router.post("/", status_code=201)
def create_book(book_in:BookDto, session:Session=Depends(get_session)):
    db_book = Book.model_validate(book_in)#これで変換される
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@router.get("/")
def read_books(session:Session=Depends(get_session)):
    return session.exec(select(Book)).all()
# excelがクエリ
# 返ってきた結果をallがリストにする