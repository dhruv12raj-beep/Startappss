## **Project Synopsis** 

## **Project Title** 

Interview Question Bank Manager with Secure User Authentication 

## **Project Description** 

The Interview Question Bank Manager is a console-based, menu-driven Python application designed to manage technical interview questions efficiently. The system provides secure user authentication using hashed passwords and Role-Based Access Control (Admin/User). The application follows OOP principles and stores all data in CSV files. Administrators can perform CRUD operations on interview questions, while users can view, search, filter, and count questions. The project also implements input validation and exception handling. 

## **Objectives** 

- Develop a menu-driven interview question management system. 

- Implement OOP concepts. 

- Use CSV files for data storage. 

- Implement secure authentication using hashed passwords. 

- Implement Role-Based Access Control (Admin/User). 

- Perform CRUD operations. 

- Validate user input and handle exceptions. 

## **Technologies Used** 

- Python 

- OOP 

- CSV File Handling 

- Exception Handling 

- hashlib (Password Hashing) 

## **Modules** 

- Authentication: Registration, Login, Password Hashing, Role-Based Access. 

- Question Management: Add (Admin), View, Search, Update (Admin), Delete (Admin), Count, Filter. 

- Validation & Exception Handling. 

## **User Roles** 

- Admin: Add, View, Search, Update, Delete, Count and Filter. 

- User: View, Search, Count and Filter. 

## **Data Storage** 

- users.csv: User ID, Username, Password Hash, Role. 

- questions.csv: Question ID, Technology, Category, Difficulty, Question, Answer. 

## **OOP Concepts Used** 

- Classes and Objects 

- Constructors 

- Encapsulation 

- Methods 

- File Handling 

- Exception Handling 

## **ER Diagram** 

+----+ |User| +---------+
 | User_ID (PK)         |
  | Username             | 
  | Password_Hash        | 
  | Role                 | 

+----------------------+ 

Logs In |
        v

+------------------------------+ 

| Interview Question Manager   | 

| Admin Manages Questions | 

|     InterviewQuestion          | 

| Question_ID (PK)               | 

| Technology                     | 
| Category                       |
| Difficulty                     | 
| Question                       | 
| Answer                         |

 +--------------------------------+ 

Note: Authentication controls access to the application. Interview questions are stored independently in questions.csv. 

## **Expected Outcome** 

The project will provide a secure and user-friendly console application for managing interview questions. It demonstrates Python OOP, CSV file handling, authentication with hashed passwords, role-based access control, input validation, and exception handling while fulfilling the assignment requirements. 

