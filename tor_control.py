###Config_file /etc/tor/torrc
## Uncomment following lines 
#ControlPort 9051
#HashedControlPassword 16:xXxxxx (where 16:xxxx comes from running "tor --hash-password PWD_HERE")

#sudo service tor restart
#create tor_pass.secret with the hashedcontrolpassword when prompted

import socket
import socks
from stem import Signal
from stem.control import Controller


class TorControl():
    def __init__(self):
        print("TOR CONTROLLER")
        print("Make sure that Tor is active in port 9050 and the Controller is active in port 9051")
        print("to activate uncomment lines ControlPort and HashedControlPassword from /etc/tor/torrc and restart tor")
        self.controller = Controller.from_port(port=9051)
        try:
            self.controller.authenticate(open('./tor_pass.secret').read())
        except:
            import getpass
            psw = getpass.getpass("What's the HashedControlPassword? (from /etc/tor/torrc):" )
            self.controller.authenticate(psw)
               
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
        socket.socket = socks.socksocket
    
    def renew_tor(self):
        self.controller.signal(Signal.NEWNYM)
        
    