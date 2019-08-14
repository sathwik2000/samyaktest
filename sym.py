import tkinter as tk
from functools import partial
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
from fpdf import FPDF
import qrcode,sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image
import sqlite3
import cv2
import numpy as np
def clear(number1, number2,number3,number4,number5):
    if(number5.get()=='paid'):
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('idimage.png', image)
        del(camera)
        f=open('data.txt','a+')
        f.write(number1.get()+" ")
        f.write(number2.get()+" ")
        f.write(number3.get()+" ")
        fu=open('uni.txt','r')
        uni=int(fu.read())
        uni=uni+1
        uni=str(uni)
        fu.close()
        conn=sqlite3.connect(':memory:')
        conn=sqlite3.connect('samyak.db')
        cursor=conn.cursor()
        pr=(uni,number1.get(),number2.get(),number3.get(),int(number4.get()))
        cursor.execute("insert into reg(id,name,mail,clg,amount) values(?,?,?,?,?)",pr)
        conn.commit()
        fu=open('uni.txt','w')
        fu.write(uni)
        fu.close()
        f.write(uni+"\n")
        fu=open('id.txt','w')
        #fu.write('___________________________________________________________________\n')
        fu.write("\n")
        t=number1.get()
        fu.write('Name:'+number1.get()+"\n")
        '''o=len(t)+7
        o=67-o
        fu.write('Name:'+number1.get()+"\n")
        for y in range(0,o):
            fu.write(" ")'''
        #fu.write("___________________________________________________________________\n")
        fu.write("\n")
        t=number2.get()
        fu.write('Mail:'+number2.get()+"\n")
        '''o=len(t)+7
        o=67-o
        fu.write('Mail:'+number2.get()+"\n")
        for y in range(0,o):
            fu.write(" ")'''
        #fu.write("___________________________________________________________________\n")
        fu.write("\n")
        t=number3.get()
        fu.write('collage:'+number3.get()+"\n")
        '''o=len(t)+6
        o=67-o
        fu.write('clg:'+number3.get()+"\n")
        for y in range(0,o):
            fu.write(" ")'''
        #fu.write("___________________________________________________________________\n")
        fu.write("\n")
        fu.write('Id:'+uni+"\n")
        '''t=0
        u=int(uni)
        while(u!=0):
            t=t+1
            u=u//10
        o=t+5
        o=67-o
        fu.write('Id:'+uni+"\n")
        for y in range(0,o):
            fu.write(" ")'''
        #fu.write('___________________________________________________________________\n')
        fu.write("\n")
        fu.write('Paid:'+number4.get()+"\n")
        '''t=0
        u=int(uni)
        while(u!=0):
            t=t+1
            u=u//10
        o=t+5
        o=67-o
        fu.write('Id:'+uni+"\n")
        for y in range(0,o):
            fu.write(" ")'''
        #fu.write('___________________________________________________________________\n')
        fu.write("\n")
        '''with open("id.txt", "rb") as foo:
            file_content = foo.read()
            foo.close()
        c = canvas.Canvas("id.pdf")
        c.setFont('Helvetica', 12)
        c.drawString(0,800, file_content)
        c.save()'''
        fu.close()
        f.close()
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )

        # The data that you want to store

        # Add data
        data="Id:"+str(uni)+"\n"+"Name:"+number1.get()+"\n"+"Mail:"+number2.get()+"\n"+"Collage:"+number3.get()
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        # Save it somewhere, change the extension as needed:
        # img.save("image.png")
        # img.save("image.bmp")
        # img.save("image.jpeg")
        img.save("image.png")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(10,10 , 100, 10)
        pdf.line(10,20 , 100, 20)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(10,40 , 100, 40)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(10,60 , 100, 60)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(10,80 , 100, 80)
        pdf.line(10, 100,100, 100)
        pdf.line(10, 120,100, 120)
        pdf.line(100,10,100, 120)
        pdf.set_draw_color(255, 0, 0)
        pdf.line(10,10,10,120)
        q=open('id.txt','r')
        tr=q.read().split("\n")
        pdf.set_text_color(0,255,0)
        pdf.cell(0, 10, txt="KLU SAMYAK", ln=1, align="L")
        pdf.set_text_color(0,0,0)
        for font in tr:
            pdf.cell(0, 10, txt=font, ln=1, align="L")
        pdf.image(name='idimage.png', x = 76, y = 21 ,w = 23, h = 18, type = 'png', link = '')
        pdf.image(name='samyak.jpg', x = 89, y = 11 ,w = 10, h = 7, type = 'jpg', link = '')
        pdf.image(name='image.png', x = 105, y = 10, w = 50, h = 50, type = 'png', link = '')
        pdf.output('idcard.pdf')
        fromaddr = "fusionbysathwik@gmail.com"
        toaddr = number2.get()

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = number1.get()+" "+str(uni)

        # string to store the body of the mail
        body = "Body_of_the_mail"
        text = "this is from klu SAMYAK"
        html ='<html><head><style>table { width:0%;}table, th, td {  border: 1px solid black; border-collapse: collapse;}th, td { padding: 15px; text-align: left;}</style></head><body><p><table><tr><td><strong>Name</strong></td><td>'+number1.get()+'</td></tr><tr><td><strong>Mail</strong></td><td>'+number2.get()+'</td></tr></table>thank you<br>Team klu samyak<br>kowthasathwik@gmail.co</p>\</body></html>'
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        msg.attach(part1)
        msg.attach(part2)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "fusionsathwik2000")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()
        top.destroy
    else:
        toop = tk.Tk()
        toop.geometry("130x60")
        display = tk.Label(toop, text="please pay amount")
        display.place(x=10,y=0)
        tk.Button(toop, text="ok", command=toop.destroy).place(x = 10, y = 20)
        toop.mainloop()
        print("please pay amount")
top = tk.Tk()
top.geometry("400x250")
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
L1 = tk.Label(top, text="Name")
L1.place(x = 0, y = 10)
E1 = tk.Entry(top, textvariable=number1,bd=5).place(x = 70, y = 10)
L1 = tk.Label(top, text="mail")
L1.place(x = 0, y = 40)
E1 = tk.Entry(top, textvariable=number2,bd=5).place(x = 70, y = 40)
L1 = tk.Label(top, text="collage")
L1.place(x = 0, y = 70)
E1 = tk.Entry(top, textvariable=number3,bd=5).place(x = 70, y = 70)
number4 = tk.StringVar(top)
number4.set("sholud pay") # default value
w = tk.OptionMenu(top,number4,"0","100", "200", "300")
w.place(x = 70, y = 100)
#E1.pack(side = tk.RIGHT )
rt="should pay "+number4.get()
number5 = tk.StringVar(top)
number5.set("status") # default value
w = tk.OptionMenu(top,number5,"paid","not paied")
w.place(x = 10, y = 130)
clear = partial(clear, number1, number2,number3,number4,number5)
sbmitbtn = tk.Button(top, text = "Submit",activebackground = "pink", command=clear,activeforeground = "blue").place(x = 10, y = 160)
tk.Button(top, text="Done", command=top.destroy).place(x = 10, y = 190)
top.mainloop()
