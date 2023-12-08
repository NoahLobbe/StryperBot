"""
Neater way to store helper functions

Created: Noah Lobbe, 8 December 2023
"""
import logging
import requests
from bs4 import BeautifulSoup
import validators

Logger = logging.getLogger( __name__)


### Miscellaneous helper functions
def _getDictKey(Dict, value):
    """Returns key from the key:value pair in a dict. Returns None if not found"""
    if type(Dict) == dict:
        for k, v in Dict.items(): 
            if v == value:
                return k
        Logger.info("Couldn't find %s in %s", value, Dict)
        return None
    else:
        Logger.debug("type error in _getDictKey(), %s is not dict", Dict)
        return None
        
def _str2DList(List):
    """Returns the string of a 2D list. Returns False if List is not a list"""
    if type(List) == list:
        string = ""
        for row in List:
            string += str(row) + '\n'
        return string
    else:
        Logger.debug("type error in _str2DList(), %s is not list", List)
        return False




### User input (parsing?) helper functions
def _isYoutube(url):
    """Returns bool and str. Bool for whether 'url' (str) is a youtube video url,
    and str of the youtube video's title if it is legit."""
    is_youtube = False
    key_str = "https://www.youtube.com/watch?v="
    if key_str in url:
        R = requests.get(url)
        Logger.debug("Requests status: %s", R.status_code)
        html = BeautifulSoup(R.content, features="html.parser")
        if html is not None:

            for tag in html.find_all("link", attrs={'itemprop':'url'}): #simplest and first spot to find ...
                if "href" in tag.attrs.keys(): #HTML tag 'link' would have to have a href right?
                    if (tag.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng"): #...stryper's official channel URL
                        is_youtube = True
            #get title
            result = html.find("meta", attrs={"name":"title"})
            if result is None:
                Logger.debug("meta tag with title not found in url, %s", url)
                return False, ""
            else:
                title = result.attrs["content"]
                Logger.info("in _isYoutube, is_youtube: %s, title: %s", is_youtube, title)
                return is_youtube, title
        else:
            Logger.debug("html is None, weird url??? '%s'", url)
            return False, ""
    else:
        Logger.info("url (%s) doesn't contain '%s', automatic fail", url, key_str)
        return False, ""
    

def _cleanYoutubeURL(url):
    """Returns str. Gets rid of extra unneccessary data in url (str)"""
    Logger.info("cleaning youtube url...")
    cut_off_index = url.find("&") #first one found is returned, which is the start of extra needless data in url

    if cut_off_index != -1: 
        yt_url = url[:cut_off_index]
    else:
        yt_url = url
    Logger.info("url parameters removed: %s", yt_url)
    #If people want to suppress preview of a link, eg. <link string>, the angle brackets need to be removed
    if yt_url[0] == '<':
        yt_url = yt_url[1:]
        Logger.info("Removed '<', %s", yt_url)

    if yt_url[-1] == '>':
        yt_url = yt_url[:-1]
        Logger.info("Removed '>', %s", yt_url)

    Logger.info("Cleaned youtube url: %s", yt_url)
    return yt_url


def _validateYoutubeURL(url):
    """Returns bool as to whether 'url' (str) is legit 
    and if it is actually a youtube video link"""
    Logger.info("Validating youtube url...")
    key_str = "https://www.youtube.com/watch?v="
    if key_str in url:
        clean_url = _cleanYoutubeURL(url)
        is_valid_url = bool(validators.url(clean_url))
        
        if is_valid_url:
            Logger.info("Valid url is cleaned to: %s", clean_url)
            is_youtube, yt_title = _isYoutube(clean_url)
            Logger.info("Cleaned url is youtube: %s", is_youtube)
            return is_youtube, yt_title, clean_url       
        else:
            Logger.debug("Invalid url! %s", clean_url)
            return False, "", clean_url
    else:
        Logger.info("url (%s) doesn't contain '%s', automatic fail", url, key_str)
        return False, "", url


def _validateRating(rating_str):
    """Returns bool as to whether rating is valid"""
    try:
        rating = float(rating_str)
        if (rating).is_integer():
            rating = int(rating) #makes the text output nicer later :D
        Logger.info("rating conversion successful, %s", rating)
        return (rating >= 0 and rating <= 10)
    except ValueError as e:
        Logger.debug("rating is not a float, %s", e)
        return False
    
