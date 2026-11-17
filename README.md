# Gemini MCP Starter

This server exposes one read-only tool, `hello(name)`. It does not call an API or need a key.

1. In FastMCP Gateway, select **Hosted > Build and deploy** and choose this repository. Use `main.py:mcp` as the entrypoint. Keep authentication enabled and restrict access to your account.
2. Copy the deployed HTTPS URL ending in `/mcp`. Add it in [Gemini Developer Mode](https://gemini.google.com/devmode). Leave the optional client ID and secret blank on your first attempt so Gemini can try dynamic client registration.
3. Select the connector in Gemini and send: "Call the `hello` tool with the name `Gemini`." The tool should return `Hello, Gemini! Your MCP connector is working.` Check the event log to confirm the tool actually ran.

Only after this works, add a tool for your API. Store the API key in the hosting service's secret settings, not in the repository or Gemini.
