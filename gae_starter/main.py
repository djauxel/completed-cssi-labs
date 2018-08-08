#main.py
import webapp2
import jinja2
import os
import logging
import datetime
from lmao import ay

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('This is the welcome page')
        mypage = env.get_template('templates/welcome.html')
        self.response.write(mypage.render({'name': 'alex',
                                            'age': 18,
                                            'clock': datetime.datetime.now()}))

class SecondPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('This is the pluralize page')
        mypage = env.get_template('templates/pluralize.html')
        self.response.write(mypage.render())

    def post(self):  # for a post method
        word = self.request.get('singular')
        words = ay(word)
        jinja_values = {'singular': word, 'plural': words}
        mypage = env.get_template('templates/pluralize.html')
        self.response.write(mypage.render(jinja_values))

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/pluralize', SecondPage),
], debug=True)
