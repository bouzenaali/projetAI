from aima3.utils import *
from aima3.logic import *
from utils import *

kb = FolKB()

# Define fields of study
fields = [
    {"name": "Computer Science", "Type": "Science", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Mechanical Engineering", "Type": "Engineering", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Psychology", "Type": "Social Science", "JobProspects": "Medium", "High School": "Literary"},
    {"name": "Economics", "Type": "Social Science", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Art History", "Type": "Humanities", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Biology", "Type": "Science", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "History", "Type": "Humanities", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Physics", "Type": "Science", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "Political Science", "Type": "Social Science", "JobProspects": "Medium", "High School": "Literary"},
    {"name": "Mathematics", "Type": "Science", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Chemistry", "Type": "Science", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "Philosophy", "Type": "Humanities", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Sociology", "Type": "Social Science", "JobProspects": "Medium", "High School": "Literary"},
    {"name": "Anthropology", "Type": "Social Science", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Geology", "Type": "Science", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "Linguistics", "Type": "Humanities", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Astronomy", "Type": "Science", "JobProspects": "Medium", "High School": "Scientific"},
    # Add more fields of study as needed

]

# Add fields of study to the knowledge base
for field in fields:
    kb.tell(expr(f"Field({field['name']})"))
    kb.tell(expr(f"Type({field['name']}, {field['Type']})"))
    kb.tell(expr(f"JobProspects({field['name']}, {field['JobProspects']})"))
    kb.tell(expr(f"HighSchool({field['name']}, {field['High School']})"))

# Define student preferences and constraints
kb.tell(expr('Student(Me)'))
kb.tell(expr('Gender(Me, "male")'))  # Example gender
kb.tell(expr('Age(Me, 18)'))  # Example age
kb.tell(expr('PreferredType(Me, "Science")'))  # Example preferred field type
# Add more preferences or constraints as needed
