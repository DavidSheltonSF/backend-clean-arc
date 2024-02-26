from flask import request


def make_my_cache_key(*args, **kwargs) -> tuple:
    """Make a cache key

    Returns:
        tuple: Tuple that will be converted into a cache key
    """

    key = {}

    headers = request.headers
    body = request.get_json(silent=True)
    req_args = request.view_args

    # To generate a hash cache key it's necessary
    # convert all dictionaries into tuple
    if headers:
        key["headers"] = tuple(headers.items())

    if body:
        key["body"] = tuple(body.items())

    if req_args:
        key["args"] = tuple(req_args.items())

    return tuple(key.items())
