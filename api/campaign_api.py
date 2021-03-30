from flask import jsonify, Response, request
from flask_restful import Resource, reqparse
from models.campaign import Campaign
from models.candidate_list import Candidate_List
from models.people_partner import People_Partner
from db import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


class CampaignApiParam(Resource):
    @staticmethod
    def get(campaign_id):
        session = Session()
        selected_campaign = session.query(Campaign).get(campaign_id)
        session.close()
        return {"data": {"campaign_id": selected_campaign["campaign_id"]}}, 200

    @staticmethod
    def put(campaign_id):
        session = Session()
        updated_campaign = session.query(Campaign).get(campaign_id)
        updated_campaign.campaign_name = request.args.get("campaign_name", updated_campaign["campaign_name"])
        updated_campaign.campaign_status = request.args.get("campaign_status", updated_campaign["campaign_status"])
        updated_campaign.candidate_list = request.args.get("candidate_list")
        if updated_campaign.candidate_list is not None:
            updated_candidate_list_id = updated_campaign["candidate_list_id"]
            updated_candidate_list = request.args.get(updated_candidate_list_id)
            updated_candidate_list.members = updated_campaign.candidate_list
        session.commit()
        session.close()
        return {"data": {"campaign_id": updated_campaign["campaign_id"]}}, 200

    @staticmethod
    def delete(campaign_id):
        session = Session()
        deleted_campaign = session.query(Campaign).get(campaign_id)
        session.delete()
        session.commit()
        session.close()
        return {"data": {"campaign_id": deleted_campaign["campaign_id"]}}, 200


class CampaignApi(Resource):
    @staticmethod
    def get():
        session = Session()
        selected_campaigns = select_campaigns()
        session.close()
        return {"data": selected_campaigns}, 200

    @staticmethod
    def post():
        session = Session()
        created_campaign = extract_campaign_data()
        session.add(created_campaign)
        session.commit()
        session.close()
        return {"data": created_campaign["campaign_id"]}, 201


def select_campaigns():
    session = Session()
    campaigns = session.query(Campaign.campaign_name, People_Partner.name, People_Partner.surname,
                              Campaign.status) \
        .select_from(Campaign) \
        .join(People_Partner, isouter=True)
    return campaigns


def extract_campaign_data():
    session = Session()
    campaign_name = request.args.get('campaign_name')
    campaign_status = request.args.get('status')
    candidate_list = request.args.get('candidate_list')

    created_candidate_list = Candidate_List(candidate_list)
    session.add(created_candidate_list)
    session.commit()

    campaign = Campaign(campaign_name, campaign_status,
                        created_candidate_list)
    return campaign
