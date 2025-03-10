# залежність


class Program:
    def __init__(self, name):
        self._name = name

    def run_program(self):
        print(f"Програма {self._name} працює...")


class Computer:
    def __init__(self, com_name):
        self._computer_name = com_name

    def run_program(self, program: Program):
        print(f"Компʼютер {self._computer_name} запускає програму...")
        program.run_program()

if __name__ == '__main__':
    p = Program("Zoom")
    c = Computer("AK01")
    c.run_program(p)












