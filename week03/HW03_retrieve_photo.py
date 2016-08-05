import random
import urllib.request

MIN = 0
MAX = 1000

def random_num():
    return random.randrange(MIN, MAX, 1)

def generate_name():
    photo_num = str(random_num())
    photo_name = photo_num + '.png'
    return photo_name

def get_file(user_url):
    photo_name = generate_name()
    urllib.request.urlretrieve(user_url, photo_name)
    return photo_name

def get_url():
    # Gives the user an option to enter his own URL instead of the one the computer chose
    # URL has to be valid otherwise the program crashes
    answer = input('Would you like to enter an image URL? Y/N ').lower()
    if (answer == "y"):
        url = input('Enter an image URL (Please make sure your URL is valid): ')
    else:
        url = 'http://dreamatico.com/data_images/sky/sky-2.jpg'
    return url

def main():
    photo_name = get_file(get_url())
    print("Enjoy your photo! It is saved under the name '{0}'".format(photo_name))

main()