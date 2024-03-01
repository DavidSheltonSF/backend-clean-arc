from typing import Dict


class HttpRequest:
    """Class to http__request representation"""

    def __init__(self, header: Dict = None, body: Dict = None, view_args: Dict = None):
        self.header = header
        self.body = body
        self.view_args = view_args

    def __repr__(self):
        return f"HttpRequest (header={self.header}, body={self.body}, view_arg={self.view_arg})"


class HttpResponse:
    """Class to http_respose representation"""

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"
