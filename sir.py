from tkinter import*
import random
import time;
import datetime
from tkinter import messagebox


root= Tk()
root.geometry("1350x740+0+0")
root.title("MRK LIMITED")
root.configure(background='black')

Tops = Frame(root, width= 1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width= 900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width= 440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width= 900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width= 900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame(f2, width= 440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame(f2, width= 440, height=250, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width= 260, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1bb = Frame(f1a, width= 260, height=330, bd=16, relief="raise")
f1bb.pack(side=LEFT)
f1ab = Frame(f1a, width= 260, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width= 450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width= 450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)


Tops.configure(background= 'black')
f1.configure(background= 'black')
f2.configure(background= 'black')

lblInfo = Label(Tops, font=('arial',70,'bold'),text= "MRK LIMITED..", bd=10)
lblInfo.grid(row=0,column=0)


#===========================cost of item==============

def CostofItems():
    Item1 = float(E_tea.get())
    Item2 = float(E_coffee.get())
    Item3 = float(E_icecofee.get())
    Item4 = float(E_black_tea.get())
    Item5 = float(E_milk.get())
    Item6 = float(E_greentea.get())
    Item7 = float(E_milkshake.get())
    Item8 = float(E_energydrnk.get())

    Item9 = float(E_coffee_cake.get())
    Item10 = float(E_red_vel.get())
    Item11 = float(E_bk_forest.get())
    Item12 = float(E_honey_ck.get())
    Item13 = float(E_choc_cake.get())
    Item14 = float(E_hill_ck.get())
    Item15 = float(E_cream_ck.get())
    Item16 = float(E_queen_park_cholate_cake.get())

    Item17 = float(E_monky.get())
    Item18 = float(E_rat.get())
    Item19 = float(E_donky.get())
    Item20 = float(E_mouse.get())
    Item21 = float(E_cat.get())
    Item22 = float(E_ball.get())
    Item23 = float(E_peacock.get())
    Item24 = float(E_queen.get())
   

    PriceofDrinks = (Item1 * 10) + (Item2 * 11) + (Item3 * 12) + (Item4 * 13) + (Item5 * 14) + (Item6 * 15) + (Item7 * 16) + (Item8 * 17)
    Priceofcake =  (Item9 * 20) + (Item10 * 21) + (Item11 * 22) + (Item12 * 23) + (Item13 * 24) + (Item14 * 25) + (Item15 * 26) + (Item16 * 27)
    Priceoftoys =  (Item17 * 30) + (Item18 * 31) + (Item19 * 32) + (Item20 * 33) + (Item21 * 34) + (Item22 * 35) + (Item23 * 36) + (Item24 * 37)
    
    DrinksPrice = "Rs." + str('%.2f'%(PriceofDrinks))
    cakePrice = "Rs." + str('%.2f'%(Priceofcake))
    toysprice =  "Rs." + str('%.2f'%(Priceoftoys))
    Costofcake.set(cakePrice)
    CostofDrinks.set(DrinksPrice)
    Costoftoys.set(toysprice)
    SC = "Rs." + str('%.2f'%(1.1))
    ServiceCharge.set(SC)

    subtotalofITEMS = "Rs." + str('%.2f'%(PriceofDrinks + Priceofcake + Priceoftoys + 1.1))
    subtotal.set(subtotalofITEMS)
    Tax = "Rs." + str('%.2f'%((PriceofDrinks + Priceofcake + Priceoftoys+ 1.1)*0.15))
    paidtax.set(Tax)
    TT = ((PriceofDrinks + Priceofcake + Priceoftoys + 1.1)*0.15)
    TC = "Rs." + str('%.2f'%(PriceofDrinks + Priceofcake + Priceoftoys + 1.1 + TT))
    totalcost.set(TC)


#============================method========================
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do u want to quit?")
    if qExit>0:
        root.destroy()
        return
def Reset():
    paidtax.set("")
    subtotal.set("")
    totalcost.set("")
    CostofDrinks.set("")
    Costofcake.set("")
    Costoftoys.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_tea.set("0")
    E_coffee.set("0")
    E_icecofee.set("0")
    E_black_tea.set("0")
    E_milk.set("0")
    E_greentea.set("0")
    E_milkshake.set("0")
    E_energydrnk.set("0")
    E_coffee_cake.set("0")
    E_red_vel.set("0")
    E_bk_forest.set("0")
    E_honey_ck.set("0")
    E_choc_cake.set("0")
    E_hill_ck.set("0")
    E_cream_ck.set("0")
    E_queen_park_cholate_cake.set("0")

    E_monkey.set("0")
    E_rat.set("0")
    E_donky.set("0")
    E_mouse.set("0")
    E_cat.set("0")
    E_ball.set("0")
    E_peacock.set("0")
    E_queen.set("0")
   
#===============check button=============================
def chkbutton_value():

    if(var1.get() == 1):
        txttea.configure(state = NORMAL)
    elif var1.get() == 0:
        txttea.configure(state = DISABLED)
        E_tea.set("0")
    if(var2.get() == 1):
        txtcoffee.configure(state = NORMAL)
    elif var2.get() == 0:
        txtcoffee.configure(state = DISABLED)
        E_coffee.set("0")
    if(var3.get() == 1):
        txticecofee.configure(state = NORMAL)
    elif var3.get() == 0:
        txticecofee.configure(state = DISABLED)
        E_icecofee.set("0")
    if(var4.get() == 1):
        txtblack_tea.configure(state = NORMAL)
    elif var4.get() == 0:
        txtblack_tea.configure(state = DISABLED)
        E_black_tea.set("0")
    if(var5.get() == 1):
        txtmilk.configure(state = NORMAL)
    elif var5.get() == 0:
        txtmilk.configure(state = DISABLED)
        E_milk.set("0")
    if(var6.get() == 1):
        txtgreentea.configure(state = NORMAL)
    elif var6.get() == 0:
        txtgreentea.configure(state = DISABLED)
        E_greentea.set("0")
    if(var7.get() == 1):
        txtmilkshake.configure(state = NORMAL)
    elif var7.get() == 0:
        txtmilkshake.configure(state = DISABLED)
        E_milkshake.set("0")
    if(var8.get() == 1):
        txtenergydrnk.configure(state = NORMAL)
    elif var8.get() == 0:
        txtenergydrnk.configure(state = DISABLED)
        E_energydrnk.set("0")
    if(var9.get() == 1):
        txtcoffee_cake.configure(state = NORMAL)
    elif var9.get() == 0:
        txtcoffee_cake.configure(state = DISABLED)
        E_coffee_cake.set("0")
    if(var10.get() == 1):
        txtred_vel.configure(state = NORMAL)
    elif var10.get() == 0:
        txtred_vel.configure(state = DISABLED)
        E_red_vel.set("0")
    if(var11.get() == 1):
        txtbk_forest.configure(state = NORMAL)
    elif var11.get() == 0:
        txtbk_forest.configure(state = DISABLED)
        E_bk_forest.set("0")
    if(var12.get() == 1):
        txthoney_ck.configure(state = NORMAL)
    elif var12.get() == 0:
        txthoney_ck.configure(state = DISABLED)
        E_honey_ck.set("0")
    if(var13.get() == 1):
        txtchoc_cake.configure(state = NORMAL)
    elif var13.get() == 0:
        txtchoc_cake.configure(state = DISABLED)
        E_choc_cake.set("0")
    if(var14.get() == 1):
        txthill_ck.configure(state = NORMAL)
    elif var14.get() == 0:
        txthill_ck.configure(state = DISABLED)
        E_hill_ck.set("0")
    if(var15.get() == 1):
        txtcream_ck.configure(state = NORMAL)
    elif var15.get() == 0:
        txtcream_ck.configure(state = DISABLED)
        E_cream_ck.set("0")
    if(var16.get() == 1):
        txtqueen_park.configure(state = NORMAL)
    elif var16.get() == 0:
        txtqueen_park.configure(state = DISABLED)
        E_queen_park_cholate_cake.set("0")

    if(var17.get() == 1):
        txtmonky.configure(state = NORMAL)
    elif var17.get() == 0:
        txtmonky.configure(state = DISABLED)
        E_monky.set("0")
    if(var18.get() == 1):
        txtrat.configure(state = NORMAL)
    elif var18.get() == 0:
        txtrat.configure(state = DISABLED)
        E_rat.set("0")
    if(var19.get() == 1):
        txtdonky.configure(state = NORMAL)
    elif var19.get() == 0:
        txtdonky.configure(state = DISABLED)
        E_donky.set("0")
    if(var20.get() == 1):
        txtmouse.configure(state = NORMAL)
    elif var20.get() == 0:
        txtmouse.configure(state = DISABLED)
        E_mouse.set("0")
    if(var21.get() == 1):
        txtcat.configure(state = NORMAL)
    elif var21.get() == 0:
        txtcat.configure(state = DISABLED)
        E_cat.set("0")
    if(var22.get() == 1):
        txtball.configure(state = NORMAL)
    elif var22.get() == 0:
        txtball.configure(state = DISABLED)
        E_ball.set("0")
    if(var23.get() == 1):
        txtpeacock.configure(state = NORMAL)
    elif var23.get() == 0:
        txtpeacock.configure(state = DISABLED)
        E_peacock.set("0")
    if(var24.get() == 1):
        txtqueen.configure(state = NORMAL)
    elif var24.get() == 0:
        txtqueen.configure(state = DISABLED)
        E_queen.set("0")

    return 
        
#=============================================
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref: \t\t'+Receipt_Ref.get()+"\t\t\t"+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t'+'Quantity\t\t'+"Price \n\n")

    if E_tea.get() > 0:
        txtReceipt.insert(END, 'tea:\t\t'+str(E_tea.get())+'\t\t'+str('Rs%.2f'%(E_tea.get()*10))+'\n')
    if E_coffee.get() > 0:
        txtReceipt.insert(END, 'coffee:\t\t'+str(E_coffee.get())+'\t\t'+str('Rs.%.2f'%(E_coffee.get()*11))+'\n')
    if E_icecofee.get() > 0:
        txtReceipt.insert(END, 'ice cofee:\t\t'+str(E_icecofee.get())+'\t\t'+str('Rs.%.2f'%(E_icecofee.get()*12))+'\n')
    if E_black_tea.get() > 0:
        txtReceipt.insert(END, 'black coffee:\t\t'+str(E_black_tea.get())+'\t\t'+str('Rs.%.2f'%(E_black_tea.get()*13))+'\n')
    if E_milk.get() > 0:
        txtReceipt.insert(END, 'milk:\t\t'+str(E_milk.get())+'\t\t'+str('Rs.%.2f'%(E_milk.get()*14))+'\n')
    if E_greentea.get() > 0:
        txtReceipt.insert(END, 'greentea:\t\t'+str(E_greentea.get())+'\t\t'+str('Rs.%.2f'%(E_greentea.get()*15))+'\n')
    if E_milkshake.get() > 0:
        txtReceipt.insert(END, 'milk shake:\t\t'+str(E_milkshake.get())+'\t\t'+str('Rs.%.2f'%(E_milkshake.get()*16))+'\n')
    if E_energydrnk.get() > 0:
        txtReceipt.insert(END, 'energydrnk\t\t'+str(E_energydrnk.get())+'\t\t'+str('Rs.%.2f'%(E_energydrnk.get()*17))+'\n')
    if E_coffee_cake.get() > 0:
        txtReceipt.insert(END, 'coffee cake:\t\t'+str(E_coffee_cake.get())+'\t\t'+str('Rs.%.2f'%(E_coffee_cake.get()*20))+'\n')
    if E_red_vel.get() > 0:
        txtReceipt.insert(END, 'red velvet cake:\t\t'+str(E_red_vel.get())+'\t\t'+str('Rs.%.2f'%(E_red_vel.get()*21))+'\n')
    if E_bk_forest.get() > 0:
        txtReceipt.insert(END, 'black forest cake:\t\t'+str(E_bk_forest.get())+'\t\t'+str('Rs.%.2f'%(E_bk_forest.get()*22))+'\n')
    if E_honey_ck.get() > 0:
        txtReceipt.insert(END, 'boston cream cake:\t\t'+str(E_honey_ck.get())+'\t\t'+str('Rs.%.2f'%(E_honey_ck.get()*23))+'\n')
    if E_choc_cake.get() > 0:
         txtReceipt.insert(END, 'Lagos Chocolate cake:\t\t'+str(E_choc_cake.get())+'\t\t'+str('Rs.%.2f'%(E_choc_cake.get()*24))+'\n')
    if E_hill_ck.get() > 0:
        txtReceipt.insert(END, 'kilburn Chocolate cake:\t\t'+str(E_hill_ck.get())+'\t\t'+str('Rs.%.2f'%(E_hill_ck.get()*25))+'\n')
    if E_cream_ck.get() > 0:
        txtReceipt.insert(END, 'carlton hill cholate cake:\t\t'+str(E_cream_ck.get())+'\t\t'+str('Rs.%.2f'%(E_cream_ck.get()*26))+'\n')
    if E_queen_park_cholate_cake.get() > 0:
        txtReceipt.insert(END, 'queen park Cholate cake:\t\t'+str(E_queen_park_cholate_cake.get())+'\t\t'+str('Rs.%.2f'%(E_queen_park_cholate_cake.get()*27))+'\n')

    if E_monky.get() > 0:
        txtReceipt.insert(END, 'monky:\t\t'+str(E_monky.get())+'\t\t'+str('Rs.%.2f'%(E_monky.get()*30))+'\n')
    if E_rat.get() > 0:
        txtReceipt.insert(END, 'rat:\t\t'+str(E_rat.get())+'\t\t'+str('Rs.%.2f'%(E_rat.get()*31))+'\n')
    if E_donky.get() > 0:
        txtReceipt.insert(END, 'donky:\t\t'+str(E_donky.get())+'\t\t'+str('Rs.%.2f'%(E_donky.get()*32))+'\n')
    if E_mouse.get() > 0:
        txtReceipt.insert(END, 'mouse:\t\t'+str(E_mouse.get())+'\t\t'+str('Rs.%.2f'%(E_mouse.get()*33))+'\n')
    if E_cat.get() > 0:
         txtReceipt.insert(END, 'cat:\t\t'+str(E_cat.get())+'\t\t'+str('Rs.%.2f'%(E_cat.get()*34))+'\n')
    if E_ball.get() > 0:
        txtReceipt.insert(END, 'ball:\t\t'+str(E_ball.get())+'\t\t'+str('Rs.%.2f'%(E_ball.get()*35))+'\n')
    if E_peacock.get() > 0:
        txtReceipt.insert(END, 'peacock:\t\t'+str(E_peacock.get())+'\t\t'+str('Rs.%.2f'%(E_peacock.get()*36))+'\n')
    if E_queen.get() > 0:
        txtReceipt.insert(END, 'queen:\t\t'+str(E_queen.get())+'\t\t'+str('Rs.%.2f'%(E_queen.get()*37))+'\n')


    txtReceipt.insert(END, '\nCost of Drinks:\t'+CostofDrinks.get()+"\tTax Paid:\t"+ paidtax.get()+"\n")
    txtReceipt.insert(END, 'Cost of cake:\t'+Costofcake.get()+"\tSubTotal:\t"+ subtotal.get()+"\n")
    txtReceipt.insert(END, 'Cost of toys:\t'+Costoftoys.get()+"\tSubTotal:\t"+ subtotal.get()+"\n")
    txtReceipt.insert(END, 'Service Charge:\t'+ServiceCharge.get()+"\tTotal Cost:\t"+ totalcost.get()+"\n")

#=============================================
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)

    

    txttea.configure(state = DISABLED)
    txtcoffee.configure(state = DISABLED)
    txticecofee.configure(state = DISABLED)
    txtblack_tea.configure(state = DISABLED)
    txtgreentea.configure(state = DISABLED)
    txtmilkshake.configure(state = DISABLED)
    txtenergydrnk.configure(state = DISABLED)
    txtcoffee_cake.configure(state = DISABLED)
    txtred_vel.configure(state = DISABLED)
    txtbk_forest.configure(state = DISABLED)
    txthoney_ck.configure(state = DISABLED)
    txtchoc_cake.configure(state = DISABLED)
    txthill_ck.configure(state = DISABLED)
    txtmilk.configure(state = DISABLED)
    txtcream_ck.configure(state = DISABLED)

    txtmonky.configure(state = DISABLED)
    txtrat.configure(state = DISABLED)
    txtdonky.configure(state = DISABLED)
    txtmouse.configure(state = DISABLED)
    txtcat.configure(state = DISABLED)
    txtball.configure(state = DISABLED)
    txtpeacock.configure(state = DISABLED)
    txtqueen.configure(state = DISABLED)
    

#============================variables=========================

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
paidtax = StringVar()
subtotal = StringVar()
totalcost = StringVar()
Costofcake = StringVar()
CostofDrinks = StringVar()
Costoftoys = StringVar()
ServiceCharge = StringVar()

E_tea = IntVar()
E_coffee = IntVar()
E_icecofee = IntVar()
E_black_tea = IntVar()
E_milk = IntVar()
E_greentea = IntVar()
E_milkshake = IntVar()
E_energydrnk = IntVar()

E_coffee_cake = IntVar()
E_red_vel = IntVar()
E_bk_forest = IntVar()
E_honey_ck = IntVar()
E_choc_cake = IntVar()
E_hill_ck = IntVar()
E_cream_ck = IntVar()
E_queen_park_cholate_cake = IntVar()

E_monky = IntVar()
E_rat = IntVar()
E_donky = IntVar()
E_mouse = IntVar()
E_cat = IntVar()
E_ball = IntVar()
E_peacock = IntVar()
E_queen = IntVar()


E_tea.set(0)
E_coffee.set(0)
E_icecofee.set(0)
E_black_tea.set(0)
E_milk.set(0)
E_greentea.set(0)
E_milkshake.set(0)
E_energydrnk.set(0)
E_coffee_cake.set(0)
E_red_vel.set(0)
E_bk_forest.set(0)
E_honey_ck.set(0)
E_choc_cake.set(0)
E_hill_ck.set(0)
E_cream_ck.set(0)
E_queen_park_cholate_cake.set(0)

E_monky.set(0)
E_rat.set(0)
E_donky.set(0)
E_mouse.set(0)
E_cat.set(0)
E_ball.set(0)
E_peacock.set(0)
E_queen.set(0)

DateofOrder.set(time.strftime("%d/%m/%Y"))

#+++++++++++++++drinks++++++++++++++++++++
tea = Checkbutton(f1aa, text= "tea ", variable = var1, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 0, column=0, sticky=W)
coffee = Checkbutton(f1aa, text= "coffee ", variable = var2, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 1, column=0, sticky=W)
icecofee = Checkbutton(f1aa, text= "icecoffee ", variable = var3, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 2, column=0, sticky=W)
black_tea = Checkbutton(f1aa, text= "blacktea ", variable = var4, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 3, column=0, sticky=W)
milk = Checkbutton(f1aa, text= "milk ", variable = var5, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 4, column=0, sticky=W)
greentea = Checkbutton(f1aa, text= "greentea ", variable = var6, onvalue = 1, command = chkbutton_value, offvalue=0, font=('arial',18,'bold')).grid(row = 5, column=0, sticky=W)
milkshake = Checkbutton(f1aa, text= "milkshake ", variable = var7, onvalue = 1, command = chkbutton_value, offvalue=0, font=('arial',18,'bold')).grid(row = 6, column=0, sticky=W)
energydrnk = Checkbutton(f1aa, text= "energydrnk ", variable = var8, onvalue = 1, command = chkbutton_value, offvalue=0, font=('arial',18,'bold')).grid(row = 7, column=0, sticky=W)

#+++++++++++++++++cake++++++++++++++++++++
coffee_cake = Checkbutton(f1ab, text= "coffe ck", variable = var9, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 0, column=0, sticky=W)
red_vel = Checkbutton(f1ab, text= "red vel", variable = var10, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 1, column=0, sticky=W)
bk_forest = Checkbutton(f1ab, text= "blk forest", variable = var11, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 2, column=0, sticky=W)
honey_ck = Checkbutton(f1ab, text= "honey ck", variable = var12, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 3, column=0, sticky=W)
choc_cake = Checkbutton(f1ab, text= "choc cake", variable = var13, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 4, column=0, sticky=W)
hill_ck = Checkbutton(f1ab, text= "hill ck ", variable = var14, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 5, column=0, sticky=W)
cream_ck = Checkbutton(f1ab, text= "cream ck", variable = var15, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 6, column=0, sticky=W)
queen_park = Checkbutton(f1ab, text= "queen park", variable = var16, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 7, column=0, sticky=W)

#===================toys====================
monky = Checkbutton(f1bb, text= "monkey \t", variable = var17, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 0, column=0, sticky=W)
rat = Checkbutton(f1bb, text= "rat \t", variable = var18, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 1, column=0, sticky=W)
donky = Checkbutton(f1bb, text= "donky \t", variable = var19, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 2, column=0, sticky=W)
mouse = Checkbutton(f1bb, text= "mouse \t", variable = var20, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 3, column=0, sticky=W)
cat = Checkbutton(f1bb, text= "cat \t", variable = var21, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 4, column=0, sticky=W)
ball = Checkbutton(f1bb, text= "ball \t", variable = var22, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 5, column=0, sticky=W)
peacock = Checkbutton(f1bb, text= "peacock\t", variable = var23, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 6, column=0, sticky=W)
queen= Checkbutton(f1bb, text= "queen\t", variable = var24, onvalue = 1, offvalue=0, command = chkbutton_value, font=('arial',18,'bold')).grid(row = 7, column=0, sticky=W)



#++++++++++++++++++widget for drinks+++++++++++++++++++
txttea = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_tea, state= DISABLED)
txttea.grid(row =0, column=1)
txtcoffee = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_coffee, state= DISABLED)
txtcoffee.grid(row =1, column=1)
txticecofee = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_icecofee, state= DISABLED)
txticecofee.grid(row =2, column=1)
txtblack_tea = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_black_tea, state= DISABLED)
txtblack_tea.grid(row =3, column=1)
txtmilk = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_milk, state= DISABLED)
txtmilk.grid(row =4, column=1)
txtgreentea = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_greentea, state= DISABLED)
txtgreentea.grid(row =5, column=1)
txtmilkshake = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_milkshake, state= DISABLED)
txtmilkshake.grid(row =6, column=1)
txtenergydrnk = Entry(f1aa,font=('arial',16,'bold'),bd=8, width=6, justify='left',textvariable= E_energydrnk, state= DISABLED)
txtenergydrnk.grid(row =7, column=1)



