from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
from tools import play_music, play_music2, play_music3, play_music4, check_entry, generate_number

generated_number = 0
attempts_number  = 0

def set_chances(num_chances):
    
    play_music()
    chances.configure(state='normal')
    chances.delete(0,END)
    chances.insert(0, num_chances)
    chances.configure(state=DISABLED)

def rang1_clicked():

    global generated_number, attempts_number
    range1.configure(bg="orange", state=DISABLED)
    range2.configure(bg="black", state=DISABLED)
    range3.configure(bg="black", state=DISABLED)
    number.configure(state='normal')
    check.configure(state="normal")
    set_chances(3)
    generated_number = generate_number(1)
    attempts_number  = 3
    

def rang2_clicked():

    global generated_number, attempts_number
    range1.configure(bg="black", state=DISABLED)
    range2.configure(bg="orange", state=DISABLED)
    range3.configure(bg="black", state=DISABLED)
    number.configure(state='normal')
    check.configure(state="normal")
    set_chances(4)
    generated_number = generate_number(2)
    attempts_number  = 4
    

def rang3_clicked():

    global generated_number, attempts_number
    range1.configure(bg="black", state=DISABLED)
    range2.configure(bg="black", state=DISABLED)
    range3.configure(bg="orange", state=DISABLED)
    number.configure(state='normal')
    check.configure(state="normal")
    set_chances(7)
    generated_number = generate_number(3)
    attempts_number  = 7
    

def new_game_func():

    play_music()
    range1.configure(bg="Green", state='normal')
    range2.configure(bg="Green", state='normal')
    range3.configure(bg="Green", state='normal')
    number.configure(state=DISABLED)
    check.configure(state=DISABLED)
    set_chances("")

    attempts.configure(state='normal')
    attempts.delete(1.0,END)
    attempts.insert(INSERT, "")
    attempts.configure(state=DISABLED)

    hints.configure(state="normal") 
    hints.delete('1.0', END)
    hints.insert(INSERT, "")
    hints.configure(state=DISABLED)

    number.configure(state='normal')
    number.delete(0,END)
    number.insert(0, "")
    number.configure(state=DISABLED)

def exit_game():
    play_music()
    exit()

def read_entry():

    
    value = number.get()
    global generated_number, attempts_number

    if(attempts_number > 0 ):

        if(check_entry(value)):
            value = int(value)
            if(value == generated_number):
                play_music3()
                messagebox.showinfo("Success", "Congratulations you win")
                new_game_func()

            else:

                play_music2()                                 

                if(value > generated_number):
                    hints.configure(state="normal") 
                    hints.delete('1.0', END)
                    hints.insert(INSERT, "The number is less than "+str(value)+"\n")
                    hints.configure(state=DISABLED)

                elif(value < generated_number):
                    hints.configure(state="normal") 
                    hints.delete('1.0', END)
                    hints.insert(INSERT, "The number is grater than "+str(value)+"\n")
                    hints.configure(state=DISABLED) 
                
                attempts.configure(state="normal")
                attempts.insert(INSERT, str(value)+", ")
                attempts.configure(state=DISABLED)

                attempts_number -= 1
                chances.configure(state='normal')
                chances.delete(0,END)
                chances.insert(0, attempts_number)
                chances.configure(state=DISABLED)


        else:
            messagebox.showerror("Error message", "Invalid input !, you must enter an integer number")

    else:
        play_music4()
        messagebox.showwarning("Error message", "No chances, you lose !")
        new_game_func()



if __name__ == "__main__":
        
        window = Tk()

        window.title("Guess the number")
        window.configure(width=585, height=500)
        window.configure(bg='lightgray')
        window.eval('tk::PlaceWindow . center')
        window.resizable(False, False)

        canvas1 = Canvas(window, width=585, height=330, bg='white')
        canvas1.pack(fill = "both", expand = True)
        img = ImageTk.PhotoImage(Image.open("bg.jpg")) 
        canvas1.create_image( 0, 0, image = img, anchor = "nw")

        range1 = Button(canvas1, text="1 to 10", width=15, font=("Helvetica", 11), bg="Green", fg="White", command=rang1_clicked)
        range1.place(x=50,y=20)

        range2 = Button(canvas1, text="1 to 100", width=15, font=("Helvetica", 11), bg="Green", fg="White", command=rang2_clicked)
        range2.place(x=230,y=20)

        range3 = Button(canvas1, text="1 to 1000", width=15, font=("Helvetica", 11), bg="Green", fg="White", command=rang3_clicked)
        range3.place(x=410,y=20)

        canvas1.create_text(230, 80, text="You have ", fill="Yellow", font=('Helvetica 13 bold'))
        chances = Entry(canvas1, width=2, font=("Helvetica", 14))
        chances.place(x=275,y=70)
        chances.configure(state=DISABLED)
        canvas1.create_text(350, 80, text="Chances", fill="Yellow", font=('Helvetica 13 bold'))

        canvas1.create_text(195, 122, text="Enter the number:", fill="Yellow", font=('Helvetica 13 bold'))
        number = Entry(canvas1, width=8, font=("Helvetica", 14))   
        number.configure(state=DISABLED)
        number.place(x=275,y=110)

        check = Button(canvas1, text="Check", width=10, font=("Helvetica", 11), bg="blue", fg="White", command=read_entry)
        check.configure(state=DISABLED)
        check.place(x=380,y=110)

        canvas1.create_text(65, 240, text="Attempts", fill="Yellow", font=('Helvetica 13 bold'))
        attempts = Text(canvas1, width=49, height=1, font=("Helvetica", 14))
        attempts.configure(state=DISABLED)   
        attempts.place(x=32,y=260)

        canvas1.create_text(55, 170, text="Hints", fill="Yellow", font=('Helvetica 13 bold'))
        hints = Text(canvas1, width=25, height=1, font=("Helvetica", 14))   
        hints.configure(state=DISABLED) 
        hints.place(x=32,y=190)

        new_game = Button(canvas1, text="New Game", width=10, font=("Helvetica", 11), bg="Gray", fg="black", command=new_game_func)
        new_game.place(x=350,y=190)

        exitg = Button(canvas1, text="Exit Game", width=10, font=("Helvetica", 11), bg="Gray", fg="black", command=exit_game)
        exitg.place(x=470,y=190)

        window.mainloop()

