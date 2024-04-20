from aima3.logic import *
from knowledge_base import kb

def suggest_fields(preferences):

    # Add user preferences to the knowledge base
    for preference, value in preferences.items():
        if value != "None":
            kb.tell(expr(f'{preference}(Me, "{value}")'))

    # Print out the contents of the KB

    recommendations = []

    # Retrieve recommended fields based on preferences and constraints
    for field in fol_fc_ask(kb, expr('RecommendField(x, Me)')):
        recommendations.append(field.bindings[0][x])
        print("Recommendation:", field.bindings[0][x])

    return recommendations
