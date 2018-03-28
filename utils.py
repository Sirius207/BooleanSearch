import re
import functools
from operator import (and_, or_, sub)

# non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》％？，、：／,.=!?[\]<>()\s]"
# non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》？，：.[<>()\s]"
non_chinese_term = r"[0-9A-Za-z！「」【】（）〈〉《》？：.\s]"

#
# Index Process
#


def splitByLength(title, split_length):
    words = set()
    title_chi = re.sub(non_chinese_term, "", title)
    for id in range(len(title_chi)):
        words.add(title_chi[id:id+split_length])
    return words


def parseEngTerm(title):
    words = re.findall('[a-zA-Z]+', title)
    return set(words)


def getWords(title):
    words_2gram = splitByLength(title, 2)
    return words_2gram.union(splitByLength(title, 3), parseEngTerm(title))

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

    results = setOperation(set_list, operation)
    return processResults(results)
