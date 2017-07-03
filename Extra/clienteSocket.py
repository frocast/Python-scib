import socket
import os

class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        # totalsent = 0
        # while totalsent < MSGLEN:
        #     sent = self.sock.send(msg[totalsent:])
        #     if sent == 0:
        #         raise RuntimeError("socket connection broken")
        #     totalsent = totalsent + sent

        try:    
            # Send data
            #message = 'This is the message.  It will be repeated.'
            #print >>system.stderr, 'sending "%s"' % msg
            sock.sendall(msg)

            # Look for the response    
            amount_received = 0
            amount_expected = len(msg)
    
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                #print >>system.stderr, 'received "%s"' % data

        finally:
            #print >>system.stderr, 'closing socket'
            #sock.close()
            pass    

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)