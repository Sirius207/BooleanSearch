import re

non_chinese_term = "[0-9A-Za-z！「」【】（）〈〉《》％？：\s]"

def splitByLength(title, split_length):
    words = set()
    title_chi = re.sub(non_chinese_term,"",title)
    string_length=len(title_chi)
    for i in range(string_length):
        for j in range(i, string_length, split_length):
            words.add(title_chi[j:j+split_length])
    return words


def parseEngTerm(title):
    words = re.split(r"[^A-Za-z]", title.strip())
    words = list(filter(None, words))
    return set(words)

def getWords(title):
    words_2gram = splitByLength(title, 2)
    words_3gram = splitByLength(title, 3)
    eng_term = parseEngTerm(title)
    return words_2gram.union(words_3gram, eng_term)


