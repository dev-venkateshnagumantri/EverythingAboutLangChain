# Everything About LangChain

A hands-on learning workspace for exploring LangChain, agents, tools, chains, Pydantic-based structured workflows, and Agentic AI.

The examples are organized as Jupyter notebooks so you can run concepts step by step and experiment with prompts, models, tools, and streaming responses.

## Topics Covered

### LangChain Fundamentals

- OpenAI SDK usage
- LangChain basics and chat models
- Messages and message roles
- Pydantic models and structured outputs
- Sequential and conditional chains
- Parallel and parallel-conditional chains

### Agentic AI

- ReAct-style agents
- Built-in and community tools
- Custom tools
- Email automation tool
- Wikipedia and web search tools
- Agent streaming
- Multi-tool AI workflows

## Project Structure

```text
EverythingAboutLangChain/
├── env-proto                 # Example environment variable template
├── pyproject.toml            # Project metadata and dependencies
├── src/
│   ├── lang_chain/           # LangChain and OpenAI SDK notebooks
│   │   ├── 1_OpenAI_SDK.ipynb
│   │   ├── 2_LangChain_Basics.ipynb
│   │   ├── 3_LangChain_Messages.ipynb
│   │   ├── 4_LangChain_Pydantic.ipynb
│   │   ├── 5_Chains.ipynb
│   │   ├── 6_ParallelChains.ipynb
│   │   └── 7_ParallelConditionalChains.ipynb
│   └── AgenticAI/            # Agent examples and utilities
│       ├── 1_Basics.ipynb    # building and integrating tools
│       ├── 2_tennis.ipynb
│       └── utils/
│           └── mail_helper.py
└── README.md
```

## Prerequisites

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) recommended for environment and dependency management
- Jupyter Notebook or JupyterLab
- API credentials for the integrations used in each notebook

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd EverythingAboutLangChain
```

Create the environment and install dependencies:

```bash
uv sync
```

## Environment Variables

Copy `env-proto` to `.env`, then add the credentials required by the notebooks:

```dotenv
OPENAI_API_KEY=
LIVETENNISAPI_KEY=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=
```

### Variable Reference

| Variable | Used for |
| --- | --- |
| `OPENAI_API_KEY` | OpenAI and LangChain chat model access |
| `LIVETENNISAPI_KEY` | Live tennis API integrations |
| `EMAIL_HOST` | SMTP server host |
| `EMAIL_PORT` | SMTP server port, usually `587` |
| `EMAIL_HOST_USER` | SMTP account username |
| `EMAIL_HOST_PASSWORD` | SMTP account password or app password |
| `DEFAULT_FROM_EMAIL` | Sender address used by the email helper |

Keep `.env` private and never commit credentials to source control.

## Running the Notebooks

Start Jupyter:

```bash
jupyter notebook
```

Open notebooks under:

- `src/lang_chain/` for LangChain fundamentals
- `src/AgenticAI/` for tools and agent examples

Run the cells from top to bottom. Some notebooks require an active API key or external service.

## Example: Custom Email Tool

`src/AgenticAI/utils/mail_helper.py` provides an SMTP-backed email helper used by an agent tool:

```python
from langchain.tools import tool
from utils.mail_helper import send_email


@tool
def email_tool(subject: str, to_mail: str, body: str) -> str:
    """Send an email to a recipient."""
    return send_email(subject=subject, to_mail=to_mail, body=body)
```

Configure the SMTP variables in `.env` before running email examples.

## Recommended Learning Order

1. `src/lang_chain/1_OpenAI_SDK.ipynb`
2. `src/lang_chain/2_LangChain_Basics.ipynb`
3. `src/lang_chain/3_LangChain_Messages.ipynb`
4. `src/lang_chain/4_LangChain_Pydantic.ipynb`
5. `src/lang_chain/5_Chains.ipynb`
6. `src/lang_chain/6_ParallelChains.ipynb`
7. `src/lang_chain/7_ParallelConditionalChains.ipynb`
8. `src/AgenticAI/1_Basics.ipynb`
9. `src/AgenticAI/2_tennis.ipynb`

## Key Dependencies

- LangChain
- LangChain OpenAI
- LangChain Anthropic
- LangChain Community
- LangChain Tavily
- Live Tennis integration
- OpenAI SDK
- Wikipedia
- DuckDuckGo Search
- Jupyter
- python-dotenv

## Notes

- Model names and provider APIs may change over time. If a notebook fails due to an unavailable model, replace it with a model currently enabled for your account.
- API usage may incur provider charges.
- External search and live-data tools require network access and valid API credentials.
- The email helper uses SMTP and may require an app-specific password depending on the provider.

## Contributing

Suggestions and improvements are welcome:

1. Create a feature branch.
2. Add or improve a notebook or utility.
3. Verify that it runs from a clean environment.
4. Do not commit API keys or generated secrets.
5. Open a pull request with a short summary of the examples added.

<p align='center'><b>Made with ❤ by Venkatesh Nagumantri</b></p>
