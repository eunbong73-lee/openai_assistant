
# openapi install
pip install openai 

# streamlit install
pip install streamlit


# Files
0_test_assistant.py : 관련 객체 생성 테스트
1_mathtutor.py      : OpenAI Assistant 예제
2_asistant_demo.py  : Assistant에게 PDF 로딩한 후, RAG처럼 테스트



# local 실행
streamlit run 0_test_assistant.py
streamlit run 1_mathtutor.py
streamlit run 2_asistant_demo.py



# local 실행과 streamlit 실행 차이
1. OPENAI_API_KEY 사용 방법
   (1) local 실행 시에는 .env 파일에 OPENAI_API_KEY 값을 저장해 사용  ( dotenv 라이브러리 사용 필요)
   (2) streamlit 실행 시에는 secret에 toml 형식으로 OPENAI_API_KEY 저장하여 사용

2. pysqlite3 처리 
   (1) streamlit 실행 시에만 필요하여 pysqlite3 모듈 처리
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')