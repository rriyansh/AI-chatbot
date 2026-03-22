# AI Chatbot (Rule-Based)

This project is a simple AI chatbot built using Python.
I created this project to understand how basic chatbots work and how user input can be processed and matched with predefined responses using simple Natural Language Processing concepts.<br><br>

The chatbot reads user messages, cleans the text, and searches for matching patterns stored in a JSON file.
If a match is found, the chatbot returns a response from the available list.
The code is written in a modular way using functions so that it is easy to understand and maintain.

---

## Features

Responds to user messages using pattern matching<br>
Uses a separate JSON file as a knowledge base<br>
Randomly selects responses to make conversations less repetitive<br>
Clean and modular function-based structure<br>
Easy to extend with new intents and responses

---

## Concepts Used

Basic Natural Language Processing (NLP)<br>
Pattern matching<br>
JSON data handling<br>
String preprocessing<br>
Function-based programming design

---

## Tech Stack

Python 3<br>
JSON<br>
Standard Python libraries

---

## Project Structure

ai-chatbot<br>
│<br>
├── chatbot.py<br>
├── intents.json<br>
├── requirements.txt<br>
└── README.md

---

## How to Run

1. Clone the repository<br>

git clone https://github.com/your-username/ai-chatbot.git

2. Navigate to the project folder<br>

cd ai-chatbot

3. Run the chatbot<br>

python chatbot.py

---

## Functions Explained

load_intents(file_path)<br>
This function loads the chatbot knowledge base from the JSON file.
It reads the file and returns the data so that the chatbot can use it during conversation.<br><br>

clean_text(text)<br>
This function processes the user input by converting it to lowercase and removing punctuation.
Cleaning the text helps improve matching accuracy between user input and stored patterns.<br><br>

find_response(user_input, intents)<br>
This function searches for a matching pattern inside the intents data.
If a matching pattern is found, it randomly selects a response from the available responses list.<br>
If no match is found, it returns a default message.<br><br>

chatbot()<br>
This is the main function that runs the chatbot loop.
It continuously accepts user input, checks for the exit condition, and prints the chatbot response.

---

## Example Conversation

You: hello<br>
Bot: Hello! How can I help you?<br><br>

You: what is your name<br>
Bot: I am an AI chatbot created using Python.<br><br>

You: bye<br>
Bot: Goodbye.

---

## How the System Works

The chatbot follows a simple workflow:<br><br>

User enters a message<br>
The message is cleaned using the clean_text function<br>
The program searches for matching patterns in the intents data<br>
If a match is found, a response is selected randomly<br>
The response is displayed to the user

---

## Why I Built This Project

I built this project to practice Python programming and understand the fundamentals of chatbot development.
It helped me learn how to structure code using functions, work with JSON files, and implement simple Natural Language Processing logic.

---

## Possible Future Improvements

Add machine learning based response prediction<br>
Add conversation context handling<br>
Create a graphical user interface<br>
Deploy the chatbot as a web application<br>
Improve response matching using NLP libraries
