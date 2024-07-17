import configuration
import data
import requests


def post_new_user(body): #This function create a new user
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_user_token(): #This function create a new token and atach it to the new user
    new_token = post_new_user(data.user_body)
    response_json = new_token.json()
    auth_token_user = response_json.get("Authorization")
    return auth_token_user #Return the token giving authorization to the new user


def post_new_client_kit(auth_token, kit_body): #Return the token giving authorization to the new user to create a Kit
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response_new_client = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                                        json=kit_body,
                                        headers=headers)
    return response_new_client
