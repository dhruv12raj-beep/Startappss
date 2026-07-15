
from file_handler import CSVFileManager
from models import InterviewQuestions
from logger import logger
from exceptions import QuestionNotFoundError


class QuestionManager:

    FILE_NAME = "questions.csv"

    @staticmethod
    def _generate_question_id():
        questions = CSVFileManager.read_csv(QuestionManager.FILE_NAME)

        if not questions:
            return 1

        last_id = int(questions[-1][0])
        return last_id + 1

    @staticmethod
    def add_question(question, answer, category, difficulty):

        question_id = QuestionManager._generate_question_id()

        new_question = InterviewQuestions(
            question_id,
            question,
            answer,
            category.upper(),
            difficulty.upper()
        )

        CSVFileManager.append_csv(
            QuestionManager.FILE_NAME,
            new_question.to_list()
        )

        logger.info(f"Question Added : {question}")

        return True

    @staticmethod
    def view_questions():

        return CSVFileManager.read_csv(
            QuestionManager.FILE_NAME
        )

    @staticmethod
    def search_question(keyword):

        questions = CSVFileManager.read_csv(
            QuestionManager.FILE_NAME
        )

        result = []

        keyword = keyword.lower()

        for question in questions:

            if (
                keyword in question[1].lower()      # Question
                or keyword in question[2].lower()   # Answer
                or keyword in question[3].lower()   # Category
                or keyword in question[4].lower()   # Difficulty
            ):

                result.append(question)

        return result

    @staticmethod
    def update_question(question_id,
                        new_question,
                        new_answer,
                        new_category,
                        new_difficulty):

        questions = CSVFileManager.read_csv(
            QuestionManager.FILE_NAME
        )

        updated = False

        for question in questions:

            if question[0] == str(question_id):

                question[1] = new_question
                question[2] = new_answer
                question[3] = new_category.upper()
                question[4] = new_difficulty.upper()

                updated = True
                break

        if not updated:
            raise QuestionNotFoundError(
                "Question ID not found."
            )

        CSVFileManager.write_csv(
            QuestionManager.FILE_NAME,
            questions
        )

        logger.info(f"Question Updated : {question_id}")

        return True

    @staticmethod
    def delete_question(question_id):

        questions = CSVFileManager.read_csv(
            QuestionManager.FILE_NAME
        )

        new_questions = []

        deleted = False

        for question in questions:

            if question[0] == str(question_id):

                deleted = True
                continue

            new_questions.append(question)

        if not deleted:
            raise QuestionNotFoundError(
                "Question ID not found."
            )

        CSVFileManager.write_csv(
            QuestionManager.FILE_NAME,
            new_questions
        )

        logger.info(f"Question Deleted : {question_id}")

        return True