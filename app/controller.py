from app.models import Call


def get_list(number: str) -> list:
    list_for_return = []
    get_info_for_number_in = Call.query.filter_by(number_in=number).all()
    for item in get_info_for_number_in:
        list_for_return.append({
            'number_in': item.number_in,
            'number_target': item.number_target,
            'timestamp_start_call': item.timestamp_start_call,
            'timestamp_end_call': item.timestamp_end_call,
            'cost_call': item.cost_call
        })
    get_info_for_number_target = Call.query.filter_by(number_target=number).all()
    for item in get_info_for_number_target:
        list_for_return.append({
            'number_in': item.number_in,
            'number_target': item.number_target,
            'timestamp_start_call': item.timestamp_start_call,
            'timestamp_end_call': item.timestamp_end_call,
            'cost_call': item.cost_call
        })
    return list_for_return
