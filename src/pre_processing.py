import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

class Textprocessor:
  def __init__(self, filepath):
    self.supported = False  
    # get filepath suffix
    filetype = filepath.split(".")[-1]
    if filetype == "txt":
      with open(filepath, 'r', encoding='utf-8') as file:
        self.booktext = file.read()
      self.supported = True

  # get stop word
  @staticmethod
  def get_stopword(lang="cn"):
      with open("stopword_cn.txt",  "r", encoding="utf-8")as f :
        allwords = f.read().split()
        print(f"loaded {len(allwords)} stop word")
        return  set(allwords)
      
  def get_text(self):
    try:
      if self.supported:
        # 使用jieba进行中文分词
        words = jieba.cut(self.booktext)
        # 过滤停用词
        stopwords = self.get_stopword();
        if stopwords:
            words = [word for word in words if word not in stopwords and len(word) > 1]     
        word_freq = Counter(words)
        return (words, word_freq)
    except Exception as e:
        print(f"An error occurred during parsing ")


