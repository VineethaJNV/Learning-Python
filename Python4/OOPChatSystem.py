#Create a chat system using OOPS concepts

class User:
    def __init__(self, user_name):
        self.user_name = user_name

class Message:
    message_counter  = 1
    def __init__(self,sender, message_text):
        self.sender = sender
        self.message_text = message_text
        self.id = Message.message_counter
        Message.message_counter+=1

    def __str__(self):
        return f"{self.id, self.message_text,self.sender}" 

class ChatRoom:
    def __init__(self, )