#+++++++++++++++++widget for cake+++++++++++++++++++++
txtcoffee_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_coffee_cake, state= DISABLED)
txtcoffee_cake.grid(row =0, column=1)
txtred_vel = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_red_vel, state= DISABLED)
txtred_vel.grid(row =1, column=1)
txtbk_forest = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_bk_forest, state= DISABLED)
txtbk_forest.grid(row =2, column=1)
txthoney_ck = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_honey_ck, state= DISABLED)
txthoney_ck.grid(row =3, column=1)
txtchoc_cake = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_choc_cake, state= DISABLED)
txtchoc_cake.grid(row =4, column=1)
txthill_ck = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_hill_ck, state= DISABLED)
txthill_ck.grid(row =5, column=1)
txtcream_ck = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_cream_ck, state= DISABLED)
txtcream_ck.grid(row =6, column=1)
txtqueen_park = Entry(f1ab,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_queen_park_cholate_cake, state= DISABLED)
txtqueen_park.grid(row =7, column=1)


#+++++++++++++++++widget for toy+++++++++++++++++++++
txtmonky = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_monky, state= DISABLED)
txtmonky.grid(row =0, column=1)
txtrat = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_rat, state= DISABLED)
txtrat.grid(row =1, column=1)
txtdonky = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_donky, state= DISABLED)
txtdonky.grid(row =2, column=1)
txtmouse = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_mouse, state= DISABLED)
txtmouse.grid(row =3, column=1)
txtcat = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_cat, state= DISABLED)
txtcat.grid(row =4, column=1)
txtball = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_ball, state= DISABLED)
txtball.grid(row =5, column=1)
txtpeacock = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_peacock, state= DISABLED)
txtpeacock.grid(row =6, column=1)
txtqueen = Entry(f1bb,font=('arial',16,'bold'),bd=8, width=6, justify='left', textvariable= E_queen, state= DISABLED)
txtqueen.grid(row =7, column=1)

