# Student Notes MCP Server

A simple Model Context Protocol (MCP) server that allows an AI client to save and search student study notes.

## What it does

The server provides two MCP tools:

### 1. `add_note`

Saves a study note to a local `notes.txt` file.

Inputs:
- `title` — the title of the note
- `content` — the study note content

### 2. `search_notes`

Searches the saved study notes.

Input:
- `query` — the word or phrase to search for

## Validation and safety

The server validates all inputs before changing stored data.

It:
- Rejects empty titles, content, and search queries.
- Limits note titles to 100 characters.
- Limits note content to 2000 characters.
- Rejects line breaks in titles and content.
- Only stores notes in its own local `notes.txt` file.
- Does not accept arbitrary file paths.
- Does not execute system commands.
- Does not delete or modify unrelated files.

## Requirements

- Python 3.10 or newer
- MCP Python package

## Installation

Open a terminal in the project folder and run:

```bash
py -m pip install "mcp[cli]"