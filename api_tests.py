import logging
import requests
from conftest import auth_token

logging.basicConfig(filename='api_tests.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def test_api_check_post_existence(auth_token):
    headers = {"X-Auth-Token": auth_token}
    params = {"owner": "notMe"}

    try:
        response = requests.get("https://test-stand.gb.ru/api/posts", headers=headers, params=params)
        response.raise_for_status()

        posts = response.json()
        assert any(post['title'] == 'I want drink' for post in posts), "Post not found in the list"

        logging.info("API test_api_check_post_existence passed successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"API test_api_check_post_existence failed. {e}")
        raise

def test_api_create_and_check_post(auth_token):
    headers = {"X-Auth-Token": auth_token}

    new_post_data = {
        "title": "New API Post",
        "description": "Description of the new post",
        "content": "Content of the new post"
    }

    try:
        # Create a new post
        response_create = requests.post("https://test-stand.gb.ru/api/posts", headers=headers, json=new_post_data)
        response_create.raise_for_status()

        created_post = response_create.json()
        assert created_post, "No data received for the created post"

        # Check the existence of the new post by the 'description' field
        response_check = requests.get(f"https://test-stand.gb.ru/api/posts/{created_post['id']}", headers=headers)
        response_check.raise_for_status()

        retrieved_post = response_check.json()
        assert retrieved_post['description'] == new_post_data['description'], "Description of the created post does not match"

        logging.info("API test_api_create_and_check_post passed successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"API test_api_create_and_check_post failed. {e}")
        raise
