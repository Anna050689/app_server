from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import models.candidate_list as candidate_list

Base = declarative_base()


class Campaign(Base):
    __tablename__ = 'campaign'

    people_partner_phone = Column(String(15), unique=True, nullable=False)
    campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_name = Column(String(50), nullable=False)
    candidate_list_id = Column(Integer, ForeignKey("candidate_list.id_list"))
    status = Column(String(10), nullable=False)

    def __init__(self, id_PP, campaign_id, campaign_name, candidate_list, status):
        self.id_PP = id_PP
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.candidate_list = candidate_list
        self.status = status