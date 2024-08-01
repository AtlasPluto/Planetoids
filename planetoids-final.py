import tkinter as t, random as r, time as ti
from playsound import playsound
from tkinter import *
c = Tk()
c.title("PLANETOIDS")
c = Canvas(c,width=1920,height=1080,bg="black")
c.pack()

#Dôležité!!!!! -- ako správne spustiť projekt!
#
#   1. - png a wav  -  kvôli tomu že je potreba mať ich stiahnuté na pc (sú stym nejaké problémy) - je treba sy spraviť na ploche folder , v ktorom budú files uložené
#   súbor sa musí volať --   png-wav   , pokial sa tak volat nebude program fungovať  (nebude vedieť vyvolať obrázky a zvuky)
#   pre istotu si aj code dajte na plchu a v vscode si otvorte folder - pracovná plocha ,malo by to fungovat aj v idle ale radšej odstránte c.mainloop() a bude to trocha pomalšie
#   je možne že code bude niekedy trocha pomalší - pythhon nie vzdy stíha - hlavne pri pohybe ked zostrelíte asteroid tak trva kým sa vymaže ale pridali sme premenú ktorá zabráni pohybu po kolizii aby sme predočli buggom plus uz to ide trochu rýchlejšie
#   ked hrá konečná hudba vypnite hru až dohraje lebo ked ju preručite spadne code
#   niekedy sa môže stať že je python pretažený - vyhodí chybu xs not identified - nie je bug(dufam) ale len pretaženie pythonu


##Premenné
x = 940
y = 890
xs=500
ys=780
ys1 = 650
ys2 = 650
ys3 = 650
ys4 = 650
ys5 = 650
ys6 = 650
ys7 = 650
ys8 = 650
ys9 = 650
ys10 = 650
s = 0
control_variable1 = 0
control_variable2 = 0
control_variable3 = 0
control_variable4 = 0
control_variable5 = 0
asteroids_destroyed = 0
score = 0
shot_counter = 0
difficuilty = 0
ButtonSEStatus = "on"
EndGameMusicStatus = "on"
a1_d = 0
a2_d = 0
a3_d = 0
a4_d = 0
a5_d = 0
a6_d = 0
a7_d = 0
a8_d = 0
a9_d = 0
a10_d = 0


##Vlozenie obrazkov do hry
r_ast_m = PhotoImage(file = "png-wav/as-r-100x50.png")  # r_ast_m - cervený asteroid malý
r_ast_v = PhotoImage(file = "png-wav/as-r-100x100.png") # r_ast_v - cervený asteroid velký
w_ast_m = PhotoImage(file = "png-wav/as-w-100x50.png")  # w_ast_m - biely asteroid malý
w_ast_v = PhotoImage(file = "png-wav/as-w-100x100.png") # w_ast_v - biely asteroid velký
g_ast_m = PhotoImage(file = "png-wav/as-g-100x50.png")  # g_ast_m - zlatý asteroid malý
g_ast_v = PhotoImage(file = "png-wav/as-g-100x100.png") # g_ast_v - zlatý asteroid velký
space_ship = PhotoImage(file = "png-wav/space-s.png")   # space-s - space ship
missile = PhotoImage(file="png-wav/raketka_.png")       # missile - zobrazuje rakety



def GameModeMenu():
    global difficuilty,shot_counter
    shot_counter = 0
    difficuilty = 0

    c.delete("all")

    textSelectPlayMode = c.create_text(x,y-690,text="SELECT PLAY MODE",fill="white",font="Times 20 bold",tag="PlayButton")

    BackButton = c.create_rectangle(x-45,y,x+45,y+40,outline="white",tag="BackButton")
    textBackButton = c.create_text(x,y+20,text="BACK",fill="white",font="Times 20 bold",tag="BackButton")

    EasyGameModeButton = c.create_rectangle(x-45,y-610,x+45,y-570,outline="white",tag="EasyGameModeButton")
    textEasyGameModeButton = c.create_text(x,y-590,text="EASY",fill="white",font="Times 20 bold",tag="EasyGameModeButton")
    
    MediumGameModeButton = c.create_rectangle(x-65,y-510,x+65,y-470,outline="white",tag="MediumGameModeButton")
    textMediumGameModeButton = c.create_text(x,y-490,text="MEDIUM",fill="white",font="Times 20 bold",tag="MediumGameModeButton")
    
    HardGameModeButton = c.create_rectangle(x-45,y-410,x+45,y-370,outline="white",tag="HardGameModeButton")
    textHardGameModeButton = c.create_text(x,y-390,text="HARD",fill="white",font="Times 20 bold",tag="HardGameModeButton")
    
    def click(event):   
        global x,y,kx,ky,difficuilty
        kx, ky = event.x, event.y
        
        if x-45 <= kx <= x+45 and y <= ky <= y+40:
            if ButtonSEStatus == "on":
                sound_effect1()
            MainMenu()
        elif x-45 <= kx <= x+45 and y-610 <= ky <= y-570:
            difficuilty = "easy"
            if ButtonSEStatus == "on":
                sound_effect1()
            planetoids_start() 
        elif x-65 <= kx <= x+65 and y-510 <= ky <= y-470:
            difficuilty = "medium"
            if ButtonSEStatus == "on":
                sound_effect1()
            planetoids_start()
        elif x-45 <= kx <= x+45 and y-410 <= ky <= y-370:
            difficuilty = "hard"
            if ButtonSEStatus == "on":
                sound_effect1()
            planetoids_start()
        
    c.bind("<Button-1>",click)



def MainMenu():

    global x,y

    c.delete("all")

    textTitle = c.create_text(x,y-690,text="PLANETOIDS",fill="white",font="Times 20 bold",tag="Title")

    ExitButton = c.create_rectangle(x-40,y,x+40,y+40,outline="white",tag="ExitButton")
    textEexitButton = c.create_text(x,y+20,text="EXIT",fill="white",font="Times 20 bold",tag="ExitButton")

    SettingsButton = c.create_rectangle(x-80,y-200,x+80,y-160,outline="white",tag="SettingsButton")
    textSettingsButton = c.create_text(x,y-180,text="SETTINGS",fill="white",font="Times 20 bold",tag="SettingsButton")

    CreditsButton = c.create_rectangle(x-70,y-100,x+70,y-60,outline="white",tag="CreditsButton")
    textCreditsButton = c.create_text(x,y-80,text="CREDITS",fill="white",font="Times 20 bold",tag="CreditsButton")

    PlayButton = c.create_rectangle(x-45,y-300,x+45,y-260,outline="white",tag="PlayButton")
    textPlayButton = c.create_text(x,y-280,text="PLAY",fill="white",font="Times 20 bold",tag="PlayButton")
    
    def click(event):
        global x,y,kx,ky
        kx, ky = event.x, event.y
        if x-40 <= kx <= x+40 and y <= ky <= y+40:
            if ButtonSEStatus == "on":
                sound_effect1()
            quit()
        elif x-80 <= kx <= x+80 and y-200 <= ky <= y-160:  
            if ButtonSEStatus == "on":
                sound_effect1()
            SettingsMenu()
        elif x-70 <= kx <= x+70 and y-100 <= ky <= y-60:
            if ButtonSEStatus == "on":
                sound_effect1()
            Credits()
        elif x-45 <= kx <= x+45 and y-300 <= ky <= y-260:
            if ButtonSEStatus == "on":
                sound_effect1()
            GameModeMenu()
        return

    
    c.bind("<Button-1>",click)



def Credits():

    c.delete("all")

    BackButton = c.create_rectangle(x-45,y,x+45,y+40,outline="white",tag="BackButton")
    textBackButton = c.create_text(x,y+20,text="BACK",fill="white",font="Times 20 bold",tag="BackButton")

    textMeno1 = c.create_text(x,y-300,text="Lukáš - ",fill="white",font="Times 20 bold")
    textMeno2 = c.create_text(x,y-400,text="Alex - ",fill="white",font="Times 20 bold")
    textMeno3 = c.create_text(x,y-200,text="Bruno - ",fill="white",font="Times 20 bold")

    def click(event):   
        global x,y,kx,ky
        kx, ky = event.x, event.y
        if x-45 <= kx <= x+45 and y <= ky <= y+40:
            if ButtonSEStatus == "on":
                sound_effect1()
            MainMenu()

    c.bind("<Button-1>",click)



def SettingsMenu():

    c.delete("all")

    BackButton = c.create_rectangle(x-45,y,x+45,y+40,outline="white",tag="BackButton")
    textBackButton = c.create_text(x,y+20,text="BACK",fill="white",font="Times 20 bold",tag="BackButton")

    SettingsBorder = c.create_rectangle(400,390,1520,690,outline="white")

    AudioButton = c.create_rectangle(715,400,865,440,outline="white")
    textAudioButton = c.create_text(790,420,text="AUDIO",font="times 30 bold",fill="white")

    ControlsButton = c.create_rectangle(1060,400,1300,440,outline="white")
    textControlsButton = c.create_text(1180,420,text="CONTROLS",fill="white",font="times 30 bold")

    def click(event):
        global x,y,kx,ky
        kx, ky = event.x, event.y
        if x-45 <= kx <= x+45 and y <= ky <= y+40:
            if ButtonSEStatus == "on":
                sound_effect1()
            MainMenu()
        elif 715 <= kx <= 865 and 400 <= ky <= 440:
            if ButtonSEStatus == "on":
                sound_effect1()
            AudioSettings()
        elif 1060 <= kx <= 1300 and 400 <= ky <= 440:
            if ButtonSEStatus == "on":
                sound_effect1()
            Controls()
        
    c.bind("<Button-1>",click)



def Controls():

    c.delete("all")

    BackButton = c.create_rectangle(x-45,y,x+45,y+40,outline="white",tag="BackButton")
    textBackButton = c.create_text(x,y+20,text="BACK",fill="white",font="Times 20 bold",tag="BackButton")

    SettingsBorder = c.create_rectangle(400,390,1520,690,outline="white")

    AudioButton = c.create_rectangle(715,400,865,440,outline="white")
    textAudioButton = c.create_text(790,420,text="AUDIO",font="times 30 bold",fill="white")

    ControlsButton = c.create_rectangle(1060,400,1300,440,outline="white",fill="grey")
    textControlsButton = c.create_text(1180,420,text="CONTROLS",fill="white",font="times 30 bold")

    textControls = c.create_text(940,540,text="Move left         :         A\nMove right      :         D\nShoot               :         LMB",fill="white",font="Times 20 bold")

    def click(event):
        global x,y,kx,ky
        kx, ky = event.x, event.y
        if x-45 <= kx <= x+45 and y <= ky <= y+40:
            if ButtonSEStatus == "on":
                sound_effect1()
            MainMenu()
        elif 715 <= kx <= 865 and 400 <= ky <= 440:
            if ButtonSEStatus == "on":
                sound_effect1()
            AudioSettings()

    c.bind("<Button-1>",click)



def AudioSettings():

    c.delete("all")

    BackBbutton = c.create_rectangle(x-45,y,x+45,y+40,outline="white",tag="BackButton")
    textBackButton = c.create_text(x,y+20,text="BACK",fill="white",font="Times 20 bold",tag="BackButton")

    SwttingsBorder = c.create_rectangle(400,390,1520,690,outline="white")

    AudioButton = c.create_rectangle(715,400,865,440,outline="white",fill="grey")
    textAudioButton = c.create_text(790,420,text="AUDIO",font="times 30 bold",fill="white")

    SoundEffectButton = c.create_rectangle(1060,460,1080,480,outline="white")
    textSoundEffectButton = c.create_text(800,470,text="Button Sound Effects",font="times 20 bold",fill="white")

    EndGameSEButton = c.create_rectangle(1060,510,1080,530,outline="white")
    textEndGameSEButton = c.create_text(800,520,text="End Game Music",font="times 20 bold",fill="white")

    ControlsButton = c.create_rectangle(1060,400,1300,440,outline="white")
    textControlsButton = c.create_text(1180,420,text="CONTROLS",fill="white",font="times 30 bold")

    if ButtonSEStatus == "on":
        SoundEffectsCheck1 = c.create_rectangle(1065,465,1075,475,fill="white",tag="SoundEffectCheck1")
    if EndGameMusicStatus == "on":
        SoundEffectsCheck2 = c.create_rectangle(1065,515,1075,525,fill="white",tag="SoundEffectCheck2")

    def click(event):
        global x,y,kx,ky,control_variable2,ButtonSEStatus,EndGameMusicStatus,control_variable1
        kx,ky = event.x, event.y
        if x-45 <= kx <= x+45 and y <= ky <= y+40:
            if ButtonSEStatus == "on":
                sound_effect1()
            MainMenu()
        elif 1065 <= kx <= 1075 and 460 <= ky <= 480:
            if control_variable2 == 0:
                c.delete("SoundEffectCheck1")
                ButtonSEStatus = "off"
                control_variable2 = 1
            elif control_variable2 == 1:
                SoundEffectsCheck1 = c.create_rectangle(1065,465,1075,475,fill="white",tag="SoundEffectCheck1")
                control_variable2 = 0
                ButtonSEStatus = "on"
        elif 1065 <= kx <= 1075 and 510 <= ky <= 530:
            if control_variable1 == 0:
                c.delete("SoundEffectCheck2")
                EndGameMusicStatus = "off"
                control_variable1 = 1
            elif control_variable1 == 1:
                SoundEffectsCheck2 = c.create_rectangle(1065,515,1075,525,fill="white",tag="SoundEffectCheck2")
                EndGameMusicStatus = "on"
                control_variable1 = 0
        elif 1060 <= kx <= 1300 and 400 <= ky <= 440:
            if ButtonSEStatus == "on":
                sound_effect1()
            Controls()
        
    c.bind("<Button-1>",click)



def planetoids_start():
    global b

    c.delete("all")
    StartButton = c.create_rectangle(400,150,1520,930,outline="white",tag="sb")
    textStartButton = c.create_text(960,540,text="START",fill="white",tag="sb",font= "times 250 bold")
    b  = 0
    
    def click(event):   
        global x,y,kx,ky,b
        kx, ky = event.x, event.y
        if 400 <= kx <= 1520 and 150 <= ky <= 930 and b == 0:
            if ButtonSEStatus == "on":
                sound_effect1()
            b += 1
            c.delete("sb")
            c.update()
            c.create_rectangle(400,200,1520,880,outline="white")

            c.after(1)
            c.update()

            trojka = c.create_text(960,540,text="3",fill="red", font= "times 250 bold")
            c.update()
            c.after(1000)
            c.delete(trojka)

            dvojka = c.create_text(960,540,text="2",fill="yellow", font= "times 250 bold") 
            c.update()
            c.after(1000)
            c.delete(dvojka)

            jednotka = c.create_text(960,540,text="1",fill="green", font= "times 250 bold")
            c.update()
            c.after(1000)
            c.delete(jednotka)
            if difficuilty == "easy":
                print("\nGame mode is on easy difficulty")
                game()
            elif difficuilty == "medium":
                print("\nGame mode is on medium difficulty")
                game()
            elif difficuilty == "hard":
                print("\ngame mode is on hard difficulty")
                game()
        elif 400 <= kx <= 1520 and 150 <= ky <= 930 and b != 0:
            print("\nCountdown sequence  already started!")

    c.bind("<Button-1>",click)



def victory():
    global control_variable5, elapsed_time, sft, start_time
    if control_variable5 == 0:
        control_variable5 += 1
        c.delete("all")
        c.create_text(960,540,text="VICTORY",font="times 40 bold",fill="green")
        rEB = c.create_rectangle(x-40,y,x+40,y+40,outline="white",tag="ExitButton")
        tEB = c.create_text(x,y+20,text="EXIT",fill="white",font="Times 20 bold",tag="ExitButton")
        if elapsed_time <= 4.0:
            sft = 50
        elif elapsed_time > 4.0 and elapsed_time <= 5.0:
            sft = 40
        elif elapsed_time > 5.0 and elapsed_time <= 7.5:
            sft = 30
        elif elapsed_time > 7.5 and elapsed_time <= 8.5:
            sft = 20
        else:
            sft = 0
        whole_score1 = score + sft
        whole_score2 = f"SCORE: {int(whole_score1)}"
        c.create_text(960,640,fill="white",text=whole_score2,font="times 25 bold")
        c.update()
        if EndGameMusicStatus == "on":
            music1()
        def click(event):
            global ky,kx,x,y
            kx, ky = event.x, event.y
            if x-45 <= kx <= x+45 and y <= ky <= y+40:
                if ButtonSEStatus == "on":
                    sound_effect1()
                quit()
        c.bind("<Button-1>",click)



