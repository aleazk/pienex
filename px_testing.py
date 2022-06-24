import pienex as px

r = px.reasoning(((1, 1, 2), 3, -3))

#r.programme()

print (r.ndpredict("ND")[70:80])

import numpy as np

ND_distance = np.loadtxt("ND_distance.csv", delimiter=",")

print (ND_distance[70:80])