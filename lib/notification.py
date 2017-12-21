#This code sends the email notification whenever sendmail() function is called
import smtplib
from lib.weight import getWeight
def sendmail(product, jobsite_no):
    content = "Hi there, \n"
    #content += getWeight(product)
    content =content + product + " is running below threshold at jobsite no. " + str(jobsite_no)
    #content = "hello"
    mail = smtplib.SMTP('smtp.gmail.com', port = 587) #Set up the smtp mail server port
    mail.ehlo()                                       #Identify yourself to the server
    mail.starttls()                                   #Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted
    mail.login('autonotif2017@gmail.com', 'ilab2017') #Login with your email id and password
    mail.sendmail('autonotif2017@gmail.com' , 'autonotif2017@gmail.com', content)  #This sends the mail. First parameter is from, second is to, and third is the content of the mail
    mail.close()                                      #Close the server
  

