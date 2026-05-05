    from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class AIApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Phap Su AI Offline")
        btn = Button(text="Hoi AI (Vit ga!)")
        btn.bind(on_press=self.on_click)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.label.text = "Dang nan chu..."
        