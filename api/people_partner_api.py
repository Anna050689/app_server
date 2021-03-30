"""
API endpoints for people partner entity
"""

from flask_restful import Resource, reqparse
from flask import Response, jsonify

campaign_args = reqparse.RequestParser()
# TODO set people partner arguments, args types, required or not


class PeoplePartnerApi(Resource):
    """
    handlers for APIs without parameters
    """

    @staticmethod
    def get():
        # TODO add logic and functionality
        return Response(response=jsonify({"data": ['all', 'items']}), status=200)

    @staticmethod
    def post():
        # TODO add logic and functionality
        return Response(response=jsonify({"data": "new created item"}), status=201)

    @staticmethod
    def put():
        # TODO add logic and functionality
        return Response(response=jsonify({"data": "edited item"}), status=200)
