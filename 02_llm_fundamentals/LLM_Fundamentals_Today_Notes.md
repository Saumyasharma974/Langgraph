# LLM Fundamentals --- Today's Detailed Notes

## Today's Coverage

``` text
14 Streaming
15 Async Basics
16 Async LLM
17 Error Handling
18 Retry Strategy
19 Exponential Backoff
20 Timeout
21 LLM Timeout
22 Rate Limits
23 Token Rate Limit
24 Token Usage
25 Cost Optimization
26 Model Selection
27 Latency Optimization
28 Grounding
29 Grounding Comparison
30 LLM Evaluation
31 Regression Testing
32 Evaluation Dataset
```

------------------------------------------------------------------------

# 1. Streaming

## What is Streaming?

Normally, an LLM returns the complete response after generation
finishes:

``` text
User
 ↓
LLM
 ↓
Complete Response
 ↓
User
```

With streaming, the response is received gradually in chunks:

``` text
User
 ↓
LLM
 ↓
Chunk 1 → User
Chunk 2 → User
Chunk 3 → User
Chunk 4 → User
...
```

### LangChain

Synchronous streaming:

``` python
for chunk in llm.stream(messages):
    print(chunk.content, end="", flush=True)
```

Asynchronous streaming:

``` python
async for chunk in llm.astream(messages):
    print(chunk.content, end="", flush=True)
```

### Why use streaming?

The main benefit is **perceived latency**. The user starts seeing the
response earlier instead of waiting for the entire answer.

------------------------------------------------------------------------

# 2. Async Programming

You learned:

-   `async`
-   `await`
-   `asyncio`
-   `asyncio.gather()`

## `async`

Makes a function asynchronous:

``` python
async def research_task():
    ...
```

## `await`

Waits for an asynchronous operation:

``` python
result = await research_task()
```

## `asyncio.gather()`

Runs independent asynchronous tasks concurrently:

``` python
results = await asyncio.gather(
    research_task(),
    news_task()
)
```

Example:

``` python
async def research_task():
    await asyncio.sleep(2)
    return "Research completed"


async def news_task():
    await asyncio.sleep(5)
    return "News completed"
```

Sequential execution:

``` text
2 + 5 = approximately 7 seconds
```

Concurrent execution:

``` text
max(2, 5) = approximately 5 seconds
```

Actual API timings can vary.

### Important

Async does not make the LLM itself faster. It allows the application to
use waiting time efficiently for independent I/O operations.

------------------------------------------------------------------------

# 3. Async LLM Calls

Normal LLM call:

``` python
response = llm.invoke("Explain JWT")
```

Async LLM call:

``` python
response = await llm.ainvoke("Explain JWT")
```

Async streaming:

``` python
async for chunk in llm.astream(messages):
    print(chunk.content)
```

### Parallel LLM calls

Independent LLM calls can be executed concurrently:

``` python
results = await asyncio.gather(
    explain_jwt(),
    explain_oauth()
)
```

Architecture:

``` text
                 main()
                   ↓
            asyncio.gather()
              ↙         ↘
             ↓           ↓
        JWT Call     OAuth Call
             ↓           ↓
            Groq       Groq
```

This can reduce total latency when the tasks are independent.

------------------------------------------------------------------------

# 4. Error Handling

LLM APIs are external services, so failures can happen.

Possible failures include:

-   API errors
-   Network errors
-   Timeouts
-   Rate limits
-   Invalid requests
-   Temporary service failures

Basic handling:

``` python
try:
    response = llm.invoke("Hello")
except Exception as e:
    print(e)
```

Production applications should decide what to do after an error:

``` text
Error
 ↓
Retry?
 ├── Yes → Retry
 ├── No → Fallback
 └── Critical → Stop / Report
```

------------------------------------------------------------------------

# 5. Retry Strategy

A retry means attempting the same operation again after a failure.

Example:

``` text
Attempt 1 → Failed
Attempt 2 → Failed
Attempt 3 → Success
```

Retries are useful for temporary failures, but unlimited retries are
dangerous.

A retry strategy should consider:

-   Maximum retry attempts
-   Delay between attempts
-   Type of error
-   Fallback behavior

