from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnablePassthrough


load_dotenv()

prompt1=PromptTemplate(
    template='Write a deatlised  report  on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Summaries  the  following the input {text}',
    input_variables=['text']
)

model=ChatOpenAI()

parser=StrOutputParser()


report_gen_chain=prompt1 |model |parser


branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300,prompt2 | model | parser),
    RunnablePassthrough()
)


final_chain=RunnableParallel(report_gen_chain,branch_chain)

chain=final_chain.invoke({'topic':'machine learning in healthcare'})
print(chain)

chain.get_graph().print_ascii() 

