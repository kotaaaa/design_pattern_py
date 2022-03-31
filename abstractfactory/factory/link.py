from abc import ABCMeta, abstractmethod
from factory.item import Item


class Link(Item):
    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url

    @abstractmethod
    def make_html(self):
        pass
