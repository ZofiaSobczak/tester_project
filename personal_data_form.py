# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:12:36 2024

@author: Zonia
"""

### Formularz danych osobowych ###

import re

postcode_pattern = re.compile(r"^\d{2}-\d{3}$")
phone_number_pattern = re.compile(r"^\+\d{2}\d{9}$")
                               
def personal_data (name, surname, PESEL, address, street_number, postcode, city, country, email, phone_number):
    
    if not name or not surname or not PESEL or not address or not street_number or not postcode or not country or not email or not phone_number:
       return False
   
    if not len(name) > 2 or not name.isalpha() or not len(surname) > 2 or not surname.isalpha():
        return False
    
    if not len(PESEL) == 11 and not PESEL.isdigit():
        return False
    
    if not int (street_number) > 0:
        return False
    
    if not postcode_pattern.match(postcode):
        return False
    
    if not "@" in email or "." not in email:
        return False
    
    if not phone_number_pattern.match(phone_number):
        return False
    
    return True


    
    
    