import socket

#data = input("Data to send > ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = "192.168.43.7"
portNum = 80
s.connect((address, portNum))

def sendData(message):
    try:
        
        n = 10
        b = 1
        for i in range(0, len(message), n):
            message[i:i+n]
            #print("Message chunk {0}: {1}".format(b,i))
            byteLen = s.send(bytes(message[i:i+n], "utf-8"))
            #print("Byte {0}: {1}".format(b, byteLen))
            #b = b + 1
            
        #s.close()

    except Exception as exc:
            print("Exception ESP: {0}".format(exc))
            
#sendData(s, data)
     
