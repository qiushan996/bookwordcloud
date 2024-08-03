

class WordCloudConfig:
    def __init__(self):
        self.font_path = '/System/Library/Fonts/PingFang.ttc'
        self.width = 1000
        self.height = 800
        self.background_color = 'white'
        self.max_font_size = 140
        self.min_font_size = 30
        self.colormap = "inferno"
        self.max_words = 150
        self.figsize = (14, 10)
        self.margin = 10                 # 词与词之间的边距
        self.relative_scaling = 0.5      # 词频和字体大小的相关性
        self.interpolation = 'bilinear'  # 添加插值方法配置
        self.outputdir = "./img/"