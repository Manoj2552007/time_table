from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def home(request):
    # Time table data
    timetable = {
        "Monday": ["FREE SLOT", "MATHS", "", "STATS", "FREE SLOT"],
        "Tuesday": ["Free Slot", "OS", "Lunch", "DBMS", "MATHS"],
        "Wednesday": ["CN", "OS", "Lunch", "MENTOR MEET", "FWAD"],
        "Thursday": ["C", "STATS", "Lunch", "EMPD", "CN"],
        "Friday": ["C", "FWAD", "Lunch", "EMPD", "MATHS"]
    }

    subjects = [
        {"code": "19AI414", "name": "Fundamentals of Web Application Development "},
        {"code": "19MA220", "name": "MATHS FOR AI"},
        {"code": "19AI303", "name": "EMPD"},
        {"code": "19CS404", "name": "DataBase Management Systems and its Applications"},
        {"code": "19MA211", "name": "Statistics and Numerical Methods"},
        {"code": "19CS406", "name": "COMPUTER NEWTORKS"},
        {"code": "19CS405", "name": "Operating Systems"},
        {"code": "19AI304", "name": "C programming"}
    ]

    return render(request, 'home.html', {
        'timetable': timetable,
        'subjects': subjects,
    })

# Create your views here.
