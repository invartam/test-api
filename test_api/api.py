import connexion

from swagger_ui_bundle import swagger_ui_3_path

options = {'swagger_path': swagger_ui_3_path}
application = connexion.FlaskApp(__name__, specification_dir="spec/", options=options)
application.add_api("api.yaml")
