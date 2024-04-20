import streamlit as st
from field_suggestion import suggest_fields

def get_recommendations(preferences):
    recommended_fields = suggest_fields(preferences)
    if not recommended_fields:
        st.info("No recommendations found based on specified preferences.")
    else:
        st.success("Recommended Fields:")
        for field in recommended_fields:
            st.write("-", field)

def main():
    st.title("kheyer specialite Expert System")

    # Questions with predefined answers
    answers = {
        "PreferredField": ["None", "Computer Science", "Mechanical Engineering", "Psychology", "Economics", "Art History", "Biology", "History", "Physics", "Political Science", "Mathematics", "Chemistry", "Philosophy", "Sociology", "Anthropology", "Geology", "Linguistics", "Astronomy"],
        "PreferredJobProspects": ["None", "High", "Medium", "Low"],
        "PreferredHighSchool": ["Scientific", "Literary"],
        "PreferredType": ["None", "Science", "Engineering", "Social Science", "Humanities"]
    }

    questions = {
        "PreferredField": "What field of study are you interested in?",
        "PreferredJobProspects": "What level of job prospects are you looking for?",
        "PreferredHighSchool": "What type of high school did you attend?",
        "PreferredType": "What type of field are you interested in?"
    }

    preferences = {}

    # Ask questions and get answers
    for answer, question_text in questions.items():
        preferences[answer] = st.selectbox(question_text, answers[answer])

    # Button to get recommendations
    if st.button("Get Recommendations"):
        get_recommendations(preferences)

if __name__ == "__main__":
    main()
