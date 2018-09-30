from difflib import SequenceMatcher as sim
import os

test1 = ["String", "String", "Strong", "Strang", "String", "Boolty", "bitty", "boolY"]
test2 = ["Str!ng", "St^)ing", "StrOng", "Str0ng", "Str+ng", "Boolty", "bitty", "boolY"]
test3 = ["Str!ng", "St^)ing", "StrOng", "Str0ng", "Str+ng", "Boolty", "bitty", "boolY", "String", "String", "Strong", "Strang", "String", "Boolty", "bitty", "boolY"]

def similarity(a, b):
    return sim(None, a, b).ratio()

def getSimilars(list1):
    startDict = []
    # print(startDict)
    for string in list1:
        found = False
        stringl = string.lower()
        stringl = ''.join(i for i in stringl if i.isalnum())
        if len(startDict) == 0:
            startDict.append({stringl:1})
            # print(stringl, "put in new dict", startDict[0])
            found = True
        else:
            for dict in startDict:
                if stringl in dict:
                    # print(stringl, "found in", dict)
                    dict[stringl] += 1
                    found = True
                    break
                else:
                    for key in dict:
                        if similarity(stringl, key) >= 0.75:
                            # print(stringl, "similar word found in", dict)
                            dict[stringl] = 1
                            found = True
                            break
                    if found:
                        break
        if not found:
            startDict.append({stringl:1})
            # print(stringl, "put in new dict")
    # print(startDict)
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
            topWords[total] += "/" + topKey
        else:
            topWords[total] = topKey
    return topWords


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open('{0}/log2.txt'.format(dir_path), 'r') as fin:
        data = fin.read().splitlines(True)
    if len(data) > 300:
        with open('{0}/currentPoll.txt'.format(dir_path), 'w') as fout:
            fout.writelines(data[len(data)-300:])
    with open('{0}/currentPoll.txt'.format(dir_path)) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    f.close()
    print(content)

    top_words = getTopWords(getSimilars(content))

    # print(getTopWords(getSimilars(test1)))
    # print(getTopWords(getSimilars(test2)))
    # print(getTopWords(getSimilars(test3)))

    w = open('{0}/topWords.txt'.format(dir_path), "w")
    w.write("")
    w.close()
    w = open('{0}/topWords.txt'.format(dir_path), "a")
    total = 0
    while (len(top_words) > 0):
        topKey = 0
        for key in top_words:
            total += key
            if key > topKey:
                topKey = key
        perc = (topKey*100) // total
        keyVal = "#"*perc + " {0} {1}\n".format(topKey, top_words[topKey])
        w.write(keyVal)
        del top_words[topKey]
    w.close()

if __name__ == '__main__':
    main()
