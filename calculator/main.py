from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import re

class CalcApp(App):
    # Initializes the app, it will be called once
    def build(self):
        body_layout = BoxLayout()
        body_layout.orientation = "vertical"

        self.calc_screen = TextInput()
        self.calc_screen.background_color = "black"
        self.calc_screen.foreground_color = "white"
        self.calc_screen.multiline = False
        self.calc_screen.readonly = True
        self.calc_screen.halign = "right"
        self.calc_screen.font_size = 55
        body_layout.add_widget(self.calc_screen)

        self.operators = ["+", "-", "*", "/", "(", ")", "%", "^"]
        self.last_input = ""
        calc_buttons = [
            ["(", ")", "^", "%"],
            ["√"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            ["←", "="]
        ]

        for row in calc_buttons:
            row_layout = BoxLayout()
            for column in row:
                new_button = Button()
                new_button.text = column
                new_button.font_size = 35
                new_button.bold = 20
                new_button.background_color = "yellow"
                new_button.pos_hint = {"center_x": 0.5, "center_y": 0.5}
                row_layout.add_widget(new_button)

                if new_button.text in self.operators or new_button.text == "√":
                    new_button.background_color = "cyan"
                elif new_button.text == "C":
                    new_button.background_color = "red"
                elif new_button.text == "←":
                    new_button.background_color = "orange"

                if new_button.text == "=":
                    new_button.bind(on_press=self.handle_equal_pressed)
                    new_button.background_color = "cyan"
                    new_button.font_size = 30
                elif new_button.text == "←":
                    new_button.bind(on_press=self.handle_backspace_pressed)
                else:
                    new_button.bind(on_press=self.handle_button_pressed)

            body_layout.add_widget(row_layout)
        return body_layout

    # Handle events functions
    def handle_button_pressed(self, button_pressed):
        if button_pressed.text == "C":
            self.calc_screen.text = ""
        elif (self.calc_screen.text == "") and (button_pressed.text in self.operators) and (button_pressed.text not in ["(", "√"]):
            return
        elif (button_pressed.text in self.operators) and (self.last_input in self.operators) and (self.last_input not in ["(", ")", "√"]):
            return
        else:
            self.calc_screen.text = self.calc_screen.text + button_pressed.text

        self.last_input = button_pressed.text

    def handle_equal_pressed(self, button_pressed):
        if (self.calc_screen.text != "") and (self.last_input not in self.operators):
            try:
                # Replace "^" with "**" for exponentiation and "√" with "math.sqrt"
                expression = self.calc_screen.text.replace("^", "**")
                expression = re.sub(r'√(\d+)', r'(\1**0.5)', expression)
                # Preprocess the expression to handle leading zeros
                expression = re.sub(r'\b0+(\d)', r'\1', expression)
                self.calc_screen.text = str(eval(expression))
            except Exception as e:
                self.calc_screen.text = "Error"

    def handle_backspace_pressed(self, button_pressed):
        self.calc_screen.text = self.calc_screen.text[:-1]

if __name__ == "__main__":
    calc_app = CalcApp()  # <- Object to be run
    calc_app.run()