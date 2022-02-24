from flask import Flask
import pymongo
import os # importing operating system module

MONGODB_URI = 'mongodb+srv://sirnaelc7:<password>@30daysofpython.f8p8y.mongodb.net/30DaysOfPython?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client.thirty_days_of_python

students = [
        {'name':'Tanjiro','country':'Japan','city':'Kyoto','age':16},
        {'name':'Inosuke','country':'Japan','city':'Kyoto','age':16},
        {'name':'Zenitsu','country':'Japan','city':'Kyoto','age':16},
    ]

for student in students:
    db.students.insert_one(student)

print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
