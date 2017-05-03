import numpy as np

query_path = "/home/zhaoqike/Documents/60_selected.txt"
train_path = "/home/zhaoqike/Documents/t_given_s_train_words.txt"


def get_train_pairs():
    f = open(train_path,"r")
    lines = f.readlines()
    pairs = []
    for line in lines:
        parts = line.split('|')
        parts = map(str.strip, parts)
        pairs.append(parts)
    return pairs


def get_queries():
    f = open(query_path,"r")
    lines = f.readlines()
    queries = map(lambda x: x.split('|')[0].strip(), lines)
    realresp = map(lambda x: x.split('|')[1].strip(), lines)
    return queries, realresp


def sent_to_set(sent):
    return set(sent.split(' '))


def jaccard(p,q):
    interlen = len(list(p & q))
    unionlen = len(list(p | q))
    return float(interlen) / float(unionlen)


def find_similar(query, pairs):
    set1 = sent_to_set(query)
    posts = map(lambda x: x[0], pairs)
    sets2 = map(sent_to_set, posts)
    simi = map(lambda x: jaccard(set1, x), sets2)
    index = np.argmax(simi)
    return pairs[index]


def create_whole_pair_file():
    post_file = open('/home/zhaoqike/Downloads/stc_weibo_train_post')
    response_file = open('/home/zhaoqike/Downloads/stc_weibo_train_response')
    conv_file = open('/home/zhaoqike/Downloads/conv.txt', 'w')
    count = 0
    while True:
        post = post_file.readline().strip()
        if not post:
            break
        response = response_file.readline().strip()
        if post.find('|') != -1 or response.find('|') != -1:
            continue
        conv_file.write(post + " | " + response + "\n")
        count = count + 1
        if count % 10000 == 0:
            print("processed %d lines" % count)

    conv_file.close()
    response_file.close()
    post_file.close()


def delete_queries(queries, pairs):
    queries_strip = map(str.strip, queries)
    deleted_pairs = [p for p in pairs if p[0].strip() not in queries_strip]
    return deleted_pairs


if __name__ == "__main__":
    # create_whole_pair_file()

    pairs = get_train_pairs()
    queries, realresp = get_queries()
    pairs = delete_queries(queries, pairs)
    result_file = open('/home/zhaoqike/Documents/retrieval_60.txt', 'w')
    for qi in range(len(queries)):
        query = queries[qi]
        similar_pair = find_similar(query, pairs)
        result = queries[qi] + " | " + similar_pair[1] + " | " + realresp[qi] + " | from post: " + similar_pair[0] + "\n"
        print result
        result_file.write(result)
        result_file.flush()

    result_file.close()


