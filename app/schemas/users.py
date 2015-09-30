from .. import ma
from ..models.users import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


user_schema = UserSchema()
user_schema = UserSchema(many=True)