def defeat():
    global control_variable4, control_variable5
    if control_variable5 == 0:
        control_variable5 += 1
        if control_variable4 == 0:
            control_variable4 += 1
            c.delete("all")
            c.create_rectangle(260,150,1650,460,outline="red",tag="koniec_1")
            c.create_text(960,300,text="_DEFEAT_",fill="red",font= "times 170 bold",tag="koniec_1")
            c.create_text(960,650,text="XD",fill="red",font="times 300 bold",tag="koniec_1")
            rEB = c.create_rectangle(x-40,y,x+40,y+40,outline="red",tag="ExitButton")
            tEB = c.create_text(x,y+20,text="EXIT",fill="red",font="Times 20 bold",tag="ExitButton")
            c.update()
            if EndGameMusicStatus == "on":
                music2()

        def click(event):
            global ky,kx,x,y
            kx, ky = event.x, event.y
            if x-45 <= kx <= x+45 and y <= ky <= y+40:
                if ButtonSEStatus == "on":
                    sound_effect1()
                quit()
        c.bind("<Button-1>",click)


##Vlozenie zvukov do hry
def music1():
    playsound("png-wav/8-Bit-Rick-Roll-2.WAV")

def music2():
    playsound("png-wav/8-bit-Coffin-Dance-from-Astronomia-2.WAV")

def music3():
    playsound("png-wav/8-bit-Gangnam-Style-M_V-2.WAV")

def sound_effect1():
    playsound("png-wav/Button-sound-1.wav")



def game():
    global start_time,ammo,defeat,asteroids_destroyed
    ammo = 10

    start_time = ti.time()

    #vytvorenie hry
    def ship_spawn():
        c.create_rectangle(xs,ys,xs+100,ys+50,outline="",width=0,tag="ship")
        cship = c.create_image(xs,ys,anchor=NW,image=space_ship,tag="ship")

    ##vytvorenie hranice, ak za nu padne asteroid prehral si
    def border_spawn():
        c.create_rectangle(400,840,1520,880,outline="white")

    ##pohyb do lava
    def ship_left(event):
        global xs
        if xs == 410:
            c.move("ship",0,0)
        else:
            c.move("ship",-10,0)
            xs -= 10
            c.update()
            c.after(5)

    ##pohyb do prava
    def ship_right(event):
        global xs
        if xs+100 == 1510:
            c.move("ship",0,0)
        else:
            c.move("ship",10,0)
            xs += 10
            c.update()
            c.after(5)
    
    ##stopky, ktore sa zobrazuju pocas hry v pravom hornom rohu
    def update_timer():
        global start_time, control_variable5, elapsed_time
        if control_variable5 == 0:
            elapsed_time = ti.time() - start_time  
            minutes, seconds = divmod(elapsed_time, 60)  
            timer_text = f"TIME: {int(minutes):02d}:{int(seconds):02d}"  
            c.delete("timer")  
            c.create_text(115, 200, text=timer_text,fill="white", font="times 20 bold", tag="timer")
            c.update()
            if asteroids_destroyed < 10:
                c.after(998,update_timer)
    
    ##zobrazenie aktualneho poctu nabojov
    def update_ammo():
        global score
        c.itemconfigure("score", text="SCORE: " + str(score))
        if ammo == 0 and control_variable5 == 0:
            print("out of ammo")
        if control_variable5 == 0:
            c.delete("ammo_update")
            ammo_text = f"AMMO: {int(ammo)}"
            c.create_text(120,300,text=ammo_text,fill="white",tag="ammo_update",font="times 20 bold")
            print("ammo:",ammo)

    ##kontroluje ci boli vsetky asteroidy znicene, ak ano spusti funkciu vyhry
    def score_check():
        global score,control_variable3,control_variable5
        if asteroids_destroyed == 10:
            if control_variable3 == 0:
                control_variable3 += 1
                victory()
        else:
            c.after(100,score_check)
        return

    ##vytvorenie asteroidov, su 2 velkosti a 3 druhy:sivy = 5 bodov, cerveny = 0 bodov, zlaty = 10 bodov
    def planetoids_spawn_easy():
        global  a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
        global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
        global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
        global sa1,sa2,sa3,sa4,sa5,sa6,sa7,sa8,sa9,sa10
        global ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9,ta10
        global ca1,ca2,ca3,ca4,ca5,ca6,ca7,ca8,ca9,ca10
        global a1_d,a2_d,a3_d,a4_d,a5_d,a6_d,a7_d,a8_d,a9_d,a10_d

        x1=r.randint(401,502)
        y1=r.randint(200,250)
        ta1 = r.randint(1,2)
        d1 = r.randint(1,100)
        x2=r.randint(502,604)
        y2=r.randint(200,250)
        ta2 = r.randint(1,2)
        d2= r.randint(1,100)
        x3=r.randint(604,706)
        y3=r.randint(200,250)
        ta3 = r.randint(1,2)
        d3 = r.randint(1,100)
        x4=r.randint(706,808)
        y4=r.randint(200,250)
        ta4 = r.randint(1,2)
        d4 = r.randint(0,100)
        x5=r.randint(808,910)
        y5=r.randint(200,250)
        ta5 = r.randint(1,2)
        d5 = r.randint(1,100)
        x6=r.randint(910,1012)
        y6=r.randint(200,250)
        ta6 = r.randint(1,2)
        d6= r.randint(1,100)
        x7=r.randint(1012,1114)
        y7=r.randint(200,250)
        ta7 = r.randint(1,2)
        d7 = r.randint(1,100)
        x8=r.randint(1114,1216)
        y8=r.randint(200,250)
        ta8 = r.randint(1,2)
        d8 = r.randint(1,100)
        x9=r.randint(1216,1318)
        y9=r.randint(200,250)
        ta9 = r.randint(1,2)
        d9 = r.randint(1,100)
        x10=r.randint(1318,1420)
        y10=r.randint(200,250)
        ta10 = r.randint(1,2)
        d10 = r.randint(1,100)
  
##       1.asteroid
    
        if ta1 == 1 and d1 <= 60:
            a1=c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="grey")
            ca1 = c.create_image(x1,y1,anchor=NW,image = w_ast_m,tag="grey")
            sa1 = 5
            ac1 = "w"
        elif ta1 == 2 and d1 <= 60:  
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="grey")
            ca1 = c.create_image(x1,y1,anchor=NW,image = w_ast_v,tag="grey")
            sa1 = 5
            ac1 = "w"
        elif ta1 == 2 and d1 <=90 and d1 >= 61:
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="red")
            ca1 = c.create_image(x1,y1,anchor=NW,image = r_ast_v,tag="red")
            sa1 = 0
            ac1 = "r"
        elif ta1 == 1 and d1 <=90 and d1 >= 61:
            a1= c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="red")
            ca1 = c.create_image(x1,y1,anchor=NW,image = r_ast_m,tag="red")
            sa1 = 0
            ac1 = "r"
        elif ta1 == 2 and d1 >= 91: 
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="gold")
            ca1 = c.create_image(x1,y1,anchor=NW,image = g_ast_v,tag="gold")
            sa1 = 10
            ac1 = "g"
        elif ta1 == 1 and d1 >= 91:
            a1=c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="gold")
            ca1 = c.create_image(x1,y1,anchor=NW,image = g_ast_m,tag="gold")
            sa1 = 10
            ac1 = "g"

##       2. asteroid

        if ta2 == 1 and d2 <= 60:
            a2=c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="grey")
            ca2 = c.create_image(x2,y2,anchor=NW,image = w_ast_m,tag="grey")
            sa2 = 5
            ac2 = "w"
        elif ta2 == 2 and d2 <= 60:  
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="grey")
            ca2 = c.create_image(x2,y2,anchor=NW,image = w_ast_v,tag="grey")
            sa2 = 5
            ac2 = "w"
        elif ta2 == 2 and d2 <=90 and d2 >= 61:
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="red")
            ca2 = c.create_image(x2,y2,anchor=NW,image = r_ast_v,tag="red")
            sa2 = 0
            ac2 = "r"
        elif ta2 == 1 and d2 <=90 and d2 >= 61:
            a2= c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="red")
            ca2 = c.create_image(x2,y2,anchor=NW,image = r_ast_m,tag="red")
            sa2 = 0
            ac2 = "r"
        elif ta2 == 2 and d2 >= 91: 
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="gold")
            ca2 = c.create_image(x2,y2,anchor=NW,image = g_ast_v,tag="gold")
            sa2 = 10
            ac2 = "g"
        elif ta2 == 1 and d2 >= 91:
            a2=c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="gold")
            ca2 = c.create_image(x2,y2,anchor=NW,image = g_ast_m,tag="gold")
            sa2 = 10
            ac2 = "g"

##       3. asteroid

        if ta3 == 1 and d3 <= 60:
            a3=c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="grey")
            ca3 = c.create_image(x3,y3,anchor=NW,image = w_ast_m,tag="grey")
            sa3 = 5
            ac3 = "w"
        elif ta3 == 2 and d3 <= 60:  
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="grey")
            ca3 = c.create_image(x3,y3,anchor=NW,image = w_ast_v,tag="grey")
            sa3 = 5
            ac3 = "w"
        elif ta3 == 2 and d3 <=90 and d3 >= 61:
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="red")
            ca3 = c.create_image(x3,y3,anchor=NW,image = r_ast_v,tag="red")
            sa3 = 0
            ac3 = "r"
        elif ta3 == 1 and d3 <=90 and d3 >= 61:
            a3= c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="red")
            ca3 = c.create_image(x3,y3,anchor=NW,image = r_ast_m,tag="red")
            sa3 = 0
            ac3 = "r"
        elif ta3 == 2 and d3 >= 91: 
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="gold")
            ca3 = c.create_image(x3,y3,anchor=NW,image = g_ast_v,tag="gold")
            sa3 = 10
            ac3 = "g"
        elif ta3 == 1 and d3 >= 91:
            a3=c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="gold")
            ca3 = c.create_image(x3,y3,anchor=NW,image = g_ast_m,tag="gold")
            sa3 = 10
            ac3 = "g"
                                                                                                                                                               
##       4. asteroid

        if ta4 == 1 and d4 <= 60:
            a4=c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="grey")
            ca4 = c.create_image(x4,y4,anchor=NW,image = w_ast_m,tag="grey")
            sa4 = 5
            ac4 = "w"
        elif ta4 == 2 and d4 <= 60:  
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="grey")
            ca4 = c.create_image(x4,y4,anchor=NW,image = w_ast_v,tag="grey")
            sa4 = 5
            ac4 = "w"
        elif ta4 == 2 and d4 <=90 and d4 >= 61:
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="red")
            ca4 = c.create_image(x4,y4,anchor=NW,image = r_ast_v,tag="red")
            sa4 = 0
            ac4 = "r"
        elif ta4 == 1 and d4 <=90 and d4 >= 61:
            a4= c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="red")
            ca4 = c.create_image(x4,y4,anchor=NW,image = r_ast_m,tag="red")
            sa4 = 0
            ac4 = "r"
        elif ta4 == 2 and d4 >= 91: 
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="gold")
            ca4 = c.create_image(x4,y4,anchor=NW,image = g_ast_v,tag="gold")
            sa4 = 10
            ac4 = "g"
        elif ta4 == 1 and d4 >= 91:
            a4=c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="gold")
            ca4 = c.create_image(x4,y4,anchor=NW,image = g_ast_m,tag="gold")
            sa4 = 10
            ac4 = "g"

##       5. asteroid

        if ta5 == 1 and d5 <= 60:
            a5=c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="grey")
            ca5 = c.create_image(x5,y5,anchor=NW,image = w_ast_m,tag="grey")
            sa5 = 5
            ac5 = "w"
        elif ta5 == 2 and d5 <= 60:  
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="grey")
            ca5 = c.create_image(x5,y5,anchor=NW,image = w_ast_v,tag="grey")
            sa5 = 5
            ac5 = "w"
        elif ta5 == 2 and d5 <=90 and d5 >= 61:
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="red")
            ca5 = c.create_image(x5,y5,anchor=NW,image = r_ast_v,tag="red")
            sa5 = 0
            ac5 = "r"
        elif ta5 == 1 and d5 <=90 and d5 >= 61:
            a5= c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="red")
            ca5 = c.create_image(x5,y5,anchor=NW,image = r_ast_m,tag="red")
            sa5 = 0
            ac5 = "r"
        elif ta5 == 2 and d5 >= 91: 
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="gold")
            ca5 = c.create_image(x5,y5,anchor=NW,image = g_ast_v,tag="gold")
            sa5 = 10
            ac5 = "g"
        elif ta5 == 1 and d5 >= 91:
            a5=c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="gold")
            ca5 = c.create_image(x5,y5,anchor=NW,image = g_ast_m,tag="gold")
            sa5 = 10
            ac5 = "g"

##       6. asteroid

        if ta6 == 1 and d6 <= 60:
            a6=c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="grey")
            ca6 = c.create_image(x6,y6,anchor=NW,image = w_ast_m,tag="grey")
            sa6 = 5
            ac6 = "w"
        elif ta6 == 2 and d6 <= 60:  
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="grey")
            ca6 = c.create_image(x6,y6,anchor=NW,image = w_ast_v,tag="grey")
            sa6 = 5
            ac6 = "w"
        elif ta6 == 2 and d6 <=90 and d6 >= 61:
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="red")
            ca6 = c.create_image(x6,y6,anchor=NW,image = r_ast_v,tag="red")
            sa6 = 0
            ac6 = "r"
        elif ta6 == 1 and d6 <=90 and d6 >= 61:
            a6= c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="red")
            ca6 = c.create_image(x6,y6,anchor=NW,image = r_ast_m,tag="red")
            sa6 = 0
            ac6 = "r"
        elif ta6 == 2 and d6 >= 91: 
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="gold")
            ca6 = c.create_image(x6,y6,anchor=NW,image = g_ast_v,tag="gold")
            sa6 = 10
            ac6 = "g"
        elif ta6 == 1 and d6 >= 91:
            a6=c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="gold")
            ca6 = c.create_image(x6,y6,anchor=NW,image = g_ast_m,tag="gold")
            sa6 = 10
            ac6 = "g"

##       7. asteroid

        if ta7 == 1 and d7 <= 60:
            a7=c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="grey")
            ca7 = c.create_image(x7,y7,anchor=NW,image = w_ast_m,tag="grey")
            sa7 = 5
            ac7 = "w"
        elif ta7 == 2 and d7 <= 60:  
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="grey")
            ca7 = c.create_image(x7,y7,anchor=NW,image = w_ast_v,tag="grey")
            sa7 = 5
            ac7 = "w"
        elif ta7 == 2 and d7 <=90 and d7 >= 61:
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="red")
            ca7 = c.create_image(x7,y7,anchor=NW,image = r_ast_v,tag="red")
            sa7 = 0
            ac7 = "r"
        elif ta7 == 1 and d7 <=90 and d7 >= 61:
            a7= c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="red")
            ca7 = c.create_image(x7,y7,anchor=NW,image = r_ast_m,tag="red")
            sa7 = 0
            ac7 = "r"
        elif ta7 == 2 and d7 >= 91: 
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="gold")
            ca7 = c.create_image(x7,y7,anchor=NW,image = g_ast_v,tag="gold")
            sa7 = 10
            ac7 = "g"
        elif ta7 == 1 and d7 >= 91:
            a7=c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="gold")
            ca7 = c.create_image(x7,y7,anchor=NW,image = g_ast_m,tag="gold")
            sa7 = 10
            ac7 = "g"

##       8. asteroid

        if ta8 == 1 and d8 <= 60:
            a8=c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="grey")
            ca8 = c.create_image(x8,y8,anchor=NW,image = w_ast_m,tag="grey")
            sa8 = 5
            ac8 = "w"
        elif ta8 == 2 and d8 <= 60:  
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="grey")
            ca8 = c.create_image(x8,y8,anchor=NW,image = w_ast_v,tag="grey")
            sa8 = 5
            ac8 = "w"
        elif ta8 == 2 and d8 <=90 and d8 >= 61:
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="red")
            ca8 = c.create_image(x8,y8,anchor=NW,image = r_ast_v,tag="red")
            sa8 = 0
            ac8 = "r"
        elif ta8 == 1 and d8 <=90 and d8 >= 61:
            a8= c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="red")
            ca8 = c.create_image(x8,y8,anchor=NW,image = r_ast_m,tag="red")
            sa8 = 0
            ac8 = "r"
        elif ta8 == 2 and d8 >= 91: 
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="gold")
            ca8 = c.create_image(x8,y8,anchor=NW,image = g_ast_v,tag="gold")
            sa8 = 10
            ac8 = "g"
        elif ta8 == 1 and d8 >= 91:
            a8=c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="gold")
            ca8 = c.create_image(x8,y8,anchor=NW,image = g_ast_m,tag="gold")
            sa8 = 10
            ac8 = "g"

