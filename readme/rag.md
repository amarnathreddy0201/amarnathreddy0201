# RAG Interview Questions and Answers (Basic to Advanced)

## Q1. What is RAG?

### Answer

RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with Large Language Models (LLMs). Instead of relying only on the model's training data, it retrieves relevant information from external sources and uses that context to generate accurate responses.

---

## Q2. Why do we need RAG?

### Answer

LLMs have limitations such as:

* Knowledge cutoffs
* Hallucinations
* Lack of access to private enterprise data

RAG solves these problems by providing real-time and domain-specific information during inference.

---

## Q3. What are the main components of a RAG pipeline?

### Answer

A typical RAG pipeline consists of:

1. Data Ingestion
2. Document Chunking
3. Embedding Generation
4. Vector Database
5. Retriever
6. Prompt Construction
7. LLM Generation

---

## Q4. What are embeddings?

### Answer

Embeddings are numerical vector representations of text that capture semantic meaning.

For example:

* "Car" and "Automobile" will have similar embeddings.
* Similar texts are located close together in vector space.

---

## Q5. What is a vector database?

### Answer

A vector database stores embeddings and performs similarity searches efficiently.

Examples:

* Pinecone
* ChromaDB
* Weaviate
* Milvus
* FAISS
* Qdrant

---

## Q6. What is chunking in RAG?

### Answer

Chunking is the process of splitting large documents into smaller pieces before generating embeddings.

Benefits:

* Improves retrieval accuracy
* Fits within token limits
* Reduces processing costs

---

## Q7. What chunking strategies have you used?

### Answer

Common chunking strategies include:

* Fixed-size chunking
* Recursive chunking
* Semantic chunking
* Hierarchical chunking

For production systems, semantic chunking often provides better retrieval quality because it preserves context.

---

## Q8. Why do RAG systems often perform well in demos but fail in production?

### Answer

RAG systems are usually tested on clean datasets and predictable questions.

In production:

* Users ask ambiguous questions
* Use different terminology
* Make spelling mistakes
* Require information from multiple documents

As a result, retrieval quality decreases and answer accuracy suffers.

---

## Q9. What is the most common reason for RAG failure in real-world applications?

### Answer

Poor retrieval quality.

If the correct documents are not retrieved, the LLM cannot generate accurate answers regardless of how powerful the model is.

Most production failures occur in retrieval rather than generation.

---

## Q10. How can chunking negatively impact RAG performance?

### Answer

Poor chunking can split related information across multiple chunks.

Example:

Chunk 1:
"Refunds are available."

Chunk 2:
"Refunds are only valid within 14 days."

If only Chunk 1 is retrieved, the generated answer becomes incorrect or incomplete.

---

## Q11. Why is embedding model selection important?

### Answer

Embedding models determine how text is represented in vector space.

Generic models may struggle with domain-specific terminology such as:

* Healthcare
* Finance
* Legal
* Manufacturing

Domain-specific embedding models often improve retrieval accuracy.

---

## Q12. What is Hybrid Search?

### Answer

Hybrid Search combines:

1. Dense Retrieval (Vector Search)
2. Sparse Retrieval (BM25 Keyword Search)

Benefits:

* Better recall
* Better precision
* Improved handling of exact keywords and semantic meaning

---

## Q13. What is BM25?

### Answer

BM25 is a keyword-based ranking algorithm used in information retrieval.

Unlike vector search, BM25 focuses on:

* Exact keyword matching
* Term frequency
* Document relevance

It is commonly used as part of hybrid search systems.

---

## Q14. What is reranking?

### Answer

Reranking is a second-stage retrieval process.

Workflow:

1. Retrieve Top 20 documents.
2. Apply a cross-encoder reranker.
3. Select the best Top 5 documents.
4. Pass them to the LLM.

This improves the quality of retrieved context.

---

## Q15. What is Top-K retrieval?

### Answer

Top-K retrieval determines how many documents are retrieved.

Example:

* Top-K = 5
* Five most relevant chunks are returned.

Trade-offs:

* Small K → Miss important information
* Large K → Introduce noise

---

## Q16. What is multi-hop retrieval?

### Answer

