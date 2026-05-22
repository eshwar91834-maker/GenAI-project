# Meeting Minutes Generator

This project generates structured meeting minutes from raw meeting notes using OpenAI's GPT models.

## Features

- Converts unstructured meeting notes into organized meeting minutes
- Extracts agenda items, decisions made, action items, and next meeting details
- Built with Streamlit for an easy-to-use web interface
- Uses Pydantic for data validation and structured output

## Installation

1. Clone this repository if you get this from github, if you directly get the project you can ignore this step
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the root directory
2. Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

1. Start the Streamlit application:

```bash
streamlit run app.py
```

2. Enter your raw meeting notes in the text area
3. Click "Generate Meeting Minutes"
4. View the structured output including:
   - Summary
   - Agenda Items
   - Decisions Made
   - Action Items
   - Next Meeting Details

## Project Structure

- `app.py`: Main Streamlit application
- `summariser.py`: Handles the meeting minutes generation logic
- `prompts.py`: Contains the prompt template for the AI model
- `schema.py`: Defines the data structure for meeting minutes using Pydantic
- `requirements.txt`: Lists the Python dependencies

## Dependencies

- streamlit: Web application framework
- openai: OpenAI API client
- pydantic: Data validation and settings management
- python-dotenv: Environment variable management
- jinja2: Template engine for prompt rendering

## Notes

- The application uses the `gpt-4.1-mini` model by default
- Temperature is set to 0.2 for consistent, focused outputs
- Ensure you have a valid OpenAI API key with sufficient credits