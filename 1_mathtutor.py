from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']



## Reference : https://platform.openai.com/docs/assistants/overview?context=without-streaming, 
from openai import OpenAI
client = OpenAI(api_key=API_KEY)


# # Step 1: Create an Assistant
# assistant = client.beta.assistants.create(
#   name="Math Tutor-2",
#   instructions="You are a personal math tutor. Write and run code to answer math questions.",
#   tools=[{"type": "code_interpreter"}],
#   model="gpt-4-turbo-preview",
# )
# # to confirm assistant_id ( asst_Ia1SmRObwI7ppyApejbfpT1Q )
# print(assistant)

# # Step 2: Create a Thread
# thread = client.beta.threads.create()
# # to confirm thread_id ( thread_QzmRLgoQrVpWyxPGV5CTBjDP )
# print(thread)


# Step 3: Add a Message to the Thread
# message = client.beta.threads.messages.create(
#     #thread_id=thread.id,
#     thread_id="thread_QzmRLgoQrVpWyxPGV5CTBjDP",
#     role="user",
#     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )

# print(message)

# run = client.beta.threads.runs.create(
#   # thread_id=thread.id,
#   # assistant_id=assistant.id,
#   thread_id="thread_QzmRLgoQrVpWyxPGV5CTBjDP",
#   assistant_id="asst_Ia1SmRObwI7ppyApejbfpT1Q",
#   instructions="Please address the user as Jane Doe. The user has a premium account."
# )
# print(run)


# import time
# time.sleep(30)
messages = client.beta.threads.messages.list(
    # thread_id=thread.id
    thread_id="thread_QzmRLgoQrVpWyxPGV5CTBjDP"
  )
# print(messages)

# https://platform.openai.com/docs/api-reference/messages/listMessages
print (messages.data[0].content[0].text.value)

