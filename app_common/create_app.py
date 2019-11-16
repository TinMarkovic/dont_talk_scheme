from connexion.apps.flask_app import FlaskApp
from connexion.resolver import RestyResolver
from prance import ResolvingParser
from pathlib import Path


def create_connexion_app(package_name: str) -> FlaskApp:
    connexion_app = FlaskApp(package_name)

    spec = Path() / 'openapi.yaml'
    parser = ResolvingParser(str(spec), backend="openapi-spec-validator")
    connexion_app.openapi_schema = parser.specification

    connexion_app.add_api(
        connexion_app.openapi_schema,
        validate_responses=True,
        strict_validation=True,
        resolver=RestyResolver("{}.handlers".format(package_name)),
    )
    return connexion_app
