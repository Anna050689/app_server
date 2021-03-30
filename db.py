"""
Initializing db and db session module
"""
import logging
from sqlalchemy import create_engine, exc
from models import campaign, candidate_list, people_partner

DB_CONN = 'postgresql+psycopg2://postgres:root@localhost:5433/chatbot'

def create_db_if_not_exists():
    """
    creates database if it not exists
    :return:
    """
    try:
        db_check = create_engine(DB_CONN + '/chatbot', echo=True)
        db_check.connect()
    except exc.OperationalError:
        try:
            db_engine = create_engine(DB_CONN)
            connection = db_engine.connect()
            connection.execute("commit")
            connection.execute("select 'create database chatbot' where not exists "
                               "(select from pg_database WHERE datname = 'chatbot')")
            connection.close()
            db_en = create_engine(DB_CONN + '/chatbot', echo=True)
            campaign.Base.metadata.create_all(bind=db_en)
            candidate_list.Base.metadata.create_all(bind=db_en)
            people_partner.Base.metadata.create_all(bind=db_en)
        except exc.OperationalError:
            logging.log(logging.WARNING, 'cannot create connection to db: %s', DB_CONN)


def db_conn():
    """
    returns engine
    :return:
    """
    return create_engine(DB_CONN + '/chatbot', echo=True)


engine = db_conn()

