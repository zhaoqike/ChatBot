
dl_cui = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/4m_evaluate0/unk_replace_evaluate_result_beam_15_result_cuijianwei.txt'
dl_zhao = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/4m_evaluate0/unk_replace_evaluate_result_beam_15_result_zhaoqike.txt'

rt_cui = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/4m_retrieval_evaluate/4m_retrieval_50_evaluate_zhaoqike.txt'
rt_zhao = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/4m_retrieval_evaluate/4m_retrieval_50_evaluate_zhaoqike.txt'


# dl_cui = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/evaluate4/manually_evaluate_result_beam_15_result_cuijianwei.txt'
# dl_zhao = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/evaluate4/manually_evaluate_result_beam_15_result_zhaoqike.txt'
#
# rt_cui = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/retrieval_evaluate/retrieval_60_cuijianwei.txt'
# rt_zhao = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/retrieval_evaluate/retrieval_60_zhaoqike.txt'


dl_zhao_file = open(dl_zhao)
dl_zhao_lines = dl_zhao_file.readlines()

rt_zhao_file = open(rt_zhao)
rt_zhao_lines = rt_zhao_file.readlines()

ori_posts_file = '/home/zhaoqike/Downloads/xiuxi/chatbot/manually_evaluation/weibo_4million/retrieval_evaluate/retrieval_60_with_match_post.txt'


def get_ori_posts(file):
    lines = open(file).readlines()
    posts = map(lambda x: x.split('|')[3], lines)
    return posts

ori_posts = get_ori_posts(ori_posts_file)


def getscore(line):
    parts = line.split('|')
    score = int(parts[0])
    return score

lineidx = range(len(dl_zhao_lines))

dl_scores = map(getscore, dl_zhao_lines)
rt_scores = map(getscore, rt_zhao_lines)

print dl_scores
print rt_scores

dl_idx = [i for i in lineidx if getscore(dl_zhao_lines[i]) > getscore(rt_zhao_lines[i])]
rt_idx = [i for i in lineidx if getscore(dl_zhao_lines[i]) < getscore(rt_zhao_lines[i])]

print dl_idx
print rt_idx

print 'dl result'
for i in dl_idx:
    print dl_zhao_lines[i]
    print rt_zhao_lines[i].strip()+' | '+ori_posts[i]


print 'rt result'
for i in rt_idx:
    print dl_zhao_lines[i]
    print rt_zhao_lines[i].strip()+' | '+ori_posts[i]


# print len(ori_posts)
# for i in range(len(ori_posts)):
#     print ori_posts[i]

print len(dl_idx), len(rt_idx), len(dl_scores)-len(dl_idx)-len(rt_idx)



