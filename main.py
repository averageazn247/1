import cgi
import datetime
import urllib
import wsgiref.handlers
import os
import json
import time
import datetime
import csv
import sys
import webapp2

from google.appengine.ext import ndb
from google.appengine.ext import db

from google.appengine.api import users

from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

from webapp2_extras import security

from google.appengine.ext.webapp import template

class BaseHandler(webapp2.RequestHandler):

 # @webapp2.cached_property
 # def auth(self):
   # return auth.get_auth()

 # @webapp2.cached_property
 # def user_info(self):
   # return self.auth.get_user_by_session()
	
 # @webapp2.cached_property
  #def user(self):
    #u = self.user_info
   # return self.user_model.get_by_id(u['user_id']) if u else None

  #@webapp2.cached_property
  #def session(self):
      #return self.session_store.get_session(backend="datastore")

  def render_template(self, view_filename, params={}):
    #user = self.user_info
    #params['user'] = user
    path = os.path.join(os.path.dirname(__file__), 'templates' ,view_filename)
    self.response.out.write(template.render(path,params))

 # def dispatch(self):
      #self.session_store = sessions.get_store(request=self.request)
      #try:
      #    webapp2.RequestHandler.dispatch(self)
     # finally:
        #  self.session_store.save_sessions(self.response)		  
class DirectionPage(BaseHandler):
  def get(self):
    self.render_template('direction.html')
class HomePage(BaseHandler):
  def get(self):
    self.render_template('homePage.html')
	
#class RegistrationPage(BaseHandler):

  #def get(self):
   # self.render_template('registration.html')
	
  #def post(self):
    #if self.request.get('userPassword') != self.request.get('confirm'):
	
     #   self.render_template('errorMessage.html', {'error': 'The passwords you entered do not match.'})
		
    #elif self.request.get('userPassword') == '' or self.request.get('firstName') == '' 
	#	 or self.request.get('lastName') == '' or self.request.get('userName') == '' 
	#	 or self.request.get('userName') == 'E-mail' or self.request.get('firstName') == 'First Name' 
	#	 or self.request.get('lastName') == 'Last Name':
		 
    #     self.render_template('errorMessage.html', {'Please properly complete the form.'})
		 
   # else:
    #    userName = self.request.get('userName')
    #    userEmail = self.request.get('userEmail')
    #    firstName = self.request.get('firstName')
	#	lastName = self.request.get('lastName')
       # userPassword = self.request.get('userPassword')        
       # collect = [' ']
       # unique_properties = ['email_address']
       # user_data = self.user_model.create_user(userName,
         # unique_properties,
         # email_address=email, name=name, password_raw=userPassword,
         # lastName=lastName, verified=False, collect=collect)
		  
        #if not user_data[0]: 
         # self.render_template('error.html', {'error': 'That user already exists!'})
         # return
        
        #user = user_data[1]
        #user_id = user.get_id()
        #self.render_template('facebook.html', {'confirm': True})


#config = {
#  'webapp2_extras.sessions': {
#    'secret_key': '9XKFL-8KCLQM-9M44AR-49C9D-LLO99'
#  }
#}

app = webapp2.WSGIApplication([
    webapp2.Route('/', HomePage, name='homePage'),
    webapp2.Route('/directPage/', DirectionPage, name='directPage'),
    #webapp2.Route('/login/', LoginPage, name='login'),
    #webapp2.Route('/logout/', LogoutPage, name='logout'),
    #webapp2.Route('/register/', RegisterPage, name='register'),
    #webapp2.Route('/facebook/', FacebookPage, name='facebook'),
], debug=True)


def main():
  app.RUN()


if __name__ == '__main__':
  main()