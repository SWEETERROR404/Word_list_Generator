from itertools import permutations
import os
logo='''
\033[1;33;40m.---.               .    `.---                 
\___  . , , ,-. ,-. |-    |__  ,-. ,-. ,-. ,-. 
    \ |/|/  |-' |-' |    ,|    |   |   | | |   
`---' ' '   `-' `-' `'   `^--- '   '   `-' ' 
\t\t \033[1;33;40mAn Error is a Sweet Taste
\033[1;32;40m\n▌│█║▌║▌║ \033[1;31;40m█▓▒░░ \033[1;34;40mMubeen Ahmad \033[1;31;40m░░▒▓█\033[1;32;40m ║▌║▌║█│▌\n\t-: Contact me on Facebook :-\n     \033[1;36;40mhttps://m.facebook.com/sweeterror404\033[1;32;40m\n\t-: my Github Account :- \n     \033[1;36;40mhttps://github.com/Sweeterror404\n\t\033[1;32;40m-: Join Facebook Group :-\n  \033[1;36;40mhttps://m.facebook.com/groups/sweeterror404
'''
print(logo)
print("\033[1;33;40m\t  𝐖𝐨𝐫𝐝 𝐋𝐢𝐬𝐭 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫")

def check(filename):
    for i in os.listdir():
        if i == filename+".txt":
            return "found"
def create(filename,passwords):
    with open(f"{filename}.txt", "a") as p:
        p.write(passwords + "\n")

while True:
    passwords = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter Password :- ")
    if len(passwords)<2:
        print("\033[1;32;40mPlease Type Two Characters Must")
    else:
        break

while True:
    save_file = input("\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] Enter The File Name :- ")
    if check(save_file):
        print("\033[1;32;40mFile Are Already Exist")
    else:
        lst = []
        for i in passwords:
            lst.append(i)
        perm = permutations(lst)
        for pos,i in enumerate(perm):
            x = str(i).replace("('", "").replace("')", "").replace("'", "").replace(",", "").replace(" ", "")
            print(f"\033[1;31;40m[\033[1;32;40m*\033[1;31;40m] {pos+1} {x}")
            create(save_file,x)
        print(f"\033[1;32;40mTotal Passwords {pos+1}")
        print(f"\033[1;32;40mPasswords are Saved in {os.getcwd()}/{save_file}.txt")
        break