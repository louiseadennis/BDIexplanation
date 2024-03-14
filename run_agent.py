from parser import parse_string,parse_file
from simpleBDI import *
from rule import Rule
import sys

ruleset="""
  hungry,no_food,at_home-(1)-> +go_to_shops
  at_home,go_to_shops -(2)-> .drive,-at_home,+at_shops,-go_to_shops
  no_food,at_shops -(1)-> .buy_food,+go_home,+have_food,-no_food
  go_home -(1)-> .drive,-at_shops,+at_home,-go_home
  hungry,have_food,at_home -(1)-> .eat,-hungry,-have_food,+no_food

  at_shops,need_clothing-(2)->.buy_clothes,-need_clothing

  0:+hungry,+no_food,+at_home,+need_clothing
 24:+hungry
"""
p=parse_string(ruleset,timesteps=31)
# p=parse_file(sys.argv[1])

trace=create_trace(TraceElement(set(),p[0],None,p[1],None,"p"))

i=0
print("TRACE BASED ON EXTERNAL OBSERVATIONS")
for t in trace:
  #print(i,t.state,t.beliefs)
  if t.action!=None:
    print(i,t.action)
  i+=1

