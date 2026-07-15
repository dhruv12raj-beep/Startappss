import hashlib

from file_handler import CSVFileManager
from models import User
from exceptions import (
    UsernameAlreadyExists,
    InvalidCredentialsError,
)


class AuthenticationManager:

    FILE_NAME = "users.csv"

    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @staticmethod
    def _verify_password(password, stored_hash):
        return (
            AuthenticationManager._hash_password(password)
            == stored_hash
        )

    @staticmethod
    def _username_exists(username):

        users = CSVFileManager.read_csv(AuthenticationManager.FILE_NAME)

        for user in users:
            if user[1] == username:
                return True

        return False

    @staticmethod
    def _generate_user_id():

        users = CSVFileManager.read_csv(AuthenticationManager.FILE_NAME)

        if not users:
            return 1

        return int(users[-1][0]) + 1

    @staticmethod
    def register(username, password, role="User"):

        if AuthenticationManager._username_exists(username):
            raise UsernameAlreadyExists("Username already exists.")

        user = User(
            AuthenticationManager._generate_user_id(),
            username,
            AuthenticationManager._hash_password(password),
            role
        )

        CSVFileManager.append_csv(
            AuthenticationManager.FILE_NAME,
            user.to_list()
        )

        return user

    @staticmethod
    def login(username, password):

        users = CSVFileManager.read_csv(AuthenticationManager.FILE_NAME)

        for user in users:

            if user[1] == username:

                if AuthenticationManager._verify_password(
                    password,
                    user[2]
                ):
                    return User(
                        int(user[0]),
                        user[1],
                        user[2],
                        user[3]
                    )

                raise InvalidCredentialsError(
                    "Incorrect password."
                )

        raise InvalidCredentialsError(
            "Username not found."
        )