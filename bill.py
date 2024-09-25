from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #==================variables
        #==================cosmectics
        self.soap=IntVar()
        self.face=IntVar()
        self.shampoo=IntVar()
        self.body=IntVar()
        self.conditioner=IntVar()
#=================grocery
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.tea=IntVar()
        self.wheat=IntVar()
        #====================
        self.frooti=IntVar()
        self.maaza=IntVar()
        self.diet_coke=IntVar()
        self.sprite=IntVar()
        self.limca=IntVar()
        #============product price & tax variables
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar() 
        self.cold_drink_tax=StringVar()
        #=================customer
        self.c_name=StringVar()
        self.c_phn=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #===============customer detail frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)


        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cname_phn=Label(F1,text="Contact No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cname_bill=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #=============cosmetics frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=325)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        shampoo_lbl=Label(F2,text="Shampoo",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        shampoo_txt=Entry(F2,width=10,textvariable=self.shampoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        body_wash_lbl=Label(F2,text="Body Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        body_wash_txt=Entry(F2,width=10,textvariable=self.body,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        conditioner_lbl=Label(F2,text="Conditioner",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        conditioner_txt=Entry(F2,width=10,textvariable=self.conditioner,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

       


        #=============grocery frame
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=325)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        food_oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_oil_cream_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        

        #=============beverages frame
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Beverages",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=325)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        maaza_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        maaza_txt=Entry(F4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        limca_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        dietcoke_lbl=Label(F4,text="Diet Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        dietcoke_txt=Entry(F4,width=10,textvariable=self.diet_coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        

          #===============bill area
        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=260,height=325)
        bill_title=Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #========button frame

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=505,relwidth=1,height=150)
        m1_lbl=Label(F6,text="total cosmetic price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)


        m2_lbl=Label(F6,text="total grocery price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="total beverages price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)


        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Beverages Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=500,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=8,bd=5,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,width=10,bd=5,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,width=8,bd=5,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.exit_app,bg="cadetblue",fg="white",pady=15,width=8,bd=5,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)

     def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_f_p=(self.face.get()*80)
        self.c_sh_p=(self.shampoo.get()*120)
        self.c_b_p=(self.body.get()*130)
        self.c_c_p=(self.conditioner.get()*90)
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_f_p+
                                    self.c_sh_p+
                                    self.c_b_p+
                                    self.c_c_p   )
        
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=(self.rice.get()*40)
        self.g_fo_p=(self.food_oil.get()*120)
        self.g_d_p=(self.daal.get()*130)
        self.g_w_p=(self.wheat.get()*180)
        self.g_t_p=(self.tea.get()*50)
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_t_p   )
        
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.10),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.cd_f_p=(self.frooti.get()*20)
        self.cd_m_p=(self.maaza.get()*30)
        self.cd_d_p=(self.diet_coke.get()*40)
        self.cd_l_p=(self.limca.get()*60)
        self.cd_s_p=(self.sprite.get()*80)
        self.total_cold_drink_price=float(
                                    self.cd_f_p+
                                    self.cd_m_p+
                                    self.cd_d_p+
                                    self.cd_l_p+
                                    self.cd_s_p   )
        
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round((self.total_cold_drink_price*0.18),2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_cold_drink_price+self.c_tax+self.g_tax+self.cd_tax)
     def welcome_bill(self):
            self.textarea.delete('1.0',END)
            self.textarea.insert(END,"\t---MEGA STORE---")
            self.textarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
            self.textarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
            self.textarea.insert(END,f"\nPhone Number : {self.c_phn.get()}")
            self.textarea.insert(END,f"\n=========================") 
            self.textarea.insert(END,f"\nProduct  \tQTY\tPrice")
            self.textarea.insert(END,f"\n=========================")
     def bill_area(self):
          if self.c_name.get()=="" or self.c_phn.get()=="":
               messagebox.showerror("Error","Customer details are must")
          else:
             self.welcome_bill()
             #====cosmetics===
             if self.soap.get()!=0:
                  self.textarea.insert(END,f"\nBath Soap\t  {self.soap.get()}\t{self.c_s_p}")
             if self.face.get()!=0:
                  self.textarea.insert(END,f"\nFace Wash\t  {self.face.get()}\t{self.c_f_p}")

             if self.shampoo.get()!=0:
                  self.textarea.insert(END,f"\nShampoo\t  {self.shampoo.get()}\t{self.c_sh_p}")

             if self.body.get()!=0:
                  self.textarea.insert(END,f"\nBody Wash\t  {self.shampoo.get()}\t{self.c_b_p}")
             if self.conditioner.get()!=0:
                  self.textarea.insert(END,f"\nConditioner\t  {self.conditioner.get()}\t{self.c_c_p}")

            #==========grocery
             if self.rice.get()!=0:
                  self.textarea.insert(END,f"\nRice\t    {self.rice.get()}\t{self.g_r_p}")
             if self.food_oil.get()!=0:
                  self.textarea.insert(END,f"\nFood Oil\t  {self.food_oil.get()}\t{self.g_fo_p}")

             if self.daal.get()!=0:
                  self.textarea.insert(END,f"\nDaal\t    {self.daal.get()}\t{self.g_d_p}")

             if self.wheat.get()!=0:
                  self.textarea.insert(END,f"\nWheat\t   {self.wheat.get()}\t{self.g_w_p}")
             if self.tea.get()!=0:
                  self.textarea.insert(END,f"\nTea\t   {self.tea.get()}\t{self.g_t_p}")

            #=============cold drinks
             if self.frooti.get()!=0:
                  self.textarea.insert(END,f"\nFrooti\t   {self.frooti.get()}\t{self.cd_f_p}")
             if self.maaza.get()!=0: 
                  self.textarea.insert(END,f"\nMaaza\t   {self.maaza.get()}\t{self.cd_m_p}")

             if self.diet_coke.get()!=0:
                  self.textarea.insert(END,f"\nDiet Coke\t {self.diet_coke.get()}\t{self.cd_d_p}")

             if self.limca.get()!=0:
                  self.textarea.insert(END,f"\nLimca\t   {self.limca.get()}\t{self.cd_l_p}")
             if self.sprite.get()!=0:
                  self.textarea.insert(END,f"\nSprite\t   {self.sprite.get()}\t{self.cd_s_p}")

             self.textarea.insert(END,f"\n-------------------------")
             if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\nCosmetic Tax\t\t{self.cosmetic_tax.get()}")
             if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\nGrocery Tax\t\t{self.grocery_tax.get()}")  
             if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\nCold Drink Tax\t\t{self.cold_drink_tax.get()}")
             self.textarea.insert(END,f"\nTotal Bill : \t\tRs. {self.total_bill}")    
             self.textarea.insert(END,f"\n-------------------------")
             self.save_bill()
     def save_bill(self):
             op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
             ##messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved Successfully")
             if op>0:
                self.bill_data=self.textarea.get('1.0',END)
                f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved Successfully")
             else:
                return
             
     def find_bill(self):
          present="no"
          for i in os.listdir("bills/"):
                 if i.split('.')[0]==self.search_bill.get():
                   f1=open(f"bills/{i}","r")
                   self.textarea.delete('1.0',END)
                   for d in f1:
                     self.textarea.insert(END,d)
                   f1.close()
                   present="yes"
          if present=="no":
                 messagebox.showerror("Error","invalid Bill No.")

     def clear_data(self):
        self.soap.set(0)
        self.face.set(0)
        self.shampoo.set(0)
        self.body.set(0)
        self.conditioner.set(0)
#=================grocery
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.tea.set(0)
        self.wheat.set(0)
        #====================
        self.frooti.set(0)
        self.maaza.set(0)
        self.diet_coke.set(0)
        self.sprite.set(0)
        self.limca.set(0)
        #============product price & tax variables
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")
        #=================customer
        self.c_name.set("")
        self.c_phn.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

     def exit_app(self):
         op=messagebox.askyesno("Exit","Do you really want to exit ? ")
         if op>0:
             self.root.destroy()
 
root=Tk()     


obj=Bill_App(root)
root.mainloop()