from abc import ABC, abstractmethod
from color import ColorScheme


color_scheme = ColorScheme(colors=["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"])


class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def take_break(self, minutes):
        pass

    def apply_color_scheme(self, text):
        colored_text = ""
        lines = text.split("\n")
        for line in lines:
            if line.strip() != "":
                colored_line = color_scheme.apply_color_scheme(line)
                colored_text += colored_line + "\n"
            else:
                colored_text += line + "\n"
        return colored_text

    def print_colored_output(self, text):
        colored_output = self.apply_color_scheme(text)
        print(colored_output, end="")


class Programmer(Worker):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"{self.name} codes with {self.language}"

    def work(self):
        self.print_colored_output(f"The programmer is coding")

    def take_break(self, minutes):
        self.print_colored_output(f"The programmer takes a {minutes}-minute break")


class Janitor(Worker):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def __str__(self):
        return f"{self.name} uses {self.tool}"

    def work(self):
        self.print_colored_output(f"Janitor is working with {self.tool}")

    def take_break(self, minutes):
        self.print_colored_output(f"Janitor is listening to music for {minutes} minutes")
