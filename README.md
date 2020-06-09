Email: emilybest878@hotmail.com
# Something Diffie-rent

## Flag
Flag: `S3cR3T_D1fFi3_He11m4n_K3yZ_64`
## Briefing
We recently found this TCP service on `<ip>` port number `<portnumber>` which asks for a secret key. There appears to be an encoded message, but our agents couldn’t work out what it meant.  Can you decode it and work out the secret key to access the flag?

By Emily

#### Optional Hint:
Research methods of exchanging cyptographic keys over a public channel securely.

## Infrastructure
* Programming Language: Python
* Host the Python File (The TCP port it is hosted on can be changed within the script, it is currently set to 9999 for example purposes)
* Python Modules Required:
  * socketserver
  * random
  * base64

## Walkthrough
1. The user connects to the service with `nc <ip> <port>`:
 ![](WalkthroughImage1.png)
1. The user will now need to decode the base64 presented to them in step one. The command `echo <base64> | base64 -d` can be used to complete this step:
 ![](WalkthroughImage2.png)
