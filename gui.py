from algorithm import generate_key_string,encrypt_message,decrypt_message
import tkinter as tk
import pyperclip

class GUI():
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Matrix Cryptography")
        self.root.geometry("600x330")

        #Generate key frame
        self.generate_key_frame=tk.Frame(self.root)
        self.key=""

        self.generate_key_frame.columnconfigure((0,1,2),weight=1)
        self.generate_key_frame.rowconfigure(0,weight=1)

        self.generate_key_button=tk.Button(self.generate_key_frame,text="Generate Key",command=self.generate_key_command)
        self.generate_key_button.grid(row=0,column=0,sticky='w',padx=20)

        self.generate_key_text=tk.Label(self.generate_key_frame,text=f"Key: {self.key}")
        self.generate_key_text.grid(row=0,column=1,sticky='we',padx=20)

        self.generate_key_copy=tk.Button(self.generate_key_frame,text="Copy",command=self.key_copy_command)
        self.generate_key_copy.grid(row=0,column=2,sticky='w',padx=20)

        self.generate_key_frame.pack(anchor='n',padx=10,pady=10)
        
        #Current session key frame
        self.session_key_frame=tk.Frame(self.root)
        self.session_key=""

        self.session_key_frame.columnconfigure((0,1,2),weight=1)
        self.session_key_frame.rowconfigure(0,weight=1)

        self.session_key_label=tk.Label(self.session_key_frame,text="Current session key:")
        self.session_key_label.grid(row=0,column=0,sticky='w',padx=20)

        self.session_key_textbox = tk.Entry(self.session_key_frame)
        self.session_key_textbox.grid(row=0,column=1,sticky='we',padx=20)

        self.session_key_paste=tk.Button(self.session_key_frame,text="Paste",command=self.key_paste_command)
        self.session_key_paste.grid(row=0,column=2,sticky='w',padx=20)

        self.session_key_frame.pack(padx=10,pady=10)

        #Message frame
        self.message_frame=tk.Frame(self.root)
        self.current_message=""

        self.message_frame.columnconfigure(0,weight=1)
        self.message_frame.columnconfigure(1,weight=3)
        self.message_frame.rowconfigure((0,1,2,3),weight=1)

        self.message_textbox = tk.Text(self.message_frame,width=40,height=4)
        self.message_textbox.grid(row=0,column=0,rowspan=4,sticky="nesw")

        self.encrypt_button = tk.Button(self.message_frame,text='Encrypt',width=10,command=self.message_encrypt_command)
        self.encrypt_button.grid(row=0,column=1,sticky='nw')

        self.message_copy = tk.Button(self.message_frame,text='Copy',width=10,command=self.message_copy_command)
        self.message_copy.grid(row=1,column=1,sticky='nw')

        self.message_paste = tk.Button(self.message_frame,text='Paste',width=10,command=self.message_paste_command)
        self.message_paste.grid(row=2,column=1,sticky='nw')

        self.decrypt_button = tk.Button(self.message_frame,text='Decrypt',width=10,command=self.message_decrypt_command)
        self.decrypt_button.grid(row=3,column=1,sticky='nw')

        self.message_frame.pack(padx=10,pady=10)
        self.root.mainloop()
    
    def generate_key_command(self):
        self.key = generate_key_string()
        self.generate_key_text.config(text=f"Key: {self.key}")

    def key_copy_command(self):
        pyperclip.copy(self.key)
    
    def key_paste_command(self):
        self.session_key=pyperclip.paste()
        self.session_key_textbox.delete(0,tk.END)
        self.session_key_textbox.insert(0,self.session_key)

    def message_encrypt_command(self):
        self.current_message=self.message_textbox.get("1.0", "end-1c")
        self.message_textbox.delete("1.0","end")
        self.message_textbox.insert("1.0",encrypt_message(self.current_message,self.session_key))
    
    def message_copy_command(self):
        self.current_message=self.message_textbox.get("1.0", "end-1c")
        pyperclip.copy(self.current_message)
    
    def message_paste_command(self):
        self.message_textbox.delete("1.0","end")
        self.message_textbox.insert("1.0",pyperclip.paste())

    def message_decrypt_command(self):
        self.current_message=self.message_textbox.get("1.0", "end-1c")
        self.message_textbox.delete("1.0","end")
        self.message_textbox.insert("1.0",decrypt_message(self.current_message,self.session_key))

GUI()