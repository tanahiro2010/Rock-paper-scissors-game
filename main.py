# import
import random
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog

tk.Tk().withdraw()
messagebox.showinfo('game', "じゃんけんgameスタート!")

def msbox(title, main):
    tk.Tk().withdraw()
    messagebox.showinfo(title, main)

def nybox(title, main):
    tk.Tk().withdraw()
    A = simpledialog.askinteger(title, main)




# main program
while True:
    teki = random.randint(1, 3)  
    print(teki)
    tk.Tk().withdraw()
    x = simpledialog.askstring('じゃんけんgame', 'グーなら1、チョキなら2，パーなら3を入力してください')
    if teki == 1:
        if x == 1:
            tk.Tk().withdraw()
            messagebox.showinfo("惜しい！あと一押し","あいこです")
    
        if x == 2:
            tk.Tk().withdraw()
            messagebox.showinfo("残念","あなたの負けです")

        if x == 3:
            tk.Tk().withdraw()
            messagebox.showinfo("おめでとう！","あなたは勝利しました！おめでとう")

    elif teki == 2:
        if x == 1:
            tk.Tk().withdraw()
            messagebox.showinfo("おめでとう！","あなたは勝利しました！おめでとう")
    
        elif x == 2:
            tk.Tk().withdraw()
            messagebox.showinfo("惜しい！あと一押し","あいこです")

        else:
            tk.Tk().withdraw()
            messagebox.showinfo("残念", "残念、あなたの負けです")

    else:
        if x == 1:
            tk.Tk().withdraw()
            messagebox.showinfo("残念", "残念、あなたの負けです")
    
        elif x == 2:
            tk.Tk().withdraw()
            messagebox.showinfo("おめでとう！","あなたは勝利しました！おめでとう")

        else:
            tk.Tk().withdraw()
            messagebox.showinfo("惜しい！あと一押し","あいこです")

    #2回目から
    vs = ""
    print(vs)
    _random_ = random.randint(1, 3)
    print(_random_)

    tk.Tk().withdraw()
    messagebox.showinfo("2回戦","第2回戦スタート‼")
    while vs != 0:
        tk.Tk().withdraw()
        x = simpledialog.askstring('じゃんけんgame', 'グーなら1、チョキなら2，パーなら3を入力してください')

        if _random_ == 1:
            if x == 1:
                tk.Tk().withdraw()
                messagebox.showinfo("惜しい！あと一押し","あいこです")

            elif x == 2:
                tk.Tk().withdraw()
                messagebox.showinfo("残念", "残念、あなたの負けです")
 
            else:              
                tk.Tk().withdraw()
                messagebox.showinfo("おめでとう！","あなたは勝利しました！おめでとう")

        if _random_ == 2:
            if x == 1:
                tk.Tk().withdraw()
                messagebox.showinfo("おめでとう！","あなたは勝利しました！おめでとう")
    
            elif x == 2:
                tk.Tk().withdraw()
                messagebox.showinfo("惜しい！あと一押し","あいこです")

            else:
                tk.Tk().withdraw()
                messagebox.showinfo("残念", "残念、あなたの負けです")

        elif _random_ == 3:
            if x == 1:
                tk.Tk().withdraw()
                messagebox.showinfo("残念", "残念、あなたの負けです")
    
            elif x == 2:
                tk.Tk().withdraw()
                messagebox.showinfo("おめでとう！","あなたは勝利しました！おめでとう")

            else:
                tk.Tk().withdraw()
                messagebox.showinfo("惜しい！あと一押し","あいこです")


        else:
            tk.Tk().withdraw()
            messagebox.showinfo("惜しい！あと一押し","あいこです")

