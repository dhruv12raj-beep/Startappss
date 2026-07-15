from auth import AuthenticationManager
from manager import QuestionManager


def display_questions(questions):

    if not questions:
        print("\nNo Questions Found.")
        return

    print("\n" + "=" * 70)

    for question in questions:

        print(f"Question ID : {question[0]}")
        print(f"Question    : {question[1]}")
        print(f"Answer      : {question[2]}")
        print(f"Category    : {question[3]}")
        print(f"Difficulty  : {question[4]}")
        print("-" * 70)


def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Search Question")
        print("4. Update Question")
        print("5. Delete Question")
        print("6. Logout")

        choice = input("Enter Choice : ")

        try:

            if choice == "1":

                question = input("Enter Question : ")
                answer = input("Enter Answer : ")
                category = input("Enter Category : ")
                difficulty = input("Enter Difficulty (Easy/Medium/Hard): ")

                QuestionManager.add_question(
                    question,
                    answer,
                    category,
                    difficulty
                )

                print("\nQuestion Added Successfully.")

            elif choice == "2":

                questions = QuestionManager.view_questions()
                display_questions(questions)

            elif choice == "3":

                keyword = input("Enter Keyword : ")

                questions = QuestionManager.search_question(keyword)
                display_questions(questions)

            elif choice == "4":

                question_id = input("Question ID : ")
                question = input("New Question : ")
                answer = input("New Answer : ")
                category = input("New Category : ")
                difficulty = input("New Difficulty : ")

                QuestionManager.update_question(
                    question_id,
                    question,
                    answer,
                    category,
                    difficulty
                )

                print("\nQuestion Updated Successfully.")

            elif choice == "5":

                question_id = input("Question ID : ")

                confirm = input(
                    "Are you sure you want to delete? (Y/N): "
                )

                if confirm.lower() == "y":
                    QuestionManager.delete_question(question_id)
                    print("\nQuestion Deleted Successfully.")

            elif choice == "6":

                print("\nLogged Out Successfully.")
                break

            else:

                print("Invalid Choice.")

        except Exception as e:

            print(e)


def user_menu():

    while True:

        print("\n========== USER MENU ==========")
        print("1. View Questions")
        print("2. Search Question")
        print("3. Logout")

        choice = input("Enter Choice : ")

        try:

            if choice == "1":

                questions = QuestionManager.view_questions()
                display_questions(questions)

            elif choice == "2":

                keyword = input("Enter Keyword : ")

                questions = QuestionManager.search_question(keyword)
                display_questions(questions)

            elif choice == "3":

                print("\nLogged Out Successfully.")
                break

            else:

                print("Invalid Choice.")

        except Exception as e:

            print(e)


def main():

    while True:

        print("\n========== Interview Question Bank Manager ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter Choice : ")

        try:

            if choice == "1":

                username = input("Username : ").strip().lower()
                password = input("Password : ")

                role = input(
                    "Role (Admin/User) [Default User] : "
                ).strip().capitalize()

                if role == "":
                    role = "User"

                if role not in ["Admin", "User"]:
                    role = "User"

                AuthenticationManager.register(
                    username,
                    password,
                    role
                )

                print("\nRegistration Successful.")

            elif choice == "2":

                username = input("Username : ").strip().lower()
                password = input("Password : ")

                logged_in_user = AuthenticationManager.login(
                    username,
                    password
                )

                print(
                    f"\nWelcome {logged_in_user.username} ({logged_in_user.role})"
                )

                if logged_in_user.role.lower() == "admin":

                    admin_menu()

                else:

                    user_menu()

            elif choice == "3":

                print("\nThank You.")
                break

            else:

                print("Invalid Choice.")

        except Exception as e:

            print(e)


if __name__ == "__main__":
    main()