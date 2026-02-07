# Tool Integrations Guide

FreeAIAPIKey.com works seamlessly with your favorite AI tools and frameworks. Just change the base URL to `https://freeaiapikey.com/v1` and use your FreeAIAPIKey.

---

## 📋 Quick Reference

| Tool | Configuration | Difficulty |
|------|---------------|------------|
| **n8n** | Base URL + API Key | ⭐ Easy |
| **Claude Desktop** | MCP config | ⭐ Easy |
| **Claude Code** | Environment variables | ⭐ Easy |
| **LangChain** | `openai_api_base` param | ⭐ Easy |
| **Vercel AI SDK** | Custom fetch | ⭐⭐ Medium |
| **Continue.dev** | Config JSON | ⭐ Easy |
| **Flowise** | Base URL setting | ⭐ Easy |
| **Dify** | API endpoint config | ⭐ Easy |
| **OpenWebUI** | Connection settings | ⭐ Easy |
| **LibreChat** | Custom endpoint | ⭐ Easy |

---

## 🔧 n8n (Workflow Automation)

### Setup
1. Open n8n workflow editor
2. Add an **OpenAI** node
3. Configure credentials:

```
Base URL: https://freeaiapikey.com/v1
API Key: your-freeaiapikey
```

### Screenshot
```
[OpenAI Node Configuration]
├─ Resource: Chat Message
├─ Operation: Create
├─ Model: gpt-4 (or claude-opus, gemini-pro, etc.)
├─ Credentials: FreeAIAPIKey
│   ├─ Base URL: https://freeaiapikey.com/v1
│   └─ API Key: sk-xxxxxxxx
```

### Example Workflow
```json
{
  "nodes": [
    {
      "parameters": {
        "model": "gpt-4",
        "options": {},
        "messages": {
          "values": [
            {
              "role": "user",
              "content": "={{ $json.input }}"
            }
          ]
        }
      },
      "id": "ai-chat",
      "name": "AI Chat",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "credentials": {
        "openAiApi": {
          "id": "freeaiapikey",
          "name": "FreeAIAPIKey"
        }
      }
    }
  ]
}
```

**Save**: 80-90% on your n8n AI workflow costs!

---

## 🤖 Claude Desktop (Anthropic's Desktop App)

### Setup with MCP (Model Context Protocol)

1. Open Claude Desktop settings
2. Navigate to **Developer** → **Config**
3. Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "freeai": {
      "command": "npx",
      "args": ["-y", "@anthropics-ai/mcp-openai"],
      "env": {
        "OPENAI_API_KEY": "your-freeaiapikey",
        "OPENAI_BASE_URL": "https://freeaiapikey.com/v1"
      }
    }
  }
}
```

### Alternative: Direct Configuration

If using a custom OpenAI-compatible endpoint:

```json
{
  "openai": {
    "api_key": "your-freeaiapikey",
    "base_url": "https://freeaiapikey.com/v1",
    "model": "gpt-4"
  }
}
```

### Using Claude Models

To use Claude models through FreeAIAPIKey:

```json
{
  "mcpServers": {
    "freeai-claude": {
      "command": "npx",
      "args": ["-y", "@anthropics-ai/mcp-freeai"],
      "env": {
        "FREEAI_API_KEY": "your-freeaiapikey",
        "FREEAI_BASE_URL": "https://freeaiapikey.com/v1",
        "DEFAULT_MODEL": "claude-opus"
      }
    }
  }
}
```

---

## 💻 Claude Code (CLI Tool)

### Environment Setup

Set environment variables before running Claude Code:

```bash
# Bash/Zsh
export OPENAI_API_KEY="your-freeaiapikey"
export OPENAI_BASE_URL="https://freeaiapikey.com/v1"

# Then run
claude-code
```

### Configuration File

Create `~/.claude-code/config.json`:

```json
{
  "openai": {
    "api_key": "your-freeaiapikey",
    "base_url": "https://freeaiapikey.com/v1",
    "default_model": "gpt-4"
  }
}
```

### Using Different Models

```bash
# Use Claude through FreeAIAPIKey
export DEFAULT_MODEL="claude-opus"
claude-code

