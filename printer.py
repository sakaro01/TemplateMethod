from abc import ABCMeta, abstractmethod

class AbstractPrinter(metaclass=ABCMeta):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def is_color(self):
        pass

    @abstractmethod
    def get_text(self):
        pass

    def print(self):
        print('size：', self.get_size())
        if self.is_color():
            print('色：カラフル')
        else:
            print('色：白黒')
        print('文章：')
        print(self.get_text())

class NewPrinter(AbstractPrinter):
    def __init__(self, text):
        self._text = text

    def get_size(self):
        return 'A4'

    def is_color(self):
        return True

    def get_text(self):
        return self._text

class OldPrinter(AbstractPrinter):
    def __init__(self, text):
        self._text = text

    def get_size(self):
        return 'B4'

    def is_color(self):
        return False

    def get_text(self):
        return '\n'.join(list(self._text))

