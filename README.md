# Backdoor-generator
Backdoor Generator is a tool to create encoded payloads for reverse shells.

## How to install
Only need Python 3.

## How to use
The functionality is very simple. The script asks for the IP and PORT of the attacker, and the language to be used for the reverse shell. 

The languages available for the reverse shells are the following: 
- Netcat
- Netcat (SSL)
- Socat
- SBD (Alternative to Netcat encrypted)
- Bash
- Python

The script asks for everything it needs to generate a file sh file. This file is the payload that needs to be executed in the victim machine (Linux machines). 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
