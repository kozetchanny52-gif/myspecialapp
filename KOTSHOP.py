from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import sounddevice as sd
import soundfile as sf
import numpy as np
from itertools import cycle

win=Tk()
win.geometry("600x600+450+90")
win.config(bg="#FFFA00")


logo=Image.open("updated_logo.png")
logo=logo.resize((280,280))
Logo=ImageTk.PhotoImage(logo)
pur_win=None 
logo2=Image.open("KOTSHOP_logo.png")
logo2=logo2.resize((120,63))
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

animal_backgr=Image.open("meats.jpg")
animal_backgr=animal_backgr.resize((455,358))
animal_backgr=ImageTk.PhotoImage(animal_backgr)

frame_animal_backgr=Image.open("animalback.png")
frame_animal_backgr=frame_animal_backgr.resize((455,400))
frame_animal_backgr=ImageTk.PhotoImage(frame_animal_backgr)

veg_win_backg=Image.open("vegetables.png")
veg_win_backg=veg_win_backg.resize((455,358))
veg_win_backg=ImageTk.PhotoImage(veg_win_backg)

info_pic=Image.open("info.jpg")
info_pic=info_pic.resize((30,30))
info_pic=ImageTk.PhotoImage(info_pic)
onions_pic=Image.open("onions.jpg")
onions_pic=onions_pic.resize((130,90))
onions_pic=ImageTk.PhotoImage(onions_pic)

carrot_pic=Image.open("carrots.jpg")
carrot_pic=carrot_pic.resize((130,90))
carrot_pic=ImageTk.PhotoImage(carrot_pic)

beef_pic=Image.open("beef.png")
beef_pic=beef_pic.resize((130,90))
beef_pic=ImageTk.PhotoImage(beef_pic)

steak_pic=Image.open("steak.jpg")
steak_pic=steak_pic.resize((130,90))
steak_pic=ImageTk.PhotoImage(steak_pic)

chicken_pic=Image.open("chicken.jpg")
chicken_pic=chicken_pic.resize((130,90))
chicken_pic=ImageTk.PhotoImage(chicken_pic)

pork_pic=Image.open("pork.jpeg")
pork_pic=pork_pic.resize((130,90))
pork_pic=ImageTk.PhotoImage(pork_pic)
add_to_cart=Image.open("add_to_cart.png")
add_to_cart=add_to_cart.resize((54,36))
add_to_cart=ImageTk.PhotoImage(add_to_cart)
columns=("A","B")

tomatoes_pic=Image.open("tomatos.jpg")
tomatoes_pic=tomatoes_pic.resize((130,90))
tomatoes_pic=ImageTk.PhotoImage(tomatoes_pic)

cabbage_pic=Image.open("cabbage.jpg")
cabbage_pic=cabbage_pic.resize((130,90))
cabbage_pic=ImageTk.PhotoImage(cabbage_pic)

Log=Label(win,image=Logo,bg="#FFFA00")
Log.place(relx=0.5,rely=0.5,anchor="center")
hist_frame=None
info_frame=None
loc_frame=None
item_frame=None
current_language="English"
veg_btn=None
an_btn=None
cereal_btn=None
fruit_btn=None
season_btn=None
drink_btn=None
tr_frame=None
text_reader=None
tr=None
R=[]
BTN=None
colors_toggle=["#1EFF00","#FF7300","#FF0000"]


def click_sound():
    sr = 44600

    # --- First impact (sharp) ---
    t1 = np.linspace(0, 0.012, int(sr * 0.012), False)
    noise1 = np.random.randn(len(t1))
    thump1 = np.sin(2 * np.pi * 250 * t1)
    click1 = (0.8 * noise1 + 0.2 * thump1) * np.exp(-90 * t1)

    # --- Tiny gap ---
    gap = np.zeros(int(sr * 0.003))

    # --- Second lighter impact (bounce) ---
    t2 = np.linspace(0, 0.015, int(sr * 0.015), False)
    noise2 = np.random.randn(len(t2))
    thump2 = np.sin(2 * np.pi * 180 * t2)
    click2 = (0.6 * noise2 + 0.4 * thump2) * np.exp(-70 * t2)

    # Combine
    sound = np.concatenate([click1, gap, click2])

    # Normalize & soften
    sound = sound / np.max(np.abs(sound)) * 5

    sd.play(sound, sr)


