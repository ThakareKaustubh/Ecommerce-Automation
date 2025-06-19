import os
import requests
from faker import Faker
import random

fake = Faker()


def generate_fake_registration_data():
    birthdate = fake.date_of_birth(minimum_age=18, maximum_age=80)
    return {
        "username": fake.user_name(),
        "email": fake.unique.email(),
        "password": fake.password(),
        "title": random.choice(["Mr", "Ms", "Mrs", "Dr"]),
        "birthdate": {
            "day": birthdate.day,
            "month": birthdate.month,
            "year": birthdate.year
        },
        "address": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "company": fake.company(),
            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "country": fake.country(),
            "zipcode": fake.postcode(),
            "state": fake.state(),
            "city": fake.city(),
            "mobile_number": fake.phone_number()
        }
    }


def create_user_from_api(url):
    data = generate_fake_registration_data()
    payload = {
        "name": data["username"],
        "email": data["email"],
        "password": data["password"],
        "title": data["title"],
        "birth_date": data["birthdate"]["day"],
        "birth_month": data["birthdate"]["month"],
        "birth_year": data["birthdate"]["year"],
        "firstname": data["address"]["first_name"],
        "lastname": data["address"]["last_name"],
        "company": data["address"]["company"],
        "address1": data["address"]["address1"],
        "address2": data["address"]["address2"],
        "country": data["address"]["country"],
        "zipcode": data["address"]["zipcode"],
        "state": data["address"]["state"],
        "city": data["address"]["city"],
        "mobile_number": data["address"]["mobile_number"],
        "form_type": "create_account",
    }

    response = requests.post(f"{url}/api/createAccount", data=payload)

    if response.status_code == 200 and response.json().get("responseCode") == 201:
        return data["email"], data["password"], data["username"]
    elif response.json().get("responseCode") != 200:
        if response.json().get("message") == "Email already exists!":
            return data["email"], data["password"], data["username"]
        else:
            raise Exception(f"User creation failed: {response.text}")
    else:
        raise Exception(f"Unexpected response: {response.status_code} - {response.text}")
