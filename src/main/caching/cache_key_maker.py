def make_cache_key() -> tuple:
    """Make a cache key

    Returns:
        tuple: Tuple that will be converted into a cache key
    """
    from flask import request

    key = {}

    headers = request.headers
    body = request.get_json(silent=True)
    args = request.args.to_dict()

    # To generate a hash cache key it's necessary
    # convert all dictionaries into tuple
    if headers:
        key["headers"] = tuple(headers.items())

    if body:
        key["body"] = tuple(body.items())

    if args:
        key["args"] = tuple(args.items())

    return tuple(key.items())
