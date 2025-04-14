import os # os모듈을 통해서 환경 변수가 관리.
from dotenv import load_dotenv # .env 파일 저장된 환경변수 불러오기.
from openai import OpenAI# openai api를 사용하기 위한 클라이언트 불러오기

load_dotenv()

API_KEY = os.environ["APT_KEY"] # os.environ:마치 파이썬 내장 자료구조인 사전을 사용하듯이 사용할 수 있다. 
SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]

BASE_URL = "https://api.together.xyz"
MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL )# 클라이언트 초기화 

messages =[
    {"role" : "system", "content" : SYSTEM_MESSAGE}
] #챗봇 성경, 규칙 지정

print("챗봇을 시작합니다! (종료하려면 'exit' 입력)")

while True:
    user_input = input("You: ")#콘솔에서 사용자 입력을 계속 받고 exit입력하면 종료
    if user_input.lower() in ["exit", "quit"]:
        print("챗봇을 종료합니다.")
        break
    
    messages.append({"role": "user", "content": user_input}) # 사용자 입력을 메시지 리스트에 추가한 뒤 메시지 보내고 응답 요청.

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7 #0 -> 매우 정확 1-> 매우 창의적
    )
    chatbot_reply = response.choices[0].message.content
    print("Chatbot:", chatbot_reply)

    messages.append({"role": "assistant", "content": chatbot_reply})
    
    #--- 아이디어 작성 ---
    # 이 챗봇을 어디에 응용할 수 있을까요?
    # 병원에서 의사에 진단을 받기 전에 환자가 챗봇과 대화하고 그 대화 내용을 의사에게 전달을 해서 의사가 빠르게 진단을 내릴 수 있도록 한다. 
    # 아니면 환자가 병원에 가기 전에 챗봇에게 질문을 하면서 해결할 수 있으면 혼자 해결 할 수 있도록 도움을 줄 수 있다. 
