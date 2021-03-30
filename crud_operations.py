# from flask import jsonify
# from flask_restful import abort
# from sqlalchemy.orm import sessionmaker
# from models.campaign import Campaign
# from models.candidate_list import Candidate_List
# from models.people_partner import People_Partner
# from db import engine
#
# Session = sessionmaker(bind=engine)
#
#
# def get(id_, table_name):
#     if table_name == 'campaign':
#         table = Campaign
#     elif table_name == 'candidate_list':
#         table = Candidate_List
#     elif table_name == 'people_partner':
#         table = People_Partner
#     session = Session()
#     selected_item = session.query(table).filter_by(id=id_).first()
#     if not selected_item:
#         abort(406, message='This item is absent in the database')
#     session.close()
#
#     return jsonify({'data': selected_item.to_dict()})
#
#
# def get_all(table_name):
#     if table_name == 'campaign':
#         table = Campaign
#         session = Session()
#         selected_items = session.query(Campaign.campaign_name, People_Partner.name, People_Partner.surname,
#                                        Campaign.status) \
#                                 .select_from(Campaign) \
#                                 .join(People_Partner, isouter=True)
#         return selected_items
#
#     elif table_name == 'candidate_list':
#         table = Candidate_List
#     elif table_name == 'people_partner':
#         table = People_Partner
#


