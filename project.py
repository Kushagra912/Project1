from kivy.app import App
from kivy.uix.widget import Widget
class CanteenMain(Widget):
    pass
class CanteenApp(App):
    def build(self):
        return CanteenMain()
    
CanteenApp().run()
