from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pre_processing import Textprocessor
from Configure import WordCloudConfig

def generate_wordcloud(words, word_freq, config, imgname): 
  # 创建并生成词云对象
  wordcloud = WordCloud(font_path=config.font_path,  # 请替换为适当的中文字体路径
                        width=config.width, 
                        height=config.height,
                        max_font_size=config.max_font_size,
                        min_font_size=config.min_font_size,
                        colormap=config.colormap,  # 使用viridis配色方案： 'plasma', 'inferno', 'magma'
                        max_words=config.max_words,  # 最多显示200个词
                        margin=config.margin,  # 添加边距参数
                        relative_scaling=config.relative_scaling,  # 添加相对缩放参数
                        random_state=42,
                        background_color=config.background_color).generate_from_frequencies(word_freq)
  
  # 显示词云
  plt.figure(figsize=config.figsize)
  plt.imshow(wordcloud, interpolation=config.interpolation)
  plt.axis('off')
  plt.tight_layout(pad=0)
  #plt.show()
  plt.savefig(config.outputdir + imgname + ".png")


def main(bookpath):
  #Setting for generate wordcloud
  config = WordCloudConfig()
  # Pre processing book text
  bookinfo = Textprocessor(bookpath)
  if bookinfo.supported:
    word, word_freq = bookinfo.get_text()
    if word and word_freq:
      bookname = bookpath.split("/")[-1].split(".")[0]
      generate_wordcloud(word, word_freq, config,bookname)
    else:
      print(f"error to generate word cloud for{bookname}")
  else:
      print("sorry, current file formate isn't supported")



if __name__ == "__main__":
   book_path = './books/基督山伯爵.txt'  # 请替换为你的TXT文件路径
   main(book_path)
   