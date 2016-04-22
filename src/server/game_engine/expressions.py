#
#  Expression game
#

import json, random

with open('JSON/expressions.json') as data_file:
        JSONexp = json.load(data_file)['expressions']

class JSONHandler:
    def ranexp(self):
        return (random.choice(JSONexp))   

class expressionGame:

    def __init__(self):
        self.currentExp = None

    def newExpression(self):
        self.currentExp = JSONHandler.ranexp(self)
        self.request.send(str(self.currentExp).encode('utf-8'))
        
    def inputCheck(self, text, force):
        if ('aze' in text):
    self.newExpression()
                
    def responseCheck(self, response):
        print(self.currentExp['answer'])
        if (response is self.currentExp['answer']):
            return True
        return False
            
