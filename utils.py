import re
import functools
from operator import (and_, or_, sub)

non_chinese_term = r"[0-9A-Za-z！「」【】（）〈〉《》％？，、：／,.=!?[\]()…%\"/\-+\s]"
# non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》？，：.[<>()\s]"
# non_chinese_term = r"[0-9A-Za-z！「」【】（）〈〉《》？：.\s]"

#
# Index Process
#


def titleSplit(title):
    words = []
    titleLength = len(title)
    for id in range(titleLength - 2):
        if ' ' not in title[id:id+2]: 
            words.append(title[id:id+2])
            if title[id+2] != ' ': 
                words.append(title[id:id+3])
    # append last 2 gram
    words.append(title[titleLength-2:titleLength])
    return words


def parseEngTerm(title):
    return re.findall('[a-zA-Z]+', title)


def getWords(title):
    words_gram = titleSplit(re.sub(non_chinese_term, " ", title))
    return words_gram + parseEngTerm(title)

#
# Query Process
#

# e.g. '1,3,5,6' => {'1','3','5','6'}
def stringToSet(string):
    list = string.split(',')
    return set(list)


def setOperation(stringList, operation):
    results = set()
    sets = map(stringToSet, stringList)
    if (len(stringList) == 0):
        results.add(0)
    elif (operation == 'and'):
        results = functools.reduce(and_, sets)
    elif (operation == 'or'):
        results = functools.reduce(or_, sets)
    else:
        results = functools.reduce(sub, sets)

    if(len(results) == 0):
        results.add(0)

    return results


def processResults(setResults):
    intlist_results = list(map(int, list(setResults)))
    intlist_results.sort()
    str_results = map(str, intlist_results)
    return str_results


def search(query_word, index):
    operation = query_word[1]
    set_list = []

    for order in range(0, len(query_word), 2):
        key = query_word[order]
        key = re.sub("\n", "", key)
        if key in index:
            set_list.append(index[key])

    if (query_word[0] not in index and query_word[1] != 'or'):
        results = {0}
    else:
        results = setOperation(set_list, operation)
    return processResults(results)