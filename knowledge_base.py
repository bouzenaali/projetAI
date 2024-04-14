from aima3.utils import *
from aima3.logic import *
from utils import *

kb = FolKB()

# Define fields of study
fields = [
    {"name": "Computer Science", "Type": "Science", "Interest": "High", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Mechanical Engineering", "Type": "Engineering", "Interest": "Medium", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Psychology", "Type": "Social Science", "Interest": "High", "JobProspects": "Medium", "High School": "Literary"},
    {"name": "Economics", "Type": "Social Science", "Interest": "Medium", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Art History", "Type": "Humanities", "Interest": "Low", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Biology", "Type": "Science", "Interest": "High", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "History", "Type": "Humanities", "Interest": "Medium", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Physics", "Type": "Science", "Interest": "High", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "Political Science", "Type": "Social Science", "Interest": "Medium", "JobProspects": "Medium", "High School": "Literary"},
    {"name": "Mathematics", "Type": "Science", "Interest": "High", "JobProspects": "High", "High School": "Scientific"},
    {"name": "Chemistry", "Type": "Science", "Interest": "High", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "Philosophy", "Type": "Humanities", "Interest": "Medium", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Sociology", "Type": "Social Science", "Interest": "Medium", "JobProspects": "Medium", "High School": "Literary"},
    {"name": "Anthropology", "Type": "Social Science", "Interest": "Medium", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Geology", "Type": "Science", "Interest": "Medium", "JobProspects": "Medium", "High School": "Scientific"},
    {"name": "Linguistics", "Type": "Humanities", "Interest": "Medium", "JobProspects": "Low", "High School": "Literary"},
    {"name": "Astronomy", "Type": "Science", "Interest": "High", "JobProspects": "Medium", "High School": "Scientific"},
    # Add more fields of study as needed

]

# Add fields of study to the knowledge base
for field in fields:
    kb.tell(expr(f"Field('{field['name']}')"))  # Enclose field name in quotes
    kb.tell(expr(f"Type('{field['name']}', '{field['Type']}')"))  # Enclose field type in quotes
    kb.tell(expr(f"JobProspects('{field['name']}', '{field['JobProspects']}')"))  # Enclose job prospects in quotes
    kb.tell(expr(f"HighSchool('{field['name']}', '{field['High School']}')"))  # Enclose high school in quotes

# Define student preferences and constraints
kb.tell(expr('Student(Me)'))
kb.tell(expr('PreferredField(Me, "Computer Science")'))  # Example preferred field of study
kb.tell(expr('PreferredJobProspects(Me, "High")'))  # Example preferred job prospects
kb.tell(expr('PreferredHighSchool(Me, "Scientific")'))  # Example preferred high school association
kb.tell(expr('PreferredType(Me, "Science")'))  # Example preferred type of field

# Rules and Preferences
# Prefer fields that match the student's preferred field of study
kb.tell(expr('PreferField(Me, x) & PreferredField(Me, x) ==> RecommendField(x, Me)'))

# Prefer fields with high job prospects
kb.tell(expr('PreferField(Me, x) & PreferredJobProspects(Me, "High") & JobProspects(x, "High") ==> RecommendField(x, Me)'))

# Prefer fields associated with the student's preferred high school type
kb.tell(expr('PreferField(Me, x) & PreferredHighSchool(Me, y) & HighSchool(x, y) ==> RecommendField(x, Me)'))

# If no specific preferences match, recommend fields with high job prospects by default
kb.tell(expr('PreferField(Me, x) ==> RecommendField(x, Me)'))  # Default recommendation

# If multiple fields match preferences, recommend the one with the highest interest level
kb.tell(expr('PreferField(Me, x) & PreferField(Me, y) & Interest(x, "High") & Interest(y, "Medium") ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) & PreferField(Me, y) & Interest(x, "Medium") & Interest(y, "Low") ==> RecommendField(x, Me)'))

# Prefer fields with high interest level
kb.tell(expr('PreferField(Me, x) & Interest(x, "High") ==> RecommendField(x, Me)'))

# Prefer fields with medium interest level if high interest level fields are not available
kb.tell(expr('PreferField(Me, x) & Interest(x, "Medium") & Not(Interest(x, "High")) ==> RecommendField(x, Me)'))

# Prefer fields with high job prospects and interest level
kb.tell(expr('PreferField(Me, x) & PreferredJobProspects(Me, "High") & JobProspects(x, "High") & Interest(x, "High") ==> RecommendField(x, Me)'))

# Avoid recommending fields with low interest level
kb.tell(expr('PreferField(Me, x) & Interest(x, "Low") ==> Not(RecommendField(x, Me))'))

# Prefer fields of the preferred type if available
kb.tell(expr('PreferField(Me, x) & PreferredType(Me, Type(x)) ==> RecommendField(x, Me)'))

# If no specific preferences match, recommend fields with medium job prospects by default
kb.tell(expr('PreferField(Me, x) ==> RecommendField(x, Me)'))  # Default recommendation
