from tkinter import Tk, Label, Entry, W, E, EW, Button, Listbox, Checkbutton, Frame, SINGLE, IntVar, messagebox
import os

root = Tk()
root.geometry("700x500")
root.title('Form')
root.configure(background='#004e10')
root.resizable(0,0)


students_data = []


game_dev_var = IntVar()
ai_var = IntVar()
uiux_var = IntVar()


FILE_PATH = "student_label.txt"

def save_to_file():
    """Funksioni që ruan të gjitha regjistrimet në file"""
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.write("SUMMER SCHOOL REGISTRATIONS\n")
            file.write("="*60 + "\n\n")
            for i, student in enumerate(students_data, 1):
                file.write(f"{i}. {student}\n")
            file.write("\n" + "="*60 + "\n")
            file.write(f"Total Students: {len(students_data)}\n")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Gabim në ruajtjen e file: {str(e)}")
        return False

def load_from_file():
    """Funksioni që ngarkon regjistrimet nga file në hapjen e programit"""
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    
                    if line and line[0].isdigit() and ". " in line:
                        student_entry = line.split(". ", 1)[1]
                        students_data.append(student_entry)
                        lb.insert(len(students_data), student_entry)
        except Exception as e:
            messagebox.showerror("Error", f"Gabim në leximin e file: {str(e)}")

def submit_registration():
    """Funksioni që ruan regjistrimin e ri"""
    name = name_input.get().strip()
    surname = surname_input.get().strip()
    

    if not name or not surname:
        messagebox.showwarning("Warning", "Ju lutem plotësoni emrin dhe mbiemrin!")
        return
    
    selected_programs = []
    if game_dev_var.get() == 1:
        selected_programs.append("3D Game Development")
    if ai_var.get() == 1:
        selected_programs.append("Artificial Intelligence")
    if uiux_var.get() == 1:
        selected_programs.append("Web Development")
    
    if not selected_programs:
        messagebox.showwarning("Warning", "Ju lutem zgjidhni të paktën një program!")
        return
    

    full_name = f"{name} {surname}"
    for program in selected_programs:
        student_entry = f"{full_name} - {program}"
        students_data.append(student_entry)
        lb.insert(len(students_data), student_entry)
    

    if save_to_file():
        # Pastro inputet
        name_input.delete(0, 'end')
        surname_input.delete(0, 'end')
        game_dev_var.set(0)
        ai_var.set(0)
        uiux_var.set(0)
        
        messagebox.showinfo("Success", f"Regjistrimi u ruajt me sukses!\n{full_name} - {', '.join(selected_programs)}")

def cancel_form():
    """Funksioni për anulimin e formularit"""
    name_input.delete(0, 'end')
    surname_input.delete(0, 'end')
    game_dev_var.set(0)
    ai_var.set(0)
    uiux_var.set(0)


first_frame = Frame(root, bg="#61c853", width=700, height=50)
second_frame = Frame(root,bg="#004e10", width=700, height=50)
third_frame = Frame(root, bg='#004e10', width=700, height=100)
fourth_frame = Frame(root, bg='#004e10', width=700, height=200) 
fifth_frame = Frame(root, bg='#004e10', width=700, height=100)


first_frame.grid(row=0, sticky=W)
second_frame.grid(row=1, sticky=W)
third_frame.grid(row=2)
fourth_frame.grid(row=3, sticky=W)
fifth_frame.grid(row=4, sticky=W)

header_label = Label(first_frame, text="Project 1", bg='#61c853', fg='white', font=("Courier", 15))
header_label.grid(row=0, column=0, pady=15, padx=180)


second_frame_left = Frame(second_frame, bg='#004e10', width=350, height=50, padx=56)
second_frame_right = Frame(second_frame, bg='#004e10', width=350, height=50, padx=20)

second_frame_left.grid(row=0, column=0)
second_frame_right.grid(row=0, column=1)