# Use Gemini
export DEFAULT_MODEL="gemini-pro"
claude-code
```

---

## 🔗 LangChain

### Python

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Configure with FreeAIAPIKey
llm = ChatOpenAI(
    model="gpt-4",  # or "claude-opus", "gemini-pro", etc.
    openai_api_key="your-freeaiapikey",
    openai_api_base="https://freeaiapikey.com/v1",
    temperature=0.7
)

# Use in your chain
messages = [HumanMessage(content="Hello!")]
response = llm.invoke(messages)
print(response.content)
```

### With Streaming

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key="your-freeaiapikey",
    openai_api_base="https://freeaiapikey.com/v1",
    streaming=True
)

for chunk in llm.stream("Tell me a joke"):
    print(chunk.content, end="")
```

### JavaScript/TypeScript

```typescript
import { ChatOpenAI } from '@langchain/openai';

const model = new ChatOpenAI({
  modelName: 'gpt-4',
  openAIApiKey: 'your-freeaiapikey',
  configuration: {
    baseURL: 'https://freeaiapikey.com/v1',
  },
});

const response = await model.invoke('Hello!');
console.log(response.content);
```

### LangChain with Claude

```python
from langchain_openai import ChatOpenAI

claude = ChatOpenAI(
    model="claude-opus",
    openai_api_key="your-freeaiapikey",
    openai_api_base="https://freeaiapikey.com/v1"
)
```

---

## ▲ Vercel AI SDK

### Next.js App Router

```typescript
// app/api/chat/route.ts
import { OpenAIStream, StreamingTextResponse } from 'ai';

export async function POST(req: Request) {
  const { messages } = await req.json();

  const response = await fetch('https://freeaiapikey.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.FREEAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'gpt-4',
      messages,
      stream: true,
    }),
  });

  const stream = OpenAIStream(response);
  return new StreamingTextResponse(stream);
}
```

### Environment Variables

```env
# .env.local
FREEAI_API_KEY=your-freeaiapikey
```

### Using AI SDK with Custom Provider

```typescript
import { OpenAI } from 'ai';

const freeai = new OpenAI({
  apiKey: process.env.FREEAI_API_KEY,
  baseURL: 'https://freeaiapikey.com/v1',
});

export async function generateText(prompt: string) {
  const response = await freeai.chat.completions.create({
    model: 'gpt-4',
    messages: [{ role: 'user', content: prompt }],
  });
  
  return response.choices[0].message.content;
}
```

---

## 🔵 Continue.dev (AI Coding Assistant)

### Configuration

Edit `~/.continue/config.json`:

```json
{
  "models": [
    {
      "title": "FreeAI GPT-4",
      "provider": "openai",
      "model": "gpt-4",
      "apiKey": "your-freeaiapikey",
      "apiBase": "https://freeaiapikey.com/v1"
    },
    {
      "title": "FreeAI Claude",
      "provider": "openai",
      "model": "claude-opus",
      "apiKey": "your-freeaiapikey",
      "apiBase": "https://freeaiapikey.com/v1"
    },
    {
      "title": "FreeAI Gemini",
      "provider": "openai",
      "model": "gemini-pro",
      "apiKey": "your-freeaiapikey",
      "apiBase": "https://freeaiapikey.com/v1"
    }
  ],
  "tabAutocompleteModel": {
    "title": "FreeAI Sonnet",
    "provider": "openai",
    "model": "claude-sonnet",
    "apiKey": "your-freeaiapikey",
    "apiBase": "https://freeaiapikey.com/v1"
  }
}
```

### VS Code Settings

You can also configure through VS Code settings:

```json
{
  "continue.models": [
    {
      "title": "FreeAI GPT-4",
      "provider": "openai",
      "model": "gpt-4",
      "apiKey": "your-freeaiapikey",
      "apiBase": "https://freeaiapikey.com/v1"
    }
  ]
}
```

---

## 🌊 Flowise (Low-Code LLM Builder)

### Setup

1. Open Flowise canvas
2. Drag "ChatOpenAI" node
3. Configure:

```
Base Path: https://freeaiapikey.com/v1
OpenAI Api Key: your-freeaiapikey
Model Name: gpt-4 (or claude-opus, gemini-pro, etc.)
```

### Screenshot
```
[ChatOpenAI Node]
├─ Base Path: https://freeaiapikey.com/v1
├─ OpenAI Api Key: sk-xxxxxxxx
├─ Model Name: gpt-4
├─ Temperature: 0.7
└─ Max Tokens: 2000
```

---

## 🎨 Dify (LLM App Development Platform)

### Setup

1. Go to **Settings** → **Model Provider**
2. Select **OpenAI-API-compatible**
3. Configure:

```
Model Name: gpt-4
API Key: your-freeaiapikey
Endpoint URL: https://freeaiapikey.com/v1
```

### For Claude/Gemini Models

```
Model Name: claude-opus (or gemini-pro, deepseek-chat, etc.)
API Key: your-freeaiapikey
Endpoint URL: https://freeaiapikey.com/v1
```

---

## 💬 OpenWebUI (Self-Hosted Chat Interface)

### Admin Configuration

1. Go to **Admin Panel** → **Settings** → **Connections**
2. Add OpenAI API connection:

```
URL: https://freeaiapikey.com/v1
Key: your-freeaiapikey
```

3. Enable models:
   - gpt-4
   - claude-opus
   - claude-sonnet
   - gemini-pro
   - deepseek-chat
   - kimi-k2

### User Settings

Users can select any enabled model from the dropdown.

---

## 🗨️ LibreChat (Open Source ChatGPT Clone)

### Configuration

Edit `.env` file:

```env
# OpenAI (FreeAIAPIKey)
OPENAI_API_KEY=your-freeaiapikey
OPENAI_BASE_URL=https://freeaiapikey.com/v1
OPENAI_MODELS=gpt-4,gpt-3.5-turbo,claude-opus,claude-sonnet,gemini-pro
```

Or use `librechat.yaml`:

```yaml
endpoints:
  openAI:
    name: "FreeAIAPIKey"
    apiKey: "${FREEAI_API_KEY}"
    baseURL: "https://freeaiapikey.com/v1"
    models:
      default: ["gpt-4", "claude-opus", "gemini-pro"]
