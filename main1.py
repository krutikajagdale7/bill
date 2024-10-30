import os.path
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#fun part

def clear():
    oilEntry.delete(0, END)
    riceEntry.delete(0, END)
    peanutsEntry.delete(0, END)
    saltEntry.delete(0, END)
    DaalEntry.delete(0, END)
    wheatEntry.delete(0, END)

#
    frutiEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    mazaEntry.delete(0, END)
    spriteEntry.delete(0, END)
    coldcoffeEntry.delete(0, END)
    dewEntry.delete(0, END)

    #
    oilEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    peanutsEntry.insert(0, 0)
    saltEntry.insert(0, 0)
    DaalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)

    #
    frutiEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    mazaEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    coldcoffeEntry.insert(0, 0)
    dewEntry.insert(0, 0)

    #
    groceriestaxEntry.delete(0,END)
    colddrinktaxEntry.delete(0, END)

    #
    groceriespriceEntry.delete(0,END)
    colddrinkEntry.delete(0, END)

    #
    nameEntry.delete(0,END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)
    #

    textarea.delete(1.0,END)

#


#




def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)#mail and port number
            ob.starttls()#this method use to establish secure connection
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),reciverEntry.get(),message)#pass from address to address and the mesg
            ob.quit()
            messagebox.showinfo('Success','Bill is Successsful Sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong , Please Try again',parent=root1)
    if textarea.get(1.0,END)=='\n':#text area empty
        messagebox.showerror('Error','Bill is Empty')
    else:
        root1=Toplevel()
        root1.grab_set()#only email window work not main window buttons work
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0,0)


        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10 ,pady=8)

    #
        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10 ,pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        reciverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        reciverLabel.grid(row=0, column=0, padx=10, pady=8)

        reciverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        reciverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=10)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


        sendButton=Button(root1,text='SEND',font=('arial',14,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2, column=0,pady=20)




    root1.mainloop()




def print_bill():
    if textarea.get(1.0,END)=='\n':#text area empty
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')






def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid bill Number')





#create folder
if not os.path.exists('bills'):
    os.mkdir('bills')



def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you Want to save the Bill ?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is Saved Successfully')
        billnumber= random.randint(500,1000)


billnumber=random.randint(500,1000)

def bill_area():

    #add validation
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif groceriespriceEntry.get()=='' and colddrinkEntry.get()=='':
        messagebox.showerror('Error', 'No Products Are Selected')
    elif groceriespriceEntry.get()== '0 Rs' and colddrinkEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No Products Are Selected')
    else:

        textarea.delete(1.0,END)


        textarea.insert(END,'\t\t**Welcome Custmor**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END, f'\nPhone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n==================================================')
        textarea.insert(END,'Product\t\tQuantity\t\tPrice')
        textarea.insert(END, '\n==================================================')
        if oilEntry.get()!='0':
            textarea.insert(END,f'Oil\t\t{oilEntry.get()}\t\t{oilprice} Rs')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t{riceEntry.get()}\t\t{riceprice} Rs')
        if peanutsEntry.get()!='0':
            textarea.insert(END,f'\nPeanuts\t\t{peanutsEntry.get()}\t\t{peanutsprice} Rs')
        if saltEntry.get() != '0':
            textarea.insert(END, f'\nSalt\t\t{saltEntry.get()}\t\t{saltprice} Rs')
        if DaalEntry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t{DaalEntry.get()}\t\t{daalprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t{wheatEntry.get()}\t\t{wheatprice} Rs')
        if frutiEntry.get() != '0':
            textarea.insert(END, f'\nFruti\t\t{frutiEntry.get()}\t\t{frutiprice} Rs')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t{pepsiEntry.get()}\t\t{pepsiprice} Rs')
        if mazaEntry.get() != '0':
            textarea.insert(END, f'\nMaza\t\t{mazaEntry.get()}\t\t{mazaprice} Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t{spriteEntry.get()}\t\t{spriteprice} Rs')
        if coldcoffeEntry.get() != '0':
            textarea.insert(END, f'\nCold Coffee\t\t{coldcoffeEntry.get()}\t\t{coldcoffeprice} Rs')
        if dewEntry.get() != '0':
            textarea.insert(END, f'\nDew\t\t{dewEntry.get()}\t\t{dewprice} Rs')
        textarea.insert(END, '\n--------------------------------------------------')

        if groceriestaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGroceries Tax\t\t\t{groceriestaxEntry.get()}')
        if colddrinktaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCold Drink Tax\t\t\t{colddrinktaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t{totalbill}')

        textarea.insert(END, '\n--------------------------------------------------')
        save_bill()




def total():
    global oilprice,riceprice,peanutsprice,saltprice,daalprice,wheatprice
    global frutiprice,pepsiprice,mazaprice,spriteprice,coldcoffeprice,dewprice
    global totalbill
    #groceries
    oilprice=int(oilEntry.get())*100
    riceprice=int(riceEntry.get())*50
    peanutsprice=int(peanutsEntry.get())*90
    saltprice=int(saltEntry.get())*20
    daalprice=int(DaalEntry.get())*50
    wheatprice=int(wheatEntry.get())*70


    totalgroceriesprice=oilprice+riceprice+peanutsprice+saltprice+daalprice+wheatprice
    groceriespriceEntry.delete(0,END)
    groceriespriceEntry.insert(0,f'{totalgroceriesprice} Rs')
    groceriestax=totalgroceriesprice*0.05
    groceriestaxEntry.delete(0,END)
    groceriestaxEntry.insert(0,str(groceriestax) + 'Rs')

#colddrinks
    frutiprice = int(frutiEntry.get())*50
    pepsiprice=int(pepsiEntry.get())*20
    mazaprice=int(mazaEntry.get())*10
    spriteprice=int(spriteEntry.get())*40
    coldcoffeprice=int(coldcoffeEntry.get())*50
    dewprice=int(dewEntry.get())*30

    totalcolddrinkprice=frutiprice+pepsiprice+mazaprice+spriteprice+coldcoffeprice+dewprice
    colddrinkEntry.delete(0, END)
    colddrinkEntry.insert(0,f'{totalcolddrinkprice} Rs')
    colddrinktax = totalcolddrinkprice *0.08
    colddrinktaxEntry.delete(0, END)
    colddrinktaxEntry.insert(0, str(colddrinktax) + 'Rs')

    totalbill=totalgroceriesprice+totalcolddrinkprice+groceriestax+colddrinktax


#GUI part
root=Tk()
root.title('Billing System')
root.geometry('1270x685')
root.iconbitmap('kon.ico')
headingLabel=Label(root,text='Billing System',font=('times new roman',30,'bold')
                   ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)


customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)
phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',
                    font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(fill =X,padx=70)

groceriesFrame=LabelFrame(productsFrame,text='Groceries',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceriesFrame.grid(row=0,column=0)

oilLabel=Label(groceriesFrame,text='Oil',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
oilLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceriesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=0,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

riceLabel=Label(groceriesFrame,text='Rice',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
riceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceriesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=1,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

peanutsLabel=Label(groceriesFrame,text='Peanuts',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
peanutsLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
peanutsEntry=Entry(groceriesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
peanutsEntry.grid(row=2,column=1,pady=9,padx=10)
peanutsEntry.insert(0,0)

saltLabel=Label(groceriesFrame,text='Salt',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
saltLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
saltEntry=Entry(groceriesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
saltEntry.grid(row=3,column=1,pady=9,padx=10)
saltEntry.insert(0,0)

DaalLabel=Label(groceriesFrame,text='Daal',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
DaalLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
DaalEntry=Entry(groceriesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DaalEntry.grid(row=4,column=1,pady=9,padx=10)
DaalEntry.insert(0,0)


wheatLabel=Label(groceriesFrame,text='Wheat',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
wheatLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceriesFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=5,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

#cold drink
colddrinkFrame=LabelFrame(productsFrame,text='Cold Drink',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
colddrinkFrame.grid(row=0,column=1)

frutiLabel=Label(colddrinkFrame,text='Fruti',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
frutiLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
frutiEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frutiEntry.grid(row=0,column=1,pady=9,padx=10)
frutiEntry.insert(0,0)
pepsiLabel=Label(colddrinkFrame,text='Pepsi',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

mazaLabel=Label(colddrinkFrame,text='Maza',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
mazaLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
mazaEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
mazaEntry.grid(row=3,column=1,pady=9,padx=10)
mazaEntry.insert(0,0)

spriteLabel=Label(colddrinkFrame,text='Sprite',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
spriteLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=4,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

coldcoffeLabel=Label(colddrinkFrame,text='Coldcoffe',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
coldcoffeLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
coldcoffeEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
coldcoffeEntry.grid(row=5,column=1,pady=9,padx=10)
coldcoffeEntry.insert(0,0)

dewLabel=Label(colddrinkFrame,text='Dew',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
dewLabel.grid(row=6,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=6,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

'''cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=2)

fashwashLabel=Label(cosmeticsFrame,text='Fash Wash',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
fashwashLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
fashwashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fashwashEntry.grid(row=0,column=1,pady=9,padx=10)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
bodylotionLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=1,column=1,pady=9,padx=10)



soapLabel=Label(cosmeticsFrame,text='Soap',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
soapLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
soapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
soapEntry.grid(row=2,column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
facecreamLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=3,column=1,pady=9,padx=10)


hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)


hairspreyLabel=Label(cosmeticsFrame,text='Hair Sprey',font=('times new roman',15,'bold'),bg="gray20",
                fg='white')
hairspreyLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
hairspreyEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairspreyEntry.grid(row=5,column=1,pady=9,padx=10)'''



#
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=150)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=-7,relief=GROOVE)
billareaLabel.pack(fill=X)



scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',14,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()


groceriespriceLabel=Label(billmenuFrame,text='Groceries Price',font=('times new roman',14,'bold'),bg="gray20",
                fg='white')
groceriespriceLabel.grid(row=0,column=0,pady=9,padx=10)

groceriespriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
groceriespriceEntry.grid(row=0,column=1,pady=9,padx=5)



#
colddrinkLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),bg="gray20",
                fg='white')
colddrinkLabel.grid(row=1,column=0,pady=9,padx=10)

colddrinkEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
colddrinkEntry.grid(row=1,column=1,pady=9,padx=5)


'''cosmeticspriceLabel=Label(billmenuFrame,text='Cosmetics Price',font=('times new roman',14,'bold'),bg="gray20",
                fg='white')
cosmeticspriceLabel.grid(row=2,column=0,pady=9,padx=10)

cosmeticspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=2,column=1,pady=9,padx=5)'''



groceriestaxLabel=Label(billmenuFrame,text='Groceries Tax',font=('times new roman',14,'bold'),bg="gray20",
                fg='white')
groceriestaxLabel.grid(row=0,column=2,pady=9,padx=10)

groceriestaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
groceriestaxEntry.grid(row=0,column=3,pady=9,padx=5)





colddrinktaxLabel=Label(billmenuFrame,text='ColdDrink Tax',font=('times new roman',14,'bold'),bg="gray20",
                fg='white')
colddrinktaxLabel.grid(row=1,column=2,pady=9,padx=10)

colddrinktaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
colddrinktaxEntry.grid(row=1,column=3,pady=9,padx=5)


'''cosmeticstaxLabel=Label(billmenuFrame,text='Cosmetics Tax',font=('times new roman',14,'bold'),bg="gray20",
                fg='white')
cosmeticstaxLabel.grid(row=2,column=2,pady=9,padx=10)

cosmeticstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticstaxEntry.grid(row=2,column=3,pady=9,padx=5)'''


buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',
                   bd=5,width=8,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)


billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',
                   bd=5,width=8,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)



emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',
                   bd=5,width=8,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)


printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',
                   bd=5,width=8,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)


clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',
                   bd=5,width=8,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()