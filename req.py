from colorama import Fore, init, Style
import requests,os,time


init(convert = True)


logo = """
	███╗ ██╗███╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
	██╔╝███║╚██║    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
	██║ ╚██║ ██║    ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
	██║  ██║ ██║    ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
	███╗ ██║███║    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
	╚══╝ ╚═╝╚══╝    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                                 
	███╗██████╗ ███╗     ██████╗ ███████╗████████╗                   
	██╔╝╚════██╗╚██║    ██╔════╝ ██╔════╝╚══██╔══╝                   
	██║  █████╔╝ ██║    ██║  ███╗█████╗     ██║                      
	██║ ██╔═══╝  ██║    ██║   ██║██╔══╝     ██║                      
	███╗███████╗███║    ╚██████╔╝███████╗   ██║                      
	╚══╝╚══════╝╚══╝     ╚═════╝ ╚══════╝   ╚═╝      

	███╗██████╗ ███╗    ███████╗██╗  ██╗██╗████████╗
	██╔╝╚════██╗╚██║    ██╔════╝╚██╗██╔╝██║╚══██╔══╝
	██║  █████╔╝ ██║    █████╗   ╚███╔╝ ██║   ██║   
	██║  ╚═══██╗ ██║    ██╔══╝   ██╔██╗ ██║   ██║   
	███╗██████╔╝███║    ███████╗██╔╝ ██╗██║   ██║   
	╚══╝╚═════╝ ╚══╝    ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
                                                                                                                
"""

while True:
	print(f"{Fore.GREEN}{logo}")
	print(Fore.CYAN)
	reqopt = input(f"	[+] Choice?\n	[+] ")
	reqopt = reqopt.lower()
	if reqopt == "1" or reqopt == "delete":
		print(Fore.RED)
		link = input("	[-] Link to send a delete request to\n	[+] ")
		requests.delete(link)
		print("	[-] Deleted.")
	elif reqopt == "2" or reqopt == "get": 
		print(Fore.GREEN)
		textornot = input("	[+] Type yes if I should print the response text\n	[+] ")
		textornot = textornot.lower()
		link = input("	[+] Link to send a get request to\n	[+] ")
		details = requests.get(link)
		print(f"	Status code from {link} = {details}")
		if textornot == "yes":
			print(f"	Response text from {link} = {details.text}")
			time.sleep(5)
	elif reqopt == "3" or reqopt == "exit":
		print(Fore.RED)
		print("	[-] Exiting.")
		time.sleep(1)
		os._exit()
	else:
                print("	[-] Invalid option.")
	time.sleep(2)
	os.system("cls")
	
