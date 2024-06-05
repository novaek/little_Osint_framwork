import itertools
from tqdm import tqdm

def mnasha():

    def generate_wordlist(first_name, last_name, birth_year, birth_month, birth_day, favorite_animal, output_file):
        wordlist = []
        
        # Add combinations of first name, last name, and favorite animal
        wordlist.extend([first_name, last_name, favorite_animal])
        
        # Add combinations of birth date
        birth_date_combinations = [
            str(birth_year),
            str(birth_year % 100),  # Last two digits of the birth year
            str(birth_month),
            str(birth_day),
            str(birth_year) + str(birth_month),
            str(birth_year) + str(birth_day),
            str(birth_month) + str(birth_day),
            str(birth_year) + str(birth_month) + str(birth_day)
        ]
        wordlist.extend(birth_date_combinations)
        
        # Open file for writing
        with open(output_file, "w") as bsh:
            # Generate combinations of the provided information
            total_combinations = sum(itertools.combinations(range(len(wordlist)), r).__sizeof__() for r in range(1, len(wordlist) + 1))
            for r in tqdm(range(1, len(wordlist) + 1), desc="Generating wordlist", total=total_combinations):
                combinations = itertools.permutations(wordlist, r)
                for combination in combinations:
                    bsh.write("".join(combination) + '\n')

    # Example usage
    first_name = input("[~] the name of the target > ")
    last_name = input("[@] the family name of the target > ")
    birth_year = int(input("[¤] the birth year of the target > "))
    birth_month = int(input("[¤] the birth month of the target > "))
    birth_day = int(input("[¤] the birth day of the target > "))
    favorite_animal = input("[¤] the favorite animal of the target > ")
    output_file = input("[¤] the output file for the datas > ")

    generate_wordlist(first_name, last_name, birth_year, birth_month, birth_day, favorite_animal, output_file)
