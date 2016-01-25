import urllib.request
class DownloadDesigner:
    # Download the file from URL and save it locally under file_name
    #
    def getnewdesignerversion(url,directory,file_name):
        filename = file_name + "\\" + directory
        print(filename)
        urllib.request.urlretrieve(url,filename)

#url = "http://www.voipmechanic.com/documents/sip_tutorial.pdf"
#file_name = "sip_tutorial.pdf"
#dir = "/tmp"
#DownloadDesigner.getnewdesignerversion(url,dir,file_name)
