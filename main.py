import streamlit as st
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, tool
import os
from dotenv import load_dotenv
import pandas as pd
from IPython.display import Markdown

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Initialize LLM and Search Tool
llm = ChatGroq(
    temperature=0, 
    model_name="groq/llama-3.1-70b-versatile", 
    api_key=GROQ_API_KEY,
    provider="Meta"
)
search_tool = SerperDevTool(api_key=SERPER_API_KEY)

def create_agent(role, goal, backstory):
    return Agent(
        llm=llm,
        role=role,
        goal=goal,
        backstory=backstory,
        allow_delegation=False,
        verbose=True,
    )

planner = create_agent(
    role="Data Structures and Algorithms Teacher",
    goal="Provide a detailed, step-by-step plan for implementing the specified Data Structures concept ({topic}) in a chosen programming language.",
    backstory="You are tasked with creating a precise algorithm plan for a specific Data Structures concept ({topic}). Your plan should include each step required to implement the algorithm, necessary data structures, and best practices specific to {topic}.",
)

writer = create_agent(
    role="Algorithm Writer",
    goal="Generate a detailed and precise algorithm for the specified Data Structures concept ({topic}), using clear step-by-step instructions in the chosen programming language.",
    backstory="You are tasked with creating a step-by-step algorithm for {topic}, providing code snippets and explanations for each step. Ensure the instructions align with {topic}'s requirements and common implementations in the specified programming language.",
)

editor = create_agent(
    role="Editor",
    goal="Review and refine the algorithm for {topic}, ensuring each step is clear, logically structured, and correctly implemented in the specified programming language.",
    backstory="You review the algorithm for {topic} to ensure clarity, logical consistency, and adherence to programming best practices. Each step should be appropriately numbered and easy to understand, enhancing the instructional value for {topic}.",
)

def create_task(description, expected_output, agent):
    return Task(description=description, expected_output=expected_output, agent=agent)

plan = create_task(
    description=(
        "1. Identify key steps involved in implementing the {topic} algorithm.\n"
        "2. Outline a step-by-step plan for setting up {topic} and its operations in the chosen programming language.\n"
        "3. Highlight important considerations, common use cases, and potential edge cases specific to {topic}.\n"
        "4. Choose an appropriate programming language for implementing {topic}."
    ),
    expected_output="A detailed step-by-step algorithm outline tailored to the specified Data Structures concept ({topic}) in a selected programming language.",
    agent=planner,
)

write = create_task(
    description=(
        "1. Using the outlined plan, write the complete algorithm for {topic} step-by-step in the chosen programming language.\n"
        "2. Number each step clearly, providing code snippets and detailed explanations tailored to {topic}.\n"
        "3. Incorporate logical flow and handle edge cases specific to {topic}.\n"
        "4. Ensure the algorithm is easy to follow and directly executable in the specified language."
    ),
    expected_output="A well-written, step-by-step algorithm for {topic} with numbered steps, written in the specified programming language.",
    agent=writer,
)

edit = create_task(
    description="Review the algorithm for {topic} to ensure it is logically sound, each step is clearly numbered, and the code aligns with best practices for the chosen programming language.",
    expected_output="A refined algorithm for {topic}, accurately written in markdown format, with each step clearly numbered and correctly implemented in the specified programming language.",
    agent=editor,
)

crew = Crew(agents=[planner, writer, editor], tasks=[plan, write, edit], verbose=True)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def main():
    st.title("AI Algorithm Generator!")

    # Sidebar to display chat history
    st.sidebar.title("Chat History")
    for i, chat in enumerate(st.session_state['chat_history']):
        with st.sidebar.expander(f"{chat['topic']}"):
            st.write(chat)

    topic = st.text_input("Enter the topic for Algorithm creation (e.g., 'Singly Linked List')", "Singly Linked List")

    if st.button("Start Workflow"):
        with st.spinner("Running the Algorithm creation workflow..."):
            result = crew.kickoff(inputs={"topic": topic})
        
        # Extract the necessary outputs and format them
        try:
            plan_output = result.tasks_output[0].raw
            write_output = result.tasks_output[1].raw
            edit_output = result.tasks_output[2].raw

            # Display the outputs in a readable format
            st.subheader("Algorithm Plan")
            st.markdown(plan_output)

            st.subheader("Draft Algorithm Post")
            st.markdown(write_output)

            st.subheader("Edited Algorithm Post")
            st.markdown(edit_output)

            st.success("Workflow completed!")

            # Store the chat in session state
            chat_summary = {
                "topic": topic,
                "plan": plan_output,
                "write": write_output,
                "edit": edit_output,
            }
            st.session_state['chat_history'].append(chat_summary)

        except Exception as e:
            st.error(f"An error occurred while extracting the output: {e}")

if __name__ == "__main__":
    main()
