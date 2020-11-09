from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget


class correct_ans_layout(FloatLayout):
    pass

class correct_ans2_layout(FloatLayout):
    pass

class end_game_layout(FloatLayout):
    pass

class wrong_ans_layout(FloatLayout):
    pass

class WindowManager(ScreenManager):
    pass

class EndScreen(Screen):
    pass


class QuestionOne(Screen, Widget):

    def correct_btn(self):
        correct_ans()

    def wrong_btn(self):
        wrong_ans()


class QuestionTwo(Screen):

    def correct_btn(self):
        correct_ans_2()

    def wrong_btn(self):
        wrong_ans()


class QuestionThree(Screen):

    def correct_btn(self):
        end_game()

    def wrong_btn(self):
        wrong_ans()


def correct_ans():
    ca_layout = correct_ans_layout()
    correct = Popup(title = 'Correct', content = ca_layout, size_hint = (0.75,0.4))
    correct.open()


def correct_ans_2():
    ca2_layout = correct_ans2_layout()
    correct2 = Popup(title = 'Correct', content = ca2_layout, size_hint = (0.75,0.4))
    correct2.open()


def end_game():
    eg_layout = end_game_layout()
    end = Popup(title = 'Correct', content = eg_layout, size_hint = (0.75,0.4))
    end.open()


def wrong_ans():
    wa_layout = wrong_ans_layout()
    wrong = Popup(title = 'Incorrect', content = wa_layout, size_hint = (0.75,0.4))
    wrong.open()


kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()