##       9. asteroid

        if ta9 == 1 and d9 <= 60:
            a9=c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="grey")
            ca9 = c.create_image(x9,y9,anchor=NW,image = w_ast_m,tag="grey")
            sa9 = 5
            ac9 = "w"
        elif ta9 == 2 and d9 <= 60:  
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="grey")
            ca9 = c.create_image(x9,y9,anchor=NW,image = w_ast_v,tag="grey")
            sa9 = 5
            ac9 = "w"
        elif ta9 == 2 and d9 <=90 and d9 >= 61:
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="red")
            ca9 = c.create_image(x9,y9,anchor=NW,image = r_ast_v,tag="red")
            sa9 = 0
            ac9 = "r"
        elif ta9 == 1 and d9 <=90 and d9 >= 61:
            a9= c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="red")
            ca9 = c.create_image(x9,y9,anchor=NW,image = r_ast_m,tag="red")
            sa9 = 0
            ac9 = "r"
        elif ta9 == 2 and d9 >= 91: 
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="gold")
            ca9 = c.create_image(x9,y9,anchor=NW,image = g_ast_v,tag="gold")
            sa9 = 10
            ac9 = "g"
        elif ta9 == 1 and d9 >= 91:
            a9=c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="gold")
            ca9 = c.create_image(x9,y9,anchor=NW,image = g_ast_m,tag="gold")
            sa9 = 10
            ac9 = "g"

##       10. asteroid

        if ta10 == 1 and d10 <= 60:
            a10=c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="grey")
            ca10 = c.create_image(x10,y10,anchor=NW,image = w_ast_m,tag="grey")
            sa10 = 5
            ac10 = "w"
        elif ta10 == 2 and d10 <= 60:  
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="grey")
            ca10 = c.create_image(x10,y10,anchor=NW,image = w_ast_v,tag="grey")
            sa10 = 5
            ac10 = "w"
        elif ta10 == 2 and d10 <=90 and d10 >= 61:
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="red")
            ca10 = c.create_image(x10,y10,anchor=NW,image = r_ast_v,tag="red")
            sa10 = 0
            ac10 = "r"
        elif ta10 == 1 and d10 <=90 and d10 >= 61:
            a10= c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="red")
            ca10 = c.create_image(x10,y10,anchor=NW,image = r_ast_m,tag="red")
            sa10 = 0
            ac10 = "r"
        elif ta10 == 2 and d10 >= 91: 
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="gold")
            ca10 = c.create_image(x10,y10,anchor=NW,image = g_ast_v,tag="gold")
            sa10 = 10
            ac10 = "g"
        elif ta10 == 1 and d10 >= 91:
            a10=c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="gold")
            ca10 = c.create_image(x10,y10,anchor=NW,image = g_ast_m,tag="gold")
            sa10 = 10
            ac10 = "g"

    ##pohyb asteroidov
    def loopinmovement_easy():
        global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
        global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
        global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
        global ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9,ta10
        global ca1,ca2,ca3,ca4,ca5,ca6,ca7,ca8,ca9,ca10
  
#velkost pohybu horizontalne(y) 
        
        y1m=r.randint(-1,3)
        x1m=r.randint(-1,1)
        y2m=r.randint(-1,3)
        x2m=r.randint(-1,1)
        y3m=r.randint(-1,3)
        x3m=r.randint(-1,1)
        y4m=r.randint(-1,3)
        x4m=r.randint(-1,1)
        y5m=r.randint(-1,3)
        x5m=r.randint(-1,1)
        y6m=r.randint(-1,3)
        x6m=r.randint(-1,1)   
        y7m=r.randint(-1,3)
        x7m=r.randint(-1,1)
        y8m=r.randint(-1,3)
        x8m=r.randint(-1,1)
        y9m=r.randint(-1,3)
        x9m=r.randint(-1,1)
        y10m=r.randint(-1,3)
        x10m=r.randint(-1,1)
    
#---------------------------------pohyb--asteroidu--1------------------------------------------#
        if a1_d == 0 :    
            c.move(a1,x1m,y1m)
            c.move(ca1,x1m,y1m)
            y1 += y1m
            x1 += x1m
            
            if x1 <= 400 :
                x1 += 10
                c.move(a1,10,1)
                c.move(ca1,10,1)
            elif x1 + 100 >= 1520 :
                x1 -= 10
                c.move(a1,-10,1)
                c.move(ca1,-10,1)

            if y1 + 50 >= 850 and ta1 == 1 :
                defeat()
            elif y1 + 100 >= 850 and ta1 == 2 :
                defeat()
        else:
            pass   
                
    #---------------------------------pohyb--asteroidu--2------------------------------------------#
        if a2_d == 0 :
            c.move(a2,x2m,y2m)
            c.move(ca2,x2m,y2m)
            y2 += y2m
            x2 += x2m
            
            if x2 <= 400 :
                x2 += 10
                c.move(a2,10,1)
                c.move(ca2,10,1)
            elif x2 + 100 >= 1520 :
                x2 -= 10
                c.move(a2,-10,1)
                c.move(ca2,-10,1) 
            
            if y2 + 50 >= 850 and ta2 == 1 :
                defeat()
            elif y2 + 100 >= 850 and ta2 == 2 :
                defeat()
        else:
            pass       
    #---------------------------------pohyb--asteroidu--3------------------------------------------#
        if a3_d == 0 :    
            c.move(a3,x3m,y3m)
            c.move(ca3,x3m,y3m)
            y3 += y3m
            x3 += x3m 
            if x3 <= 400 :
                x3 += 10
                c.move(a3,10,1)
                c.move(ca3,10,1)
            elif x3 + 100 >= 1520 :
                x3 -= 10
                c.move(a3,-10,1)
                c.move(ca3,-10,1)

                
            if y3 + 50 >= 850 and ta3 == 1 :
                defeat()
            elif y3 + 100 >= 850 and ta3 == 2 :
                defeat()
        else:
            pass        
    #---------------------------------pohyb--asteroidu--4------------------------------------------# 
        if a4_d == 0 :
            c.move(a4,x4m,y4m)
            c.move(ca4,x4m,y4m)
            y4 += y4m
            x4 += x4m
            
            if x4 <= 400 :
                x4 += 10
                c.move(a4,10,1)
                c.move(ca4,10,1)
            elif x4 + 100 >= 1520 :
                x4 -= 10
                c.move(a4,-10,1)
                c.move(ca4,-10,1)

                
            if y4 + 50 >= 850 and ta4 == 1 :
                defeat()
            elif y4 + 100 >= 850 and ta4 == 2 :
                defeat()
        else:
            pass
        
    #---------------------------------pohyb--asteroidu--5------------------------------------------#
        if a5_d == 0 :
            c.move(a5,x5m,y5m)
            c.move(ca5,x5m,y5m)
            y5 += y5m
            x5 += x5m
            
            if x5 <= 400 :
                x5 += 10
                c.move(a5,10,1)
                c.move(ca5,10,1)
            elif x5 + 100 >= 1520 :
                x5 -= 10
                c.move(a5,-10,1)
                c.move(ca5,-10,1)

            
                
            if y5 + 50 >= 850 and ta5 == 1 :
                defeat()
            elif y5 + 100 >= 850 and ta5 == 2 :
                defeat()
        else:
            pass        
    #---------------------------------pohyb--asteroidu--6------------------------------------------#
        if a6_d == 0 :    
            c.move(a6,x6m,y6m)
            c.move(ca6,x6m,y6m)
            y6 += y6m
            x6 += x6m
            
            if x6 <= 400 :
                x6 += 10
                c.move(a6,10,1)
                c.move(ca6,10,1)
            elif x6 + 100 >= 1520 :
                x6 -= 10
                c.move(a6,-10,1)
                c.move(ca6,-10,1)

            if y6 + 50 >= 850 and ta6 == 1 :
                defeat()
            elif y6 + 100 >= 850 and ta6 == 2 :
                defeat()
        else:
            pass    
    #---------------------------------pohyb--asteroidu--7------------------------------------------#
        if a7_d == 0 :
            c.move(a7,x7m,y7m)
            c.move(ca7,x7m,y7m)
            y7 += y7m
            x7 += x7m
            
            if x7 <= 400 :
                x7 += 10
                c.move(a7,10,1)
                c.move(ca7,10,1)
            elif x7 + 100 >= 1520 :
                x7 -= 10
                c.move(a7,-10,1)
                c.move(ca7,-10,1)

            if y7 + 50 >= 850 and ta7 == 1 :
                defeat()
            elif y7 + 100 >= 850 and ta7 == 2 :
                defeat()
        else:
            pass        
    #---------------------------------pohyb--asteroidu--8------------------------------------------#
        if a8_d == 0 :        
            c.move(a8,x8m,y8m)
            c.move(ca8,x8m,y8m)
            y8 += y8m
            x8 += x8m
            
            if x8 <= 400 :
                x8 += 10
                c.move(a8,10,1)
                c.move(ca8,10,1)
            elif x8 + 100 >= 1520 :
                x8 -= 10
                c.move(a8,-10,1)
                c.move(ca8,-10,1)
                
            if y8 + 50 >= 850 and ta8 == 1 :
                defeat()
            elif y8 + 100 >= 850 and ta8 == 2 :
                defeat()
        else:
            pass        
    #---------------------------------pohyb--asteroidu--9------------------------------------------#
        if a9_d == 0 :
            c.move(a9,x9m,y9m)
            c.move(ca9,x9m,y9m)
            y9 += y9m
            x9 += x9m
            
            if x9 <= 400 :
                x9 += 10
                c.move(a9,10,1)
                c.move(ca9,10,1)
            elif x9 + 100 >= 1520 :
                x9 -= 10
                c.move(a9,-10,1)
                c.move(ca9,-10,1)

            if y9 + 50 >= 850 and ta9 == 1 :
                defeat()
            elif y9 + 100 >= 850 and ta9 == 2 :
                defeat()
        else:
            pass        
    #---------------------------------pohyb--asteroidu--10------------------------------------------#      
        if a10_d == 0 :
            c.move(a10,x10m,y10m)
            c.move(ca10,x10m,y10m)
            y10 += y10m
            x10 += x10m
            
            if x10 <= 400 :
                x10 += 10
                c.move(a10,10,1)
                c.move(ca10,10,1)
            elif x10 + 100 >= 1520 :
                x10 -= 10
                c.move(a10,-10,1)
                c.move(ca10,-10,1)

            if y10 + 50 >= 850 and ta10 == 1 :
                defeat()
            elif y10 + 100 >= 850 and ta10 == 2 :
                defeat()
                
            c.update()
            if asteroids_destroyed < 10:
                c.after(20,loopinmovement_easy)
        else:
            pass
        
    ##vytvorenie asteroidov v strednej obtiaznosti
    def planetoids_spawn_medium():
        global  a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
        global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
        global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
        global sa1,sa2,sa3,sa4,sa5,sa6,sa7,sa8,sa9,sa10
        global ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9,ta10
        global ac1,ac2,ac3,ac4,ac5,ac6,ac7,ac8,ac9,ac10
        global ca1,ca2,ca3,ca4,ca5,ca6,ca7,ca8,ca9,ca10

        x1=r.randint(401,502)
        y1=r.randint(200,250)
        ta1 = r.randint(1,2)
        d1 = r.randint(1,100)
        x2=r.randint(502,604)
        y2=r.randint(200,250)
        ta2 = r.randint(1,2)
        d2= r.randint(1,100)
        x3=r.randint(604,706)
        y3=r.randint(200,250)
        ta3 = r.randint(1,2)
        d3 = r.randint(1,100)
        x4=r.randint(706,808)
        y4=r.randint(200,250)
        ta4 = r.randint(1,2)
        d4 = r.randint(0,100)
        x5=r.randint(808,910)
        y5=r.randint(200,250)
        ta5 = r.randint(1,2)
        d5 = r.randint(1,100)
        x6=r.randint(910,1012)
        y6=r.randint(200,250)
        ta6 = r.randint(1,2)
        d6= r.randint(1,100)
        x7=r.randint(1012,1114)
        y7=r.randint(200,250)
        ta7 = r.randint(1,2)
        d7 = r.randint(1,100)
        x8=r.randint(1114,1216)
        y8=r.randint(200,250)
        ta8 = r.randint(1,2)
        d8 = r.randint(1,100)
        x9=r.randint(1216,1318)
        y9=r.randint(200,250)
        ta9 = r.randint(1,2)
        d9 = r.randint(1,100)
        x10=r.randint(1318,1420)
        y10=r.randint(200,250)
        ta10 = r.randint(1,2)
        d10 = r.randint(1,100)
  
##       1.asteroid
    
        if ta1 == 1 and d1 <= 60:
            a1=c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="grey")
            ca1 = c.create_image(x1,y1,anchor=NW,image = w_ast_m,tag="grey")
            sa1 = 5
            ac1 = "w"
        elif ta1 == 2 and d1 <= 60:  
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="grey")
            ca1 = c.create_image(x1,y1,anchor=NW,image = w_ast_v,tag="grey")
            sa1 = 5
            ac1 = "w"
        elif ta1 == 2 and d1 <=90 and d1 >= 61:
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="red")
            ca1 = c.create_image(x1,y1,anchor=NW,image = r_ast_v,tag="red")
            sa1 = 0
            ac1 = "r"
        elif ta1 == 1 and d1 <=90 and d1 >= 61:
            a1= c.create_rectangle(x1,y1,x1+100,y1+50,outline=",width=0",tag="red")
            ca1 = c.create_image(x1,y1,anchor=NW,image = r_ast_m,tag="red")
            sa1 = 0
            ac1 = "r"
        elif ta1 == 2 and d1 >= 91: 
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="gold")
            ca1 = c.create_image(x1,y1,anchor=NW,image = g_ast_v,tag="gold")
            sa1 = 10
            ac1 = "g"
        elif ta1 == 1 and d1 >= 91:
            a1=c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="gold")
            ca1 = c.create_image(x1,y1,anchor=NW,image = g_ast_m,tag="gold")
            sa1 = 10
            ac1 = "g"     

##       2. asteroid

        if ta2 == 1 and d2 <= 60:
            a2=c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="grey")
            ca2 = c.create_image(x2,y2,anchor=NW,image = w_ast_m,tag="grey")
            sa2 = 5
            ac2 = "w"
        elif ta2 == 2 and d2 <= 60:  
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="grey")
            ca2 = c.create_image(x2,y2,anchor=NW,image = w_ast_v,tag="grey")
            sa2 = 5
            ac2 = "w"
        elif ta2 == 2 and d2 <=90 and d2 >= 61:
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="red")
            ca2 = c.create_image(x2,y2,anchor=NW,image = r_ast_v,tag="red")
            sa2 = 0
            ac2 = "r"
        elif ta2 == 1 and d2 <=90 and d2 >= 61:
            a2= c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="red")
            ca2 = c.create_image(x2,y2,anchor=NW,image = r_ast_m,tag="red")
            sa2 = 0
            ac2 = "r"
        elif ta2 == 2 and d2 >= 91: 
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="gold")
            ca2 = c.create_image(x2,y2,anchor=NW,image = g_ast_v,tag="gold")
            sa2 = 10
            ac2 = "g"
        elif ta2 == 1 and d2 >= 91:
            a2=c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="gold")
            ca2 = c.create_image(x2,y2,anchor=NW,image = g_ast_m,tag="gold")
            sa2 = 10
            ac2 = "g"       
       
##       3. asteroid

        if ta3 == 1 and d3 <= 60:
            a3=c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="grey")
            ca3 = c.create_image(x3,y3,anchor=NW,image = w_ast_m,tag="grey")
            sa3 = 5
            ac3 = "w"
        elif ta3 == 2 and d3 <= 60:  
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="grey")
            ca3 = c.create_image(x3,y3,anchor=NW,image = w_ast_v,tag="grey")
            sa3 = 5
            ac3 = "w"
        elif ta3 == 2 and d3 <=90 and d3 >= 61:
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="red")
            ca3 = c.create_image(x3,y3,anchor=NW,image = r_ast_v,tag="red")
            sa3 = 0
            ac3 = "r"
        elif ta3 == 1 and d3 <=90 and d3 >= 61:
            a3= c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="red")
            ca3 = c.create_image(x3,y3,anchor=NW,image = r_ast_m,tag="red")
            sa3 = 0
            ac3 = "r"
        elif ta3 == 2 and d3 >= 91: 
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="gold")
            ca3 = c.create_image(x3,y3,anchor=NW,image = g_ast_v,tag="gold")
            sa3 = 10
            ac3 = "g"
        elif ta3 == 1 and d3 >= 91:
            a3=c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="gold")
            ca3 = c.create_image(x3,y3,anchor=NW,image = g_ast_m,tag="gold")
            sa3 = 10
            ac3 = "g"
                                                                                                                                                               
