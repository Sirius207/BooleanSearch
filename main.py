import pandas as pd
from utils import (getWords, search)

import time

start = time.time()

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                        default='source.csv',
                        help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()

    # Import Data
    Source = pd.read_csv(args.source, names=["ID", "Title"])

    # Create Index
    index = dict()
    for id, title in enumerate(Source['Title']):
        words = getWords(title)
        for word in words:
            if (word in index):
                index[word].add(id+1)
            else:
                index[word] = set()
                index[word].add(id+1)

    # Searching & Output
    with open(args.query, 'r') as query_file, open(args.output, 'w') as output:
        for no, query in enumerate(query_file, 1):
            query_word = query.split(' ')
            results = search(query_word, index)

            if no != 1:
                output.write('\n')
            
            output.write(','.join(results))

    end = time.time()
    duration = end - start
    print(duration)
