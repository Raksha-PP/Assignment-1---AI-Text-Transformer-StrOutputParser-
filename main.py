from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1️⃣ Create local Ollama model
model = OllamaLLM(
    model="llama3",   # Make sure this model is pulled
    temperature=0.7
)

# 2️⃣ Create Prompt Template
prompt = PromptTemplate(
    input_variables=["paragraph"],
    template="""
You are an AI Text Transformer.

Given the paragraph below, do the following:

1. Provide a short summary (3-4 lines).
2. Detect the tone (Formal / Casual / Technical).
3. Provide an improved version of the paragraph.

Return everything clearly formatted as plain text (NOT JSON).

Paragraph:
{paragraph}
"""
)

# 3️⃣ Output parser (converts model output to string)
parser = StrOutputParser()

# 4️⃣ Create clean chain
chain = prompt | model | parser

# 5️⃣ Take user input
user_input = input("Enter a paragraph:\n")

# 6️⃣ Invoke chain
result = chain.invoke({"paragraph": user_input})

print("\n===== OUTPUT =====\n")
print(result)
