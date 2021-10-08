import random

order = {}

def player(prev_play, opponent_history=[]):
  global order

  n = 3

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R"

  if len(opponent_history) >= n:
    input = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in order.keys():
      order["".join(opponent_history[-(n+1):])]+=1
    else:
      order["".join(opponent_history[-(n+1):])]=1

    possible =[input + "R", input + "P", input + "S"]

    for i in possible:
      if not i in order.keys():
        order[i] = 0

    predict = max(possible, key=lambda key: order[key])

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"


  return guess
