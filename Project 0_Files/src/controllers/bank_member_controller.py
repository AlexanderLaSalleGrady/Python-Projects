from src.models.bank_member import *

from flask import request, Response

from json import dumps

import src.services.bank_member_service as member_service

from src.controllers.flask_cf import app


@app.route('/clients/new', methods=['POST'])
def create_new_bank_member():
    client_json = request.get_json()
    # add logging here
    member_service.create_new_member(client_json)
    return Response("Member has been created!", status=201)


@app.route('/clients', methods=['GET'])
def get_all_bank_members():
    my_json = dumps(member_service.get_all_members(), cls=MemberEncoder)

    return Response(my_json, status=200)


@app.route('/clients/<int:bank_member_id>')
def get_client_by_id(bank_member_id):
    return member_service.get_member_by_id(bank_member_id)


@app.route('/clients/<int:bank_member_id>', methods=['PUT'])
def update_client_information(bank_member_id):
    return member_service.update_client_information(bank_member_id)


@app.route('/clients/<int:bank_member_id>', methods=['DELETE'])
def delete_client_by_id(bank_member_id):
    return member_service.delete_client_by_id(bank_member_id)


@app.route('/clients/<int:bank_member_id>/accounts', methods=['POST'])
def create_new_account_for_client_by_id(bank_member_id):
    return member_service.create_new_account_for_client_by_id(bank_member_id)


@app.route('/clients/<int:bank_member_id>/accounts', methods=['GET'])
def get_accounts_for_clients_by_id(bank_member_id):
    if 'lessThan' and 'greaterThan' in request.args:
        return member_service.get_accounts_for_client_between_value(bank_member_id)
    else:
        return member_service.get_accounts_by_client_id(bank_member_id)


@app.route('/clients/<int:bank_member_id>/accounts/<int:account_id>', methods=['GET'])
def get_single_account_by_client_id(bank_member_id, account_id):
    return member_service.get_single_account_by_client_id(bank_member_id, account_id)


@app.route('/clients/<int:bank_member_id>/accounts/<int:account_id>', methods=['PUT'])
def update_account_type_by_client_id(bank_member_id, account_id):
    return member_service.update_account_type_by_client_id(bank_member_id, account_id)


@app.route('/clients/<int:bank_member_id>/accounts/<int:account_id>', methods=['DELETE'])
def delete_account_by_client_id(bank_member_id, account_id):
    return member_service.delete_account_by_client_id(bank_member_id, account_id)


@app.route('/clients/<int:bank_member_id>/accounts/<int:account_id>', methods=['PATCH'])
def withdraw_or_deposit_funds_into_account(bank_member_id, account_id):
    return member_service.withdraw_or_deposit_funds_into_account(bank_member_id, account_id)


@app.route('/clients/<int:bank_member_id>/accounts/<int:account_id>/transfer/<int:transfer_account_id>', methods=['PATCH'])
def transfer_funds_between_accounts(bank_member_id, account_id, transfer_account_id):
    return member_service.transfer_funds_between_accounts(bank_member_id, account_id, transfer_account_id)

