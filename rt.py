import datetime,sys
from functools import partial
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sqlite3
def mail(fromaddr,toaddr,number1,number2,number3,number4,uni):
    try:
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = number1+" "+str(uni)

        # string to store the body of the mail
        body = "Body_of_the_mail"
        text = "this is from klu SAMYAK"
        html = '<html><head><style>table { width:0%;}table, th, td {  border: 1px solid black; border-collapse: collapse;}th, td { padding: 15px; text-align: left;}</style></head><body><p><table><tr><td><strong>Name</strong></td><td>'+number1+'</td></tr><tr><td><strong>Mail</strong></td><td>'+number2+'</td></tr><tr><td><strong>Id</strong></td><td>'+str(uni)+'</td></tr><tr><td><strong>Paid</strong></td><td>'+number4+'</td></tr></table>thank you<br>Team klu samyak<br>kowthasathwik@gmail.com</p>\</body></html>'
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        msg.attach(part1)
        msg.attach(part2)
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr, "fusionsathwik2000")

        # Converts the Multipart msg into a string
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        s.quit()
        return 'success'
    except:
        return 'mailFailed'
def key():
    f=datetime.datetime.now().strftime('%m%d%H%M%S%f')
    f=int(f)
    return f
def clear(number1, number2,number3,number4):
    uni=key()
    conn=sqlite3.connect(':memory:')
    conn=sqlite3.connect('samyak.db')
    cursor=conn.cursor()
    t=mail('fusionbysathwik@gmail.com',number2,number1,number2,number3,number4,uni)
    r=0
    if(t=='success'):
        r=1
    if r==1:
        try:
            pr=(uni,number1,number2,number3,int(number4))
            cursor.execute("insert into reg(id,name,mail,clg,amount) values(?,?,?,?,?)",pr)
            conn.commit()
            return 'done'
        except:
            return 'faileReg'
    else:
        return 'faileMail'
def clear1(id):
    conn=sqlite3.connect(':memory:')
    conn=sqlite3.connect('samyak.db')
    cursor=conn.cursor()
    id=int(id)
    cursor.execute("select * from reg where id=?",[id])
    u=cursor.fetchall()
    if len(u)>0:
        return True
    return False
clear1(813210418240773)
'''def start():
    clear(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])'''
