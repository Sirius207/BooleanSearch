import csv
from utils import (getWords, search)

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

    # Create Index
    index = dict()
    with open(args.source, 'r') as source:
        source = csv.reader(source, delimiter=',')
        for id, row in enumerate(source):
            words = getWords(row[1])
            for word in words:
                if (word in index):
                    index[word] = index[word] + ',' + str(id+1)
                else:
                    index[word] = str(id+1)

    # Searching & Output
    not_first_line = False
    with open(args.query, 'r') as query_file, open(args.output, 'w') as output:
        for query in query_file:
            query_word = query.split(' ')
            results = search(query_word, index)

            if (not_first_line):
                output.write('\n')
            else:
                not_first_line = True

            output.write(','.join(results))
