import os
import requests
import wget
from bs4 import BeautifulSoup

def getLinks(linkUrl):
	r = requests.get(linkUrl)
	soupLinks = BeautifulSoup(r.content, "html.parser")
	for links in soupLinks.find_all("a"):
		hrefs = links.get("href")
		print()
		print(hrefs)
		linkFile = open("links.txt", "a")
		linkFile.write("\n" + hrefs)
	linkFile.close()
	print()
	print("Done.")
	input("Press Enter.")
	print()

def getSource(sourceUrl):
	s = requests.get(sourceUrl)
	file = wget.download(sourceUrl)
	os.rename(file, "source.html")
	file = "source.html"
	print()
	print("Done.")
	print("Saved as " + file)
	input("Press Enter.")
	print()

def getImages(imageUrl):
	imgUrl = requests.get(imageUrl)
	soupImg = BeautifulSoup(imgUrl.content, "html.parser")
	linkFile = open("images.txt", "a")
	linkFile.write("<!doctype html />\n<html>\n<center>")
	for imgs in soupImg.find_all("img"):
		imgLink = imgs.get("src")
		print()
		print(imgLink)
		linkFile.write("\n" + "<img src='" + str(imgLink) + "'/>")
	linkFile.write("\n</center>")
	linkFile.write("\n<style>\nbody\n {padding:0px; margin:0px;} \nimg\n {padding:0px; margin:0px; height:100px; width:100px; border:none;} \n</style>")
	linkFile.write("\n</html>")
	linkFile.close()
	os.rename("images.txt", "images.html")
	print()
	print("Done.")
	input("Press Enter.")
	print()

def getContent(contentUrl):
	conUrl = requests.get(contentUrl)
	soupCon = BeautifulSoup(conUrl.content, "html.parser")
	contentFile = open("content.txt", "a")
	for stanzas in soupCon.find_all(["h1", "h2", "p", "span"]):
		content = stanzas.get_text()
		contentFile.write("\n" + content)
	contentFile.close()
	print()
	print("Done.")
	input("Press Enter.")
	print()