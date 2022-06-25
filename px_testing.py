#Example on how to use it

import pienex as px

r = px.reasoning(((1, 1, 2), 3, -3))

r.programme()

ndpredictions = r.ndpredict("ND")

print (ndpredictions)
