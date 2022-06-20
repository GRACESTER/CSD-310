Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pymongomyclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.ln46gl0.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["pytech"]
mycol = mydb["students"]

###this will print all of the documents in the database
docs = mydb.students.find({})
for doc in docs:
  print(doc)


###this will only print the document associated with student id 1007
doc = mydb.students.find_one({"student_id": "1007"})
print(doc)