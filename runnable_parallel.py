from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv



load_dotenv()


prompt=PromptTemplate(
    template='Generate a tweet about{topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    temaplate='Generate a LinkedIn post about{topic}',
    input_variables=['topic']   
)

model = ChatOpenAI()

parser = StrOutputParser()


parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt, model, parser),
    'linkedin_post':RunnableSequence(prompt2, model, parser)    
})

result=parallel_chain.invoke({'topic':'Machine Learning'})

print(result)
print("Tweet: ", result['tweet'])
print("LinkedIn Post: ", result['linkedin_post'])

