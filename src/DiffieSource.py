import socketserver
import random
import base64
systemRandom = random.SystemRandom()

# list of prime numbers
Primes = [101, 103, 107, 109, 113, 127, 131,
          137, 139, 149, 151, 157, 163, 167, 173,
          179, 181, 191, 193, 197, 199, 211, 223,
          227, 229, 233, 239, 241, 251, 257, 263,
          269, 271, 277, 281, 283, 293, 307, 311,
          313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409,
          419, 421, 431, 433, 439, 443, 449, 457,
          461, 463, 467, 479, 487, 491, 499, 503,
          509, 521, 523, 541, 547, 557, 563, 569,
          571, 577, 587, 593, 599, 601, 607, 613,
          617, 619, 631, 641, 643, 647, 653, 659,
          661, 673, 677, 683, 691, 701, 709, 719,
          727, 733, 739, 743, 751, 757, 761, 769,
          773, 787, 797, 809, 811, 821, 823, 827,
          829, 839, 853, 857, 859, 863, 877, 881,
          883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997]


class MyTCPServer(socketserver.BaseRequestHandler):  # custom TCP Service class, must inherit socketserver.BaseRequestHandler
    def handle(self):  # Override this class,
        keydata, key, B64Text = Base64Encode()
        # sends output containing the numbers (encoded in base64) to the user
        self.request.sendall(str(B64Text).encode("utf-8") + b"\n\nWhat is the secret key?\n")
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        if self.data == str(key).encode("utf-8"):
            # if the user inputs the value of key, the flag is produced
            self.request.sendall(b"\nCORRECT, " + self.data + b" is the secret key! \nFlag: S3cR3T_D1fFi3_He11m4n_K3yZ_64\n")
        else:
            # if the input is not equal to key, the flag is not produced
            self.request.sendall(b"INCORRECT\n")

def NumberGeneration():
    # Generates all numbers to be used in the key exchange
    a = systemRandom.randint(10,99)
    b = systemRandom.randint(10,99)
    n = random.choice(Primes)
    g = systemRandom.randint(20,80)
    # key is calculated
    k = pow(g,a*b,n)
    return [a,b,n,g], k

def Base64Encode():
    # produces the base64 text
    keydata, key = NumberGeneration()
    TextToBeEncoded = (b"\nAlice's Private Key is: " + str(keydata[0]).encode("utf-8") + b"\nBob's Private Key is: " + str(keydata[1]).encode("utf-8") + b"\nThe prime number chosen is: " + str(keydata[2]).encode("utf-8") + b"\nThe generator number chosen is: " + str(keydata[3]).encode("utf-8"))
    B64Text = (base64.b64encode(TextToBeEncoded)).decode('utf-8')
    return keydata, key, B64Text


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer): # Class names are arbitrary and must inherit both classes
    pass
if __name__ == "__main__":
    ip_port = ("127.0.0.1", 9999)  # TCP Address and port of the server

    with socketserver.ThreadingTCPServer(ip_port, MyTCPServer) as server:
        server.serve_forever()  # open TCP service
