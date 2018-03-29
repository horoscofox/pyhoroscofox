class Response():

    text = ''
    date_start = None
    date_end = None

    def __init__(self, text, date_start, date_end=None):
        self.text = text
        self.date_start = date_start
        self.date_end = date_end

    def json(self):
        return self.__dict__