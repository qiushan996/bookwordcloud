

class WordCloudConfig:
    def __init__(self):
        self.font_path = '/System/Library/Fonts/PingFang.ttc'
        self.width = 750
        self.height = 500
        self.background_color =  "lightgray"
        self.max_font_size = 80
        self.min_font_size = 15
        self.colormap = "inferno"
        self.max_words = 200
        self.figsize = (12, 8)
        self.margin = 15                 # 词与词之间的边距
        self.relative_scaling = 0.6      # 词频和字体大小的相关性
        self.interpolation = 'bilinear'  # 添加插值方法配置
        self.outputdir = "./img/"