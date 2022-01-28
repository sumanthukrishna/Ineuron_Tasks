
import logging
f1=open("C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\diclog.txt","w")
logging.basicConfig(filename="C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\diclog.txt",level=logging.DEBUG,format ='%(asctime)s %(message)s')

class dicmethods:

    def __init__(self,d):
        logging.info("Entered init method with input as ".format(d))
        if type(d)==dict:
            self.d=d
            logging.info("Exiting the init method with input as {} ".format(self.d))
        else:
            logging.error("Some irrelevant data is inputed {}".format(d))
            raise Exception ("You have not given dictionary as input ,please check once ")

    def getkeys(self):
        """returns the keys of the dictionary object"""
        logging.info("entered get keys methods")
        b=list( self.d.keys())
        logging.info("keys for the object are ..{}".format(b))
        logging.info("exiting the getkeys method")
        return b

    def getvalues(self):
        """returns the values of the dictionary object"""
        logging.info("entered getvalues methods")
        b = list(self.d.values())
        logging.info("values  for the object are ..{}".format(b))
        logging.info("exiting the getvalues method")
        return b

    def getvalueforkey(self,key):
        """it will fetch thw value for a particular key"""
        logging.info("entered the getvalueforkey method")
        value= self.d[key]
        logging.info("values in that key is ..{}".format(value))
        logging.info("exiting the getvalueforkey method")
        return value

    def takeinput(self,key,value):
        """it will add a new pair to the dicitonary object"""
        logging.info("entered the takeinput method with key and value as ".format(key,value))
        self.d[key]=value
        logging.info("now the new dictionary is ...{}".format(self.d))
        logging.info("exiting the takeinput method ")

    def showmydict(self):
        """return the current dicitonary object"""
        logging.info("entered the showmydict method")
        mydict= self.d
        logging.info("hey here is your dictionary {}".format(mydict))

