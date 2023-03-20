import random
from re import I
from tkinter import*   
from tkinter import messagebox

import tkinter as tk  



# Define the paths to the text files containing the idioms
ENG_FILE = "eng_lan.txt"
RUS_FILE = "rus_lan.txt" 



idioms={}
#function call transation idiom. Takes an idiom as an argument and returns translation 
#in the other language. Works by opening two files
# It reads the idioms from both files simultaneously using zip()
# and compares each idiom with the given idiom. If a match is found, it returns the 
# corresponding idiom from the other file.
def translate_idiom(idiom):
    with open(ENG_FILE, 'r', encoding='utf-8-sig') as eng_file:
        with open(RUS_FILE, 'r', encoding='utf-8-sig') as rus_file:
            for eng, rus in zip(eng_file, rus_file):
                if eng.strip() == idiom:
                    return rus.strip()
                elif rus.strip() == idiom:
                    return eng.strip()
    return "Idiom not found"
# Create the function for the button
def on_translate():
    idiom = entry.get().strip()
    translation = translate_idiom(idiom)
    result_label.config(text=translation)

root = Tk()
root.geometry('400x600')
root.title("English-Russian translation")

# Create the input field
entry = Entry(root)
entry.pack()

# Create the translate button
translate_button = Button(root, text="Translate", command=on_translate)
translate_button.pack()

# Create the label for the translation result
result_label = Label(root, text="", font='Italic 15')
result_label.pack() 

results_label = tk.Label(root, text="", font='Italic 15')
results_label.pack()

# Create a label for the add entry
add_label = tk.Label(root, text="Add a new word:")
add_label.pack()
# Create the input fields for English and Russian idioms
eng_lbl = tk.Label(root, text="Eng", padx=5, pady=5)
eng_lbl.pack(padx=10, pady=5, fill="both")
eng_entry = Entry(root)
eng_entry.pack()
rus_lbl = tk.Label(root, text="Rus", padx=5, pady=5)
rus_lbl.pack(padx=10, pady=5, fill="both")
rus_entry = Entry(root)
rus_entry.pack()
# Define a function to handle adding a new idiom
def add_idiom():
    # Get the new idioms from the entries
    new_eng_idiom = eng_entry.get().strip()
    new_rus_idiom = rus_entry.get().strip()

    # Add the new idioms to the dictionary and the text files
    if new_eng_idiom and new_rus_idiom:
        idioms[new_eng_idiom.lower()] = new_rus_idiom.lower()
        with open(ENG_FILE, "a", encoding="utf-8-sig") as f_eng, open(RUS_FILE, "a", encoding="utf-8-sig") as f_rus:
            f_eng.write(new_eng_idiom.lower() + "\n")
            f_rus.write(new_rus_idiom.lower() + "\n")

        # Clear the entries and show a success message
        eng_entry.delete(0, tk.END)
        rus_entry.delete(0, tk.END)
        results_label.config(text="Idiom added successfully!")
    else:
        results_label.config(text="Please enter an idiom in both languages to add.")
        
def quiz():
    with open('eng_lan.txt', encoding='utf-8-sig') as f:
        eng = [line.strip() for line in f.readlines()]
    with open('rus_lan.txt', encoding='utf-8-sig') as f:
        rus = [line.strip() for line in f.readlines()]
    words = dict(zip(eng, rus))
    random_idioms = random.sample(eng, 4)
    score = 0

    def check_answer(entry, word):
        nonlocal score
        answer = entry.get().strip()
        expected_answer = words[word]
        if answer == expected_answer:
            result_lbl=tk.Label(root, text='Correct!', fg='Green', font='Times 25')
            result_lbl.pack(side='bottom')
            
            score += 1
        else:
            result_lbl1=tk.Label(root, text='Incorrect!',fg='Red',font='Cmabria 25')
            result_lbl1.pack(side='bottom')
        messagebox.showinfo("Expected answer:",f" {expected_answer}")
        print(f"Your answer: {answer}")
        if len(random_idioms) > 0:
            ask_question()
        else:
            print(f'You scored {score}')
    
    def ask_question():
        word = random_idioms.pop()
        label = Label(root, text=f'What is the word "{word}" in Russian?: ')
        label.pack()
        entry = Entry(root)
        entry.pack()
        button = Button(root, text='Submit', command=lambda: check_answer(entry, word))
        button.pack()
        
    for i, idiom in enumerate(random_idioms): 
        ask_question()

add_button = tk.Button(root, text="Add", command=add_idiom)
add_button.pack()
quiz_button = Button(root, text='Start quiz', command=quiz)
quiz_button.pack()

root.mainloop()
