## Python controller for TOR, to scrape anonymously.
### Be nice!

## Steps (Ubuntu + Debian)

1. Install tor
```
sudo apt install tor
```
2. Install required libraries
```
pip install pysocks
pip install stem
```

3. Create hash of password
```
tor --hash-password your_password_here
```
4. Edit /etc/tor/torrc, uncommenting 
    * ControlPort 9051
    * HashedControlPassword 16:xXxxxx (where 16:xxxx comes from step 3")

5. Restart tor
```
sudo service tor restart
```

## Run the controller
To run the controller (this will ask you for your hashed password the first time **and will create a file with it**):
```
from tor_control import TorControl
tc = TorControl()
    
```

To change identities:
```
tc.renew_tor()
```

Example [jupyter notebook here](example_tor.ipynb):
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
