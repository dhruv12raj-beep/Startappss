

class User:

    def __init__(self, user_id, username, password_hash, role="User"):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def to_list(self):
        return [
            self.user_id,
            self.username,
            self.password_hash,
            self.role
        ]

    def __str__(self):
        return (
            f"User(ID={self.user_id}, "
            f"Username={self.username}, "
            f"Role={self.role})"
        )


    
class InterviewQuestions:

    def __init__(self, question_id, question, answer, category, difficulty):
        self.question_id = question_id
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def to_list(self):
        return [
            self.question_id,
            self.question,
            self.answer,
            self.category,
            self.difficulty
    ]

    def __str__(self):
        return (
            f"{self.question_id} | "
            f"{self.question} | "
            f"{self.category} | "
            f"{self.difficulty}"
        )