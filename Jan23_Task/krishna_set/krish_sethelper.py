import logging
f3=open("C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\setlog.txt","w")
logging.basicConfig(filename="C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\setlog.txt",level=logging.INFO,format ='%(asctime)s %(message)s')


class setmethods:

    def __init__(self,s1):
        logging.info("Entered init method with input as {}".format(s1))
        if type(s1)==set:
            self.s1=s1
            logging.info("Exiting the  init method after setting the object as  as {} ".format(self.s1))
        else:
            logging.error("Some irrelevant data is inputed {}".format(s1))
            raise Exception("You have not given set as input ,please check once ")


    def myset(self):
        """this helps in obtaining the set"""
        logging.info("Entered myset method ")
        logging.info("My set is ...{}".format(self.s1))
        logging.info("Exiting the myset method")
        return self.s1

    def unionmynewset(self,s2):
        """This helps in union of two sets"""
        logging.info("Entered union set method with new inputs as ..{}".format(s2))
        self.s1=self.s1.union(s2)
        logging.info("Executed the union oprration successfully")
        return self.s1

    def findinterectionwithset(self,s2):
        """This helps to find out the intersection with the set and object"""
        logging.info("Entered findinterectionwithset  with set as {} ".format(s2))
        int=self.s1.interesect(s2)
        logging.info("Intersection elements are ...{}".format(int))
        return int

    def findsymdiff(self,s2):
        """This helps to find out the symmetric difference  with the set we pass and object and returns the ouput but no update to the set"""
        logging.info("Entered findsymdiff  with set as {} ".format(s2))
        diff = self.s1.symmetric_difference(s2)
        logging.info("Symmetric difference is  ...{}".format(diff))
        return diff

    def popmyset(self):
        "This helps to pop elemets in the set"""
        logging.info("Entered the popmyset method...")
        self.s1.pop()
        logging.info("after pop executed the object has values {}".format(self.s1))
        return self.s1

    def ismysetsubset(self,s2):
        """Helps us to determinse if this object is subset of the set we pass"""
        logging.info("The set that has been passed is {}".format(s2))
        logging.info("The data inside the set object we have is {}".format(self.s1))
        bool=self.s1.issubset(s2)
        return bool

    def discardelefrommyset(self,k):
        """Helps us to remove a particular elem from a set"""
        logging.info("Entered discardelefrommyset with elem to be removed as {}".format(k))
        self.s1.discard(k)
        logging.info("Post discard of element we have the set as".format(self.s1))
        return self.s1

    def sizeofset(self):
        """Determines the size of ser"""
        logging.info("Entering the sizeofset")
        sz= len(self.s1)
        logging.info("Size of set is {}".format(sz))
        return sz