from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

    tables = db.Model.metadata.tables.keys()
    print("Список таблиц в базе данных:")
    for table in tables:
            print(table)

    with app.app_context():
        db.create_all()

