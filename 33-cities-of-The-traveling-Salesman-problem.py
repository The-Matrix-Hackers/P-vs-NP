# My video about 33-cities https://www.youtube.com/watch?v=6h8i87zK0qo
import itertools
num = 1
# Given list of cities
sities = ["Cape Town -->", "Marrakesh -->", "Cairo -->","Johannesburg -->", "Durban -->", "Nairobi -->", "Lagos -->", "Algiers -->", "Accra -->", "Luxor -->", "Dar es Salaam -->", "Stone Town, Zanzibar -->", "Kigali, Rwanda -->", "Essaouira, Morocco -->", "Windhoek, Namibia -->", "Fes, Morocco -->", "Kinshasa -->", "Giza -->", "Luanda -->", "Khartoum -->", "Abidjan -->", "Alexandria -->", "Addis Ababa -->", "Yaoundé -->", "Kano -->", "Ekurhuleni (East Rand) -->", "Douala -->", "Casablanca -->", "Ibadan -->", "Antananarivo -->", "Abuja -->", "Kampala -->", "Kumasi -->"]

# Generate all unique strings without repeating cities
all_strings = set(itertools.permutations(sities))

# Print the result (only one occurrence of each unique string)
for string in all_strings:
    print("".join(string), num)
    num += 1
  
