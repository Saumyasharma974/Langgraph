# LangChain Notes — Day 1

## Architecture + Models + Messages + ChatPromptTemplate

> **Goal:** Ye notes tumhare `04_langchain` folder ke notes/code ke saath rakh sakte ho. Maine **sirf woh concepts include kiye hain jo humne ab tak actually padhe aur hands-on kiye hain**. Jo topics abhi nahi padhe, unhe intentionally include nahi kar raha.

---

# 1. What is LangChain?

**LangChain is an open-source framework/ecosystem for building applications and agents powered by language models.**

LangChain humein reusable building blocks deta hai, jaise:

```text
Models
Messages
Prompts
Runnables
Tools
Retrieval
Structured Output
Agents
Middleware
```

In components ko combine karke hum LLM applications bana sakte hain.

### Simple example

Without composition:

```text
User
 ↓
LLM
 ↓
Response
```

A more complex application:

```text
User
 ↓
Prompt
 ↓
Model
 ↓
Tool
 ↓
Model
 ↓
Structured Output
 ↓
Response
```

LangChain ka main benefit hai ki ye different components ko **compose** karne ke liye abstractions provide karta hai.

---

# 2. LangChain vs LLM

LangChain khud LLM nahi hai.

Example:

```text
Llama
   ↓
LLM / Model

LangChain
   ↓
Framework / Ecosystem
```

Humare project mein:

```text
LangChain
    ↓
ChatGroq
    ↓
Llama 3.1 8B
```

`ChatGroq` Groq model provider ke saath LangChain integration provide karta hai.

---

# 3. Basic LangChain Architecture

Abhi tak jo mental model banaya hai:

```text
                    LANGCHAIN
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
      Models          Prompts           Tools
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                    Runnables
                        │
             ┌──────────┼──────────┐
             ↓          ↓          ↓
        Structured   Retrieval    Agents
          Output
```

**Important:** Is diagram ke kuch components humne abhi sirf conceptually dekhe hain. Unki detailed implementation abhi baaki hai.

---

# 4. Models

Model LLM response generate/process karne wala component hai.

Humne Groq ke saath model banaya:

```python
from langchain_groq import ChatGroq

model = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0
)
```

Yahan:

```text
ChatGroq
   ↓
Llama 3.1 8B Instant
```

---

# 5. Chat Models

LangChain mein hum chat models ke saath **messages** ke form mein interact kar sakte hain.

Simple conceptual flow:

```text
Messages
   ↓
Chat Model
   ↓
AIMessage
```

Instead of thinking only:

```text
string → string
```

chat applications mein:

```text
SystemMessage
HumanMessage
AIMessage
ToolMessage
```

jaise structured messages use hote hain.

---

# 6. Messages

Messages conversation ke individual parts ko represent karte hain.

Important message types:

```text
SystemMessage
HumanMessage
AIMessage
ToolMessage
```

Humne inmein se first three practically use kiye aur `ToolMessage` ka basic concept dekha.

---

# 7. `SystemMessage`

`SystemMessage` model ke behavior/instructions define karta hai.

Example:

```python
from langchain_core.messages import SystemMessage

message = SystemMessage(
    content="You are an expert programming teacher."
)
```

Meaning:

> Model ko programming teacher ki tarah behave karna hai.

Example:

```text
System:
You are an expert programming teacher.
```

---

# 8. `HumanMessage`

`HumanMessage` user ke input ko represent karta hai.

Example:

```python
from langchain_core.messages import HumanMessage

message = HumanMessage(
    content="Explain JWT."
)
```

Meaning:

```text
Human:
Explain JWT.
```

---

# 9. `AIMessage`

`AIMessage` model ke response ko represent karta hai.

Flow:

```text
HumanMessage
      ↓
Chat Model
      ↓
AIMessage
```

Humne practically verify kiya:

```python
response = model.invoke(messages)

print(type(response))
```

Output:

```text
<class 'langchain_core.messages.ai.AIMessage'>
```

### Important

`model.invoke()` se plain string nahi milti.

Chat model ke case mein response ek `AIMessage` object hota hai.

---

# 10. `AIMessage.content`

Actual generated text:

```python
response.content
```

Example:

```python
response = model.invoke(messages)

print(response.content)
```

Flow:

```text
AIMessage
    │
    └── content
          ↓
      AI response
```

---

# 11. `AIMessage` ka structure

Humne actual output mein kuch important fields dekhe:

