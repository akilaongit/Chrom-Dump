import os
import sys
import sqlite3

# This is the Windows Path
PathName = os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\'
if (os.path.isdir(PathName) == False):
    print('[!] Chrome Doesn\'t exists')
    sys.exit(0)

def DownloadsHash():
	hash_file = open('downloadhash.txt', 'w', encoding="utf-8")
	downloadsPath = PathName + 'History'
	connexion = sqlite3.connect(downloadsPath)
	c = connexion.cursor()
	hashes = c.execute("SELECT guid from downloads ")

	for haash in hashes:
		haash = str(haash)
		hash_file.write("\n,%s" %haash)

	print("Hash file wrote successfully 1:)")

def DownloadsFullReport():
	download_full_file = open('downloadfull.txt', 'w', encoding="utf-8")
	downloadsPath = PathName + 'History'
	connexion = sqlite3.connect(downloadsPath)
	c = connexion.cursor()
	downloads = c.execute("SELECT * from downloads ")

	for download in downloads:
		download = str(download)
		download_full_file.write("\n,%s" %download)

	print("Download full report wrote successfully 1:)")

def History():
	history_file = open('history.txt', 'w', encoding="utf-8")
	historyPath = PathName + 'History'
	connexion = sqlite3.connect(historyPath)
	c = connexion.cursor()
	urls = c.execute("SELECT * from urls")

	for url in urls:
		url = str(url)
		history_file.write("\n,%s" %url)

	print("History file wrote successfully 1:)")

def Cookies():
	cookie_file = open('cookies.txt', 'w', encoding="utf-8")
	cokkiesPath = PathName + 'Cookies'
	connexion = sqlite3.connect(cokkiesPath)
	c = connexion.cursor()
	cookies = c.execute("SELECT * from cookies")

	for cookie in cookies:
		cookie = str(cookie)
		cookie_file.write("\n,%s" %cookie)

	print("Cookie file wrote successfully 1:)")

def mainMenu():
	print('[*]Make sure Google Chrom is closed')
	print("1.History Dump")
	print("2.Downloads Dump")
	print("3.Cookies Dump")
	
	try:
		want = int(input("?> "))
	except ValueError:
		print("Enter number of your choice!")
		want = int(input("?> "))

	if want == 1:
		History()
	elif want == 2:
		print("1.Download Hash Dump")
		print("2.Full Report")

		try:
			want_for_downloads = int(input("?> "))
		except ValueError:
			print("Enter number of your choice!")
			want_for_downloads = int(input("?> "))

		if want_for_downloads == 1:
			DownloadsHash()
		elif want_for_downloads == 2:
			DownloadsFullReport()

	elif want == 3:
		Cookies()

def banner():
	print(f"""		                                                             
	$$$$$$\   $$\                                         
	$$  __$$\ $$ |                                        
	$$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\$$$$\  
	$$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\ 
	$$ |      $$ |  $$ |$$ |  \__|$$ /  $$ |$$ / $$ / $$ |
	$$ |  $$\ $$ |  $$ |$$ |      $$ |  $$ |$$ | $$ | $$ |
	\$$$$$$  |$$ |  $$ |$$ |      \$$$$$$  |$$ | $$ | $$ |
	 \______/ \__|  \__|\__|       \______/ \__| \__| \__|
                                                                                                                                                           
	     $$$$$$$\                                        
	      $$  __$$\                                       
	      $$ |  $$ |$$\   $$\ $$$$$$\$$$$\   $$$$$$\      
	      $$ |  $$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\     
	      $$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ /  $$ |    
	      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |    
	      $$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |    
	      \_______/  \______/ \__| \__| \__|$$  ____/     
	                                        $$ |          
	                                        $$ |          
	                                        \__|       

		[*] Make sure Google Chrom is Closed
		[i]Author: Akila Bandara
		[i]Follow: twitter.com/akklaontweet
		[i]Website: www.akilabandara.rf.gd 
		""")
def main():
	banner()
	mainMenu()

main()