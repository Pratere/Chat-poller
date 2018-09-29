from difflib import SequenceMatcher

test1 = ["String", "String", "Strong", "Strang", "String", "Booty"]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getSimilars(list1):
    startDict = []
    print(startDict)
    for string in list1:
        found = False
        stringl = string.lower()
        stringl = ''.join(i for i in stringl if i.isalnum())
        if len(startDict) == 0:
            startDict.append({stringl:1})
            print(stringl, "put in new dict", startDict[0])
            found = True
        else:
            for dict in startDict:
                if stringl in dict:
                    print(stringl, "found in", dict)
                    dict[stringl] += 1
                    found = True
                    break
                else:
                    for key in dict:
                        if similar(stringl, key) >= 0.75:
                            print(stringl, "similar word found in", dict)
                            dict[stringl] = 1
                            found = True
                            break
                    if found:
                        break
        if not found:
            startDict.append({stringl:1})
            print(stringl, "put in new dict")
    return startDict

def getTopWords(list):
    topWords = {}
    for dict in list:
        top = 0
        total = 0
        for key in dict:
            if dict[key] > top:
                top = dict[key]
                topKey = key
            total += dict[key]


def main():
    getSimilars(test1)

main()
