import os
from openai import OpenAI


from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']
assistant_id = os.environ['assistant_id']
client = OpenAI(api_key=API_KEY)


import streamlit as st
# thread id를 하나로 관리하기 위함
if 'thread_id' not in st.session_state:
  thread = client.beta.threads.create()
  st.session_state.thread_id = thread.id

thread_id = st.session_state.thread_id
thread_messages = client.beta.threads.messages.list(thread_id)

st.header("현진건 작가님과의 대화")
for msg in reversed(thread_messages.data):
  with st.chat_message(msg.role): # ref : https://docs.streamlit.io/develop/api-reference/chat/st.chat_message
    st.write( msg.content[0].text.value)

# ref : https://docs.streamlit.io/develop/api-reference/chat/st.chat_input
prompt = st.chat_input("물어보고 싶은 것을 입력하세요.")
if prompt:
  message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=prompt)
  
  with st.chat_message(message.role): 
    st.write( message.content[0].text.value)
  
  run = client.beta.threads.runs.create(
      thread_id=thread_id,
      assistant_id=assistant_id
   )
  

  with st.spinner('응답 기다리는 중'):
    while run.status != "completed":
      import time
      time.sleep(1)
      # print("status 확인 중", run.status)
      run = client.beta.threads.runs.retrieve(
        thread_id=thread_id, run_id=run.id
      )

  messages = client.beta.threads.messages.list(thread_id)
  with st.chat_message(messages.data[0].role): 
    st.write( messages.data[0].content[0].text.value)


    


# # File Upload 
# # file.id : file-aJ0E6Aeg8DzJhJW933eolr5f
# file = client.files.create(
#   file=open("unsu.pdf", "rb"),
#   purpose="assistants"
# )
# print(file)


# # Step 1: Create an Assistant
# assistant = client.beta.assistants.create(
#   name="현진건 작가님",
#   instructions="당신은 소설 운수 좋은 날을 집필한 현진건 작가님입니다.",
#   tools=[{"type": "retrieval"}],
#   model="gpt-4-turbo-2024-04-09",
#   file_ids=["file-aJ0E6Aeg8DzJhJW933eolr5f"]
# )
# # to confirm assistant_id ( asst_1Uk251mYdbaadsC )
# print(assistant)

# # Step 2: Create a Thread
# thread = client.beta.threads.create()
# # to confirm thread_id ( thread_nMvepvqfPdbbbg34Fpcex )
# print(thread)


# # Step 3: Add a Message to the Thread
# message = client.beta.threads.messages.create(
#     thread_id="thread_nMvepvqfPdbbbg34Fpcex",
#     role="user",
#     content="아내가 먹고 싶어 한 음식이 뭐야?"
# )
# print(message)

# run = client.beta.threads.runs.create(
#   # thread_id=thread.id,
#   # assistant_id=assistant.id,
#   thread_id="thread_nMvepvqfPdbbbg34Fpcex",
#   assistant_id="asst_1Uk251mYdbaadsC",
# )
# # run.id : run_WhRo6DVDddbassSt9YbxpSeuQ
# print(run)

# # confirm response's complete
# run = client.beta.threads.runs.retrieve(
#     thread_id="thread_nMvepvqfPdbbbg34Fpcex",
#     run_id="run_WhRo6DVDddbassSt9YbxpSeuQ"
# )
# print(run)

# messages = client.beta.threads.messages.list(
#     thread_id="thread_nMvepvqfPdbbbg34Fpcex"
#   )

# # https://platform.openai.com/docs/api-reference/messages/listMessages
# print (messages.data[0].content[0].text.value)



# #------------------------
# # Step 3: 추가 질문해보기...
# message = client.beta.threads.messages.create(
#     thread_id="thread_nMvepvqfPdbbbg34Fpcex",
#     role="user",
#     content="주제를 1000자 내외로 정리해줘"
# )
# print(message)

# run = client.beta.threads.runs.create(
#   # thread_id=thread.id,
#   # assistant_id=assistant.id,
#   thread_id="thread_nMvepvqfPdbbbg34Fpcex",
#   assistant_id="asst_1Uk251mYdbaadsC",
# )
# print(run)


# messages = client.beta.threads.messages.list(
#     thread_id="thread_nMvepvqfPdbbbg34Fpcex"
#   )
# print (messages.data[0].content[0].text.value)
