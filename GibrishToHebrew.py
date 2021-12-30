from tkinter import *
from tkinter import filedialog
window = Tk()
window.title("Gibrish to Hebrew")
window.geometry("497x135")
window.iconbitmap('closed-caption.ico')

# Set window background color
window.configure(background="black")


def exit():
    quit()


def gibrishToHebrew(file_type='utf8'):
    # chatching errors in file convertion
    try:
        new_string = ""  # saving the text converted to hebrew
        uni_text = "àáâãäåæçèéêëìíîïðñòóôõö÷øùú"
        text = "אבגדהוזחטיךכלםמןנסעףפץצקרשת"

        try:
            file_name = filename
            pass
        # catching NameError file was not selected
        except NameError:
            label_file_explorer.configure(text="You must choose a file!")
            return

        if file_type == "utf8":
            f = open(file_name, "r", encoding=file_type)
        else:
            f = open(file_name, "r")

        for line in f:
            new_line = ""  # saveing the line converted to heberw
            isUni = False
            for i in range(len(line)):
                # checking if the character is a uni_text character
                # that need to be converted to hebrew
                if (line[i] in uni_text):
                    # converting character to hebrew
                    new_line += chr(ord(line[i]) - ord('à') + ord('א'))
                    isUni = True
                # converting special characters or not converting non uni_text characters
                elif(line[i] == '×'):
                    new_line += "'"
                elif(line[i] == 'Ø'):
                    new_line += '"'
                else:
                    new_line += line[i]
            # adding tha line to the text string
            new_string += new_line

        f.close()

        # opening same file in write mode and write to it the converted text saved in new_string
        with open(file_name, 'w', encoding='utf8') as w:
            w.write(new_string)

        label_file_success.configure(text="File transformation success!")
        return

    # catching all errors
    except Exception as e:
        # print to console error
        print(e)
        # trying same function but opening file not as utf8
        if(file_type == 'utf8'):
            gibrishToHebrew(file_type='non-utf8')
            return
        # showing user there was an error
        label_file_success.configure(
            text="Error accured in transformation!")


def browseFiles():
    # opening file browser and save the name of the file in filename
    global filename
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Text files", "*.srt*"), ("all files", "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


# intiating labels and buttons
button_explore = Button(window, text="Browse Files", command=browseFiles)
button_transform = Button(window, text="transform",
                          command=gibrishToHebrew)
label_file_explorer = Label(
    window, text="Choose a FIle", width=70, height=5, fg="white", bg="black")
label_file_success = Label(
    window, text="", width=50, fg="white", bg="black")
button_exit = Button(window, text="Exit", command=exit)


# locating labels and button on screen using the grid method
label_file_explorer.grid(column=0, row=0, columnspan=3)
label_file_success.grid(column=1, row=1)
button_explore.grid(column=0, row=1, sticky=W)
button_transform.grid(column=2, row=1, sticky=E)
button_exit.grid(column=2, row=2, sticky=E)

# Let the window wait for any events
window.mainloop()
