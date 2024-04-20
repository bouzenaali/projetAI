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
    questions = {
        "PreferredField": ["None", "Computer Science", "Mechanical Engineering", "Psychology", "Economics", "Art History", "Biology", "History", "Physics", "Political Science", "Mathematics", "Chemistry", "Philosophy", "Sociology", "Anthropology", "Geology", "Linguistics", "Astronomy"],
        "PreferredJobProspects": ["None", "High", "Medium", "Low"],
        "PreferredHighSchool": ["Scientific", "Literary"],
        "PreferredType": ["None", "Science", "Engineering", "Social Science", "Humanities"]
    }

    preferences = {}

    # Ask questions and get answers
    for question, options in questions.items():
        preferences[question] = st.selectbox(question, options)

    # Button to get recommendations
    if st.button("Get Recommendations"):
        get_recommendations(preferences)

if __name__ == "__main__":
    main()