------------------------------------------------------------------------

# 6. Exponential Backoff

You learned the formula:

``` python
delay = 2 ** (attempt - 1)
```

Examples:

``` text
Attempt 1 → 2^0 = 1 second
Attempt 2 → 2^1 = 2 seconds
Attempt 3 → 2^2 = 4 seconds
Attempt 4 → 2^3 = 8 seconds
```

So:

``` text
Attempt 1 → wait 1 sec
Attempt 2 → wait 2 sec
Attempt 3 → wait 4 sec
Attempt 4 → wait 8 sec
```

## Why exponential backoff?

If many clients retry immediately after a server failure:

``` text
Request fails
 ↓
Everyone retries immediately
 ↓
Server gets more load
 ↓
More failures
```

Backoff spreads retries over time.

------------------------------------------------------------------------

# 7. Timeout

A timeout defines the maximum time an application should wait for an
operation.

Example:

``` python
response = await llm.ainvoke(
    "Explain JWT",
    timeout=1
)
```

If the operation does not complete within the allowed time, it can fail
with a timeout.

## Why timeout?

Without a timeout:

``` text
LLM Request
 ↓
Waiting...
 ↓
Waiting...
 ↓
Waiting...
```

The application may remain stuck for too long.

Timeouts are an important reliability mechanism.

------------------------------------------------------------------------

# 8. LLM Timeout

You specifically practiced adding a timeout to an asynchronous LLM call:

``` python
response = await llm.ainvoke(
    "Explain how JWT works",
    timeout=1
)
```

Typical structure:

``` python
async def ask_llm():
    try:
        response = await llm.ainvoke(
            "Explain how JWT works",
            timeout=1
        )

        print(response.content)

    except Exception as e:
        print(e)
```

The important idea is:

``` text
LLM Request
     ↓
Time limit
     ↓
Response?
 ┌───┴────┐
YES       NO
 ↓         ↓
Success   Timeout/Error
```

------------------------------------------------------------------------

# 9. Rate Limits

A rate limit controls how many requests can be made within a particular
time period.

Simple example:

``` python
RATE_LIMIT = 3

for request in range(1, 6):

    if request <= RATE_LIMIT:
        print("request approved")
    else:
        print("request rejected")
```

Conceptually:

``` text
Request 1 → Approved
Request 2 → Approved
Request 3 → Approved
Request 4 → Rejected
Request 5 → Rejected
```

Real providers may apply limits over a time window.

------------------------------------------------------------------------

# 10. Token Rate Limits

Rate limits can also apply to tokens.

Example:

``` text
Token limit = 10,000 tokens
```

Requests:

``` text
Request 1 → 2,000 tokens
Request 2 → 3,000 tokens
Request 3 → 4,000 tokens
```

Total:

``` text
2,000 + 3,000 + 4,000
= 9,000 tokens
```

Remaining:

``` text
10,000 - 9,000
= 1,000 tokens
```

If another request needs 2,500 tokens:

``` text
9,000 + 2,500
= 11,500
```

The token limit is exceeded.

## Important distinction

``` text
RPM = Requests Per Minute

TPM = Tokens Per Minute
```

------------------------------------------------------------------------

# 11. Token Usage

LLM response metadata can contain token usage.

Example:

``` python
{
    "token_usage": {
        "completion_tokens": 685,
        "prompt_tokens": 43,
        "total_tokens": 728
    }
}
```

## Prompt Tokens

Tokens used by the input:

``` text
Prompt = 43 tokens
```

## Completion Tokens

Tokens generated by the model:

``` text
Completion = 685 tokens
```

## Total Tokens

``` text
43 + 685 = 728
```

Formula:

``` text
Total Tokens
=
Prompt Tokens
+
Completion Tokens
```

Token usage is important for:

-   Cost tracking
-   Rate-limit awareness
-   Prompt optimization
-   Monitoring model behavior

------------------------------------------------------------------------

# 12. Cost Optimization

LLM cost can increase when applications use:

-   Very large prompts
-   Large context
-   Long conversations
-   Unnecessarily long outputs
-   Expensive models
-   Duplicate API calls

## Cost optimization strategies

