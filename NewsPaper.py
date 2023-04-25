class Paper():
    def __init__(self, name):
        self.__name = name
        self.pages = None
        self.type = None
    
    #Setter methods
    def set_name(self, name):
        self.__name = name
    def set_pages(self, pages):
        self.pages = pages
    def set_type(self, type):
        self.type = type
    #Getter Methods
    def get_pages(self):
        return self.pages
    def get_name(self):
        return self.__name
    def get_type(self):
        return self.type

news = Paper('Bombay Times')
print(news.get_name())
news.set_pages(10)
print(news.get_pages())