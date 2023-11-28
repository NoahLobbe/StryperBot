Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
R = requests.get("https://www.youtube.com/watch?v=sG0zAn0dL2I")
R.status_code
200
R.headers
{'Content-Type': 'text/html; charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache', 'Expires': 'Mon, 01 Jan 1990 00:00:00 GMT', 'Date': 'Fri, 24 Nov 2023 03:27:30 GMT', 'Strict-Transport-Security': 'max-age=31536000', 'X-Frame-Options': 'SAMEORIGIN', 'Origin-Trial': 'AvC9UlR6RDk2crliDsFl66RWLnTbHrDbp+DiY6AYz/PNQ4G4tdUTjrHYr2sghbkhGQAVxb7jaPTHpEVBz0uzQwkAAAB4eyJvcmlnaW4iOiJodHRwczovL3lvdXR1YmUuY29tOjQ0MyIsImZlYXR1cmUiOiJXZWJWaWV3WFJlcXVlc3RlZFdpdGhEZXByZWNhdGlvbiIsImV4cGlyeSI6MTcxOTUzMjc5OSwiaXNTdWJkb21haW4iOnRydWV9', 'Content-Security-Policy-Report-Only': "require-trusted-types-for 'script';report-uri /cspreport", 'Permissions-Policy': 'ch-ua-arch=*, ch-ua-bitness=*, ch-ua-full-version=*, ch-ua-full-version-list=*, ch-ua-model=*, ch-ua-wow64=*, ch-ua-form-factor=*, ch-ua-platform=*, ch-ua-platform-version=*', 'Report-To': '{"group":"youtube_main","max_age":2592000,"endpoints":[{"url":"https://csp.withgoogle.com/csp/report-to/youtube_main"}]}', 'Cross-Origin-Opener-Policy': 'same-origin-allow-popups; report-to="youtube_main"', 'P3P': 'CP="This is not a P3P policy! See http://support.google.com/accounts/answer/151657?hl=en-GB for more info."', 'Content-Encoding': 'gzip', 'Server': 'ESF', 'X-XSS-Protection': '0', 'Set-Cookie': 'GPS=1; Domain=.youtube.com; Expires=Fri, 24-Nov-2023 03:57:30 GMT; Path=/; Secure; HttpOnly, YSC=Z65GYmtdG64; Domain=.youtube.com; Path=/; Secure; HttpOnly; SameSite=none, VISITOR_INFO1_LIVE=jvHU_bcqWrw; Domain=.youtube.com; Expires=Wed, 22-May-2024 03:27:30 GMT; Path=/; Secure; HttpOnly; SameSite=none, VISITOR_PRIVACY_METADATA=CgJBVRICGgA%3D; Domain=.youtube.com; Expires=Wed, 22-May-2024 03:27:30 GMT; Path=/; Secure; HttpOnly; SameSite=lax', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000', 'Transfer-Encoding': 'chunked'}
for i in R.headers:
    print(i)

    
Content-Type
X-Content-Type-Options
Cache-Control
Pragma
Expires
Date
Strict-Transport-Security
X-Frame-Options
Origin-Trial
Content-Security-Policy-Report-Only
Permissions-Policy
Report-To
Cross-Origin-Opener-Policy
P3P
Content-Encoding
Server
X-XSS-Protection
Set-Cookie
Alt-Svc
Transfer-Encoding
R.headers["content-type"]
'text/html; charset=utf-8'
R.content

from BeautifulSoup import BeautifulSoup
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    from BeautifulSoup import BeautifulSoup
ModuleNotFoundError: No module named 'BeautifulSoup'
import pytube
from pytube import Channel
C = Channel("http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng")
C.name
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    C.name
AttributeError: 'Channel' object has no attribute 'name'
C.author
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    C.author
AttributeError: 'Channel' object has no attribute 'author'
C.title
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    C.title
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\contrib\playlist.py", line 351, in title
    return self.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer'][
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\contrib\playlist.py", line 93, in sidebar_info
    self._sidebar_info = self.initial_data['sidebar'][
KeyError: 'sidebar'
C.channel_name
'Stryper - Topic'
C.owner
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    C.owner
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\contrib\playlist.py", line 394, in owner
    return self.sidebar_info[1]['playlistSidebarSecondaryInfoRenderer'][
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\pytube\contrib\playlist.py", line 93, in sidebar_info
    self._sidebar_info = self.initial_data['sidebar'][
KeyError: 'sidebar'
R.text

type(R.text)
<class 'str'>
J = R.json()
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 971, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    J = R.json()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
import json
J = R.json()
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 971, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    J = R.json()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
R.json
<bound method Response.json of <Response [200]>>
R.json.keys
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    R.json.keys
AttributeError: 'function' object has no attribute 'keys'
help(R.json)
Help on method json in module requests.models:

json(**kwargs) method of requests.models.Response instance
    Returns the json-encoded content of a response, if any.
    
    :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
    :raises requests.exceptions.JSONDecodeError: If the response body does not
        contain valid json.

R.json["channel_id"]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    R.json["channel_id"]
TypeError: 'method' object is not subscriptable
R.json()
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 971, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    R.json()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
data = json.loads(R.text)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data = json.loads(R.text)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
R.status_code
200
R.data
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    R.data
AttributeError: 'Response' object has no attribute 'data'
R.encoding = "utf-8"
J = R.json()
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 971, in json
    return complexjson.loads(self.text, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    J = R.json()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
from bs4 import BeautifulSoup
html = BeautifulSoup(R.content, features="html.parser")
html.text
'To Hell with the Devil - YouTubeAboutPressCopyrightContact usCreatorAdvertiseDevelopersTermsPrivacyPolicy & SafetyHow YouTube worksTest new features© 2023 Google LLC'
html.content
help(html)
Help on BeautifulSoup in module bs4 object:

class BeautifulSoup(bs4.element.Tag)
 |  BeautifulSoup(markup='', features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, element_classes=None, **kwargs)
 |  
 |  A data structure representing a parsed HTML or XML document.
 |  
 |  Most of the methods you'll call on a BeautifulSoup object are inherited from
 |  PageElement or Tag.
 |  
 |  Internally, this class defines the basic interface called by the
 |  tree builders when converting an HTML/XML document into a data
 |  structure. The interface abstracts away the differences between
 |  parsers. To write a new tree builder, you'll need to understand
 |  these methods as a whole.
 |  
 |  These methods will be called by the BeautifulSoup constructor:
 |    * reset()
 |    * feed(markup)
 |  
 |  The tree builder may call these methods from its feed() implementation:
 |    * handle_starttag(name, attrs) # See note about return value
 |    * handle_endtag(name)
 |    * handle_data(data) # Appends to the current data node
 |    * endData(containerClass) # Ends the current data node
 |  
 |  No matter how complicated the underlying parser is, you should be
 |  able to build a tree using 'start tag' events, 'end tag' events,
 |  'data' events, and "done with data" events.
 |  
 |  If you encounter an empty-element tag (aka a self-closing tag,
 |  like HTML's <br> tag), call handle_starttag and then
 |  handle_endtag.
 |  
 |  Method resolution order:
 |      BeautifulSoup
 |      bs4.element.Tag
 |      bs4.element.PageElement
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __getstate__(self)
 |      Helper for pickle.
 |  
 |  __init__(self, markup='', features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, element_classes=None, **kwargs)
 |      Constructor.
 |      
 |      :param markup: A string or a file-like object representing
 |       markup to be parsed.
 |      
 |      :param features: Desirable features of the parser to be
 |       used. This may be the name of a specific parser ("lxml",
 |       "lxml-xml", "html.parser", or "html5lib") or it may be the
 |       type of markup to be used ("html", "html5", "xml"). It's
 |       recommended that you name a specific parser, so that
 |       Beautiful Soup gives you the same results across platforms
 |       and virtual environments.
 |      
 |      :param builder: A TreeBuilder subclass to instantiate (or
 |       instance to use) instead of looking one up based on
 |       `features`. You only need to use this if you've implemented a
 |       custom TreeBuilder.
 |      
 |      :param parse_only: A SoupStrainer. Only parts of the document
 |       matching the SoupStrainer will be considered. This is useful
 |       when parsing part of a document that would otherwise be too
 |       large to fit into memory.
 |      
 |      :param from_encoding: A string indicating the encoding of the
 |       document to be parsed. Pass this in if Beautiful Soup is
 |       guessing wrongly about the document's encoding.
 |      
 |      :param exclude_encodings: A list of strings indicating
 |       encodings known to be wrong. Pass this in if you don't know
 |       the document's encoding but you know Beautiful Soup's guess is
 |       wrong.
 |      
 |      :param element_classes: A dictionary mapping BeautifulSoup
 |       classes like Tag and NavigableString, to other classes you'd
 |       like to be instantiated instead as the parse tree is
 |       built. This is useful for subclassing Tag or NavigableString
 |       to modify default behavior.
 |      
 |      :param kwargs: For backwards compatibility purposes, the
 |       constructor accepts certain keyword arguments used in
 |       Beautiful Soup 3. None of these arguments do anything in
 |       Beautiful Soup 4; they will result in a warning and then be
 |       ignored.
 |       
 |       Apart from this, any keyword arguments passed into the
 |       BeautifulSoup constructor are propagated to the TreeBuilder
 |       constructor. This makes it possible to configure a
 |       TreeBuilder by passing in arguments, not just by saying which
 |       one to use.
 |  
 |  __setstate__(self, state)
 |  
 |  decode(self, pretty_print=False, eventual_encoding='utf-8', formatter='minimal', iterator=None)
 |      Returns a string or Unicode representation of the parse tree
 |          as an HTML or XML document.
 |      
 |      :param pretty_print: If this is True, indentation will be used to
 |          make the document more readable.
 |      :param eventual_encoding: The encoding of the final document.
 |          If this is None, the document will be a Unicode string.
 |  
 |  endData(self, containerClass=None)
 |      Method called by the TreeBuilder when the end of a data segment
 |      occurs.
 |  
 |  handle_data(self, data)
 |      Called by the tree builder when a chunk of textual data is encountered.
 |  
 |  handle_endtag(self, name, nsprefix=None)
 |      Called by the tree builder when an ending tag is encountered.
 |      
 |      :param name: Name of the tag.
 |      :param nsprefix: Namespace prefix for the tag.
 |  
 |  handle_starttag(self, name, namespace, nsprefix, attrs, sourceline=None, sourcepos=None, namespaces=None)
 |      Called by the tree builder when a new tag is encountered.
 |      
 |      :param name: Name of the tag.
 |      :param nsprefix: Namespace prefix for the tag.
 |      :param attrs: A dictionary of attribute values.
 |      :param sourceline: The line number where this tag was found in its
 |          source document.
 |      :param sourcepos: The character position within `sourceline` where this
 |          tag was found.
 |      :param namespaces: A dictionary of all namespace prefix mappings 
 |          currently in scope in the document.
 |      
 |      If this method returns None, the tag was rejected by an active
 |      SoupStrainer. You should proceed as if the tag had not occurred
 |      in the document. For instance, if this was a self-closing tag,
 |      don't call handle_endtag.
 |  
 |  insert_after(self, *args)
 |      This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
 |      it because there is nothing before or after it in the parse tree.
 |  
 |  insert_before(self, *args)
 |      This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
 |      it because there is nothing before or after it in the parse tree.
 |  
 |  new_string(self, s, subclass=None)
 |      Create a new NavigableString associated with this BeautifulSoup
 |      object.
 |  
 |  new_tag(self, name, namespace=None, nsprefix=None, attrs={}, sourceline=None, sourcepos=None, **kwattrs)
 |      Create a new Tag associated with this BeautifulSoup object.
 |      
 |      :param name: The name of the new Tag.
 |      :param namespace: The URI of the new Tag's XML namespace, if any.
 |      :param prefix: The prefix for the new Tag's XML namespace, if any.
 |      :param attrs: A dictionary of this Tag's attribute values; can
 |          be used instead of `kwattrs` for attributes like 'class'
 |          that are reserved words in Python.
 |      :param sourceline: The line number where this tag was
 |          (purportedly) found in its source document.
 |      :param sourcepos: The character position within `sourceline` where this
 |          tag was (purportedly) found.
 |      :param kwattrs: Keyword arguments for the new Tag's attribute values.
 |  
 |  object_was_parsed(self, o, parent=None, most_recent_element=None)
 |      Method called by the TreeBuilder to integrate an object into the parse tree.
 |  
 |  popTag(self)
 |      Internal method called by _popToTag when a tag is closed.
 |  
 |  pushTag(self, tag)
 |      Internal method called by handle_starttag when a tag is opened.
 |  
 |  reset(self)
 |      Reset this object to a state as though it had never parsed any
 |      markup.
 |  
 |  string_container(self, base_class=None)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  ASCII_SPACES = ' \n\t\x0c\r'
 |  
 |  DEFAULT_BUILDER_FEATURES = ['html', 'fast']
 |  
 |  NO_PARSER_SPECIFIED_WARNING = 'No parser was explicitly specified, so ...
 |  
 |  ROOT_TAG_NAME = '[document]'
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from bs4.element.Tag:
 |  
 |  __bool__(self)
 |      A tag is non-None even if it has no contents.
 |  
 |  __call__(self, *args, **kwargs)
 |      Calling a Tag like a function is the same as calling its
 |      find_all() method. Eg. tag('a') returns a list of all the A tags
 |      found within this tag.
 |  
 |  __contains__(self, x)
 |  
 |  __copy__(self)
 |      A copy of a Tag must always be a deep copy, because a Tag's
 |      children can only have one parent at a time.
 |  
 |  __deepcopy__(self, memo, recursive=True)
 |      A deepcopy of a Tag is a new Tag, unconnected to the parse tree.
 |      Its contents are a copy of the old Tag's contents.
 |  
 |  __delitem__(self, key)
 |      Deleting tag[key] deletes all 'key' attributes for the tag.
 |  
 |  __eq__(self, other)
 |      Returns true iff this Tag has the same name, the same attributes,
 |      and the same contents (recursively) as `other`.
 |  
 |  __getattr__(self, tag)
 |      Calling tag.subtag is the same as calling tag.find(name="subtag")
 |  
 |  __getitem__(self, key)
 |      tag[key] returns the value of the 'key' attribute for the Tag,
 |      and throws an exception if it's not there.
 |  
 |  __hash__(self)
 |      Return hash(self).
 |  
 |  __iter__(self)
 |      Iterating over a Tag iterates over its contents.
 |  
 |  __len__(self)
 |      The length of a Tag is the length of its list of contents.
 |  
 |  __ne__(self, other)
 |      Returns true iff this Tag is not identical to `other`,
 |      as defined in __eq__.
 |  
 |  __repr__ = __unicode__(self)
 |  
 |  __setitem__(self, key, value)
 |      Setting tag[key] sets the value of the 'key' attribute for the
 |      tag.
 |  
 |  __str__ = __unicode__(self)
 |  
 |  __unicode__(self)
 |      Renders this PageElement as a Unicode string.
 |  
 |  childGenerator(self)
 |      Deprecated generator.
 |  
 |  clear(self, decompose=False)
 |      Wipe out all children of this PageElement by calling extract()
 |         on them.
 |      
 |      :param decompose: If this is True, decompose() (a more
 |          destructive method) will be called instead of extract().
 |  
 |  decode_contents(self, indent_level=None, eventual_encoding='utf-8', formatter='minimal')
 |      Renders the contents of this tag as a Unicode string.
 |      
 |      :param indent_level: Each line of the rendering will be
 |         indented this many levels. (The formatter decides what a
 |         'level' means in terms of spaces or other characters
 |         output.) Used internally in recursive calls while
 |         pretty-printing.
 |      
 |      :param eventual_encoding: The tag is destined to be
 |         encoded into this encoding. decode_contents() is _not_
 |         responsible for performing that encoding. This information
 |         is passed in so that it can be substituted in if the
 |         document contains a <META> tag that mentions the document's
 |         encoding.
 |      
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard Formatters.
 |  
 |  decompose(self)
 |      Recursively destroys this PageElement and its children.
 |      
 |      This element will be removed from the tree and wiped out; so
 |      will everything beneath it.
 |      
 |      The behavior of a decomposed PageElement is undefined and you
 |      should never use one for anything, but if you need to _check_
 |      whether an element has been decomposed, you can use the
 |      `decomposed` property.
 |  
 |  encode(self, encoding='utf-8', indent_level=None, formatter='minimal', errors='xmlcharrefreplace')
 |      Render a bytestring representation of this PageElement and its
 |      contents.
 |      
 |      :param encoding: The destination encoding.
 |      :param indent_level: Each line of the rendering will be
 |         indented this many levels. (The formatter decides what a
 |         'level' means in terms of spaces or other characters
 |         output.) Used internally in recursive calls while
 |         pretty-printing.
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard formatters.
 |      :param errors: An error handling strategy such as
 |          'xmlcharrefreplace'. This value is passed along into
 |          encode() and its value should be one of the constants
 |          defined by Python.
 |      :return: A bytestring.
 |  
 |  encode_contents(self, indent_level=None, encoding='utf-8', formatter='minimal')
 |      Renders the contents of this PageElement as a bytestring.
 |      
 |      :param indent_level: Each line of the rendering will be
 |         indented this many levels. (The formatter decides what a
 |         'level' means in terms of spaces or other characters
 |         output.) Used internally in recursive calls while
 |         pretty-printing.
 |      
 |      :param eventual_encoding: The bytestring will be in this encoding.
 |      
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard Formatters.
 |      
 |      :return: A bytestring.
 |  
 |  find(self, name=None, attrs={}, recursive=True, string=None, **kwargs)
 |      Look in the children of this PageElement and find the first
 |      PageElement that matches the given criteria.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param recursive: If this is True, find() will perform a
 |          recursive search of this PageElement's children. Otherwise,
 |          only the direct children will be considered.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  findAll = find_all(self, name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)
 |  
 |  findChild = find(self, name=None, attrs={}, recursive=True, string=None, **kwargs)
 |  
 |  findChildren = find_all(self, name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)
 |  
 |  find_all(self, name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)
 |      Look in the children of this PageElement and find all
 |      PageElements that match the given criteria.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param recursive: If this is True, find_all() will perform a
 |          recursive search of this PageElement's children. Otherwise,
 |          only the direct children will be considered.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |  
 |  get(self, key, default=None)
 |      Returns the value of the 'key' attribute for the tag, or
 |      the value given for 'default' if it doesn't have that
 |      attribute.
 |  
 |  get_attribute_list(self, key, default=None)
 |      The same as get(), but always returns a list.
 |      
 |      :param key: The attribute to look for.
 |      :param default: Use this value if the attribute is not present
 |          on this PageElement.
 |      :return: A list of values, probably containing only a single
 |          value.
 |  
 |  has_attr(self, key)
 |      Does this PageElement have an attribute with the given name?
 |  
 |  has_key(self, key)
 |      Deprecated method. This was kind of misleading because has_key()
 |      (attributes) was different from __in__ (contents).
 |      
 |      has_key() is gone in Python 3, anyway.
 |  
 |  index(self, element)
 |      Find the index of a child by identity, not value.
 |      
 |      Avoids issues with tag.contents.index(element) getting the
 |      index of equal elements.
 |      
 |      :param element: Look for this PageElement in `self.contents`.
 |  
 |  prettify(self, encoding=None, formatter='minimal')
 |      Pretty-print this PageElement as a string.
 |      
 |      :param encoding: The eventual encoding of the string. If this is None,
 |          a Unicode string will be returned.
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard formatters.
 |      :return: A Unicode string (if encoding==None) or a bytestring
 |          (otherwise).
 |  
 |  recursiveChildGenerator(self)
 |      Deprecated generator.
 |  
 |  renderContents(self, encoding='utf-8', prettyPrint=False, indentLevel=0)
 |      Deprecated method for BS3 compatibility.
 |  
 |  select(self, selector, namespaces=None, limit=None, **kwargs)
 |      Perform a CSS selection operation on the current element.
 |      
 |      This uses the SoupSieve library.
 |      
 |      :param selector: A string containing a CSS selector.
 |      
 |      :param namespaces: A dictionary mapping namespace prefixes
 |         used in the CSS selector to namespace URIs. By default,
 |         Beautiful Soup will use the prefixes it encountered while
 |         parsing the document.
 |      
 |      :param limit: After finding this number of results, stop looking.
 |      
 |      :param kwargs: Keyword arguments to be passed into SoupSieve's
 |         soupsieve.select() method.
 |      
 |      :return: A ResultSet of Tags.
 |      :rtype: bs4.element.ResultSet
 |  
 |  select_one(self, selector, namespaces=None, **kwargs)
 |      Perform a CSS selection operation on the current element.
 |      
 |      :param selector: A CSS selector.
 |      
 |      :param namespaces: A dictionary mapping namespace prefixes
 |         used in the CSS selector to namespace URIs. By default,
 |         Beautiful Soup will use the prefixes it encountered while
 |         parsing the document.
 |      
 |      :param kwargs: Keyword arguments to be passed into Soup Sieve's
 |         soupsieve.select() method.
 |      
 |      :return: A Tag.
 |      :rtype: bs4.element.Tag
 |  
 |  smooth(self)
 |      Smooth out this element's children by consolidating consecutive
 |      strings.
 |      
 |      This makes pretty-printed output look more natural following a
 |      lot of operations that modified the tree.
 |  
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from bs4.element.Tag:
 |  
 |  children
 |      Iterate over all direct children of this PageElement.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  css
 |      Return an interface to the CSS selector API.
 |  
 |  descendants
 |      Iterate over all children of this PageElement in a
 |      breadth-first sequence.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  isSelfClosing
 |      Is this tag an empty-element tag? (aka a self-closing tag)
 |      
 |      A tag that has contents is never an empty-element tag.
 |      
 |      A tag that has no contents may or may not be an empty-element
 |      tag. It depends on the builder used to create the tag. If the
 |      builder has a designated list of empty-element tags, then only
 |      a tag whose name shows up in that list is considered an
 |      empty-element tag.
 |      
 |      If the builder has no designated list of empty-element tags,
 |      then any tag with no contents is an empty-element tag.
 |  
 |  is_empty_element
 |      Is this tag an empty-element tag? (aka a self-closing tag)
 |      
 |      A tag that has contents is never an empty-element tag.
 |      
 |      A tag that has no contents may or may not be an empty-element
 |      tag. It depends on the builder used to create the tag. If the
 |      builder has a designated list of empty-element tags, then only
 |      a tag whose name shows up in that list is considered an
 |      empty-element tag.
 |      
 |      If the builder has no designated list of empty-element tags,
 |      then any tag with no contents is an empty-element tag.
 |  
 |  self_and_descendants
 |      Iterate over this PageElement and its children in a
 |      breadth-first sequence.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  strings
 |      Yield all strings of certain classes, possibly stripping them.
 |      
 |      :param strip: If True, all strings will be stripped before being
 |          yielded.
 |      
 |      :param types: A tuple of NavigableString subclasses. Any strings of
 |          a subclass not found in this list will be ignored. By
 |          default, the subclasses considered are the ones found in
 |          self.interesting_string_types. If that's not specified,
 |          only NavigableString and CData objects will be
 |          considered. That means no comments, processing
 |          instructions, etc.
 |      
 |      :yield: A sequence of strings.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from bs4.element.Tag:
 |  
 |  parserClass
 |  
 |  string
 |      Convenience property to get the single string within this
 |      PageElement.
 |      
 |      TODO It might make sense to have NavigableString.string return
 |      itself.
 |      
 |      :return: If this element has a single string child, return
 |       value is that string. If this element has one child tag,
 |       return value is the 'string' attribute of the child tag,
 |       recursively. If this element is itself a string, has no
 |       children, or has more than one child, return value is None.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from bs4.element.Tag:
 |  
 |  DEFAULT_INTERESTING_STRING_TYPES = (<class 'bs4.element.NavigableStrin...
 |  
 |  EMPTY_ELEMENT_EVENT = <object object>
 |  
 |  END_ELEMENT_EVENT = <object object>
 |  
 |  START_ELEMENT_EVENT = <object object>
 |  
 |  STRING_ELEMENT_EVENT = <object object>
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from bs4.element.PageElement:
 |  
 |  append(self, tag)
 |      Appends the given PageElement to the contents of this one.
 |      
 |      :param tag: A PageElement.
 |  
 |  extend(self, tags)
 |      Appends the given PageElements to this one's contents.
 |      
 |      :param tags: A list of PageElements. If a single Tag is
 |          provided instead, this PageElement's contents will be extended
 |          with that Tag's contents.
 |  
 |  extract(self, _self_index=None)
 |      Destructively rips this element out of the tree.
 |      
 |      :param _self_index: The location of this element in its parent's
 |         .contents, if known. Passing this in allows for a performance
 |         optimization.
 |      
 |      :return: `self`, no longer part of the tree.
 |  
 |  fetchNextSiblings = find_next_siblings(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  fetchParents = find_parents(self, name=None, attrs={}, limit=None, **kwargs)
 |  
 |  fetchPrevious = find_all_previous(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  fetchPreviousSiblings = find_previous_siblings(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  findAllNext = find_all_next(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  findAllPrevious = find_all_previous(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  findNext = find_next(self, name=None, attrs={}, string=None, **kwargs)
 |  
 |  findNextSibling = find_next_sibling(self, name=None, attrs={}, string=None, **kwargs)
 |  
 |  findNextSiblings = find_next_siblings(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  findParent = find_parent(self, name=None, attrs={}, **kwargs)
 |  
 |  findParents = find_parents(self, name=None, attrs={}, limit=None, **kwargs)
 |  
 |  findPrevious = find_previous(self, name=None, attrs={}, string=None, **kwargs)
 |  
 |  findPreviousSibling = find_previous_sibling(self, name=None, attrs={}, string=None, **kwargs)
 |  
 |  findPreviousSiblings = find_previous_siblings(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |  
 |  find_all_next(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |      Find all PageElements that match the given criteria and appear
 |      later in the document than this PageElement.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet containing PageElements.
 |  
 |  find_all_previous(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |      Look backwards in the document from this PageElement and find all
 |      PageElements that match the given criteria.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |  
 |  find_next(self, name=None, attrs={}, string=None, **kwargs)
 |      Find the first PageElement that matches the given criteria and
 |      appears later in the document than this PageElement.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  find_next_sibling(self, name=None, attrs={}, string=None, **kwargs)
 |      Find the closest sibling to this PageElement that matches the
 |      given criteria and appears later in the document.
 |      
 |      All find_* methods take a common set of arguments. See the
 |      online documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  find_next_siblings(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |      Find all siblings of this PageElement that match the given criteria
 |      and appear later in the document.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |  
 |  find_parent(self, name=None, attrs={}, **kwargs)
 |      Find the closest parent of this PageElement that matches the given
 |      criteria.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :kwargs: A dictionary of filters on attribute values.
 |      
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  find_parents(self, name=None, attrs={}, limit=None, **kwargs)
 |      Find all parents of this PageElement that match the given criteria.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  find_previous(self, name=None, attrs={}, string=None, **kwargs)
 |      Look backwards in the document from this PageElement and find the
 |      first PageElement that matches the given criteria.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  find_previous_sibling(self, name=None, attrs={}, string=None, **kwargs)
 |      Returns the closest sibling to this PageElement that matches the
 |      given criteria and appears earlier in the document.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  find_previous_siblings(self, name=None, attrs={}, string=None, limit=None, **kwargs)
 |      Returns all siblings to this PageElement that match the
 |      given criteria and appear earlier in the document.
 |      
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |      
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param string: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |  
 |  format_string(self, s, formatter)
 |      Format the given string using the given formatter.
 |      
 |      :param s: A string.
 |      :param formatter: A Formatter object, or a string naming one of the standard formatters.
 |  
 |  formatter_for_name(self, formatter)
 |      Look up or create a Formatter for the given identifier,
 |      if necessary.
 |      
 |      :param formatter: Can be a Formatter object (used as-is), a
 |          function (used as the entity substitution hook for an
 |          XMLFormatter or HTMLFormatter), or a string (used to look
 |          up an XMLFormatter or HTMLFormatter in the appropriate
 |          registry.
 |  
 |  getText = get_text(self, separator='', strip=False, types=<object object at 0x000001611FE14860>)
 |  
 |  get_text(self, separator='', strip=False, types=<object object at 0x000001611FE14860>)
 |      Get all child strings of this PageElement, concatenated using the
 |      given separator.
 |      
 |      :param separator: Strings will be concatenated using this separator.
 |      
 |      :param strip: If True, strings will be stripped before being
 |          concatenated.
 |      
 |      :param types: A tuple of NavigableString subclasses. Any
 |          strings of a subclass not found in this list will be
 |          ignored. Although there are exceptions, the default
 |          behavior in most cases is to consider only NavigableString
 |          and CData objects. That means no comments, processing
 |          instructions, etc.
 |      
 |      :return: A string.
 |  
 |  insert(self, position, new_child)
 |      Insert a new PageElement in the list of this PageElement's children.
 |      
 |      This works the same way as `list.insert`.
 |      
 |      :param position: The numeric position that should be occupied
 |         in `self.children` by the new PageElement.
 |      :param new_child: A PageElement.
 |  
 |  nextGenerator(self)
 |      # Old non-property versions of the generators, for backwards
 |      # compatibility with BS3.
 |  
 |  nextSiblingGenerator(self)
 |  
 |  parentGenerator(self)
 |  
 |  previousGenerator(self)
 |  
 |  previousSiblingGenerator(self)
 |  
 |  replaceWith = replace_with(self, *args)
 |  
 |  replaceWithChildren = unwrap(self)
 |  
 |  replace_with(self, *args)
 |      Replace this PageElement with one or more PageElements, keeping the
 |      rest of the tree the same.
 |      
 |      :param args: One or more PageElements.
 |      :return: `self`, no longer part of the tree.
 |  
 |  replace_with_children = unwrap(self)
 |  
 |  setup(self, parent=None, previous_element=None, next_element=None, previous_sibling=None, next_sibling=None)
 |      Sets up the initial relations between this element and
 |      other elements.
 |      
 |      :param parent: The parent of this element.
 |      
 |      :param previous_element: The element parsed immediately before
 |          this one.
 |      
 |      :param next_element: The element parsed immediately before
 |          this one.
 |      
 |      :param previous_sibling: The most recently encountered element
 |          on the same level of the parse tree as this one.
 |      
 |      :param previous_sibling: The next element to be encountered
 |          on the same level of the parse tree as this one.
 |  
 |  unwrap(self)
 |      Replace this PageElement with its contents.
 |      
 |      :return: `self`, no longer part of the tree.
 |  
 |  wrap(self, wrap_inside)
 |      Wrap this PageElement inside another one.
 |      
 |      :param wrap_inside: A PageElement.
 |      :return: `wrap_inside`, occupying the position in the tree that used
 |         to be occupied by `self`, and with `self` inside it.
 |  
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from bs4.element.PageElement:
 |  
 |  decomposed
 |      Check whether a PageElement has been decomposed.
 |      
 |      :rtype: bool
 |  
 |  next
 |      The PageElement, if any, that was parsed just after this one.
 |      
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  next_elements
 |      All PageElements that were parsed after this one.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  next_siblings
 |      All PageElements that are siblings of this one but were parsed
 |      later.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  parents
 |      All PageElements that are parents of this PageElement.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  previous
 |      The PageElement, if any, that was parsed just before this one.
 |      
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |  
 |  previous_elements
 |      All PageElements that were parsed before this one.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  previous_siblings
 |      All PageElements that are siblings of this one but were parsed
 |      earlier.
 |      
 |      :yield: A sequence of PageElements.
 |  
 |  stripped_strings
 |      Yield all strings in this PageElement, stripping them first.
 |      
 |      :yield: A sequence of stripped strings.
 |  
 |  text
 |      Get all child strings of this PageElement, concatenated using the
 |      given separator.
 |      
 |      :param separator: Strings will be concatenated using this separator.
 |      
 |      :param strip: If True, strings will be stripped before being
 |          concatenated.
 |      
 |      :param types: A tuple of NavigableString subclasses. Any
 |          strings of a subclass not found in this list will be
 |          ignored. Although there are exceptions, the default
 |          behavior in most cases is to consider only NavigableString
 |          and CData objects. That means no comments, processing
 |          instructions, etc.
 |      
 |      :return: A string.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from bs4.element.PageElement:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  nextSibling
 |  
 |  previousSibling
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from bs4.element.PageElement:
 |  
 |  default = <object object>
 |  
 |  known_xml = None

'Stryper" in html
                                                         
SyntaxError: unterminated string literal (detected at line 1)
"Stryper" in html
                                                         
False
"owner" in html
                                                         
False
type(html)
                                                         
<class 'bs4.BeautifulSoup'>
html.find_all("div")
                                                         

for i in html.find_all("div"):
    print(i)

                                                         
<div class="watch-main-col" id="watch7-content" itemid="" itemscope="" itemtype="http://schema.org/VideoObject"><link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/><meta content="To Hell with the Devil" itemprop="name"/><meta content="Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc..." itemprop="description"/><meta content="False" itemprop="requiresSubscription"/><meta content="sG0zAn0dL2I" itemprop="identifier"/><meta content="PT4M5S" itemprop="duration"/><span itemprop="author" itemscope="" itemtype="http://schema.org/Person"><link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/><link content="Stryper - Topic" itemprop="name"/></span><script nonce="IrvoVklBlQOW5t6z7RMPLw" type="application/ld+json">{"@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@id": "http:\/\/www.youtube.com\/channel\/UC20qdRIIoh4Xr6jnmZ4HBng", "name": "Stryper - Topic"}}]}</script><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="thumbnailUrl"/><span itemprop="thumbnail" itemscope="" itemtype="http://schema.org/ImageObject"><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/><meta content="1280" itemprop="width"/><meta content="720" itemprop="height"/></span><link href="https://www.youtube.com/embed/sG0zAn0dL2I" itemprop="embedUrl"/><meta content="HTML5 Flash" itemprop="playerType"/><meta content="960" itemprop="width"/><meta content="720" itemprop="height"/><meta content="true" itemprop="isFamilyFriendly"/><meta content="AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA" itemprop="regionsAllowed"/><meta content="1685732" itemprop="interactionCount"/><meta content="2018-07-25T20:04:48-07:00" itemprop="datePublished"/><meta content="2018-07-25T20:04:48-07:00" itemprop="uploadDate"/><meta content="Music" itemprop="genre"/></div>
<div class="skeleton flexy" id="player"><div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div></div>
<div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div>
<div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div>
<div class="round" id="player-api"></div>
<div class="watch-skeleton" id="watch-page-skeleton"><div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div></div>
<div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div>
<div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div>
<div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div>
<div class="skeleton-bg-color" id="upnext"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
<div class="thumbnail skeleton-bg-color"></div>
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
<div class="video-title text-shell skeleton-bg-color"></div>
<div class="video-meta text-shell skeleton-bg-color"></div>
<div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div>
<div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div>
<div class="text-shell skeleton-bg-color" id="title"></div>
<div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div>
<div class="text-shell skeleton-bg-color" id="count"></div>
<div class="flex-1"></div>
<div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div>
<div class="menu-button skeleton-bg-color"></div>
<div class="menu-button skeleton-bg-color"></div>
<div class="menu-button skeleton-bg-color"></div>
<div class="menu-button skeleton-bg-color"></div>
<div class="menu-button skeleton-bg-color"></div>
<div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div>
<div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div>
<div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div>
<div class="skeleton-bg-color" id="channel-icon"></div>
<div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div>
<div class="text-shell skeleton-bg-color" id="owner-name"></div>
<div class="text-shell skeleton-bg-color" id="published-date"></div>
<div class="skeleton-bg-color" id="subscribe-button"></div>
<div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div>
<div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div>

<div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div>
<div class="masthead-skeleton-icon"></div>
<div class="masthead-skeleton-icon"></div>
<div class="masthead-skeleton-icon"></div>
<div id="copyright" slot="copyright" style="display: none;"><div dir="ltr" style="display:inline">© 2023 Google LLC</div></div>
<div dir="ltr" style="display:inline">© 2023 Google LLC</div>
for i in html.find_all("div"):
    if "owner" in i or "channel" in i:
        print(i)

                                                         
type(html.find_all("div"))
                                                         
<class 'bs4.element.ResultSet'>
html.find_all("div")[0]
                                                         
<div class="watch-main-col" id="watch7-content" itemid="" itemscope="" itemtype="http://schema.org/VideoObject"><link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/><meta content="To Hell with the Devil" itemprop="name"/><meta content="Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc..." itemprop="description"/><meta content="False" itemprop="requiresSubscription"/><meta content="sG0zAn0dL2I" itemprop="identifier"/><meta content="PT4M5S" itemprop="duration"/><span itemprop="author" itemscope="" itemtype="http://schema.org/Person"><link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/><link content="Stryper - Topic" itemprop="name"/></span><script nonce="IrvoVklBlQOW5t6z7RMPLw" type="application/ld+json">{"@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@id": "http:\/\/www.youtube.com\/channel\/UC20qdRIIoh4Xr6jnmZ4HBng", "name": "Stryper - Topic"}}]}</script><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="thumbnailUrl"/><span itemprop="thumbnail" itemscope="" itemtype="http://schema.org/ImageObject"><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/><meta content="1280" itemprop="width"/><meta content="720" itemprop="height"/></span><link href="https://www.youtube.com/embed/sG0zAn0dL2I" itemprop="embedUrl"/><meta content="HTML5 Flash" itemprop="playerType"/><meta content="960" itemprop="width"/><meta content="720" itemprop="height"/><meta content="true" itemprop="isFamilyFriendly"/><meta content="AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA" itemprop="regionsAllowed"/><meta content="1685732" itemprop="interactionCount"/><meta content="2018-07-25T20:04:48-07:00" itemprop="datePublished"/><meta content="2018-07-25T20:04:48-07:00" itemprop="uploadDate"/><meta content="Music" itemprop="genre"/></div>
type(html.find_all("div")[0])
                                                         
<class 'bs4.element.Tag'>
for i in html.find_all("div"):
    if "owner" in i['id']:
        print("0", i)
    if "channel" in i['id']:
        print("1", i)

                                                         
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    if "owner" in i['id']:
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 1573, in __getitem__
    return self.attrs[key]
KeyError: 'id'
for i in html.find_all("div"):
    if "owner" in i.b['id']:
        print("0", i)
    if "channel" in i.b['id']:
        print("1", i)

        
Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    if "owner" in i.b['id']:
TypeError: 'NoneType' object is not subscriptable
for i in html.find_all("div"):
    print(type(i))
    
    if "owner" in i.b['id']:
        print("0", i)
    if "channel" in i.b['id']:
        print("1", i)

        
<class 'bs4.element.Tag'>
Traceback (most recent call last):
  File "<pyshell#56>", line 4, in <module>
    if "owner" in i.b['id']:
TypeError: 'NoneType' object is not subscriptable
for i in html.find_all("div"):
    print(type(i))
    print(i.attrs)

    
<class 'bs4.element.Tag'>
{'id': 'watch7-content', 'class': ['watch-main-col'], 'itemscope': '', 'itemid': '', 'itemtype': 'http://schema.org/VideoObject'}
<class 'bs4.element.Tag'>
{'id': 'player', 'class': ['skeleton', 'flexy']}
<class 'bs4.element.Tag'>
{'id': 'player-wrap'}
<class 'bs4.element.Tag'>
{'id': 'player-placeholder', 'style': "background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');", 'class': []}
<class 'bs4.element.Tag'>
{'id': 'player-api', 'class': ['round']}
<class 'bs4.element.Tag'>
{'id': 'watch-page-skeleton', 'class': ['watch-skeleton']}
<class 'bs4.element.Tag'>
{'id': 'container'}
<class 'bs4.element.Tag'>
{'id': 'related'}
<class 'bs4.element.Tag'>
{'class': ['autoplay', 'skeleton-light-border-bottom']}
<class 'bs4.element.Tag'>
{'id': 'upnext', 'class': ['skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['video-skeleton']}
<class 'bs4.element.Tag'>
{'class': ['video-details']}
<class 'bs4.element.Tag'>
{'class': ['thumbnail', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['details', 'flex-1']}
<class 'bs4.element.Tag'>
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['video-skeleton']}
<class 'bs4.element.Tag'>
{'class': ['video-details']}
<class 'bs4.element.Tag'>
{'class': ['thumbnail', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['details', 'flex-1']}
<class 'bs4.element.Tag'>
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
{'class': ['video-skeleton']}
<class 'bs4.element.Tag'>
{'class': ['video-details']}
<class 'bs4.element.Tag'>
{'class': ['thumbnail', 'skeleton-bg-color']}
<class 'bs4.element.Tag'>
Traceback (most recent call last):
  File "<pyshell#59>", line 2, in <module>
    print(type(i))
KeyboardInterrupt
for i in html.find_all("div"):
    print(i.attrs)

    
{'id': 'watch7-content', 'class': ['watch-main-col'], 'itemscope': '', 'itemid': '', 'itemtype': 'http://schema.org/VideoObject'}
{'id': 'player', 'class': ['skeleton', 'flexy']}
{'id': 'player-wrap'}
{'id': 'player-placeholder', 'style': "background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');", 'class': []}
{'id': 'player-api', 'class': ['round']}
{'id': 'watch-page-skeleton', 'class': ['watch-skeleton']}
{'id': 'container'}
{'id': 'related'}
{'class': ['autoplay', 'skeleton-light-border-bottom']}
{'id': 'upnext', 'class': ['skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'id': 'info-container'}
{'id': 'primary-info', 'class': ['skeleton-light-border-bottom']}
{'id': 'title', 'class': ['text-shell', 'skeleton-bg-color']}
{'id': 'info'}
{'id': 'count', 'class': ['text-shell', 'skeleton-bg-color']}
{'class': ['flex-1']}
{'id': 'menu'}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'id': 'secondary-info', 'class': ['skeleton-light-border-bottom']}
{'id': 'top-row'}
{'id': 'video-owner', 'class': ['flex-1']}
{'id': 'channel-icon', 'class': ['skeleton-bg-color']}
{'id': 'upload-info', 'class': ['flex-1']}
{'id': 'owner-name', 'class': ['text-shell', 'skeleton-bg-color']}
{'id': 'published-date', 'class': ['text-shell', 'skeleton-bg-color']}
{'id': 'subscribe-button', 'class': ['skeleton-bg-color']}
{'id': 'search-container', 'class': ['ytd-searchbox-spt'], 'slot': 'search-container'}
{'id': 'search-input', 'class': ['ytd-searchbox-spt'], 'slot': 'search-input'}
{'id': 'masthead-logo', 'slot': 'masthead-logo'}
{'id': 'masthead-skeleton-icons', 'slot': 'masthead-skeleton'}
{'class': ['masthead-skeleton-icon']}
{'class': ['masthead-skeleton-icon']}
{'class': ['masthead-skeleton-icon']}
{'id': 'copyright', 'slot': 'copyright', 'style': 'display: none;'}
{'dir': 'ltr', 'style': 'display:inline'}
for i in html.find_all("ytd-channel-name"):
    print(i.attrs)

    
for i in html.find_all("meta"):
    print(i.attrs)

    
{'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'}
{'http-equiv': 'origin-trial', 'content': 'ApvK67ociHgr2egd6c2ZjrfPuRs8BHcvSggogIOPQNH7GJ3cVlyJ1NOq/COCdj0+zxskqHt9HgLLETc8qqD+vwsAAABteyJvcmlnaW4iOiJodHRwczovL3lvdXR1YmUuY29tOjQ0MyIsImZlYXR1cmUiOiJQcml2YWN5U2FuZGJveEFkc0FQSXMiLCJleHBpcnkiOjE2OTUxNjc5OTksImlzU3ViZG9tYWluIjp0cnVlfQ=='}
{'name': 'theme-color', 'content': 'rgba(255, 255, 255, 0.98)'}
{'name': 'title', 'content': 'To Hell with the Devil'}
{'name': 'description', 'content': 'Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc...'}
{'name': 'keywords', 'content': 'Stryper, ストライパー, To Hell With The Devil, To Hell with the Devil, トゥヘルウィズザデビル, トゥ・ヘル・ウィズ・ザ・デヴィル'}
{'property': 'og:site_name', 'content': 'YouTube'}
{'property': 'og:url', 'content': 'https://www.youtube.com/watch?v=sG0zAn0dL2I'}
{'property': 'og:title', 'content': 'To Hell with the Devil'}
{'property': 'og:image', 'content': 'https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg'}
{'property': 'og:image:width', 'content': '1280'}
{'property': 'og:image:height', 'content': '720'}
{'property': 'og:description', 'content': 'Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc...'}
{'property': 'al:ios:app_store_id', 'content': '544007664'}
{'property': 'al:ios:app_name', 'content': 'YouTube'}
{'property': 'al:ios:url', 'content': 'vnd.youtube://www.youtube.com/watch?v=sG0zAn0dL2I&feature=applinks'}
{'property': 'al:android:url', 'content': 'vnd.youtube://www.youtube.com/watch?v=sG0zAn0dL2I&feature=applinks'}
{'property': 'al:web:url', 'content': 'http://www.youtube.com/watch?v=sG0zAn0dL2I&feature=applinks'}
{'property': 'og:type', 'content': 'video.other'}
{'property': 'og:video:url', 'content': 'https://www.youtube.com/embed/sG0zAn0dL2I'}
{'property': 'og:video:secure_url', 'content': 'https://www.youtube.com/embed/sG0zAn0dL2I'}
{'property': 'og:video:type', 'content': 'text/html'}
{'property': 'og:video:width', 'content': '960'}
{'property': 'og:video:height', 'content': '720'}
{'property': 'al:android:app_name', 'content': 'YouTube'}
{'property': 'al:android:package', 'content': 'com.google.android.youtube'}
{'property': 'og:video:tag', 'content': 'Stryper'}
{'property': 'og:video:tag', 'content': 'ストライパー'}
{'property': 'og:video:tag', 'content': 'To Hell With The Devil'}
{'property': 'og:video:tag', 'content': 'To Hell with the Devil'}
{'property': 'og:video:tag', 'content': 'トゥヘルウィズザデビル'}
{'property': 'og:video:tag', 'content': 'トゥ・ヘル・ウィズ・ザ・デヴィル'}
{'property': 'fb:app_id', 'content': '87741124305'}
{'name': 'twitter:card', 'content': 'player'}
{'name': 'twitter:site', 'content': '@youtube'}
{'name': 'twitter:url', 'content': 'https://www.youtube.com/watch?v=sG0zAn0dL2I'}
{'name': 'twitter:title', 'content': 'To Hell with the Devil'}
{'name': 'twitter:description', 'content': 'Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc...'}
{'name': 'twitter:image', 'content': 'https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg'}
{'name': 'twitter:app:name:iphone', 'content': 'YouTube'}
{'name': 'twitter:app:id:iphone', 'content': '544007664'}
{'name': 'twitter:app:name:ipad', 'content': 'YouTube'}
{'name': 'twitter:app:id:ipad', 'content': '544007664'}
{'name': 'twitter:app:url:iphone', 'content': 'vnd.youtube://www.youtube.com/watch?v=sG0zAn0dL2I&feature=applinks'}
{'name': 'twitter:app:url:ipad', 'content': 'vnd.youtube://www.youtube.com/watch?v=sG0zAn0dL2I&feature=applinks'}
{'name': 'twitter:app:name:googleplay', 'content': 'YouTube'}
{'name': 'twitter:app:id:googleplay', 'content': 'com.google.android.youtube'}
{'name': 'twitter:app:url:googleplay', 'content': 'https://www.youtube.com/watch?v=sG0zAn0dL2I'}
{'name': 'twitter:player', 'content': 'https://www.youtube.com/embed/sG0zAn0dL2I'}
{'name': 'twitter:player:width', 'content': '960'}
{'name': 'twitter:player:height', 'content': '720'}
{'itemprop': 'name', 'content': 'To Hell with the Devil'}
{'itemprop': 'description', 'content': 'Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc...'}
{'itemprop': 'requiresSubscription', 'content': 'False'}
{'itemprop': 'identifier', 'content': 'sG0zAn0dL2I'}
{'itemprop': 'duration', 'content': 'PT4M5S'}
{'itemprop': 'width', 'content': '1280'}
{'itemprop': 'height', 'content': '720'}
{'itemprop': 'playerType', 'content': 'HTML5 Flash'}
{'itemprop': 'width', 'content': '960'}
{'itemprop': 'height', 'content': '720'}
{'itemprop': 'isFamilyFriendly', 'content': 'true'}
{'itemprop': 'regionsAllowed', 'content': 'AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA'}
{'itemprop': 'interactionCount', 'content': '1685732'}
{'itemprop': 'datePublished', 'content': '2018-07-25T20:04:48-07:00'}
{'itemprop': 'uploadDate', 'content': '2018-07-25T20:04:48-07:00'}
{'itemprop': 'genre', 'content': 'Music'}
for i in html.find_all("div"):
    print(i.attrs)
    if 'id' in i.attrs.keys():
        print(i.attrs['id'])

        
{'id': 'watch7-content', 'class': ['watch-main-col'], 'itemscope': '', 'itemid': '', 'itemtype': 'http://schema.org/VideoObject'}
watch7-content
{'id': 'player', 'class': ['skeleton', 'flexy']}
player
{'id': 'player-wrap'}
player-wrap
{'id': 'player-placeholder', 'style': "background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');", 'class': []}
player-placeholder
{'id': 'player-api', 'class': ['round']}
player-api
{'id': 'watch-page-skeleton', 'class': ['watch-skeleton']}
watch-page-skeleton
{'id': 'container'}
container
{'id': 'related'}
related
{'class': ['autoplay', 'skeleton-light-border-bottom']}
{'id': 'upnext', 'class': ['skeleton-bg-color']}
upnext
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-skeleton']}
{'class': ['video-details']}
{'class': ['thumbnail', 'skeleton-bg-color']}
{'class': ['details', 'flex-1']}
{'class': ['video-title', 'text-shell', 'skeleton-bg-color']}
{'class': ['video-meta', 'text-shell', 'skeleton-bg-color']}
{'id': 'info-container'}
info-container
{'id': 'primary-info', 'class': ['skeleton-light-border-bottom']}
primary-info
{'id': 'title', 'class': ['text-shell', 'skeleton-bg-color']}
title
{'id': 'info'}
info
{'id': 'count', 'class': ['text-shell', 'skeleton-bg-color']}
count
{'class': ['flex-1']}
{'id': 'menu'}
menu
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'class': ['menu-button', 'skeleton-bg-color']}
{'id': 'secondary-info', 'class': ['skeleton-light-border-bottom']}
secondary-info
{'id': 'top-row'}
top-row
{'id': 'video-owner', 'class': ['flex-1']}
video-owner
{'id': 'channel-icon', 'class': ['skeleton-bg-color']}
channel-icon
{'id': 'upload-info', 'class': ['flex-1']}
upload-info
{'id': 'owner-name', 'class': ['text-shell', 'skeleton-bg-color']}
owner-name
{'id': 'published-date', 'class': ['text-shell', 'skeleton-bg-color']}
published-date
{'id': 'subscribe-button', 'class': ['skeleton-bg-color']}
subscribe-button
{'id': 'search-container', 'class': ['ytd-searchbox-spt'], 'slot': 'search-container'}
search-container
{'id': 'search-input', 'class': ['ytd-searchbox-spt'], 'slot': 'search-input'}
search-input
{'id': 'masthead-logo', 'slot': 'masthead-logo'}
masthead-logo
{'id': 'masthead-skeleton-icons', 'slot': 'masthead-skeleton'}
masthead-skeleton-icons
{'class': ['masthead-skeleton-icon']}
{'class': ['masthead-skeleton-icon']}
{'class': ['masthead-skeleton-icon']}
{'id': 'copyright', 'slot': 'copyright', 'style': 'display: none;'}
copyright
{'dir': 'ltr', 'style': 'display:inline'}
for i in html.find_all("div"):
    if 'id' in i.attrs.keys():
        print(i.attrs['id'])

        
watch7-content
player
player-wrap
player-placeholder
player-api
watch-page-skeleton
container
related
upnext
info-container
primary-info
title
info
count
menu
secondary-info
top-row
video-owner
channel-icon
upload-info
owner-name
published-date
subscribe-button
search-container
search-input
masthead-logo
masthead-skeleton-icons
copyright
for i in html.find_all("div"):
    msg = str(i)
    if 'id' in i.attrs.keys():
        msg += " ID: " + i.attrs['id']
    if 'class' in i.attrs.keys():
        msg += " CLASS: " + i.attrs['class']
    print(msg)

    
Traceback (most recent call last):
  File "<pyshell#76>", line 6, in <module>
    msg += " CLASS: " + i.attrs['class']
TypeError: can only concatenate str (not "list") to str
for i in html.find_all("div"):
    msg = str(i)
    if 'id' in i.attrs.keys():
        msg += " ID: " + str(i.attrs['id'])
    if 'class' in i.attrs.keys():
        msg += " CLASS: " + str(i.attrs['class'])
    print(msg)

    
<div class="watch-main-col" id="watch7-content" itemid="" itemscope="" itemtype="http://schema.org/VideoObject"><link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/><meta content="To Hell with the Devil" itemprop="name"/><meta content="Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc..." itemprop="description"/><meta content="False" itemprop="requiresSubscription"/><meta content="sG0zAn0dL2I" itemprop="identifier"/><meta content="PT4M5S" itemprop="duration"/><span itemprop="author" itemscope="" itemtype="http://schema.org/Person"><link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/><link content="Stryper - Topic" itemprop="name"/></span><script nonce="IrvoVklBlQOW5t6z7RMPLw" type="application/ld+json">{"@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@id": "http:\/\/www.youtube.com\/channel\/UC20qdRIIoh4Xr6jnmZ4HBng", "name": "Stryper - Topic"}}]}</script><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="thumbnailUrl"/><span itemprop="thumbnail" itemscope="" itemtype="http://schema.org/ImageObject"><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/><meta content="1280" itemprop="width"/><meta content="720" itemprop="height"/></span><link href="https://www.youtube.com/embed/sG0zAn0dL2I" itemprop="embedUrl"/><meta content="HTML5 Flash" itemprop="playerType"/><meta content="960" itemprop="width"/><meta content="720" itemprop="height"/><meta content="true" itemprop="isFamilyFriendly"/><meta content="AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA" itemprop="regionsAllowed"/><meta content="1685732" itemprop="interactionCount"/><meta content="2018-07-25T20:04:48-07:00" itemprop="datePublished"/><meta content="2018-07-25T20:04:48-07:00" itemprop="uploadDate"/><meta content="Music" itemprop="genre"/></div> ID: watch7-content CLASS: ['watch-main-col']
<div class="skeleton flexy" id="player"><div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div></div> ID: player CLASS: ['skeleton', 'flexy']
<div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div> ID: player-wrap
<div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div> ID: player-placeholder CLASS: []
<div class="round" id="player-api"></div> ID: player-api CLASS: ['round']
<div class="watch-skeleton" id="watch-page-skeleton"><div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div></div> ID: watch-page-skeleton CLASS: ['watch-skeleton']
<div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div> ID: container
<div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div> ID: related
<div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div> CLASS: ['autoplay', 'skeleton-light-border-bottom']
<div class="skeleton-bg-color" id="upnext"></div> ID: upnext CLASS: ['skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div> CLASS: ['video-skeleton']
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div> CLASS: ['video-details']
<div class="thumbnail skeleton-bg-color"></div> CLASS: ['thumbnail', 'skeleton-bg-color']
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div> CLASS: ['details', 'flex-1']
<div class="video-title text-shell skeleton-bg-color"></div> CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
<div class="video-meta text-shell skeleton-bg-color"></div> CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
<div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div> ID: info-container
<div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div> ID: primary-info CLASS: ['skeleton-light-border-bottom']
<div class="text-shell skeleton-bg-color" id="title"></div> ID: title CLASS: ['text-shell', 'skeleton-bg-color']
<div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div> ID: info
<div class="text-shell skeleton-bg-color" id="count"></div> ID: count CLASS: ['text-shell', 'skeleton-bg-color']
<div class="flex-1"></div> CLASS: ['flex-1']
<div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div> ID: menu
<div class="menu-button skeleton-bg-color"></div> CLASS: ['menu-button', 'skeleton-bg-color']
<div class="menu-button skeleton-bg-color"></div> CLASS: ['menu-button', 'skeleton-bg-color']
<div class="menu-button skeleton-bg-color"></div> CLASS: ['menu-button', 'skeleton-bg-color']
<div class="menu-button skeleton-bg-color"></div> CLASS: ['menu-button', 'skeleton-bg-color']
<div class="menu-button skeleton-bg-color"></div> CLASS: ['menu-button', 'skeleton-bg-color']
<div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div> ID: secondary-info CLASS: ['skeleton-light-border-bottom']
<div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div> ID: top-row
<div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div> ID: video-owner CLASS: ['flex-1']
<div class="skeleton-bg-color" id="channel-icon"></div> ID: channel-icon CLASS: ['skeleton-bg-color']
<div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div> ID: upload-info CLASS: ['flex-1']
<div class="text-shell skeleton-bg-color" id="owner-name"></div> ID: owner-name CLASS: ['text-shell', 'skeleton-bg-color']
<div class="text-shell skeleton-bg-color" id="published-date"></div> ID: published-date CLASS: ['text-shell', 'skeleton-bg-color']
<div class="skeleton-bg-color" id="subscribe-button"></div> ID: subscribe-button CLASS: ['skeleton-bg-color']
<div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div> ID: search-container CLASS: ['ytd-searchbox-spt']
<div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div> ID: search-input CLASS: ['ytd-searchbox-spt']
<div id="masthead-logo" slot="masthead-logo"><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a><span id="country-code"></span></div> ID: masthead-logo
<div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div> ID: masthead-skeleton-icons
<div class="masthead-skeleton-icon"></div> CLASS: ['masthead-skeleton-icon']
<div class="masthead-skeleton-icon"></div> CLASS: ['masthead-skeleton-icon']
<div class="masthead-skeleton-icon"></div> CLASS: ['masthead-skeleton-icon']
<div id="copyright" slot="copyright" style="display: none;"><div dir="ltr" style="display:inline">© 2023 Google LLC</div></div> ID: copyright
<div dir="ltr" style="display:inline">© 2023 Google LLC</div>
for i,n in enumerate(html.find_all("div")):
    msg = f"{n}: "
    if 'id' in i.attrs.keys():
        msg += " ID: " + str(i.attrs['id'])
    if 'class' in i.attrs.keys():
        msg += " CLASS: " + str(i.attrs['class'])
    print(msg)

                                                         
Traceback (most recent call last):
  File "<pyshell#80>", line 3, in <module>
    if 'id' in i.attrs.keys():
AttributeError: 'int' object has no attribute 'attrs'
for n,i in enumerate(html.find_all("div")):
    msg = f"{n}: "
    if 'id' in i.attrs.keys():
        msg += " ID: " + str(i.attrs['id'])
    if 'class' in i.attrs.keys():
        msg += " CLASS: " + str(i.attrs['class'])
    print(msg)

                                                         
0:  ID: watch7-content CLASS: ['watch-main-col']
1:  ID: player CLASS: ['skeleton', 'flexy']
2:  ID: player-wrap
3:  ID: player-placeholder CLASS: []
4:  ID: player-api CLASS: ['round']
5:  ID: watch-page-skeleton CLASS: ['watch-skeleton']
6:  ID: container
7:  ID: related
8:  CLASS: ['autoplay', 'skeleton-light-border-bottom']
9:  ID: upnext CLASS: ['skeleton-bg-color']
10:  CLASS: ['video-skeleton']
11:  CLASS: ['video-details']
12:  CLASS: ['thumbnail', 'skeleton-bg-color']
13:  CLASS: ['details', 'flex-1']
14:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
15:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
16:  CLASS: ['video-skeleton']
17:  CLASS: ['video-details']
18:  CLASS: ['thumbnail', 'skeleton-bg-color']
19:  CLASS: ['details', 'flex-1']
20:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
21:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
22:  CLASS: ['video-skeleton']
23:  CLASS: ['video-details']
24:  CLASS: ['thumbnail', 'skeleton-bg-color']
25:  CLASS: ['details', 'flex-1']
26:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
27:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
28:  CLASS: ['video-skeleton']
29:  CLASS: ['video-details']
30:  CLASS: ['thumbnail', 'skeleton-bg-color']
31:  CLASS: ['details', 'flex-1']
32:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
33:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
34:  CLASS: ['video-skeleton']
35:  CLASS: ['video-details']
36:  CLASS: ['thumbnail', 'skeleton-bg-color']
37:  CLASS: ['details', 'flex-1']
38:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
39:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
40:  CLASS: ['video-skeleton']
41:  CLASS: ['video-details']
42:  CLASS: ['thumbnail', 'skeleton-bg-color']
43:  CLASS: ['details', 'flex-1']
44:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
45:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
46:  CLASS: ['video-skeleton']
47:  CLASS: ['video-details']
48:  CLASS: ['thumbnail', 'skeleton-bg-color']
49:  CLASS: ['details', 'flex-1']
50:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
51:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
52:  CLASS: ['video-skeleton']
53:  CLASS: ['video-details']
54:  CLASS: ['thumbnail', 'skeleton-bg-color']
55:  CLASS: ['details', 'flex-1']
56:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
57:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
58:  CLASS: ['video-skeleton']
59:  CLASS: ['video-details']
60:  CLASS: ['thumbnail', 'skeleton-bg-color']
61:  CLASS: ['details', 'flex-1']
62:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
63:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
64:  CLASS: ['video-skeleton']
65:  CLASS: ['video-details']
66:  CLASS: ['thumbnail', 'skeleton-bg-color']
67:  CLASS: ['details', 'flex-1']
68:  CLASS: ['video-title', 'text-shell', 'skeleton-bg-color']
69:  CLASS: ['video-meta', 'text-shell', 'skeleton-bg-color']
70:  ID: info-container
71:  ID: primary-info CLASS: ['skeleton-light-border-bottom']
72:  ID: title CLASS: ['text-shell', 'skeleton-bg-color']
73:  ID: info
74:  ID: count CLASS: ['text-shell', 'skeleton-bg-color']
75:  CLASS: ['flex-1']
76:  ID: menu
77:  CLASS: ['menu-button', 'skeleton-bg-color']
78:  CLASS: ['menu-button', 'skeleton-bg-color']
79:  CLASS: ['menu-button', 'skeleton-bg-color']
80:  CLASS: ['menu-button', 'skeleton-bg-color']
81:  CLASS: ['menu-button', 'skeleton-bg-color']
82:  ID: secondary-info CLASS: ['skeleton-light-border-bottom']
83:  ID: top-row
84:  ID: video-owner CLASS: ['flex-1']
85:  ID: channel-icon CLASS: ['skeleton-bg-color']
86:  ID: upload-info CLASS: ['flex-1']
87:  ID: owner-name CLASS: ['text-shell', 'skeleton-bg-color']
88:  ID: published-date CLASS: ['text-shell', 'skeleton-bg-color']
89:  ID: subscribe-button CLASS: ['skeleton-bg-color']
90:  ID: search-container CLASS: ['ytd-searchbox-spt']
91:  ID: search-input CLASS: ['ytd-searchbox-spt']
92:  ID: masthead-logo
93:  ID: masthead-skeleton-icons
94:  CLASS: ['masthead-skeleton-icon']
95:  CLASS: ['masthead-skeleton-icon']
96:  CLASS: ['masthead-skeleton-icon']
97:  ID: copyright
98: 
for i, tag in html.find_all(True):
    if tag.has_attr('class'):
        print(f"{i}: \n{tag}")

                                                         
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    for i, tag in html.find_all(True):
ValueError: too many values to unpack (expected 2)
for i, tag in enumerate(html.find_all(True)):
    if tag.has_attr('class'):
        print(f"{i}: \n{tag}")

                                                         
33: 
<style class="global_styles" nonce="EF-RWE85yb3i4NSZr3DVHg">body{padding:0;margin:0;overflow-y:scroll}body.autoscroll{overflow-y:auto}body.no-scroll{overflow:hidden}body.no-y-scroll{overflow-y:hidden}.hidden{display:none}textarea{--paper-input-container-input_-_white-space:pre-wrap}.grecaptcha-badge{visibility:hidden}</style>
34: 
<style class="masthead_shell" nonce="EF-RWE85yb3i4NSZr3DVHg">ytd-masthead.shell{background-color:#fff!important;position:fixed;top:0;right:0;left:0;display:-ms-flex;display:-webkit-flex;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:flex;height:56px;-ms-flex-align:center;-webkit-align-items:center;-webkit-box-align:center;-moz-box-align:center;align-items:center}ytd-masthead.shell #menu-icon{margin-left:16px}ytd-app>ytd-masthead.chunked{position:fixed;top:0;width:100%}ytd-masthead.shell.dark,ytd-masthead.shell.theater{background-color:#0f0f0f!important}ytd-masthead.shell.full-window-mode{background-color:#0f0f0f!important;opacity:0;-webkit-transform:translateY(calc(-100% - 5px));transform:translateY(calc(-100% - 5px))}ytd-masthead.shell>:first-child{padding-left:16px}ytd-masthead.shell>:last-child{padding-right:16px}ytd-masthead #masthead-logo{display:-ms-flex;display:-webkit-flex;display:-webkit-box;display:-moz-box;display:-ms-flexbox;display:flex}ytd-masthead #masthead-logo #country-code{margin-right:2px}ytd-masthead.shell #yt-logo-red-svg,ytd-masthead.shell #yt-logo-red-updated-svg,ytd-masthead.shell #yt-logo-svg,ytd-masthead.shell #yt-logo-updated-svg{-webkit-align-self:center;-ms-flex-item-align:center;align-self:center;margin-left:8px;padding:0;color:#000}ytd-masthead.shell #a11y-skip-nav{display:none}ytd-masthead.shell svg{width:40px;height:40px;padding:8px;margin-right:8px;-moz-box-sizing:border-box;box-sizing:border-box;color:#606060;fill:currentColor}ytd-masthead .external-icon{width:24px;height:24px}ytd-masthead .yt-icons-ext{fill:currentColor;color:#606060}ytd-masthead.shell.dark .yt-icons-ext ytd-masthead.shell.theater .yt-icons-ext{fill:#fff}ytd-masthead svg#yt-logo-svg{width:80px}ytd-masthead svg#yt-logo-red-svg{width:106.4px}ytd-masthead svg#yt-logo-updated-svg{width:90px}ytd-masthead svg#yt-logo-red-updated-svg{width:97px}@media (max-width:656px){ytd-masthead.shell>:first-child{padding-left:8px}ytd-masthead.shell>:last-child{padding-right:8px}ytd-masthead.shell svg{margin-right:0}ytd-masthead #masthead-logo{-ms-flex:1 1 0.000000001px;-webkit-flex:1;-webkit-box-flex:1;-moz-box-flex:1;flex:1;-webkit-flex-basis:0.000000001px;-ms-flex-preferred-size:0.000000001px;flex-basis:0.000000001px}ytd-masthead.shell #yt-logo-red-svg,ytd-masthead.shell #yt-logo-svg{margin-left:4px}}@media (min-width:876px){ytd-masthead #masthead-logo{width:129px}}#masthead-skeleton-icons{display:-webkit-box;display:-webkit-flex;display:-moz-box;display:-ms-flexbox;display:flex;-webkit-box-flex:1;-webkit-flex:1;-moz-box-flex:1;-ms-flex:1;flex:1;-webkit-box-orient:horizontal;-webkit-box-direction:normal;-webkit-flex-direction:row;-moz-box-orient:horizontal;-moz-box-direction:normal;-ms-flex-direction:row;flex-direction:row;-webkit-box-pack:end;-webkit-justify-content:flex-end;-moz-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}ytd-masthead.masthead-finish #masthead-skeleton-icons{display:none}.masthead-skeleton-icon{border-radius:50%;height:32px;width:32px;margin:0 8px;background-color:#e3e3e3}ytd-masthead.dark .masthead-skeleton-icon{background-color:#292929}</style>
35: 
<style class="masthead_custom_styles" id="ext-styles" is="custom-style" nonce="EF-RWE85yb3i4NSZr3DVHg">:-stv-set-elsewhere{--yt-spec-icon-active-other:initial}ytd-masthead .yt-icons-ext{color:var(--yt-spec-icon-active-other)}ytd-masthead svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead svg#yt-logo-red-updated-svg #youtube-red-paths path,ytd-masthead svg#yt-logo-svg #youtube-paths path,ytd-masthead svg#yt-logo-updated-svg #youtube-paths path{fill:#282828}ytd-masthead.dark svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead.dark svg#yt-logo-red-updated-svg #youtube-red-paths path,ytd-masthead.dark svg#yt-logo-svg #youtube-paths path,ytd-masthead.dark svg#yt-logo-updated-svg #youtube-paths path,ytd-masthead.theater svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead.theater svg#yt-logo-svg #youtube-paths path{fill:#fff}</style>
36: 
<style class="searchbox" nonce="EF-RWE85yb3i4NSZr3DVHg">#search-input.ytd-searchbox-spt input{-webkit-appearance:none;-webkit-font-smoothing:antialiased;background-color:transparent;border:none;box-shadow:none;color:inherit;font-family:Roboto,Noto,sans-serif;font-size:16px;font-weight:400;line-height:24px;margin-left:4px;max-width:100%;outline:none;text-align:inherit;width:100%;-ms-flex:1 1 0.000000001px;-webkit-flex:1;-webkit-box-flex:1;-moz-box-flex:1;flex:1;-webkit-flex-basis:0.000000001px;-ms-flex-preferred-size:0.000000001px;flex-basis:0.000000001px}#search-container.ytd-searchbox-spt{pointer-events:none;position:absolute;top:0;right:0;bottom:0;left:0}#search-input.ytd-searchbox-spt #search::-webkit-input-placeholder{color:#888}#search-input.ytd-searchbox-spt #search::-moz-input-placeholder{color:#888}#search-input.ytd-searchbox-spt #search:-ms-input-placeholder{color:#888}</style>
37: 
<style class="kevlar_global_styles" nonce="EF-RWE85yb3i4NSZr3DVHg">html{background-color:#fff!important;-webkit-text-size-adjust:none}html[dark]{background-color:#0f0f0f!important}#logo-red-icon-container.ytd-topbar-logo-renderer{width:86px}</style>
100: 
<div class="watch-main-col" id="watch7-content" itemid="" itemscope="" itemtype="http://schema.org/VideoObject"><link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/><meta content="To Hell with the Devil" itemprop="name"/><meta content="Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc..." itemprop="description"/><meta content="False" itemprop="requiresSubscription"/><meta content="sG0zAn0dL2I" itemprop="identifier"/><meta content="PT4M5S" itemprop="duration"/><span itemprop="author" itemscope="" itemtype="http://schema.org/Person"><link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/><link content="Stryper - Topic" itemprop="name"/></span><script nonce="IrvoVklBlQOW5t6z7RMPLw" type="application/ld+json">{"@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@id": "http:\/\/www.youtube.com\/channel\/UC20qdRIIoh4Xr6jnmZ4HBng", "name": "Stryper - Topic"}}]}</script><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="thumbnailUrl"/><span itemprop="thumbnail" itemscope="" itemtype="http://schema.org/ImageObject"><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/><meta content="1280" itemprop="width"/><meta content="720" itemprop="height"/></span><link href="https://www.youtube.com/embed/sG0zAn0dL2I" itemprop="embedUrl"/><meta content="HTML5 Flash" itemprop="playerType"/><meta content="960" itemprop="width"/><meta content="720" itemprop="height"/><meta content="true" itemprop="isFamilyFriendly"/><meta content="AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA" itemprop="regionsAllowed"/><meta content="1685732" itemprop="interactionCount"/><meta content="2018-07-25T20:04:48-07:00" itemprop="datePublished"/><meta content="2018-07-25T20:04:48-07:00" itemprop="uploadDate"/><meta content="Music" itemprop="genre"/></div>
128: 
<div class="skeleton flexy" id="player"><div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div></div>
130: 
<div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div>
131: 
<div class="round" id="player-api"></div>
134: 
<div class="watch-skeleton" id="watch-page-skeleton"><div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div></div>
137: 
<div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div>
138: 
<div class="skeleton-bg-color" id="upnext"></div>
139: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
140: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
141: 
<div class="thumbnail skeleton-bg-color"></div>
142: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
143: 
<div class="video-title text-shell skeleton-bg-color"></div>
144: 
<div class="video-meta text-shell skeleton-bg-color"></div>
145: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
146: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
147: 
<div class="thumbnail skeleton-bg-color"></div>
148: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
149: 
<div class="video-title text-shell skeleton-bg-color"></div>
150: 
<div class="video-meta text-shell skeleton-bg-color"></div>
151: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
152: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
153: 
<div class="thumbnail skeleton-bg-color"></div>
154: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
155: 
<div class="video-title text-shell skeleton-bg-color"></div>
156: 
<div class="video-meta text-shell skeleton-bg-color"></div>
157: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
158: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
159: 
<div class="thumbnail skeleton-bg-color"></div>
160: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
161: 
<div class="video-title text-shell skeleton-bg-color"></div>
162: 
<div class="video-meta text-shell skeleton-bg-color"></div>
163: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
164: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
165: 
<div class="thumbnail skeleton-bg-color"></div>
166: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
167: 
<div class="video-title text-shell skeleton-bg-color"></div>
168: 
<div class="video-meta text-shell skeleton-bg-color"></div>
169: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
170: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
171: 
<div class="thumbnail skeleton-bg-color"></div>
172: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
173: 
<div class="video-title text-shell skeleton-bg-color"></div>
174: 
<div class="video-meta text-shell skeleton-bg-color"></div>
175: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
176: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
177: 
<div class="thumbnail skeleton-bg-color"></div>
178: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
179: 
<div class="video-title text-shell skeleton-bg-color"></div>
180: 
<div class="video-meta text-shell skeleton-bg-color"></div>
181: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
182: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
183: 
<div class="thumbnail skeleton-bg-color"></div>
184: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
185: 
<div class="video-title text-shell skeleton-bg-color"></div>
186: 
<div class="video-meta text-shell skeleton-bg-color"></div>
187: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
188: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
189: 
<div class="thumbnail skeleton-bg-color"></div>
190: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
191: 
<div class="video-title text-shell skeleton-bg-color"></div>
192: 
<div class="video-meta text-shell skeleton-bg-color"></div>
193: 
<div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div>
194: 
<div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div>
195: 
<div class="thumbnail skeleton-bg-color"></div>
196: 
<div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div>
197: 
<div class="video-title text-shell skeleton-bg-color"></div>
198: 
<div class="video-meta text-shell skeleton-bg-color"></div>
200: 
<div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div>
201: 
<div class="text-shell skeleton-bg-color" id="title"></div>
203: 
<div class="text-shell skeleton-bg-color" id="count"></div>
204: 
<div class="flex-1"></div>
206: 
<div class="menu-button skeleton-bg-color"></div>
207: 
<div class="menu-button skeleton-bg-color"></div>
208: 
<div class="menu-button skeleton-bg-color"></div>
209: 
<div class="menu-button skeleton-bg-color"></div>
210: 
<div class="menu-button skeleton-bg-color"></div>
211: 
<div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div>
213: 
<div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div>
214: 
<div class="skeleton-bg-color" id="channel-icon"></div>
215: 
<div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div>
216: 
<div class="text-shell skeleton-bg-color" id="owner-name"></div>
217: 
<div class="text-shell skeleton-bg-color" id="published-date"></div>
218: 
<div class="skeleton-bg-color" id="subscribe-button"></div>
232: 
<ytd-masthead class="shell chunked" disable-upgrade="true" id="masthead" logo-type="YOUTUBE_LOGO" slot="masthead"><div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div><div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div><svg class="external-icon" id="menu-icon" preserveaspectratio="xMidYMid meet"><g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g></svg><div id="masthead-logo" slot="masthead-logo"><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a><span id="country-code"></span></div><div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div></ytd-masthead>
233: 
<div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div>
234: 
<div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div>
236: 
<svg class="external-icon" id="menu-icon" preserveaspectratio="xMidYMid meet"><g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g></svg>
237: 
<g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g>
241: 
<svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg>
256: 
<svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg>
272: 
<div class="masthead-skeleton-icon"></div>
273: 
<div class="masthead-skeleton-icon"></div>
274: 
<div class="masthead-skeleton-icon"></div>
for i, tag in enumerate(html.find_all(True)):
    if tag.has_attr('title'):
        print(f"{i}: {tag.attrs['title']} \n{tag}")

                                                                        
39: YouTube 
<link href="https://www.youtube.com/opensearch?locale=en_GB" rel="search" title="YouTube" type="application/opensearchdescription+xml"/>
52: To Hell with the Devil 
<link href="https://www.youtube.com/oembed?format=json&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DsG0zAn0dL2I" rel="alternate" title="To Hell with the Devil" type="application/json+oembed"/>
53: To Hell with the Devil 
<link href="https://www.youtube.com/oembed?format=xml&amp;url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DsG0zAn0dL2I" rel="alternate" title="To Hell with the Devil" type="text/xml+oembed"/>
240: YouTube 
<a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a>
255: YouTube 
<a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a>
for i, tag in enumerate(html.find_all(True)):
    if tag.has_attr('id'):
        print(f"\t{i}: {tag.attrs['id']} \n\t{tag}")

                                                                        
	35: ext-styles 
	<style class="masthead_custom_styles" id="ext-styles" is="custom-style" nonce="EF-RWE85yb3i4NSZr3DVHg">:-stv-set-elsewhere{--yt-spec-icon-active-other:initial}ytd-masthead .yt-icons-ext{color:var(--yt-spec-icon-active-other)}ytd-masthead svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead svg#yt-logo-red-updated-svg #youtube-red-paths path,ytd-masthead svg#yt-logo-svg #youtube-paths path,ytd-masthead svg#yt-logo-updated-svg #youtube-paths path{fill:#282828}ytd-masthead.dark svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead.dark svg#yt-logo-red-updated-svg #youtube-red-paths path,ytd-masthead.dark svg#yt-logo-svg #youtube-paths path,ytd-masthead.dark svg#yt-logo-updated-svg #youtube-paths path,ytd-masthead.theater svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead.theater svg#yt-logo-svg #youtube-paths path{fill:#fff}</style>
	100: watch7-content 
	<div class="watch-main-col" id="watch7-content" itemid="" itemscope="" itemtype="http://schema.org/VideoObject"><link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/><meta content="To Hell with the Devil" itemprop="name"/><meta content="Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc..." itemprop="description"/><meta content="False" itemprop="requiresSubscription"/><meta content="sG0zAn0dL2I" itemprop="identifier"/><meta content="PT4M5S" itemprop="duration"/><span itemprop="author" itemscope="" itemtype="http://schema.org/Person"><link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/><link content="Stryper - Topic" itemprop="name"/></span><script nonce="IrvoVklBlQOW5t6z7RMPLw" type="application/ld+json">{"@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@id": "http:\/\/www.youtube.com\/channel\/UC20qdRIIoh4Xr6jnmZ4HBng", "name": "Stryper - Topic"}}]}</script><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="thumbnailUrl"/><span itemprop="thumbnail" itemscope="" itemtype="http://schema.org/ImageObject"><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/><meta content="1280" itemprop="width"/><meta content="720" itemprop="height"/></span><link href="https://www.youtube.com/embed/sG0zAn0dL2I" itemprop="embedUrl"/><meta content="HTML5 Flash" itemprop="playerType"/><meta content="960" itemprop="width"/><meta content="720" itemprop="height"/><meta content="true" itemprop="isFamilyFriendly"/><meta content="AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA" itemprop="regionsAllowed"/><meta content="1685732" itemprop="interactionCount"/><meta content="2018-07-25T20:04:48-07:00" itemprop="datePublished"/><meta content="2018-07-25T20:04:48-07:00" itemprop="uploadDate"/><meta content="Music" itemprop="genre"/></div>
	128: player 
	<div class="skeleton flexy" id="player"><div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div></div>
	129: player-wrap 
	<div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div>
	130: player-placeholder 
	<div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div>
	131: player-api 
	<div class="round" id="player-api"></div>
	134: watch-page-skeleton 
	<div class="watch-skeleton" id="watch-page-skeleton"><div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div></div>
	135: container 
	<div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div>
	136: related 
	<div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div>
	138: upnext 
	<div class="skeleton-bg-color" id="upnext"></div>
	199: info-container 
	<div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div>
	200: primary-info 
	<div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div>
	201: title 
	<div class="text-shell skeleton-bg-color" id="title"></div>
	202: info 
	<div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div>
	203: count 
	<div class="text-shell skeleton-bg-color" id="count"></div>
	205: menu 
	<div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div>
	211: secondary-info 
	<div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div>
	212: top-row 
	<div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div>
	213: video-owner 
	<div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div>
	214: channel-icon 
	<div class="skeleton-bg-color" id="channel-icon"></div>
	215: upload-info 
	<div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div>
	216: owner-name 
	<div class="text-shell skeleton-bg-color" id="owner-name"></div>
	217: published-date 
	<div class="text-shell skeleton-bg-color" id="published-date"></div>
	218: subscribe-button 
	<div class="skeleton-bg-color" id="subscribe-button"></div>
	232: masthead 
	<ytd-masthead class="shell chunked" disable-upgrade="true" id="masthead" logo-type="YOUTUBE_LOGO" slot="masthead"><div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div><div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div><svg class="external-icon" id="menu-icon" preserveaspectratio="xMidYMid meet"><g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g></svg><div id="masthead-logo" slot="masthead-logo"><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a><span id="country-code"></span></div><div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div></ytd-masthead>
	233: search-container 
	<div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div>
	234: search-input 
	<div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div>
	235: search 
	<input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/>
	236: menu-icon 
	<svg class="external-icon" id="menu-icon" preserveaspectratio="xMidYMid meet"><g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g></svg>
	237: menu 
	<g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g>
	239: masthead-logo 
	<div id="masthead-logo" slot="masthead-logo"><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a><span id="country-code"></span></div>
	241: yt-logo-updated-svg 
	<svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg>
	242: yt-logo-updated 
	<g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g>
	247: youtube-paths 
	<g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g>
	256: yt-logo-red-updated-svg 
	<svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg>
	257: yt-logo-red-updated 
	<g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g>
	261: youtube-red-paths 
	<g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g>
	270: country-code 
	<span id="country-code"></span>
	271: masthead-skeleton-icons 
	<div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div>
	287: copyright 
	<div id="copyright" slot="copyright" style="display: none;"><div dir="ltr" style="display:inline">© 2023 Google LLC</div></div>
	292: base-js 
	<script id="base-js" nonce="IrvoVklBlQOW5t6z7RMPLw" src="https://www.youtube.com/s/desktop/bd3558ba/jsbin/desktop_polymer_legacy_browsers.vflset/desktop_polymer_legacy_browsers.js"></script>
for i, tag in enumerate(html.find_all(True)):
    if tag.has_attr('id'):
        print("stryper" in tag.text)
        print(f"\t{i}: {tag.attrs['id']} \n\t{tag}")

                                                                        
False
	35: ext-styles 
	<style class="masthead_custom_styles" id="ext-styles" is="custom-style" nonce="EF-RWE85yb3i4NSZr3DVHg">:-stv-set-elsewhere{--yt-spec-icon-active-other:initial}ytd-masthead .yt-icons-ext{color:var(--yt-spec-icon-active-other)}ytd-masthead svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead svg#yt-logo-red-updated-svg #youtube-red-paths path,ytd-masthead svg#yt-logo-svg #youtube-paths path,ytd-masthead svg#yt-logo-updated-svg #youtube-paths path{fill:#282828}ytd-masthead.dark svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead.dark svg#yt-logo-red-updated-svg #youtube-red-paths path,ytd-masthead.dark svg#yt-logo-svg #youtube-paths path,ytd-masthead.dark svg#yt-logo-updated-svg #youtube-paths path,ytd-masthead.theater svg#yt-logo-red-svg #youtube-red-paths path,ytd-masthead.theater svg#yt-logo-svg #youtube-paths path{fill:#fff}</style>
False
	100: watch7-content 
	<div class="watch-main-col" id="watch7-content" itemid="" itemscope="" itemtype="http://schema.org/VideoObject"><link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/><meta content="To Hell with the Devil" itemprop="name"/><meta content="Provided to YouTube by Universal Music GroupTo Hell with the Devil · StryperTo Hell With The Devil℗ 1986 Hollywood Records, Inc.Released on: 1986-01-01Produc..." itemprop="description"/><meta content="False" itemprop="requiresSubscription"/><meta content="sG0zAn0dL2I" itemprop="identifier"/><meta content="PT4M5S" itemprop="duration"/><span itemprop="author" itemscope="" itemtype="http://schema.org/Person"><link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/><link content="Stryper - Topic" itemprop="name"/></span><script nonce="IrvoVklBlQOW5t6z7RMPLw" type="application/ld+json">{"@context": "http://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@id": "http:\/\/www.youtube.com\/channel\/UC20qdRIIoh4Xr6jnmZ4HBng", "name": "Stryper - Topic"}}]}</script><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="thumbnailUrl"/><span itemprop="thumbnail" itemscope="" itemtype="http://schema.org/ImageObject"><link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/><meta content="1280" itemprop="width"/><meta content="720" itemprop="height"/></span><link href="https://www.youtube.com/embed/sG0zAn0dL2I" itemprop="embedUrl"/><meta content="HTML5 Flash" itemprop="playerType"/><meta content="960" itemprop="width"/><meta content="720" itemprop="height"/><meta content="true" itemprop="isFamilyFriendly"/><meta content="AE,AR,AS,AT,AU,AW,BA,BD,BE,BG,BH,BM,BO,BR,CH,CL,CO,CR,CY,CZ,DE,DK,DO,DZ,EC,EE,EG,ES,FI,FR,GB,GE,GF,GH,GP,GR,GT,GU,HK,HN,HR,HU,ID,IE,IL,IN,IQ,IS,IT,JO,JP,KE,KH,KR,KW,KY,LA,LB,LI,LK,LT,LU,LV,MA,MK,MP,MQ,MT,MX,MY,NC,NG,NI,NL,NO,NP,NZ,OM,PA,PE,PF,PG,PH,PK,PL,PR,PT,PY,QA,RO,RS,SA,SE,SG,SI,SK,SN,SV,TC,TH,TN,TR,TW,UA,US,UY,VE,VI,VN,YT,ZA" itemprop="regionsAllowed"/><meta content="1685732" itemprop="interactionCount"/><meta content="2018-07-25T20:04:48-07:00" itemprop="datePublished"/><meta content="2018-07-25T20:04:48-07:00" itemprop="uploadDate"/><meta content="Music" itemprop="genre"/></div>
False
	128: player 
	<div class="skeleton flexy" id="player"><div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div></div>
False
	129: player-wrap 
	<div id="player-wrap"><div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div><div class="round" id="player-api"></div></div>
False
	130: player-placeholder 
	<div class="" id="player-placeholder" style="background-image: url('https://i.ytimg.com/vi/sG0zAn0dL2I/hqdefault.jpg');"></div>
False
	131: player-api 
	<div class="round" id="player-api"></div>
False
	134: watch-page-skeleton 
	<div class="watch-skeleton" id="watch-page-skeleton"><div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div></div>
False
	135: container 
	<div id="container"><div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div></div>
False
	136: related 
	<div id="related"><div class="autoplay skeleton-light-border-bottom"><div class="skeleton-bg-color" id="upnext"></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div><div class="video-skeleton"><div class="video-details"><div class="thumbnail skeleton-bg-color"></div><div class="details flex-1"><div class="video-title text-shell skeleton-bg-color"></div><div class="video-meta text-shell skeleton-bg-color"></div></div></div></div></div>
False
	138: upnext 
	<div class="skeleton-bg-color" id="upnext"></div>
False
	199: info-container 
	<div id="info-container"><div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div><div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div></div>
False
	200: primary-info 
	<div class="skeleton-light-border-bottom" id="primary-info"><div class="text-shell skeleton-bg-color" id="title"></div><div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div></div>
False
	201: title 
	<div class="text-shell skeleton-bg-color" id="title"></div>
False
	202: info 
	<div id="info"><div class="text-shell skeleton-bg-color" id="count"></div><div class="flex-1"></div><div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div></div>
False
	203: count 
	<div class="text-shell skeleton-bg-color" id="count"></div>
False
	205: menu 
	<div id="menu"><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div><div class="menu-button skeleton-bg-color"></div></div>
False
	211: secondary-info 
	<div class="skeleton-light-border-bottom" id="secondary-info"><div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div></div>
False
	212: top-row 
	<div id="top-row"><div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div><div class="skeleton-bg-color" id="subscribe-button"></div></div>
False
	213: video-owner 
	<div class="flex-1" id="video-owner"><div class="skeleton-bg-color" id="channel-icon"></div><div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div></div>
False
	214: channel-icon 
	<div class="skeleton-bg-color" id="channel-icon"></div>
False
	215: upload-info 
	<div class="flex-1" id="upload-info"><div class="text-shell skeleton-bg-color" id="owner-name"></div><div class="text-shell skeleton-bg-color" id="published-date"></div></div>
False
	216: owner-name 
	<div class="text-shell skeleton-bg-color" id="owner-name"></div>
False
	217: published-date 
	<div class="text-shell skeleton-bg-color" id="published-date"></div>
False
	218: subscribe-button 
	<div class="skeleton-bg-color" id="subscribe-button"></div>
False
	232: masthead 
	<ytd-masthead class="shell chunked" disable-upgrade="true" id="masthead" logo-type="YOUTUBE_LOGO" slot="masthead"><div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div><div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div><svg class="external-icon" id="menu-icon" preserveaspectratio="xMidYMid meet"><g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g></svg><div id="masthead-logo" slot="masthead-logo"><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a><span id="country-code"></span></div><div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div></ytd-masthead>
False
	233: search-container 
	<div class="ytd-searchbox-spt" id="search-container" slot="search-container"></div>
False
	234: search-input 
	<div class="ytd-searchbox-spt" id="search-input" slot="search-input"><input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/></div>
False
	235: search 
	<input autocapitalize="none" autocomplete="off" autocorrect="off" hidden="" id="search" name="search_query" spellcheck="false" tabindex="0" type="text"/>
False
	236: menu-icon 
	<svg class="external-icon" id="menu-icon" preserveaspectratio="xMidYMid meet"><g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g></svg>
False
	237: menu 
	<g class="yt-icons-ext" id="menu" viewbox="0 0 24 24"><path d="M21,6H3V5h18V6z M21,11H3v1h18V11z M21,17H3v1h18V17z"></path></g>
False
	239: masthead-logo 
	<div id="masthead-logo" slot="masthead-logo"><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg></a><a href="/" style="display: none;" title="YouTube"><svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg></a><span id="country-code"></span></div>
False
	241: yt-logo-updated-svg 
	<svg class="external-icon" id="yt-logo-updated-svg" viewbox="0 0 90 20"><g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g></svg>
False
	242: yt-logo-updated 
	<g id="yt-logo-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 90 20"><g><path d="M27.9727 3.12324C27.6435 1.89323 26.6768 0.926623 25.4468 0.597366C23.2197 2.24288e-07 14.285 0 14.285 0C14.285 0 5.35042 2.24288e-07 3.12323 0.597366C1.89323 0.926623 0.926623 1.89323 0.597366 3.12324C2.24288e-07 5.35042 0 10 0 10C0 10 2.24288e-07 14.6496 0.597366 16.8768C0.926623 18.1068 1.89323 19.0734 3.12323 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6768 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9727 3.12324Z" fill="#FF0000"></path><path d="M11.4253 14.2854L18.8477 10.0004L11.4253 5.71533V14.2854Z" fill="white"></path></g><g><g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g></g></g>
False
	247: youtube-paths 
	<g id="youtube-paths"><path d="M34.6024 13.0036L31.3945 1.41846H34.1932L35.3174 6.6701C35.6043 7.96361 35.8136 9.06662 35.95 9.97913H36.0323C36.1264 9.32532 36.3381 8.22937 36.665 6.68892L37.8291 1.41846H40.6278L37.3799 13.0036V18.561H34.6001V13.0036H34.6024Z"></path><path d="M41.4697 18.1937C40.9053 17.8127 40.5031 17.22 40.2632 16.4157C40.0257 15.6114 39.9058 14.5437 39.9058 13.2078V11.3898C39.9058 10.0422 40.0422 8.95805 40.315 8.14196C40.5878 7.32588 41.0135 6.72851 41.592 6.35457C42.1706 5.98063 42.9302 5.79248 43.871 5.79248C44.7976 5.79248 45.5384 5.98298 46.0981 6.36398C46.6555 6.74497 47.0647 7.34234 47.3234 8.15137C47.5821 8.96275 47.7115 10.0422 47.7115 11.3898V13.2078C47.7115 14.5437 47.5845 15.6161 47.3329 16.4251C47.0812 17.2365 46.672 17.8292 46.1075 18.2031C45.5431 18.5771 44.7764 18.7652 43.8098 18.7652C42.8126 18.7675 42.0342 18.5747 41.4697 18.1937ZM44.6353 16.2323C44.7905 15.8231 44.8705 15.1575 44.8705 14.2309V10.3292C44.8705 9.43077 44.7929 8.77225 44.6353 8.35833C44.4777 7.94206 44.2026 7.7351 43.8074 7.7351C43.4265 7.7351 43.156 7.94206 43.0008 8.35833C42.8432 8.77461 42.7656 9.43077 42.7656 10.3292V14.2309C42.7656 15.1575 42.8408 15.8254 42.9914 16.2323C43.1419 16.6415 43.4123 16.8461 43.8074 16.8461C44.2026 16.8461 44.4777 16.6415 44.6353 16.2323Z"></path><path d="M56.8154 18.5634H54.6094L54.3648 17.03H54.3037C53.7039 18.1871 52.8055 18.7656 51.6061 18.7656C50.7759 18.7656 50.1621 18.4928 49.767 17.9496C49.3719 17.4039 49.1743 16.5526 49.1743 15.3955V6.03751H51.9942V15.2308C51.9942 15.7906 52.0553 16.188 52.1776 16.4256C52.2999 16.6631 52.5045 16.783 52.7914 16.783C53.036 16.783 53.2712 16.7078 53.497 16.5573C53.7228 16.4067 53.8874 16.2162 53.9979 15.9858V6.03516H56.8154V18.5634Z"></path><path d="M64.4755 3.68758H61.6768V18.5629H58.9181V3.68758H56.1194V1.42041H64.4755V3.68758Z"></path><path d="M71.2768 18.5634H69.0708L68.8262 17.03H68.7651C68.1654 18.1871 67.267 18.7656 66.0675 18.7656C65.2373 18.7656 64.6235 18.4928 64.2284 17.9496C63.8333 17.4039 63.6357 16.5526 63.6357 15.3955V6.03751H66.4556V15.2308C66.4556 15.7906 66.5167 16.188 66.639 16.4256C66.7613 16.6631 66.9659 16.783 67.2529 16.783C67.4974 16.783 67.7326 16.7078 67.9584 16.5573C68.1842 16.4067 68.3488 16.2162 68.4593 15.9858V6.03516H71.2768V18.5634Z"></path><path d="M80.609 8.0387C80.4373 7.24849 80.1621 6.67699 79.7812 6.32186C79.4002 5.96674 78.8757 5.79035 78.2078 5.79035C77.6904 5.79035 77.2059 5.93616 76.7567 6.23014C76.3075 6.52412 75.9594 6.90747 75.7148 7.38489H75.6937V0.785645H72.9773V18.5608H75.3056L75.5925 17.3755H75.6537C75.8724 17.7988 76.1993 18.1304 76.6344 18.3774C77.0695 18.622 77.554 18.7443 78.0855 18.7443C79.038 18.7443 79.7412 18.3045 80.1904 17.4272C80.6396 16.5476 80.8653 15.1765 80.8653 13.3092V11.3266C80.8653 9.92722 80.7783 8.82892 80.609 8.0387ZM78.0243 13.1492C78.0243 14.0617 77.9867 14.7767 77.9114 15.2941C77.8362 15.8115 77.7115 16.1808 77.5328 16.3971C77.3564 16.6158 77.1165 16.724 76.8178 16.724C76.585 16.724 76.371 16.6699 76.1734 16.5594C75.9759 16.4512 75.816 16.2866 75.6937 16.0702V8.96062C75.7877 8.6196 75.9524 8.34209 76.1852 8.12337C76.4157 7.90465 76.6697 7.79646 76.9401 7.79646C77.2271 7.79646 77.4481 7.90935 77.6034 8.13278C77.7609 8.35855 77.8691 8.73485 77.9303 9.26636C77.9914 9.79787 78.022 10.5528 78.022 11.5335V13.1492H78.0243Z"></path><path d="M84.8657 13.8712C84.8657 14.6755 84.8892 15.2776 84.9363 15.6798C84.9833 16.0819 85.0821 16.3736 85.2326 16.5594C85.3831 16.7428 85.6136 16.8345 85.9264 16.8345C86.3474 16.8345 86.639 16.6699 86.7942 16.343C86.9518 16.0161 87.0365 15.4705 87.0506 14.7085L89.4824 14.8519C89.4965 14.9601 89.5035 15.1106 89.5035 15.3011C89.5035 16.4582 89.186 17.3237 88.5534 17.8952C87.9208 18.4667 87.0247 18.7536 85.8676 18.7536C84.4777 18.7536 83.504 18.3185 82.9466 17.446C82.3869 16.5735 82.1094 15.2259 82.1094 13.4008V11.2136C82.1094 9.33452 82.3987 7.96105 82.9772 7.09558C83.5558 6.2301 84.5459 5.79736 85.9499 5.79736C86.9165 5.79736 87.6597 5.97375 88.1771 6.32888C88.6945 6.684 89.059 7.23433 89.2707 7.98457C89.4824 8.7348 89.5882 9.76961 89.5882 11.0913V13.2362H84.8657V13.8712ZM85.2232 7.96811C85.0797 8.14449 84.9857 8.43377 84.9363 8.83593C84.8892 9.2381 84.8657 9.84722 84.8657 10.6657V11.5641H86.9283V10.6657C86.9283 9.86133 86.9001 9.25221 86.846 8.83593C86.7919 8.41966 86.6931 8.12803 86.5496 7.95635C86.4062 7.78702 86.1851 7.7 85.8864 7.7C85.5854 7.70235 85.3643 7.79172 85.2232 7.96811Z"></path></g>
False
	256: yt-logo-red-updated-svg 
	<svg class="external-icon" id="yt-logo-red-updated-svg" style="width: 97px;" viewbox="0 0 97 20"><g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g></svg>
False
	257: yt-logo-red-updated 
	<g id="yt-logo-red-updated" preserveaspectratio="xMidYMid meet" viewbox="0 0 97 20"><g><path d="M27.9704 3.12324C27.6411 1.89323 26.6745 0.926623 25.4445 0.597366C23.2173 2.24288e-07 14.2827 0 14.2827 0C14.2827 0 5.34807 2.24288e-07 3.12088 0.597366C1.89323 0.926623 0.924271 1.89323 0.595014 3.12324C-2.8036e-07 5.35042 0 10 0 10C0 10 -1.57002e-06 14.6496 0.597364 16.8768C0.926621 18.1068 1.89323 19.0734 3.12324 19.4026C5.35042 20 14.285 20 14.285 20C14.285 20 23.2197 20 25.4468 19.4026C26.6769 19.0734 27.6435 18.1068 27.9727 16.8768C28.5701 14.6496 28.5701 10 28.5701 10C28.5701 10 28.5677 5.35042 27.9704 3.12324Z" fill="#FF0000"></path><path d="M11.4275 14.2854L18.8475 10.0004L11.4275 5.71533V14.2854Z" fill="white"></path></g><g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g></g>
False
	261: youtube-red-paths 
	<g id="youtube-red-paths"><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path><path d="M46.5336 5.8345L46.3901 9.08238C45.2259 8.83779 44.264 9.02123 43.836 9.77382V18.5579H41.1196V6.0391H43.2857L43.5303 8.75312H43.6337C43.9183 6.77288 44.8379 5.771 46.0232 5.771C46.1949 5.7757 46.3666 5.79687 46.5336 5.8345Z"></path><path d="M49.6567 13.2456V13.8782C49.6567 16.0842 49.779 16.8415 50.7198 16.8415C51.6182 16.8415 51.8228 16.1501 51.8439 14.7178L54.2734 14.8613C54.4568 17.5565 53.0481 18.763 50.6586 18.763C47.7588 18.763 46.9004 16.8627 46.9004 13.4126V11.223C46.9004 7.58707 47.8599 5.80908 50.7409 5.80908C53.6407 5.80908 54.3769 7.32131 54.3769 11.0984V13.2456H49.6567ZM49.6567 10.6703V11.5687H51.7193V10.675C51.7193 8.37258 51.5547 7.71172 50.6821 7.71172C49.8096 7.71172 49.6567 8.38669 49.6567 10.675V10.6703Z"></path><path d="M68.4103 9.09902V18.5557H65.5928V9.30834C65.5928 8.28764 65.327 7.77729 64.7132 7.77729C64.2216 7.77729 63.7724 8.06186 63.4667 8.59338C63.4832 8.76271 63.4902 8.93439 63.4879 9.10373V18.5605H60.668V9.30834C60.668 8.28764 60.4022 7.77729 59.7884 7.77729C59.2969 7.77729 58.8665 8.06186 58.5631 8.57456V18.5628H55.7456V6.03929H57.9728L58.2221 7.63383H58.2621C58.8947 6.42969 59.9178 5.77588 61.1219 5.77588C62.3072 5.77588 62.9799 6.36854 63.288 7.43157C63.9418 6.34973 64.9225 5.77588 66.0443 5.77588C67.7564 5.77588 68.4103 7.00119 68.4103 9.09902Z"></path><path d="M69.8191 2.8338C69.8191 1.4862 70.3106 1.09814 71.3501 1.09814C72.4132 1.09814 72.8812 1.54734 72.8812 2.8338C72.8812 4.22373 72.4108 4.57181 71.3501 4.57181C70.3106 4.56945 69.8191 4.22138 69.8191 2.8338ZM69.9837 6.03935H72.6789V18.5629H69.9837V6.03935Z"></path><path d="M81.891 6.03955V18.5631H79.6849L79.4403 17.032H79.3792C78.7466 18.2573 77.827 18.7677 76.684 18.7677C75.0095 18.7677 74.2522 17.7046 74.2522 15.3975V6.0419H77.0697V15.2352C77.0697 16.3382 77.3002 16.7874 77.867 16.7874C78.3844 16.7663 78.8477 16.4582 79.0688 15.9902V6.0419H81.891V6.03955Z"></path><path d="M96.1901 9.09893V18.5557H93.3726V9.30825C93.3726 8.28755 93.1068 7.7772 92.493 7.7772C92.0015 7.7772 91.5523 8.06177 91.2465 8.59329C91.263 8.76027 91.2701 8.9296 91.2677 9.09893V18.5557H88.4502V9.30825C88.4502 8.28755 88.1845 7.7772 87.5706 7.7772C87.0791 7.7772 86.6487 8.06177 86.3453 8.57447V18.5627H83.5278V6.0392H85.7527L85.9973 7.63139H86.0372C86.6699 6.42725 87.6929 5.77344 88.8971 5.77344C90.0824 5.77344 90.755 6.3661 91.0631 7.42913C91.7169 6.34729 92.6976 5.77344 93.8194 5.77344C95.541 5.77579 96.1901 7.0011 96.1901 9.09893Z"></path><path d="M40.0566 6.34524V7.03668C40.0566 10.4915 38.5255 12.5118 35.1742 12.5118H34.6638V18.5583H31.9263V1.42285H35.414C38.6078 1.42285 40.0566 2.7728 40.0566 6.34524ZM37.1779 6.59218C37.1779 4.09924 36.7287 3.50658 35.1765 3.50658H34.6662V10.4727H35.1365C36.6064 10.4727 37.1803 9.40968 37.1803 7.10253L37.1779 6.59218Z"></path></g>
False
	270: country-code 
	<span id="country-code"></span>
False
	271: masthead-skeleton-icons 
	<div id="masthead-skeleton-icons" slot="masthead-skeleton"><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div><div class="masthead-skeleton-icon"></div></div>
False
	287: copyright 
	<div id="copyright" slot="copyright" style="display: none;"><div dir="ltr" style="display:inline">© 2023 Google LLC</div></div>
False
	292: base-js 
	<script id="base-js" nonce="IrvoVklBlQOW5t6z7RMPLw" src="https://www.youtube.com/s/desktop/bd3558ba/jsbin/desktop_polymer_legacy_browsers.vflset/desktop_polymer_legacy_browsers.js"></script>
R
                                                                        
<Response [200]>
"a" in R
                                                                        
False
"a" in R.text
                                                                        
True
tags = html.find_all("link", attrs={'itemprop':'url'})
                                                                        
for i in tags:
                                                                        print(i)

                                                                        
<link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/>
<link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/>
<link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/>
for i in tags:
                                                                        if "href" in i.attrs.keys():
                                                                            if i.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                                                                                print("stryper")

                                                                        
stryper
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, parser="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            if i.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
  File "<pyshell#117>", line 3, in check
    html = BeautifulSoup(R.content, parser="html.parser")
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\__init__.py", line 259, in __init__
    builder = builder_class(**kwargs)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\builder\_htmlparser.py", line 316, in __init__
    super(HTMLParserTreeBuilder, self).__init__(**kwargs)
TypeError: TreeBuilder.__init__() got an unexpected keyword argument 'parser'
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            if i.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
False
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            print(tag)
            if i.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
<link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/>
<link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/>
<link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/>
False
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            print(tag, i.attrs['href'])
            if i.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
<link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/> https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg
<link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/> https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg
<link href="https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg" itemprop="url"/> https://i.ytimg.com/vi/sG0zAn0dL2I/maxresdefault.jpg
False
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            print(tag, tag.attrs['href'])
            if tag.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
<link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/> https://www.youtube.com/watch?v=sG0zAn0dL2I
<link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/> http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng
True
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            print(tag, "|", tag.attrs['href'])
            if tag.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=sG0zAn0dL2I")
<link href="https://www.youtube.com/watch?v=sG0zAn0dL2I" itemprop="url"/> | https://www.youtube.com/watch?v=sG0zAn0dL2I
<link href="http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng" itemprop="url"/> | http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng
True
def check(url):
    R = requests.get(url)
    html = BeautifulSoup(R.content, features="html.parser")
    for tag in html.find_all("link", attrs={'itemprop':'url'}):
        if "href" in tag.attrs.keys():
            if tag.attrs['href'] == "http://www.youtube.com/channel/UC20qdRIIoh4Xr6jnmZ4HBng":
                return True
    return False

check("https://www.youtube.com/watch?v=5VlcfXszkfA&list=OLAK5uy_lWsF2gOUCoNvFjzAUXGKE-Ldr6byjkEhI&index=1&pp=8AUB")
True
L = ["https://www.youtube.com/watch?v=5VlcfXszkfA&list=OLAK5uy_lWsF2gOUCoNvFjzAUXGKE-Ldr6byjkEhI&index=1&pp=8AUB",
     "https://www.youtube.com/watch?v=srNCdHwJzBk&list=OLAK5uy_lWsF2gOUCoNvFjzAUXGKE-Ldr6byjkEhI&index=2&pp=8AUB",
     "https://www.youtube.com/watch?v=ERMKZhFwGEU&list=OLAK5uy_lWsF2gOUCoNvFjzAUXGKE-Ldr6byjkEhI&index=6&pp=8AUB"
     ]
for i in L:
    check(i)

    
True
True
True
R
<Response [200]>
R.headers
{'Content-Type': 'text/html; charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache', 'Expires': 'Mon, 01 Jan 1990 00:00:00 GMT', 'Date': 'Fri, 24 Nov 2023 03:27:30 GMT', 'Strict-Transport-Security': 'max-age=31536000', 'X-Frame-Options': 'SAMEORIGIN', 'Origin-Trial': 'AvC9UlR6RDk2crliDsFl66RWLnTbHrDbp+DiY6AYz/PNQ4G4tdUTjrHYr2sghbkhGQAVxb7jaPTHpEVBz0uzQwkAAAB4eyJvcmlnaW4iOiJodHRwczovL3lvdXR1YmUuY29tOjQ0MyIsImZlYXR1cmUiOiJXZWJWaWV3WFJlcXVlc3RlZFdpdGhEZXByZWNhdGlvbiIsImV4cGlyeSI6MTcxOTUzMjc5OSwiaXNTdWJkb21haW4iOnRydWV9', 'Content-Security-Policy-Report-Only': "require-trusted-types-for 'script';report-uri /cspreport", 'Permissions-Policy': 'ch-ua-arch=*, ch-ua-bitness=*, ch-ua-full-version=*, ch-ua-full-version-list=*, ch-ua-model=*, ch-ua-wow64=*, ch-ua-form-factor=*, ch-ua-platform=*, ch-ua-platform-version=*', 'Report-To': '{"group":"youtube_main","max_age":2592000,"endpoints":[{"url":"https://csp.withgoogle.com/csp/report-to/youtube_main"}]}', 'Cross-Origin-Opener-Policy': 'same-origin-allow-popups; report-to="youtube_main"', 'P3P': 'CP="This is not a P3P policy! See http://support.google.com/accounts/answer/151657?hl=en-GB for more info."', 'Content-Encoding': 'gzip', 'Server': 'ESF', 'X-XSS-Protection': '0', 'Set-Cookie': 'GPS=1; Domain=.youtube.com; Expires=Fri, 24-Nov-2023 03:57:30 GMT; Path=/; Secure; HttpOnly, YSC=Z65GYmtdG64; Domain=.youtube.com; Path=/; Secure; HttpOnly; SameSite=none, VISITOR_INFO1_LIVE=jvHU_bcqWrw; Domain=.youtube.com; Expires=Wed, 22-May-2024 03:27:30 GMT; Path=/; Secure; HttpOnly; SameSite=none, VISITOR_PRIVACY_METADATA=CgJBVRICGgA%3D; Domain=.youtube.com; Expires=Wed, 22-May-2024 03:27:30 GMT; Path=/; Secure; HttpOnly; SameSite=lax', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000', 'Transfer-Encoding': 'chunked'}
T = R.html.find("link")
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    T = R.html.find("link")
AttributeError: 'Response' object has no attribute 'html'
from requests_html import HTMLSession
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    from requests_html import HTMLSession
ModuleNotFoundError: No module named 'requests_html'
R.find("link")
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    R.find("link")
AttributeError: 'Response' object has no attribute 'find'
help(R)
Help on Response in module requests.models object:

class Response(builtins.object)
 |  The :class:`Response <Response>` object, which contains a
 |  server's response to an HTTP request.
 |  
 |  Methods defined here:
 |  
 |  __bool__(self)
 |      Returns True if :attr:`status_code` is less than 400.
 |      
 |      This attribute checks if the status code of the response is between
 |      400 and 600 to see if there was a client error or a server error. If
 |      the status code, is between 200 and 400, this will return True. This
 |      is **not** a check to see if the response code is ``200 OK``.
 |  
 |  __enter__(self)
 |  
 |  __exit__(self, *args)
 |  
 |  __getstate__(self)
 |      Helper for pickle.
 |  
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self)
 |      Allows you to use a response as an iterator.
 |  
 |  __nonzero__(self)
 |      Returns True if :attr:`status_code` is less than 400.
 |      
 |      This attribute checks if the status code of the response is between
 |      400 and 600 to see if there was a client error or a server error. If
 |      the status code, is between 200 and 400, this will return True. This
 |      is **not** a check to see if the response code is ``200 OK``.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  __setstate__(self, state)
 |  
 |  close(self)
 |      Releases the connection back to the pool. Once this method has been
 |      called the underlying ``raw`` object must not be accessed again.
 |      
 |      *Note: Should not normally need to be called explicitly.*
 |  
 |  iter_content(self, chunk_size=1, decode_unicode=False)
 |      Iterates over the response data.  When stream=True is set on the
 |      request, this avoids reading the content at once into memory for
 |      large responses.  The chunk size is the number of bytes it should
 |      read into memory.  This is not necessarily the length of each item
 |      returned as decoding can take place.
 |      
 |      chunk_size must be of type int or None. A value of None will
 |      function differently depending on the value of `stream`.
 |      stream=True will read data as it arrives in whatever size the
 |      chunks are received. If stream=False, data is returned as
 |      a single chunk.
 |      
 |      If decode_unicode is True, content will be decoded using the best
 |      available encoding based on the response.
 |  
 |  iter_lines(self, chunk_size=512, decode_unicode=False, delimiter=None)
 |      Iterates over the response data, one line at a time.  When
 |      stream=True is set on the request, this avoids reading the
 |      content at once into memory for large responses.
 |      
 |      .. note:: This method is not reentrant safe.
 |  
 |  json(self, **kwargs)
 |      Returns the json-encoded content of a response, if any.
 |      
 |      :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
 |      :raises requests.exceptions.JSONDecodeError: If the response body does not
 |          contain valid json.
 |  
 |  raise_for_status(self)
 |      Raises :class:`HTTPError`, if one occurred.
 |  
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |  
 |  apparent_encoding
 |      The apparent encoding, provided by the charset_normalizer or chardet libraries.
 |  
 |  content
 |      Content of the response, in bytes.
 |  
 |  is_permanent_redirect
 |      True if this Response one of the permanent versions of redirect.
 |  
 |  is_redirect
 |      True if this Response is a well-formed HTTP redirect that could have
 |      been processed automatically (by :meth:`Session.resolve_redirects`).
 |  
 |  links
 |      Returns the parsed header links of the response, if any.
 |  
 |  next
 |      Returns a PreparedRequest for the next request in a redirect chain, if there is one.
 |  
 |  ok
 |      Returns True if :attr:`status_code` is less than 400, False if not.
 |      
 |      This attribute checks if the status code of the response is between
 |      400 and 600 to see if there was a client error or a server error. If
 |      the status code is between 200 and 400, this will return True. This
 |      is **not** a check to see if the response code is ``200 OK``.
 |  
 |  text
 |      Content of the response, in unicode.
 |      
 |      If Response.encoding is None, encoding will be guessed using
 |      ``charset_normalizer`` or ``chardet``.
 |      
 |      The encoding of the response content is determined based solely on HTTP
 |      headers, following RFC 2616 to the letter. If you can take advantage of
 |      non-HTTP knowledge to make a better guess at the encoding, you should
 |      set ``r.encoding`` appropriately before accessing this property.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __attrs__ = ['_content', 'status_code', 'headers', 'url', 'history', '...

R.links
                 
{}
R.attrs
                 
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    R.attrs
AttributeError: 'Response' object has no attribute 'attrs'
R.title
                 
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    R.title
AttributeError: 'Response' object has no attribute 'title'
html.title
                 
<title>To Hell with the Devil - YouTube</title>
html.title.string
                 
'To Hell with the Devil - YouTube'
html.title.text
                 
'To Hell with the Devil - YouTube'
title_tags = html.find_all("meta", attrs={"property":"og:title"})
                 
for i in title_tags:
                 print(i)

                 
<meta content="To Hell with the Devil" property="og:title"/>
title_tags.text
                 
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    title_tags.text
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2428, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
title_tags["content"]
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    title_tags["content"]
TypeError: list indices must be integers or slices, not str
title_tags.attrs["content"]
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    title_tags.attrs["content"]
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2428, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'attrs'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
title_tags.attr["content"]
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    title_tags.attr["content"]
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2428, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'attr'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
title_tags[0].attr["content"]
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    title_tags[0].attr["content"]
TypeError: 'NoneType' object is not subscriptable
title_tags[0].attrs["content"]
'To Hell with the Devil'
title_tags = html.find("meta", attrs={"property":"og:title"})
title_tags
<meta content="To Hell with the Devil" property="og:title"/>
html

html.title
<title>To Hell with the Devil - YouTube</title>
>>> html["meta"]
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    html["meta"]
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 1573, in __getitem__
    return self.attrs[key]
KeyError: 'meta'
>>> html.meta
<meta content="IE=edge" http-equiv="X-UA-Compatible"/>
>>> html.meta["name"]
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    html.meta["name"]
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 1573, in __getitem__
    return self.attrs[key]
KeyError: 'name'
>>> html.meta.attrs
{'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'}
>>> s = "https://www.youtube.com/watch?v=EhRJiiF11vo&list=OLAK5uy_lWsF2gOUCoNvFjzAUXGKE-Ldr6byjkEhI&index=58"
>>> s.find("&")
43
>>> s[:43]
'https://www.youtube.com/watch?v=EhRJiiF11vo'
>>> 7.5 > 0
True
>>> 7.5 <10
True
>>> 9.9 < 10
True
>>> 3.0 %1
0.0
>>> 3.3%1
0.2999999999999998
>>> is_integer(3.0)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    is_integer(3.0)
NameError: name 'is_integer' is not defined
>>> L = ["a", "b", "c", "d"]
>>> if len(L) > 2:
...     notes = (L[2:-1]).join(" ")
... 
...     
Traceback (most recent call last):
  File "<pyshell#189>", line 2, in <module>
    notes = (L[2:-1]).join(" ")
AttributeError: 'list' object has no attribute 'join'
>>> L[-1]
'd'
>>> L[2:-1]
['c']
>>> L[1:]
['b', 'c', 'd']
>>> L[2:]
['c', 'd']
>>> " ".join(L[2:])
'c d'
>>> L = ["a", "b", "c"]
>>> " ".join(L[2:])
'c'
