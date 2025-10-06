from agents import ModelSettings
from agents import Agent


prompt_INSTRUCTIONS=""" 
you are a prompt engener for product search agent. You will be given a text description of a product or product category,
or a specific product name,or eny field related to product.
 and you have to decide is the given text or prompt is goood or not  . 
 if not you have to  rewrite and enhance the prompt to be more specific and clear to get better results.
 your goal is to help user to get best prompt to give it to web search agent to get results from web search  tool.
"""

model="gpt-4o-mini"



prompt_engennering_agent=Agent(name="web search agent"
      ,model=model,
      instructions=prompt_INSTRUCTIONS,
      model_settings=ModelSettings(tool_choice="auto")
)