name_label = Label(second_frame_left, text="Name:", bg='#004e10', fg='white', font=("Arial", 10))
name_label.grid(row=0, column=0, padx=5,pady=30)


name_input = Entry(second_frame_left)
name_input.grid(row=0, column=1, ipadx=30,padx=5, pady=30)


surname_label = Label(second_frame_right, text="Surname:", bg='#004e10', fg='white', font=("Arial", 10))
surname_label.grid(row=0, column=0, padx=5,pady=30)


surname_input = Entry(second_frame_right)
surname_input.grid(row=0, column=1, ipadx=30, padx=5, pady=30)


third_frame_left = Frame(third_frame, bg='#004e10', width=200, height=100, padx=15, pady=3)
third_frame_mid = Frame(third_frame,  bg='#004e10',width=200, height=100, padx=15, pady=3)
third_frame_right = Frame(third_frame,  bg='#004e10',width=200, height=100, padx=15, pady=3)

third_frame_left.grid(row=0, column=0)
third_frame_mid.grid(row=0, column=1)
third_frame_right.grid(row=0, column=2)

game_dev_label = Label(third_frame_left, text="3D Game Development", bg='#004e10', fg='white', font=("Arial", 10))
game_dev_label.grid(row=0, column=0, pady=30)


game_dev_checkbox = Checkbutton(third_frame_left, variable=game_dev_var, bg='#004e10')
game_dev_checkbox.grid(row=0, column=1,pady=30)


ai_label = Label(third_frame_mid, text="Artificial Intelligence", bg='#004e10', fg='white', font=("Arial", 10))
ai_label.grid(row=0, column=0, pady=30)


ai_checkbox = Checkbutton(third_frame_mid, variable=ai_var, bg='#004e10')
ai_checkbox.grid(row=0, column=1, pady=30)


uiux_label = Label(third_frame_right, text="Web Developement", bg='#004e10', fg='white', font=("Arial", 10))
uiux_label.grid(row=0, column=0, pady=30)


uiux_checkbox = Checkbutton(third_frame_right, variable=uiux_var, bg='#004e10')
uiux_checkbox.grid(row=0, column=1, pady=30)

students_label = Label(fourth_frame, text="Students:", bg='#004e10', fg='white', font=("Arial", 10))
students_label.grid(row=0, column=0)


lb = Listbox(
    fourth_frame,
    width=65,
    height=8,
    borderwidth=0,
    selectmode=SINGLE,
    font=('Arial', 12),
    bd=0,
    fg='#004e10',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"  
)
lb.grid(row=1, column=0,padx=60, pady=15)

load_from_file()

if len(students_data) == 0:
    initial_students = [
        "Esko 11- 3D Game Development",
        "Arber Gegaj - Web Development",
        "Ensar Maliqi - Artificial Intelligence",
        "Festa Qoqaj - Artificial Intelligence"
    ]
    
    for i, student in enumerate(initial_students, 1):
        students_data.append(student)
        lb.insert(i, student)
    

    save_to_file()

fifth_frame_left = Frame(fifth_frame, bg='#004e10', width=350, height=50)
fifth_frame_right = Frame(fifth_frame, bg='#004e10', width=350, height=50, padx=65, pady=3)

fifth_frame_left.grid(row=0, column=0)
fifth_frame_right.grid(row=0, column=1)

button1 = Button(
    fifth_frame_right,
    text='Submit',
    font=('arial 10'),
    width=10,
    padx=10,
    pady=3,
    bg='#7eb900',
    fg='white',
    command=submit_registration
)
button1.grid(row=0, column=0, sticky=W, pady=15)


button2 = Button(
    fifth_frame_right,
    text='Cancel',
    font=('arial 10'),
    width=10,
    padx=10,
    pady=3,
    bg='#61c853',
    fg='white',
    command=cancel_form
)
button2.grid(row=0, column=1, sticky=W, padx=15, pady=15)


root.mainloop()
