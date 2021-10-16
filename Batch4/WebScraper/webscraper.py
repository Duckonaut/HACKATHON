import requests
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

webpage = ''
toaster = ToastNotifier()

# Latest post in LoL news section, new notification whenever it changes, checks every 10 minutes

url_to_check = 'https://www.leagueoflegends.com/en-us/news/game-updates/' # url

element_type = 'h2'

element_class = 'style__Title-sc-1h41bzo-8 fEywOQ'

element_index = 0

def check_for_changes():
    global webpage
    
    try:
        response = requests.get(url_to_check)

        if response.ok:
            content = response.text

            if content != webpage:
                webpage = content

                post_title = extract_post_title(webpage)

                toaster.show_toast("Exam Date Alert", f'New post: {post_title}', duration=10)
        else:
            print(f'ERROR: {response.status_code}')
    except:
        print(f'ENCOUNTERED ERROR')


def extract_post_title(webpage: str) -> str:
    soup = BeautifulSoup(webpage, 'html.parser')

    page_elements = soup.find_all(element_type, { 'class': element_class })

    if len(page_elements) > element_index:
        element = page_elements[element_index]
        return element.get_text()

    return 'NOT FOUND'

while True:
    check_for_changes()
    time.sleep(60 * 10) # 10 minutes