from typing import NoReturn
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields


ma = Marshmallow()

class PlaceHoldSchema(ma.Schema):
    id = fields.Raw(required=True)
    title = fields.Raw(required=True)

    class Meta:
        fields = ('id',
                  'title',
                )

        ...
def configure_app(app) -> NoReturn:
    ma.init_app(app)
