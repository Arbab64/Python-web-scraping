import requests
import smtplib
from bs4 import BeautifulSoup

posturl='https://lms.iiitb.ac.in/moodle/login/index.php'
requrl='https://lms.iiitb.ac.in/moodle/my/'
values={'username': 'username','password': 'Password'}
post = requests.post('https://lms.iiitb.ac.in/moodle/login/index.php', data=values,verify=False)
#print(post.text)
c=post.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div",{"class":"name"})
#print(all)
#print(all[1].find("a").get('href'))
mesg=[]
message="\n"
for links in all:
    mesg.append(links.find("a").get('href'))
for msg in mesg:
    print(msg)
    message+=(msg+'\n')
print(message)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sender mail id", "your password")
s.sendmail("sender email id", "receiver mail id", str(message))
s.quit()


