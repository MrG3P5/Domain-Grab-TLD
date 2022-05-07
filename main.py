#!/usr/bin/env python3
# Created By X-MrG3P5

import requests, os
from re import findall as reg
from string import ascii_lowercase


class Grab_TLD:
    def __start__(self, extension):
        arr_alphabet = list(ascii_lowercase)
        for y in arr_alphabet:
            try:
                req = requests.get(f"https://www.pagesinventory.com/tld/{extension}/{y}.html")
        
                if req.status_code == 200:
                    regx = reg('<td><a href="\\/domain\\/(.*?).html">', req.text)
                    print(f"[*] Grabbed {len(regx)} Domain")

                    for x in regx:
                        if x in open(f"resut_{extension}.txt", "r").read():
                            pass
                        else:
                            open(f"resut_{extension}.txt", "a").write(x + "\n")

            except:
                print(f"[*] Domain Data Not Found In Page")

if __name__=="__main__":
    os.system("cls||clear")
    tld_input = input("[?] Domain (ex: com) : ")

    try:
        open(f"resut_{tld_input}.txt", "a")
    except:
        pass

    Grab_TLD().__start__(tld_input)
