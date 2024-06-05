import requests
import json

def heheheboy():

    def check_email(email):
        url = f"https://leakcheck.io/api/public?check={email}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def generate_emails(first_name, last_name, domains):
        
        email_addresses = []
        
        # Various formats for email addresses
        formats = [
            "{first}.{last}@{domain}",
            "{first}{last}@{domain}",
            "{first}_{last}@{domain}",
            "{first[0]}{last}@{domain}",
            "{first}{last[0]}@{domain}",
            "{last}.{first}@{domain}",
            "{last}{first}@{domain}",
            "{last}_{first}@{domain}"
        ]
        
        for domain in domains:
            for fmt in formats:
                email = fmt.format(first=first_name.lower(), last=last_name.lower(), domain=domain)
                email_addresses.append(email)
        
        return email_addresses

    # Example usage
    first_name = input("[+] the name of the target> ")
    last_name = input("[+] the family name of the target> ")
    output_file = input("[#] output file to save datas> ")
    domains = [
        "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", 
        "aol.com", "icloud.com", "mail.com", "protonmail.com", 
        "yandex.com", "zoho.com"
    ]

    emails = generate_emails(first_name, last_name, domains)

    for email in emails:
        result = check_email(email)
        if result and result['success']:
            print(f"Email: {email}")
            print(f"Found: {result['found']} breaches")
            for source in result['sources']:
                print(f" - Source: {source['name']}, Date: {source['date']}")
                with open(f"2_{output_file}", "a+") as output:
                    output.write(f" - Source:{email}:{source['name']}, Date: {source['date']}"+"\n")
        else:
            continue



    # Open the file once before the loop and write all emails to it
    with open(output_file, "w") as output:
        for email in emails:
            print(email)
            output.write(email + "\n")

    



            
