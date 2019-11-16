from connexion.apps.flask_app import FlaskApp
from connexion.resolver import RestyResolver


def create_connexion_app(package_name: str) -> FlaskApp:
    connexion_app = FlaskApp(package_name)

    connexion_app.add_api(
        'schema/openapi.yaml',
        validate_responses=True,
        strict_validation=True,
        resolver=RestyResolver("{}.handlers".format(package_name)),
    )
    return connexion_app
