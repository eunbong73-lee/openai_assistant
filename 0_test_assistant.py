import os
from openai import OpenAI


from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=API_KEY)



# # File Upload 
# # file.id : file-aJ0E6Aeg8DzJhJW933eolr5f
# file = client.files.create(
#   file=open("unsu.pdf", "rb"),
#   purpose="assistants"
# )
# print(file)


# Step 1: Create an Assistant
assistant = client.beta.assistants.create(
  name="현진건 작가님",
  instructions="당신은 소설 운수 좋은 날을 집필한 현진건 작가님입니다.",
  tools=[{"type": "retrieval"}],
  model="gpt-4-turbo-2024-04-09",
  file_ids=["file-aJ0E6Aeg8DzJhJW933eolr5f"]
)
# to confirm assistant_id ( asst_1Uk251mYQHVI4XvkC8XvFxsC )
print(assistant)

# # Step 2: Create a Thread
# thread = client.beta.threads.create()
# # to confirm thread_id ( thread_nMvepvqfPo90Jkbdg34Fpcex )
# print(thread)


# # Step 3: Add a Message to the Thread
# message = client.beta.threads.messages.create(
#     thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex",
#     role="user",
#     content="아내가 먹고 싶어 한 음식이 뭐야?"
# )
# print(message)

# run = client.beta.threads.runs.create(
#   # thread_id=thread.id,
#   # assistant_id=assistant.id,
#   thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex",
#   assistant_id="asst_1Uk251mYQHVI4XvkC8XvFxsC",
# )
# # run.id : run_WhRo6DVD8ryyBSt9YbxpSeuQ
# print(run)

# # confirm response's complete
# run = client.beta.threads.runs.retrieve(
#     thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex",
#     run_id="run_WhRo6DVD8ryyBSt9YbxpSeuQ"
# )
# print(run)

# messages = client.beta.threads.messages.list(
#     thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex"
#   )

# # https://platform.openai.com/docs/api-reference/messages/listMessages
# print (messages.data[0].content[0].text.value)



# #------------------------
# # Step 3: 추가 질문해보기...
# message = client.beta.threads.messages.create(
#     thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex",
#     role="user",
#     content="주제를 1000자 내외로 정리해줘"
# )
# print(message)

# run = client.beta.threads.runs.create(
#   # thread_id=thread.id,
#   # assistant_id=assistant.id,
#   thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex",
#   assistant_id="asst_1Uk251mYQHVI4XvkC8XvFxsC",
# )
# print(run)


# messages = client.beta.threads.messages.list(
#     thread_id="thread_nMvepvqfPo90Jkbdg34Fpcex"
#   )
# print (messages.data[0].content[0].text.value)
