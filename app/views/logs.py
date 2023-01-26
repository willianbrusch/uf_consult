from app.services.logs_service import get_state_info, get_logs, delete_log
from flask import Blueprint, request


bp_logs = Blueprint('logs', __name__)


@bp_logs.route('/search', methods=['GET'])
def get_state():
    search_state = request.args['state']
    ip = request.remote_addr

    return get_state_info(search_state, ip)


@bp_logs.route('/logs', methods=['GET'])
def get_all():
    return get_logs()


@bp_logs.route('/logs/<int:log_id>', methods=['DELETE'])
def delete(log_id):
    return delete_log(log_id)
