import numpy as np

query_path = "/home/zhaoqike/Documents/queries.txt"
train_path = "/home/zhaoqike/Documents/100selected.txt"

def get_train_pairs():
    f = open(train_path,"r")
    lines = f.readlines()
    pairs = []
    for line in lines:
        # print line
        # print line
        parts = line.split('|')
        # print parts
        # print len(parts)
        parts = map(str.strip, parts)
        # print len(parts)
        pairs.append(parts)
    return pairs

def get_queries():
    f = open(query_path,"r")
    lines = f.readlines()
    lines = map(str.strip, lines)
    return lines


def sent_to_set(sent):
    return set(sent.split(' '))

def jaccard(p,q):
    interlen = len(list(p & q))
    unionlen = len(list(p | q))
    return float(interlen) / float(unionlen)

# p = ['shirt','shoes','pants','socks', 'socksfff']
# q = ['shirt','shoes','pants', 'socksffffff']
# print jaccard(set(p), set(q))

def find_similar(query, pairs):
    set1 = sent_to_set(query)
    posts = map(lambda x: x[0], pairs)
    sets2 = map(sent_to_set, posts)
    simi = map(lambda x: jaccard(set1, x), sets2)
    # print simi, len(set1), len(posts), len(sets2), len(pairs)
    index = np.argmax(simi)
    # print index, pairs[index][1]
    return pairs[index][1]


if __name__ == "__main__":
    pairs = get_train_pairs()
    queries = get_queries()
    for query in queries:
        response = find_similar(query, pairs)
        print "query", query, "response", response


