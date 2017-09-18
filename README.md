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
```
ControlPort 9051
HashedControlPassword 16:xXxxxx (where 16:xxxx comes from step 3")
```

5. Restart tor
```
sudo service tor restart
```

6. Optional: Create a file with the password in the directory of the scraper. If you don't do it the scraper will ask for the password every time it runs.
```
echo 16:xxxxxx > tor_pass.secret
```

## Run the controller
```
from tor_control import TorControl
tc = TorControl()
    
```

To change identities:
```
tc.renew_tor()
```

You can get sites using requests and run tc.renew_tor() whenever you need a new ip. Remember to be nice.


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
