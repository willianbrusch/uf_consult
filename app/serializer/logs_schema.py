from app.models import ma, Log


class LogSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Log

    id = ma.auto_field()
    user_ip = ma.auto_field()
    searched_state = ma.auto_field()
    date_access = ma.auto_field()
