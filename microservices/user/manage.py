from flask.cli import FlaskGroup
from flask_migrate import MigrateCommand
from flask_migrate import Migrate

from app import app
from app import db

cli = FlaskGroup(app)
migrate = Migrate(app, db)

@cli.command("create_db")
def create_db():
    migrate.db.drop_all()
    migrate.db.create_all()
    migrate.db.session.commit()

@cli.command("db")
def db():
    return MigrateCommand

if __name__ == "__main__":
    cli()
