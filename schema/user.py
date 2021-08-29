from models.user import User
import marshmallow_sqlalchemy as ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User