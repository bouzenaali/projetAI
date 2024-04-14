class UserInterface:
    def display_welcome_message(self):
        print("Welcome to the Educational Guidance Expert System!")
        print("Please enter the subjects you excel in, love, or hate (separated by commas).")
        print("For example: 'Mathematics, Literature, Biology'")
        print("You can also specify your preferences like 'loves Mathematics, hates Physics'")
        print("Type 'exit' to quit.")

    def prompt_user_input(self):
        while True:
            user_input = input("Your input: ").strip()
            if user_input.lower() == 'exit':
                return 'exit'
            elif user_input:
                return user_input
            else:
                print("Invalid input. Please try again.")

    def get_preferences(self, user_input):
        loves = []
        hates = []

        # Parse user input to extract loves and hates
        for part in user_input.split(','):
            part = part.strip().lower()
            if 'loves' in part:
                loves.append(part.split('loves')[1].strip())
            elif 'hates' in part:
                hates.append(part.split('hates')[1].strip())

        return loves, hates

    def display_recommendations(self, recommendations):
        if recommendations:
            print("\nRecommended academic programs:")
            for program in recommendations:
                print("-", program)
        else:
            print("\nNo recommendations found.")
