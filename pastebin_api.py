'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'RERhae4OsH8GKKpMnV9QIGY_yDNRgP4O'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 
    payload = {
        'api_dev_key': API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': '0' if listed else '1'
    }

    # Send the POST request to the PasteBin API
    response = requests.post(PASTEBIN_API_POST_URL, data=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the URL of the new paste
        return response.text
    else:
        # Print the error and return None
        print(f"Error: Unable to post paste. Status code: {response.status_code}")
        return None

if _name_ == '_main_':
    # Test the function (You can remove or comment out this part in production)
    test_title = "Test Paste"
    test_body_text = "This is a test paste."
    test_expiration = "10M"
    test_listed = True
    
    paste_url = post_new_paste(test_title, test_body_text, test_expiration, test_listed)
    print(f"New Paste URL: {paste_url}")
    return