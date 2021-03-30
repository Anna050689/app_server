from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import models.campaign as campaign

Base = declarative_base()


class People_Partner(Base):
    __tablename__ = 'people_partner'

    id_PP = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, ForeignKey("campaign.people_partner_phone"))

    def __init__(self, id_PP, name, surname, phone):
        self.id_PP = id_PP
        self.name = name
        self.surname = surname
        self.phone = phone
