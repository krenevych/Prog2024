from Labs.CompMat_1.oop13.FileReader import FileReaderObserver, FileReader


class ShowLiner(FileReaderObserver):

    def onReceive(self, line):
        line = line.rstrip()
        print(line)

class WordsCounter(FileReaderObserver):

    def __init__(self):
        self.word_counter = 0

    def onReceive(self, line):
        words = line.split()
        self.word_counter += len(words)

if __name__ == '__main__':
    filereader = FileReader('input01.txt')

    # showliner = ShowLiner()
    # filereader.subscribe(showliner)

    wordcounter = WordsCounter()
    filereader.subscribe(wordcounter)

    filereader.read()

    print(wordcounter.word_counter)