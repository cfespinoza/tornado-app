"""Home page handlers"""
import logging
import tornado
from tornado import gen
from ..base.handlers import BaseHandler

LOGGER = logging.getLogger(__name__)

class HomeHandler(BaseHandler):
    """ Home page handler """
    @gen.coroutine
    def get(self):
        "GET method on home page"
        # user_locale = tornado.locale.get()
        # print(user_locale.translate("Sign out"))
        elementos = ["aaaaaa", "bbbbbbb", "ccccc"]
        self.render("home/home.html", elementos=elementos)
