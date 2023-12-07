puzzle = """Time:        40     82     91     66
Distance:   277   1338   1349   1063"""

#t = puzzle.split("\n")[0].split(":")[1].split()
#d = puzzle.split("\n")[1].split(":")[1].split()
#t = list(map(int, filter(lambda x: x != "", t)))
#d = list(map(int, filter(lambda x: x != "", d)))
race_time = int(puzzle.split("\n")[0].replace(" ", "").split(":")[1])
record_dist = int(puzzle.split("\n")[1].replace(" ", "").split(":")[1])


def button_down_wins(button_down_time):
  return ((race_time - button_down_time) * button_down_time) - record_dist > 0



def solve( b):
  t = race_time
  d = record_dist
  # −b**2 +tb −d=0

  z = - (b**2) + (t*b) - d
  
  print(f"z = {z}")

print(len(range(8598434 , 32230732 +1)))
