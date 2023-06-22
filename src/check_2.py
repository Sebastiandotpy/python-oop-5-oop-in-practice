import unittest
from abc import ABC, abstractmethod
from worker import Worker, Programmer, Janitor
from color import ColorScheme
from colorama import init

# Initialize colorama
init()

# Define the color scheme with transitioning colors
color_scheme = ColorScheme(colors=["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN"])

class TestWorker(unittest.TestCase):
    def setUp(self):
        self.color_scheme = color_scheme

    def test_0_worker_abstract_class(self):
        self.assertTrue(issubclass(Worker, ABC))

    def test_1_abstract_method_work(self):
        self.assertTrue(getattr(Worker.work, '__isabstractmethod__', False), "The method work in the class Worker is not an abstract method")

    def test_2_abstract_method_take_break(self):
        self.assertTrue(getattr(Worker.take_break, '__isabstractmethod__', False), "The method take_break in the class Worker is not an abstract method")

    def test_3_abstract_methods_implemented_Programmer(self):
        try:
            p1 = Programmer("Hamid", "C++")
            p1.work()
            p1.take_break(10)
            result = True, "All OK"
        except Exception as e:
            result = False, str(e)
        self.assertTrue(result[0], result[1])

    def test_4_janitor_inheritance(self):
        try:
            j1 = Janitor("Andrei", "Wrench")
        except Exception as e:
            j1 = None
        self.assertIsInstance(j1, Worker, "The class Janitor doesn't inherit from the class Worker")

    def test_5_abstract_methods_implemented_Janitor(self):
        try:
            j2 = Janitor("Paula", "Glue")
            j2.work()
            j2.take_break(20)
            result = True, "All OK"
        except Exception as e:
            result = False, str(e)
        self.assertTrue(result[0], result[1])

    def apply_color_scheme(self, text):
        colored_text = ""
        for line in text.split("\n"):
            colored_line = self.color_scheme.apply_color_scheme(line)
            colored_text += colored_line + "\n"
        return colored_text

    def print_colored_output(self, text):
        colored_output = self.apply_color_scheme(text)
        print(colored_output)


        

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

