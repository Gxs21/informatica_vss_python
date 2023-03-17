import tkinter as tk # importo il modulo, con as indico il nome col quale verrà chiamato

root = tk.Tk()  #root crea oggetto di tipo finestra
message = tk.Label (root, text="hello, World")
message.pack()
root.mainloop()