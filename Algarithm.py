from difflib import SequenceMatcher
test1 = ["String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "Clong"]
test2 = [" String", "string", "Strwing", "Strong ", "Sta ir", "Stare", "s Tor"]
test3 = ["String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "Clong", " String", "string", "Strwing", "Strong ", "Sta ir", "Stare", "s Tor"]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getSimilars(list1):
    startDict = []
    for string in list1:
        found = False
        # print(string)
        stringl = string.lower().replace(" ", "")
        req = len(string) - (len(string)//5)
        if len(startDict) == 0:
            startDict.append({stringl:1})
            # print(stringl, "Added to new Dict")
            found = True
        else:
            for dict in startDict:
                if stringl in dict:
                    dict[stringl] += 1
                    # print(stringl, "Found in Dict:", dict)
                    found = True
                    break
                else:
                    for key in dict:
                        if similar(stringl, key) >= 0.75:
                            dict[stringl] = 1
                            found = True
                            # print(stringl, "Found to be similar in Dict")
                            break
            if not found:
                startDict.append({stringl:1})
                # print(stringl, "Added to new Dict")


    return startDict

def getTopWords(listOfDicts):
    topWords = {}
    for dict in listOfDicts:
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
    print(getTopWords(getSimilars(test3)))

if __name__ == '__main__':
    main()
