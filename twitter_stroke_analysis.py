from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import collections


t = Tokenizer("/ユーザー辞書の場所/user_dict.csv", udic_type="simpledic", udic_enc="utf8")

f = open('/解析するテキストの場所/twitter_analysis_alltext.txt', 'r')
data = f.read()
f.close()

words_list = ''
unique_words = []
token_filters = [CompoundNounFilter(), POSKeepFilter(['名詞']), TokenCountFilter(sorted=True)]
a = Analyzer(tokenizer=t, token_filters=token_filters)
  #tokens = t.tokenize(i, wakati=True) #フィルターなし
tokens = a.analyze(data)  #アナライズフィルターあり

for k, v in a.analyze(data):
  print('%s: %d' % (k, v))
