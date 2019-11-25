# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:40:57 2019

@author: Kischy
"""

from math import factorial as fac

problem_number = 15


print("Calculation started")

fac_20 = fac(20)


# The number of possible arangments for 40 elements
# divided by the number of possibilities that where counted multiple times
# the miscount stems from the fact that right and right are not distinguishable
the_answer = int(fac(40) / (fac_20*fac_20))





print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)
