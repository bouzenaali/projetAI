from aima3.logic import *
from knowledge_base import kb, fields

def suggest_fields(preferences):
    """
    Suggest fields of study based on the given user preferences.
    
    Args:
        preferences (dict): A dictionary containing the user's preferences.
            The keys should be the question names (e.g., "PreferredField",
            "PreferredJobProspects", "PreferredHighSchool", "PreferredType")
            and the values should be the selected options.
    
    Returns:
        list: A list of recommended fields of study.
    """
    recommended_fields = []

    # Add the user's preferences to the knowledge base
    for question, option in preferences.items():
        kb.tell(expr(f'{question}(Me, "{option}")'))

    # Query the knowledge base for recommended fields
    for field in fields:
        if kb.ask(expr(f'RecommendField("{field["name"]}", Me)')):
            recommended_fields.append(field["name"])

    # Remove the user's preferences from the knowledge base
    for question, option in preferences.items():
        kb.retract(expr(f'{question}(Me, "{option}")'))

    return recommended_fields