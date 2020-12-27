import phonenumbers
from user import number   #create a file name("User") & write number="   "


from phonenumbers import geocoder


                          # "gecoder is the process of converting address into geographic coordinates"

ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))

