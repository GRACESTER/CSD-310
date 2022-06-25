from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ln46gl0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})
print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

result = db.students.update_one(
     {"student_id" : "1007"},
     {
    "$set": {"last_name":"Smith"}
     }
) 

print("-- DISPLAYING STUDENT DOCUMENT FROM find one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

print("End of program, press any key to continue...")