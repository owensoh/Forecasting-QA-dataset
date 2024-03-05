from openai import OpenAI
import os

QUESTION_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/3.5/bin_formatted/04/5-bin-question.txt"
ANSWER_PATH = "C:/Users/user/Documents/FYP/OpenAI/answers/Chain of Thought/3.5/bin/04/5-bin-answer.txt"


API_KEY = open("API_KEY.txt", "r").read()
client = OpenAI(
    api_key = API_KEY
)

prompt = open("COT_prompt.txt", "r").read()

with open(QUESTION_PATH) as f:
        user_query = f.read()

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "You are an assistant and your task is to answer the given forecasting question, selecting the answer with the highest probability of occuring based on a given storyline. You are to use chain of thought reasoning, explaining how you evenutally get to the answer. Your task flow is based on the following rules:"},
        {"role": "assistant", "content": prompt},
        {"role": "user", "content": "Complete the task with the storyline, question and options: " + user_query}
    ]
)

answer = response.choices[0].message.content
with open(ANSWER_PATH, 'w') as f:
    f.write(answer)


'''
#Change this
folder_path = '01/'
gpt = '4/'

MCQ_QUESTION_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/" + gpt + "mcq_formatted/" + folder_path
BIN_QUESTION_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/" + gpt + "bin_formatted/" + folder_path
MCQ_ANSWER_PATH = "C:/Users/user/Documents/FYP/OpenAI/answers/Chain of Thought/" + gpt + "mcq/" + folder_path
BIN_ANSWER_PATH = "C:/Users/user/Documents/FYP/OpenAI/answers/Chain of Thought/" + gpt + "bin/" + folder_path

## Create directory if does not exist
if not os.path.exists(MCQ_ANSWER_PATH):
    os.makedirs(MCQ_ANSWER_PATH)
if not os.path.exists(BIN_ANSWER_PATH):
    os.makedirs(BIN_ANSWER_PATH)

mcq_file_list = os.listdir(MCQ_QUESTION_PATH)
bin_file_list = os.listdir(BIN_QUESTION_PATH)

API_KEY = open("API_KEY.txt", "r").read()
client = OpenAI(
    api_key = API_KEY
)

prompt = open("COT_prompt.txt", "r").read()

## Go through MCQ questions
mcq_counter = 1
for mcq_question in mcq_file_list:
    with open(MCQ_QUESTION_PATH + mcq_question) as f:
        user_query = f.read()

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an assistant and your task is to answer the given forecasting question, selecting the answer with the highest probability of occuring based on a given storyline. You are to use chain of thought reasoning, explaining how you evenutally get to the answer. Your task flow is based on the following rules:"},
            {"role": "assistant", "content": prompt},
            {"role": "user", "content": "Complete the task with the storyline, question and options: " + user_query}
        ]
    )

    answer = response.choices[0].message.content
    with open(MCQ_ANSWER_PATH + str(mcq_counter) + '-mcq-answer.txt', 'w') as f:
        f.write(answer)
    mcq_counter += 1

## Go through BIN questions
bin_counter = 1
for bin_question in bin_file_list:
    with open(BIN_QUESTION_PATH + bin_question) as f:
        user_query = f.read()

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an assistant and your task is to answer the given forecasting question, selecting the answer with the highest probability of occuring based on a given storyline. You are to use chain of thought reasoning, explaining how you evenutally get to the answer. Your task flow is based on the following rules:"},
            {"role": "assistant", "content": prompt},
            {"role": "user", "content": "Complete the task with the storyline, question and options: " + user_query}
        ]
    )

    answer = response.choices[0].message.content
    with open(BIN_ANSWER_PATH + str(bin_counter) + '-bin-answer.txt', 'w') as f:
        f.write(answer)
    bin_counter += 1
    '''