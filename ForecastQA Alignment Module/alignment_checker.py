from openai import OpenAI
import os

# Change this
folder_path = "05/"
openai_model = "3.5/"

MCQ_SAVE_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/" + openai_model + "mcq/" + folder_path
BIN_SAVE_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/" + openai_model + "bin/" + folder_path
DOC_PATH = "C:/Users/user/Documents/FYP/OpenAI/result_temp/result_temp/"

API_KEY = open("API_KEY.txt", "r").read()
client = OpenAI(
    api_key = API_KEY
)

mcq_alignment_prompt = open("mcq_alignment_prompt.txt", "r").read()
bin_alignment_prompt = open("bin_alignment_prompt.txt", "r").read()

# Change this
user_query = open(DOC_PATH + folder_path + "Rewrite_BRONZE PRESIDENT Targets Government Officials _ Secureworks.txt", "r").read()

mcq_file_list = os.listdir(MCQ_SAVE_PATH)
bin_file_list = os.listdir(BIN_SAVE_PATH)

## For MCQ
faithfulness_string = ""
for file in (mcq_file_list):
    if "question" in file:
        with open(MCQ_SAVE_PATH + file) as f:
            text = f.read().split('\n')
        ## Parsing the triplet
        triplet = ['','','']
        for string in text:
            if "Question:" in string:
                triplet[0] = string
            elif "Tag:" in string:
                triplet[1] = string
            elif "Option 1:" in string:
                triplet[2] = string


        ## Alignment checker with GPT 4
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are an assistant and your task is to create verify if the question, tag, answer triplet given to you is faithful to the article as given. Your task flow is based on the following rules:"},
                {"role": "assistant", "content": mcq_alignment_prompt},
                {"role": "user", "content": "Complete the task with the article: " + user_query},
                {"role": "user", "content": "Complete the task with the triplet: " + str(triplet)}
            ]
        )
        answer = response.choices[0].message.content
        faithfulness_string += answer + '\n'

with open(MCQ_SAVE_PATH + 'faithfulness.txt', 'w') as f:
    f.write(faithfulness_string)

## For BIN
faithfulness_string = ""
for file in (bin_file_list):
    if "question" in file:
        with open(BIN_SAVE_PATH + file) as f:
            text = f.read().split('\n')
        ## Parsing the triplet
        triplet = ['','','']
        for string in text:
            if "Question:" in string:
                triplet[0] = string
            elif "Tag:" in string:
                triplet[1] = string
            elif "Answer:" in string:
                triplet[2] = string


        ## Alignment checker with GPT 4
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are an assistant and your task is to create verify if the question, tag, answer triplet given to you is faithful to the article as given. Your task flow is based on the following rules:"},
                {"role": "assistant", "content": bin_alignment_prompt},
                {"role": "user", "content": "Complete the task with the article: " + user_query},
                {"role": "user", "content": "Complete the task with the triplet: " + str(triplet)}
            ]
        )
        answer = response.choices[0].message.content
        faithfulness_string += answer + '\n'

with open(BIN_SAVE_PATH + 'faithfulness.txt', 'w') as f:
    f.write(faithfulness_string)
