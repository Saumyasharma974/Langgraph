from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage


parser = StrOutputParser()


message = AIMessage(
    content="JWT is a token used for authentication."
)


print("INPUT:")
print(message)

print("\nINPUT TYPE:")
print(type(message))


result = parser.invoke(message)


print("\nPARSED OUTPUT:")
print(result)

print("\nOUTPUT TYPE:")
print(type(result))


print("\nIS STRING:")
print(isinstance(result, str))

print("\nOUTPUT CLASS:")
print(result.__class__)

print("\nOUTPUT MRO:")
print(result.__class__.__mro__)