Multi-hop retrieval combines information from multiple documents to answer a query.

Example:
To answer a leave eligibility question, the system may need:

* Employee Policy
* Regional Compliance Policy
* Leave Rules Document

---

## Q17. What challenges do users introduce in production?

### Answer

Users often:

* Ask vague questions
* Use abbreviations
* Use synonyms
* Make spelling mistakes
* Ask multi-part questions

These make retrieval significantly harder than in testing environments.

---

## Q18. What are hallucinations in RAG systems?

### Answer

Hallucinations occur when the model generates information not supported by retrieved documents.

Causes:

* Missing context
* Poor retrieval
* Ambiguous prompts
* Model assumptions

---

## Q19. How do you reduce hallucinations?

### Answer

Common approaches include:

* Better retrieval
* Hybrid Search
* Reranking
* Grounded prompting
* Citations
* Confidence scoring
* Answer verification

---

## Q20. How do you evaluate a RAG system?

### Answer

### Retrieval Metrics

* Recall@K
* Precision@K
* MRR
* NDCG

### Generation Metrics

* Answer Accuracy
* Faithfulness
* Context Relevance
* User Satisfaction

Always evaluate using real user queries, not only synthetic datasets.

---

## Q21. How would you debug a failing RAG system?

### Answer

I would inspect each stage:

1. Was the correct document retrieved?
2. Was it ranked highly?
3. Was chunking effective?
4. Was the prompt constructed correctly?
5. Did the LLM understand the context?
6. Was the answer supported by evidence?

This helps isolate the root cause.

---

## Q22. What production improvements would you make to a basic RAG system?

### Answer

I would add:

* Hybrid Search
* Query Rewriting
* Metadata Filtering
* Semantic Chunking
* Cross-Encoder Reranking
* Multi-Query Retrieval
* Answer Validation
* Monitoring and Evaluation Pipelines

These improvements significantly increase accuracy and reliability.

---

## Q23. What is Query Expansion?

### Answer

Query expansion generates alternative versions of a user query to improve retrieval.

Example:

User Query:
"Vacation policy"

Expanded Queries:

* Leave policy
* Annual leave rules
* Employee leave guidelines

This increases recall.

---

## Q24. What is Metadata Filtering?

### Answer

Metadata filtering narrows retrieval using attributes such as:

* Department
* Region
* Date
* Document Type

Example:
Retrieve only HR documents from India.

This improves retrieval precision.

---

## Q25. Explain a real-world challenge you faced while implementing RAG.

### Answer

During development, our RAG system achieved excellent results on internal test datasets.

However, in production, users used terminology different from the documents. The retriever often missed relevant content.

To solve this, we implemented:

* Hybrid Search
* Query Expansion
* Cross-Encoder Reranking

These improvements significantly improved retrieval quality and user satisfaction.

---

## Q26. What is the biggest lesson you learned from implementing RAG?

### Answer

The biggest lesson is:

> Retrieval quality determines answer quality.

Even the most powerful LLM cannot provide correct answers if the relevant information is not retrieved.

Most production failures are retrieval failures rather than LLM failures.

---

## Q27. Difference Between Naive RAG, Advanced RAG, and Agentic RAG?

### Answer

| Type         | Description                                                    |
| ------------ | -------------------------------------------------------------- |
| Naive RAG    | Basic retrieval + generation                                   |
| Advanced RAG | Hybrid search, reranking, query rewriting                      |
| Agentic RAG  | Uses agents for planning, retrieval, validation, and reasoning |

Accuracy generally increases from Naive → Advanced → Agentic RAG.


## Q28. Overcoming Context Window Limitations in Large Language Models (LLMs)

### Overview

Large Language Models (LLMs) have a fixed **context window**, which limits the number of input tokens they can process in a single request. When documents, conversations, or codebases exceed this limit, several techniques can be used to effectively overcome or mitigate the constraint.

---

### 1. Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) retrieves only the most relevant information instead of sending the entire dataset to the LLM.

### Workflow

```
Documents
     │
Chunking
     │
Embeddings
     │
Vector Database
     │
User Query
     │
Query Embedding
     │
Similarity Search
     │
Top-k Relevant Chunks
     │
LLM
```