##       4. asteroid

        if ta4 == 1 and d4 <= 60:
            a4=c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="grey")
            ca4 = c.create_image(x4,y4,anchor=NW,image = w_ast_m,tag="grey")
            sa4 = 5
            ac4 = "w"
        elif ta4 == 2 and d4 <= 60:  
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="grey")
            ca4 = c.create_image(x4,y4,anchor=NW,image = w_ast_v,tag="grey")
            sa4 = 5
            ac4 = "w"
        elif ta4 == 2 and d4 <=90 and d4 >= 61:
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="red")
            ca4 = c.create_image(x4,y4,anchor=NW,image = r_ast_v,tag="red")
            sa4 = 0
            ac4 = "r"
        elif ta4 == 1 and d4 <=90 and d4 >= 61:
            a4= c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="red")
            ca4 = c.create_image(x4,y4,anchor=NW,image = r_ast_m,tag="red")
            sa4 = 0
            ac4 = "r"
        elif ta4 == 2 and d4 >= 91: 
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="gold")
            ca4 = c.create_image(x4,y4,anchor=NW,image = g_ast_v,tag="gold")
            sa4 = 10
            ac4 = "g"
        elif ta4 == 1 and d4 >= 91:
            a4=c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="gold")
            ca4 = c.create_image(x4,y4,anchor=NW,image = g_ast_m,tag="gold")
            sa4 = 10
            ac4 = "g"     

##       5. asteroid

        if ta5 == 1 and d5 <= 60:
            a5=c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="grey")
            ca5 = c.create_image(x5,y5,anchor=NW,image = w_ast_m,tag="grey")
            sa5 = 5
            ac5 = "w"
        elif ta5 == 2 and d5 <= 60:  
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="grey")
            ca5 = c.create_image(x5,y5,anchor=NW,image = w_ast_v,tag="grey")
            sa5 = 5
            ac5 = "w"
        elif ta5 == 2 and d5 <=90 and d5 >= 61:
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="red")
            ca5 = c.create_image(x5,y5,anchor=NW,image = r_ast_v,tag="red")
            sa5 = 0
            ac5 = "r"
        elif ta5 == 1 and d5 <=90 and d5 >= 61:
            a5= c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="red")
            ca5 = c.create_image(x5,y5,anchor=NW,image = r_ast_m,tag="red")
            sa5 = 0
            ac5 = "r"
        elif ta5 == 2 and d5 >= 91: 
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="gold")
            ca5 = c.create_image(x5,y5,anchor=NW,image = g_ast_v,tag="gold")
            sa5 = 10
            ac5 = "g"
        elif ta5 == 1 and d5 >= 91:
            a5=c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="gold")
            ca5 = c.create_image(x5,y5,anchor=NW,image = g_ast_m,tag="gold")
            sa5 = 10
            ac5 = "g"
     
##       6. asteroid

        if ta6 == 1 and d6 <= 60:
            a6=c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="grey")
            ca6 = c.create_image(x6,y6,anchor=NW,image = w_ast_m,tag="grey")
            sa6 = 5
            ac6 = "w"
        elif ta6 == 2 and d6 <= 60:  
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="grey")
            ca6 = c.create_image(x6,y6,anchor=NW,image = w_ast_v,tag="grey")
            sa6 = 5
            ac6 = "w"
        elif ta6 == 2 and d6 <=90 and d6 >= 61:
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="red")
            ca6 = c.create_image(x6,y6,anchor=NW,image = r_ast_v,tag="red")
            sa6 = 0
            ac6 = "r"
        elif ta6 == 1 and d6 <=90 and d6 >= 61:
            a6= c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="red")
            ca6 = c.create_image(x6,y6,anchor=NW,image = r_ast_m,tag="red")
            sa6 = 0
            ac6 = "r"
        elif ta6 == 2 and d6 >= 91: 
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="gold")
            ca6 = c.create_image(x6,y6,anchor=NW,image = g_ast_v,tag="gold")
            sa6 = 10
            ac6 = "g"
        elif ta6 == 1 and d6 >= 91:
            a6=c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="gold")
            ca6 = c.create_image(x6,y6,anchor=NW,image = g_ast_m,tag="gold")
            sa6 = 10
            ac6 = "g"        

##       7. asteroid

        if ta7 == 1 and d7 <= 60:
            a7=c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="grey")
            ca7 = c.create_image(x7,y7,anchor=NW,image = w_ast_m,tag="grey")
            sa7 = 5
            ac7 = "w"
        elif ta7 == 2 and d7 <= 60:  
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="grey")
            ca7 = c.create_image(x7,y7,anchor=NW,image = w_ast_v,tag="grey")
            sa7 = 5
            ac7 = "w"
        elif ta7 == 2 and d7 <=90 and d7 >= 61:
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="red")
            ca7 = c.create_image(x7,y7,anchor=NW,image = r_ast_v,tag="red")
            sa7 = 0
            ac7 = "r"
        elif ta7 == 1 and d7 <=90 and d7 >= 61:
            a7= c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="red")
            ca7 = c.create_image(x7,y7,anchor=NW,image = r_ast_m,tag="red")
            sa7 = 0
            ac7 = "r"
        elif ta7 == 2 and d7 >= 91: 
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="gold")
            ca7 = c.create_image(x7,y7,anchor=NW,image = g_ast_v,tag="gold")
            sa7 = 10
            ac7 = "g"
        elif ta7 == 1 and d7 >= 91:
            a7=c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="gold")
            ca7 = c.create_image(x7,y7,anchor=NW,image = g_ast_m,tag="gold")
            sa7 = 10
            ac7 = "g"
       
##       8. asteroid

        if ta8 == 1 and d8 <= 60:
            a8=c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="grey")
            ca8 = c.create_image(x8,y8,anchor=NW,image = w_ast_m,tag="grey")
            sa8 = 5
            ac8 = "w"
        elif ta8 == 2 and d8 <= 60:  
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="grey")
            ca8 = c.create_image(x8,y8,anchor=NW,image = w_ast_v,tag="grey")
            sa8 = 5
            ac8 = "w"
        elif ta8 == 2 and d8 <=90 and d8 >= 61:
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="red")
            ca8 = c.create_image(x8,y8,anchor=NW,image = r_ast_v,tag="red")
            sa8 = 0
            ac8 = "r"
        elif ta8 == 1 and d8 <=90 and d8 >= 61:
            a8= c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="red")
            ca8 = c.create_image(x8,y8,anchor=NW,image = r_ast_m,tag="red")
            sa8 = 0
            ac8 = "r"
        elif ta8 == 2 and d8 >= 91: 
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="gold")
            ca8 = c.create_image(x8,y8,anchor=NW,image = g_ast_v,tag="gold")
            sa8 = 10
            ac8 = "g"
        elif ta8 == 1 and d8 >= 91:
            a8=c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="gold")
            ca8 = c.create_image(x8,y8,anchor=NW,image = g_ast_m,tag="gold")
            sa8 = 10
            ac8 = "g"   

##       9. asteroid

        if ta9 == 1 and d9 <= 60:
            a9=c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="grey")
            ca9 = c.create_image(x9,y9,anchor=NW,image = w_ast_m,tag="grey")
            sa9 = 5
            ac9 = "w"
        elif ta9 == 2 and d9 <= 60:  
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="grey")
            ca9 = c.create_image(x9,y9,anchor=NW,image = w_ast_v,tag="grey")
            sa9 = 5
            ac9 = "w"
        elif ta9 == 2 and d9 <=90 and d9 >= 61:
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="red")
            ca9 = c.create_image(x9,y9,anchor=NW,image = r_ast_v,tag="red")
            sa9 = 0
            ac9 = "r"
        elif ta9 == 1 and d9 <=90 and d9 >= 61:
            a9= c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="red")
            ca9 = c.create_image(x9,y9,anchor=NW,image = r_ast_m,tag="red")
            sa9 = 0
            ac9 = "r"
        elif ta9 == 2 and d9 >= 91: 
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="gold")
            ca9 = c.create_image(x9,y9,anchor=NW,image = g_ast_v,tag="gold")
            sa9 = 10
            ac9 = "g"
        elif ta9 == 1 and d9 >= 91:
            a9=c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="gold")
            ca9 = c.create_image(x9,y9,anchor=NW,image = g_ast_m,tag="gold")
            sa9 = 10
            ac9 = "g"       

##       10. asteroid

        if ta10 == 1 and d10 <= 60:
            a10=c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="grey")
            ca10 = c.create_image(x10,y10,anchor=NW,image = w_ast_m,tag="grey")
            sa10 = 5
            ac10 = "w"
        elif ta10 == 2 and d10 <= 60:  
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="grey")
            ca10 = c.create_image(x10,y10,anchor=NW,image = w_ast_v,tag="grey")
            sa10 = 5
            ac10 = "w"
        elif ta10 == 2 and d10 <=90 and d10 >= 61:
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="red")
            ca10 = c.create_image(x10,y10,anchor=NW,image = r_ast_v,tag="red")
            sa10 = 0
            ac10 = "r"
        elif ta10 == 1 and d10 <=90 and d10 >= 61:
            a10= c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="red")
            ca10 = c.create_image(x10,y10,anchor=NW,image = r_ast_m,tag="red")
            sa10 = 0
            ac10 = "r"
        elif ta10 == 2 and d10 >= 91: 
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="gold")
            ca10 = c.create_image(x10,y10,anchor=NW,image = g_ast_v,tag="gold")
            sa10 = 10
            ac10 = "g"
        elif ta10 == 1 and d10 >= 91:
            a10=c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="gold")
            ca10 = c.create_image(x10,y10,anchor=NW,image = g_ast_m,tag="gold")
            sa10 = 10
            ac10 = "g"

    ##pohyb asteroidov v strednej obtiaznosti
    def loopinmovement_medium():
        global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
        global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
        global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
        global sa1,sa2,sa3,sa4,sa5,sa6,sa7,sa8,sa9,sa10
        global ac1,ac2,ac3,ac4,ac5,ac6,ac7,ac8,ac9,ac10
        global ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9,ta10
        global a1_d,a2_d,a3_d,a4_d,a5_d,a6_d,a7_d,a8_d,a9_d,a10_d

