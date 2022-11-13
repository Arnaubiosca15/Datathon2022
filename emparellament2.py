import json
import pandas 

def edat(n:int, m:int)->int:
    return abs(n-m)
def hobbies(x: list[str], y: list[str])->int:
    proximitat = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if y[j] == x[i]:
                proximitat -=1
    return proximitat
def emparellament(n:int)->bool:
    if n<=15:
        return True
    else: 
        return False
def main()->None:

    #with open('C:/Users/arnau/OneDrive/Documents/AP1/datathon/perfils.json') as file:
    dictperfils = pandas.read_json("perfils.json")
    for row1 in dictperfils.iterrows():
        for row2 in dictperfils.iterrows():
            mitjana = edat(row1['age'],row2['age'])+ hobbies(row1['hobbies'], row2['hobbies'])
    print(emparellament(mitjana))
        

if __name__ == "__main__":
    main()
