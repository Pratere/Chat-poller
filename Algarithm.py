from difflib import SequenceMatcher
test1 = ["String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "String", "String", "Strong", "Strang", "String", "Wrong", "Wrang", "Wong", "Dong", "Clong"]
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getSimilars(list1):
    startDict = []
    for string in list1:
        found = False
        print(string)
        stringl = string.lower()
        req = len(string) - (len(string)//5)
        if len(startDict) == 0:
            startDict.append({stringl:1})
            print(stringl, "Added to new Dict")
            found = True
        else:
            for dict in startDict:
                if stringl in dict:
                    dict[stringl] += 1
                    print(stringl, "Found in Dict:", dict)
                    found = True
                    break
                else:
                    for key in dict:
                        # count = 0
                        # if len(stringl) <= len(key):
                        #     length = len(stringl)
                        # else:
                        #     length = len(key)
                        # for i in range(length):
                        #     if stringl[i] == key[i]:
                        #         count+=1
                        # if count >= req:
                        if similar(stringl, key) >= 0.75:
                            dict[stringl] = 1
                            found = True
                            print(stringl, "Found to be similar in Dict")
                            break
            if not found:
                startDict.append({stringl:1})
                print(stringl, "Added to new Dict")


    print(startDict)

def main():
    getSimilars(test1)
    print(similar("wong", "dong"))

main()
