from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from config import Configuration
from db import create_db_if_not_exists
from models.campaign import Campaign
from models.candidate_list import Candidate_List
from models.people_partner import People_Partner

from api.campaign_api import CampaignApi, CampaignApiParam
from api.people_partner_api import PeoplePartnerApi

# This test module works independently from other modules

app = Flask(__name__)
api_server = Api(app)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


api_server.add_resource(CampaignApi, '/api/v1/campaigns')
api_server.add_resource(CampaignApiParam, '/api/v1/campaigns/<campaign_id>')
api_server.add_resource(PeoplePartnerApi, '/api/v1/people_partners')


# campaigns = [
#     {
#         'id_PP': 1,
#         'campaign_id': 1,
#         'campaign_name': 'Java',
#         'candidate_list': ['Olga', 'Anna', 'Alex'],
#         'status': 'new'
#     },
#     {
#         'id_PP': 2,
#         'campaign_id': 2,
#         'campaign_name': 'Python',
#         'candidate_list': ['Dmytro', 'Olena', 'Danilo'],
#         'status': 'new'
#     }
# ]
#
# candidate_lists = [
#     {
#         'id_list': 1,
#         'members': ['Olga', 'Anna', 'Alex']
#     },
#     {
#         'id_list': 2,
#         'members': ['Dmytro', 'Olena', 'Danilo']
#     }
# ]
#
# people_partners = [
#     {
#         'id_PP': 1,
#         'name': 'Anna',
#         'surname': 'Petrova',
#         'phone': '+38(099)1467234'
#     },
#     {
#         'id_PP': 2,
#         'name': 'Olga',
#         'surname': 'Ivanova',
#         'phone': '+38(093)1467231'
#     }
# ]
create_db_if_not_exists()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run(debug=True)


