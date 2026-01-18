from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template='generate a creative title for a book  about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="Generate a 5 point deatliled outline for a book titled '{title}'",
    input_variables=['title']
)

model=ChatOpenAI()

parser=StrOutputParser()
chain=prompt1 | model |prompt2 | model | parser

result=chain.invoke({'topic':'artificial intelligence'})    

print(result)



