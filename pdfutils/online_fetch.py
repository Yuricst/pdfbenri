"""
Grab all pdfs in a website and save
"""


import os
import urllib.request
import requests
from bs4 import BeautifulSoup


def get_files(url, dest="./", use_flename=True, extension='pdf'):
    """Get all files from URL with given extension, using BeautifulSoup

    Args:
        url (str): URL where files are embedded
        dest (str): directory where files are to be saved
        use_flenmae (bool): whether to use filename of file
        extension (str): extension of files to be downloaded, embeded in html    
    """

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    elts = soup.find_all("a", href=True)
    count = 1
    for el in elts:
        if el["href"].endswith(extension):
            flepath = os.path.join(url, el["href"])
            # get the file
            if use_flename==True:
                _ = download_file(flepath, dest=dest, filename=None, extension=None)
            else:
                flename_tmp = "file_" + str(count)
                count += 1
                _ = download_file(flepath, dest=dest, filename=flename_tmp, extension=None)
            print("Saved ", el["href"])
    print("Completed! :)")


def download_file(flepath, dest="./", filename=None, extension=None):
    """Function downloads file from URL provided

    Args:
        flepath (str): web URL for file to be downloaded
        dest (str): path to directory where files should be saved
        filename (str): name of file, default takes it from the URL
        extension (str): extension of file to be generated, default takes it from the URL
    
    Returns:
        (str): path to the generated file, including file name and extension
    """

    # set file name if none is provided
    if filename==None:
        filename = os.path.splitext(os.path.basename(flepath))[0]

    # set extension from filename if none is provided
    if extension==None:
        extension = os.path.splitext(os.path.basename(flepath))[1]

    response = urllib.request.urlopen(flepath)    
    fle_fullname = os.path.join(dest, filename + extension)
    file = open(fle_fullname, 'wb')
    file.write(response.read())
    file.close()
    return fle_fullname
 

if __name__=="__main__":
    url = "https://bb.imperial.ac.uk/webapps/blackboard/content/listContent.jsp?course_id=_9819_1&content_id=_1016622_1"
    destination = r"C:\Users\yurio\Google Drive\reflibs\LectureNotes\imperial_ae107"
    get_files(url, destination, extension='pdf')
