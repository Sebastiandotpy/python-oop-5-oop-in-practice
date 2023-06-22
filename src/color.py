from colorama import Fore, Style

class ColorScheme:
    def __init__(self, colors):
        self.colors = colors
        self.num_colors = len(colors)

    def apply_color_scheme(self, text):
        colored_text = ""
        words = text.split()
        for i, word in enumerate(words):
            color_index = i % self.num_colors
            color_code = self.colors[color_index]
            colored_word = f"{getattr(Fore, color_code)}{word}{Style.RESET_ALL}"
            colored_text += colored_word + " "
        return colored_text.rstrip()
