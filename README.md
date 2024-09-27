# Crewai-DSA-Meta-Llama3-Chatbot
AI Algorithm Generator
This project is an AI-powered tool that generates step-by-step algorithms for various Data Structures concepts in any programming language. Built using Streamlit, CrewAI, and Meta's LLaMA model via Groq Cloud, the application assists in the creation, writing, and editing of algorithms, ensuring they are accurate, easy to understand, and executable in the specified language.

Features
Algorithm Planning: Automatically creates a detailed step-by-step plan for the specified Data Structures concept, highlighting key implementation steps and best practices.
Algorithm Writing: Generates precise, numbered algorithms with code snippets in the specified programming language.
Algorithm Editing: Reviews and refines the algorithm for clarity, logical consistency, and best practices.
Interactive UI: Built using Streamlit for an intuitive and interactive user experience.
Chat History: Stores the user's input and generated algorithms for easy reference and revision.
Tech Stack
Streamlit: Provides a user-friendly interface for input and displaying results.
CrewAI: Orchestrates the workflow between agents (Planner, Writer, Editor) for algorithm generation.
Meta's LLaMA Model (via Groq Cloud): Used for natural language processing to generate and edit algorithms.
Groq Cloud: Hosts Meta's LLaMA model to power the algorithm generation.
LangChain: Integrated for advanced language processing tasks.
Serper API: Utilized for search capabilities within the workflow.
How It Works
User Input: The user enters a Data Structures topic (e.g., "Singly Linked List") into the Streamlit interface.
Planning Phase: The Planner agent creates a detailed outline of the algorithm, including the required data structures and the steps to implement the algorithm in the selected programming language.
Writing Phase: The Writer agent uses the outline to generate a step-by-step algorithm with numbered steps, code snippets, and detailed explanations.
Editing Phase: The Editor agent refines the algorithm for logical accuracy, coding best practices, and clarity.
Output: The final algorithm is displayed in the Streamlit app, along with intermediate outputs (plan, draft, and edited version) for reference.
Chat History: The session stores each generated algorithm for later review, accessible through the sidebar.

Prerequisites
Python 3.7+
Streamlit
CrewAI
Meta's LLaMA model API key (via Groq Cloud)
Serper API key
dotenv for environment variable management

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/ai-algorithm-generator.git
cd ai-algorithm-generator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables: Create a .env file in the root directory and add your API keys:

env
Copy code
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
Run the application:

bash
Copy code
streamlit run app.py

Usage
Launch the Streamlit app.
Enter a Data Structures topic in the input field (e.g., "Singly Linked List").
Click the "Start Workflow" button to generate the algorithm.
View the algorithm plan, draft, and edited version in the output area.
Access previous workflows in the sidebar's "Chat History."

Example Topics
Singly Linked List
Binary Search Tree
Graph Traversal (DFS, BFS)
Sorting Algorithms (Merge Sort, Quick Sort)


Future Enhancements
Support for additional data structures and algorithms.
Integration with more programming languages.
Enhanced editing capabilities for customized algorithms.
Add an option to save the generated algorithms to local files.
Contributing
Contributions are welcome! Please fork the repository and create a pull request for any improvements or bug fixes.
