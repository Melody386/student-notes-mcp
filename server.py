from mcp.server import MCPServer

mcp = MCPServer("Student Notes Server")


@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Save a study note."""

    title = title.strip()
    content = content.strip()

    if not title:
        raise ValueError("Title cannot be empty.")

    if not content:
        raise ValueError("Content cannot be empty.")

    if len(title) > 100:
        raise ValueError("Title cannot be longer than 100 characters.")

    if len(content) > 2000:
        raise ValueError("Content cannot be longer than 2000 characters.")

    if "\n" in title or "\r" in title:
        raise ValueError("Title cannot contain line breaks.")

    if "\n" in content or "\r" in content:
        raise ValueError("Content cannot contain line breaks.")

    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{title} | {content}\n")

    return f"Note '{title}' saved successfully."


@mcp.tool()
def search_notes(query: str) -> str:
    """Search saved study notes."""

    query = query.strip()

    if not query:
        raise ValueError("Search query cannot be empty.")

    if len(query) > 100:
        raise ValueError("Search query cannot be longer than 100 characters.")

    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()
    except FileNotFoundError:
        return "No notes have been saved yet."

    matches = []

    for note in notes:
        if query.lower() in note.lower():
            matches.append(note.strip())

    if not matches:
        return f"No notes found for '{query}'."

    return "\n".join(matches)


if __name__ == "__main__":
    mcp.run()