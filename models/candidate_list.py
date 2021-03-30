from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Candidate_List(Base):
    __tablename__ = 'candidate_list'

    id_list = Column(Integer, primary_key=True, autoincrement=True)
    members = Column(String, nullable=False)

    def __init__(self, members):
        self.members = members
