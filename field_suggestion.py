from aima3.logic import *
from knowledge_base import kb
from utils import *

def suggest_fields():
    # Retrieve student preferences and constraints
    preferences = list(fol_fc_ask(kb, expr('PreferField(Me, x)')))
    if not preferences:
        print("No preferences specified.")
        return []

    # Retrieve recommended fields based on preferences and constraints
    recommended_fields = []
    for preference in preferences:
        field = preference[x]
        recommendations = list(fol_fc_ask(kb, expr(f'RecommendField({field}, Me)')))
        recommended_fields.extend([recommendation[x] for recommendation in recommendations])

    return recommended_fields

if __name__ == "__main__":
    # Get recommended fields based on student preferences and constraints
    recommended_fields = suggest_fields()

    # Print recommended fields
    print("Recommended Fields:")
    for field in recommended_fields:
        print("-", field)
