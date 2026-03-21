
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

win=Tk()
win.geometry("600x600+450+90")
win.config(bg="#FFFA00")

logo=Image.open("KOTSHOP_logo.png")
logo=logo.resize((280,280))
Logo=ImageTk.PhotoImage(logo)

logo2=Image.open("KOTSHOP_logo.png")
logo2=logo.resize((120,63))
Logo2=ImageTk.PhotoImage(logo2)

logo1=Image.open("KOTSHOP_logo.png")
logo1=logo.resize((208,102))
Logo1=ImageTk.PhotoImage(logo1)

intro_backgr=Image.open("Bac.png")
intro_backgr=intro_backgr.resize((710,600))
intro_backgr=ImageTk.PhotoImage(intro_backgr)

main_frame_back=Image.open("Fram back.png")
main_frame_back=main_frame_back.resize((405,290))
main_frame_back=ImageTk.PhotoImage(main_frame_back)

main_frame_back1=Image.open("Fram back.png")
main_frame_back1=main_frame_back1.resize((500,313))
main_frame_back1=ImageTk.PhotoImage(main_frame_back1)

Location_backgr=Image.open("Location_back.png")
Location_backgr=Location_backgr.resize((360,400))
Location_backgr=ImageTk.PhotoImage(Location_backgr)

Left_Arrow=Image.open("left-arrow.png")
Left_Arrow=Left_Arrow.resize((100,100))
Left_Arrow=ImageTk.PhotoImage(Left_Arrow)

vegetables=Image.open("vegetables.png")
vegetables=vegetables.resize((127,105))
vegetables=ImageTk.PhotoImage(vegetables)

cereals=Image.open("cereals.jpg")
cereals=cereals.resize((127,105))
cereals=ImageTk.PhotoImage(cereals)

meats=Image.open("meats.jpg")
meats=meats.resize((127,105))
meats=ImageTk.PhotoImage(meats)

fruits=Image.open("OIP.jpg")
fruits=fruits.resize((127,105))
fruits=ImageTk.PhotoImage(fruits)

seasonings=Image.open("Seasonings.png")
seasonings=seasonings.resize((127,105))
seasonings=ImageTk.PhotoImage(seasonings)

drinks=Image.open("drinks.png")
drinks=drinks.resize((127,105))
drinks=ImageTk.PhotoImage(drinks)

Vegetables=["Tomatoes","Onions","Carrots","Cabbage","Spinach","Eggplant"]
Cereals=["Rice","Maize flour","Wheat Flour","Sorghum","Pasta","Oats"]
animal_products=["Beef","Steak","Chicken","Fish","Pork"]
Seasonings=["Salt","Vinegar","Oil","Black pepper","Maggi","Curry powder"]
columns=("A","B")

Log=Label(win,image=Logo,bg="#FFFA00")
Log.place(relx=0.5,rely=0.5,anchor="center")
info_frame=None
loc_frame=None
item_frame=None
current_language="English"
tr_frame=None
text_reader=None
tr=None
R=[]
BTN=None
def set_language(lang):
    print("Selected language:", lang)
Tree_item={"English":{"columns":["Animal","Vegetables"],"items":[("Beef","Tomatoes"),("Steak","Onions"),("Chicken","Carrots"),("Fish","Cabbage"),("Pork","Spinach"),("Cereals","Seasonings"),("Rice","Salt"),("Maize flour","Cooking Oil"),("Pasta","Black pepper"),("Sorghum","Maggi cubes"),("Oats","Vinegar"),("Fruits","Drinks"),("Banana","Water"),("Apple","Soda"),("Mango","Juice"),("Orange","Milk"),("Pineapple","Chocolate Drink")]},
           "French":{"columns":["Animal","Légumineuses"],"items":[("Boeuf","Tomates"),("Steak","Onions"),("Poulet","Carrotes"),("Poisson","Chou"),("Porc","Epinard"),("Céréales", "Assaisonnements"), ("Riz", "Sel"), ("Farine de maïs", "Huile de cuisson"), ("Pâtes", "Poivre noir"), ("Sorgho", "Cubes Maggi"), ("Avoine", "Vinaigre"),("Fruits", "Boissons"), ("Banane", "Eau"), ("Pomme", "Soda"), ("Mangue", "Jus"), ("Orange", "Lait"), ("Ananas", "Boisson au chocolat")]}}
