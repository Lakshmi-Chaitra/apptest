import webapp2
import os
import jinja2
import urllib
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Entry(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    compliance= ndb.StringProperty(indexed=False)
    workload = ndb.StringProperty(indexed=False)

class MainPage(webapp2.RequestHandler):
  def get(self):
            
        Compliance = self.request.get("Compliance")
        Workload = self.request.get("Workload")
        template_values = {
            'Compliance': Compliance,
            'Workload': Workload,
        }
      
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    
  def post(self):
        entry = Entry()
        entry.compliance = self.request.get("Compliance")
        entry.workload = self.request.get("Workload")
        entry.put()
        print('Success')
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
