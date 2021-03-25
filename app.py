from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)

campaigns = [
    {
        'id_PP': 1,
        'campaign_id': 1,
        'campaign_name': 'Java',
        'candidate_list': ['Olga', 'Anna', 'Alex'],
        'status': 'new'
    },
    {
        'id_PP': 2,
        'campaign_id': 2,
        'campaign_name': 'Python',
        'candidate_list': ['Dmytro', 'Olena', 'Danilo'],
        'status': 'new'
    }
]

candidate_lists = [
    {
        'id_list': 1,
        'members': ['Olga', 'Anna', 'Alex']
    },
    {
        'id_list': 2,
        'members': ['Dmytro', 'Olena', 'Danilo']
    }
]

people_partners = [
    {
        'id_PP': 1,
        'name': 'Anna',
        'surname': 'Petrova',
        'phone': '+38(099)1467234'
    },
    {
        'id_PP': 2,
        'name': 'Olga',
        'surname': 'Ivanova',
        'phone': '+38(093)1467231'
    }
]


@app.route('/campaigns', methods=['GET'])
def get_all_campaigns():
    return jsonify({'campaigns': campaigns})


@app.route('/campaigns/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    campaign = list(filter(lambda t: t['campaign_id'] == campaign_id, campaigns))
    if len(campaign) == 0:
        abort(404)
    return jsonify({'campaign': campaign[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/campaigns', methods=['POST'])
def create_campaign():
    if not request.json or not 'campaign_name' in request.json:
        abort(404)
    campaign = {
        'id_PP': request.json.get('id_PP'),
        'campaign_id': campaigns[-1]['campaign_id'] + 1,
        'campaign_name': request.json.get('campaign_name'),
        'candidate_list': request.json.get('candidate_list'),
        'status': 'new'
    }
    campaigns.append(campaign)
    return jsonify({'campaign': campaign})


@app.route('/campaigns/<int:campaign_id>', methods=['PUT'])
def update_campaign(campaign_id):
    campaign = list(filter(lambda t: t['campaign_id'] == campaign_id, campaigns))
    if len(campaign) == 0:
        abort(404)
    if not request.json:
        abort(400)
    campaign[0]['id_PP'] = request.json.get('id_PP', campaign[0]['id_PP'])
    campaign[0]['campaign_id'] = request.json.get('campaign_id', campaign[0]['campaign_id'])
    campaign[0]['campaign_name'] = request.json.get('campaign_name', campaign[0]['campaign_name'])
    campaign[0]['candidate_list'] = request.json.get('candidate_list', campaign[0]['candidate_list'])
    campaign[0]['status'] = request.json.get('status', campaign[0]['status'])
    return jsonify({'campaign': campaign[0]})


@app.route('/campaigns/<int:campaign_id>', methods=['DELETE'])
def delete_campaign(campaign_id):
    campaign = list(filter(lambda t: t['campaign_id'] == campaign_id, campaigns))
    if len(campaign) == 0:
        abort(404)
    campaigns.remove(campaign[0])
    return jsonify({'The campaign was deleted': True})


@app.route('/candidate_lists', methods=['GET'])
def get_all_candidates_lists():
    return {'candidate_lists': candidate_lists}


@app.route('/candidate_lists/<int:id_list>', methods=['GET'])
def get_candidate_list(id_list):
    candidate_list = list(filter(lambda t: t['id_list'] == id_list, candidate_lists))
    if len(candidate_list) == 0:
        abort(404)
    return jsonify({'candidate_list': candidate_list[0]})


@app.route('/candidate_lists', methods=['POST'])
def create_candidate_list():
    if not request.json:
        abort(404)
    if len(request.json.get('members')) == 0:
        return jsonify({'candidate_list': 'empty'})
    candidate_list = {
        'id_list': candidate_lists[-1]['id_list'] + 1,
        'members': ['Nikita', 'Oleg']
    }
    candidate_lists.append(candidate_list)
    return jsonify({'candidate_list': candidate_list})


@app.route('/candidate_lists/<int:id_list>', methods=['PUT'])
def update_candidate_list(id_list):
    candidate_list = list(filter(lambda t: t['id_list'] == id_list, candidate_lists))
    if len(candidate_list) == 0:
        abort(404)
    if not request.json:
        abort(400)
    candidate_list[0]['id_list'] = request.json.get('id_PP', candidate_list[0]['id_list'])
    candidate_list[0]['members'] = request.json.get('members', candidate_list[0]['members'])
    return jsonify({'candidate_list': candidate_list[0]})


@app.route('/candidate_lists/<int:id_list>', methods=['DELETE'])
def delete_candidate_list(id_list):
    candidate_list = list(filter(lambda t: t['id_list'] == id_list, candidate_lists))
    if len(candidate_lists) == 0:
        abort(404)
    candidate_lists.remove(candidate_list[0])
    return jsonify({'The list of candidates was deleted': True})


@app.route('/people_partners', methods=['GET'])
def get_all_people_partners():
    return jsonify({'people_partners': people_partners})


@app.route('/people_partners/<int:id_PP>', methods=['GET'])
def get_people_partner(id_PP):
    people_partner = list(filter(lambda t: t['id_PP'] == id_PP, people_partners))
    if len(people_partner) == 0:
        abort(404)
    return jsonify({'people_partner': people_partner[0]})


@app.route('/people_partners', methods=['POST'])
def add_people_partner():
    if not request.json or not 'name' in request.json and not 'surname' in request.json:
        abort(404)
    people_partner = {
        'id_PP': people_partners[-1]['id_PP'] + 1,
        'name': request.json.get('name'),
        'surname': request.json.get('surname'),
        'phone': request.json.get('phone')
    }
    people_partners.append(people_partner)
    return jsonify({'people_partner': people_partner})


@app.route('/people_partners/<int:id_PP>', methods=['PUT'])
def update_people_partner(id_PP):
    people_partner = list(filter(lambda t: t['id_PP'] == id_PP, people_partners))
    if len(people_partner) == 0:
        abort(404)
    if not request.json:
        abort(400)
    people_partner[0]['id_PP'] = request.json.get('id_PP', people_partner[0]['id_PP'])
    people_partner[0]['name'] = request.json.get('name', people_partner[0]['name'])
    people_partner[0]['surname'] = request.json.get('surname', people_partner[0]['surname'])
    people_partner[0]['phone'] = request.json.get('phone', people_partner[0]['phone'])
    return jsonify({'people_partner': people_partner[0]})


@app.route('/people_partners/<int:id_PP>', methods=['DELETE'])
def delete_people_partner(id_PP):
    people_partner = list(filter(lambda t: t['id_PP'] == id_PP, people_partners))
    if len(people_partner) == 0:
        abort(404)
    people_partners.remove(people_partner[0])
    return jsonify({'The people partner was deleted': True})


if __name__ == '__main__':
    app.run(debug=True)


