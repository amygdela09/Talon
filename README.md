# Talon
A Python module to make it a simple task to scrape a website.  Example:  Talon.ScrapeFunction(URL).

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Python Module Dependencies:

1.)os
2.)requests
3.)wget
4.)BeautifulSoup

How To Use:

1.)  Drag Talon.pyc to your project folder.
2.)  In the top of your program's script put "import Talon" without quotations.
3.)  Call the function you so desire.

How To Modify Source:

1.)  Open Talon.py in your preferred text editor or IDE.
2.)  Go to town modifying the code.  It's just plain old Python.

Functions:

Talon.getImages(URL) - Extracts image sources from HTML and generates an HTML file containing the images. (images.html)

Talon.getLinks(URL) - Extracts all href links from HTML and generates a TXT file containing the link addresses. (links.txt)

Talon.getSource(URL) - Downloads the HTML file from the url you chose. (source.html)
