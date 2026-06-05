from deepagents import create_deep_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    model=ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        project=os.getenv('GOOGLE_CLOUD_PROJECT')
    )
    result=model.invoke("what is 5 plus 4?")
    print(result.content)

    agent=create_deep_agent(
        model=model,
        tools=[],
        system_prompt="You are a helpful assistant."
    )
    result=agent.invoke({
        "messages":[
            {
                "role":"user",
                "content":"what is 5 plus 4?"
            }
        ]
    })
    for message in result['messages']:
        message.pretty_print()

if __name__=="__main__":
        main()


