import requests

URL = "https://jsonplaceholder.typicode.com/users/1"


def main():
    try:
        response = requests.get(URL, timeout=10)

        if response.status_code == 200:
            data = response.json()

            print("API Request Successful")
            print(f"Name: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"City: {data['address']['city']}")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.RequestException as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
