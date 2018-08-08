#main.py
#the import section
import webapp2

#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, Youwen!') 

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
