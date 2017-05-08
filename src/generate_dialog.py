import seq2seq
import collections



# To create your own data, we recommend taking a look at the data generation scripts above. A typical data preprocessing pipeline looks as follows:
#
# Generate data in parallel text format
# Tokenize your data
# Create fixed vocabularies for your source and target data
# Learn and apply subword units to handle rare and unknown words

def generate_vocab(inpath, min_frequency, max_vocab_size, outfile):
    cnt = collections.Counter()
    infile = open(inpath)
    count = 0
    for line in infile:
        tokens = line.strip().split(' ')
        tokens = [_ for _ in tokens if len(_) > 0]
        cnt.update(tokens)
        count += 1
        if count % 1000 == 0:
            print 'done with ', count, 'lines'
    infile.close()

    # Filter tokens below the frequency threshold
    if min_frequency > 0:
        filtered_tokens = [(w, c) for w, c in cnt.most_common()
                           if c > min_frequency]
        cnt = collections.Counter(dict(filtered_tokens))

    # Sort tokens by 1. frequency 2. lexically to break ties
    word_with_counts = cnt.most_common()
    word_with_counts = sorted(
        word_with_counts, key=lambda x: (x[1], x[0]), reverse=True)

    # Take only max-vocab
    if max_vocab_size is not None:
        word_with_counts = word_with_counts[:max_vocab_size]

    out = open(outfile, 'w')
    for word, count in word_with_counts:
        print >> out, ("{}\t{}".format(word, count))
    out.close()



if __name__ == "__main__":
    generate_vocab('/home/zhaoqike/weibo_data/stc_weibo_train_post', -1, 30000, '/home/zhaoqike/Documents/post_vocab.txt')
    generate_vocab('/home/zhaoqike/weibo_data/stc_weibo_train_response', -1, 30000, '/home/zhaoqike/Documents/response_vocab.txt')