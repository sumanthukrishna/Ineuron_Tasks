from databaseCon import dbmethods
import logging
logging.getLoggerClass()
logging.basicConfig(filename="C:\\DS\\Ineuron_Tasks\\MongoDB\\logfiles\\userops.txt", level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

#First lets create an object to access the methods as we have created them in the class
u=dbmethods.dbhelper()


#Menu of Operations is as below
#All the Inputs are cllected from the User from CMD only
#1.Load data into the Database
#2.Retrive given number of documents
#3.Retrieve a document matching certain parametrs
#4.Insert a Document  by taking input from user
#5.Update a Document by taking input from user
#6 delete a document matching few params
#7.Drop the collection --And here once collection is dropped you will be exited out of the program
#If you want to abruptly end the loop of processing the data give your input  as 100

#Lets check if a aparticlaur data
loadflag=False
dic1={}
dic2={}
choice=0
while (choice!=100):
    try:
        choice = int(input("Enter your choice "))
        if choice >=1 and choice <=7:
            if choice ==1 and loadflag==False:
                logging.info("Entereed Load Data Operation ")
                loadflag = True
                u.loaddata()
            elif choice ==2:
                logging.info("Entereed retrieval doc Operation ")
                data=u.retrivealldoc(int(input(('Enter no of documnets to be retrieved '))))
                for i in data:
                    logging.info(i)
            elif choice ==3:
                logging.info("Retrieve a document matching certain parameters Operation ")
                par1=input('Enter param1')
                par2=input('Enter the param2')
                u.finddocument(par1,par2)
            elif choice ==4:
                flag=False
                d={}
                logging.info("Insert a Document operation by taking input from user ")
                try:
                    d['Chiral indice n'] = input('Enter chiral n indice value')
                    d['Chiral indice m'] = input('Enter chiral m indice value ')
                    d['Initial atomic coordinate u'] = input('Initial atomic coordinate u')
                    d['Initial atomic coordinate v'] = input('Initial atomic coordinate v')
                    d['Initial atomic coordinate w'] = input('Initial atomic coordinate w')
                    d["Calculated atomic coordinates u'"] = input("Calculated atomic coordinates u'")
                    d["Calculated atomic coordinates v'"] = input("Calculated atomic coordinates v'")
                    d["Calculated atomic coordinates w'"] = input("Calculated atomic coordinates w'")
                except Exception as e:
                    flag=True
                    logging.error("Encountered an error while collection input from user "+str(e))
                if flag==False:
                    u.insertdocintocollection(d)
            elif choice ==5:
                logging.info('Entering the updatedocument operation as per user request operation')
                try:
                    key=input('Enter key ')
                    value1=input('Enter old value ')
                    value2=input('Enter new value ')
                except Exception as e:
                    logging.error("Encounterd an while collection input from user ")
                    u.updatedocument(key,value1,value2)
            elif choice ==6:
                d3={}
                logging.info('Entering the delete  a document as per user request operation')
                try:
                    key3 = input('Enter key 1 ')
                    value3 = input('Enter value 1')
                    d3[key3]=value3
                except Exception as e:
                    logging.error("Encounterd an while collection input from user ")
                u.deletedocument(d3)
            elif choice==7:
                logging.info('Entering the drop collection operation as per user request ')
                u.dropcollection()
                loadFlag=False
            else:
                logging.info("Please enter valid choice number from menu")

    except Exception as che:
        logging.error('Invalid entry by the user ,please enter only postive integers '+str(che))






