from mcp.server import MCPServer

mcp = MCPServer("Student Notes Server")


@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Save a study note."""
    if not title.strip():
        raise ValueError("Title cannot be empty.")

    if not content.strip():
        raise ValueError("Content cannot be empty.")

    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{title.strip()} | {content.strip()}\n")

    return f"Note '{title.strip()}' saved successfully."


@mcp.tool()
def search_notes(query: str) -> str:
    """Search saved study notes."""
    if not query.strip():
        raise ValueError("Search query cannot be empty.")

    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()
    except FileNotFoundError:
        return "No notes have been saved yet."

    matches = []

    for note in notes:
        if query.strip().lower() in note.lower():
            matches.append(note.strip())

    if not matches:
        return f"No notes found for '{query.strip()}'."

    return "\n".join(matches)


if __name__ == "__main__":
    mcp.run()