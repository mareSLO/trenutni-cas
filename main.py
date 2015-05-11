#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime







template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        stevilo = 29
        seznam = ["bla", "ha", "bu"]
        cas = datetime.datetime.now()
        params = {"stevilo": stevilo, "lista": seznam, "cas": cas}
        self.render_template("hello.html", params=params)


class Cas(BaseHandler):
    def get(self):
        cas = datetime.datetime.now()
        params = {"cas": cas}
        self.render_template("cas.html", params=params)







class KrNekiHandler(BaseHandler):
    def get(self):
        self.write("Hello World")



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/ura', Cas),
    webapp2.Route('/hello', KrNekiHandler)
], debug=True)
