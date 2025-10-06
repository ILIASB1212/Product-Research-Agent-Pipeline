### 🤖 Product Research Agent Pipeline
This project is a multi-agent AI system built using the agents framework and Streamlit. It automates the end-to-end process of market research: refining a product query, executing a web search, writing a detailed, structured report, and delivering the final document via email.

It serves as a strong demonstration of modern AI development practices, including multi-step agent orchestration, structured output enforcement (Pydantic), custom tool utilization (SendGrid), and robust logging.

### ✨ Features
- Multi-Agent Orchestration: A sequential pipeline involving four specialized agents (Prompt Refinement, Web Search, Report Writer, Email Sender).

- Intelligent Prompt Refinement: A dedicated agent ensures the final search query is optimized for maximum web search effectiveness.

- Structured Reporting: Uses Pydantic to enforce a structured report output, including a summary, the main report content, and suggested follow-up questions.

- Tool Integration: Seamlessly uses the built-in WebSearchTool for research and a custom SendGrid tool for email delivery.

- Dynamic Configuration: Allows the user to input their OpenAI API key and recipient email address via the Streamlit sidebar.

- Comprehensive Logging: Uses a dedicated Logs directory to record agent steps, queries, and results for auditing and debugging.

- Clean Web UI: Built with Streamlit for an interactive, modern user interface.

### 🏗️ Architecture and Agent Flow
The pipeline executes four distinct steps, ensuring high-quality, actionable results:

PromptAgent (gpt-4o-mini): Takes the user's initial query and enhances it into a refined, specific search term.

WebSearchAgent (gpt-4o-mini): Executes the web search using the optimized prompt and summarizes the results.

ReportAgentWriter (gpt-4o-mini): Receives the original query and summarized results, then generates a detailed report in a structured ReportData format (enforced by Pydantic).

EmailAgent (gpt-4o-mini): Uses the custom send_email tool (backed by SendGrid) to format the Markdown report into HTML and deliver it to the user-specified email address.

### 🚀 Getting Started
Prerequisites
Python 3.9+

A Virtual Environment (env folder in your project)

API Keys for:

OpenAI: For the LLM agents.

SendGrid: For sending the final email report.

Configuration
Clone the repository:

git clone github repo link
cd Product-Research-Agent-Pipeline

Install dependencies:

pip install -r requirements.txt

Create a .env file in the root directory (where main.py is located) and add your secret keys:

# .env file content
- SENDGRID_API_KEY="SG.**************************************"

### How to Run the App
Execute the Streamlit command from the root directory of the project:

streamlit run main.py

The application will open in your browser, where you can enter your query and settings (API Key and recipient email address) in the sidebar.

### 📁 Project Structure
The project is designed for maximum modularity and clarity:

Product-Research-Agent-Pipeline/
├── Agents/
│   ├── __init__.py
│   ├── EmailAgent.py         # Defines the EmailAgent and the custom `send_email` tool.
│   ├── PromptAgent.py        # Defines the PromptAgent for query refinement.
│   ├── ReportAgentWriter.py  # Defines the WriterAgent and the Pydantic `ReportData` schema.
│   └── WebSearchAgent.py     # Defines the WebSearchAgent with the WebSearchTool.
├── Logs/
│   ├── __init__.py
│   └── logs.py               # Handles logging configuration and timestamped file creation.
├── .env                      # Contains local API keys (ignored by Git).
├── main.py                   # The Streamlit application entry point and agent pipeline orchestrator.
└── requirements.txt          # List of Python dependencies.

### 🤝 Contributing
Feedback and contributions are welcome! Feel free to open issues or submit pull requests.
