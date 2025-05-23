class EmailNotifier:

    def __connect_to_smtp(self):
        print("connecting to smtp server")

    def __prepare_email(self,message):
        print("preparing email")
        print(message)

    def __send_email(self):
        print("message sent")

    def send_notification(self, message):
        self.__connect_to_smtp()
        self.__prepare_email(message)
        self.__send_email()
    
email = EmailNotifier()
message = "hello"
email.send_notification(message)


class SMSNotifier:

    def __connecting(self):
        print("Connecting to SMS gateway")
    
    def __formatting(self, message):
        print("Formatting SMS: ", message)
    
    def send_notification(self, message):
        print("------------SMS----------")
        self.__connecting()
        self.__formatting(message)
        print("SMS sent")

sms = SMSNotifier()
sms.send_notification("Hi, your OTP is 101010")