```text
AIMessage(
    content="...",
    additional_kwargs={},
    response_metadata={...},
    tool_calls=[],
    invalid_tool_calls=[],
    usage_metadata={...}
)
```

Important fields:

```text
content
response_metadata
usage_metadata
tool_calls
invalid_tool_calls
```

---

# 12. `usage_metadata`

`usage_metadata` token usage information provide karta hai.

Humare output mein:

```python
response.usage_metadata
```

gave:

```python
{
    'input_tokens': 52,
    'output_tokens': 237,
    'total_tokens': 289
}
```

Meaning:

```text
Input tokens  = 52
Output tokens = 237
Total tokens  = 289
```

Ye directly LLM Fundamentals ke token usage concepts se related hai.

---

# 13. `response_metadata`

Provider/model related metadata `response_metadata` mein mil sakta hai.

Example:

```python
response.response_metadata
```

Humare output mein information thi:

```text
token_usage
model_name
completion_time
prompt_time
queue_time
total_time
finish_reason
model_provider
```

Example:

```text
model_name:
llama-3.1-8b-instant

model_provider:
groq

finish_reason:
stop
```

### Difference

```text
usage_metadata
     ↓
Normalized token usage

response_metadata
     ↓
Provider/model specific metadata
```

---

# 14. `tool_calls`

`AIMessage` mein tool calls bhi aa sakte hain.

Abhi humare output mein:

```python
tool_calls=[]
```

tha.

Ye expected tha because humne model ko koi tool nahi diya tha.

Future tool-calling flow:

```text
HumanMessage
      ↓
AIMessage
      ↓
tool_calls
      ↓
Tool
      ↓
ToolMessage
      ↓
AIMessage
```

Humne abhi tool calling implement nahi kiya hai.

---

# 15. `invalid_tool_calls`

AIMessage mein:

```python
invalid_tool_calls=[]
```

bhi dekha.

Abhi empty tha because humne tool calling nahi ki thi.

Iski detailed behavior hum **Tool Calling** topic mein padhenge.

---

# 16. `ToolMessage`

`ToolMessage` tool ke execution ke result ko represent karta hai.

Conceptual flow:

```text
User
 ↓
AIMessage
 ↓
Tool Call
 ↓
Tool executes
 ↓
ToolMessage
 ↓
AIMessage
```

Example scenario:

```text
User:
What is the weather in Delhi?

AI:
I need to call weather tool.

Tool:
32°C

ToolMessage:
32°C

AI:
Delhi is currently 32°C.
```

**Abhi humne `ToolMessage` ko sirf conceptually cover kiya hai.**

---

# 17. Runnables — Basic Concept

Runnable LangChain ka ek **composable unit** hai.

Simple mental model:

```text
Input
 ↓
Runnable
 ↓
Output
```

Multiple runnable components combine ho sakte hain:

```text
Prompt
 ↓
Model
 ↓
Parser
```

Ye LangChain ki compositional architecture ka important foundation hai.

---

# 18. Runnable Methods — Basic Introduction

Humne in methods ka concept dekha:

### `.invoke()`

Normal/synchronous execution.

```python
result = component.invoke(input)
```

### `.ainvoke()`

Asynchronous execution.

```python
result = await component.ainvoke(input)
```

### `.stream()`

Streaming output.

```python
for chunk in component.stream(input):
    ...
```

### `.batch()`

Multiple inputs process karna.

```python
results = component.batch(inputs)
```

Async variants:

```text
ainvoke()
astream()
abatch()
```

**Important:** In methods ko abhi deeply nahi padha. Runnables/LCEL chapter mein one-by-one detail mein karenge.

---

# 19. Prompt Templates

Ab hum `ChatPromptTemplate` section mein aaye.

Problem:

Agar baar-baar different topics explain karne hain:

```text
Explain JWT
Explain Docker
Explain RAG
Explain LangGraph
```

toh har baar prompt manually banana inefficient hai.

Instead reusable template:

```text
Explain {topic}
```

---

# 20. `ChatPromptTemplate`

Simple definition:

> **`ChatPromptTemplate` is used to create reusable, dynamic chat-message templates.**

Import:

```python
from langchain_core.prompts import ChatPromptTemplate
```

Basic:

```python
prompt = ChatPromptTemplate.from_messages([
    (
        "human",
        "Explain {topic}"
    )
])
```

---

# 21. Template Variable

