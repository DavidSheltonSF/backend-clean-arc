from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask

    Args:
        request (any): Flask request
        api_route (Type[Route]): Composite Routes

    Returns:
        any: ....
    """

    # Get json from flask request
    http_request = HttpRequest(body=request.get_json())

    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