#velkosť pohybu horizontálne(y) - tak trocha funguje- ide aj do mínusi(podla obtiažnosti) 
        y1mw=r.randint(0,3)
        x1mw=r.randint(-1,1)
        y1mr=r.randint(-10,11)
        x1mr=r.randint(-10,10)
    
        y2mw=r.randint(0,3)
        x2mw=r.randint(-1,1)
        y2mr=r.randint(-10,11)
        x2mr=r.randint(-10,10)
    
        y3mw=r.randint(0,3)
        x3mw=r.randint(-1,1)
        y3mr=r.randint(-10,11)
        x3mr=r.randint(-10,10)
    
        y4mw=r.randint(0,3)
        x4mw=r.randint(-1,1)
        y4mr=r.randint(-10,11)
        x4mr=r.randint(-10,10)
    
        y5mw=r.randint(0,3)
        x5mw=r.randint(-1,1)
        y5mr=r.randint(-10,11)
        x5mr=r.randint(-10,10)
    
        y6mw=r.randint(0,3)
        x6mw=r.randint(-1,1)
        y6mr=r.randint(-10,11)
        x6mr=r.randint(-10,10)
    
        y7mw=r.randint(0,3)
        x7mw=r.randint(-1,1)
        y7mr=r.randint(-10,11)
        x7mr=r.randint(-10,10)
    
        y8mw=r.randint(0,3)
        x8mw=r.randint(-1,1)
        y8mr=r.randint(-10,11)
        x8mr=r.randint(-10,10)
    
        y9mw=r.randint(0,3)
        x9mw=r.randint(-1,1)
        y9mr=r.randint(-10,11)
        x9mr=r.randint(-10,10)
    
        y10mw=r.randint(0,3)
        x10mw=r.randint(-1,1)
        y10mr=r.randint(-10,11)
        x10mr=r.randint(-10,10)
    
    #--------------------------------------pohyb-asteroidu--1-------------------------------------------------------------------#        
        if a1_d == 0 :
    #-pohyb-bieleho-asteroidu
        
            if ac1 == "w" or ac1 == "g" :
                c.move(a1,x1mw,y1mw)
                c.move(ca1,x1mw,y1mw)
                y1 += y1mw
                x1 += x1mw
            
                if x1 <= 400 :
                    x1 += 10
                    c.move(a1,10,1)
                    c.move(ca1,10,1)
                elif x1 + 100 >= 1520 :
                    x1 -= 10
                    c.move(a1,-10,1)
                    c.move(ca1,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac1 == "r" :
                c.move(a1,x1mr,y1mr)
                c.move(ca1,x1mr,y1mr)
                y1 += y1mr
                x1 += x1mr
                if x1 <= 400 :
                    x1 += 10  
                    c.move(a1,10,1)
                    c.move(ca1,10,1)
                elif x1 + 100 >= 1520 :
                    x1 -= 10
                    c.move(a1,-10,1)
                    c.move(ca1,-10,1)

                    
                elif y1 <= 200  :
                    y1 += 10 
                    c.move(a1,0,10)
                    c.move(ca1,0,10)
            

        
            if y1 + 50 >= 850 and ta1 == 1 :
                defeat()
            elif y1 + 100 >= 850 and ta1 == 2 :
                defeat()
        else:    
            pass
    #--------------------------------------pohyb-asteroidu--2-------------------------------------------------------------------#  
        if a2_d == 0 :
    #-pohyb-bieleho-asteroidu
        
            if ac2 == "w" or ac2 == "g" :
                c.move(a2,x2mw,y2mw)
                c.move(ca2,x2mw,y2mw)
                y2 += y2mw
                x2 += x2mw
            
                if x2 <= 400 :
                    x2 += 10
                    c.move(a2,10,1)
                    c.move(ca2,10,1)
                elif x2 + 100 >= 1520 :
                    x2 -= 10
                    c.move(a2,-10,1)
                    c.move(ca2,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac2 == "r" :
                c.move(a2,x2mr,y2mr)
                c.move(ca2,x2mr,y2mr)
                y2 += y2mr
                x2 += x2mr
                if x2 <= 400 :
                    x2 += 10  
                    c.move(a2,10,1)
                    c.move(ca2,10,1)
                elif x2 + 100 >= 1520 :
                    x2 -= 10
                    c.move(a2,-10,1)
                    c.move(ca2,-10,1)

                elif y2 <= 200  :
                    y2 += 10 
                    c.move(a2,0,10)
                    c.move(ca2,0,10)

        
            if y2 + 50 >= 850 and ta2 == 1 :
                defeat()
            elif y2 + 100 >= 850 and ta2 == 2 :
                defeat()           
        else:
            pass
    #--------------------------------------pohyb-asteroidu--3-------------------------------------------------------------------#  
        if a3_d == 0 :    
    #-pohyb-bieleho-asteroidu
        
            if ac3 == "w" or ac3 == "g" :
                c.move(a3,x3mw,y3mw)
                c.move(ca3,x3mw,y3mw)
                y3 += y3mw
                x3 += x3mw
            
                if x3 <= 400 :
                    x3 += 10
                    c.move(a3,10,1)
                    c.move(ca3,10,1)
                elif x3 + 100 >= 1520 :
                    x3 -= 10
                    c.move(a3,-10,1)
                    c.move(ca3,-10,1)
            
            
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac3 == "r" :
                c.move(a3,x3mr,y3mr)
                c.move(ca3,x3mr,y3mr)
                y3 += y3mr
                x3 += x3mr
                if x3 <= 400 :
                    x3 += 10  
                    c.move(a3,10,1)
                    c.move(ca3,10,1)
                elif x3 + 100 >= 1520 :
                    x3 -= 10
                    c.move(a3,-10,1)
                    c.move(ca3,-10,1)

                    
                elif y3 <= 200  :
                    y3 += 10 
                    c.move(a3,0,10)
                    c.move(ca3,0,10)

                            
            
            if y3 + 50 >= 850 and ta3 == 1 :
                defeat()
            elif y3 + 100 >= 850 and ta3 == 2 :
                defeat()
        else:        
            pass    

    #--------------------------------------pohyb-asteroidu--4-------------------------------------------------------------------#  
        if a4_d == 0 :        
                #-pohyb-bieleho-asteroidu
        
            if ac4 == "w" or ac4 == "g" :
                c.move(a4,x4mw,y4mw)
                c.move(ca4,x4mw,y4mw)
                y4 += y4mw
                x4 += x4mw
            
                if x4 <= 400 :
                    x4 += 10
                    c.move(a4,10,1)
                    c.move(ca4,10,1)
                elif x4 + 100 >= 1520 :
                    x4 -= 10
                    c.move(a4,-10,1)
                    c.move(ca4,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac4 == "r" :
                c.move(a4,x4mr,y4mr)
                c.move(ca4,x4mr,y4mr)
                y4 += y4mr
                x4 += x4mr
                if x4 <= 400 :
                    x4 += 10  
                    c.move(a4,10,1)
                    c.move(ca4,10,1)
                elif x4 + 100 >= 1520 :
                    x4 -= 10
                    c.move(a4,-10,1)
                    c.move(ca4,-10,1)

                    
                elif y4 <= 200  :
                    y4 += 10 
                    c.move(a4,0,10)
                    c.move(ca4,0,10)
                                        
                            
            
            if y4 + 50 >= 850 and ta4 == 1 :
                defeat()
            elif y4 + 100 >= 850 and ta4 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--5-------------------------------------------------------------------#  
        if a5_d == 0 :        
            #-pohyb-bieleho-asteroidu
        
            if ac5 == "w" or ac5 == "g" :
                c.move(a5,x5mw,y5mw)
                c.move(ca5,x5mw,y5mw)
                y5 += y5mw
                x5 += x5mw
            
                if x5 <= 400 :
                    x5 += 10
                    c.move(a5,10,1)
                    c.move(ca5,10,1)
                elif x5 + 100 >= 1520 :
                    x5 -= 10
                    c.move(a5,-10,1)
                    c.move(ca5,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac5 == "r" :
                c.move(a5,x5mr,y5mr)
                c.move(ca5,x5mr,y5mr)
                y5 += y5mr
                x5 += x5mr
                if x5 <= 400 :
                    x5 += 10  
                    c.move(a5,10,1)
                    c.move(ca5,10,1)
                elif x5 + 100 >= 1520 :
                    x5 -= 10
                    c.move(a5,-10,1)
                    c.move(ca5,-10,1)

                    
                elif y5 <= 200  :
                    y5 += 10 
                    c.move(a5,0,10)
                    c.move(ca5,0,10)
                                        
        
            
            if y5 + 50 >= 850 and ta5 == 1 :
                defeat()
            elif y5 + 100 >= 850 and ta5 == 2 :
                defeat()
        else:
            pass        
    #--------------------------------------pohyb-asteroidu--6-------------------------------------------------------------------#  
        if a6_d == 0 :    
            #-pohyb-bieleho-asteroidu
        
            if ac6 == "w" or ac6 == "g" :
                c.move(a6,x6mw,y6mw)
                c.move(ca6,x6mw,y6mw)
                y6 += y6mw
                x6 += x6mw
            
                if x6 <= 400 :
                    x6 += 10
                    c.move(a6,10,1)
                    c.move(ca6,10,1)
                elif x6 + 100 >= 1520 :
                    x6 -= 10
                    c.move(a6,-10,1)
                    c.move(ca6,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac6 == "r" :
                c.move(a6,x6mr,y6mr)
                c.move(ca6,x6mr,y6mr)
                y6 += y6mr
                x6 += x6mr
                if x6 <= 400 :
                    x6 += 10  
                    c.move(a6,10,1)
                    c.move(ca6,10,1)
                elif x6 + 100 >= 1520 :
                    x6 -= 10
                    c.move(a6,-10,1)
                    c.move(ca6,-10,1)

                    
                elif y6 <= 200  :
                    y6 += 10 
                    c.move(a6,0,10)
                    c.move(ca6,0,10)    

                    
            
            if y6 + 50 >= 850 and ta6 == 1 :
                defeat()
            elif y6 + 100 >= 850 and ta6 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--7-------------------------------------------------------------------#  
        if a7_d == 0 :        
                #-pohyb-bieleho-asteroidu
        
            if ac7 == "w" or ac7 == "g" :
                c.move(a7,x7mw,y7mw)
                c.move(ca7,x7mw,y7mw)
                y7 += y7mw
                x7 += x7mw
            
                if x7 <= 400 :
                    x7 += 10
                    c.move(a7,10,1)
                    c.move(ca7,10,1)
                elif x7 + 100 >= 1520 :
                    x7 -= 10
                    c.move(a7,-10,1)
                    c.move(ca7,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac7 == "r" :
                c.move(a7,x7mr,y7mr)
                c.move(ca7,x7mr,y7mr)
                y7 += y7mr
                x7 += x7mr
                if x7 <= 400 :
                    x7 += 10  
                    c.move(a7,10,1)
                    c.move(ca7,10,1)
                elif x7 + 100 >= 1520 :
                    x7 -= 10
                    c.move(a7,-10,1)
                    c.move(ca7,-10,1)

                    
                elif y7 <= 200  :
                    y7 += 10 
                    c.move(a7,0,10)
                    c.move(ca7,0,10)   

            if y7 + 50 >= 850 and ta7 == 1 :
                defeat()
            elif y7 + 100 >= 850 and ta7 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--8-------------------------------------------------------------------#  
        if a8_d == 0 :        
            #-pohyb-bieleho-asteroidu
        
            if ac8 == "w" or ac8 == "g" :
                c.move(a8,x8mw,y8mw)
                c.move(ca8,x8mw,y8mw)
                y8 += y8mw
                x8 += x8mw
            
                if x8 <= 400 :
                    x8 += 10
                    c.move(a8,10,1)
                    c.move(ca8,10,1)
                elif x8 + 100 >= 1520 :
                    x8 -= 10
                    c.move(a8,-10,1)
                    c.move(ca8,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac8 == "r" :
                c.move(a8,x8mr,y8mr)
                c.move(ca8,x8mr,y8mr)
                y8 += y8mr
                x8 += x8mr
                if x8 <= 400 :
                    x8 += 10  
                    c.move(a8,10,1)
                    c.move(ca8,10,1)
                elif x8 + 100 >= 1520 :
                    x8 -= 10
                    c.move(a8,-10,1)
                    c.move(ca8,-10,1)
                    
                elif y8 <= 200  :
                    y8 += 10 
                    c.move(a8,0,10)
                    c.move(ca8,0,10)
                            
            if y8 + 50 >= 850 and ta8 == 1 :
                defeat()
            elif y8 + 100 >= 850 and ta8 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--9-------------------------------------------------------------------#  
        if a9_d == 0 :        
                #-pohyb-bieleho-asteroidu
        
            if ac9 == "w" or ac9 == "g" :
                c.move(a9,x9mw,y9mw)
                c.move(ca9,x9mw,y9mw)
                y9 += y9mw
                x9 += x9mw
            
                if x9 <= 400 :
                    x9 += 10
                    c.move(a9,10,1)
                    c.move(ca9,10,1)
                elif x9 + 100 >= 1520 :
                    x9 -= 10
                    c.move(a9,-10,1)
                    c.move(ca9,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac9 == "r" :
                c.move(a9,x9mr,y9mr)
                c.move(ca9,x9mr,y9mr)
                y9 += y9mr
                x9 += x9mr
                if x9 <= 400 :
                    x9 += 10  
                    c.move(a9,10,1)
                    c.move(ca9,10,1)
                elif x9 + 100 >= 1520 :
                    x9 -= 10
                    c.move(a9,-10,1)
                    c.move(ca9,-10,1)

                    
                elif y9 <= 200  :
                    y9 += 10 
                    c.move(a9,0,10)
                    c.move(ca9,0,10)
                
            if y9 + 50 >= 850 and ta9 == 1 :
                defeat()
            elif y9 + 100 >= 850 and ta9 == 2 :
                defeat()
        else:
            pass         
                
    #--------------------------------------pohyb-asteroidu--10-------------------------------------------------------------------#  
        if a10_d == 0 :        
            #-pohyb-bieleho-asteroidu
        
            if ac10 == "w" or ac10 == "g" :
                c.move(a10,x10mw,y10mw)
                c.move(ca10,x10mw,y10mw)
                y10 += y10mw
                x10 += x10mw
            
                if x10 <= 400 :
                    x10 += 10
                    c.move(a10,10,1)
                    c.move(ca10,10,1)
                elif x10 + 100 >= 1520 :
                    x10 -= 10
                    c.move(a10,-10,1)
                    c.move(ca10,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac10 == "r" :
                c.move(a10,x10mr,y10mr)
                c.move(ca10,x10mr,y10mr)
                y10 += y10mr
                x10 += x10mr
                if x10 <= 400 :
                    x10 += 10  
                    c.move(a10,10,1)
                    c.move(ca10,10,1)
                elif x10 + 100 >= 1520 :
                    x10 -= 10
                    c.move(a10,-10,1)
                    c.move(ca10,-10,1)

                    
                elif y10 <= 200  :
                    y10 += 10 
                    c.move(a10,0,10)
                    c.move(ca10,0,10)
                            
                
            if y10 + 50 >= 850 and ta10 == 1 :
                defeat()
            elif y10 + 100 >= 850 and ta10 == 2 :
                defeat()  
        else:
            pass
                        

            c.update()
            if asteroids_destroyed < 10:
                c.after(20,loopinmovement_medium)

    ##vytvorenie asteroidov v tazkej obtiaznosti
    def planetoids_spawn_hard():
        global  a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
        global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
        global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
        global sa1,sa2,sa3,sa4,sa5,sa6,sa7,sa8,sa9,sa10
        global ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9,ta10
        global ac1,ac2,ac3,ac4,ac5,ac6,ac7,ac8,ac9,ac10
        global ca1,ca2,ca3,ca4,ca5,ca6,ca7,ca8,ca9,ca10
        global a1_d,a2_d,a3_d,a4_d,a5_d,a6_d,a7_d,a8_d,a9_d,a10_d

        x1=r.randint(401,502)
        y1=r.randint(200,250)
        ta1 = r.randint(1,2)
        d1 = r.randint(1,100)
        x2=r.randint(502,604)
        y2=r.randint(200,250)
        ta2 = r.randint(1,2)
        d2= r.randint(1,100)
        x3=r.randint(604,706)
        y3=r.randint(200,250)
        ta3 = r.randint(1,2)
        d3 = r.randint(1,100)
        x4=r.randint(706,808)
        y4=r.randint(200,250)
        ta4 = r.randint(1,2)
        d4 = r.randint(0,100)
        x5=r.randint(808,910)
        y5=r.randint(200,250)
        ta5 = r.randint(1,2)
        d5 = r.randint(1,100)
        x6=r.randint(910,1012)
        y6=r.randint(200,250)
        ta6 = r.randint(1,2)
        d6= r.randint(1,100)
        x7=r.randint(1012,1114)
        y7=r.randint(200,250)
        ta7 = r.randint(1,2)
        d7 = r.randint(1,100)
        x8=r.randint(1114,1216)
        y8=r.randint(200,250)
        ta8 = r.randint(1,2)
        d8 = r.randint(1,100)
        x9=r.randint(1216,1318)
        y9=r.randint(200,250)
        ta9 = r.randint(1,2)
        d9 = r.randint(1,100)
        x10=r.randint(1318,1420)
        y10=r.randint(200,250)
        ta10 = r.randint(1,2)
        d10 = r.randint(1,100)
  
##       1.asteroid
    
        if ta1 == 1 and d1 <= 60:
            a1=c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="grey")
            ca1 = c.create_image(x1,y1,anchor=NW,image = w_ast_m,tag="grey")
            sa1 = 5
            ac1 = "w"
        elif ta1 == 2 and d1 <= 60:  
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="grey")
            ca1 = c.create_image(x1,y1,anchor=NW,image = w_ast_v,tag="grey")
            sa1 = 5
            ac1 = "w"
        elif ta1 == 2 and d1 <=90 and d1 >= 61:
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="red")
            ca1 = c.create_image(x1,y1,anchor=NW,image = r_ast_v,tag="red")
            sa1 = 0
            ac1 = "r"
        elif ta1 == 1 and d1 <=90 and d1 >= 61:
            a1= c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="red")
            ca1 = c.create_image(x1,y1,anchor=NW,image = r_ast_m,tag="red")
            sa1 = 0
            ac1 = "r"
        elif ta1 == 2 and d1 >= 91: 
            a1=c.create_rectangle(x1,y1,x1+100,y1+100,outline="",width=0,tag="gold")
            ca1 = c.create_image(x1,y1,anchor=NW,image = g_ast_v,tag="gold")
            sa1 = 10
            ac1 = "g"
        elif ta1 == 1 and d1 >= 91:
            a1=c.create_rectangle(x1,y1,x1+100,y1+50,outline="",width=0,tag="gold")
            ca1 = c.create_image(x1,y1,anchor=NW,image = g_ast_m,tag="gold")
            sa1 = 10
            ac1 = "g"

##       2. asteroid

        if ta2 == 1 and d2 <= 60:
            a2=c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="grey")
            ca2 = c.create_image(x2,y2,anchor=NW,image = w_ast_m,tag="grey")
            sa2 = 5
            ac2 = "w"
        elif ta2 == 2 and d2 <= 60:  
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="grey")
            ca2 = c.create_image(x2,y2,anchor=NW,image = w_ast_v,tag="grey")
            sa2 = 5
            ac2 = "w"
        elif ta2 == 2 and d2 <=90 and d2 >= 61:
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="red")
            ca2 = c.create_image(x2,y2,anchor=NW,image = r_ast_v,tag="red")
            sa2 = 0
            ac2 = "r"
        elif ta2 == 1 and d2 <=90 and d2 >= 61:
            a2= c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="red")
            ca2 = c.create_image(x2,y2,anchor=NW,image = r_ast_m,tag="red")
            sa2 = 0
            ac2 = "r"
        elif ta2 == 2 and d2 >= 91: 
            a2=c.create_rectangle(x2,y2,x2+100,y2+100,outline="",width=0,tag="gold")
            ca2 = c.create_image(x2,y2,anchor=NW,image = g_ast_v,tag="gold")
            sa2 = 10
            ac2 = "g"
        elif ta2 == 1 and d2 >= 91:
            a2=c.create_rectangle(x2,y2,x2+100,y2+50,outline="",width=0,tag="gold")
            ca2 = c.create_image(x2,y2,anchor=NW,image = g_ast_m,tag="gold")
            sa2 = 10
            ac2 = "g"

##       3. asteroid

        if ta3 == 1 and d3 <= 60:
            a3=c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="grey")
            ca3 = c.create_image(x3,y3,anchor=NW,image = w_ast_m,tag="grey")
            sa3 = 5
            ac3 = "w"
        elif ta3 == 2 and d3 <= 60:  
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="grey")
            ca3 = c.create_image(x3,y3,anchor=NW,image = w_ast_v,tag="grey")
            sa3 = 5
            ac3 = "w"
        elif ta3 == 2 and d3 <=90 and d3 >= 61:
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="red")
            ca3 = c.create_image(x3,y3,anchor=NW,image = r_ast_v,tag="red")
            sa3 = 0
            ac3 = "r"
        elif ta3 == 1 and d3 <=90 and d3 >= 61:
            a3= c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="red")
            ca3 = c.create_image(x3,y3,anchor=NW,image = r_ast_m,tag="red")
            sa3 = 0
            ac3 = "r"
        elif ta3 == 2 and d3 >= 91: 
            a3=c.create_rectangle(x3,y3,x3+100,y3+100,outline="",width=0,tag="gold")
            ca3 = c.create_image(x3,y3,anchor=NW,image = g_ast_v,tag="gold")
            sa3 = 10
            ac3 = "g"
        elif ta3 == 1 and d3 >= 91:
            a3=c.create_rectangle(x3,y3,x3+100,y3+50,outline="",width=0,tag="gold")
            ca3 = c.create_image(x3,y3,anchor=NW,image = g_ast_m,tag="gold")
            sa3 = 10
            ac3 = "g"
                                                                                                                                                               
##       4. asteroid

        if ta4 == 1 and d4 <= 60:
            a4=c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="grey")
            ca4 = c.create_image(x4,y4,anchor=NW,image = w_ast_m,tag="grey")
            sa4 = 5
            ac4 = "w"
        elif ta4 == 2 and d4 <= 60:  
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="grey")
            ca4 = c.create_image(x4,y4,anchor=NW,image = w_ast_v,tag="grey")
            sa4 = 5
            ac4 = "w"
        elif ta4 == 2 and d4 <=90 and d4 >= 61:
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="red")
            ca4 = c.create_image(x4,y4,anchor=NW,image = r_ast_v,tag="red")
            sa4 = 0
            ac4 = "r"
        elif ta4 == 1 and d4 <=90 and d4 >= 61:
            a4= c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="red")
            ca4 = c.create_image(x4,y4,anchor=NW,image = r_ast_m,tag="red")
            sa4 = 0
            ac4 = "r"
        elif ta4 == 2 and d4 >= 91: 
            a4=c.create_rectangle(x4,y4,x4+100,y4+100,outline="",width=0,tag="gold")
            ca4 = c.create_image(x4,y4,anchor=NW,image = g_ast_v,tag="gold")
            sa4 = 10
            ac4 = "g"
        elif ta4 == 1 and d4 >= 91:
            a4=c.create_rectangle(x4,y4,x4+100,y4+50,outline="",width=0,tag="gold")
            ca4 = c.create_image(x4,y4,anchor=NW,image = g_ast_m,tag="gold")
            sa4 = 10
            ac4 = "g"

