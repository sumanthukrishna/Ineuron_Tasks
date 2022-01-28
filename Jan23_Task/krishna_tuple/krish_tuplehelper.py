import logging
logging.basicConfig(filename="C:\\Users\\krishna\\PycharmProjects\\Jan23_Task\\Logs\\tuplelog.txt", level=logging.DEBUG)

class tupleMethods:
    def __init__(self, t1):
        logging.info("Entered init method with input as {}".format(t1))
        if type(t1) == tuple:
            self.t = t1
            logging.info("Exiting the  init method after setting the object as  as {} ".format(self.t))
        else:
            logging.error("Some irrelevant data is inputed {}".format(t1))
            raise Exception("You have not given List as input ,please check once ")

    def mytuple(self):
        """This just return the tuple"""
        logging.info("tuple object has data ..{}".format(self.t))
        return self.t

    def tuplength(self):
        """This return the length of the tuples"""
        ln = len(self.t)
        logging.info("Size of the tuples is {}".format(ln))
        return ln

    def getindxformyval(self, k):
        """This helps to fetch the index of a certain value"""
        idx = self.t.index(k)
        logging.info("Index of k is..{}".format(idx))
        return idx

    def nooftimeelpresentintuple(self, k):
        """returns the no of times am element is present in tuple"""
        cnt = self.t.count(k)
        logging.info("No of time ele is present in tuple is ..{}")
        return cnt

    def addnewelementsintuple(self, l):
        """This metod helps us to add new elements to tuple """
        logging.info("Entered addnewelementsintuple method with input list as ..{}".format(l))
        l1 = list(self.t)
        l1.extend(l)
        self.t = tuple(l1)
        logging.info("After the elemets are added now the new tuple object is ..{}".format(self.t))
        return self.t
