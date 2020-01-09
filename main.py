from kivy import app
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from database import Database
from database1 import Database1
from database2 import Database2
from kivy.uix.popup import Popup
from kivy.base import EventLoop

from kivy.graphics import Color


class Start(Screen):
    def clear_history(self):
        db1.clear_entries()


class Show(Screen):
    amountt = ObjectProperty(None)

    def on_enter(self, *args):
        thing = db2.get_entry()
        
        if thing is None:
            thing = 0

        if int(thing) >= 0:
            self.amountt.text = "You owe " + str(int(thing)) + " rupees"
        else:
            thing = int(thing)*-1
            self.amountt.text = str(int(thing)) + " already paid in advance"


class PayMoney(Screen):
    money = ObjectProperty(None)

    def submit(self):
        get_val = self.money.text

        if get_val == "":
            get_val = 0

        amount = db2.get_entry()

        if amount is None:
            amount = 0

        new_amount = int(amount) - int(get_val)
        db2.add_entry(new_amount)
        self.money.text = ""


class FixPrice(Screen, Widget):
    shirt_qty = ObjectProperty(None)
    pant_qty = ObjectProperty(None)
    saree_qty = ObjectProperty(None)
    others_qty = ObjectProperty(None)
    fixed_shirt = ObjectProperty(None)
    fixed_pant = ObjectProperty(None)
    fixed_saree = ObjectProperty(None)
    fixed_others = ObjectProperty(None)

    def submit(self):
        if self.shirt_qty.text != "":
            db.add_entry("Shirt", self.shirt_qty.text)
            self.shirt_qty.text = ""
        if self.pant_qty.text != "":
            db.add_entry("Pant", self.pant_qty.text)
            self.pant_qty.text = ""
        if self.saree_qty.text != "":
            db.add_entry("Saree", self.saree_qty.text)
            self.saree_qty.text = ""
        if self.others_qty.text != "":
            db.add_entry("Others", self.others_qty.text)
            self.others_qty.text = ""

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            print("entered")
            print(sm.current)
            print(sm.current_screen)
            sm.get_parent_window()
            return True

    def on_enter(self, *args):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        shirt_val = db.get_entry("Shirt")
        pant_val = db.get_entry("Pant")
        saree_val = db.get_entry("Saree")
        others_val = db.get_entry("Others")

        if shirt_val == "" or shirt_val == -1:
            shirt_val = "Not fixed yet"

        self.fixed_shirt.text = str(shirt_val)

        if pant_val == "" or pant_val == -1:
            pant_val = "Not fixed yet"

        self.fixed_pant.text = str(pant_val)

        if saree_val == "" or saree_val == -1:
            saree_val = "Not fixed yet"

        self.fixed_saree.text = str(saree_val)

        if others_val == "" or others_val == -1:
            others_val = "Not fixed yet"

        self.fixed_others.text = str(others_val)