`{topic}` ek template variable hai.

```text
Explain {topic}
        ↑
     variable
```

Value:

```python
messages = prompt.invoke({
    "topic": "JWT"
})
```

Result conceptually:

```text
Explain JWT
```

Flow:

```text
"Explain {topic}"
       ↓
topic = JWT
       ↓
"Explain JWT"
```

---

# 22. `prompt.invoke()` vs `model.invoke()`

Ye **bahut important distinction** hai.

### `prompt.invoke()`

Prompt ko format karta hai.

```python
messages = prompt.invoke({
    "topic": "JWT"
})
```

Flow:

```text
Dictionary
    ↓
ChatPromptTemplate
    ↓
Messages
```

**LLM call nahi hota.**

### `model.invoke()`

Actual model call karta hai:

```python
response = model.invoke(messages)
```

Flow:

```text
Messages
   ↓
ChatGroq
   ↓
AIMessage
```

### Complete flow

```text
Variables
   ↓
ChatPromptTemplate
   ↓
Messages
   ↓
ChatGroq
   ↓
AIMessage
```

---

# 23. Multiple Variables

Ek template mein multiple variables ho sakte hain.

Example:

```python
prompt = ChatPromptTemplate.from_messages([
    (
        "human",
        "Explain {topic} in {language} for a {level} student."
    )
])
```

Invoke:

```python
messages = prompt.invoke({
    "topic": "JWT",
    "language": "English",
    "level": "beginner"
})
```

Result:

```text
Explain JWT in English for a beginner student.
```

### Flow

```text
{topic}    → JWT
{language} → English
{level}    → beginner
```

---

# 24. Duplicate Dictionary Key

Humne ek experiment mein ye dekha:

```python
{
    "topic": "JWT",
    "topic": "nodemon"
}
```

Python dictionary mein same key do baar nahi rakhni chahiye.

Second value first ko overwrite kar deti hai.

Effectively:

```python
{
    "topic": "nodemon"
}
```

Isliye agar multiple independent values chahiye, different keys use karo:

```python
{
    "topic1": "JWT",
    "topic2": "Nodemon"
}
```

---

# 25. `system` + `human`

`ChatPromptTemplate` mein humne multiple message roles use kiye.

```python
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert programming teacher."
    ),
    (
        "human",
        "Explain {topic}."
    )
])
```

Output:

```text
SystemMessage
HumanMessage
```

### Meaning

```text
system
  ↓
AI ka behavior/instructions

human
  ↓
User ka request
```

---

# 26. Dynamic System Prompt

System message bhi dynamic ho sakta hai.

Example:

```python
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert {role}."
    ),
    (
        "human",
        "Explain {topic} in {language} for a {level} student."
    )
])
```

Invoke:

```python
messages = prompt.invoke({
    "role": "Python teacher",
    "topic": "JWT",
    "language": "English",
    "level": "beginner"
})
```

Result:

```text
SystemMessage:
You are an expert Python teacher.

HumanMessage:
Explain JWT in English for a beginner student.
```

---

# 27. `MessagesPlaceholder`

Ab humne conversation history ko dynamic prompt mein insert karna seekha.

Import:

```python
from langchain_core.messages import HumanMessage, AIMessage
```

Prompt:

```python
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant."
    ),
    (
        "placeholder",
        "{history}"
    ),
    (
        "human",
        "{question}"
    )
])
```

Yahan:

```text
{history}
```

special purpose variable hai.

---

# 28. History kya hai?

Example:

```python
history = [
    HumanMessage(
        content="My name is Saumya."
    ),
    AIMessage(
        content="Nice to meet you, Saumya."
    )
]
```

Then:

```python
messages = prompt.invoke({
    "history": history,
    "question": "What is my name?"
})
```

Result:

```text
SystemMessage:
You are a helpful assistant.

HumanMessage:
My name is Saumya.

AIMessage:
Nice to meet you, Saumya.

HumanMessage:
What is my name?
```

---

# 29. `MessagesPlaceholder` ka main purpose

Simple:

> **`MessagesPlaceholder` allows a list of messages to be inserted dynamically into a chat prompt.**

Normal variable:

```text
{topic}
```

normally ek value:

```python
"JWT"
```

receive karta hai.

History:

```text
{history}
```

message list receive karti hai:

```python
[
    HumanMessage(...),
    AIMessage(...),
    HumanMessage(...),
    AIMessage(...)
]
```

