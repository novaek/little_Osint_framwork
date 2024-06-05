from password import pass2
from mail import adre
from phonenumber import phone

def main():
    print('[+] OSINT Framework')
    print('[+] OSINT Framework> Initiating')
    print('[+] OSINT Framework> Choose a command:')
    print('1) Mail Address Generator')
    print('2) Phone Number Lookup (light)')
    print('3) Password Generator (Heavy Duty)')

    while True:
        try:
            choice = input("Choose> ")
            if choice == "1":
                adre.heheheboy()

            elif choice == "2":
                phone_number = input("[+] Phone number to lookup on (+33)> ")
                phone.main(phone_number)

            elif choice == "3":
                pass2.mnasha()

            else:
                print("Invalid choice. Please choose a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")

        break

if __name__ == "__main__":
    main()