#++++++++++++++++INFORMATION++++++++++++++++++++++++++++
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt",bd = 2, anchor = "w")
lblReceipt.grid(row = 0, column = 0, sticky = W)
txtReceipt = Text(ft2, font=('arial', 11, 'bold'), width = 59, height =22, bg="white", bd=8)
txtReceipt.grid(row = 1, column = 0)

#++++++++++++++++cost of item INFORMATION++++++++++++++++++++++++++++
lblCostofDrinks = Label(f2aa, font=('arial', 12, 'bold'), text = "Cost of Drinks\t", bd = 6, anchor="w")
lblCostofDrinks.grid(row = 0, column = 0, sticky = W)
txtCostofDrinks = Entry(f2aa,font=('arial', 12, 'bold'), bd = 6, justify = "left",textvariable=CostofDrinks)
txtCostofDrinks.grid(row = 0, column = 1, sticky = W)

lblCostofcake = Label(f2aa, font=('arial', 12, 'bold'), text = "Cost of cakes", bd = 6, anchor="w")
lblCostofcake.grid(row = 1, column = 0, sticky = W)
txtCostofcake = Entry(f2aa,font=('arial', 12, 'bold'), bd = 6, justify = "left",textvariable=Costofcake)
txtCostofcake.grid(row = 1, column = 1, sticky = W)

