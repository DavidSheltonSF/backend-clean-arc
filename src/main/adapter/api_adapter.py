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

    # Try convert user_id or pet_it into integer
    try:

        view_args = request.view_args

        # Check if pet_id is in view_args
        if "pet_id" in view_args.keys():
            view_args["pet_id"] = int(view_args["pet_id"])

        # Check if user_id is in query_string_params
        if "user_id" in view_args.keys():
            view_args["user_id"] = int(view_args["user_id"])

    # If coldn't convert IDs
    except:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    # Get headers, body and query from flask request
    http_request = HttpRequest(
        header=request.headers,
        body=request.get_json(silent=True),
        view_args=view_args,
    )

    # Try do a request to route
    try:
        response = api_route.route(http_request)

    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    # Unknown error
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
