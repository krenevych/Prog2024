from abc import ABCMeta, abstractmethod


class FileReaderObserver(metaclass=ABCMeta):
    @abstractmethod
    def onReceive(self, line):
        pass

class FileReader:

    def __init__(self, filename):
        self.filename = filename
        self.observers : list[FileReaderObserver]= []

    def subscribe(self, observer: FileReaderObserver):
        self.observers.append(observer)

    def notify(self, line):
        for observer in self.observers:
            observer.onReceive(line)

    def read(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            for line in f:
                self.notify(line)
                # line = line.rstrip()
                # print(line)


if __name__ == '__main__':
    filereader = FileReader('input01.txt')
    filereader.read()

