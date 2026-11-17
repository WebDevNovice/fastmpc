from fastmcp import FastMCP

mcp = FastMCP("Gemini MCP Starter")


@mcp.tool(annotations={"readOnlyHint": True})
def hello(name: str) -> str:
    """Return a greeting to verify that the MCP connection works."""
    return f"Hello, {name}! Your MCP connector is working."
