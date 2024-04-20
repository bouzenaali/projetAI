from aima3.logic import *

kb = FolKB()

# Define fields of study
fields = [
    {"name": "Computer Science", "type": "Science", "interest": "High", "job_prospects": "High", "high_school": "Scientific"},
    {"name": "Computer Engineering", "type": "Engineering", "interest": "High", "job_prospects": "High", "high_school": "Scientific"},
    {"name": "Mechanical Engineering", "type": "Engineering", "interest": "Medium", "job_prospects": "High", "high_school": "Scientific"},
    {"name": "Psychology", "type": "Social Science", "interest": "High", "job_prospects": "Medium", "high_school": "Literary"},
    {"name": "Economics", "type": "Social Science", "interest": "Medium", "job_prospects": "High", "high_school": "Scientific"},
    {"name": "Art History", "type": "Humanities", "interest": "Low", "job_prospects": "Low", "high_school": "Literary"},
    {"name": "Biology", "type": "Science", "interest": "High", "job_prospects": "Medium", "high_school": "Scientific"},
    {"name": "History", "type": "Humanities", "interest": "Medium", "job_prospects": "Low", "high_school": "Literary"},
    {"name": "Physics", "type": "Science", "interest": "High", "job_prospects": "Medium", "high_school": "Scientific"},
    {"name": "Political Science", "type": "Social Science", "interest": "Medium", "job_prospects": "Medium", "high_school": "Literary"},
    {"name": "Mathematics", "type": "Science", "interest": "High", "job_prospects": "High", "high_school": "Scientific"},
    {"name": "Chemistry", "type": "Science", "interest": "High", "job_prospects": "Medium", "high_school": "Scientific"},
    {"name": "Philosophy", "type": "Humanities", "interest": "Medium", "job_prospects": "Low", "high_school": "Literary"},
    {"name": "Sociology", "type": "Social Science", "interest": "Medium", "job_prospects": "Medium", "high_school": "Literary"},
    {"name": "Anthropology", "type": "Social Science", "interest": "Medium", "job_prospects": "Low", "high_school": "Literary"},
    {"name": "Geology", "type": "Science", "interest": "Medium", "job_prospects": "Medium", "high_school": "Scientific"},
    {"name": "Linguistics", "type": "Humanities", "interest": "Medium", "job_prospects": "Low", "high_school": "Literary"},
    {"name": "Astronomy", "type": "Science", "interest": "High", "job_prospects": "Medium", "high_school": "Scientific"},
]

# Add fields of study to the knowledge base
for field in fields:
    kb.tell(expr(f'Field("{field["name"]}")'))
    kb.tell(expr(f'Type("{field["name"]}", "{field["type"]}")'))
    kb.tell(expr(f'Interest("{field["name"]}", "{field["interest"]}")'))
    kb.tell(expr(f'JobProspects("{field["name"]}", "{field["job_prospects"]}")'))
    kb.tell(expr(f'HighSchool("{field["name"]}", "{field["high_school"]}")'))


# Rules and Preferences
kb.tell(expr('PreferredField(Me, x) & Field(x) ==> RecommendField(x, Me)'))
kb.tell(expr('PreferredJobProspects(Me, y) & JobProspects(x, y) ==> RecommendField(x, Me)'))
kb.tell(expr('PreferredHighSchool(Me, z) & HighSchool(x, z) ==> RecommendField(x, Me)'))
kb.tell(expr('PreferredType(Me, w) & Type(x, w) ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) ==> RecommendField(x, Me)')) 
kb.tell(expr('PreferField(Me, x) & PreferredType(Me, Type(x)) ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) & Interest(x, "Low") ==> Not(RecommendField(x, Me))'))
kb.tell(expr('PreferField(Me, x) & PreferredJobProspects(Me, "High") & JobProspects(x, "High") & Interest(x, "High") ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) & Interest(x, "Medium") & Not(Interest(x, "High")) ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) & Interest(x, "High") ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) & PreferField(Me, y) & Interest(x, "High") & Interest(y, "Medium") ==> RecommendField(x, Me)'))
kb.tell(expr('PreferField(Me, x) & PreferField(Me, y) & Interest(x, "Medium") & Interest(y, "Low") ==> RecommendField(x, Me)'))

