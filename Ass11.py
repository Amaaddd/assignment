import tkinter as tk
import webbrowser as wb

root = tk.Tk()
def display_yt():
    user_enq = enq.get()
    print(user_enq)
    if user_enq:
        l2.config(text="Where did you hear about us?")
        wb.open("https://support.google.com/youtube/?hl=en#topic=9257498")
    else:
        l2.config(text="Please enter required information")
        
def display_ig():
        user_enq = enq.get()
        print(user_enq)
        if user_enq: 
            l2.config(text="Where did you hear about us?")
            wb.open("https://help.instagram.com/561062241952036")
        else:
            l2.config(text="Please enter required information")

def display_pin():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://business.pinterest.com/blog/faqs-small-businesses-pinterest/")
    else:
        l2.config(text="Please enter required information")


def display_google():
    user_enq = enq.get()
    print(user_enq)
    if user_enq: 
        l2.config(text="Where did you hear about us?")
        wb.open("https://policies.google.com/faq?hl=en-US")
    else:
        print("Please enter required information")

enq = tk.Entry(root, 
               font=("Times New Roman", 20),
               width=30)
enq.grid(row=0,column=1)

l1 = tk.Label(root, 
              text="Enter enquiry:", 
              font=("Times New Roman", 25))
l1.grid(row=0,column=0)

l2 = tk.Label(root, 
              font=("Times New Roman", 25))
l2.grid()

yt = tk.Button(root, 
               text="YouTube", 
               font=("Times New Roman", 20),
               width=10,
               bg="#b4faeb", 
               activebackground="#ff7581", 
               command=display_yt)
yt.grid()

ig = tk.Button(root, 
               text="Instagram", 
               font=("Times New Roman", 20),
               width=10,
               bg="#b4faeb", 
               activebackground="#bc79f7", 
               command=display_ig)
ig.grid()

pin = tk.Button(root, 
               text="Pinterest", 
               font=("Times New Roman", 20),
               width=10,
               bg="#b4faeb", 
               activebackground="#fc5157", 
               command=display_pin)
pin.grid()

google = tk.Button(root, 
               text="Google", 
               font=("Times New Roman", 20),
               width=10, 
               bg="#b4faeb", 
               activebackground="#69ff69", 
               command=display_google)
google.grid()



root.mainloop()
