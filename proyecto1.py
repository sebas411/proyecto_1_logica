import itertools as it

def bruteForce(clause):
  variables = []

  for item in clause:
    for var in item:
      if var[0] == "!": var = var[1]
      if not var in variables: variables.append(var)
  
  values = [True, False]
  allPosible =  it.product(values, repeat=len(variables))
  allPosible = [{variable:posibility[variables.index(variable)] for variable in variables} for posibility in allPosible]
  
  #ors
  for i in range(len(allPosible)):
    posibility = allPosible[i]
    satisfied = True
    for disjuncion in clause: #ejemplo disj: {"!p", "q"}
      djValue = False
      for variable in disjuncion:
        inversion = True if variable[0] == "!" else False
        if inversion: variable = variable[1]
        value = posibility[variable] ^ inversion
        djValue = djValue or value
      satisfied = satisfied and djValue
    if satisfied:
      return (True, posibility)
  return (False, None)

        

def DPLL(clause, I):
  if len(clause) == 0: return True, I

  for item in clause:
    if len(item) == 0: return False
  




#[{"p"}, {"!p"}]
#[{"q", "p", "!p"}]
#[{"!p", "!r", "!s"}, {"!q", "!p", "!s"}]
#[{"!p", "!q"}, {"q", "!s"}, {"!p", "s"}, {"!q", "s"}]
#[{"!p", "!q", "!r"}, {"q", "!r", "p"}, {"!p", "q", "r"}]
#[{"r"}, {"!q", "!r"}, {"!p", "q", "!r"}, {"q"}]

result, combination = bruteForce([{"r"}, {"!q", "!r"}, {"!p", "q", "!r"}, {"q"}])
if result:
  print("Exito con combinación: ", combination)
else:
  print("No tiene solucion")