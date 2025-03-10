# асоціація один до багатьох
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
        self._programs = []

    @property
    def program(self):
        return self._programs

    @program.setter
    def program(self, prog):
        self._programs.append(prog)

    def run_programs(self):
        print(f"Компʼютер {self._computer_name} запускає програму...")
        for prog in self._programs:
            prog.run()

if __name__ == '__main__':
    p = Program("Zoom")
    p1 = Program("PyCharm")
    c = Computer("AK01")
    c.program = p  # be careful with such approach of adding
    c.program = p1
    p.computer = c
    c.run_programs()














