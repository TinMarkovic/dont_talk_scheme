from app_common.create_app import create_connexion_app

connexion_app = create_connexion_app("bird_keepers")
connexion_app.run(port=8081)
