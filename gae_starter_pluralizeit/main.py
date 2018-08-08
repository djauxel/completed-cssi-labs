#main.py
import webapp2
import jinja2
import os
import logging
from pluralizer import *
from rps import *

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

winCount = 0
tieCount = 0
loseCount = 0

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/welcome.html')
        self.response.write(mypage.render())

class PluralizePage(webapp2.RequestHandler):
    def get(self):  # for a get request
        logging.info('in get self')
        mypage = env.get_template('templates/pluralize.html')
        self.response.write(mypage.render())

    def post(self):  # for a post request
        singular = self.request.get('singular')
        plural = pluralizer(singular)
        jinja_values = {"singular": singular, "plural": plural}
        mypage = env.get_template('templates/pluralize.html')
        self.response.write(mypage.render(jinja_values))

class RpsPage(webapp2.RequestHandler):
    def get(self): # for a get request
        mypage = env.get_template('templates/rps.html')
        self.response.write(mypage.render())
    
    def post(self): # for a post request
        playerMove = self.request.get('player_move')
        compMove = get_computer_move()
        #rpsResult = determine_winner(playerMove, compMove)  
        compWinChance = avgPercentWin()
        playerWinChance = 100 - compWinChance
        rpsResult = hal_9000(playerMove, compMove, compWinChance)

        global winCount, tieCount, loseCount # accesses the winCount variable
        winCount += player_wins(rpsResult)
        loseCount += player_losses(rpsResult)
        tieCount += player_ties(rpsResult)
        jinja_values = {"player_move": playerMove, 
                        "computer_move": compMove, 
                        "result": rpsResult,
                        "player_chance": playerWinChance,
                        "computer_chance": compWinChance, 
                        "player_wins": winCount,
                        "player_losses": loseCount,
                        "player_ties": tieCount}
        mypage = env.get_template('templates/rps.html')
        self.response.write(mypage.render(jinja_values))

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/pluralize', PluralizePage), 
    ('/rps', RpsPage)
], debug=True)
