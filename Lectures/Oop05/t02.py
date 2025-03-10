# асоціація
class Program:
    def __init__(self, name):
        self._name = name
        self._computer = None

    @property
    def computer(self):
        return self._computer

    @computer.setter
    def computer(self, comp):
        self._computer = comp

    def run(self):
        print(f"Програма {self._name} працює...")


class Computer:
    def __init__(self, com_name):
        self._computer_name = com_name
        self._program = None

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, prog):
        self._program = prog

    def run_program(self):
        if self._program is None:
            return

        print(f"Компʼютер {self._computer_name} запускає програму...")
        self._program.run()

if __name__ == '__main__':
    p = Program("Zoom")
    c = Computer("AK01")
    c.program = p
    p.computer = c
    c.run_program()














