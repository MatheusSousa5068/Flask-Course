from flask import Flask
from SocialCompanyBlog.core.views import core
from SocialCompanyBlog.error_pages.handlers import error_pages

app = Flask(__name__)
app.register_blueprint(core)
app.register_blueprint(error_pages)