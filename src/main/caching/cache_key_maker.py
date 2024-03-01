from flask import request


def make_my_cache_key(*args, **kwargs) -> tuple:
    """Make a cache key

    Returns:
        tuple: Tuple that will be converted into a cache key
    """

    key = {}

    headers = request.headers
    body = request.get_json(silent=True)
    view_args = request.view_args
    query_params = request.args

    # To generate a hash cache key it's necessary
    # convert all dictionaries into tuple
    if headers:
        key["headers"] = tuple(headers.items())

    if body:
        key["body"] = tuple(body.items())

    if view_args:
        key["args"] = tuple(view_args.items())

    if query_params:
        key["query_params"] = tuple(query_params.items())

    return tuple(key.items())
