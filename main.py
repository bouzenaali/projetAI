from aima3.logic import *
from knowledge_base import kb
from field_suggestion import suggest_fields

if __name__ == "__main__":
    # Initialize knowledge base with student's information
    kb.tell(expr('Student(Me)'))
    kb.tell(expr('PreferredField(Me, "Computer Science")'))  # Example preferred field of study
    kb.tell(expr('PreferredJobProspects(Me, "High")'))  # Example preferred job prospects
    kb.tell(expr('PreferredHighSchool(Me, "Scientific")'))  # Example preferred high school association

    # Get recommended fields based on student preferences and constraints
    recommended_fields = suggest_fields()

    # Print recommended fields
    print("Recommended Fields:")
    for field in recommended_fields:
        print("-", field)
