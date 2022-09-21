from subprocess import call
import os

print("""
	
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗██╗  ██╗███████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗████╗ ████║██╔═══██╗████╗  ██║██║ ██╔╝██╔════╝
███████║███████║██║     █████╔╝ █████╗  ██████╔╝██╔████╔██║██║   ██║██╔██╗ ██║█████╔╝ ███████╗
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██║╚██╗██║██╔═██╗ ╚════██║
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║  ██╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
	""") 
	
print ("""
    ///////////////////////////////////
   //                               //
  //      GOA POLICE HACKATHON     //
 //                               //
///////////////////////////////////
""")
	
print ("Select the option below")
print ("1: Capture the criminal")
print ("2: Perform DOS (Denial of Service)")
print ("3: Perform Email Check")
print ("4: List of active darkweb Links")
a = input("Enter the option [1,2,3,4]:")



def dos():
	call(["python", "dos.py"])
	

def mail():
	os.system(email3)
	
	

def darklink():
	os.system("cat darkweb_active.txt")
	
def trapcam():
	os.system("bash camphish.sh")

if a == '1' :
  trapcam()
  
elif a == '2':
  dos()
  
elif a == '3':
  email1="python3 checkmail.py -q "
  email2 = input("Enter the email:")
  email3 = email1+email2	
  mail()
 
elif a == '4':
  darklink()
  
