#main.py
#the import section
import webapp2

#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello!')

class SecondPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Goodbye!')

#the app configuration section
app = webapp2.WSGIApplication([
    ('/hi', MainPage),
    ('/bye', SecondPage)
], debug=True)
