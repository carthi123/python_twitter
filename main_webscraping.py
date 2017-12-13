__author__='Carthi'

#Used Python 2.7 and linux system for writing the script
#give the approriate path for chromedriver and use python 2.7, if you are checking the code in Windows

# Importing all required libraries
from bs4 import BeautifulSoup
from selenium import webdriver
#Importing sentiment analysis module (tweetanalysis)
import tweetanalysis

#Loading the given page with the help of selenium and parsing it with help of beautiful soup
def get_page_html( webpage ):
    chromedriver_path = r"/home/m1037619/Desktop/Python_Project_carthi/chromedriver"
    driver = webdriver.Chrome(chromedriver_path)
    driver.get(webpage)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup

#Exracting the celebrity data from the html
def get_data_from_html( soup ):
    imdbinfo = {}
    count = 0
    for tag in soup.section.find_all('a'):
        s = tag.getText(":")
        if ":" in s:
            imdbinfo[count] = {}
            info=tag.getText(":")
            namep, movie = info.split(",", 1)
            name, profession = namep.split(":")
            image = (tag.next_element).attrs['src']
            imdbinfo[count]["Name"] = str(name.encode('utf8'))
            imdbinfo[count]["Profession"] = str(profession)
            imdbinfo[count]["Movie"] = str(movie)
            imdbinfo[count]["Image address : "] = str(image)
            count += 1
    return imdbinfo

# writing the analysed output to the file ( output.txt )
def writing_output( data ):
    output = open ("output.txt", 'w')
    for i,j in data.iteritems():
        #print "Name : ", j['Name']
        output.write("Name : " + j['Name']+ '\n')
        #print "Image address : ",j['Image address : ']
        output.write("Image address : " +j['Image address : ']+ '\n')
        #print "Profession :", j['Profession']
        output.write("Profession :" + j['Profession']+ '\n' )
        #print "Movie : ", j['Movie']
        output.write("Movie : " + j['Movie'] + '\n' )
        #print "Overall Sentiment on Twitter :",j['Twitter sentimental analysis']
        output.write("Overall Sentiment on Twitter :" + j['Twitter sentimental analysis'] + '\n')
        output.write("\n\n")

if __name__ == '__main__':
    print ("""
-------------------------------------------------------------------------
            ( USED PYTHON 2.7 AND LINUX FOR EXECUTION)
Download the Chromedriver(https://chromedriver.storage.googleapis.com/index.html?path=2.29/)
and change appropriate the path of the chrome driver in the get_page_html () function
--------------------------------------------------------------------------
           """)
    webpage = "http://m.imdb.com/feature/bornondate"
    soup = get_page_html( webpage )
    celeb_data =  get_data_from_html( soup )
    data =  tweetanalysis.tweetanalysis( celeb_data )
    writing_output( data )
    print ("PROGRAM EXCEUTED SUCSSFULLY CHECK THE output.txt file for output")