info_switch_language={"English":"ABOUT","French":"KOTSHOP-FRENCH-DESCRIPTION"}
def intro_win():
    global R,BTN
    win.withdraw()
    introwin=Toplevel(win)
    introwin.geometry("710x600+450+90")
    widgets_updates={"English":{"ITEMS":"ITEMS","LOC":"LOCATION","HIST":"HISTORY","AB":"ABOUT","LANGUAGE":"LANGUAGES","PUR":"PURCHASE","REG":"Register your name","SL":"Connecting you to simple\n local food\n in the quickest way possible"},"French":{"ITEMS":"ARTICLES","LOC":"PLACE","HIST":"HISTORIQUE","AB":"PROPOS","LANGUAGE":"LANGUES","PUR":"COMMENCER","REG":"Enregistrer votre nom","SL":"Vous connectez à une nourriture \n locale simple\n de la manière la plus rapide possible"}}
    for _,s in widgets_updates.items():
        for j,_ in s.items():
            R.append(j)

    def update_text():
        global current_language,BTN
        BTN=list((items_btn,location_btn,history_btn,guidline_btn,language_btn,purchase,Register_text,main_frame_lab))
        for key,B in zip(R,BTN):
            B.config(text=widgets_updates[current_language][key])
    def toggle_items():

        # If already visible → remove it
        global info_frame, loc_frame, item_frame, columns,tr,tr_frame

        if item_frame and item_frame.winfo_exists():
            item_frame.destroy()
            item_frame = None
            return
        elif loc_frame and loc_frame.winfo_exists():
            loc_frame.destroy()
            loc_frame = None

        elif info_frame and info_frame.winfo_exists():
            info_frame.destroy()

        item_frame = Frame(introwin, bg="#FFFA00", width=442, height=520, relief="solid")
        vscrll=Scrollbar(item_frame,orient="vertical")
        vscrll.pack(side="left",fill="y")

        canva_about_2 = Canvas(item_frame, bg="#FFFA00", height=70)
        canva_about_2.pack(fill="both", side="top")

        canva_about_2.create_image(208, 38, image=Logo2)

        text_about_2 =Text(item_frame, width=50, height=20, background="#005E05",yscrollcommand=vscrll)
        text_about_2.pack(fill="both", expand=True)


        tr_frame=text_about_2
        treeview = ttk.Treeview(text_about_2, columns=columns, show='headings', height=20,yscrollcommand=vscrll)
        tr=treeview
        vscrll.config(command=tr.yview)
        tr.tag_configure("highlight", foreground="#005E05", background="#FFF902", font=("Times New Roman", 8, "bold"))
        tr.tag_configure("highlight2", background="#005E05", foreground="#FFF902", font=("Segoe Print", 13, "bold"))
        if current_language=="English":
            for c, t in zip(columns, Tree_item[current_language]["columns"]):
                tr.heading(c, text=t)
                tr.column(c, anchor="center")
            for index,init_row in enumerate(Tree_item[current_language]["items"]):
                if index==5 or index==11:
                    tr.insert("", "end", values=init_row, tags=("highlight2",))
                else:
                    tr.insert("", "end", values=init_row, tags=("highlight",))
        else:
            for c1, t1 in zip(columns, Tree_item[current_language]["columns"]):
                tr.heading(c1, text=t1)
                tr.column(c1, anchor="center")
            for index,init_row in enumerate(Tree_item[current_language]["items"]):
                if index == 5 or index==11:
                    tr.insert("", "end", values=init_row, tags=("highlight2",))
                else:
                    tr.insert("", "end", values=init_row, tags=("highlight",))
        ST = ttk.Style()
        ST.theme_use("clam")
        ST.configure("Treeview",background="#005E05", foreground="#FFF902",borderwidth=10,rowheight=30)
        ST.configure("Treeview.Heading", background="#005E05", foreground="#FFF902", font=("Segoe Print", 12, "bold"))#,bordercolor="green",borderwidth=5,activebackground="#005E05",activeforeground="#FFF902")
        tr.place(relwidth=1, relheight=1)

        x = location_btn.winfo_x() - guidline_btn.winfo_width() - 200
        y = guidline_btn.winfo_y()
        item_frame.place(x=x, y=y)
    def tree_change_language():
        global current_language,columns

        for col,text in zip(columns,Tree_item[current_language]["columns"]):
            tr.heading(col,text=text)
        for item in tr.get_children():
            tr.delete(item)
        for index, init_row in enumerate(Tree_item[current_language]["items"]):
            if index == 5 or index==11:
                tr.insert("", "end", values=init_row, tags=("highlight2",))
            else:
                tr.insert("", "end", values=init_row, tags=("highlight",))
    def switch_language_french():
        global current_language
        current_language="French"
        update_text()
        if item_frame is not None:
            tree_change_language()
        elif info_frame is not None:
            info_switch()


    def switch_language_english():
        global current_language
        current_language="English"
        update_text()
        if item_frame is not None:
            tree_change_language()
        elif info_frame is not None:
            info_switch()

    def toggle_info():
        global info_frame,loc_frame,item_frame,text_reader
        # If already visible → remove it
        if info_frame and info_frame.winfo_exists():
            info_frame.destroy()
            info_frame = None
            return
        elif loc_frame and loc_frame.winfo_exists():
            loc_frame.destroy()
            loc_frame = None
        elif item_frame and item_frame.winfo_exists():
            item_frame.destroy()
            item_frame = None


            # Create info box
        info_frame = Frame(introwin, bg="#FFFA00",width=442,height=520, relief="solid")

        # Position it beside the button
        x = guidline_btn.winfo_x() + guidline_btn.winfo_width()-50
        y = guidline_btn.winfo_y()
        info_frame.place(x=x, y=y)

        horizontal_scrollbar = Scrollbar(info_frame, orient="horizontal")
        horizontal_scrollbar.pack(side="bottom", fill="x")


        vertical_scrollbar = Scrollbar(info_frame, orient="vertical")
        vertical_scrollbar.pack(side="left", fill="y")

        canva_about=Canvas(info_frame,bg="#FFFA00",height=70)
        canva_about.pack(fill="both",side="top")

        canva_about.create_image(208,38,image=Logo2)


        text_about=Text(info_frame,width=50,height=20,background="#005E05",wrap="none",xscrollcommand=horizontal_scrollbar,yscrollcommand=vertical_scrollbar)
        text_about.pack()
        text_reader=text_about
        horizontal_scrollbar.config(command=text_about.xview)
        vertical_scrollbar.config(command=text_about.yview)
        if current_language=="English":
            with open("ABOUT", "r", encoding="utf-8") as File:
                content = File.read()
                text_about.insert(1.0, f"{content}")
                text_about.tag_add("highlight", "1.0","3.7")
                text_about.tag_config("highlight", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"), relief="raised",
                            underline=True)
                text_about.tag_add("highlight2","17.0","17.10")
                text_about.tag_config("highlight2", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                  relief="raised",
                                  underline=True)
                text_about.tag_add("highlight3","3.0","43.719")
                text_about.tag_config("highlight3",foreground="#FFF902",font=("Franklin Gothic Medium", 7, "bold"), relief="raised")
                text_about.config(state=DISABLED)
        else:
            with open("KOTSHOP-FRENCH-DESCRIPTION", "r", encoding="utf-8") as File:
                content = File.read()
                text_about.insert(1.0, "\n")
                text_about.insert(2.0, f"{content}")
                text_about.tag_add("highlight", "2.0", "2.7")
                text_about.tag_config("highlight", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                      relief="raised",
                                      underline=True)
                text_reader.tag_add("highlight2", "16.0", "16.10")
                text_about.tag_config("highlight2", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                      relief="raised",
                                      underline=True)
                text_about.tag_add("highlight3", "3.0", "43.719")
                text_about.tag_config("highlight3", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                      relief="raised")
                text_about.config(state=DISABLED)

    def info_switch():
        global current_language,text_reader,info_switch_language
        text_reader.config(state=NORMAL)
        text_reader.delete("1.0",END)
        with open(f"{info_switch_language[current_language]}","r",encoding="utf-8") as File:
            content = File.read()
            if current_language=="French":
                text_reader.insert(1.0, "\n")
                text_reader.insert(2.0, f"{content}")
            else:
                text_reader.insert(1.0, f"{content}")
            if current_language=="English":
                text_reader.tag_add("highlight", "1.0", "3.7")
            else:
                text_reader.tag_add("highlight", "2.0", "2.7")
            if current_language == "English":
                text_reader.tag_add("highlight2", "17.0", "17.10")
            else:
                text_reader.tag_add("highlight2", "16.0", "16.10")
            text_reader.tag_config("highlight", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                  relief="raised",
                                  underline=True)
            
            text_reader.tag_config("highlight2", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                  relief="raised",
                                  underline=True)
            text_reader.tag_add("highlight3", "3.0", "43.719")
            text_reader.tag_config("highlight3", foreground="#FFF902", font=("Franklin Gothic Medium", 7, "bold"),
                                  relief="raised")
            text_reader.config(state=DISABLED)
    def toggle_loc():
        global info_frame,loc_frame,item_frame

        # If already visible → remove it
        if loc_frame and loc_frame.winfo_exists():
            loc_frame.destroy()
            loc_frame = None
            return
        elif info_frame and info_frame.winfo_exists():
            info_frame.destroy()
            info_frame = None
        elif item_frame and item_frame.winfo_exists():
            item_frame.destroy()
            item_frame = None

        # Create info box
        loc_frame = Frame(introwin, bg="#FFFA00",width=360,height=400, relief="solid")
        loc_fame_backgr=Label(loc_frame,image=Location_backgr)
        loc_fame_backgr.place(x=0,y=0,relwidth=1,relheight=1)

        #loc_image=Label(loc_frame,image=)
        # Position it beside the button
        x = location_btn.winfo_x() - guidline_btn.winfo_width()-190
        y = guidline_btn.winfo_y()
        loc_frame.place(x=x, y=y)

    super_backg=Label(introwin,image=intro_backgr)
    super_backg.place(x=0,y=0,relwidth=1,relheight=1)

    flyer=Label(introwin,font=("Segoe UI Variable Text Semibold",15),fg="#3BFF00",bg="#FF7100",image=Logo1,borderwidth=5,compound="bottom",anchor="center")
    flyer.pack(pady=60)

    guidline_btn=Button(introwin,text=f"ABOUT",bg="#FFD400",font=("Segoe UI Black",10),fg="#2A6000",width=17,relief="raised",borderwidth=10,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_info)
    guidline_btn.place(x=19,y=35)


    language_btn = Menubutton(introwin, text=f"LANGUAGES", bg="#FFD400", font=("Segoe UI Black", 10), fg="#2A6000", width=17,
                          relief="raised", borderwidth=10,activeforeground="#2A6000",activebackground="#FFD400")
    language_btn.place(x=19, y=100)


    menu = Menu(language_btn, tearoff=0,font=("Segoe UI Black", 10),bg="#FFD400",fg="#2A6000",activeforeground="#FFD400",activebackground="#2A6000")

    language_btn.config(menu=menu)

    menu.add_command(label=f"English",command=switch_language_english)
    menu.add_separator()
    menu.add_command(label=f"French",command=switch_language_french)

    items_btn = Button(introwin, text="ITEMS", bg="#FFD400", font=("Segoe UI Black", 10), fg="#2A6000", width=17,
                          relief="raised", borderwidth=10,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_items)
    items_btn.place(x=530, y=35)

    location_btn = Button(introwin, text=f"LOCATION" , bg="#FFD400", font=("Segoe UI Black", 10), fg="#2A6000", width=17,
                          relief="raised", borderwidth=10,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_loc)
    location_btn.place(x=530, y=100)

    history_btn = Button(introwin, text=f"HISTORY", bg="#FFD400", font=("Segoe UI Black", 10), fg="#2A6000", width=17,
                          relief="raised", borderwidth=10,activeforeground="#FFD400",activebackground="#2A6000")
    history_btn.place(x=530, y=165)


    canva=Canvas(introwin,width=160,height=70,bg="#FFD400")
    canva.place(x=19,y=163)
    canva_text=Frame(canva)
    canva.create_window((78, 12), window=canva_text, width=140, height=20)
    Register_text=Label(canva_text,text="Register your name",font=("Segoe UI Black", 10),fg="#2A6000",bg="#FFD400")
    Register_text.place(relwidth=1,relheight=1)
    canva_frame=Frame(canva)

    canva.create_window((78,35),window=canva_frame,width=122,height=20)
    register_name=Entry(canva_frame,font=("Segoe UI Black", 8),fg="#2A6000",highlightthickness=2,highlightcolor="#2A6000")
    register_name.place(relwidth=1,relheight=1)

    validate_Btn=Button(canva,text="Ok",font=("Segoe UI Black", 10),activeforeground="#FFD400",activebackground="#2A6000",bg="#FFD400",fg="#2A6000")

    canva.create_window((78, 59), window=validate_Btn, width=52, height=20)

    main_frame=Frame(introwin,bg="pink",width=405,height=290)
    main_frame.pack(pady=33)
    slogan="Connecting you to simple\n local food\n in the quickest way possible"
      
    def purchase_win():
      global R,BTN
      introwin.withdraw()
      Purchase_win=Toplevel(win)
      Purchase_win.geometry("710x600+450+90")
      Purchase_win_backg=Label(Purchase_win,image=intro_backgr)
      Purchase_win_backg.place(x=0,y=0,relwidth=1,relheight=1)
      
      def back_main_win():
        Purchase_win.withdraw()
        introwin.deiconify()
      canva_about2=Canvas(Purchase_win,bg="#FFF902",height=70)
      canva_about2.pack(fill="both",side="top")
      canva_about2.create_image(340, 38, image=Logo2)
      left_arrow_back=Button(canva_about2,font=("Segoe UI Black", 8),anchor="center",image=Left_Arrow,bg="#FFF902",command=back_main_win)
      left_arrow_back.place(relheight=1,relwidth=1)
      canva_about2.create_window((48,35),window=left_arrow_back,width=50,height=50)

      can=Canvas(Purchase_win,width=200,height=120,highlightthickness=0,bg="#FFF902",borderwidth=5,relief="groove")
      can.pack(pady=12)
      oval=can.create_oval(7, 10, 200, 120, fill="#005E05", outline="green",width=7)

      text=can.create_text(110,68,text=f"CaTeGoRiEs",font=("Ink Free",20,"bold"),fill="#FFF902")
      
      main_frame1=Frame(Purchase_win,bg="white",width=500,height=313)
      main_frame1.pack()

      main_frame_im=Label(main_frame1,image=main_frame_back1)
      main_frame_im.place(x=0,y=0,relwidth=1,relheight=1)
      
      vegetables_btn=Button(main_frame1,width=125,height=125,image=vegetables,background="#005E05",foreground="yellow",text="Vegetables",font=("Ink Free",15,"bold"),compound="top",activebackground="green",activeforeground="yellow")
      vegetables_btn.place(x=20,y=20)

      animal_btn=Button(main_frame1,width=125,height=125,image=meats,background="#005E05",foreground="yellow",text="Meats",font=("Ink Free",15,"bold"),compound="top",activebackground="green",activeforeground="yellow")
      animal_btn.place(x=190,y=20)
      
      cereals_btn=Button(main_frame1,width=125,height=125,image=cereals,background="#005E05",foreground="yellow",text="Cereals",font=("Ink Free",15,"bold"),compound="top",activebackground="green",activeforeground="yellow")
      cereals_btn.place(x=360,y=20)

      fruits_btn=Button(main_frame1,width=125,height=125,image=fruits,background="#005E05",foreground="yellow",text="Fruits",font=("Ink Free",15,"bold"),compound="top",activebackground="green",activeforeground="yellow")
      fruits_btn.place(x=20,y=163)

      seasons_btn=Button(main_frame1,width=125,height=125,image=seasonings,background="#005E05",foreground="yellow",text="Seasonings",font=("Ink Free",15,"bold"),compound="top",activebackground="green",activeforeground="yellow")
      seasons_btn.place(x=190,y=163)
      
      drinks_btn=Button(main_frame1,width=125,height=125,image=drinks,background="#005E05",foreground="yellow",text="Drinks",font=("Ink Free",15,"bold"),compound="top",activebackground="green",activeforeground="yellow")
      drinks_btn.place(x=360,y=163)

    main_frame_im=Label(main_frame,image=main_frame_back)
    main_frame_im.place(x=0,y=0,relwidth=1,relheight=1)
    main_frame_lab=Label(main_frame,text=slogan,font=("Impact",10),borderwidth=9,width=65,bg="#FFD400",fg="#005E05")
    main_frame_lab.place(y=100,relx=0.5,rely=0.5,anchor="center")

    purchase=Button(main_frame,text=f"PURCHASE",font=("Segoe Print",15,"bold"),relief="raised",borderwidth=4,bg="#FF0800",fg="#FFD400",width=15,activebackground="#FF4F14",activeforeground="#FFD400",command=purchase_win)
    purchase.place(relx=0.5,rely=0.5,anchor="center")

win.after(3000,intro_win)

win.mainloop()
