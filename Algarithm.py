from difflib import SequenceMatcher as sim

test1 = ["String", "String", "Strong", "Strang", "String", "Boolty", "bitty", "boolY"]
test2 = ["Str!ng", "St^)ing", "StrOng", "Str0ng", "Str+ng", "Boolty", "bitty", "boolY"]

def similarity(a, b):
    return sim(None, a, b).ratio()

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
                        if similarity(stringl, key) >= 0.75:
                            print(stringl, "similar word found in", dict)
                            dict[stringl] = 1
                            found = True
                            break
                    if found:
                        break
        if not found:
            startDict.append({stringl:1})
            print(stringl, "put in new dict")
    print(startDict)
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
        if total in topWords:
            topWords[total] += " + " + topKey
        else:
            topWords[total] = topKey
    return topWords


def main():
    print(getTopWords(getSimilars(test1)))
    print(getTopWords(getSimilars(test2)))

main()
