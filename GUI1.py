from email import message
import email
import smtplib
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import ImageTk
from tkinter import messagebox
import random
import array
import pyrebase
import pyrebase.pyrebase 
import os

firebaseConfig = {
    'apiKey': "AIzaSyBEapbPNQFoJJPHqkbYytXKc10EKnW4ZSk",
    'authDomain': "attendance-management-sy-59713.firebaseapp.com",
    'databaseURL': "https://attendance-management-sy-59713-default-rtdb.firebaseio.com",
    'projectId': "attendance-management-sy-59713",
    'storageBucket': "attendance-management-sy-59713.appspot.com",
    'messagingSenderId': "536903474701",
    'appId': "1:536903474701:web:9c48127a90a84b57113f44",
    'measurementId': "G-WEGC8M0TRN"
  }


firebase1=pyrebase.initialize_app(firebaseConfig)

auth=firebase1.auth()

class login:
    def __init__(self,root):
        self.root = root
        self.root.title("Attandance Management System")
        self.root.geometry("900x600+100+50")
        self.root.resizable(False,False)
        self.bg = ImageTk.PhotoImage(file = "Images/background.jpg")
        self.bg_Image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #login frame
        frame_login = Frame(self.root, bg="white",border=5, borderwidth=10)
        frame_login.place(x=220, y=80,width=450, height=400)

        title1 = Label(frame_login, text="Login Here", font=("Impact", 35,"bold", "underline"),bg="white").place(x=105, y=1)
        desc = Label(frame_login, text="Welcome to Attendance Management System", font=("Cooper Black", 12),fg="#353332",bg="white").place(x=30, y=65)


        lbl_user = Label(frame_login, text="E-Mail", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=65, y=95)
        self.text_user= Entry(frame_login, font=("times new roman", 12 ),bg="lightgrey")
        self.text_user.place(x=65, y=125,width=300, height=35)

        
        

        lbl_pass1 = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=65, y=170)
        self.text_pass1= Entry(frame_login, show="*",font=("times new roman", 12),bg="lightgrey")
        self.text_pass1.place(x=65, y= 210,width=300, height=35)

        

        otp = StringVar()
        def send_message():
            sender_email = "minorprojectsem2@gmail.com"
            receiver_email = self.text_user.get()
            MAX_LEN = 8

            # declare arrays of the character that we need in out password
            # Represented as chars to enable easy string concatenation
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                'z']

            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                'Z']

            SYMBOLS = ['@', '#',]

            # combines all the character arrays above to form one array
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            # randomly select at least one character from each character set above
            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)

            # combine the character randomly selected above
            # at this stage, the password contains only 4 characters but
            # we want a 12-character password
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


            # now that we are sure we have at least one character from each
            # set of characters, we fill the rest of
            # the password length by selecting randomly from the combined
            # list of character above.
            for x in range(MAX_LEN - 4):
                temp_pass = temp_pass + random.choice(COMBINED_LIST)

                # convert temporary password into array and shuffle to
                # prevent it from having a consistent pattern
                # where the beginning of the password is predictable
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)

            # traverse the temporary password array and append the chars
            # to form the password
            password = ""
            for x in temp_pass_list:
                password = password + x

            otp.set(password) 
                            
            print(password)
            sender_password = "Minor@1234"
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email,sender_password)
            print("loggined")
            server.sendmail(sender_email,receiver_email,password)
            print("Message Send..!!")
            messagebox.showinfo("Alert", f"OTP sent to {receiver_email}")


        get_otp = Button(frame_login,command=send_message ,text="Get OTP", bg="lightgrey", font=("Georgia", 8, "bold")).place(x=65, y=332)

        lbl_pass = Label(frame_login, text="Enter OTP", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=65, y=265)
        self.text_pass= Entry(frame_login, font=("times new roman", 12 ),bg="lightgrey")
        self.text_pass.place(x=65, y=295,width=300, height=35)

        def login_function():
            emails=self.text_user.get()
            password=self.text_pass1.get()
            
            try:
                auth.sign_in_with_email_and_password(emails, password)
                if self.text_pass.get() == otp.get():
                    messagebox.showinfo("Welcome", "You are logined")
                    root.destroy()
                   
        
            except:
                messagebox.showerror("Alert", "You entered wrong E-mail/Password/OTP")

               
        def mark():
            if var1.get()==1:
                self.text_pass1.configure(show="")
            elif var1.get()==0:
                self.text_pass1.configure(show="*")
           

        var1 = IntVar()
        cb = Checkbutton(frame_login,command = mark, offvalue = 0, onvalue = 1, variable=var1 ,text="👁️",bg="lightgrey").place(x=300, y=215)

        #
        login_btn = Button(self.root,command=login_function ,text="Login", fg="white",bg="#585858", font=("Georgia", 16, "bold")).place(x=370, y=460,width=150)

    

        
    # def frgt_pass(self):
    #     frame1 = Frame(self.root, bg="white",border=5, borderwidth=10)
    #     frame1.place(x=170, y=100,width=550, height=400)

    #     title2 = Label(frame1, text="Forgot Password", font=("Impact", 35,"bold", "underline"),bg="white").place(x=95, y=10)
    #     desc1 = Label(frame1, text="Please provide your username", font=("Cooper Black", 12),fg="#353332",bg="white").place(x=130, y=75)

    #     lbl_user_frgt = Label(frame1, text="Username", font=("Goudy old style", 15, "bold"),fg="#353332",bg="white").place(x=120, y=125)
    #     self.text_user_frgt= Entry(frame1, font=("times new roman", 12 ),bg="lightgrey")
    #     self.text_user_frgt.place(x=120, y=155,width=290, height=35)

    #     cb = Checkbutton(frame1,text="above information is correct",bg="white").place(x=170, y=207)
    # # def chk_btn(self):
    # #     if var.get()==1:

    
    #     submit_butn = Button(frame1 ,text="Submit",command=self.send_message, fg="white",bg="#585858", font=("Georgia", 16, "bold")).place(x=180, y=250,width=150)

    # def send_message(self):
    #     sender_email = "minorprojectsem2@gmail.com"
    #     receiver_email = self.text_user_frgt.get()
    #     email_info = "hello"
    #     sender_password = "Qwerty@1234"
    #     # message = "Accident has been detected"
    #     server = smtplib.SMTP('smtp.gmail.com',587)
    #     server.starttls()
    #     server.login(sender_email,sender_password)
    #     print("loggined")
    #     server.sendmail(sender_email,receiver_email,email_info)
    #     print("Message Send..!!")
    #     messagebox.showinfo("Alert", "Message")

    #     self.text_user_frgt.delete(0,END)



    # def login_function(self):
    #     if self.text_pass.get()=="" or self.text_user.get()=="":
    #         messagebox.showerror("Error!!", "Please Enter Correct Username/Password", parent=self.root)
    #     else:
    #         messagebox.showinfo("Welcome", "You are logged In", parent=self.root)
            


root = Tk()
obj = login(root)
root.mainloop()
