# Precision RAG: Prompt Tuning For Building Enterprise RAG Systems

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [License](#license)

## Project Overview

The project is an AI-driven solution that optimizes the use of Language Models (LLMs) across various industries by automating prompt generation, evaluation, and ranking using Retrieval-Augmented Generation (RAG). It streamlines the creation of effective prompts, ensures comprehensive test case generation for reliable performance, and ranks prompts for optimal outcomes, enhancing decision-making, operational efficiency, and customer experience.

## Tech Stack

- **Programming Languages:** Python,
- **API Frameworks:** Flask

## Setup Instructions

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository**
   ```sh
   git clone git@github.com:jadmassu/PromptBuilder-for-RAG.git
   cd PromptBuilder-for-RAG
   ```
2. **Set Up Virtual Environment**

   ```sh
      python3 -m venv .venv
   . .venv/bin/activate
   ```

3. **Install Backend Requirements**

   ```sh
   pip install -r requirements.txt
   ```

4. **Install Frontend Modules**
   ```sh
   npm i
   ```
5. **SetUP environments**
   ```sh
   OPENAI_API_KEY = Your_open_api_key
   PATH_TO_PDF = Your_file_Path
   ```

## API Development

**Run Flask Application**

```sh
cd backend
flask --app main run
```

## Frontend Development

**Run Next Application**

```sh
cd frontend
npm run dev
```

**Open with your browser to see the result.**

[http://localhost:3000](http://localhost:3000)

## Project Structure

    ├── backend
    │   ├── main.py               # API entry point
    │   ├── controller            # All the controllers
    │   └── service               # All service that interact with outside
    ├── data
    │   ├── data       		      # Raw data files
    │   └──...
    ├── frontend
    │   ├── public               # Static resource
    │   ├── src                  # Contains all the components pages and styles
    │   └── ...
    ├── requirements.txt          # Python dependencies
    ├── README.md                 # Project documentation
    └── ...

## Key Features

* Load & Chunk Data: Efficiently load and chunk large datasets for streamlined processing.
* Embedding & Storage: Generate and store embeddings in ChromaDB for fast and scalable retrieval.
* Query with Simplicity Search: Perform efficient queries using Simplarity search to find relevant information quickly.
* Evaluate & Retrieve Prompts: Assess and retrieve prompts to improve the accuracy and relevance of responses.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
