#/usr/bin/env python
import subprocess
import sys, getopt,commands,re

#Set Global variables.
#application name:
appname = 'DesignerUpgrade.py'
url = ''
fdirectory = ''
version = '10127'
file = ''
debug = False

class RunCmd(object):
    def cmd_run(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd,shell=True)

def usage():
    global appname
    print(str(appname) + ' instructions')
    print('Options: ')
    print('-h    help, shows help')
    print('-u    URL parameter that will download the designer version. You must ensure this url is to the correct designer version.  ')
    print('-d    dependant on -u option, location to store the downloaded url file')
    print('')
    print('')
    print('')
    print('')
    sys.exit(2)

def iswitch():
    if debug == True :
        print("entering Method iswitch()")
    setGlobal('debug',True)

def dswitch():
    global url,fdirectory,version,file,debug
    if debug == True :
        print("entering Method dswitch() with params :")
    checkdir(fdirectory,version)

    #setGlobal("file", )



def setGlobal(var ,opt):
    global url,fdirectory,version,file,debug
    if debug == True :
        print("entering Method setGlobal() with params :" + str(var) + " = " + str(opt))
    if var == 'url':
        url = opt
    elif var == 'fdirectory':
        fdirectory = opt
    elif var == 'version':
        version = opt
    elif var == 'file' :
        file = opt
    elif var == 'debug' :
        debug = True
    
def checkdir(d , v):
    global debug
    if debug == True :
        print("entering Method checkdir() with params :" + str(d) + " - " + str(v))
      
    subprocess.call('cd '+ d, shell=True)
    #TODO: need to figure out the subprocess method of this as this is Depricated in python3
    
    output = commands.getstatusoutput('ls | grep ' + v + ".zip")

    #if debug == True :
    print("Output is : " + str(output) + " and file should be " + str(output[1]))

#    if output

    #setGlobal('file',output[1])
    if debug == True :
        print str(output)
    #for invalidchars in output:

    if debug == True :
        print "here" + " length " + str(len(output[1])) +" Type : " \
    + str(type(output[1])) + "- " + str(output)



def main(argv):
    global url,fdirectory,version,file,debug
    try:
        opts, args = getopt.getopt(argv, "hid:u:v:", ["help",'dir=',"url=","version="])
    except getopt.GetoptError:
        print('ERROR: ')
        usage()

# Switch processing
    for opt, arg in opts:
        #usage option
        if opt in ('-h','--help'):
            usage()
        elif opt == '-i':
            iswitch()
            print('******debug is set to: ' + str(debug)+ "******")
        elif opt in ('-d', 'dir='):
            setGlobal('fdirectory', arg)
        elif opt in ('-u', '--url='):
            setGlobal('url', arg)
        elif opt in ('-v', '--version='):
            setGlobal('version', arg)
#no switch added!
        #print('else')


    if debug == True :
        print('***END for***')

    #Check File exists
    dswitch()

    if len(url) > 1:
        pass
        if debug == True :
            print('Entered IF urllenght with variables: '+ url +" - " + fdirectory +" - " + version)
            #print(str(file))
            #print(checkdir(fdirectory,version))

    else:
        if debug == True :
            print("Error: no url, please provide a url")
            print("Error: no directory, please provide a directory with -d [location to save url file]")




#Sample usage

#a = RunCmd()
#a.cmd_run('ls -al')
#a.cmd_run('echo "hello"')
#print("starting")
#print("the args passed are ")
#print getopt.getopt(args, optiojns, [long_options])

if __name__ == "__main__":
   main(sys.argv[1:])
