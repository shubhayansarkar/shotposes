import pymongo
def mongo_insert(data):
    client = pymongo.MongoClient("mongodb+srv://shubhayan:shubhayan@cricketshotsdb.t5ljuo9.mongodb.net/?retryWrites=true&w=majority")
    shorts_db=client['shorts_db']
    shorts_tab=shorts_db['shorts_tab']
    done=shorts_tab.insert_one(data)
    # return True
