import data
import sender_stand_request


def positive_assert(kit_body):  #Assigns a positive response to the test
    auth_token_user = sender_stand_request.get_new_user_token()
    user_response_kit = sender_stand_request.post_new_client_kit(auth_token_user, kit_body)
    assert user_response_kit.json()["name"] == kit_body["name"]
    assert user_response_kit.status_code == 201


def negative_assert(kit_body):  #Assigns a negative response to the test
    auth_token_user = sender_stand_request.get_new_user_token()
    user_response_kit = sender_stand_request.post_new_client_kit(auth_token_user, kit_body)
    assert user_response_kit.status_code == 400


def test_only_one_character():  #Value entered in body
    positive_assert(data.only_one_character)


def test_allow_number_of_characters():  #Value entered in body
    positive_assert(data.allow_number_of_characters)


def test_characters_under_allowed():  #No value entered in body
    negative_assert(data.characters_under_allowed)


def test_characters_above_the_allowed():  #Value entered in body
    negative_assert(data.characters_above_the_allowed)


def test_especial_characters_allowed():  #Value entered in body
    positive_assert(data.especial_characters_allowed)


def test_spaces_are_allowed():  #Value entered in body
    positive_assert(data.spaces_are_allowed)


def test_numbers_are_allowed():  #Value entered in body
    positive_assert(data.numbers_are_allowed)


def test_dont_pass_without_characters():  #No value entered in body
    negative_assert(data.dont_pass_without_characters)


def test_different_parameter():  #Value entered in body
    negative_assert(data.different_parameter)
