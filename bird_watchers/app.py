from app_common.create_app import create_connexion_app

connexion_app = create_connexion_app("bird_watchers")
connexion_app.run(port=8080)
