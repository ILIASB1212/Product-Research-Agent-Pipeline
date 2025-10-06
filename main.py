from dotenv import load_dotenv
from agents import Runner, trace
import os
from agents import  trace, Runner
from dotenv import load_dotenv
import os
from agents import  trace
import asyncio
from Agents.EmailAgent import email_agent
import streamlit as st
from Agents.PromptAgent import prompt_engennering_agent
from Agents.WebSearchAgent import web_search_agent
from Agents.RepportWriterAgent import writer_agent
from Agents.EmailAgent import email_agent
from Logs.logs import logging

load_dotenv()



with st.sidebar:
    st.title("Settings")
    api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    email_adress=st.text_input("Enter your Email Address:")
    if api_key and email_adress:
        st.success("API Key and Email set successfully!")
os.environ["OPENAI_API_KEY"] = api_key

st.title("Product Researcher")

query=st.text_input("Enter your product research query:", key="query_input")
if st.button("Start Researching"):
    async def main():
            try:
                with trace("Research trace"):
                    with st.spinner("Planning searches..."):
                        try:
                            agent_prompt = await Runner.run(prompt_engennering_agent, f"Query: {query}")
                        except Exception as e:
                            st.error(f"Error in prompt engineering agent: {e}")
                            return
                    st.success(f"finished generating prompt")
                    prompt = f"Search term: {agent_prompt.final_output}"
                    with st.spinner("Searching the web..."):
                        try:
                            search = await Runner.run(web_search_agent, prompt)
                        except Exception as e:
                            st.error(f"Error in web search agent: {e}")
                            return

                    input_query = f"Original query: {query}\nSummarized search results: {search.final_output}"
                    with st.spinner("Writing report..."):
                        try:
                            result = await Runner.run(writer_agent, input_query)
                            logging.info(f"user asked for {query}\nthe aagent rewrite the prompt to : {agent_prompt.final_output}\nthe web search result is : {search.final_output}\n")
                        except Exception as e:
                            st.error(f"Error in report writing agent: {e}")
                            return
                    st.success("Finished writing report")
                    report_data = result.final_output 
                    st.markdown(report_data.markdown_report)
                    with st.spinner("Writing email..."):
                        try:         
                            email = await Runner.run(email_agent, f"Recipient Email: {email_adress}\nReport:\n{report_data.markdown_report}")
                        except Exception as e:
                            st.error(f"Error in email agent: {e}")
                            return
                    st.success("Email sent") 
            except Exception as e:
                st.error(f"An error occurred: {e}")
    asyncio.run(main())