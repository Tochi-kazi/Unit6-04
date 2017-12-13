# Created by: Tochukwu Iroakazi
# Created on: Nov 2017
# Created for: ICS3U
# This program show address with Enum and structure 

from enum import Enum

province = Enum('1','AB','BC','MB','NB','NL','NT','NS','NU','ON','PE','QC','SK','YT')
street = Enum('Baseline','Longsfield','Fallowfield','Claridge','Beatrice')


class Address():
    def __init__(self, First_names, Last_names, Streets, house_numbers, Provinces, Citys, Postal_codes):
      self.First_names = First_names
      self.Last_names = Last_names 
      self.Streets = Streets
      self.Provinces = Provinces
      self.Citys = Citys
      self.Postal_codes = Postal_codes
      self.house_numbers = house_numbers


First_name = raw_input("Type in your first name :")
Last_name = raw_input('Type in your last name: ')
Street = raw_input('Type in your street: ')
while Street not in street:
   print(Street + ' is not a name of a street in your province:')
   Street = raw_input('Type in a valid street: ')
else:
   pass
house_number = raw_input('Type in the number of the house: ')
Province = raw_input('Type in the abbreviation of your province: ')
while Province not in province:
   print(Province + ' is not a province in Canada')
   Province = raw_input('Type in your province: ')
else:
   pass
City = raw_input('Type in your city : ')
Postal_code = raw_input('Type in your postal code: ')


Details = Address(First_name, Last_name, Street, house_number, Province, City, Postal_code)
print(Details.First_names + ' ' + Details.Last_names)
print(Details.house_numbers + ' ' + Details.Streets)
print(Details.Postal_codes + ' ' + Details.Citys + ' ' + Details.Provinces)



