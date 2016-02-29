import os
import requests
import wget
from bs4 import BeautifulSoup

def getLinks(linkUrl):
	r = requests.get(linkUrl)
	soup = BeautifulSoup(r.content, "html.parser")
	for links in soup.find_all("a"):
		hrefs = links.get("href")
		print(hrefs)
		linkFile = open("links.txt", "a")
		linkFile.write("\n" + hrefs)
	print("")
	print("Answer is case sensitive. (Use Lower Case.)")
	saveOrNah = input("Save Links? y/n: ")
	if saveOrNah == "y":
		linkFile.close()
		print("Saved.")
		os.system("pause")
	else:
		linkFile.close()
		os.remove("links.txt")
		print("Not Saved.")
		os.system("pause")

def getSource(sourceUrl):
	s = requests.get(sourceUrl)
	print(s.content)
	os.system("pause")
	file = wget.download(sourceUrl)
	os.rename(file, "source.html")
	file = "source.html"
	print("")
	print("Saved as " + file)
	os.system("pause")

def getImages(imageUrl):
	imgUrl = requests.get(imageUrl)
	soupImg = BeautifulSoup(imgUrl.content, "html.parser")
	linkFile = open("images.txt", "a")
	linkFile.write("<!doctype html />\n<html>\n<center>")
	for imgs in soupImg.find_all("img"):
		imgLink = imgs.get("src")
		print(imgLink)
		linkFile.write("\n" + "<img src='" + str(imgLink) + "'/>")
	linkFile.write("\n</center>")
	linkFile.write("\n<style>\nbody\n {padding:0px; margin:0px;} \nimg\n {padding:0px; margin:0px; height:100px; width:100px; border:none;} \n</style>")
	linkFile.write("\n</html>")
	linkFile.close()
	os.rename("images.txt", "images.html")
	os.system("pause")