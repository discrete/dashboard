#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello, World!!')

def main():
    app = webapp.WSGIApplication([
            (r'.*', MainHandler)
            ], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()