### Common Vector Databases

- FAISS
- Milvus
- Pinecone
- Chroma
- Weaviate
- Qdrant

### Advantages

- Handles millions of documents
- Reduces token usage
- Improves response quality
- Lower inference cost

---

### 2. Context Compression

Instead of passing the complete document, compress it into a smaller representation.

### Techniques

- Extractive Summarization
- Abstractive Summarization
- LLM-generated Summaries
- Token Pruning

### Example

```
100 Page Document

↓

3 Page Summary

↓

LLM
```

### Advantages

- Saves context space
- Faster inference
- Lower cost

---

### 3. Sliding Window

Split long text into overlapping chunks and process them sequentially.

```
Window 1 : [1 ---------------- 100]

Window 2 :          [80 ---------------- 180]

Window 3 :                    [160 ---------------- 260]
```

### Advantages

- Preserves continuity
- Suitable for long conversations
- Effective for large documents

---

### 4. Hierarchical Summarization

Summarize large documents recursively.

```
1000 Pages

↓

100 Summaries

↓

10 Summaries

↓

1 Final Summary

↓

LLM
```

### Applications

- Research Papers
- Books
- Reports
- Documentation

---

### 5. Memory-Augmented LLMs

Maintain different types of memory outside the context window.

```
                User Query
                     │
      ┌──────────────┴──────────────┐
      │                             │
 Short-Term Memory         Long-Term Memory
      │                             │
      └──────────────┬──────────────┘
                     │
              Vector Database
                     │
                    LLM
```

### Examples

- LangGraph Memory
- MemGPT
- Letta
- Zep

---

### 6. KV Cache (Key-Value Cache)

During autoregressive generation, previously computed attention keys and values are cached.

```
Prompt

↓

KV Cache

↓

Next Token

↓

Reuse Cached KV
```

### Benefits

- Faster inference
- Lower GPU computation
- Reduced latency

---

### 7. Prefix Cache / Prompt Cache

Reuse computation for common system prompts.

```
System Prompt

↓

Cached Once

↓

User A

↓

User B

↓

User C
```

### Use Cases

- Chatbots
- AI Assistants
- Shared Enterprise Prompts

---

### 8. Sparse Attention

Instead of every token attending to every other token, attention is restricted.

### Standard Attention

```
Every Token

↓

Every Other Token
```

### Sparse Attention

```
Token

↓

Nearby Tokens

↓

Important Tokens Only
```

### Models

- Longformer
- BigBird
- ETC

### Complexity

| Method | Complexity |
|----------|------------|
| Standard Attention | O(n²) |
| Sparse Attention | O(n) or O(n log n) |

---

### 9. FlashAttention

FlashAttention is an optimized attention algorithm designed for modern GPUs.

### Advantages

- Faster attention computation
- Lower GPU memory usage
- Enables longer context windows

### Applications

- Llama
- Mistral
- Gemma
- Qwen

---

### 10. State Space Models (SSMs)

Alternative architectures replace self-attention with state-space mechanisms.

### Examples

- Mamba
- RWKV

### Advantages

- Linear complexity
- Efficient long-sequence processing
- Lower memory usage

---

### 11. Chunk-and-Reason

Retrieve and reason over information incrementally.

```
Question

↓

Retrieve Chunk 1

↓

Reason

↓

Retrieve Chunk 2

↓

Reason

↓

Merge Results

↓

Answer
```

### Advantages

- Supports multi-hop reasoning
- Better handling of large knowledge bases

---

### 12. Agentic Retrieval

AI agents iteratively retrieve information as needed.

```
Question

↓

Search

↓

Reason

↓

Search Again

↓

Reason

↓

Final Answer
```

### Frameworks

- LangGraph
- LlamaIndex
- AutoGen
- CrewAI

---

### 13. Fine-Tuning

Store domain-specific knowledge within model weights instead of prompts.

### Suitable For

- Company Policies
- Domain Knowledge
- Specialized Tasks

### Not Suitable For

- Frequently changing information
- Dynamic databases

---

### 14. Long Context Models

Use models that natively support larger context windows.

### Examples

