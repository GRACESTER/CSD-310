Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ln46gl0.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["pytech"]
mycol = mydb["students"]
mylist = [
        { "first_name": "Fred", "last_name": "Jones", "student_id": "1007"},
        { "first_name": "Jill", "last_name": "Johnson", "student_id": "1008"},
        { "first_name": "Jack", "last_name": "Wilson", "student_id": "1009"}
         ]
x = mycol.insert_many(mylist)
print(x.inserted_ids)