# Precision RAG: Prompt Tuning For Building Enterprise RAG Systems

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
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
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. **Set Up Virtual Environment**

   ```sh
      python3 -m venv .venv
   . .venv/bin/activate
   ```

3. **Install Requirements**
   ```sh
   pip install -r requirements.txt
   ```
4. **Install Requirements**
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

## Code Structure

    ├── backend
    │   ├── main.py               # API entry point
    │   ├── controller
    │   └── service
    ├── data
    │   ├── data       		  # Raw data files
    │   └──...
    ├── frontend
    │   ├──
    │   ├──
    │   └──
    ├── requirements.txt          # Python dependencies
    ├── README.md                 # Project documentation
    └── ...

### License

This project is licensed under the MIT License. See the LICENSE file for details.