| Model | Context Window |
|---------|----------------|
| GPT-4.1 | Up to 1M Tokens |
| Gemini 2.5 | Up to 1M Tokens |
| Claude 4 | Up to 200K Tokens |
| Qwen Long | Large Context Support |

> **Note:** Even with long-context models, RAG is often preferred to reduce cost and improve retrieval precision.

---

### Comparison of Techniques

| Technique | Best Use Case | Advantages |
|------------|---------------|------------|
| RAG | Knowledge Retrieval | Scalable and accurate |
| Context Compression | Long Documents | Reduces token usage |
| Sliding Window | Long Conversations | Maintains continuity |
| Hierarchical Summarization | Books & Reports | Multi-level summarization |
| Memory-Augmented LLM | Chatbots | Persistent memory |
| KV Cache | Text Generation | Faster inference |
| Prefix Cache | Shared Prompts | Avoids redundant computation |
| Sparse Attention | Long Sequences | Lower computational complexity |
| FlashAttention | GPU Optimization | Faster attention computation |
| State Space Models | Very Long Context | Linear scaling |
| Chunk-and-Reason | Multi-hop QA | Better reasoning |
| Agentic Retrieval | Autonomous Agents | Dynamic information retrieval |
| Fine-Tuning | Domain Expertise | Stores knowledge in model |
| Long Context Models | Large Inputs | Supports massive context windows |

---

### Recommended Learning Path

For engineers working in **LLMs**, **Vision-Language Models (VLMs)**, or **Generative AI**, the following progression is recommended:

1. Retrieval-Augmented Generation (RAG)
2. Hybrid Search & Reranking
3. Context Compression
4. KV Cache & Prefix Cache
5. FlashAttention
6. Sparse Attention
7. Agentic RAG
8. Long Context Models
9. State Space Models (Mamba, RWKV)

---

### Conclusion

There is no single solution to overcome context window limitations. Modern LLM systems combine multiple techniques such as **RAG**, **context compression**, **memory augmentation**, **efficient attention mechanisms**, and **long-context models** to build scalable, efficient, and high-performing AI applications.

The optimal strategy depends on the application requirements, available computational resources, latency constraints, and the size of the knowledge base.


## Q29. Maintaining Context in Large Language Models (LLMs)

### Overview

Large Language Models (LLMs) have a fixed context window, meaning they can only process a limited number of input tokens at once. To build conversational AI, assistants, coding copilots, and enterprise applications, maintaining context across multiple interactions is essential.

This document explains the most common techniques used to preserve context in LLM applications.

---

### 1. Conversation History

The simplest way to maintain context is by sending previous conversation messages along with the current user query.

### Example

```
System:
You are an AI assistant.

User:
What is Machine Learning?

Assistant:
Machine Learning is...

User:
Explain supervised learning.
```

The LLM understands that the second question refers to the previous discussion.

### Advantages

- Easy to implement
- Maintains conversational flow

### Limitations

- Context grows continuously
- Eventually exceeds the model's context window

---

### 2. Sliding Context Window

Instead of sending the entire conversation history, keep only the most recent interactions.

### Example

```
Conversation

Message 1
Message 2
...
Message 20

↓

Keep only

Message 15
Message 16
Message 17
Message 18
Message 19
Message 20
```

### Advantages

- Constant memory usage
- Faster inference

### Limitations

- Older information is forgotten

---

### 3. Conversation Summarization

Summarize older parts of the conversation and replace them with a concise summary.

### Workflow

```
Conversation

↓

Summarizer

↓

Conversation Summary

↓

Current Conversation

↓

LLM
```

### Example

Instead of

```
100 conversation messages
```

Store

```
Summary:
"The user is building a RAG chatbot using LangChain."
```

### Advantages

- Preserves important information
- Saves tokens

---

### 4. Memory Buffer

Store all previous interactions in memory.

```
User

↓

Memory Buffer

↓

LLM
```

### Suitable For

- Short conversations
- Small chatbots

### Limitation

Memory size increases continuously.

---

### 5. Buffer Window Memory

Store only the last **N** interactions.

Example

```
Memory Size = 5

Message 96
Message 97
Message 98
Message 99
Message 100
```

