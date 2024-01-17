# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:40:11 2024

@author: Zonia
"""

from personal_data_form import personal_data

def test_personal_data_form_missing_data():
    result = personal_data("Jan", "Kowalski" , "" , "Dworcowa", 8, "83-154","pozman" ,"Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert not result, "błąd"
       
def test_personal_data_form_no_missing_data():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    print(result)
    assert result
    
def test_personal_data_form_name_and_surname_incorrect():
    result = personal_data("J", "Ko54tr","00257489654" , "Dworcowa", 8, "86-154","Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert not result

def test_personal_data_form_name_and_surname_correct():   
    result = personal_data("Janek","Kowalski","00257489654" , "Dworcowa", 8, "86-154","Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert result
    
def test_personal_data_form_PESEL_incorrect():
    result = personal_data("Janek","Kowalski", "589" , "Dworcowa", 8, "86-154","Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "123875964")
    assert not result

def test_personal_data_form_PESEL_correct():
    result = personal_data("Janek","Kowalski","00257489781" , "Dworcowa", 8, "86-154","Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert result

def test_personal_data_form_street_number_incorrect():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 0, "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert not result
    
def test_personal_data_form_street_number_correct():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert result

def test_personal_data_form_post_code_incorrect():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-14" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert not result

def test_personal_data_form_post_code_correct():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert result

def test_personal_data_form_email_incorrect():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalskigmail.com", "+48123875964")
    assert not result

def test_personal_data_form_email_correct():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert result

def test_personal_data_form_phone_number_incorrect():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "123864")
    assert not result

def test_personal_data_form_phone_number_correct():
    result = personal_data("Jan", "Kowalski", "00257489654" , "Dworcowa", 8 , "86-154" , "Bydgoszcz", "Polska", "jan.kowalski@gmail.com", "+48123875964")
    assert result