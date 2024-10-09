# Project Title

**Depression-Detection-System-DEPSIGN**

## Description

A web application built using Django and Python for assessing depression levels in users through a series of questions and providing recommendations. This system also aims to expand into assessing other mental health conditions like anxiety and addiction through quiz-based tests.

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Future Enhancements](#Future-Enhancements)


## Features

- User authentication and login system.
- Depression assessment quiz with SVM-based prediction.
- Classification of depression levels (severe, mild, none) based on user responses.
- Recommendations and precautions based on the assessment result.
- Planned integration of quizzes for anxiety, addiction, and other mental health conditions.
- Future expansion to include tests for anxiety, addiction, and other mental health conditions.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Deepak-Dhanoliya/Depression-Detection-System-DEPSIGN.git
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install project dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Migrate the database:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the Django development server:
   ```
   python manage.py runserver
   ```
6. Access the application in your web browser at http://localhost:8000/.

## Usage

* Register or log in to your account.
* Take the depression assessment quiz by answering the questions honestly.
* Receive your depression assessment result and follow the provided recommendations and precautions.

## Future Enhancements

* Add anxiety assessment quiz.
* Incorporate addiction assessment.
* Expand the application to provide a comprehensive mental health assessment through various quizzes.
* Improve the accuracy and depth of the quiz-based assessments.







