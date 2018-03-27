import re
import functools
from operator import (and_, or_, sub)

# non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》％？，、：／,.=!?[\]<>()\s]"
# non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》％？，、：[<>()\s]"
non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》％？：.\s]"

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

def setOperation(sets, operation):
    results = set()
    if (len(sets) == 0):
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

def processResults(results):
    list_results = list(results)  
    list_results.sort()
    str_results = map(str, list_results)
    return str_results

def search(query_word, index):
    operation = query_word[1]
    set_list = []

    for order in range(0, len(query_word), 2):
        key = query_word[order]
        key = re.sub("\n","", key)
        if key in index:
            set_list.append(index[key])
    
    results = setOperation(set_list, operation)
    return processResults(results)
