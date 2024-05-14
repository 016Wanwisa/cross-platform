from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen

class Scr1(Screen):
    pass

class Scr2(Screen):  # ui 1
    def convert(self,*args):
        num = int(self.ids.txt_number.text)
        # รับค่าจาก id: txt_number แปลงเป็นตัวเลขเก็บไว้ที่ตัวแปร num
        if args[0].text=='base 2':
            self.ids.lbl_output.text = bin(num)[2:]
        elif args[0].text=='base 8':
            self.ids.lbl_output.text = oct(num)[2:]
        elif args[0].text=='base 16':
            self.ids.lbl_output.text = hex(num)[2:]




class UI(ScreenManager): #ทำหน้าที่จัดการหน้าจอต่าง ๆ 
    pass

class convertApp(App):
    def build(self):
        return UI()

if __name__=="__main__":
    convertApp().run()
