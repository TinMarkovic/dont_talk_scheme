from os import path
from importlib import import_module

from connexion.apps.flask_app import FlaskApp
from connexion.resolver import RestyResolver

from app_common.schema_loader import prepare_schema


def create_connexion_app(package_name: str) -> FlaskApp:
    connexion_app = FlaskApp(package_name)

    package = import_module(package_name)
    base_package = import_module("avian_schema")
    connexion_app.openapi_schema = prepare_schema(
        [
            "{}/schema".format(path.dirname(path.realpath(package.__file__))),
            "{}/schema".format(path.dirname(path.realpath(base_package.__file__))),
        ]
    )

    connexion_app.add_api(
        connexion_app.openapi_schema,
        validate_responses=True,
        strict_validation=True,
        resolver=RestyResolver("{}.handlers".format(package_name)),
    )
    return connexion_app


connexion_app = create_connexion_app("bird_watchers")
connexion_app.run(port=8080)
