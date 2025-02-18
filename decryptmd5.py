import pyfiglet
import sys
import hashlib

def disp():
    print("\n" + "*" * 65) 
    print(pyfiglet.figlet_format("CHAKRA"))
    print("*\t\t\t\tChakra\t\t\t\t*")
    print("*\t\t    geekhacker875@gmail.com\t\t\t*")
    print("*\t      https://github.com/theHackerGeek\t\t*")
    print("*" * 65)
    print("\nDecrypt MD5 Hashes with wordlist")
    print("\n" + "-" * 50)
    args()

def usage():
    print("\nPlease specify MD5 hash and wordlist correctly!")
    print("\nUSAGE:")
    print("\tpython crackmd5hash.py md5hash wordlistpath")
    print("EXAMPLE\n\tpython crackmd5hash.py ab334feeb31c05124cb73fa12571c2f6 /home/wordlist.txt\n")
    print("\tpython crackmd5hash.py ab334feeb31c05124cb73fa12571c2f6 D:\\myfiles\\welcome.txt\n")
    sys.exit(0)

def args():
    try:
        if len(sys.argv) != 3:
            usage()
        work(sys.argv[1], sys.argv[2])
    except KeyboardInterrupt:
        print("\nKeyboard interrupted. Exiting...")
        sys.exit(0)

def work(phash, wlist):
    found = False
    try:
        with open(wlist, "rb") as passfile:  # Open file in binary mode
            print("Working...")
            for line in passfile:
                try:
                    word = line.decode('utf-8', errors='ignore').strip()  # Decode safely
                    if not word:
                        continue
                    digest = hashlib.md5(word.encode('utf-8')).hexdigest()
                    if digest == phash:
                        print(f"\nFound A Match for '{digest}'")
                        print("The Plaintext Is: " + word)
                        found = True
                        break
                except UnicodeDecodeError:
                    continue  # Skip problematic lines

    except FileNotFoundError:
        print("Wordlist Not Found!")
        usage()

    if not found:
        print("\nPlaintext Not Found In Wordlist, Try A Different List\n")

if __name__ == "__main__":
    disp()