lblCostoftoys = Label(f2aa, font=('arial', 12, 'bold'), text = "Cost of toys", bd = 6, anchor="w")
lblCostoftoys.grid(row = 2, column = 0, sticky = W)
txtCostoftoys = Entry(f2aa,font=('arial', 12, 'bold'), bd = 6, justify = "left",textvariable=Costoftoys)
txtCostoftoys.grid(row = 2, column = 1, sticky = W)

lblServiceCharge = Label(f2aa, font=('arial', 12, 'bold'), text = "Service Charge\t", bd = 6, anchor = "w")
lblServiceCharge.grid(row = 3, column = 0, sticky = W)
txtServiceCharge = Entry(f2aa,font=('arial', 12, 'bold'), bd = 6, justify = "left",textvariable=ServiceCharge)
txtServiceCharge.grid(row = 3, column = 1, sticky = W)
txtServiceCharge.grid(row = 3 ,column=1, sticky = W)

#++++++++++++++++payment INFORMATION++++++++++++++++++++++++++++
lblpaidtax = Label(f2ab, font=('arial', 16, 'bold'), text = "paidtax\t", bd = 8, anchor="w")
lblpaidtax.grid(row = 0, column = 0, sticky = W)
txtpaidtax = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable= paidtax)
txtpaidtax.grid(row = 0, column = 1, sticky = W)

