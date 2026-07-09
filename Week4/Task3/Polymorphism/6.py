'''16.	Create a Notification system with EmailNotification, SMSNotification, and PushNotification classes. Each class should implement a send() method.'''


class Notification:
    def __init__(self,name,text):
        self.name = name
        self.text = text

class EmailNotification(Notification):
    def send(self):
        print("Sending Email...")
        print(f"Email send to {self.name}")
        print(f"---body----")
        print(f"FYI: {self.text}")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS... ")
        print(f"SMS send to {self.name}")
        print(f"---Msg----")
        print(f"FYI: {self.text}")

class PushNotification(Notification):
    def send(self):
        print("Notification Sended..")
        print(f"Notificaiton send to {self.name}")
        print(f"---body----")
        print(f"FYI: {self.text}")


e = EmailNotification("Dhruv","hey, Congrates, here is your offer letter ")
s= SMSNotification("Dhruv","Your Account XXXX has been credited with 124000")
p = PushNotification("BMW", "Delivery Update")

notify = [e,s,p]

for n in notify:
    n.send()




