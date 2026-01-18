from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableParallel, RunnableSequence
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

Prompt=PromptTemplate(
    template='Write down the about onece jok in this {subject}',
    input_variables=['subject']
)

model=ChatOpenAI()

parser=StrOutputParser()

prompt2=PromptTemplate(
    template="Explain this fooloing joke{text}",
    input_variables=['text']

)

joke_chain=RunnableSequence(Prompt, model, parser)

parallel_chain=RunnableParallel({
    'joke':joke_chain,
    'explanation':RunnableSequence(prompt2, model, parser)
})

final_chain=RunnableSequence(parallel_chain,joke_chain)
result=final_chain.invoke({'subject':'programming'})
print(result)