---

# 30. Multiple Conversation Turns

Humne practically test kiya:

```python
history = [
    HumanMessage(content="My name is Saumya."),
    AIMessage(content="Nice to meet you, Saumya."),
    HumanMessage(content="I am learning Agentic AI."),
    AIMessage(content="That's great!")
]
```

Question:

```python
"question": "What am I learning?"
```

Final messages:

```text
SystemMessage
HumanMessage → My name is Saumya.
AIMessage    → Nice to meet you, Saumya.
HumanMessage → I am learning Agentic AI.
AIMessage    → That's great!
HumanMessage → What am I learning?
```

Model correctly used the conversation context.

---

# 31. `MessagesPlaceholder + ChatGroq`

Complete flow we implemented:

```text
History
   ↓
MessagesPlaceholder
   ↓
ChatPromptTemplate
   ↓
Messages
   ↓
ChatGroq
   ↓
AIMessage
   ↓
response.content
```

Code pattern:

```python
messages = prompt.invoke({
    "history": history,
    "question": "What is my name?"
})

response = model.invoke(messages)

print(response.content)
```

Output:

```text
Your name is Saumya.
```

---

# 32. `PromptTemplate`

We then compared normal `PromptTemplate`.

Import:

```python
from langchain_core.prompts import PromptTemplate
```

Example:

```python
prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)
```

Invoke:

```python
result = prompt.invoke({
    "topic": "JWT"
})
```

Our current LangChain version returned:

```text
<class 'langchain_core.prompt_values.StringPromptValue'>
```

And:

```python
result.text
```

gave:

```text
Explain JWT in simple language.
```

---

# 33. `StringPromptValue`

`PromptTemplate.invoke()` ke result ko humne practically dekha:

```text
StringPromptValue
```

Example:

```python
print(type(result))
```

Output:

```text
<class 'langchain_core.prompt_values.StringPromptValue'>
```

Actual text:

```python
print(result.text)
```

Output:

```text
Explain JWT in simple language.
```

Flow:

```text
PromptTemplate
      ↓
StringPromptValue
      ↓
.text
      ↓
Actual text
```

---

# 34. `ChatPromptValue`

`ChatPromptTemplate.invoke()` se humne:

```text
ChatPromptValue
```

observe kiya.

Example:

```python
chat_result = chat_prompt.invoke({
    "topic": "JWT"
})
```

Type:

```text
<class 'langchain_core.prompt_values.ChatPromptValue'>
```

Messages:

```python
chat_result.messages
```

Output:

```text
[
    SystemMessage(...),
    HumanMessage(...)
]
```

Flow:

```text
ChatPromptTemplate
       ↓
ChatPromptValue
       ↓
.messages
       ↓
SystemMessage
HumanMessage
```

---

# 35. `PromptTemplate` vs `ChatPromptTemplate`

## `PromptTemplate`

Text-oriented prompt.

```text
PromptTemplate
      ↓
StringPromptValue
      ↓
.text
```

Example:

```text
Explain JWT in simple language.
```

## `ChatPromptTemplate`

Chat/message-oriented prompt.

```text
ChatPromptTemplate
       ↓
ChatPromptValue
       ↓
.messages
       ↓
SystemMessage
HumanMessage
```

---

# 36. Main Difference

| Feature       | PromptTemplate          | ChatPromptTemplate            |
| ------------- | ----------------------- | ----------------------------- |
| Purpose       | Text-oriented prompts   | Chat/message-oriented prompts |
| Result        | `StringPromptValue`     | `ChatPromptValue`             |
| Access        | `.text`                 | `.messages`                   |
| System role   | ❌                       | ✅                             |
| Human role    | ❌ as a structured role  | ✅                             |
| AI messages   | ❌                       | ✅                             |
| Tool messages | ❌ as chat roles         | ✅                             |
| Chat history  | Not its primary purpose | ✅                             |

### Interview answer

> **`PromptTemplate` is primarily used to construct text-oriented prompts, while `ChatPromptTemplate` is designed for chat models and constructs structured messages with roles such as system and human.**

---

# 37. Complete `ChatPromptTemplate` Flow

Abhi tak ka complete flow:

```text
                         ChatPromptTemplate
                                │
                  ┌─────────────┼──────────────┐
                  ↓             ↓              ↓
              Variables     System/Human    History
                  │             │              │
                  └─────────────┼──────────────┘
                                ↓
                         ChatPromptValue
                                ↓
                           .messages
                                ↓
                         ChatGroq Model
                                ↓
                            AIMessage
                                ↓
                         response.content
```

