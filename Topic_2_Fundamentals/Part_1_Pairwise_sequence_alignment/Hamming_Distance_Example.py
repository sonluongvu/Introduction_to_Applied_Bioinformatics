from __future__ import division, print_function

import numpy as np 
from IPython.core.display import HTML 
from IPython.core import page
page.page = print 

from scipy.spatial.distance import hamming

r1 = DNA("ACCCAGGTTAACGGTGACCAGGTACCAGAAGGGTACCAGGTAGGACACACGGGGATTAA")
r2 = DNA("ACCGAGGTTAACGGTGACCAGGTACCAGAAGGGTACCAGGTAGGAGACACGGCGATTAA")
q1 = DNA("TTCCAGGTAAACGGTGACCAGGTACCAGTTGCGTTTGTTGTAGGAGACACGGGGACCCA")
print(r1)
print(r2)
print(q1)   