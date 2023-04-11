
empty_response = {
    'code': 0,
    'data': '',
}

unknown_error = {
    'error': 'Unknown error',
    'msg': 'Server encountered an unknown error',
    'code': -1,
    'data': ''
}

rate_limit_exceeded = {
    "error": "Rate limit exceeded",
    'msg': 'Too many requests',
    'code': -2,
    'data': ''
}

host_not_allowed = {
    'error': 'Host not allowed',
    'msg': 'Host not allowed',
    'code': -3,
    'data': ''
}

