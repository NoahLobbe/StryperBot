"""
Neater way to store helper functions

Created: Noah Lobbe, 8 December 2023
"""
import logging
import requests
from bs4 import BeautifulSoup
import validators


### Miscellaneous helper functions
def _getDictKey(Dict, value):
    """Returns key from the key:value pair in a dict. Returns None if not found"""
    if type(Dict) == dict:
        for k, v in Dict.items(): 
            if v == value:
                return k
        logging.info("Couldn't find %s in %s", value, Dict)
        return None
    else:
        logging.debug("type error in _getDictKey(), %s is not dict", Dict)
        return None
        
def _str2DList(List):
    """Returns the string of a 2D list. Returns False if List is not a list"""
    if type(List) == list:
        string = ""
        for row in List:
            string += str(row) + '\n'
        return string
    else:
        logging.debug("type error in _str2DList(), %s is not list", List)
        return False




### User input (parsing?) helper functions
def _isYoutube(url):
    """Returns bool and str. Bool for whether 'url' (str) is a youtube video url,
    and str of the youtube video's title if it is legit."""
    is_youtube = False
    R = requests.get(url)
    logging.debug("Requests status: %s", R.status_code)
    html = BeautifulSoup(R.content, features="html.parser")
    if html is not None:

        for tag in html.find_all("link", attrs={'itemprop':'url'}): #simplest and first spot to find ...
            if "href" in tag.attrs.keys(): #HTML tag 'link' would have to have a href right?
                if (tag.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng"): #...stryper's official channel URL
                    is_youtube = True
        #get title
        title = html.find("meta", attrs={"name":"title"}).attrs["content"]
        logging.info("in _isYoutube, is_youtube: %s, title: %s", is_youtube, title)
        return is_youtube, title
    else:
        logging.debug("html is None, weird url??? '%s'", url)
        return False, ""
    

def _cleanYoutubeURL(url):
    """Returns str. Gets rid of extra unneccessary data in url (str)"""
    logging.info("cleaning youtube url...")
    cut_off_index = url.find("&") #first one found is returned, which is the start of extra needless data in url

    if cut_off_index != -1: 
        yt_url = url[:cut_off_index]
    else:
        yt_url = url
    logging.info("url parameters removed: %s", yt_url)
    #If people want to suppress preview of a link, eg. <link string>, the angle brackets need to be removed
    if yt_url[0] == '<':
        yt_url = yt_url[1:]
        logging.info("Removed '<', %s", yt_url)

    if yt_url[-1] == '>':
        yt_url = yt_url[:-1]
        logging.info("Removed '>', %s", yt_url)

    logging.info("Cleaned youtube url: %s", yt_url)
    return yt_url


def _validateYoutubeURL(url):
    """Returns bool as to whether 'url' (str) is legit 
    and if it is actually a youtube video link"""
    logging.info("Validating youtube url...")
    clean_url = _cleanYoutubeURL(url)
    is_valid_url = bool(validators.url(clean_url))
    
    if is_valid_url:
        logging.info("Valid url is cleaned to: %s", clean_url)
        is_youtube, yt_title = _isYoutube(clean_url)
        logging.info("Cleaned url is youtube: %s", is_youtube)
        return is_youtube, yt_title, clean_url       
    else:
        logging.debug("Invalid url! %s", clean_url)
        return False, "", clean_url


def _validateRating(rating_str):
    """Returns bool as to whether rating is valid"""
    try:
        rating = float(rating_str)
        if (rating).is_integer():
            rating = int(rating) #makes the text output nicer later :D
        logging.info("rating conversion successful, %s", rating)
        return (rating >= 0 and rating <= 10)
    except ValueError as e:
        logging.debug("rating is not a float, %s", e)
        return False