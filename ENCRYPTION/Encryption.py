from tkinter import *
from tkinter import messagebox
import base64

# Main window setup
screen = Tk()
screen.geometry("500x500")
screen.title("Encryption and Decryption")

# Optional: Handle missing icon file gracefully
try:
    screen.iconbitmap("C:/Users/asus/Downloads/icon.ico")
except:
    pass

screen.configure(bg="lightblue")
screen.resizable(False, False)

# Encrypt Function
def encrypt():
    password = code.get()
    input_text = text1.get(1.0, END).strip()

    if password == "":
        messagebox.showerror("Error", "Please enter the secret key")
        return
    if password != "1234":
        messagebox.showerror("Oops", "Invalid secret Key")
        return
    if not input_text:
        messagebox.showerror("Error", "Please enter text to encrypt")
        return

    encoded_bytes = base64.b64encode(input_text.encode("ascii"))
    encrypted_text = encoded_bytes.decode("ascii")

    screen1 = Toplevel(screen)
    screen1.title("Cipher Text")
    screen1.geometry("400x250")
    screen1.configure(bg="lightblue")

    Label(screen1, text="Your Text has been Encrypted", font=("Times New Roman", 16), bg="lightblue").place(x=5, y=5, width=385)
    text2 = Text(screen1, font=("Arial", 12), bd=4, wrap=WORD)
    text2.place(x=5, y=40, width=385, height=120)
    text2.insert(END, encrypted_text)

# Decrypt Function
def decrypt():
    password = code.get()
    input_text = text1.get(1.0, END).strip()

    if password == "":
        messagebox.showerror("Error", "Please enter the secret key")
        return
    if password != "1234":
        messagebox.showerror("Oops", "Invalid secret Key")
        return
    if not input_text:
        messagebox.showerror("Error", "Please enter text to decrypt")
        return

    try:
        decoded_bytes = base64.b64decode(input_text.encode("ascii"))
        decrypted_text = decoded_bytes.decode("ascii")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Base64 input or corrupted data")
        return

    screen2 = Toplevel(screen)
    screen2.title("Plain Text")
    screen2.geometry("400x250")
    screen2.configure(bg="lightblue")

    Label(screen2, text="Your Text has been Decrypted", font=("Times New Roman", 16), bg="lightblue").place(x=5, y=5, width=385)
    text2 = Text(screen2, font=("Arial", 12), bd=4, wrap=WORD)
    text2.place(x=5, y=40, width=385, height=120)
    text2.insert(END, decrypted_text)

# Reset Function
def reset():
    text1.delete(1.0, END)
    code.set("")

# UI Layout
Label(screen, text="Enter text to be Encrypted or Decrypted", font=("Times New Roman", 16), bg="lightblue").pack(pady=10)

text1 = Text(screen, font=("Arial", 12), bd=4, height=7, wrap=WORD)
text1.pack(pady=10)

Label(screen, text="Enter Secret Key", font=("Times New Roman", 14), bg="lightblue").pack(pady=10)

code = StringVar()
Entry(screen, textvariable=code, bd=4, font=("Arial", 12), show="*").pack()

Button(screen, text="Encrypt", font=("Times New Roman", 15, "bold"), bg="blue", fg="white", command=encrypt).place(x=65, y=325, width=180)
Button(screen, text="Decrypt", font=("Times New Roman", 15, "bold"), bg="green", fg="white", command=decrypt).place(x=260, y=325, width=180)
Button(screen, text="Reset", font=("Times New Roman", 15, "bold"), bg="red", fg="white", command=reset).place(x=160, y=380, width=180)

screen.mainloop()