def set_language(lang):
    print("Selected language:", lang)
Tree_item={"English":{"columns":["Animal","Vegetables"],"items":[("Beef","Tomatoes"),("Steak","Onions"),("Chicken","Carrots"),("Pork","Spinach"),("Cereals","Seasonings"),("Rice","Salt"),("Maize flour","Cooking Oil"),("Sorghum","Maggi cubes"),("Oats","Vinegar")]}#,("Fruits","Drinks"),("Banana","Water"),("Apple","Soda"),("Mango","Juice"),("Orange","Milk"),("Pineapple","Chocolate Drink")]},
           ,"French":{"columns":["Animal","Légumineuses"],"items":[("Boeuf","Tomates"),("Steak","Onions"),("Poulet","Carrotes"),("Porc","Epinard"),("Céréales", "Assaisonnements"), ("Riz", "Sel"), ("Farine de maïs", "Huile de cuisson"), ("Sorgho", "Cubes Maggi"), ("Avoine", "Vinaigre")]}}#,("Fruits", "Boissons"), ("Banane", "Eau"), ("Pomme", "Soda"), ("Mangue", "Jus"), ("Orange", "Lait"), ("Ananas", "Boisson au chocolat")]}}
info_switch_language={"English":"ABOUT","French":"KOTSHOP-FRENCH-DESCRIPTION"}
def intro_win():
    global R,BTN,colors_toggle
    win.withdraw()
    introwin=Toplevel(win)
    introwin.geometry("710x600+450+90")
   
    widgets_updates={"English":{"ITEMS":"ITEMS","LOC":"LOCATION","HIST":"HISTORY","AB":"ABOUT","LANGUAGE":"LANGUAGES","PUR":"PURCHASE","REG":"Register your name","SL":"Connecting you to simple\n local food\n in the quickest way possible"},"French":{"ITEMS":"ARTICLES","LOC":"PLACE","HIST":"HISTORIQUE","AB":"PROPOS","LANGUAGE":"LANGUES","PUR":"COMMENCER","REG":"Enregistrer votre nom","SL":"Vous connectez à une nourriture \n locale simple\n de la manière la plus rapide possible"}}
    for _,s in widgets_updates.items():
        for j,_ in s.items():
            R.append(j)
    def update_text():
        global current_language,BTN,veg_btn,an_btn,fruit_btn,cereal_btn,season_btn,fruit_btn
        BTN=list((items_btn,location_btn,history_btn,guidline_btn,language_btn,purchase,Register_text,main_frame_lab))
        for key,B in zip(R,BTN):
            B.config(text=widgets_updates[current_language][key])

   
    def switch_language_french():
        global current_language
        current_language="French"
        click_sound()
        update_text()
        if item_frame is not None:
            tree_change_language()
        elif info_frame is not None:
            info_switch()

    def switch_language_english():
        global current_language
        current_language="English"
        click_sound()
        update_text()
        if item_frame is not None:
            tree_change_language()
        elif info_frame is not None:
            info_switch()
   
    def toggle_items():
        click_sound()
        # If already visible → remove it
        global info_frame, loc_frame, item_frame, columns,tr,tr_frame,hist_frame

        if item_frame and item_frame.winfo_exists():
            item_frame.destroy()
            item_frame = None
            return
        elif loc_frame and loc_frame.winfo_exists():
            loc_frame.destroy()
            loc_frame = None

        elif info_frame and info_frame.winfo_exists():
            info_frame.destroy()
            info_frame=None
        elif hist_frame and hist_frame.winfo_exists():
            hist_frame.destroy()
            hist_frame = None

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

    
    def toggle_info():
        global info_frame,loc_frame,item_frame,text_reader,hist_frame
        # If already visible → remove it
        click_sound()
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
        elif hist_frame and hist_frame.winfo_exists():
            hist_frame.destroy()
            hist_frame = None


            # Create info box
        info_frame = Frame(introwin, bg="#FFFA00",width=442,height=520, relief="solid")

        # Position it beside the button
        x = guidline_btn.winfo_x() + guidline_btn.winfo_width()-50
        y = guidline_btn.winfo_y()
        info_frame.place(x=x, y=y)

        horizontal_scrollbar =Scrollbar(info_frame,width=13,orient="horizontal",bg="green")
        horizontal_scrollbar.pack(side="bottom", fill="x")


        vertical_scrollbar = Scrollbar(info_frame,width=13,orient="vertical")
        vertical_scrollbar.pack(side="left", fill="y")

        canva_about=Canvas(info_frame,bg="#FFFA00",height=70)
        canva_about.pack(fill="both",side="top")

        canva_about.create_image(208,38,image=Logo2)


        text_about=Text(info_frame,width=50,height=20,background="#005E05",wrap="none",xscrollcommand=horizontal_scrollbar,yscrollcommand=vertical_scrollbar)
        text_about.pack()
        text_reader=text_about
        horizontal_scrollbar.configure(command=text_about.xview)
        vertical_scrollbar.configure(command=text_about.yview)
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
        global current_language,text_reader,info_switch_language,hist_frame
        click_sound()
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
        global info_frame,loc_frame,item_frame,colors_toggle,hist_frame
        click_sound()
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
        elif hist_frame and hist_frame.winfo_exists():
            hist_frame.destroy()
            hist_frame = None

        # Create info box
        loc_frame = Frame(introwin, bg="#FFFA00",width=360,height=400, relief="solid")
        loc_fame_backgr=Label(loc_frame,image=Location_backgr)
        loc_fame_backgr.place(x=0,y=0,relwidth=1,relheight=1)

        #loc_image=Label(loc_frame,image=)
        # Position it beside the button
        x = location_btn.winfo_x() - guidline_btn.winfo_width()-190
        y = guidline_btn.winfo_y()
        loc_frame.place(x=x, y=y)

    def toggle_hist():
      global info_frame,loc_frame,item_frame,colors_toggle,hist_frame
      click_sound()
      # If already visible → remove it
      if hist_frame and hist_frame.winfo_exists():
        hist_frame.destroy()
        hist_frame = None
        return
      elif info_frame and info_frame.winfo_exists():
        info_frame.destroy()
        info_frame = None
      elif item_frame and item_frame.winfo_exists():
        item_frame.destroy()
        item_frame = None
      elif loc_frame and loc_frame.winfo_exists():
            loc_frame.destroy()
            loc_frame = None
    

        # Create info box
      hist_frame = Frame(introwin, bg="#FFFA00",width=360,height=400, relief="solid")
      hist_fame_backgr=Label(loc_frame,image=Location_backgr)
      hist_fame_backgr.place(x=0,y=0,relwidth=1,relheight=1)

        #loc_image=Label(loc_frame,image=)
        # Position it beside the button
      x = location_btn.winfo_x() - guidline_btn.winfo_width()-190
      y = guidline_btn.winfo_y()
      hist_frame.place(x=x, y=y)
    super_backg=Label(introwin,image=intro_backgr)
    super_backg.place(x=0,y=0,relwidth=1,relheight=1)

    flyer=Label(introwin,font=("Segoe UI Variable Text Semibold",15),fg="#3BFF00",bg="#FF7300",image=Logo1,borderwidth=5,compound="bottom",anchor="center")
    flyer.pack(pady=60)
    def color1(): 
      flyer.config(bg=colors_toggle[0])
      introwin.after(500,color2)
    def color2(): 
      flyer.config(bg=colors_toggle[1])
      introwin.after(500,color3)
    def color3(): 
      flyer.config(bg=colors_toggle[2])
      introwin.after(500,color1)    
    color1()
    color2()
    color3()
    guidline_btn=Button(introwin,text=f"ABOUT",bg="#FFD400",font=("Segoe UI Black",10),fg="#2A6000",borderwidth=10,width=17,relief="raised",activeforeground="#FFD400",activebackground="#2A6000",command=toggle_info)
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
                          relief="raised", borderwidth=10,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_hist)
    history_btn.place(x=530, y=165)


    canva=Canvas(introwin,width=160,height=70,bg="#FFD400")
    canva.place(x=19,y=163)
    canva_text=Frame(canva)
    canva.create_window((78, 12), window=canva_text, width=140, height=20)
    Register_text=Label(canva_text,text="Register your name",font=("Segoe UI Black", 10),fg="#2A6000",bg="#FFD400")
    Register_text.place(relwidth=1,relheight=1)
    canva_frame=Frame(canva)

    canva.create_window((78,40),window=canva_frame,width=122,height=20)
    register_name=Entry(canva_frame,font=("Segoe UI Black", 10),fg="#2A6000",highlightthickness=2,highlightcolor="#2A6000",highlightbackground="#2A6000")
    register_name.place(relwidth=1,relheight=1)

    main_frame=Frame(introwin,bg="pink",width=405,height=290)
    main_frame.pack(pady=33)
    slogan="Connecting you to simple\n local food\n in the quickest way possible"
          
    def purchase_win():
      global R,BTN,veg_btn,an_btn,cereal_btn,season_btn,fruit_btn,drink_btn,pur_win
      click_sound()
      introwin.withdraw()
      Purchase_win=Toplevel(win)
      Purchase_win.geometry("710x600+450+90")
      Purchase_win_backg=Label(Purchase_win,image=intro_backgr)
      Purchase_win_backg.place(x=0,y=0,relwidth=1,relheight=1)
      pur_win=Purchase_win
      
      def back_main_win():
        click_sound()
        Purchase_win.withdraw()
        introwin.deiconify()
      canva_about2=Canvas(Purchase_win,bg="#FFF902",height=70)
      canva_about2.pack(fill="both",side="top")
      canva_about2.create_image(340, 38, image=Logo2)
      left_arrow_back=Button(canva_about2,font=("Segoe UI Black", 8),anchor="center",image=Left_Arrow,bg="#FFF902",command=back_main_win)
      left_arrow_back.place(relheight=1,relwidth=1)
      canva_about2.create_window((48,35),window=left_arrow_back,width=50,height=50)

      can=Canvas(Purchase_win,width=200,height=120,highlightthickness=0,bg="#FFF902",borderwidth=6,relief="groove")
      can.pack(pady=12)
      oval=can.create_oval(7, 10, 200, 120, fill="#005E05", outline="green",width=7)

      text=can.create_text(110,68,text=f"CaTeGoRiEs",font=("Ink Free",20,"bold"),fill="#FFF902")
      
      main_frame1=Frame(Purchase_win,bg="white",width=500,height=313)
      main_frame1.pack()

      main_frame_im=Label(main_frame1,image=main_frame_back1)
      main_frame_im.place(x=0,y=0,relwidth=1,relheight=1)
      
      vegetables_btn=Button(main_frame1,command=veg_win,width=125,height=125,image=vegetables,background="#005E05",foreground="yellow",font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      vegetables_btn.place(x=20,y=20)
      
      animal_btn=Button(main_frame1,command=animal_win,width=125,height=125,image=meats,background="#005E05",foreground="yellow",font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # pyright: ignore[reportUndefinedVariable]
      animal_btn.place(x=190,y=20)
       
      cereals_btn=Button(main_frame1,command=cereal_win,width=125,height=125,image=cereals,background="#005E05",foreground="yellow",font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      cereals_btn.place(x=360,y=20)

    

      seasons_btn=Button(main_frame1,width=125,height=125,image=seasonings,background="#005E05",foreground="yellow",font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      seasons_btn.place(x=190,y=163)
      
      toggle_button_colors=list((vegetables_btn,animal_btn,cereals_btn,seasons_btn))
      
      def change_button_colors_1():
        can.config(bg="yellow")
        oval=can.create_oval(7, 10, 200, 120, fill="#005E05", outline="green",width=7)
        text=can.create_text(110,68,text=f"CaTeGoRiEs",font=("Ink Free",20,"bold"),fill="yellow")
        for k1 in toggle_button_colors:
            k1.config(bg="#005E05")
            k1.config(fg="yellow")
        Purchase_win.after(400,change_button_colors_2)
      def change_button_colors_2():
        can.config(bg="red")
        oval=can.create_oval(7, 10, 200, 120, fill=colors_toggle[0], outline="green",width=7)
        text=can.create_text(110,68,text=f"CaTeGoRiEs",font=("Ink Free",20,"bold"),fill=colors_toggle[1])
        for k2 in toggle_button_colors:
            k2.config(bg="red")  
        Purchase_win.after(400,change_button_colors_1)
      change_button_colors_1()
      change_button_colors_2()
          
    
      if current_language=="English":
        vegetables_btn.config(text="Vegetables")
        animal_btn.config(text="Animal")
        cereals_btn.config(text="Cereals")
        seasons_btn.config(text="Seasonings")
      else:
        vegetables_btn.config(text="Légumineuses")
        animal_btn.config(text="Animal")
        cereals_btn.config(text="Cereals")
        seasons_btn.config(text="Saisonnements")
   
    def test_purchase_win():
        person_name=register_name.get().strip()
        click_sound()
        if not (person_name and all(cha.isalpha() or cha==" "  for cha in person_name)):
          register_name.config(highlightbackground="red")
          register_name.config(highlightcolor="red")
          register_name.config(fg="red")
          warning= "INVALID!" 
          register_name.delete(0,END)
          register_name.insert(END,warning)
          def highlight_bg_change():
            register_name.config(highlightbackground="#2A6000")
            register_name.config(highlightcolor="#2A6000")
            register_name.config(fg="#2A6000")
            register_name.delete(0,END)
          introwin.after(700,highlight_bg_change)
        else:
            register_name.config(state="readonly")
            purchase_win()

    def animal_win():
      global R,BTN,veg_btn,an_btn,cereal_btn,season_btn,fruit_btn,drink_btn,pur_win
      click_sound()
      pur_win.withdraw()
      Animal_win=Toplevel(pur_win)
      Animal_win.geometry("710x600+450+90")
      Animal_win_backg=Label(Animal_win,image=intro_backgr)
      Animal_win_backg.place(x=0,y=10,relwidth=1,relheight=1)

      def back_purchase_win():
        click_sound()
        Animal_win.withdraw()
        pur_win.deiconify()
      canva_about2=Canvas(Animal_win,bg="#FFF902",height=70)
      canva_about2.pack(fill="both",side="top")
      canva_about2.create_image(340, 38, image=Logo2)
      left_arrow_back=Button(canva_about2,font=("Segoe UI Black", 8),anchor="center",image=Left_Arrow,bg="#FFF902",command=back_purchase_win)
      left_arrow_back.place(relheight=1,relwidth=1)
      canva_about2.create_window((48,35),window=left_arrow_back,width=50,height=50)
        
      Vegetables=["Tomatoes","Onions","Carrots","Cabbage","Spinach"]
      Cereals=["Rice","Maize flour","Sorghum","Pasta","Oats"]
      animal_products=["Beef","Steak","Chicken","Fish","Pork"]
      Seasonings=["Salt","Vinegar","Oil","Black pepper","Maggi","Curry powder"]
      
      animal_frame=Frame(Animal_win,width=455,height=358)
      animal_frame.pack(pady=35)

      animal_back_pic=Label(animal_frame,image=animal_backgr)
      animal_back_pic.place(x=0,y=0,relheight=1,relwidth=1)
      
      beef_fr=Frame(animal_frame,width=135,height=130,background="#005E05")#,activebackground="green",activeforeground="yellow") # type: ignore
      beef_fr.place(x=40,y=20)

      beef_label=Label(beef_fr,background="yellow",text="Tomatoes:\n6000BIF",foreground="green",font=("Times News Romans",9,"bold"))
      beef_label.pack(side="top",fill="both")
      
      beef_image=Label(beef_fr,image=beef_pic,width=128,height=85)
      beef_image.pack()

      beef_button=Button(beef_fr,image=add_to_cart,height=30,background="yellow")
      beef_button.pack(fill="both")
      
      steak_fr=Frame(animal_frame,width=135,height=130,background="#005E05")#,activebackground="green",activeforeground="yellow") # pyright: ignore[reportUndefinedVariable]
      steak_fr.place(x=250,y=20)
      
      steak_label=Label(steak_fr,background="yellow",text="Tomatoes:\n6000BIF",foreground="green",font=("Times News Romans",9,"bold"))
      steak_label.pack(side="top",fill="both")
      
      steak_image=Label(steak_fr,image=steak_pic,width=128,height=85)
      steak_image.pack()

      steak_button=Button(steak_fr,image=add_to_cart,height=30,background="yellow")
      steak_button.pack(fill="both")
      
      chicken_fr=Frame(animal_frame,width=135,height=130,background="#005E05")#,,compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      chicken_fr.place(x=40,y=190)

      chicken_label=Label(chicken_fr,background="yellow",text="Tomatoes:\n6000BIF",foreground="green",font=("Times News Romans",9,"bold"))
      chicken_label.pack(side="top",fill="both")
      
      chicken_image=Label(chicken_fr,image=chicken_pic,width=128,height=85)
      chicken_image.pack()

      chicken_button=Button(chicken_fr,image=add_to_cart,height=30,background="yellow")
      chicken_button.pack(fill="both")

      pork_fr=Frame(animal_frame,width=135,height=130,background="#005E05")#,font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      pork_fr.place(x=250,y=190)
      
      pork_label=Label(pork_fr,background="yellow",text="Tomatoes:\n6000BIF",foreground="green",font=("Times News Romans",9,"bold"))
      pork_label.pack(side="top",fill="both")
      
      pork_image=Label(pork_fr,image=pork_pic,width=128,height=85)
      pork_image.pack()

      pork_button=Button(pork_fr,image=add_to_cart,height=30,background="yellow")
      pork_button.pack(fill="both")
      
      done_btn = Button(Animal_win, text=f"DONE", bg="#FFD400", font=("Segoe UI Black", 12), fg="#2A6000", width=15,
                          relief="raised",state="disabled", borderwidth=7,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_hist)
      done_btn.place(relx=1,rely=1,anchor="se",x=-10,y=-16) 
    def veg_win():
      global R,BTN,veg_btn,an_btn,cereal_btn,season_btn,fruit_btn,drink_btn,pur_win
      click_sound()
      pur_win.withdraw()
      Veg_win=Toplevel(pur_win)
      Veg_win.geometry("710x600+450+90")
      Veg_win_backg=Label(Veg_win,image=intro_backgr)
      Veg_win_backg.place(x=0,y=10,relwidth=1,relheight=1)

      def back_purchase_win():
        click_sound()
        Veg_win.withdraw()
        pur_win.deiconify()
      canva_about2=Canvas(Veg_win,bg="#FFF902",height=70)
      canva_about2.pack(fill="both",side="top")
      canva_about2.create_image(340, 38, image=Logo2)
      left_arrow_back=Button(canva_about2,font=("Segoe UI Black", 8),anchor="center",image=Left_Arrow,bg="#FFF902",command=back_purchase_win)
      left_arrow_back.place(relheight=1,relwidth=1)
      canva_about2.create_window((48,35),window=left_arrow_back,width=50,height=50)
        
      Vegetables=["Tomatoes","Onions","Carrots","Cabbage","Spinach"]
      Cereals=["Rice","Maize flour","Sorghum","Pasta","Oats"]
      animal_products=["Beef","Steak","Chicken","Fish","Pork"]
      Seasonings=["Salt","Vinegar","Oil","Black pepper","Maggi","Curry powder"]
      
      animal_frame1=Frame(Veg_win,width=455,height=358)
      animal_frame1.pack(pady=35)

      animal_back_pic=Label(animal_frame1,image=veg_win_backg)
      animal_back_pic.place(x=0,y=0,relheight=1,relwidth=1)
      
      tomato_fr=Frame(animal_frame1,width=135,height=130,background="#005E05")#,activebackground="green",activeforeground="yellow") # type: ignore
      tomato_fr.place(x=40,y=20)
      
      tomatoes_label=Label(tomato_fr,background="yellow",text="Tomatoes:\n6000BIF",foreground="green",font=("Times News Romans",9,"bold"))
      tomatoes_label.pack(side="top",fill="both")
      
      tomatoes_image=Label(tomato_fr,image=tomatoes_pic,width=128,height=85)
      tomatoes_image.pack()

      tomatoes_button=Button(tomato_fr,image=add_to_cart,height=30,background="yellow")
      tomatoes_button.pack(fill="both")

      onion_fr=Frame(animal_frame1,width=135,height=135,background="yellow")#,activebackground="green",activeforeground="yellow") # pyright: ignore[reportUndefinedVariable]
      onion_fr.place(x=250,y=20)

      onions_label=Label(onion_fr,background="yellow",text="Onions:\n5800BIF",foreground="green",font=("Times News Romans",9,"bold"))
      onions_label.pack(side="top",fill="both")
      
      onions_image=Label(onion_fr,image=onions_pic,width=128,height=85)
      onions_image.pack()

      onions_button=Button(onion_fr,image=add_to_cart,height=30,background="yellow")
      onions_button.pack(fill="both")

      carrot_fr=Frame(animal_frame1,width=135,height=130,background="#005E05")#,,compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      carrot_fr.place(x=40,y=190)

      carrot_label=Label(carrot_fr,background="yellow",text="carrots:\n4200BIF",foreground="green",font=("Times News Romans",9,"bold"))
      carrot_label.pack(side="top",fill="both")
      
      carrot_image=Label(carrot_fr,image=carrot_pic,width=128,height=85)
      carrot_image.pack()

      carrot_button=Button(carrot_fr,image=add_to_cart,height=30,background="yellow")
      carrot_button.pack(fill="both")

      cabbage_fr=Frame(animal_frame1,width=135,height=130,background="#005E05")#,font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      cabbage_fr.place(x=250,y=190)

      cabbage_label=Label(cabbage_fr,background="yellow",text="carrots:\n6000BIF",foreground="green",font=("Times News Romans",9,"bold"))
      cabbage_label.pack(side="top",fill="both")
      
      cabbage_image=Label(cabbage_fr,image=cabbage_pic,width=128,height=85)
      cabbage_image.pack()

      cabbage_button=Button(cabbage_fr,image=add_to_cart,height=30,background="yellow")
      cabbage_button.pack(fill="both")

      
      done_btn1= Button(Veg_win, text=f"DONE", bg="#FFD400", font=("Segoe UI Black", 12), fg="#2A6000", width=15,
                          relief="raised",state="disabled", borderwidth=7,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_hist)
      done_btn1.place(relx=1,rely=1,anchor="se",x=-10,y=-16) 
    def cereal_win():
      global R,BTN,veg_btn,an_btn,cereal_btn,season_btn,fruit_btn,drink_btn,pur_win
      click_sound()
      pur_win.withdraw()
      Cer_win=Toplevel(pur_win)
      Cer_win.geometry("710x600+450+90")
      Cer_win_backg=Label(Cer_win,image=animal_backgr)
      Cer_win_backg.place(x=0,y=10,relwidth=1,relheight=1)

      def back_purchase_win():
        click_sound()
        Cer_win.withdraw()
        pur_win.deiconify()
      canva_about2=Canvas(Cer_win,bg="#FFF902",height=70)
      canva_about2.pack(fill="both",side="top")
      canva_about2.create_image(340, 38, image=Logo2)
      left_arrow_back=Button(canva_about2,font=("Segoe UI Black", 8),anchor="center",image=Left_Arrow,bg="#FFF902",command=back_purchase_win)
      left_arrow_back.place(relheight=1,relwidth=1)
      canva_about2.create_window((48,35),window=left_arrow_back,width=50,height=50)
        
      Vegetables=["Tomatoes","Onions","Carrots","Cabbage","Spinach"]
      Cereals=["Rice","Maize flour","Sorghum","Pasta","Oats"]
      animal_products=["Beef","Steak","Chicken","Fish","Pork"]
      Seasonings=["Salt","Vinegar","Oil","Black pepper","Maggi","Curry powder"]
      
      animal_frame1=Frame(Cer_win,width=455,height=350)
      animal_frame1.pack(pady=35)

      animal_back_pic=Label(animal_frame1,image=frame_animal_backgr)
      animal_back_pic.place(x=0,y=0,relheight=1,relwidth=1)
      
      Rice_fr=Frame(animal_frame1,width=145,height=130,background="#025E56")#,activebackground="green",activeforeground="yellow") # type: ignore
      Rice_fr.place(x=40,y=20)
      
      Maize_fr=Frame(animal_frame1,width=145,height=130,background="#005E05")#,activebackground="green",activeforeground="yellow") # pyright: ignore[reportUndefinedVariable]
      Maize_fr.place(x=250,y=20)
      
      avoine_fr=Frame(animal_frame1,width=145,height=130,background="#5E4D00")#,,compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      avoine_fr.place(x=40,y=190)

      sorgho_fr=Frame(animal_frame1,width=145,height=130,background="#19005E")#,font=("Impact",13),compound="top",activebackground="green",activeforeground="yellow") # type: ignore
      sorgho_fr.place(x=250,y=190)
      
      done_btn1= Button(Cer_win, text=f"DONE", bg="#FFD400", font=("Segoe UI Black", 12), fg="#2A6000", width=15,
                          relief="raised",state="disabled", borderwidth=7,activeforeground="#FFD400",activebackground="#2A6000",command=toggle_hist)
      done_btn1.place(relx=1,rely=1,anchor="se",x=-10,y=-16) 
    main_frame_im=Label(main_frame,image=main_frame_back)
    main_frame_im.place(x=0,y=0,relwidth=1,relheight=1)
    main_frame_lab=Label(main_frame,text=slogan,font=("Impact",10),borderwidth=9,width=65,bg="#FFD400",fg="#005E05")
    main_frame_lab.place(y=100,relx=0.5,rely=0.5,anchor="center")

    purchase=Button(main_frame,text=f"PURCHASE",font=("Segoe Print",15,"bold"),relief="raised",borderwidth=4,bg="#FF0800",fg="#FFD400",width=15,activebackground="#FF4F14",activeforeground="#FFD400",command=test_purchase_win)
    purchase.place(relx=0.5,rely=0.5,anchor="center")

win.after(3000,intro_win)

win.mainloop()
