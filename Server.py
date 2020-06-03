'''from socket import socket, AF_INET, SOCK_DGRAM

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)
    source_ip = '0.0.0.0'
    source_port = 12345
    s.bind((source_ip, source_port))
    ipAndPortToNameDict = {}
    allMessages = []

    while True:
        str1 = ""

        data, sender_info = s.recvfrom(2048)
        data = data.decode("utf8")

        # divides by whitespaces
        splittedInfo = data.split()

        # num of mission
        num = splittedInfo[0]

        # condition for more than one name/ message:
        if len(splittedInfo) > 2:
            for x in range(2, len(splittedInfo)):
                splittedInfo[1] += " " + splittedInfo[x]

        if num == "1":
            # server sends to all a msg : [name] has joined
            # message format:
            messageToAll = splittedInfo[1] + " has joined"

            # send to all:
            for element in ipAndPortToNameDict:
                s.sendto(messageToAll, element)

            for str2 in ipAndPortToNameDict:
                if str1 != "":
                    str1 += ", " + ipAndPortToNameDict[str2]
                else:
                    str1 += ipAndPortToNameDict[str2]

            # send message to the new member
            s.sendto(str1, sender_info)

            # adding a new member

            ipAndPortToNameDict[sender_info] = splittedInfo[1]
            # server saves the member's name and socket info

        elif num == "2":

            name = ipAndPortToNameDict[sender_info]
            messageToAll = name + ": " + splittedInfo[1]

            # server sends all a msg : [name]:[msg]
            for element in ipAndPortToNameDict:
                s.sendto(messageToAll, element)

        elif num == "3":
            newName = splittedInfo[1]

            messageToAll = ipAndPortToNameDict[sender_info] + " changed his name to " + newName

            # server sends all the new name!
            for element in ipAndPortToNameDict:
                s.sendto(messageToAll, element)

            ipAndPortToNameDict[sender_info] = newName

        elif num == "4":

            messageToAll = ipAndPortToNameDict[sender_info] + " has left the group"

            # server sends all that the sender has left the group
            for element in ipAndPortToNameDict:
                s.sendto(messageToAll, element)

            del ipAndPortToNameDict[sender_info]

        elif num == "5":
           print "hey"

        else:
            print ("Illegal request")
            # more things to add?
            '''


from socket import socket, AF_INET, SOCK_DGRAM


def illegal_request():
    error = "Illegal request"
    s.sendto(error, sender_info)


def add_message_to_dict(message):
    for key in messagesDict:
        if key != sender_info:
            if messagesDict[key]=="":
                messagesDict[key] = message
            else:
                messagesDict[key] += '\n'
                messagesDict[key] += message


def send_all_messages():
    for client in messagesDict:
        if client != sender_info:
            s.sendto(messagesDict[client], client)
            # after sending all the appending messages we delete them
            messagesDict[client] = ""


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)
    source_ip = '0.0.0.0'
    source_port = 12345
    s.bind((source_ip, source_port))
    ipAndPortToNameDict = {}
    # messageDict - the key is client, the val is all the messages appending
    messagesDict = {}
    # a tuple of all the messages (?)
    allMessages = ()

    while True:
        str1 = ""

        data, sender_info = s.recvfrom(2048)
        data = data.decode("utf8")

        # divides by whitespaces
        splittedInfo = data.split()

        # num of mission
        num = splittedInfo[0]

        if num != "1" and sender_info not in ipAndPortToNameDict:
            illegal_request()

        if num == "1" and sender_info in ipAndPortToNameDict:
            illegal_request()

        # condition for more than one name/ message:
        if len(splittedInfo) > 2:
            for x in range(2, len(splittedInfo)):
                splittedInfo[1] += " " + splittedInfo[x]

        if num == "1":
            # server sends to all a msg : [name] has joined
            # message format:
            messageToAll = splittedInfo[1] + " has joined"

            # send to all:
            for element in ipAndPortToNameDict:
                s.sendto(messageToAll, element)

            for str2 in ipAndPortToNameDict:
                if str1 != "":
                    str1 += ", " + ipAndPortToNameDict[str2]
                else:
                    str1 += ipAndPortToNameDict[str2]

            # send message to the new member
            s.sendto(str1, sender_info)

            # adding a new member

            ipAndPortToNameDict[sender_info] = splittedInfo[1]
            messagesDict[sender_info] = ""
            # server saves the member's name as val and socket info as key

        elif num == "2":

            name = ipAndPortToNameDict[sender_info]
            messageToAll = name + ": " + splittedInfo[1]

            # server sends all but that client a msg : [name]:[msg]
            '''for element in ipAndPortToNameDict:
                if element != sender_info:
                    s.sendto(messageToAll, element)'''
            add_message_to_dict(messageToAll)
            send_all_messages()

        elif num == "3":
            newName = splittedInfo[1]

            messageToAll = ipAndPortToNameDict[sender_info] + " changed his name to " + newName

            # server sends all the new name!
            '''for element in ipAndPortToNameDict:
                if element != sender_info:
                    s.sendto(messageToAll, element)'''
            add_message_to_dict(messageToAll)
            send_all_messages()
            ipAndPortToNameDict[sender_info] = newName

        elif num == "4":

            messageToAll = ipAndPortToNameDict[sender_info] + " has left the group"

            # server sends all that the sender has left the group
            '''for element in ipAndPortToNameDict:
                if element != sender_info:
                    s.sendto(messageToAll, element)'''
            add_message_to_dict(messageToAll)
            send_all_messages()
            del ipAndPortToNameDict[sender_info]

        elif num == "5":
            send_all_messages()

        else:
            illegal_request()
            # more things to add?
