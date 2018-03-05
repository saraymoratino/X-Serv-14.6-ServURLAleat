#!/usr/bin/python3

import random
import webapp

class Urls(webapp.webApp):
	def parse(self, request):
		return random.randint(1,10000)
	def process(self, parsedRequest):	
		num_random = parsedRequest
		html_answer = '<html><body>'
		html_answer += '<h1><a href = ' + str(num_random) + '>Dame otra</a></h1>' 
		html_answer += '</html></body>'
		
		return ("200 OK", html_answer)
		
if __name__ == "__main__":
	testWebApp = Urls("localhost", 4567)