class AddClothes(Screen):
    tot_shirt = ObjectProperty(None)
    tot_pant = ObjectProperty(None)
    tot_saree = ObjectProperty(None)
    tot_others = ObjectProperty(None)

    def submit1(self):

        if self.tot_shirt.text == "":
            return

        shirt_price = db.get_entry("Shirt")
        no_of_shirt = self.tot_shirt.text

        if no_of_shirt == "":
            no_of_shirt = 0

        if shirt_price == "" or shirt_price == -1:
            show_shirtpopup()
            shirt_price = 0
            no_of_shirt = 0

        shirt_amount = int(no_of_shirt) * int(shirt_price)

        if no_of_shirt != 0:
            db1.add_entry("Shirt", str(int(no_of_shirt)), shirt_price)

        prev_amount = db2.get_entry()

        if prev_amount is None:
            prev_amount = 0

        new_amount = int(prev_amount) + shirt_amount
        db2.add_entry(new_amount)

        self.tot_shirt.text = ""

    def submit2(self):

        if self.tot_pant.text == "":
            return

        pant_price = db.get_entry("Pant")
        no_of_pant = self.tot_pant.text

        if no_of_pant == "":
            no_of_pant = 0

        if pant_price == "" or pant_price == -1:
            show_pantpopup()
            pant_price = 0
            no_of_pant = 0

        pant_amount = int(no_of_pant) * int(pant_price)

        if no_of_pant != 0:
            db1.add_entry("Pant", str(int(no_of_pant)), pant_price)

        prev_amount = db2.get_entry()

        if prev_amount is None:
            prev_amount = 0

        new_amount = int(prev_amount) + pant_amount
        db2.add_entry(new_amount)

        self.tot_pant.text = ""

    def submit3(self):

        if self.tot_saree.text == "":
            return

        saree_price = db.get_entry("Saree")
        no_of_saree = self.tot_saree.text

        if no_of_saree == "":
            no_of_saree = 0

        if saree_price == "" or saree_price == -1:
            show_sareepopup()
            saree_price = 0
            no_of_saree = 0

        saree_amount = int(no_of_saree) * int(saree_price)

        if no_of_saree != 0:
            db1.add_entry("Saree", str(int(no_of_saree)), saree_price)

        prev_amount = db2.get_entry()

        if prev_amount is None:
            prev_amount = 0

        new_amount = int(prev_amount) + saree_amount
        db2.add_entry(new_amount)

        self.tot_saree.text = ""

    def submit4(self):

        if self.tot_others.text == "":
            return

        others_price = db.get_entry("Others")
        no_of_others = self.tot_others.text

        if no_of_others == "":
            no_of_others = 0

        if others_price == "" or others_price == -1:
            show_otherspopup()
            others_price = 0
            no_of_others = 0

        others_amount = int(no_of_others)*int(others_price)

        if no_of_others != 0:
            db1.add_entry("Others", str(int(no_of_others)), others_price)

        prev_amount = db2.get_entry()

        if prev_amount is None:
            prev_amount = 0

        new_amount = int(prev_amount) + others_amount
        db2.add_entry(new_amount)
        self.tot_others.text = ""


class P1(FloatLayout):
    pass


class P2(FloatLayout):
    pass


class P3(FloatLayout):
    pass


class P4(FloatLayout):
    pass


def show_shirtpopup():
    showshirt = P1()

    PopupWindow = Popup(title="Fix Shirt Price", content=showshirt, size_hint=(None, None), size=(700, 700))

    PopupWindow.open()


def show_pantpopup():
    showpant = P2()

    PopupWindow = Popup(title="Fix Pant Price", content=showpant, size_hint=(None, None), size=(700, 700))

    PopupWindow.open()


def show_sareepopup():
    showsaree = P3()

    PopupWindow = Popup(title="Fix Saree Price", content=showsaree, size_hint=(None, None), size=(700, 700))

    PopupWindow.open()


def show_otherspopup():
    showothers = P4()

    PopupWindow = Popup(title="Fix Others Price", content=showothers, size_hint=(None, None), size=(700, 700))

    PopupWindow.open()