lblsubtotal = Label(f2ab, font=('arial', 16, 'bold'), text = "subtotal", bd = 8, anchor="w")
lblsubtotal.grid(row = 1, column = 0, sticky = W)
txtsubtotal = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable=subtotal)
txtsubtotal.grid(row = 1, column = 1, sticky = W)

lbltotalcost = Label(f2ab, font=('arial', 16, 'bold'), text = "total cost\t", bd = 8, anchor = "w")
lbltotalcost.grid(row = 2, column = 0, sticky = W)
txttotalcost = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable= totalcost)
txttotalcost.grid(row = 2, column = 1, sticky = W)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt",bd = 2, anchor = "w")
lblReceipt.grid(row = 0, column = 0, sticky = W)
txtReceipt = Text(ft2, font=('arial', 11, 'bold'), width = 59, height =22, bg="white", bd=8)
txtReceipt.grid(row = 1, column = 0, sticky = W)


#+++++++++++++++++++++++++++++++button+++++++++++++++++++++++++++++++++++
btnTotal=Button(fb2,padx=16, pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5, text="Total ", command = CostofItems).grid(row=0, column=0)
btnReceipt=Button(fb2,padx=16, pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5, text="Receipt ", command = Receipt).grid(row=0, column=1)
btnReset=Button(fb2,padx=16, pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5, text="Reset ", command=Reset).grid(row=0, column=2)
btnExit=Button(fb2,padx=16, pady=1, bd=4, fg="black",font=('arial',16,'bold'), width=5, text="Exit ", command=qExit).grid(row=0, column=3)



root.mainloop()