``` text
Reduce unnecessary prompt
        ↓
Reduce unnecessary output
        ↓
Manage context
        ↓
Avoid duplicate API calls
        ↓
Choose an appropriate model
```

### Example: Avoid duplicate calls

Bad pattern:

``` text
LLM call
 ↓
Prediction

LLM call again
 ↓
Category evaluation
```

Better:

``` text
LLM call
 ↓
Store prediction
 ↓
Reuse prediction
```

This reduces unnecessary API calls and token consumption.

------------------------------------------------------------------------

# 13. Model Selection

You compared different Groq models.

Example:

``` text
Model A:
llama-3.1-8b-instant

Model B:
llama-3.3-70b-versatile
```

Your experiment showed that different models can have different:

-   Token usage
-   Latency
-   Capability
-   Cost characteristics

Example:

``` text
Model A → 61 total tokens
Model B → 76 total tokens
```

## Model selection principle

A bigger model is not automatically the best model.

Consider:

``` text
Quality
+
Task complexity
+
Cost
+
Latency
```

For simple tasks such as:

-   Classification
-   Simple extraction
-   Basic transformation

a smaller/faster model may be sufficient.

More complex tasks may benefit from a more capable model.

------------------------------------------------------------------------

# 14. Latency Optimization

Latency is the time between starting a request and receiving the
response.

You measured latency during model comparison.

Example:

``` text
Latency: 0.5301 seconds
```

Another call:

``` text
Latency: 0.4395 seconds
```

Actual latency can vary because of:

-   Network conditions
-   Provider queueing
-   Model load
-   Prompt size
-   Output size

## Latency optimization techniques

``` text
Use appropriate model
        ↓
Reduce unnecessary prompt
        ↓
Reduce unnecessary output
        ↓
Use streaming
        ↓
Use async execution
        ↓
Parallelize independent calls
```

------------------------------------------------------------------------

# 15. Sequential vs Parallel Latency

Suppose:

``` text
Research = 3 seconds
News = 4 seconds
```

Sequential:

``` text
3 + 4 = approximately 7 seconds
```

Parallel:

``` text
max(3, 4) = approximately 4 seconds
```

Using:

``` python
results = await asyncio.gather(
    research_task(),
    news_task()
)
```

### Important

Parallelization is useful when tasks are independent.

If Task B requires Task A's result:

``` text
Task A
 ↓
Task B
```

they cannot simply be treated as independent parallel tasks.

------------------------------------------------------------------------

# 16. Grounding

Grounding means providing the LLM with reliable context/evidence and
asking it to answer based on that information.

Without grounding:

``` text
Question
 ↓
LLM
 ↓
Answer
```

With grounding:

``` text
Question
 +
Verified Context
 ↓
LLM
 ↓
Context-based Answer
```

Example context:

``` text
Our company provides 24 paid leaves per year.
Employees can carry forward up to 10 unused leaves.
```

Question:

``` text
How many paid leaves does the company provide?
```

Grounded answer:

``` text
The company provides 24 paid leaves per year.
```

------------------------------------------------------------------------

# 17. Grounded vs Ungrounded Responses

## Ungrounded

``` text
Question
 ↓
LLM
 ↓
Answer based on available model knowledge/inference
```

The model may not know company-specific information.

## Grounded

``` text
Question
 +
Verified Context
 ↓
LLM
 ↓
Answer based on provided context
```

The goal is to reduce unsupported generation.

### Safe fallback

A useful grounding instruction is:

``` text
Answer using only the provided context.

If the answer is not present,
say:
"I don't have enough information."
```

Important:

Grounding does not mathematically guarantee truth. It provides evidence
and constrains the answer to that evidence.

------------------------------------------------------------------------

# 18. Hallucination Mitigation

A hallucination occurs when an LLM generates unsupported or inaccurate
information.

Example:

``` text
Context:
Company provides 24 paid leaves.

Question:
How many paid leaves?

Correct:
24
```

If the model says:

``` text
30 paid leaves
```

that answer is unsupported by the provided context.

## Basic mitigation pattern

``` text
Question
 +
Trusted Context
 ↓
LLM
 ↓
Answer
```

If information is unavailable:

``` text
"I don't have enough information."
```

This pattern becomes especially important later when building RAG
systems.

------------------------------------------------------------------------

# 19. LLM Evaluation

Evaluation means systematically testing an LLM instead of judging its
output manually or by intuition.

Basic flow:

``` text
Test Dataset
     ↓
    LLM
     ↓
Prediction
     ↓
Expected vs Predicted
     ↓
Evaluation
```

Example:

``` text
Input:
I love this product.

Expected:
Positive

Predicted:
Positive

Result:
Correct
```

------------------------------------------------------------------------

# 20. Accuracy

Formula:

``` text
Accuracy =
Correct Predictions
-------------------- × 100
Total Predictions
```

Example:

``` text
9 / 10 × 100
= 90%
```

Your first evaluation produced:

``` text
Correct Predictions: 9/10
Accuracy: 90%
```

------------------------------------------------------------------------

# 21. Failure Analysis

Accuracy alone is not enough.

You found this failure:

``` text
Input:
The product is okay.

Expected:
Positive

Predicted:
Negative
```

Failure analysis asks:

-   Which input failed?
-   What was expected?
-   What did the model predict?
-   What category does the failure belong to?
-   Why might the model have failed?
-   How can the prompt/model/dataset be improved?

This turns a metric into an actionable engineering insight.

------------------------------------------------------------------------

# 22. Prompt V1 vs Prompt V2

You compared two prompts.

## Prompt V1

``` text
Accuracy = 90%
```

One known failure:

``` text
"The product is okay."
Expected → Positive
Predicted → Negative
```

## Prompt V2

You clarified the sentiment definitions and how satisfactory/okay
experiences should be classified.

Result:

``` text
Prompt V1 → 90%
Prompt V2 → 100%

Improvement → +10 percentage points
```

## Main lesson

Prompt quality should be measured using test cases and metrics rather
than intuition.

------------------------------------------------------------------------

# 23. Regression Testing

Regression testing checks whether a prompt/model change accidentally
breaks behavior that previously worked.

Flow:

``` text
Prompt V1
 ↓
Evaluation Dataset
 ↓
90%

Prompt V2
 ↓
Same Evaluation Dataset
 ↓
100%
```

If:

``` text
90% → 95%
```

then there is an improvement.

If:

``` text
90% → 70%
```

then:

``` text
Regression detected
```

## Core principle

Whenever you change:

-   Prompt
-   Model
-   System instructions
-   Output format
-   Context strategy

run the existing evaluation dataset again.

------------------------------------------------------------------------

# 24. Evaluation Dataset

You created a 15-case dataset containing:

``` text
5 Clear Positive
5 Clear Negative
5 Edge Cases
```

## Clear Positive examples

``` text
I love this product.
The service was excellent.
I am very happy with my purchase.
The experience was amazing.
I really enjoyed using this product.
```

## Clear Negative examples

``` text
This product is terrible.
I hate this service.
This was a disappointing experience.
I would never recommend this product.
The product completely failed to meet my expectations.
```

## Edge Cases

``` text
The product is okay.
It's fine, I guess.
Could be better.
It works, but nothing special.
Not bad, but I expected more.
```

------------------------------------------------------------------------

# 25. Edge Cases

This was one of the most important results of today's evaluation.

Overall:

``` text
12 / 15 = 80%
```

But category-wise:

``` text
Clear Positive → 5/5 = 100%
Clear Negative → 5/5 = 100%
Edge Cases     → 2/5 = 40%
```

The model was strong on obvious cases but weak on ambiguous/edge cases.

Failures included:

``` text
"The product is okay."           → Negative
"It's fine, I guess."            → Negative
"It works, but nothing special." → Negative
```

## Lesson

If you test only easy examples:

``` text
10/10 = 100%
```

you might incorrectly conclude that the model is perfect.

Adding edge cases exposes weaknesses.

------------------------------------------------------------------------

# 26. Category-wise Evaluation

Overall accuracy:

``` text
80%
```

is useful, but category-wise metrics give more information:

``` text
Clear Positive → 100%
Clear Negative → 100%
Edge Cases     → 40%
```

Therefore a strong evaluation should include:

``` text
Overall Metric
+
Category Metrics
+
Failure Analysis
```

------------------------------------------------------------------------

# 27. Evaluation Dataset Quality

A good evaluation dataset should contain representative examples.

Useful categories include:

``` text
Normal cases
+
Clear cases
+
Edge cases
+
Ambiguous cases
+
Failure-prone cases
+
Real-world examples
```

The goal is not simply to have many test cases. The test cases should
represent the situations the application will actually encounter.

------------------------------------------------------------------------

# 28. Production-Oriented LLM Architecture

The concepts covered today can be combined into a production-style flow:

``` text
                    USER
                      │
                      ↓
                Rate Limiter
                      │
                      ↓
                  LLM Call
                      │
          ┌───────────┴───────────┐
          ↓                       ↓
      Timeout                  Streaming
          │                       │
          └───────────┬───────────┘
                      ↓
                 LLM Response
                      │
                      ↓
                Validation
                      │
                      ↓
                Application
```

Reliability side:

``` text
LLM Request
    ↓
  Error?
 ┌──┴──┐
NO     YES
│       │
↓       ↓
Done   Retry
        ↓
Exponential
  Backoff
        ↓
   Still failing?
        ↓
     Fallback
```

Grounding/evaluation side:

``` text
Trusted Context
      ↓
     LLM
      ↓
Generated Response
      ↓
Validation / Evaluation
      ↓
Application
```

------------------------------------------------------------------------

# 29. Interview Answers

## How do you make an LLM application reliable?

A strong answer:

> I handle API exceptions, use timeouts, implement bounded retries with
> exponential backoff, respect request and token rate limits, validate
> outputs, monitor token usage and latency, and use fallbacks where
> appropriate.

## How do you evaluate an LLM?

> I create a representative evaluation dataset containing normal and
> edge cases, compare expected versus predicted outputs, calculate
> metrics such as accuracy, perform failure analysis, and run regression
> tests whenever the prompt or model changes.

## How do you reduce hallucinations?

> I ground the model with trusted context, constrain it to answer from
> the provided information, validate outputs where appropriate, and use
> a safe fallback when the required information is unavailable.

## How do you reduce LLM latency?

> I use an appropriate model, reduce unnecessary prompt and output
> tokens, use streaming for perceived latency, and execute independent
> LLM calls concurrently with async programming.

## How do you reduce LLM cost?

> I monitor prompt and completion tokens, avoid unnecessary API calls,
> keep context concise, reuse results where possible, and select the
> smallest model that can reliably perform the task.

------------------------------------------------------------------------

# 30. Today's Final Checklist

``` text
14 Streaming                 ✅
15 Async Basics              ✅
16 Async LLM                 ✅
17 Error Handling            ✅
18 Retry Strategy            ✅
19 Exponential Backoff       ✅
20 Timeout                   ✅
21 LLM Timeout               ✅
22 Rate Limits               ✅
23 Token Rate Limit          ✅
24 Token Usage               ✅
25 Cost Optimization         ✅
26 Model Selection           ✅
27 Latency Optimization      ✅
28 Grounding                 ✅
29 Grounding Comparison      ✅
30 LLM Evaluation            ✅
31 Regression Testing        ✅
32 Evaluation Dataset        ✅
```

------------------------------------------------------------------------

# 🏁 Overall Takeaway

``` text
LLM Fundamentals
       ↓
LLM Calls
       ↓
Streaming + Async
       ↓
Error Handling
       ↓
Retries + Backoff
       ↓
Timeouts
       ↓
Rate + Token Limits
       ↓
Token + Cost Optimization
       ↓
Model Selection
       ↓
Latency Optimization
       ↓
Grounding
       ↓
Hallucination Mitigation
       ↓
Evaluation
       ↓
Regression Testing
       ↓
Failure Analysis
       ↓
Evaluation Dataset
       ↓
✅ LLM FUNDAMENTALS COMPLETE
       ↓
🚀 LANGCHAIN
```

## Note on Guardrails

Output validation and guardrails were covered conceptually today. Their
deeper implementation will be done with **LangChain**, using structured
outputs, parsers, validation, retries, and production-oriented patterns.
