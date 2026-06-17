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
