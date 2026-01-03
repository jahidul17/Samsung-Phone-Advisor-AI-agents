import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from agents.tools import fetch_phone_specs


async def ask_ai(question: str):
    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.1
    )

    tools = [fetch_phone_specs]
    
    try:

        prompt = hub.pull("hwchase17/react")

        agent = create_react_agent(llm, tools, prompt)

        agent_executor = AgentExecutor(
            agent=agent, 
            tools=tools, 
            verbose=True, 
            handle_parsing_errors=True,
            max_iterations=5 
        )

        input_text = f"You are a Samsung mobile expert. Answer the following question: {question}"
        
        result = await agent_executor.ainvoke({"input": input_text})
        
        return result["output"]

    except Exception as e:
        print(f"Detailed Error: {e}")
        return "I'm sorry, I'm having trouble retrieving that information right now."
    