class Participant():
    def __init__(self,name):
        self.name = name
        self.history = []

    def send(self,message):
        self.history.append(message)

    def clear_history(self):
        self.history = []

class ChatServer():
    def __init__(self):
        self.participants = set() #because all users should be unique
        self.messages = []

    def join(self,participant):
        self.participants.add(participant)

        for message in self.messages[-8:]:
            participant.send(message)

    def leave(self,participant):
        if participant in self.participants:
            self.participants.remove(participant)
            participant.clear_history()
            print('{} is left the group!'.format(participant.name))


    def send_all(self, participant, text):
        message = participant.name + text
        self.messages.append(message)
        for p in self.participants:
            p.send(message)
    def online_users(self):
        print('Online users in chatserver:')
        for p in self.participants:
            print(p.name)

def main():
    p1 = Participant('ezgi')
    p2 = Participant('ozden')
    p3 = Participant('hakan')
    p4 = Participant('cinar')

    chatserver = ChatServer()
    chatserver.join(p1)
    chatserver.join(p2)
    chatserver.join(p3)
    chatserver.join(p4)
    #chatserver.leave(p1)
    chatserver.online_users()

if __name__ == '__main__':
    main()
