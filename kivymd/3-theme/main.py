from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
    

class UI(MDBoxLayout):
    pass

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Pink"
        
        return UI()
    
if __name__=="__main__":
    DemoApp().run()
    