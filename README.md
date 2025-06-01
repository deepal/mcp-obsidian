# MCP Server for Obsidian

MCP server to interact with Obsidian via the Local REST API community plugin.

<a href="https://glama.ai/mcp/servers/3wko1bhuek"><img width="380" height="200" src="https://glama.ai/mcp/servers/3wko1bhuek/badge" alt="server for Obsidian MCP server" /></a>

---

## 1. Project Introduction

This project provides an MCP server that enables programmatic interaction with your Obsidian vault using the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin. It exposes a set of tools for file management, content manipulation, and search within your vault, making it easy to automate workflows or integrate with other systems.

---

## 2. Prerequisites & Installation

### Prerequisites
- **Obsidian App** with the [Local REST API plugin](https://github.com/coddingtonbear/obsidian-local-rest-api) installed and enabled.
- **API Key** from the plugin settings.
- (Optional) [Docker Desktop](https://www.docker.com/products/docker-desktop/) for containerized runs.

### Installation

#### Obsidian REST API
1. Install the [Obsidian Local REST API plugin](https://github.com/coddingtonbear/obsidian-local-rest-api) in your Obsidian app.
2. Enable the plugin and copy the API key from its settings.

#### Claude Desktop (Optional)
- On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

---

## 3. Configuration

You can run the server either directly on your host or via Docker.

### Direct Run (using `uvx`)
```json
{
  "Obsidian": {
    "command": "uvx",
    "args": [
      "mcp-obsidian"
    ],
    "env": {
      "OBSIDIAN_API_KEY": "<your_api_key_here>",
      "OBSIDIAN_HOST": "<your_obsidian_host>"
    }
  }
}
```

### Docker Desktop (Recommended)
```json
{
  "mcpServers": {
    "Obsidian": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "OBSIDIAN_API_KEY",
        "-e",
        "OBSIDIAN_HOST",
        "mcp-obsidian-docker"
      ],
      "env": {
        "OBSIDIAN_API_KEY": "<your_api_key_here>",
        "OBSIDIAN_HOST": "host.docker.internal"
      }
    }
  }
}
```

#### Environment Variables
| Variable | Description |
| --- | --- |
| `OBSIDIAN_HOST` | The host where Obsidian API is running (typically the same host the Obsidian App is running). If you are running on Docker Desktop, use `host.docker.internal`. |
| `OBSIDIAN_API_KEY` | The API key for the Obsidian instance. You can get it from Obsidian Local REST API plugin settings. |

---

## 4. Available Tools

The server implements the following tools to interact with Obsidian:

- `obsidian_list_files_in_vault`: Lists all files and directories in the root directory of your Obsidian vault.
- `obsidian_list_files_in_dir`: Lists all files and directories that exist in a specific Obsidian directory.
- `obsidian_get_file_contents`: Return the content of a single file in your vault.
- `obsidian_simple_search`: Simple search for documents matching a specified text query across all files in the vault.
- `obsidian_patch_content`: Insert content into an existing note relative to a heading, block reference, or frontmatter field.
- `obsidian_append_content`: Append content to a new or existing file in the vault.
- `obsidian_delete_file`: Delete a file or directory from the vault.
- `obsidian_complex_search`: Complex search for documents using a JsonLogic query. Supports standard JsonLogic operators plus 'glob' and 'regexp' for pattern matching. Use this tool for advanced queries, e.g. for all documents with certain tags.
- `obsidian_batch_get_file_contents`: Return the contents of multiple files in your vault, concatenated with headers.
- `obsidian_get_periodic_note`: Get current periodic note for the specified period (daily, weekly, monthly, quarterly, yearly).
- `obsidian_get_recent_periodic_notes`: Get most recent periodic notes for the specified period type, with options for limit and including content.
- `obsidian_get_recent_changes`: Get recently modified files in the vault, with options for limit and days.

---

## 5. Example Prompts

It's good to first instruct Claude to use Obsidian. Then it will always call the tool. Example prompts:

- Get the contents of the last architecture call note and summarize them
- Search for all files where Azure CosmosDb is mentioned and quickly explain to me the context in which it is mentioned
- Summarize the last meeting notes and put them into a new note 'summary meeting.md'. Add an introduction so that I can send it via email.

---

## 6. Development & Debugging

### Building
To prepare the package for distribution:
```bash
uv sync
```

### Debugging
Since MCP servers run over stdio, debugging can be challenging. For the best debugging experience, we strongly recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

You can launch the MCP Inspector via [`npm`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) with this command:

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/mcp-obsidian run mcp-obsidian
```

Upon launching, the Inspector will display a URL that you can access in your browser to begin debugging.

You can also watch the server logs with this command:

```bash
tail -n 20 -f ~/Library/Logs/Claude/mcp-server-mcp-obsidian.log
```

---

## 7. References & Links
- [Obsidian Local REST API plugin](https://github.com/coddingtonbear/obsidian-local-rest-api)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
