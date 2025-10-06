from agents import ModelSettings
from agents import Agent,WebSearchTool
model="gpt-4o-mini"

WEB_INSTRUCTIONS=""" 
you are a product search agent. You will be given a product name
 and you have to find the best matching product from the web. 
 Use the web search tool to find the product and return the most relevant result
and find most rend products you can search chinees stores to find shepest ones that can be sell in usa.
required:
      1) if the user prompt is not related to product search you have to respond 
      with "i can only help you with product search"
      2)respond only with the prompt you will give to web search tool i want direct prompt
      3) if the user prompt is very general you have to enhance it to be more
"""




web_search_agent=Agent(name="web search agent"
      ,model=model,
      instructions=WEB_INSTRUCTIONS,
      tools=[WebSearchTool(search_context_size="low")],
      model_settings=ModelSettings(tool_choice="required")
)