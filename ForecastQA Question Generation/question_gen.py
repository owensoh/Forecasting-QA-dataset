from openai import OpenAI
import os

# Change this
folder_path = "01/"
openai_model = "3.5/"

TAGS = ["Reconnaissance","Initial Access","Execution","Persistence","Privilege Escalation","Defense Evasion","Credential Access","Discovery","Lateral Movement","Collection","Command and Control","Exfiltration","Impact","Others"]
final_tag_lst = []

MCQ_SAVE_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/" + openai_model + "mcq/" + folder_path
BIN_SAVE_PATH = "C:/Users/user/Documents/FYP/OpenAI/questions/" + openai_model + "bin/" + folder_path
DOC_PATH = "C:/Users/user/Documents/FYP/OpenAI/result_temp/result_temp/"

## Create directory if does not exist
if not os.path.exists(MCQ_SAVE_PATH):
    os.makedirs(MCQ_SAVE_PATH)

if not os.path.exists(BIN_SAVE_PATH):
    os.makedirs(BIN_SAVE_PATH)

API_KEY = open("API_KEY.txt", "r").read()
client = OpenAI(
    api_key = API_KEY
)

mcq_prompt = open("MCQ_prompt.txt", "r").read()
bin_prompt = open("BIN_prompt.txt", "r").read()

# Change this
user_query = open(DOC_PATH + folder_path + "Rewrite_Antlion_ Chinese APT Uses Custom Backdoor to Target Financial Institutions in Taiwan _ Symantec Blogs.txt", "r").read()

## Process tags to generate questions
lst = user_query.split(',\n')
for i in lst:
    string = i.split(':')
    if string[1] != ' "None"':
        final_tag_lst.append(string[0][3:-1])

for i in range(1, len(final_tag_lst)):
    print(final_tag_lst[i])
    
    ## MCQ question generation
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        # model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an assistant and your task is to create a forecasting question with the tag" + final_tag_lst[i] + ", given the summary of a cyber incident, and 4 options, where 1 answer is correct and the other 3 are wrong. Provide the section that the question is based on as well. Your task flow is based on the following rules:"},
            {"role": "assistant", "content": mcq_prompt},
            {"role": "user", "content": "Complete the task with the article: " + user_query}
        ]
    )

    answer = response.choices[0].message.content
    with open(MCQ_SAVE_PATH + str(i) + '-mcq-question.txt', 'w') as f:
        f.write(answer)

    ## Binary question generation
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        # model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an assistant and your task is to create a forecasting question with the tag" + final_tag_lst[i] + ", given the summary of a cyber incident, and 2 options, where 1 answer is yes and the other is no. Provide the section that the question is based on as well. Your task flow is based on the following rules:"},
            {"role": "assistant", "content": bin_prompt},
            {"role": "user", "content": "Complete the task with the article: " + user_query}
        ]
    )

    answer = response.choices[0].message.content
    with open(BIN_SAVE_PATH + str(i) + '-bin-question.txt', 'w') as f:
        f.write(answer)