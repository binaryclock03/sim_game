import json
from sim.industry.good import GoodTemplate as GT

dict = [GT("grain", "Grain", 0.1, 1, 0).to_dict(), GT("flour", "Flour", 0.1, 1, 0).to_dict()]
out = json.dumps(dict)
print(out)

from sim.industry.recipe import Recipe as RE
dict = [RE("millGrain", "Mill Grain", {"grain":5}, {"flour":4}, 10).to_dict()]
out = json.dumps(dict)
print(out)