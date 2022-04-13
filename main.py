from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
import requests

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'M2SI Translator'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical",]]
            elevation:5
        MDLabel:
            halign: 'center'
            
        
"""

url = "https://dlv3sgr3m5.execute-api.us-east-1.amazonaws.com/dev/res1"
headers = {
  'Content-Type': 'text/plain'
}

username_input = """
MDTextField:
    hint_text: "Enter your text"
    helper_text: "Text to translate"
    helper_text_mode: "on_focus"
    icon_right: "translate"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:None
    mode: "rectangle"
    width:250

"""
class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(screen_helper)


        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='translate now',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen
    
    def navigation_draw(self):
        print("Navigation")

    def show_data(self, obj):
        if self.username.text is not "":
            user_error = self.username.text + " user does not exist."
            payload= "{\r\n    \"text\":\""+self.username.text+"\"\r\n}"
            response = requests.request("POST", url, headers=headers, data=payload)
        else:
            response = "NO text!"
        self.dialog = MDDialog(title='la translation est : ',
                               text=response.text, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog


DemoApp().run()