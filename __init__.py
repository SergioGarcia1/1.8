from flask import Flask

app = Flask(__name__)

from app import routes



from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

# ...
from flask_login import LoginManager

app = Flask(__name__)
# ...
login = LoginManager(app)

# ...

