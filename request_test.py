##This script downloads the Romeo and Juliet text from the Gutenberg Project page
##and stores it as a txt file in your local machine.

#Import required modules
import requests
#Downloads content from the Gutenberg Project
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

#The program halts if bad download occurs
res.raise_for_status()

#Create file in current directory
playFile = open('RomeoAndJuliet.txt', 'wb')

#Writes the downloaded content on the document
for chunk in res.iter_content(100000):
  playFile.write(chunk)

#Closes file
playFile.close()
