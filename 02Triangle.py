# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:34:10 2019

@author: Margot
"""

from pyDatalog import pyDatalog
pyDatalog.clear()
pyDatalog.create_terms('X, P, rectangle,  angleDroit, quelconque,  equilateral, deuxcote, troiscote, isocele, rectangleIsocele, triangle')


pyDatalog.load("""
""")


rectangle(X) <= angleDroit(X) 
isocele(X) <= deuxcote(X)
rectangleIsocele(X) <= angleDroit(X) & deuxcote(X)
equilateral(X) <= troiscote(X)


pyDatalog.assert_fact('deuxcote', 'triangle')
pyDatalog.assert_fact('angleDroit', 'triangle')


query = 'isocele(X)'
answers = pyDatalog.ask(query).answers 
print(answers)