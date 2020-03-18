import webapp2
import os
import jinja2

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
        Entry.compliance = self.request.get("Compliance")
        Entry.workload = self.request.get("Workload")
        Entry.put()
        print("Input added to Datastore")
    
app = webapp2.WSGIApplication([('/', MainPage)], debug= True)
  
