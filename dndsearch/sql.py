import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, distinct, Text


MYSQL_USER = 'dnd'
MYSQL_PASS = 'dndpassword'
MYSQL_HOST = 'localhost'
MYSQL_DB = 'dnd'

engine = sqlalchemy.create_engine("mysql://%s:%s@%s/%s" % (
    MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_DB),
    pool_size=6, pool_recycle=600)

Session = sessionmaker(bind=engine)
Base = declarative_base()

class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    book = Column(String(150))
    page = Column(Integer)
    text = Column(Text)


    def __init__(self, book, page, text):
        self.book = book
        self.page = page
        self.text = text


    @staticmethod
    def add(page, session=(Session()), commit=True, close=False):
        session.add(page)
        if commit:
            session.commit()

    # Returns a list of matching page numbers
    @staticmethod
    def search(query, session=(Session())):
        try:
            q = session.query(Page).from_statement(
                "SELECT book, page FROM page \
                WHERE match (text) \
                AGAINST (\"%s\")" % query)
            return [(p[0], p[1]) for p in q.values('book', 'page')]
        finally:
            session.close()