Older messages are discarded.

---

### 6. Summary Memory

Combine summarization with conversation history.

```
Conversation

↓

Summarize Older Messages

↓

Conversation Summary

+

Recent Messages

↓

LLM
```

This provides both long-term understanding and recent context.

---

### 7. Vector Memory (Semantic Memory)

Instead of storing messages sequentially, convert them into embeddings and store them in a vector database.

### Workflow

```
Conversation

↓

Embeddings

↓

Vector Database

↓

Similarity Search

↓

Relevant Memories

↓

LLM
```

### Vector Databases

- FAISS
- Chroma
- Pinecone
- Weaviate
- Milvus
- Qdrant

### Advantages

- Retrieves only relevant memories
- Scales to millions of interactions

---

### 8. Knowledge Graph Memory

Represent entities and relationships as a graph.

### Example

```
User

↓

Lives in Bangalore

↓

Works at ABC

↓

Interested in LLMs
```

When the user asks:

```
Suggest AI meetups near me.
```

The system retrieves:

- Bangalore
- AI Interest

instead of the full conversation.

### Advantages

- Structured memory
- Better reasoning

---

### 9. Retrieval-Augmented Memory (RAG)

Combine conversation history with external knowledge.

```
User Query

↓

Retrieve Documents

↓

Retrieve Conversation Memory

↓

Combine

↓

LLM
```

### Advantages

- Personal context
- External knowledge
- Accurate responses

---

### 10. Long-Term Memory

Store important user information permanently.

### Example

```
User Preferences

↓

Database

↓

Retrieve When Needed

↓

LLM
```

Examples

- Preferred programming language
- Favorite framework
- Name
- Time zone
- Learning goals

### Applications

- AI assistants
- Customer support
- Personalized tutoring

---

### 11. KV Cache

During text generation, cache the attention key-value pairs.

```
Prompt

↓

KV Cache

↓

Next Token

↓

Reuse Cache
```

### Advantages

- Faster inference
- Reduced computation

> **Note:** KV Cache accelerates generation but does **not** preserve conversational memory across sessions.

---

### 12. Prefix Cache

Cache the shared system prompt or instruction.

```
System Prompt

↓

Cache Once

↓

User Prompt

↓

LLM
```

### Advantages

- Faster response
- Reduced computation
- Lower latency

---

### 13. Session-Based Memory

Maintain context only during a user's active session.

```
Session Start

↓

Conversation

↓

Memory

↓

Session End

↓

Delete Memory
```

Used in

- Chatbots
- Customer support
- Web applications

---

### 14. Persistent Memory

Store important information in a database.

```
User

↓

Database

↓

Retrieve

↓

LLM
```

Technologies

- PostgreSQL
- MongoDB
- Redis
- SQLite

---

### 15. Agent Memory

Modern AI agents maintain multiple memory types.

```
                 User Query
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Short-Term Memory          Long-Term Memory
        │                           │
        └─────────────┬─────────────┘
                      │
               Tool Memory
                      │
              Retrieved Documents
                      │
                     LLM
```

Frameworks

- LangGraph
- AutoGen
- CrewAI
- Letta
- MemGPT

---

### Best Practices

### Keep Recent Messages

Always include the most recent conversation.

---

### Summarize Older Conversations

Replace long histories with concise summaries.

---

### Retrieve Relevant Memories

Use semantic search instead of loading everything.

---

### Store User Preferences Separately

Keep long-term preferences in a database rather than the prompt.

---

### Use RAG

Retrieve both:

- Relevant documents
- Relevant conversation history

---

### Use Memory Hierarchy

```
Current Conversation
        │
        ▼
Short-Term Memory
        │
        ▼
Conversation Summary
        │
        ▼
Vector Memory
        │
        ▼
Long-Term Database
```

---

### Comparison

