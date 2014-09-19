"""
The main crowd navigation application file. Initializes the app. Handles and redirects requests to the app.
"""
import webapp2
import os
import jinja2

#Run in debug mode if on dev_appengine.
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.dirname(__file__), os.path.dirname(__file__) + "/templates"]))


class LandingPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('landing.html')
        self.response.write(template.render())


class EssayPage(webapp2.RequestHandler):
    def get(self, essay_name):
        with open('essays/' + essay_name + '.essay') as file_handle:
            file_lines = file_handle.read().decode('utf-8').split('\n')
            #Filter out blank lines.
            file_content = [line for line in file_lines if line]
            template_variables = {'essay_title': file_lines[0],
                                  'publisher': file_lines[1],
                                  'date': file_lines[2],
                                  'paragraph_list': file_content[3:]}
        template = jinja_environment.get_template('essay-container.html')
        self.response.write(template.render(template_variables))



application = webapp2.WSGIApplication([
                                      ('/', LandingPage),
                                      (r'/essay/(.*)', EssayPage),
                                      ], debug=debug)