```

---

## 📊 Comparison: Tool Integration Difficulty

| Tool | Time to Setup | Cost Savings |
|------|---------------|--------------|
| n8n | 2 minutes | 80-90% |
| Claude Desktop | 5 minutes | 85% |
| Claude Code | 2 minutes | 85% |
| LangChain | 3 minutes | 80-90% |
| Vercel AI SDK | 5 minutes | 80-90% |
| Continue.dev | 3 minutes | 80-90% |
| Flowise | 2 minutes | 80-90% |
| Dify | 3 minutes | 80-90% |
| OpenWebUI | 5 minutes | 80-90% |
| LibreChat | 3 minutes | 80-90% |

---

## 🛠️ Custom Integrations

### Generic OpenAI-Compatible Setup

Any tool that supports OpenAI API format:

```
Base URL: https://freeaiapikey.com/v1
API Key: your-freeaiapikey
Model: gpt-4 (or any supported model)
```

### Testing Your Integration

```bash
# Test with curl
curl https://freeaiapikey.com/v1/chat/completions \
  -H "Authorization: Bearer your-freeaiapikey" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## 💡 Pro Tips

### 1. Model Selection
```
Use GPT-4 for: General tasks, reasoning
Use Claude Opus for: Complex analysis, coding
Use Claude Sonnet for: Fast responses, cost-efficiency
Use Gemini for: Multimodal tasks, long context
Use DeepSeek for: Code generation
Use Kimi for: Long documents
```

### 2. Cost Optimization
```
- Start with cheaper models (Sonnet, Gemini) for testing
- Use expensive models (Opus, GPT-4) for production
- Enable streaming for better UX
- Set token limits in your tools
```

### 3. Switching Models

Most tools let you change models instantly:
```
Model: gpt-4 → claude-opus → gemini-pro
Same API key, same base URL, just change model name!
```

---

## 🆘 Troubleshooting

### Common Issues

**"Invalid API key"**
- Check your key at https://freeaiapikey.com/dashboard
- Ensure no extra spaces
- Verify key is active

**"Model not found"**
- Use exact model names: `gpt-4`, `claude-opus`, `gemini-pro`
- Check available models: https://freeaiapikey.com/v1/models

**"Connection refused"**
- Verify base URL: `https://freeaiapikey.com/v1`
- Check internet connection
- Try with curl first

**"Rate limit exceeded"**
- FreeAIAPIKey has no rate limits
- Check if your tool has internal limits
- Contact support if issues persist

---

## 📝 Need Help?

- 🌐 Website: https://freeaiapikey.com
- 💬 GitHub Issues: Open an issue on this repo

---

**Ready to integrate?** Get your API key at [https://freeaiapikey.com](https://freeaiapikey.com) 🚀
