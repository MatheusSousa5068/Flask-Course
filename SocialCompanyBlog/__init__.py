from flask import Flask
from SocialCompanyBlog.core.views import core

app = Flask(__name__)
app.register_blueprint(core)