class History(Screen):
    date = ObjectProperty(None)
    quantity = ObjectProperty(None)
    typeo = ObjectProperty(None)
    price = ObjectProperty(None)
    tot = ObjectProperty(None)
    date2 = ObjectProperty(None)
    quantity2 = ObjectProperty(None)
    typeo2 = ObjectProperty(None)
    price2 = ObjectProperty(None)
    tot2 = ObjectProperty(None)
    date3 = ObjectProperty(None)
    quantity3 = ObjectProperty(None)
    typeo3 = ObjectProperty(None)
    price3 = ObjectProperty(None)
    tot3 = ObjectProperty(None)
    date4 = ObjectProperty(None)
    quantity4 = ObjectProperty(None)
    typeo4 = ObjectProperty(None)
    price4 = ObjectProperty(None)
    tot4 = ObjectProperty(None)
    date5 = ObjectProperty(None)
    quantity5 = ObjectProperty(None)
    typeo5 = ObjectProperty(None)
    price5 = ObjectProperty(None)
    tot5 = ObjectProperty(None)

    def on_enter(self, *args):
        fdd = open("calc.txt")
        contents = fdd.readlines()

        cnt = 0

        for lin in contents:
            cnt += 1

        if cnt==0:
            self.date.text = ""
            self.quantity.text = ""
            self.typeo.text = ""
            self.price.text = ""
            self.tot.text = ""
            self.date2.text = ""
            self.quantity2.text = ""
            self.typeo2.text = ""
            self.price2.text = ""
            self.tot2.text = ""
            self.date3.text = ""
            self.quantity3.text = ""
            self.typeo3.text = ""
            self.price3.text = ""
            self.tot3.text = ""
            self.date4.text = ""
            self.quantity4.text = ""
            self.typeo4.text = ""
            self.price4.text = ""
            self.tot4.text = ""
            self.date5.text = ""
            self.quantity5.text = ""
            self.typeo5.text = ""
            self.price5.text = ""
            self.tot5.text = ""

            self.tot3.text = "No history"
        elif cnt==1:
            self.tot3.text = ""
            self.date.text = "Date: " + contents[cnt - 1].split(";")[0]
            self.quantity.text = "Quantity: " + contents[cnt - 1].split(";")[1]
            self.typeo.text = "Type: " + contents[cnt - 1].split(";")[2]
            self.price.text = "Price: " + contents[cnt - 1].split(";")[3]
            self.tot.text = "Total: " + contents[cnt - 1].split(";")[4]
        elif cnt==2:
            self.tot3.text = ""
            self.date.text = "Date: " + contents[cnt - 1].split(";")[0]
            self.quantity.text = "Quantity: " + contents[cnt - 1].split(";")[1]
            self.typeo.text = "Type: " + contents[cnt - 1].split(";")[2]
            self.price.text = "Price: " + contents[cnt - 1].split(";")[3]
            self.tot.text = "Total: " + contents[cnt - 1].split(";")[4]
            self.date2.text = "Date: " + contents[cnt - 2].split(";")[0]
            self.quantity2.text = "Quantity: " + contents[cnt - 2].split(";")[1]
            self.typeo2.text = "Type: " + contents[cnt - 2].split(";")[2]
            self.price2.text = "Price: " + contents[cnt - 2].split(";")[3]
            self.tot2.text = "Total: " + contents[cnt - 2].split(";")[4]
        elif cnt==3:
            self.tot3.text = ""
            self.date.text = "Date: " + contents[cnt - 1].split(";")[0]
            self.quantity.text = "Quantity: " + contents[cnt - 1].split(";")[1]
            self.typeo.text = "Type: " + contents[cnt - 1].split(";")[2]
            self.price.text = "Price: " + contents[cnt - 1].split(";")[3]
            self.tot.text = "Total: " + contents[cnt - 1].split(";")[4]
            self.date2.text = "Date: " + contents[cnt - 2].split(";")[0]
            self.quantity2.text = "Quantity: " + contents[cnt - 2].split(";")[1]
            self.typeo2.text = "Type: " + contents[cnt - 2].split(";")[2]
            self.price2.text = "Price: " + contents[cnt - 2].split(";")[3]
            self.tot2.text = "Total: " + contents[cnt - 2].split(";")[4]
            self.date3.text = "Date: " + contents[cnt - 3].split(";")[0]
            self.quantity3.text = "Quantity: " + contents[cnt - 3].split(";")[1]
            self.typeo3.text = "Type: " + contents[cnt - 3].split(";")[2]
            self.price3.text = "Price: " + contents[cnt - 3].split(";")[3]
            self.tot3.text = "Total: " + contents[cnt - 3].split(";")[4]
        elif cnt==4:
            self.tot3.text = ""
            self.date.text = "Date: " + contents[cnt - 1].split(";")[0]
            self.quantity.text = "Quantity: " + contents[cnt - 1].split(";")[1]
            self.typeo.text = "Type: " + contents[cnt - 1].split(";")[2]
            self.price.text = "Price: " + contents[cnt - 1].split(";")[3]
            self.tot.text = "Total: " + contents[cnt - 1].split(";")[4]
            self.date2.text = "Date: " + contents[cnt - 2].split(";")[0]
            self.quantity2.text = "Quantity: " + contents[cnt - 2].split(";")[1]
            self.typeo2.text = "Type: " + contents[cnt - 2].split(";")[2]
            self.price2.text = "Price: " + contents[cnt - 2].split(";")[3]
            self.tot2.text = "Total: " + contents[cnt - 2].split(";")[4]
            self.date3.text = "Date: " + contents[cnt - 3].split(";")[0]
            self.quantity3.text = "Quantity: " + contents[cnt - 3].split(";")[1]
            self.typeo3.text = "Type: " + contents[cnt - 3].split(";")[2]
            self.price3.text = "Price: " + contents[cnt - 3].split(";")[3]
            self.tot3.text = "Total: " + contents[cnt - 3].split(";")[4]
            self.date4.text = "Date: " + contents[cnt - 4].split(";")[0]
            self.quantity4.text = "Quantity: " + contents[cnt - 4].split(";")[1]
            self.typeo4text = "Type: " + contents[cnt - 4].split(";")[2]
            self.price4.text = "Price: " + contents[cnt - 4].split(";")[3]
            self.tot4.text = "Total: " + contents[cnt - 4].split(";")[4]
        elif cnt>=5:
            self.tot3.text = ""
            self.date.text = "Date: " + contents[cnt-1].split(";")[0]
            self.quantity.text = "Quantity: " + contents[cnt-1].split(";")[1]
            self.typeo.text = "Type: " + contents[cnt-1].split(";")[2]
            self.price.text = "Price: " + contents[cnt-1].split(";")[3]
            self.tot.text = "Total: " + contents[cnt-1].split(";")[4]
            self.date2.text = "Date: " + contents[cnt-2].split(";")[0]
            self.quantity2.text = "Quantity: " + contents[cnt-2].split(";")[1]
            self.typeo2.text = "Type: " + contents[cnt-2].split(";")[2]
            self.price2.text = "Price: " + contents[cnt-2].split(";")[3]
            self.tot2.text = "Total: " + contents[cnt-2].split(";")[4]
            self.date3.text = "Date: " + contents[cnt-3].split(";")[0]
            self.quantity3.text = "Quantity: " + contents[cnt-3].split(";")[1]
            self.typeo3.text = "Type: " + contents[cnt-3].split(";")[2]
            self.price3.text = "Price: " + contents[cnt-3].split(";")[3]
            self.tot3.text = "Total: " + contents[cnt-3].split(";")[4]
            self.date4.text = "Date: " + contents[cnt-4].split(";")[0]
            self.quantity4.text = "Quantity: " + contents[cnt-4].split(";")[1]
            self.typeo4.text = "Type: " + contents[cnt-4].split(";")[2]
            self.price4.text = "Price: " + contents[cnt-4].split(";")[3]
            self.tot4.text = "Total: " + contents[cnt-4].split(";")[4]
            self.date5.text = "Date: " + contents[cnt-5].split(";")[0]
            self.quantity5.text = "Quantity: " + contents[cnt-5].split(";")[1]
            self.typeo5.text = "Type: " + contents[cnt-5].split(";")[2]
            self.price5.text = "Price: " + contents[cnt-5].split(";")[3]
            self.tot5.text = "Total: " + contents[cnt-5].split(";")[4]


class WindowManager(ScreenManager):
    pass


db = Database("history.txt")
db1 = Database1("calc.txt")
db2 = Database2("price.txt")
sm = WindowManager()

screens = [Start(name="start"), FixPrice(name="price")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "start"


class MyApp(App):
    def build(self):
        kv = Builder.load_file("my.kv")
        return kv


if __name__ == "__main__":
    MyApp().run()
