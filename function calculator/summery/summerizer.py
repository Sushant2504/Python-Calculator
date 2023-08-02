from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import math
import heapq

def summerizer(artext, input):
    para = artext
    reduction = float(input)/100
    stop_words = set(stopwords.words("english"))

    word_repeat = {}
    for w in word_tokenize(para):
        if w not in stop_words:
            if w not in word_repeat.keys():
                word_repeat[w] = 1
            else:
                word_repeat[w] += 1
    # print(word_repeat)
    max_repeat = max(word_repeat.values())

    word_freq = {}

    for w in word_repeat.keys():
        word_freq[w] = (word_repeat[w]/max_repeat)

    # print(word_freq)

    sent_list = sent_tokenize(para)

    sent_weight = {}

    for s in sent_list:
        for w in word_tokenize(s.lower()):
            if w in word_freq.keys():
                if s not in sent_weight.keys():
                    sent_weight[s] = word_freq[w]
                else:
                    sent_weight[s] += word_freq[w]

    # print(sent_weight)

    sent_summ = heapq.nlargest(math.ceil(len(sent_list)*reduction), sent_weight, key=sent_weight.get)
    # print(sent_summ)
    summary = ' '.join(sent_summ)
    return summary 
    # print(summary)