| Technique | Best For | Scalability |
|------------|----------|-------------|
| Conversation History | Simple Chatbots | ⭐⭐ |
| Sliding Window | Recent Context | ⭐⭐⭐ |
| Summary Memory | Long Conversations | ⭐⭐⭐⭐ |
| Vector Memory | Semantic Retrieval | ⭐⭐⭐⭐⭐ |
| Knowledge Graph | Structured Facts | ⭐⭐⭐⭐ |
| RAG Memory | Enterprise AI | ⭐⭐⭐⭐⭐ |
| Session Memory | Temporary Chats | ⭐⭐⭐ |
| Persistent Memory | Personalized AI | ⭐⭐⭐⭐⭐ |
| Agent Memory | Autonomous Agents | ⭐⭐⭐⭐⭐ |

---

### Recommended Architecture

```
                  User Query
                       │
                       ▼
            Recent Conversation
                       │
                       ▼
          Conversation Summary
                       │
                       ▼
          Vector Memory Retrieval
                       │
                       ▼
        Long-Term User Preferences
                       │
                       ▼
        External Knowledge (RAG)
                       │
                       ▼
             Prompt Construction
                       │
                       ▼
                     LLM
                       │
                       ▼
                  Final Response
```

---

### Conclusion

Maintaining context in LLMs requires combining multiple strategies rather than relying solely on the model's context window. A production-ready system typically integrates **recent conversation history**, **conversation summaries**, **semantic memory (vector databases)**, **persistent user preferences**, and **RAG**. This layered approach enables scalable, personalized, and context-aware AI applications while staying within the model's token limits.


## Q30) Small Language Model (SLM) Hyperparameters

### Overview

Hyperparameters are configuration settings that control how a Small Language Model (SLM) is trained, fine-tuned, or used for inference. Choosing the right hyperparameters significantly impacts model performance, training stability, memory usage, and inference speed.

---

### 1. Learning Rate

Controls how much the model weights are updated after each optimization step.

**Formula**

\[
W_{new} = W_{old} - \eta \nabla L
\]

Where:
- **η** = Learning rate
- **L** = Loss

### Typical Values

| Model Size | Learning Rate |
|------------|---------------|
| Fine-tuning | 1e-5 – 5e-5 |
| LoRA | 1e-4 – 3e-4 |
| QLoRA | 2e-4 |
| Pretraining | 1e-4 – 1e-3 |

---

### 2. Batch Size

Number of training samples processed before updating model weights.

```
Batch Size = 32

Input

Sample 1
Sample 2
...
Sample 32

↓

Forward Pass

↓

Backward Pass

↓

Weight Update
```

### Effects

Large Batch
- Faster training
- Higher GPU memory usage
- More stable gradients

Small Batch
- Less memory
- Noisier gradients
- Better generalization in some cases

Typical Values

```
1
2
4
8
16
32
64
```

---

### 3. Epochs

One complete pass over the training dataset.

```
Dataset

↓

Epoch 1

↓

Epoch 2

↓

Epoch 3
```

Typical

- Fine-tuning: 1–5
- Pretraining: Hundreds or thousands

---

### 4. Sequence Length (Context Length)

Maximum number of tokens processed in one input.

Examples

```
512 Tokens

1024 Tokens

2048 Tokens

4096 Tokens

8192 Tokens

32768 Tokens
```

Longer context

Pros
- More context
- Better reasoning

Cons
- Higher memory usage
- Slower training

---

### 5. Optimizer

Updates model parameters during training.

Common Optimizers

- Adam
- AdamW
- SGD
- Adafactor
- Lion

Most LLM fine-tuning uses

```
AdamW
```

---

### 6. Weight Decay

Regularization to prevent overfitting.

Typical Values

```
0

0.01

0.05

0.1
```

---

### 7. Warmup Steps

Gradually increase the learning rate at the beginning of training.

```
Learning Rate

      ________
     /
    /
___/

Training Steps
```

Typical

```
3%

5%

10%
```

of total training steps.

---

### 8. Gradient Accumulation

Simulates a larger batch size without increasing GPU memory usage.

Example

```
Mini Batch = 4

Gradient Accumulation = 8

Effective Batch

4 × 8 = 32
```

---

### 9. Gradient Clipping

Limits gradient magnitude to prevent exploding gradients.

Typical

```
1.0
```

---

### 10. Dropout

Randomly disables neurons during training.

```
Neuron

↓

Dropped (Probability = p)
```

