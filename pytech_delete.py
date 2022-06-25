from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ln46gl0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})
print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY --")
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

#the insert
student_insert = { "student_id": 1010,
                    "first_name": "Sarah",
                     "last_name": "Jackson"}

new_student_Id = db.students.insert_one(student_insert).inserted_id
print("-- INSERT STATEMENTS --")
print("Inserted student record {} {} into the students collection with document_id {}".format(student_insert["first_name"], student_insert["last_name"], new_student_Id))
print()
print()
print("--DISPLAY NEW STUDENT DOCUMENT LIST--")
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")
print()
print("--DELETED STUDENT ID: 1010--")
db.students.delete_one({"student_id": 1010})
print()
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})
for doc in docs:
    print(f"Student ID: {doc['student_id']}\nFirst Name: {doc['first_name']}\nLast Name: {doc['last_name']}\n")

print("End of program, press any key to continue")