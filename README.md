## Singh, Bhanu Pratap  22201990

## Galani, Rohit   22209032

**Student Advisor Rasa ChatBot**

[Link to MyGit repository](https://mygit.th-deg.de/rg11032/rasa-chatbot.git)

[Link to Wiki repository in MyGit](https://mygit.th-deg.de/rg11032/rasa-chatbot/-/wikis/home)

# Project Description

The "Student Advisor Rasa ChatBot" is a project designed to enhance the user experience for future and existing students at the Deggendorf Institute of Technology (DIT) by providing real-time assistance and information through a conversational chatbot. The chatbot is aimed at assisting users in their inquiries related to study options, application procedures, enrollment processes, language requirements, deadlines, and other relevant information.

# Installation

## Prerequisites
Python - - version 3.9.7

Rasa -- version 3.6.16

Flask -- 3.0.1

## Installing the project
To run this chatbot properly, follow the given steps : 
- Download or clone this repository:
```
git clone https://mygit.th-deg.de/rg11032/rasa-chatbot.git
```
- Now, you must open this porject in a virtual python environment using venv module 
```
cd rasa-chatbot-main 
pip install virtualenv
```
- Create a new virtual environment (Python 3.9.7) in the working directory and activate it
```
python -m venv env

.\env\Scripts\activate.bat (on windows)
```
- Then, you have to install rasa and flask modules
```
pip install rasa, flask
```
# Basic Usage

- Next step is to train the rasa model 
```
rasa train
```
- To get appropriate responses, open a new terminal and run actions.py file on port 5055
```
rasa run actions
```
- To run the API file, run the following commands:
```
cd actions
set FLASK_APP=app.py 
set FLASK_ENV=development
flask run 
```
- Open the terminal where you trained the model and run the following command to start conversing with the chatbot
```
rasa shell
```

Note : Make sure that the action server is running on correct port. If you face any issues, try the following steps :


1.  Go to endpoints.yml, and change the action_endpoint url from 5055 to 5005
2.  Now, to start the chatbot, enter the following command: 
    ```
    rasa shell --port 5055
    ```
## Key Use Cases : 

- Study Options Inquiry
- Enrollment Process Information
- Language Requirements Query
- Internship Opportunities Exploration
- Application Procedure Information
- Deadline Query
- Contacting the University
- Looking for advice and support
- Beginning dates

# Implementation of the Requests

This Rasa chatbot project comprises a **Flask API** (`app.py`) providing study fields, with custom **actions** (`actions.py`),which fetch and format the data. NLU training data (`data/nlu.yml`) covers diverse intents, while stories (`data/stories.yml`) define conversational flows. The domain file (`domain.yml`) specifies entities, intents, actions, and responses. Rules (`data/rules.yml`) provide specific responses based on conditions. Utterances in the domain file offer predefined responses. The `endpoints.yml` file configures connections between components.

The chatbot processes user messages through Rasa NLU, determines actions via Rasa Core using stories and rules, and executes custom actions as needed.

# Work done

## Bhanu Pratap Singh : (22201990)

1) User and System Personas 
2) Example dialogs
3) Implementation yml-files (domain, data/nlu)
4) Implementation actions.py

## Rohit Galani : (22209032)

1) Use cases 
2) Dialog flow
3) Implementation yml-files (data/stories data/rules)
4) Implementation actions.py
