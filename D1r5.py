print("""
 /$$$$$$$    /$$             /$$$$$$$ 
| $$__  $$ /$$$$            | $$____/ 
| $$  \ $$|_  $$    /$$$$$$ | $$      
| $$  | $$  | $$   /$$__  $$| $$$$$$$ 
| $$  | $$  | $$  | $$  \__/|_____  $$
| $$  | $$  | $$  | $$       /$$  \ $$
| $$$$$$$/ /$$$$$$| $$      |  $$$$$$/
|_______/ |______/|__/       \______/ 
======================================
[*] D1r5 - By Afrizal F.A | R&D ICWR |
--------------------------------------
[*] Dir & Sensitive File Scanner     |
======================================
""")

import os, requests
from argparse import ArgumentParser
from random import randint
from concurrent.futures import ThreadPoolExecutor as T

class d1r5:

    def UserAgent(self):

        arr = [
            
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16",
            "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"
        
        ]

        return arr[randint(0, len(arr) - 1)]

    def CheckCode(self, URLCheck):

        try:

            header = {

                "User-Agent": self.UserAgent()

            }

            resp = requests.get(url = URLCheck, headers = header, timeout = self.args.timeout)

            if resp.status_code == 200:

                print("[+] [Found : {}]".format(URLCheck))

            else:

                print("[-] [Not Found : {}]".format(URLCheck))

        except:

            print("[-] [Error : {}]".format(URLCheck))

    def Proc(self, URLTarget, ListFile):

        try:

            if os.path.isfile(ListFile):

                print("[+] [Use List File : {}]".format(ListFile))

                for x in open(ListFile, errors = 'ignore').read().split("\n"):

                    if x != '':

                        T(max_workers = self.args.thread).submit(self.CheckCode, "{}/{}".format(URLTarget, x))

            else:

                print("[-] [Can't Find File : {}]".format(ListFile))

        except:

            print("[-] [Error]")

    def __init__(self):

        parser = ArgumentParser()
        parser.add_argument("-x", "--target", type = str, required = True, help = "Target - URL With Protocol HTTP/HTTPS")
        parser.add_argument("-l", "--list", type = str, required = True, help = "List File of File or Directory Scanner")
        parser.add_argument("-t", "--thread", type = int, required = True, help = "Thread Total")
        parser.add_argument("-d", "--timeout", type = int, required = True, help = "Timeout per Request")
        self.args = parser.parse_args()

        self.Proc(self.args.target, self.args.list)

d1r5() if __name__ == "__main__" else exit()