##       5. asteroid

        if ta5 == 1 and d5 <= 60:
            a5=c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="grey")
            ca5 = c.create_image(x5,y5,anchor=NW,image = w_ast_m,tag="grey")
            sa5 = 5
            ac5 = "w"
        elif ta5 == 2 and d5 <= 60:  
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="grey")
            ca5 = c.create_image(x5,y5,anchor=NW,image = w_ast_v,tag="grey")
            sa5 = 5
            ac5 = "w"
        elif ta5 == 2 and d5 <=90 and d5 >= 61:
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="red")
            ca5 = c.create_image(x5,y5,anchor=NW,image = r_ast_v,tag="red")
            sa5 = 0
            ac5 = "r"
        elif ta5 == 1 and d5 <=90 and d5 >= 61:
            a5= c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="red")
            ca5 = c.create_image(x5,y5,anchor=NW,image = r_ast_m,tag="red")
            sa5 = 0
            ac5 = "r"
        elif ta5 == 2 and d5 >= 91: 
            a5=c.create_rectangle(x5,y5,x5+100,y5+100,outline="",width=0,tag="gold")
            ca5 = c.create_image(x5,y5,anchor=NW,image = g_ast_v,tag="gold")
            sa5 = 10
            ac5 = "g"
        elif ta5 == 1 and d5 >= 91:
            a5=c.create_rectangle(x5,y5,x5+100,y5+50,outline="",width=0,tag="gold")
            ca5 = c.create_image(x5,y5,anchor=NW,image = g_ast_m,tag="gold")
            sa5 = 10
            ac5 = "g"

##       6. asteroid

        if ta6 == 1 and d6 <= 60:
            a6=c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="grey")
            ca6 = c.create_image(x6,y6,anchor=NW,image = w_ast_m,tag="grey")
            sa6 = 5
            ac6 = "w"
        elif ta6 == 2 and d6 <= 60:  
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="grey")
            ca6 = c.create_image(x6,y6,anchor=NW,image = w_ast_v,tag="grey")
            sa6 = 5
            ac6 = "w"
        elif ta6 == 2 and d6 <=90 and d6 >= 61:
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="red")
            ca6 = c.create_image(x6,y6,anchor=NW,image = r_ast_v,tag="red")
            sa6 = 0
            ac6 = "r"
        elif ta6 == 1 and d6 <=90 and d6 >= 61:
            a6= c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="red")
            ca6 = c.create_image(x6,y6,anchor=NW,image = r_ast_m,tag="red")
            sa6 = 0
            ac6 = "r"
        elif ta6 == 2 and d6 >= 91: 
            a6=c.create_rectangle(x6,y6,x6+100,y6+100,outline="",width=0,tag="gold")
            ca6 = c.create_image(x6,y6,anchor=NW,image = g_ast_v,tag="gold")
            sa6 = 10
            ac6 = "g"
        elif ta6 == 1 and d6 >= 91:
            a6=c.create_rectangle(x6,y6,x6+100,y6+50,outline="",width=0,tag="gold")
            ca6 = c.create_image(x6,y6,anchor=NW,image = g_ast_m,tag="gold")
            sa6 = 10
            ac6 = "g"

##       7. asteroid

        if ta7 == 1 and d7 <= 60:
            a7=c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="grey")
            ca7 = c.create_image(x7,y7,anchor=NW,image = w_ast_m,tag="grey")
            sa7 = 5
            ac7 = "w"
        elif ta7 == 2 and d7 <= 60:  
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="grey")
            ca7 = c.create_image(x7,y7,anchor=NW,image = w_ast_v,tag="grey")
            sa7 = 5
            ac7 = "w"
        elif ta7 == 2 and d7 <=90 and d7 >= 61:
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="red")
            ca7 = c.create_image(x7,y7,anchor=NW,image = r_ast_v,tag="red")
            sa7 = 0
            ac7 = "r"
        elif ta7 == 1 and d7 <=90 and d7 >= 61:
            a7= c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="red")
            ca7 = c.create_image(x7,y7,anchor=NW,image = r_ast_m,tag="red")
            sa7 = 0
            ac7 = "r"
        elif ta7 == 2 and d7 >= 91: 
            a7=c.create_rectangle(x7,y7,x7+100,y7+100,outline="",width=0,tag="gold")
            ca7 = c.create_image(x7,y7,anchor=NW,image = g_ast_v,tag="gold")
            sa7 = 10
            ac7 = "g"
        elif ta7 == 1 and d7 >= 91:
            a7=c.create_rectangle(x7,y7,x7+100,y7+50,outline="",width=0,tag="gold")
            ca7 = c.create_image(x7,y7,anchor=NW,image = g_ast_m,tag="gold")
            sa7 = 10
            ac7 = "g"

##       8. asteroid

        if ta8 == 1 and d8 <= 60:
            a8=c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="grey")
            ca8 = c.create_image(x8,y8,anchor=NW,image = w_ast_m,tag="grey")
            sa8 = 5
            ac8 = "w"
        elif ta8 == 2 and d8 <= 60:  
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="grey")
            ca8 = c.create_image(x8,y8,anchor=NW,image = w_ast_v,tag="grey")
            sa8 = 5
            ac8 = "w"
        elif ta8 == 2 and d8 <=90 and d8 >= 61:
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="red")
            ca8 = c.create_image(x8,y8,anchor=NW,image = r_ast_v,tag="red")
            sa8 = 0
            ac8 = "r"
        elif ta8 == 1 and d8 <=90 and d8 >= 61:
            a8= c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="red")
            ca8 = c.create_image(x8,y8,anchor=NW,image = r_ast_m,tag="red")
            sa8 = 0
            ac8 = "r"
        elif ta8 == 2 and d8 >= 91: 
            a8=c.create_rectangle(x8,y8,x8+100,y8+100,outline="",width=0,tag="gold")
            ca8 = c.create_image(x8,y8,anchor=NW,image = g_ast_v,tag="gold")
            sa8 = 10
            ac8 = "g"
        elif ta8 == 1 and d8 >= 91:
            a8=c.create_rectangle(x8,y8,x8+100,y8+50,outline="",width=0,tag="gold")
            ca8 = c.create_image(x8,y8,anchor=NW,image = g_ast_m,tag="gold")
            sa8 = 10
            ac8 = "g"

##       9. asteroid

        if ta9 == 1 and d9 <= 60:
            a9=c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="grey")
            ca9 = c.create_image(x9,y9,anchor=NW,image = w_ast_m,tag="grey")
            sa9 = 5
            ac9 = "w"
        elif ta9 == 2 and d9 <= 60:  
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="grey")
            ca9 = c.create_image(x9,y9,anchor=NW,image = w_ast_v,tag="grey")
            sa9 = 5
            ac9 = "w"
        elif ta9 == 2 and d9 <=90 and d9 >= 61:
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="red")
            ca9 = c.create_image(x9,y9,anchor=NW,image = r_ast_v,tag="red")
            sa9 = 0
            ac9 = "r"
        elif ta9 == 1 and d9 <=90 and d9 >= 61:
            a9= c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="red")
            ca9 = c.create_image(x9,y9,anchor=NW,image = r_ast_m,tag="red")
            sa9 = 0
            ac9 = "r"
        elif ta9 == 2 and d9 >= 91: 
            a9=c.create_rectangle(x9,y9,x9+100,y9+100,outline="",width=0,tag="gold")
            ca9 = c.create_image(x9,y9,anchor=NW,image = g_ast_v,tag="gold")
            sa9 = 10
            ac9 = "g"
        elif ta9 == 1 and d9 >= 91:
            a9=c.create_rectangle(x9,y9,x9+100,y9+50,outline="",width=0,tag="gold")
            ca9 = c.create_image(x9,y9,anchor=NW,image = g_ast_m,tag="gold")
            sa9 = 10
            ac9 = "g"

##       10. asteroid

        if ta10 == 1 and d10 <= 60:
            a10=c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="grey")
            ca10 = c.create_image(x10,y10,anchor=NW,image = w_ast_m,tag="grey")
            sa10 = 5
            ac10 = "w"
        elif ta10 == 2 and d10 <= 60:  
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="grey")
            ca10 = c.create_image(x10,y10,anchor=NW,image = w_ast_v,tag="grey")
            sa10 = 5
            ac10 = "w"
        elif ta10 == 2 and d10 <=90 and d10 >= 61:
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="red")
            ca10 = c.create_image(x10,y10,anchor=NW,image = r_ast_v,tag="red")
            sa10 = 0
            ac10 = "r"
        elif ta10 == 1 and d10 <=90 and d10 >= 61:
            a10= c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="red")
            ca10 = c.create_image(x10,y10,anchor=NW,image = r_ast_m,tag="red")
            sa10 = 0
            ac10 = "r"
        elif ta10 == 2 and d10 >= 91: 
            a10=c.create_rectangle(x10,y10,x10+100,y10+100,outline="",width=0,tag="gold")
            ca10 = c.create_image(x10,y10,anchor=NW,image = g_ast_v,tag="gold")
            sa10 = 10
            ac10 = "g"
        elif ta10 == 1 and d10 >= 91:
            a10=c.create_rectangle(x10,y10,x10+100,y10+50,outline="",width=0,tag="gold")
            ca10 = c.create_image(x10,y10,anchor=NW,image = g_ast_m,tag="gold")
            sa10 = 10
            ac10 = "g"

    ##pohyb asteroidov v tazkej obtiaznosti
    def loopinmovement_hard():
        global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
        global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10
        global y1,y2,y3,y4,y5,y6,y7,y8,y9,y10
        global sa1,sa2,sa3,sa4,sa5,sa6,sa7,sa8,sa9,sa10
        global ac1,ac2,ac3,ac4,ac5,ac6,ac7,ac8,ac9,ac10
        global ta1,ta2,ta3,ta4,ta5,ta6,ta7,ta8,ta9,ta10
        global ca1,ca2,ca3,ca4,ca5,ca6,ca7,ca8,ca9,ca10

