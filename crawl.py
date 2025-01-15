# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
 
# def urls_list(url):
 
#     response=requests.get(url)
       
#     soup=BeautifulSoup(response.text,"html.parser")
 
#     links=[]
#     for tag in soup.find_all('a',href=True):
#             url1=urljoin(url,tag['href'])
#             links.append(url1)
#     return links
 
# def xyz(links,filename):
#     with open(filename,'w') as file:
#           for link in links:
#                file.write(link + '\n')
#     print(f'Links saved : {filename}')
         
   
# if __name__=="__main__":
#     # url="https://www.cricbuzz.com/"
#     url="https://aimicrodegree.org/login"
#     links=urls_list(url)
#     if links:
#          xyz(links,"aimicro.txt")
#          print(f'Links: {links}')
#          for link in links:
#               print(link)

#################################################### DOWNLOAD IMAGE FROM WEBSITE #################################
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import os
# def ai(url):
#     response=requests.get(url)

#     soup=BeautifulSoup(response.text,'html.parser')

#     images=[] 
#     for image in soup.find_all('img',src=True):
#         img1=urljoin(url,image['src'])
#         images.append(img1)

#     print(f'Image are : {images}')
#     for image in images:
#         print(image)
#     return images 

# def aimicro(images,directory):
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#         print(f'Directory : {directory}')
    
#     for x,image1 in enumerate(images):
#         img1=requests.get(image1).content
#         name=f'image{x+1}.jpeg'
#         path=os.path.join(directory,name)

#         with open(path,'wb') as file1:
#             file1.write(img1)

#         print(f'images : {path}')

# if __name__=="__main__":
#     url="https://aimicrodegree.org/"
#     images = ai(url)
#     if images :
#         aimicro(images,'Images')

##################################################### KNOW THE CODE OF WEBSITE ##################################################
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
 
def abcd(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
 
    print(f"HTML Content: {soup.prettify()}")  # Print the HTML content for debugging
 
    images = []
    for image in soup.find_all('img', src=True):
        img1 = urljoin(url, image['src'])
        images.append(img1)
 
    print(f'Images are: {images}')
    for image in images:
        print(image)
   
    return images  # Return the list of images
 
def abcd1(images, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Directory created: {directory}')
   
    for x, image1 in enumerate(images):
        img1 = requests.get(image1).content
        name = f'image{x+1}.jpeg'
        path = os.path.join(directory, name)
 
        with open(path, 'wb') as file1:
            file1.write(img1)
 
        print(f'Saved image: {path}')
 
if __name__ == "__main__":
    url = "https://redtape.com/collections/footwear"
    images = abcd(url)
    if images:
        abcd1(images, 'Images')