---

# 38. Important Code Pattern

Ye pattern tumhe baar-baar milega:

```python
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing")


model = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert programming teacher."
    ),
    (
        "human",
        "Explain {topic} in {language} for a {level} student."
    )
])


messages = prompt.invoke({
    "topic": "JWT",
    "language": "English",
    "level": "beginner"
})


response = model.invoke(messages)


print(response.content)
```

Flow:

```text
Variables
    ↓
ChatPromptTemplate
    ↓
ChatPromptValue
    ↓
messages
    ↓
ChatGroq
    ↓
AIMessage
    ↓
content
```

---

# 39. Important Things We Have NOT Covered Yet

In `ChatPromptTemplate`, these are still pending:

```text
❌ Missing variables & validation
❌ Optional variables
❌ Advanced MessagesPlaceholder usage
❌ Different message-template formats
❌ AI message templates in detail
❌ partial()
❌ Prompt variable inspection
❌ Prompt validation/debugging
❌ Prompt composition
```

**Inko abhi notes mein learned topics mat samajhna.** Ye next sessions mein padhenge.

---

# 🎯 Interview Revision

### Q1. What is LangChain?

LangChain is an open-source framework/ecosystem for building LLM-powered applications and agents using composable components.

### Q2. What is `ChatGroq`?

A LangChain integration used to interact with chat models provided through Groq.

### Q3. What does `model.invoke()` return?

For a chat model, it returns an `AIMessage`.

### Q4. How do you get the generated text?

```python
response.content
```

### Q5. What is `AIMessage`?

A message object representing the model's response. It can contain content, metadata and tool calls.

### Q6. What is `ChatPromptTemplate`?

A reusable template for constructing dynamic chat messages.

### Q7. Does `prompt.invoke()` call the LLM?

**No.**

It formats the prompt and produces a prompt value/messages.

### Q8. What does `MessagesPlaceholder` do?

It dynamically inserts a list of messages, such as conversation history, into a chat prompt.

### Q9. `PromptTemplate` vs `ChatPromptTemplate`?

```text
PromptTemplate
    ↓
StringPromptValue
    ↓
text
```

while:

```text
ChatPromptTemplate
    ↓
ChatPromptValue
    ↓
messages
```

### Q10. What is a template variable?

A placeholder such as:

```text
{topic}
```

whose value is supplied during invocation.

### Q11. Can a prompt have multiple variables?

Yes:

```python
{
    "topic": "JWT",
    "language": "English",
    "level": "beginner"
}
```

### Q12. What is the difference between `system` and `human`?

```text
system → instructions/behavior
human  → user's request
```

---

# 🧠 Final Mental Model — Day 1

```text
                         LANGCHAIN
                             │
                             ↓
                          MODEL
                             │
                       Chat Model
                             │
                         Messages
                             │
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
        SystemMessage   HumanMessage    AIMessage
                                             │
                                        tool_calls
                                             │
                                        (later)
```

Then:

```text
                    CHAT PROMPT
                         │
                         ↓
               ChatPromptTemplate
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
    Variables      System/Human       History
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                ChatPromptValue
                         ↓
                    .messages
                         ↓
                     Chat Model
                         ↓
                      AIMessage
                         ↓
                   response.content
```

And the text-oriented alternative:

```text
PromptTemplate
      ↓
StringPromptValue
      ↓
result.text
```

---

## ✅ Your actual progress

```text
LangChain Architecture       ✅
Models                       ✅
Chat Models                  ✅
Messages                     ✅
SystemMessage                ✅
HumanMessage                 ✅
AIMessage                    ✅
AIMessage metadata            ✅
Token usage                  ✅
Tool calls                   🟡 Concept
ToolMessage                   🟡 Concept
Runnables                     🟡 Concept

ChatPromptTemplate            🟡 In Progress
  ├─ Variables                ✅
  ├─ Multiple variables       ✅
  ├─ System + Human           ✅
  ├─ Dynamic system prompt    ✅
  ├─ MessagesPlaceholder      ✅
  ├─ Conversation history     ✅
  ├─ History + ChatGroq       ✅
  └─ PromptTemplate comparison✅
```

**Next session exactly where we stopped:** `ChatPromptTemplate → Missing Variables & Validation`.
