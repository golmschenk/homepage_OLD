"""
The main crowd navigation application file. Initializes the app. Handles and redirects requests to the app.
"""
import webapp2
import os
import jinja2

#Run in debug mode if on dev_appengine.
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.dirname(__file__), os.path.dirname(__file__) + "/templates"]),
    variable_start_string="((",
    variable_end_string="))")


class LandingPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.write(template.render())


class ProposalPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('proposal.html')
        self.response.write(template.render())


application = webapp2.WSGIApplication([
                                      ('/', LandingPage),
                                      ('/proposal', ProposalPage),
                                      ], debug=debug)