Typical Values

```
0.1

0.2

0.3
```

---

### 11. Maximum Training Steps

Stop training after a fixed number of optimizer updates.

Example

```
1000 Steps

5000 Steps

10000 Steps
```

---

### 12. Scheduler

Controls how the learning rate changes during training.

Common Schedulers

- Linear
- Cosine
- Cosine with Restarts
- Polynomial
- Constant

Most Common

```
Cosine

Linear
```

---

### 13. Precision

Controls numerical precision during training.

| Precision | Memory | Speed |
|------------|--------|-------|
| FP32 | High | Slow |
| FP16 | Medium | Fast |
| BF16 | Medium | Fast |
| INT8 | Low | Very Fast |
| INT4 | Very Low | Fast |

---

### 14. LoRA Hyperparameters

If using LoRA fine-tuning:

### Rank (r)

```
4

8

16

32

64
```

### Alpha

```
16

32

64
```

### Dropout

```
0.05

0.1
```

Target Modules

```
q_proj

k_proj

v_proj

o_proj
```

---

### 15. QLoRA Hyperparameters

Common Configuration

```
Quantization

4-bit

NF4

Double Quantization

Enabled

Compute Type

BF16
```

---

### 16. Generation Hyperparameters (Inference)

### Temperature

Controls randomness.

| Value | Behavior |
|---------|----------|
| 0.0 | Deterministic |
| 0.2 | Low randomness |
| 0.7 | Balanced |
| 1.0 | Creative |
| >1.2 | Highly random |

---

### Top-k Sampling

Choose the next token from the top **k** most probable tokens.

Typical

```
20

40

50

100
```

---

### Top-p (Nucleus Sampling)

Choose tokens until cumulative probability reaches **p**.

Typical

```
0.8

0.9

0.95
```

---

### Repetition Penalty

Reduces repeated words or phrases.

Typical

```
1.05

1.1

1.2
```

---

### Max New Tokens

Maximum number of tokens generated.

Examples

```
128

256

512

1024
```

---

### Beam Search

Number of candidate sequences explored during decoding.

Typical

```
1 (Greedy)

4

8
```

---

### Early Stopping

Stop generation when an EOS (End-of-Sequence) token is produced.

```
True

False
```

---

### Common Hyperparameters for Fine-Tuning

| Hyperparameter | Typical Value |
|----------------|---------------|
| Learning Rate | 2e-5 |
| Batch Size | 8 |
| Epochs | 3 |
| Weight Decay | 0.01 |
| Warmup Ratio | 0.03 |
| Gradient Clipping | 1.0 |
| Optimizer | AdamW |
| Scheduler | Cosine |
| Precision | BF16 / FP16 |
| Sequence Length | 2048 |
| Gradient Accumulation | 4 |

---

### Common Hyperparameters for LoRA

| Hyperparameter | Typical Value |
|----------------|---------------|
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Learning Rate | 2e-4 |
| Batch Size | 8 |
| Epochs | 3 |

---

### Common Hyperparameters for Inference

| Hyperparameter | Typical Value |
|----------------|---------------|
| Temperature | 0.7 |
| Top-k | 50 |
| Top-p | 0.95 |
| Repetition Penalty | 1.1 |
| Max New Tokens | 512 |
| Beam Size | 1–4 |

---

### Best Practices

- Use **AdamW** optimizer for most fine-tuning tasks.
- Start with a **low learning rate (1e-5–5e-5)** for full fine-tuning and **2e-4** for LoRA/QLoRA.
- Enable **warmup** (3–10%) to stabilize training.
- Use **gradient accumulation** when GPU memory is limited.
- Prefer **BF16** (if supported) or **FP16** for efficient training.
- Set **temperature = 0.7**, **top-p = 0.95**, and **top-k = 50** for balanced text generation.
- Monitor validation loss and use **early stopping** to avoid overfitting.

---

### Conclusion

Hyperparameters determine the efficiency, stability, and quality of SLM training and inference. Careful tuning of parameters such as **learning rate**, **batch size**, **optimizer**, **sequence length**, **precision**, and **generation settings** is essential for achieving optimal performance while balancing computational cost.
