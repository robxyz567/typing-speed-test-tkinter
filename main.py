from tkinter import *
import random
from datetime import datetime


def start_count_down(count):
    global text, total_words, total_chars, word_counter, index

    if count == 3:

        word_counter = 0
        index = 0
        total_words = 0
        total_chars = 0

        words_list = list(open('english_words.txt'))
        text = []
        for i in range(100):
            text.append(random.choice(words_list).replace('\n', ''))

        text_label1.config(text=text[0:1], fg='black')
        text_label2.config(text=text[1:2], fg='black')
        text_label3.config(text=text[2:3], fg='black')
        text_label4.config(text=text[3:4], fg='black')
        text_label5.config(text=text[4:5], fg='black')
        text_label6.config(text=text[5:6], fg='black')

    message_label.config(text=f"Time do start: {count}", fg='#FF6D6D')
    if count > 0:
        window.after(1000, start_count_down, count-1)
    elif count == 0:
        typing()
        typing_count_down(60)
        text_entry.focus()


def typing_count_down(seconds):

    if seconds != 0:
        message_label.config(text=f"Seconds to end: {seconds}", fg='black')
    if seconds > 0:
        window.after(1000, typing_count_down, seconds-1)


def typing():

    def checking(*args):
        global word_counter, index

        words = text_entry.get().split()
        if len(words) > 0:
            if words[-1] in text[index:index + 6]:

                if words[-1] == "".join(text[index:index + 1]):
                    text_label1.config(fg='#9AE66E')
                elif words[-1] == "".join(text[index + 1:index + 2]):
                    text_label2.config(fg='#9AE66E')
                elif words[-1] == "".join(text[index + 2:index + 3]):
                    text_label3.config(fg='#9AE66E')
                elif words[-1] == "".join(text[index + 3:index + 4]):
                    text_label4.config(fg='#9AE66E')
                elif words[-1] == "".join(text[index + 4:index + 5]):
                    text_label5.config(fg='#9AE66E')
                elif words[-1] == "".join(text[index + 5:index + 6]):
                    text_label6.config(fg='#9AE66E')

                word_counter += 1
                if word_counter == 6 and len(words) == 6:           # cheating by pressing spacerbar
                    index += 6
                    text_label1.config(text=text[index:index + 1], fg='black')
                    text_label2.config(text=text[index + 1:index + 2], fg='black')
                    text_label3.config(text=text[index + 2:index + 3], fg='black')
                    text_label4.config(text=text[index + 3:index + 4], fg='black')
                    text_label5.config(text=text[index + 4:index + 5], fg='black')
                    text_label6.config(text=text[index + 5:index + 6], fg='black')

                    text_entry.delete(0, 'end')
                    word_counter = 0
        window.bind('<space>', checking)

    checking()
    window.after(60000, calculate_result)


def calculate_result():
    global total_words, total_chars

    message_label.focus()
    text_entry.delete(0, 'end')
    total_words = index + word_counter

    total_chars = 0
    for word in text[:total_words]:
        total_chars += len(word)

    message_label.config(text=f"Words/chars per min: {total_words}/{total_chars}", fg='#FF6D6D')


def save():

    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")

    try:
        with open('results.txt', 'a') as file:
            file.write(f'{now}, Words/chars per min: {total_words}/{total_chars}\n')
    except NameError:
        message_label.config(text="No results to save")


def quiting():

    window.destroy()


word_counter = 0
index = 0

window = Tk()
window.title("Typing test")
window.config(padx=50, pady=25, bg='#F2EDD7')

logo_label = Label(height=2, text="TYPING SPEED TEST APP", font=('Arial', 18, "bold"), bg='#F2EDD7')
logo_label.grid(row=0, column=0, columnspan=6)

text_label1 = Label(height=2, width=9, font=('Arial', 13), bg='#F2EDD7')
text_label1.grid(row=2, column=0)
text_label2 = Label(height=2, width=9, font=('Arial', 13), bg='#F2EDD7')
text_label2.grid(row=2, column=1)
text_label3 = Label(height=2, width=9, font=('Arial', 13), bg='#F2EDD7')
text_label3.grid(row=2, column=2)
text_label4 = Label(height=2, width=9, font=('Arial', 13), bg='#F2EDD7')
text_label4.grid(row=2, column=3)
text_label5 = Label(height=2, width=9, font=('Arial', 13), bg='#F2EDD7')
text_label5.grid(row=2, column=4)
text_label6 = Label(height=2, width=9, font=('Arial', 13), bg='#F2EDD7')
text_label6.grid(row=2, column=5)

message_label = Label(height=2, text="Waiting ...", font=('Arial', 14, "bold"), bg='#F2EDD7')
message_label.grid(row=1, column=3, columnspan=3)

text_entry = Entry(width=96)
text_entry.grid(row=3, column=0, columnspan=6)

start_button = Button(height=1, width=9, text="START", font=('Arial', 12, "bold"), bg='#9AE66E', command=lambda: start_count_down(3))
start_button.grid(row=1, column=0)
save_button = Button(height=1, width=9, text="SAVE", font=('Arial', 12, "bold"), bg='#84DFFF', command=save)
save_button.grid(row=1, column=1)
quit_button = Button(height=1, width=9, text="QUIT", font=('Arial', 12, "bold"), bg='#FF6D6D', command=quiting)
quit_button.grid(row=1, column=2)


window.mainloop()