#velkosť pohybu horizontálne(y) - tak trocha funguje- ide aj do mínusi(podla obtiažnosti) 
        y1mw=r.randint(0,3)
        x1mw=r.randint(-1,1)
        y1mr=r.randint(-10,11)
        x1mr=r.randint(-10,10)
    
        y2mw=r.randint(0,3)
        x2mw=r.randint(-1,1)
        y2mr=r.randint(-10,11)
        x2mr=r.randint(-10,10)
    
        y3mw=r.randint(0,3)
        x3mw=r.randint(-1,1)
        y3mr=r.randint(-10,11)
        x3mr=r.randint(-10,10)
    
        y4mw=r.randint(0,3)
        x4mw=r.randint(-1,1)
        y4mr=r.randint(-10,11)
        x4mr=r.randint(-10,10)
    
        y5mw=r.randint(0,3)
        x5mw=r.randint(-1,1)
        y5mr=r.randint(-10,11)
        x5mr=r.randint(-10,10)
    
        y6mw=r.randint(0,3)
        x6mw=r.randint(-1,1)
        y6mr=r.randint(-10,11)
        x6mr=r.randint(-10,10)
    
        y7mw=r.randint(0,3)
        x7mw=r.randint(-1,1)
        y7mr=r.randint(-10,11)
        x7mr=r.randint(-10,10)
    
        y8mw=r.randint(0,3)
        x8mw=r.randint(-1,1)
        y8mr=r.randint(-10,11)
        x8mr=r.randint(-10,10)
    
        y9mw=r.randint(0,3)
        x9mw=r.randint(-1,1)
        y9mr=r.randint(-10,11)
        x9mr=r.randint(-10,10)
    
        y10mw=r.randint(0,3)
        x10mw=r.randint(-1,1)
        y10mr=r.randint(-10,11)
        x10mr=r.randint(-10,10)
    
    #--------------------------------------pohyb-asteroidu--1-------------------------------------------------------------------#        
        if a1_d == 0 :
    #-pohyb-bieleho-asteroidu
        
            if ac1 == "w" :
                c.move(a1,x1mw,y1mw)
                c.move(ca1,x1mw,y1mw)
                y1 += y1mw
                x1 += x1mw
            
                if x1 <= 400 :
                    x1 += 10
                    c.move(a1,10,1)
                    c.move(ca1,10,1)
                elif x1 + 100 >= 1520 :
                    x1 -= 10
                    c.move(a1,-10,1)
                    c.move(ca1,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac1 == "r" :
                c.move(a1,x1mr,y1mr)
                c.move(ca1,x1mr,y1mr)
                y1 += y1mr
                x1 += x1mr
                if x1 <= 400 :
                    x1 += 10  
                    c.move(a1,10,1)
                    c.move(ca1,10,1)
                elif x1 + 100 >= 1520 :
                    x1 -= 10
                    c.move(a1,-10,1)
                    c.move(ca1,-10,1)

                    
                elif y1 <= 200  :
                    y1 += 10 
                    c.move(a1,0,10)
                    c.move(ca1,0,10)
                                        
                                        
    #-pohyb-zlatého-asteroidu           
            
            elif ac1 == "g" :
                tga = r.randint(1,100)
                c.move(a1,0,3)
                c.move(ca1,0,3)
                y1 += 5
                if  tga >= 1 and tga <= 5 and ta1 == 1   :
                    x1=r.randint(450,1300)
                    y1=r.randint(300,600)
                    c.coords(a1,x1,y1,x1+100,y1+50)
                    c.coords(ca1,x1,y1)

                elif tga >= 1 and tga <= 5 and ta1 == 2  :
                    x1=r.randint(450,1300)
                    y1=r.randint(300,600)
                    c.coords(a1,x1,y1,x1+100,y1+100)
                    c.coords(ca1,x1,y1)
                elif tga >= 6  :
                    pass
            
            if y3 + 50 >= 850 and ta3 == 1 :
                defeat()
            elif y3 + 100 >= 850 and ta3 == 2 :
                defeat()
        else:
            pass    
    #--------------------------------------pohyb-asteroidu--2-------------------------------------------------------------------#  
        if a2_d == 0 :
    #-pohyb-bieleho-asteroidu
        
            if ac2 == "w" :
                c.move(a2,x2mw,y2mw)
                c.move(ca2,x2mw,y2mw)
                y2 += y2mw
                x2 += x2mw
            
                if x2 <= 400 :
                    x2 += 10
                    c.move(a2,10,1)
                    c.move(ca2,10,1)
                elif x2 + 100 >= 1520 :
                    x2 -= 10
                    c.move(a2,-10,1)
                    c.move(ca2,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac2 == "r" :
                c.move(a2,x2mr,y2mr)
                c.move(ca2,x2mr,y2mr)
                y2 += y2mr
                x2 += x2mr
                if x2 <= 400 :
                    x2 += 10  
                    c.move(a2,10,1)
                    c.move(ca2,10,1)
                elif x2 + 100 >= 1520 :
                    x2 -= 10
                    c.move(a2,-10,1)
                    c.move(ca2,-10,1)

                elif y2 <= 200  :
                    y2 += 10 
                    c.move(a2,0,10)
                    c.move(ca2,0,10)                              
                                        
    #-pohyb-zlatého-asteroidu           
            
            elif ac2 == "g" :
                tga = r.randint(1,100)
                c.move(a2,0,3)
                c.move(ca2,0,3)
                y2 += 5
                if  tga >= 1 and tga <= 5 and ta2 == 1   :
                    x2=r.randint(450,1300)
                    y2=r.randint(300,600)
                    c.coords(a2,x2,y2,x2+100,y2+50)
                    c.coords(ca2,x2,y2)
                elif tga >= 1 and tga <= 5 and ta2 == 2  :
                    x1=r.randint(450,1300)
                    y1=r.randint(300,600)
                    c.coords(a2,x2,y2,x2+100,y2+100)
                    c.coords(ca2,x2,y2)

                elif tga >= 6  :
                    pass
        
            if y3 + 50 >= 850 and ta3 == 1 :
                defeat()
            elif y3 + 100 >= 850 and ta3 == 2 :
                defeat()
                
            else:
                pass   
    #--------------------------------------pohyb-asteroidu--3-------------------------------------------------------------------#  
        if a3_d == 0 :    
    #-pohyb-bieleho-asteroidu
        
            if ac3 == "w" :
                c.move(a3,x3mw,y3mw)
                c.move(ca3,x3mw,y3mw)
                y3 += y3mw
                x3 += x3mw
            
                if x3 <= 400 :
                    x3 += 10
                    c.move(a3,10,1)
                    c.move(ca3,10,1)
                elif x3 + 100 >= 1520 :
                    x3 -= 10
                    c.move(a3,-10,1)
                    c.move(ca3,-10,1)
            
            
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac3 == "r" :
                c.move(a3,x3mr,y3mr)
                c.move(ca3,x3mr,y3mr)
                y3 += y3mr
                x3 += x3mr
                if x3 <= 400 :
                    x3 += 10  
                    c.move(a3,10,1)
                    c.move(ca3,10,1)
                elif x3 + 100 >= 1520 :
                    x3 -= 10
                    c.move(a3,-10,1)
                    c.move(ca3,-10,1)

                    
                elif y3 <= 200  :
                    y3 += 10 
                    c.move(a3,0,10)
                    c.move(ca3,0,10)
            
            
    #-pohyb-zlatého-asteroidu           
            
            elif ac3 == "g" :
                tga = r.randint(1,100)
                c.move(a3,0,3)
                c.move(ca3,0,3)
                y3 += 5
                if  tga >= 1 and tga <= 5 and ta3 == 1   :
                    x3=r.randint(450,1300)
                    y3=r.randint(300,600)
                    c.coords(a3,x3,y3,x3+100,y3+50)
                    c.coords(ca3,x3,y3)
                if  tga >= 1 and tga <= 5 and ta3 == 2   :   
                    c.coords(a3,x3,y3,x3+100,y3+100)
                    c.coords(ca3,x3,y3)

                elif tga >= 6  :
                    pass
                            
            
            if y3 + 50 >= 850 and ta3 == 1 :
                defeat()
            elif y3 + 100 >= 850 and ta3 == 2 :
                defeat()
        
        else:
            pass        
                

    #--------------------------------------pohyb-asteroidu--4-------------------------------------------------------------------#  
        if a4_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac4 == "w" :
                c.move(a4,x4mw,y4mw)
                c.move(ca4,x4mw,y4mw)
                y4 += y4mw
                x4 += x4mw
            
                if x4 <= 400 :
                    x4 += 10
                    c.move(a4,10,1)
                    c.move(ca4,10,1)
                elif x4 + 100 >= 1520 :
                    x4 -= 10
                    c.move(a4,-10,1)
                    c.move(ca4,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac4 == "r" :
                c.move(a4,x4mr,y4mr)
                c.move(ca4,x4mr,y4mr)
                y4 += y4mr
                x4 += x4mr
                if x4 <= 400 :
                    x4 += 10  
                    c.move(a4,10,1)
                    c.move(ca4,10,1)
                elif x4 + 100 >= 1520 :
                    x4 -= 10
                    c.move(a4,-10,1)
                    c.move(ca4,-10,1)

                    
                elif y4 <= 200  :
                    y4 += 10 
                    c.move(a4,0,10)
                    c.move(ca4,0,10)
                                        
                                        
    #-pohyb-zlatého-asteroidu           
            
            elif ac4 == "g" :
                tga = r.randint(1,100)
                c.move(a4,0,3)
                c.move(ca4,0,3)
                y4 += 5
                if  tga >= 1 and tga <= 5 and ta4 == 1   :
                    x4=r.randint(450,1300)
                    y4=r.randint(300,600)
                    c.coords(a4,x4,y4,x4+100,y4+50)
                    c.coords(ca4,x4,y4)
                elif tga >= 1 and tga <= 5 and ta4 == 2  :
                        x4=r.randint(450,1300)
                        y4=r.randint(300,600)
                        c.coords(a4,x4,y4,x4+100,y4+100)
                        c.coords(ca4,x4,y4)
                elif tga >= 6  :
                    pass
                            
            
            if y4 + 50 >= 850 and ta4 == 1 :
                defeat()
            elif y4 + 100 >= 850 and ta4 == 2 :
                defeat()
        else:
            pass       
                
    #--------------------------------------pohyb-asteroidu--5-------------------------------------------------------------------#  
        if a5_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac5 == "w" :
                c.move(a5,x5mw,y5mw)
                c.move(ca5,x5mw,y5mw)
                y5 += y5mw
                x5 += x5mw
            
                if x5 <= 400 :
                    x5 += 10
                    c.move(a5,10,1)
                    c.move(ca5,10,1)
                elif x5 + 100 >= 1520 :
                    x5 -= 10
                    c.move(a5,-10,1)
                    c.move(ca5,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac5 == "r" :
                c.move(a5,x5mr,y5mr)
                c.move(ca5,x5mr,y5mr)
                y5 += y5mr
                x5 += x5mr
                if x5 <= 400 :
                    x5 += 10  
                    c.move(a5,10,1)
                    c.move(ca5,10,1)
                elif x5 + 100 >= 1520 :
                    x5 -= 10
                    c.move(a5,-10,1)
                    c.move(ca5,-10,1)

                    
                elif y5 <= 200  :
                    y5 += 10 
                    c.move(a5,0,10)
                    c.move(ca5,0,10)
                                        
    #-pohyb-zlatého-asteroidu           
                
            elif ac5 == "g" :
                tga = r.randint(1,100)
                c.move(a5,0,3)
                c.move(ca5,0,3)
                y5 += 5
                if  tga >= 1 and tga <= 5 and ta5 == 1   :
                    x5=r.randint(450,1300)
                    y5=r.randint(300,600)
                    c.coords(a5,x5,y5,x5+100,y5+50)
                    c.coords(ca5,x5,y5)
                elif tga >= 1 and tga <= 5 and ta5 == 2  :
                    x5=r.randint(450,1300)
                    y5=r.randint(300,600)
                    c.coords(a5,x5,y5,x5+100,y5+100)
                    c.coords(ca5,x5,y5)
                elif tga >= 6  :
                    pass
                            
            
            if y5 + 50 >= 850 and ta5 == 1 :
                defeat()
            elif y5 + 100 >= 850 and ta5 == 2 :
                defeat()
        else:
            pass        
    #--------------------------------------pohyb-asteroidu--6-------------------------------------------------------------------#       
        if a6_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac6 == "w" :
                c.move(a6,x6mw,y6mw)
                c.move(ca6,x6mw,y6mw)
                y6 += y6mw
                x6 += x6mw
            
                if x6 <= 400 :
                    x6 += 10
                    c.move(a6,10,1)
                    c.move(ca6,10,1)
                elif x6 + 100 >= 1520 :
                    x6 -= 10
                    c.move(a6,-10,1)
                    c.move(ca6,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac6 == "r" :
                c.move(a6,x6mr,y6mr)
                c.move(ca6,x6mr,y6mr)
                y6 += y6mr
                x6 += x6mr
                if x6 <= 400 :
                    x6 += 10  
                    c.move(a6,10,1)
                    c.move(ca6,10,1)
                elif x6 + 100 >= 1520 :
                    x6 -= 10
                    c.move(a6,-10,1)
                    c.move(ca6,-10,1)

                    
                elif y6 <= 200  :
                    y6 += 10 
                    c.move(a6,0,10)
                    c.move(ca6,0,10)
                                        
                                        
    #-pohyb-zlatého-asteroidu           
            
            elif ac6 == "g":
                tga = r.randint(1,100)
                c.move(a6,0,3)
                c.move(ca6,0,3)
                y6 += 5
                if  tga >= 1 and tga <= 5 and ta6 == 1   :
                    x6=r.randint(450,1300)
                    y6=r.randint(300,600)
                    c.coords(a6,x6,y6,x6+100,y6+50)
                    c.coords(ca6,x6,y6)
                elif tga >= 1 and tga <= 5 and ta6 == 2  :
                    x6=r.randint(450,1300)
                    y6=r.randint(300,600)
                    c.coords(a6,x6,y6,x6+100,y6+100)
                    c.coords(ca6,x6,y6)
                elif tga >= 6  :
                    pass
            
            if y6 + 50 >= 850 and ta6 == 1 :
                defeat()
            elif y6 + 100 >= 850 and ta6 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--7-------------------------------------------------------------------#  
        if a7_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac7 == "w" :
                c.move(a7,x7mw,y7mw)
                c.move(ca7,x7mw,y7mw)
                y7 += y7mw
                x7 += x7mw
            
                if x7 <= 400 :
                    x7 += 10
                    c.move(a7,10,1)
                    c.move(ca7,10,1)
                elif x7 + 100 >= 1520 :
                    x7 -= 10
                    c.move(a7,-10,1)
                    c.move(ca7,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac7 == "r" :
                c.move(a7,x7mr,y7mr)
                c.move(ca7,x7mr,y7mr)
                y7 += y7mr
                x7 += x7mr
                if x7 <= 400 :
                    x7 += 10  
                    c.move(a7,10,1)
                    c.move(ca7,10,1)
                elif x7 + 100 >= 1520 :
                    x7 -= 10
                    c.move(a7,-10,1)
                    c.move(ca7,-10,1)

                    
                elif y7 <= 200  :
                    y7 += 10 
                    c.move(a7,0,10)
                    c.move(ca7,0,10)
                            
    #-pohyb-zlatého-asteroidu          
                
            elif ac7 == "g" :
                tga = r.randint(1,100)
                c.move(a7,0,3)
                c.move(ca7,0,3)
                y7 += 5
                if  tga >= 1 and tga <= 5 and ta7 == 1   :
                    x1=r.randint(450,1300)
                    y1=r.randint(300,600)
                    c.coords(a7,x1,y1,x1+100,y1+50)
                    c.coords(ca7,x1,y1)
                    x7 = x1
                    y7 = y1
                elif tga >= 1 and tga <= 5 and ta7 == 2  :
                    x1=r.randint(450,1300)
                    y1=r.randint(300,600)
                    c.coords(a7,x1,y1,x1+100,y1+100)
                    c.coords(ca7,x1,y1)
                    x7 = x1
                    y7 = y1
                elif tga >= 6  :
                    pass
                
            if y7 + 50 >= 850 and ta7 == 1 :
                defeat()
            elif y7 + 100 >= 850 and ta7 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--8-------------------------------------------------------------------#  
        if a8_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac8 == "w" :
                c.move(a8,x8mw,y8mw)
                c.move(ca8,x8mw,y8mw)
                y8 += y8mw
                x8 += x8mw
            
                if x8 <= 400 :
                    x8 += 10
                    c.move(a8,10,1)
                    c.move(ca8,10,1)
                elif x8 + 100 >= 1520 :
                    x8 -= 10
                    c.move(a8,-10,1)
                    c.move(ca8,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac8 == "r" :
                c.move(a8,x8mr,y8mr)
                c.move(ca8,x8mr,y8mr)
                y8 += y8mr
                x8 += x8mr
                if x8 <= 400 :
                    x8 += 10  
                    c.move(a8,10,1)
                    c.move(ca8,10,1)
                elif x8 + 100 >= 1520 :
                    x8 -= 10
                    c.move(a8,-10,1)
                    c.move(ca8,-10,1)

                    
                elif y8 <= 200  :
                    y8 += 10 
                    c.move(a8,0,10)
                    c.move(ca8,0,10)
                                        
    #-pohyb-zlatého-asteroidu           
                
            elif ac8== "g" :
                tga = r.randint(1,100)
                c.move(a8,0,3)
                c.move(ca8,0,3)
                y8 += 5
                if  tga >= 1 and tga <=5  and ta8 == 1   :
                    x8=r.randint(450,1300)
                    y8=r.randint(300,600)
                    c.coords(a8,x8,y8,x8+100,y8+50)
                    c.coords(ca8,x8,y8)
                elif tga >= 1 and tga <= 5 and ta8 == 2  :
                    x8=r.randint(450,1300)
                    y8=r.randint(300,600)
                    c.coords(a8,x8,y8,x8+100,y8+100)
                    c.coords(ca8,x8,y8)
                elif tga >= 6  :
                    pass
                
            if y8 + 50 >= 850 and ta8 == 1 :
                defeat()
            elif y8 + 100 >= 850 and ta8 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--9-------------------------------------------------------------------#  
        if a9_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac9 == "w" :
                c.move(a9,x9mw,y9mw)
                c.move(ca9,x9mw,y9mw)
                y9 += y9mw
                x9 += x9mw
            
                if x9 <= 400 :
                    x9 += 10
                    c.move(a9,10,1)
                    c.move(ca9,10,1)
                elif x9 + 100 >= 1520 :
                    x9 -= 10
                    c.move(a9,-10,1)
                    c.move(ca9,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac9 == "r" :
                c.move(a9,x9mr,y9mr)
                c.move(ca9,x9mr,y9mr)
                y9 += y9mr
                x9 += x9mr
                if x9 <= 400 :
                    x9 += 10  
                    c.move(a9,10,1)
                    c.move(ca9,10,1)
                elif x9 + 100 >= 1520 :
                    x9 -= 10
                    c.move(a9,-10,1)
                    c.move(ca9,-10,1)

                    
                elif y9 <= 200  :
                    y9 += 10 
                    c.move(a9,0,10)
                    c.move(ca9,0,10)

    #-pohyb-zlatého-asteroidu           
                
            elif ac9 == "g" :
                tga = r.randint(1,100)
                c.move(a9,0,3)
                y9 += 5
                if  tga >= 1 and tga <=  5 and ta9 == 1   :
                    x9=r.randint(450,1300)
                    y9=r.randint(300,600)
                    c.coords(a9,x9,y9,x9+100,y9+50)
                elif tga >= 1 and tga <= 5 and ta9 == 2  :
                    x9=r.randint(450,1300)
                    y9=r.randint(300,600)
                    c.coords(a9,x9,y9,x9+100,y9+100)
                elif tga >= 6  :
                    pass
                
            if y9 + 50 >= 850 and ta9 == 1 :
                defeat()
            elif y9 + 100 >= 850 and ta9 == 2 :
                defeat()
        else:
            pass        
                
    #--------------------------------------pohyb-asteroidu--10-------------------------------------------------------------------#  
        if a10_d == 0 :        
    #-pohyb-bieleho-asteroidu
        
            if ac10 == "w" :
                c.move(a10,x10mw,y10mw)
                c.move(ca10,x10mw,y10mw)
                y10 += y10mw
                x10 += x10mw
            
                if x10 <= 400 :
                    x10 += 10
                    c.move(a10,10,1)
                    c.move(ca10,10,1)
                elif x10 + 100 >= 1520 :
                    x10 -= 10
                    c.move(a10,-10,1)
                    c.move(ca10,-10,1)
                                                
    #-pohyb-červeného-asteroidu  
            
            elif ac10 == "r" :
                c.move(a10,x10mr,y10mr)
                c.move(ca10,x10mr,y10mr)
                y10 += y10mr
                x10 += x10mr
                if x10 <= 400 :
                    x10 += 10  
                    c.move(a10,10,1)
                    c.move(ca10,10,1)
                elif x10 + 100 >= 1520 :
                    x10 -= 10
                    c.move(a10,-10,1)
                    c.move(ca10,-10,1)

                    
                elif y10 <= 200  :
                    y10 += 10 
                    c.move(a10,0,10)
                    c.move(ca10,0,10)
            
    #-pohyb-zlatého-asteroidu         
                
            elif ac10 == "g" :
                tga = r.randint(1,100)
                c.move(a10,0,3)
                c.move(ca10,0,3)
                y10 += 5
                if  tga >= 1 and tga <= 5 and ta10 == 1   :
                    x10=r.randint(450,1300)
                    y10=r.randint(300,600)
                    c.coords(a10,x10,y10,x10+100,y10+50)
                    c.coords(ca10,x10,y10)
                elif tga >= 1 and tga <= 5 and ta10 == 2  :
                    x10=r.randint(450,1300)
                    y10=r.randint(300,600)
                    c.coords(a10,x10,y10,x10+100,y10+100)
                    c.coords(ca10,x10,y10)
                elif tga >= 6  :
                    pass
                
            if y10 + 50 >= 850 and ta10 == 1 :
                defeat()
            elif y10 + 100 >= 850 and ta10 == 2 :
                defeat()  
        else:
            pass
                    

        c.update()
        c.after(20,loopinmovement_hard)

    ##kontrola kilizii asteroidov a striel
    def collision_check1():
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y1 >= ys1 and x1 <= xs1+5 <= x1+100:
                c.delete("missile1",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys2 and x1 <= xs2+5 <= x1+100:
                c.delete("missile2",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys3 and x1 <= xs3+5 <= x1+100:
                c.delete("missile3",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys4 and x1 <= xs4+5 <= x1+100:
                c.delete("missile4",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys5 and x1 <= xs5+5 <= x1+100:
                c.delete("missile5",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys6 and x1 <= xs6+5 <= x1+100:
                c.delete("missile6",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys7 and x1 <= xs7+5 <= x1+100:
                c.delete("missile7",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
            elif y1 >= ys8 and x1 <= xs8+5 <= x1+100:
                c.delete("missile8",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys9 and x1 <= xs9+5 <= x1+100:
                c.delete("missile9",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y1 >= ys10 and x1 <= xs10+5 <= x1+100:
                c.delete("missile10",a1,ca1)
                score += sa1
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check1)

    def collision_check2():
        global x2, y2
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y2 >= ys1 and x2 <= xs1+5 <= x2+100:
                c.delete("missile1",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys2 and x2 <= xs2+5 <= x2+100:
                c.delete("missile2",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys3 and x2 <= xs3+5 <= x2+100:
                c.delete("missile3",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys4 and x2 <= xs4+5 <= x2+100:
                c.delete("missile4",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys5 and x2 <= xs5+5 <= x2+100:
                c.delete("missile5",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys6 and x2 <= xs6+5 <= x2+100:
                c.delete("missile6",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys7 and x2 <= xs7+5 <= x2+100:
                c.delete("missile7",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys8 and x2 <= xs8+5 <= x2+100:
                c.delete("missile8",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys9 and x2 <= xs9+5 <= x2+100:
                c.delete("missile9",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y2 >= ys10 and x2 <= xs10+5 <= x2+100:
                c.delete("missile10",a2,ca2)
                score += sa2
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check2)

    def collision_check3():
        global x3, y3
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y3 >= ys1 and x3 <= xs1+5 <= x3+100:
                c.delete("missile1",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys2 and x3 <= xs2+5 <= x3+100:
                c.delete("missile2",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys3 and x3 <= xs3+5 <= x3+100:
                c.delete("missile3",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys4 and x3 <= xs4+5 <= x3+100:
                c.delete("missile4",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys5 and x3 <= xs5+5 <= x3+100:
                c.delete("missile5",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys6 and x3 <= xs6+5 <= x3+100:
                c.delete("missile6",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys7 and x3 <= xs7+5 <= x3+100:
                c.delete("missile7",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys8 and x3 <= xs8+5 <= x3+100:
                c.delete("missile8",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys9 and x3 <= xs9+5 <= x3+100:
                c.delete("missile9",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y3 >= ys10 and x3 <= xs10+5 <= x3+100:
                c.delete("missile10",a3,ca3)
                score += sa3
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check3)

    def collision_check4():
        global x4, y4
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y4 >= ys1 and x4 <= xs1+5 <= x4+100:
                c.delete("missile1",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys2 and x4 <= xs2+5 <= x4+100:
                c.delete("missile2",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys3 and x4 <= xs3+5 <= x4+100:
                c.delete("missile3",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys4 and x4 <= xs4+5 <= x4+100:
                c.delete("missile4",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys5 and x4 <= xs5+5 <= x4+100:
                c.delete("missile5",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys6 and x4 <= xs6+5 <= x4+100:
                c.delete("missile6",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys7 and x4 <= xs7+5 <= x4+100:
                c.delete("missile7",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys8 and x4 <= xs8+5 <= x4+100:
                c.delete("missile8",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys9 and x4 <= xs9+5 <= x4+100:
                c.delete("missile9",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y4 >= ys10 and x4 <= xs10+5 <= x4+100:
                c.delete("missile10",a4,ca4)
                score += sa4
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check4)

    def collision_check5():
        global x5, y5
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y5 >= ys1 and x5 <= xs1+5 <= x5+100:
                c.delete("missile1",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys2 and x5 <= xs2+5 <= x5+100:
                c.delete("missile2",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys3 and x5 <= xs3+5 <= x5+100:
                c.delete("missile3",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys4 and x5 <= xs4+5 <= x5+100:
                c.delete("missile4",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys5 and x5 <= xs5+5 <= x5+100:
                c.delete("missile5",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys6 and x5 <= xs6+5 <= x5+100:
                c.delete("missile6",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys7 and x5 <= xs7+5 <= x5+100:
                c.delete("missile7",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys8 and x5 <= xs8+5 <= x5+100:
                c.delete("missile8",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys9 and x5 <= xs9+5 <= x5+100:
                c.delete("missile9",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y5 >= ys10 and x5 <= xs10+5 <= x5+100:
                c.delete("missile10",a5,ca5)
                score += sa5
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check5)

    def collision_check6():
        global x6, y6
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y6 >= ys1 and x6 <= xs1+5 <= x6+100:
                c.delete("missile1",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys2 and x6 <= xs2+5 <= x6+100:
                c.delete("missile2",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys3 and x6 <= xs3+5 <= x6+100:
                c.delete("missile3",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys4 and x6 <= xs4+5 <= x6+100:
                c.delete("missile4",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys5 and x6 <= xs5+5 <= x6+100:
                c.delete("missile5",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys6 and x6 <= xs6+5 <= x6+100:
                c.delete("missile6",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys7 and x6 <= xs7+5 <= x6+100:
                c.delete("missile7",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys8 and x6 <= xs8+5 <= x6+100:
                c.delete("missile8",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys9 and x6 <= xs9+5 <= x6+100:
                c.delete("missile9",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y6 >= ys10 and x6 <= xs10+5 <= x6+100:
                c.delete("missile10",a6,ca6)
                score += sa6
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check6)

    def collision_check7():
        global x7, y7
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y7 >= ys1 and x7 <= xs1+5 <= x7+100:
                c.delete("missile1",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys2 and x7 <= xs2+5 <= x7+100:
                c.delete("missile2",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys3 and x7 <= xs3+5 <= x7+100:
                c.delete("missile3",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys4 and x7 <= xs4+5 <= x7+100:
                c.delete("missile4",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys5 and x7 <= xs5+5 <= x7+100:
                c.delete("missile5",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys6 and x7 <= xs6+5 <= x7+100:
                c.delete("missile6",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys7 and x7 <= xs7+5 <= x7+100:
                c.delete("missile7",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys8 and x7 <= xs8+5 <= x7+100:
                c.delete("missile8",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys9 and x7 <= xs9+5 <= x7+100:
                c.delete("missile9",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y7 >= ys10 and x7 <= xs10+5 <= x7+100:
                c.delete("missile10",a7,ca7)
                score += sa7
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check7)

    def collision_check8():
        global x8, y8,xs8
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y8 >= ys1 and x8 <= xs1+5 <= x8+100:
                c.delete("missile1",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys2 and x8 <= xs2+5 <= x8+100:
                c.delete("missile2",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys3 and x8 <= xs3+5 <= x8+100:
                c.delete("missile3",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys4 and x8 <= xs4+5 <= x8+100:
                c.delete("missile4",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys5 and x8 <= xs5+5 <= x8+100:
                c.delete("missile5",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys6 and x8 <= xs6+5 <= x8+100:
                c.delete("missile6",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys7 and x8 <= xs7+5 <= x8+100:
                c.delete("missile7",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys8 and x8 <= xs8+5 <= x8+100:
                c.delete("missile8",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys9 and x8 <= xs9+5 <= x8+100:
                c.delete("missile9",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y8 >= ys10 and x8 <= xs10+5 <= x8+100:
                c.delete("missile10",a8,ca8)
                score += sa8
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check8)

    def collision_check9():
        global x9, y9,xs9
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y9 >= ys1 and x9 <= xs1+5 <= x9+100:
                c.delete("missile1",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys2 and x9 <= xs2+5 <= x9+100:
                c.delete("missile2",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys3 and x9 <= xs3+5 <= x9+100:
                c.delete("missile3",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys4 and x9 <= xs4+5 <= x9+100:
                c.delete("missile4",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys5 and x9 <= xs5+5 <= x9+100:
                c.delete("missile5",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys6 and x9 <= xs6+5 <= x9+100:
                c.delete("missile6",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys7 and x9 <= xs7+5 <= x9+100:
                c.delete("missile7",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys8 and x9 <= xs8+5 <= x9+100:
                c.delete("missile8",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys9 and x9 <= xs9+5 <= x9+100:
                c.delete("missile9",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y9 >= ys10 and x9 <= xs10+5 <= x9+100:
                c.delete("missile10",a9,ca9)
                score += sa9
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check9)

    def collision_check10():
        global x10, y10
        global score,asteroids_destroyed
        if asteroids_destroyed < 10:
            if y10 >= ys1 and x10 <= xs1+5 <= x10+100:
                c.delete("missile1",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys2 and x10 <= xs2+5 <= x10+100:
                c.delete("missile2",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys3 and x10 <= xs3+5 <= x10+100:
                c.delete("missile3",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys4 and x10 <= xs4+5 <= x10+100:
                c.delete("missile4",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys5 and x10 <= xs5+5 <= x10+100:
                c.delete("missile5",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys6 and x10 <= xs6+5 <= x10+100:
                c.delete("missile6",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys7 and x10 <= xs7+5 <= x10+100:
                c.delete("missile7",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys8 and x10 <= xs8+5 <= x10+100:
                c.delete("missile8",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys9 and x10 <= xs9+5 <= x10+100:
                c.delete("missile9",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            elif y10 >= ys10 and x10 <= xs10+5 <= x10+100:
                c.delete("missile10",a10,ca10)
                score += sa10
                asteroids_destroyed += 1
                update_ammo()
                return
            c.update()
            c.after(10,collision_check10)

    ##strialanie striel
    def bullet_spawn_n_movement(event):
        global xs,ys,ys1,ys2,ys3,ys4,ys5,ys6,ys7,ys8,ys9,ys10
        global xs1,xs2,xs3,xs4,xs5,xs6,xs7,xs8,xs9,xs10,shot_counter,ammo

        if shot_counter < 11:
            shot_counter += 1
            ammo -= int(1)
            if shot_counter == 1:
                xs1 = xs+40
                c.create_rectangle(xs1+4, ys-60, xs1+15, ys, tag="missile1", outline="",width=0)
                c.create_image(xs1+5,ys-60,anchor=NW,image = missile,tag="missile1")
                update_ammo()
                collision_check1()
                def loopinmovement1():
                    global ys1
                    if ys1 <= 200:
                        c.delete("missile1")
                        return
                    else:
                        c.move("missile1", 0, -20)
                        ys1 -= 20
                        c.update()
                        c.after(20,loopinmovement1)
                loopinmovement1()

            elif shot_counter == 2:
                xs2 = xs+40
                c.create_rectangle(xs2+4, ys-60, xs2+15, ys, tag="missile2", outline="",width=0)
                c.create_image(xs2+5,ys-60,anchor=NW,image = missile,tag="missile2")
                update_ammo()
                collision_check2()
                def loopinmovement2():
                    global ys2
                    if ys2 <= 200:
                        c.delete("missile2")
                        return
                    else:
                        c.move("missile2", 0, -20)
                        ys2 -= 20
                        c.update()
                        c.after(20,loopinmovement2)
                loopinmovement2()

            elif shot_counter == 3:
                xs3 = xs+40
                c.create_rectangle(xs3+4, ys-60, xs3+15, ys, tag="missile3", outline="",width=0)
                c.create_image(xs3+5,ys-60,anchor=NW,image = missile,tag="missile3")
                update_ammo()
                collision_check3()
                def loopinmovement3():
                    global ys3
                    if ys3 <= 200:
                        c.delete("missile3")
                        return
                    else:
                        c.move("missile3", 0, -20)
                        ys3 -= 20
                        c.update()
                        c.after(20,loopinmovement3)
                loopinmovement3()

            elif shot_counter == 4:
                xs4 = xs+40
                c.create_rectangle(xs4+4, ys-60, xs4+15, ys, tag="missile4", outline="",width=0)
                c.create_image(xs4+5,ys-60,anchor=NW,image = missile,tag="missile4")
                update_ammo()
                collision_check4()
                def loopinmovement4():
                    global ys4
                    if ys4 <= 200:
                        c.delete("missile4")
                        return
                    else:
                        c.move("missile4", 0, -20)
                        ys4 -= 20
                        c.update()
                        c.after(20,loopinmovement4)
                loopinmovement4()

            elif shot_counter == 5:
                xs5 = xs+40
                c.create_rectangle(xs5+4, ys-60, xs5+15, ys, tag="missile5", outline="",width=0)
                c.create_image(xs5+5,ys-60,anchor=NW,image = missile,tag="missile5")
                update_ammo()
                collision_check5()
                def loopinmovement5():
                    global ys5
                    if ys5 <= 200:
                        c.delete("missile5")
                        return
                    else:
                        c.move("missile5", 0, -20)
                        ys5 -= 20
                        c.update()
                        c.after(20,loopinmovement5)
                loopinmovement5()

            elif shot_counter == 6:
                xs6 = xs+40
                c.create_rectangle(xs6+4, ys-60, xs6+15, ys, tag="missile6", outline="",width=0)
                c.create_image(xs6+5,ys-60,anchor=NW,image = missile,tag="missile6")
                update_ammo()
                collision_check6()
                def loopinmovement6():
                    global ys6
                    if ys6 <= 200:
                        c.delete("missile6")
                        return
                    else:
                        c.move("missile6", 0, -20)
                        ys6 -= 20
                        c.update()
                        c.after(20,loopinmovement6)
                loopinmovement6()

            elif shot_counter == 7:
                xs7 = xs+40
                c.create_rectangle(xs7+4, ys-60, xs7+15, ys, tag="missile7", outline="",width=0)
                c.create_image(xs7+5,ys-60,anchor=NW,image = missile,tag="missile7")
                update_ammo()
                collision_check7()
                def loopinmovement7():
                    global ys7
                    if ys7 <= 200:
                        c.delete("missile7")
                        return
                    else:
                        c.move("missile7", 0, -20)
                        ys7 -= 20
                        c.update()
                        c.after(20,loopinmovement7)
                loopinmovement7()

            elif shot_counter == 8:
                xs8 = xs+40
                c.create_rectangle(xs8+4, ys-60, xs8+15, ys, tag="missile8", outline="",width=0)
                c.create_image(xs8+5,ys-60,anchor=NW,image = missile,tag="missile8")
                update_ammo()
                collision_check8()
                def loopinmovement8():
                    global ys8
                    if ys8 <= 200:
                        c.delete("missile8")
                        return
                    else:
                        c.move("missile8", 0, -20)
                        ys8 -= 20
                        c.update()
                        c.after(20,loopinmovement8)
                loopinmovement8()

            elif shot_counter == 9:
                xs9 = xs+40
                c.create_rectangle(xs9+4, ys-60, xs9+15, ys, tag="missile9", outline="",width=0)
                c.create_image(xs9+5,ys-60,anchor=NW,image = missile,tag="missile9")
                update_ammo()
                collision_check9()
                def loopinmovement9():
                    global ys9
                    if ys9 <= 200:
                        c.delete("missile9")
                        return
                    else:
                        c.move("missile9", 0, -20)
                        ys9 -= 20
                        c.update()
                        c.after(20,loopinmovement9)
                loopinmovement9()

            elif shot_counter == 10:
                xs10 = xs+40
                c.create_rectangle(xs10+4, ys-60, xs10+15, ys, tag="missile10", outline="",width=0)
                c.create_image(xs10+5,ys-60,anchor=NW,image = missile,tag="missile10")
                update_ammo()
                collision_check10()
                def loopinmovement10():
                    global ys10
                    if ys10 <= 200:
                        c.delete("missile10")
                        return
                    else:
                        c.move("missile10", 0, -20)
                        ys10 -= 20
                        c.update()
                        c.after(20,loopinmovement10)
                loopinmovement10()

        elif shot_counter == 11:
            pass


    ##vyvolavanie funkcii
    if difficuilty == "easy":
        planetoids_spawn_easy()
        loopinmovement_easy()
    elif difficuilty == "medium":
        planetoids_spawn_medium()
        loopinmovement_medium()
    elif difficuilty == "hard":
        planetoids_spawn_hard()
        loopinmovement_hard()

    score_check()
    update_timer()
    border_spawn()
    update_ammo()
    ship_spawn()

    c.bind("<Button-1>",bullet_spawn_n_movement)
    c.bind_all("<a>",ship_left)
    c.bind_all("<d>",ship_right)

MainMenu()

c.mainloop()




































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































##https://www.youtube.com/watch?v=8ybW48rKBME&themeRefresh=1 - python tutorial s fetacky dobrymi informaciami
##semió
##a m n l v