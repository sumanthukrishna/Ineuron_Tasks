import logging
f2 = open("C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\listlog.txt", "w")
logging.basicConfig(filename="C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\listlog.txt", level=logging.DEBUG, format ='%(asctime)s %(message)s')


class lismethods:

    def __init__(self, l1):
        logging.info("Entered init method with input as {}".format(l1))
        if type(l1) == list:
            self.l1=l1
            logging.info("Exiting the  init method after setting the object as  as {} ".format(self.l1))
        else:
            logging.error("Some irrelevant data is inputed {}".format(l1))
            raise Exception("You have not given List as input ,please check once ")

    def listsize(self):
        logging.info("Entered the list size method")
        """this helps to get the size of the lisy"""
        sz=len(self.l1)
        logging.info("Size of the object is ..{}".format(sz))
        logging.info("Exiting the list size method")
        return sz

    def comblists(self,l2):
         """This add the new list directly to the existing list"""
         logging.info("Entered the comblists method with the new list as {}".format(l2))
         self.l1.append(l2)
         logging.info("After appeninf the new list to the current object we now have ...{}".format(self.l1))
         return self.l1

    def popelement(self,k):
        """this method helps to pop out an element"""
        logging.info("Entered the pop element methods with the element to be popped as ..{}".format(k))
        lstafterpop=self.l1.pop(k)
        logging.info("List after popped is ..{}".format(lstafterpop))
        return lstafterpop

    def revlist(self):
        """this helps to reverse the list"""
        logging.info("Entered the rev list method")
        revlst= self.l1[::-1]
        logging.info("Executed the reverse and its a inplace execution and output is {} ".format(revlst))
        return revlst

    def extendlist(self,l2):
        """add the new list to the exiting list by opening it """
        logging.info("Entered the extend list method with input as {} ".format(l2))
        self.l1.extend(l2)
        logging.info("Post extending the list object with the new list ...{}".format(self.l1))
        return self.l1

    def geteleforanIndex(self,k):
        """Pass the index and get the element at that location"""
        logging.info("Entered the geteleforanIndex methods with needed element index as {}".format(k))
        myelem=self.l1[k]
        logging.info("Exited the method after fetching the eleemnt as ..{}".format(self.l1[k]))
        return myelem



    def showmylist(self):
        """returns the data in current object """
        logging.info("Entered showmylist method")
        return self.l1