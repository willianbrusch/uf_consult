from flask import current_app
from app.models import Log
from app.serializer.logs_schema import LogSchema
from http import HTTPStatus

import json
import urllib3
from urllib3.util.ssl_ import create_urllib3_context


def get_state_info(search_state: str, user_ip: str):

    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{search_state}"

    response = {}
    ctx = create_urllib3_context()
    ctx.load_default_certs()
    ctx.options |= 0x4

    with urllib3.PoolManager(ssl_context=ctx) as http:
        res = http.request("GET", url)
        response = res.data

    if not response:
        return {'message': 'Not found'}, HTTPStatus.NOT_FOUND

    state = json.loads(response.decode('utf-8'))

    log = Log(user_ip=user_ip, searched_state=state["sigla"])

    current_app.db.session.add(log)
    current_app.db.session.commit()

    return state, HTTPStatus.OK


def get_logs():
    return LogSchema(many=True).dump(Log.query.all()), HTTPStatus.OK


def delete_log(delete_id: int):

    log = Log.query.filter_by(id=delete_id).first()

    if log == None:
        return {'message': 'Not found'}, HTTPStatus.NOT_FOUND

    current_app.db.session.delete(log)
    current_app.db.session.commit()

    return {'message': 'Deleted'}, HTTPStatus.OK
