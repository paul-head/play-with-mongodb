import pymongo

conn_str = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn_str)

db = client.the_small_bookstore

if db.books.estimated_document_count() == 0:
    print('inserting data')
    # insert some data
    r = db.books.insert_one({'title': 'The first book', 'isbn': '345355556'})
    print(r, type(r))
    r = db.books.insert_one({'title': 'The second book', 'isbn': '455234888'})
    print(r.inserted_id)
else:
    print('Books already inserted, skipping')

# book = db.books.find_one({"isbn": "765974234779"})
# #  print(book, type(book))
# #book['favorited_by'] = []
# book['favorited_by'].append(42)
# db.books.update_one({'_id': book.get('_id')}, {'$set': book})
# book = db.books.find_one({"isbn": "765974234779"})
# print(book)

db.books.update_one({"isbn": "876854643453"}, {'$addToSet': {'favorited_by': 120}})
book = db.books.find_one({"isbn": "876854643453"})
print(book)
