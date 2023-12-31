import logging

import connexion
from flask_testing import TestCase

from server.config.json_encoder import CustomJSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = CustomJSONEncoder
        app.add_api('swagger.yaml')
        return app.app
