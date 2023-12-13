import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

class mykivyApp(App):
 def build(self):
    self.layout = FloatLayout(size=(300,300))
    self.Moneyamount = Label(
    text='Hello',
    color=[46/255, 204/255, 113/255, 255/255],
    size_hint=(.5, .25),
    pos=(650, 750))

    self.money = 500
    self.toGamble = 0
    self.sum = 0
    self.GM ="pngGM.png"
    self.M = "pngM.png"
    self.Star = "star.png"

    self.image1 = Image(
    source= self.M,
    size_hint=(.5, .25),
    pos=(50, 575))

    self.image2 = Image(
    source=self.GM,
    size_hint=(.5, .25),
    pos=(350, 575))

    self.image3 = Image(
    source= self.Star,
    size_hint=(.5, .25),
    pos=(650, 575))

    self.spinB = Button(
    text='Spin!',
    size_hint=(.25, .25),
    pos=(800, 100))
    self.spinB.bind(on_press=self.connectClicker1)

    self.label = Label(
    text='Insert money amount here:',
    color=[46/255, 204/255, 113/255, 255/255],
    size_hint=(.5, .25),
    pos=(50, 250))

    self.warning = Label(
    text='No',
    size_hint=(.5, .25),
    pos=(50, 250))

    self.amount = TextInput(
    size_hint=(.5, .25),
    pos=(50, 100))

    self.connect = Button(
    size_hint=(.25, .15),
    pos=(300, 100))
    self.connect.bind(on_press=self.connectClicker)

    self.pricemoney = Label(text="price money",
    size_hint=(.25, .15),
    pos=(300, 20)
    )

    self.layout.add_widget(self.image1)
    self.layout.add_widget(self.image2)
    self.layout.add_widget(self.image3)
    self.layout.add_widget(self.spinB)
    self.layout.add_widget(self.amount)
    self.layout.add_widget(self.label)
    self.layout.add_widget(self.Moneyamount)
    self.layout.add_widget(self.connect)
    self.layout.add_widget(self.pricemoney)
    return self.layout

 def connectClicker(self,btn):
   #self.sum -= int(self.amount.text)
   #self.Moneyamount.text = str(self.sum)
   self.star = str(int(self.amount.text) * 100)
   self.gm = str(int(self.amount.text) * 10)
   self.m = str(int(self.amount.text) * 2)
   
 
   self.pricemoney.text = ("price money3 Stars!!! = " + self.star + " Green mushroom!! = " + self.gm + " Mushroom! = "+self.m)

 def connectClicker1(self,btn):
   a = random.randint(1,100)
   b = random.randint(1,100)
   c = random.randint(1,100)
   self.sum -= int(self.amount.text)
   self.Moneyamount.text = str(self.sum) + "kr"
   if a <= 50:
    self.image1.source = self.M
    if a >= 51 and a <= 90 :
      self.image1.source = self.GM 
    if a >= 91:
      self.image1.source = self.Star
   if b <= 50:
    self.image2.source = self.M
   if b >= 51 and a <= 90 :
      self.image2.source = self.GM
   if b >= 91:
      self.image2.source = self.Star
   if c <= 50:
    self.image3.source = self.M
   if c >= 51 and a <= 90 :
      self.image3.source = self.GM 
   if c >= 91:
      self.image3.source = self.Star
    
   if self.image1.source == self.M and self.image2.source == self.M and self.image3.source == self.M:
     self.sum += int(self.m)
     self.Moneyamount.text = str(self.sum)
   if self.image1.source == self.GM and self.image2.source == self.GM and self.image3.source == self.GM:
     self.sum += int(self.gm)
     self.Moneyamount.text = str(self.sum)
   if self.image1.source == self.Star and self.image2.source == self.Star and self.image3.source == self.Star:
     self.sum += int(self.star)
     self.Moneyamount.text = str(self.sum)
 #  if int(self.Moneyamount.text) <= self.money:
 #     self.toGamble = int(self.Moneyamount.text)
      

 # def spin(self,btn):
  # self.money-=self.toGamble
  #self.Moneyamount.text = str(self.money)
  
mykivyApp().run()