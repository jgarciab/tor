# tor
- Python controller for TOR, to scrape anonymously.
- Be nice!

Steps (Ubuntu + Debian)

1. sudo apt install tor
2. pip install pysocks
3. pip install stem

4. Run "tor --hash-password your_password_here"
5. Edit /etc/tor/torrc, uncommenting 
- ControlPort 9051
- HashedControlPassword 16:xXxxxx (where 16:xxxx comes from step 4")

6. sudo service tor restart


To run the controller
```
    from tor_control import TorControl
    tc = TorControl()
    
```

To change identities
```
tc.renew_tor()
```

Example:
```
from tor_control import TorControl
import requests
tc = TorControl()
print(requests.get("https://api.ipify.org?format=jso").text)
> 163.172.162.106

tc.renew_tor()
print(requests.get("https://api.ipify.org?format=jso").text)
> 18.85.22.204
```