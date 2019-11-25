import socket

data = input("Data to send > ")

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendData(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = "192.168.43.7"
    portNum = 80
    
    try:
        mySocket.connect((address, portNum))
        n = 10
        b = 1
        for i in range(0, len(message), n):
            message[i:i+n]
            #print("Message chunk {0}: {1}".format(b,i))
            byteLen = mySocket.send(bytes(message[i:i+n], "utf-8"))
            #print("Byte {0}: {1}".format(b, byteLen))
            #b = b + 1
            
        mySocket.close()

    except Exception as exc:
            print("Exception: {0}".format(exc))
            
#sendData(s, data)
     
