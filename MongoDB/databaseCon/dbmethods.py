import logging
import csv
from databaseCon import databaseconfig as dc




class dbhelper:
    def loaddata(self):
        '''This will help us to load the data into the mongodb '''
        logging.info('Starting to load the data by fetching the database connection ')
        try:
            d = dc.DBConnection()
            d1 = d.dbconstart()
            if d1 != '':
                reader = csv.reader(open("C:\\DS\\Ineuron_Tasks\\MongoDB\\coredata\\carbon_nanotubes.csv"),
                                    delimiter=";")
                f = open('C:\\DS\\Ineuron_Tasks\\MongoDB\\processedcarbon_nanotubes.csv', 'w+')
                writer = csv.writer(f)
                for row in reader:
                    writer.writerow(row)
                f.close()
                logging.info('We found the database and starting to load the data')
                coll = d1['Carbon_nanotubes']
                my_csv_file = open("C:\\DS\\Ineuron_Tasks\\MongoDB\\processedcarbon_nanotubes.csv", 'r')
                dict_reader = csv.DictReader(my_csv_file)
                #for i in dict_reader:
                    #coll.insert_one(i)
                coll.insert_many(dict_reader)
                logging.info('successfully loaded the data into the database ')
                return True
            else:
                raise Exception('"You You dont have proper DB connection "')
        except Exception as e1:
            logging.error('Unable to load the data into database' + str(e1))

    def dropcollection(self):
        try:
            logging.info('Starting to drop the colleciton')
            dbcon = dc.DBConnection()
            col = dbcon.getcollection()
            col.drop()
            logging.info ('successfully the collection has been deleted ')
            return True
        except Exception as e:
            logging.error('Unable to drop the collection  in the  database' + str(e))

    def finddocument(self, a, b):
        try:
            logging.info('Entered the method find document with parametres as  {} {} '.format(a,b))
            dbcon = dc.DBConnection()
            col = dbcon.getcollection()
            col.find_one()
            x = col.find_one({a: b})
            logging.info("Below is the document which has been fetched ")
            logging.info(str(x))
            return x
        except Exception as e:
            logging.error('unable to find a specific document matching the parameters ' + str(e))


    def insertdocintocollection(self,d):
        '''This method helps us to insert the documet into the collections '''
        logging.info("Enterd insertdocinto collection with input as {}".format(d))
        try:
            if type(d)!=dict:
                raise Exception("You have not given dictionary  as input ,please check once and try again ")
            else:
                dbcon = dc.DBConnection()
                col = dbcon.getcollection()
                logging.info('document  has been recived from user ')
                col.insert_one(d)
                logging.info('document  has been inserted successfully into collection')
                return True
        except Exception as e:
            logging.error('YInsert document operation failed ')


    def updatedocument(self,key,oldvalue,newvalue):
        ''' This method helps us to update a particular document '''
        try:
            logging.info("Entered update document method with key {} ,old value{},newvalue {}".format(key,oldvalue,newvalue))
            dbcon = dc.DBConnection()
            col = dbcon.getcollection()
            logging.info('Collection has been fetched')
            col.update_many({key:oldvalue},{"$set":{key:newvalue}})
            logging.info("Document has been updated successfully")
            return True
        except Exception as e:
            logging.error('An issue occured while updating the document ')


    def deletedocument(self,d1):
        ''' This method helps us to delete the  documents '''
        try:
            logging.info("Entered delete document method with parameter as {}".format(d1))
            dbcon = dc.DBConnection()
            col = dbcon.getcollection()
            res=col.delete_one(d1)
            cnt=res.deleted_count
            logging.info('No of documents deleted are {}'.format(cnt))
            return True
        except Exception as e:
            logging.error('Delete document operation failed ')


    def retrivealldoc(self,cnt):
        lstone=[]
        '''This methoods helps us to retrieve the documents with certain limitcount '''
        try:
            logging.info("Entered retrieve all documents method with parameter of no of documents to be fetched as {}".format(cnt))
            dbcon = dc.DBConnection()
            col=dbcon.getcollection()
            data = col.find().limit(cnt)
            for i in data:
                lstone.append(i)
            logging.info('All  the {}  documents on the database are fetched successfully '.format(cnt))
            return lstone
        except Exception as e:
            logging.error('document retrieval failed ')






