# Juniorkpabitey Bot - AI-Powered Q&A Application

## Overview
The **Juniorkpabitey Bot** is a conversational AI application designed to assist users by providing insightful answers to their questions. It leverages `LangChain` for prompt handling and integrates with the `OpenAI` or `Groq` API for language model processing.

## Features
- **Dynamic Model Selection**: Choose from a variety of pre-trained language models.
- **Customizable Parameters**:
  - **Temperature**: Adjust the randomness of responses.
  - **Max Tokens**: Control the maximum length of responses.
- **Streamlit-Powered UI**: A user-friendly interface for seamless interaction.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Juniorkpabitey-Bot.git
cd Juniorkpabitey-Bot 
```

 ### 2. Create a .env file for the environment variable
```bash
langchain_api_key=your_langchain_api_key
groq_api_key=your_groq_api_key
```
### 3. RUn the application
```bash
streamlit run app.py
```

## Usage

- **Launch the application using Streamlit.**
- **Use the sidebar to:**
    - **Select your preferred language model.**
    - **Adjust the temperature and max token parameters.**
- **Enter your question in the input field, and view the AI's response below.**




