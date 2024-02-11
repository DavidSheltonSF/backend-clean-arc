class HttpErrors:
    """Class to define erros in http"""

    @staticmethod
    def error_422():
        "HTTP 422"
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        "HTTP 400"
        return {"status_code": 400, "body": {"error": "Bad Request"}}
