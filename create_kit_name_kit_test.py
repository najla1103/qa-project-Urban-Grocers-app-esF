import configuration
import data
import sender_stand_request
import requests


def positive_assert(kit_body): #Assigns a positive response to the test
    user_response_kit = sender_stand_request.post_new_client_kit(kit_body),
    assert user_response_kit.status_code == 201

def negative_assert(kit_body): #Assigns a negative response to the test
    user_response_kit = sender_stand_request.post_new_client_kit(kit_body)
    assert user_response_kit.status_code == 400

def test_only_one_character(): #Value entered in body
    positive_assert("a")

def test_allow_number_of_characters(): #Value entered in body
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_characters_under_allowed(): #No value entered in body
    negative_assert("")

def test_characters_above_the_allowed(): #Value entered in body
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_especial_characters_allowed(): #Value entered in body
    positive_assert("№%@¡")

def test_spaces_are_allowed(): #Value entered in body
    positive_assert("A Aaa")

def test_numbers_are_allowed(): #Value entered in body
    positive_assert(123)

def test_dont_pass_without_characters(): #No value entered in body
    negative_assert()

def test_diferent_parameter(): #Value entered in body
    negative_assert(123)