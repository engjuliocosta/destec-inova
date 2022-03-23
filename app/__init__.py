from flask import Flask
from .schema import PlaceHoldSchema, configure_app

# from flask_migrate import Migrate
# from .model import configure as config_db

# Criação do App para execução no terminal
def create_app():
    app = Flask(__name__)
    configure_app(app)

    @app.route('/validate-json', methods=['POST'])
    def validate_json():
        # Tratamento de validação dos erros
        try:
            PlaceHoldSchema().loads(request.json)
            return jsonify({'ok': 'dados válidos'}, 201)
        except ValidationError as m_error:
            return jsonify(m_error.normalized_messages()), 400

    return app

    """

    ### Extensivo para SETUP de um DB ###

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/consphld.db' #Cuidar se é nome do app
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .jsonarray import bp_jsonph
    app.register_blueprint(bp_jsonph)

    """
