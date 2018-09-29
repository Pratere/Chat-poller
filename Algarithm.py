test1 = ["String", "String", "Strong", "Strang", "String"]

def getSimilars(list1):
    startDict = {}
    print(startDict)
    for string in list1:
        stringl = string.lower()
        req = len(string) - (len(string)//5)
        if len(startDict) == 0:
            stringlDict = stringl + "Dict"
            startDict[stringlDict] = {stringl:1}
        for dict in startDict:
            print(dict)
            if stringl in dict:
                dict[stringl] += 1
            else:
                found = False
                for key in dict:
                    count = 0
                    if len(stringl) <= key:
                        length = len(stringl)
                        found = True
                    else:
                        length = len(key)
                    for i in range(length):
                        if stringl[i] == key[i]:
                            count+=1
                    if count >= req:
                        dict[stringl] = 1
                        found = True
                if not found:
                    stringlDict = stringl + "Dict"
                    startDict[stringlDict] = {}

def main():
    getSimilars(test1)
    # dict = {"Hello": 1}
    # dict["Hello"] += 1
    # print(dict)

main()

!chatr 
