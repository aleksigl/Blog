# Blog

A lightweight, Python-powered blogging platform designed for simplicity and ease of use.

The blog will be running locally (`http://localhost:5000`) or under this address:

https://40ed2e9b-bb7c-412c-b158-0bd23747b106-00-1juahspjtdwdg.picard.replit.dev/


## Features

- **Dynamic Content Management**: Create and manage blog posts effortlessly.
- **SQLite Backend**: Utilizes a local SQLite database for storing blog entries.
- **Minimalistic Design**: Focused on content with a clean and straightforward layout.
- **Configuration File**: Centralized settings in `config.py` for easy customization.

## Installation

### Prerequisites

Ensure you have Python 3.7+ installed. It's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  (or use `venv\Scripts\activate` on Windows)
```

## Project Structure

```
Blog/
│
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── blog_entries.db     # SQLite database for blog posts
├── blog/               # Blog-related modules
│   ├── __init__.py     # Marks the directory as a Python package
│   ├── forms.py        # Form handling for blog posts
│   ├── models.py       # Database models for blog entries
│   ├── routes.py       # Routing logic for blog pages
│   └── templates/      # Mako templates for rendering views
│       └── ...         # Template files
└── __pycache__/        # Compiled Python files
```
