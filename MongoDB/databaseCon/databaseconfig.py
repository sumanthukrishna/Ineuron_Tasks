import logging
import pymongo


class DBConnection:

    def dbconstart(self):
        '''This method will help us to establish  the connection with Cloud MongoDatabase '''
        logging.info('Started to establish  the database connection ')

        try:
            client = pymongo.MongoClient(
                "mongodb+srv://test:test@krishnambd.81zpp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            db =client['bulk_insertion']
            #Our database name is bulk insertion here ,we want to store the data in this database
            logging.info ('successfully established the connection with database ')
            return db
        except Exception as e:
            logging.error('Unable to establish the connection due to some issues  '+str(e))

    def getcollection(self):
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://test:test@krishnambd.81zpp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            db = client.bulk_insertion
            col=db.Carbon_nanotubes
            return col
        except Exception as e:
            logging.error('Unable to get the collection   ' + str(e))









