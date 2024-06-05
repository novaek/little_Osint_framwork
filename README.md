hello, this is a little Osint framwork that should be Improved.

for educational purpose only.

it has a differents modules :

    - mail generator module , which generate patterns of mail adresses and search for possible leaks on the mail adresses (all outputs are saved in a file of your choice)

    - a (French) phone osint module that need to be improved, it can retriev the formatted_number, time_zone, region and the service_provider, 
      and generate an html file that retriev the Aerial Coverage (not really functionnal) (and you'll need an geocode API key in the file called phone.py, 
      that you can have here : https://opencagedata.com/api).

    - a wordlist module that can generate a lot of password with info like, name, family name, birt date and favorite animal (it's a heavy module that almost burned down my
      computer b generating almost 15 millions of potential password in less that 5 min).

to use it, download all the files, and launch the file 1.py like that:

python3 1.py

i'm new, and always open to suggestions to improve my code.

