"""UNIVERSIDAD DEL VALLE DE GUATEMALA 
 * LOGICA MATEMÁTICA 
 * RESULTADOS: PROYECTO 1 - IMPLEMENTACIÓN DE ALGORTIMO DPLL Y FUERZA BRUTA 
/* File:     proyecto1.py
 * Purpose:  Se implementa para determinar si las cláusulas otorgadas 
 *
 *              cumplen con las determinaciónes del algortimo. 
 *              
 * Run:      py proyecto1.py 
 *          
 *
 * Input:    none            
 * Output:   Resultado de las corridas del algortimo según 
 *           las cláusulas evaluadas en el programa
 *
 * Integrantes:
 *    1. María Mercedes Retolaza 
 *    2. Julio Roberto Herrera 
 *    3. Sebastían Maldonado
 *    4. Martha Gomez 
 *    5. Fátima González 
 */""" 

"""------------------------------------------------------------------------------"""

#Implementación de librerías a utilizar 

import itertools as it
import random
import copy as cp

#Definición de algoritmo: Por fuerza bruta 
#Parámetro de entrada: Una cláusula 

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

#Función de selección de variables 
#Parámetro de entrada: Una cláusula 

def selectVariable(clause):
  variables = []

  for item in clause:
    for var in item:
      if var[0] == "!": var = var[1]
      if not var in variables: variables.append(var)

  return variables[random.randint(0, len(variables)-1)]
  
        
#Implementación de algortimo DPLL 
#Parámetro de entrada: Una cláusula 
def DPLL(clause, I):
  if len(clause) == 0: return True, I

  for item in clause:
    if len(item) == 0: return False, None

  L = selectVariable(clause)
  Lc = "!" + L

  #caso verdadero de la variable
  Bc = cp.deepcopy(clause)

  for item in Bc:
    if L in item:
      Bc.remove(item)
    elif Lc in item:
      item.remove(Lc)
  
  Ic = cp.deepcopy(I)
  isInIc = False
  for item in Ic:
    if L in item:
      isInIc = True
  if not isInIc:
    Ic.append({L:True})

    result, I1 = DPLL(Bc, Ic)
    if result: return True, I1

  #caso falso de la variable
  Bc2 = cp.deepcopy(clause)

  for item in Bc2:
    if Lc in item:
      Bc2.remove(item)
    elif L in item:
      item.remove(L)
  
  Ic2 = cp.deepcopy(I)
  isInIc2 = False
  for item in Ic2:
    if L in item:
      isInIc2 = True
  if not isInIc2:
    Ic2.append({L:False})

    result2, I2 = DPLL(Bc2, Ic2)
    if result2: return True, I2

  return False, None


#Definición de cláusulas a analizar en algortimo 

clauses = [
  [{"p"}, {"!p"}],
  [{"q", "p", "!p"}],
  [{"!p", "!r", "!s"}, {"!q", "!p", "!s"}],
  [{"!p", "!q"}, {"q", "!s"}, {"!p", "s"}, {"!q", "s"}],
  [{"!p", "!q", "!r"}, {"q", "!r", "p"}, {"!p", "q", "r"}],
  [{"r"}, {"!q", "!r"}, {"!p", "q", "!r"}, {"q"}]
]

#Descripción de resultados 

print("RESULTADOS DE SIMULACIÓN E IMPLEMENTACIÓN:")


print("Por fuerza bruta:")
for i in range(len(clauses)):
  item = clauses[i]
  result, combination = bruteForce(item)
  if result:
    print("Clausula %i: Exito con combinación: "%(i+1), combination)
  else:
    print("Clausula %i: Es insatisfacible"%(i+1))

print("\nUtilizando DPLL:")
for i in range(len(clauses)):
  item = clauses[i]
  result, combination = DPLL(item, [])
  if result:
    print("Clausula %i: Exito con combinación: "%(i+1), combination)
  else:
    print("Clausula %i: Es insatisfacible"%(i+1))
