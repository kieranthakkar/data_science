def arithmetic_arranger(problems,reveal=False):
  topList, bottomList, ans, decorList = [],[],[],[]     # Initialise w/ empty lists
  operatorList =[]

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for i in problems:
    for j in i:
      if j not in "0987654321+- ":
        return "Error: Numbers must only contain digits."

  for i in problems:                                          # Check for +/- and form topList, bottomList and answer lists
    ans.append(eval(i))
    
    if "+" in i:                                             # Creating the operator list, looking for + or -
      individual = i.split("+")
      operatorList.append("+")
    elif "-" in i:
      individual = i.split("-")
      operatorList.append("-")
    else:
      return "Error: Operator must be '+' or '-'."
    
    if (abs(int(individual[0].strip())) or abs(int(individual[1].strip()))) > 9999:
      return "Error: Numbers cannot be more than four digits."

    topList.append(individual[0].strip())
    bottomList.append(individual[-1].strip())
  
  if abs(int(max(topList))) > 9999:
    return "Error: Numbers cannot be more than four digits."
  
  if abs(int(max(bottomList))) > 9999:
    return "Error: Numbers cannot be more than four digits."



  topString=bottomString=decorString=stringAns = ""

  for i in range(len(problems)):
    ans[i] = str(ans[i])                                      # Convert answers to string
    if int(topList[i])>int(bottomList[i]):
      longest = len(topList[i])                           # Setting the length of dashed lines (---) 
    else:
      longest = len(bottomList[i])
    decorLength = longest+2
    decorList.append("-"*(decorLength))                   # Final length is determined by the inputs not answers

    while len(topList[i]) < decorLength:
      topList[i] = " " + topList[i]
    while len(bottomList[i]) < decorLength-1:
      bottomList[i] = " " + bottomList[i]
    while len(ans[i]) < (longest+2):
      ans[i] = " " + ans[i]

    spacer = " "*4
    topString += topList[i] + spacer
    bottomString += operatorList[i] + bottomList[i] + spacer
    decorString += decorList[i] + spacer
    stringAns += ans[i] + spacer

  noAnsFinal = f"{topString}\n{bottomString}\n{decorString}"
  stringAnsFinal = stringAns
  if reveal == True:
    arranged_problems = noAnsFinal +"\n"+stringAnsFinal
  else:
    arranged_problems = noAnsFinal  
  return arranged_problems
