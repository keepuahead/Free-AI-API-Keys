# Migration Guide: From OpenAI to FreeAIAPIKey

Switch from OpenAI's expensive API to FreeAIAPIKey's 80-90% cheaper alternative in just **5 minutes**.

---

## 🎯 What Changes?

**Only ONE thing:** The `base_url`

Everything else stays exactly the same:
- ✅ Same SDK
- ✅ Same code
- ✅ Same response format
- ✅ Same models (GPT-4, GPT-5)
- ✅ Same features (streaming, function calling)

---

## 🚀 Quick Migration (30 seconds)

### Before (OpenAI - Expensive 💸)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-openai-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Cost**: $1.25/1M tokens (input) + $10/1M tokens (output)

### After (FreeAIAPIKey - 80% Cheaper 🎉)

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-freeai-key",
    base_url="https://freeaiapikey.com/v1"  # ← Only this line changed!
)

response = client.chat.completions.create(
    model="gpt-5",  # or gpt-4
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Cost**: $0.25/1M tokens (input) + $2/1M tokens (output) = **80% savings!**

---

## 📋 Step-by-Step Migration

### Step 1: Get Your FreeAIAPIKey (1 minute)

1. Visit [https://freeaiapikey.com](https://freeaiapikey.com)
2. Sign up (30 seconds)
3. Copy your API key
4. You now have **$2 free credit** to test

### Step 2: Update Environment Variables (1 minute)

**Before:**
```bash
export OPENAI_API_KEY="sk-openai-xxx"
```

**After:**
```bash
export OPENAI_API_KEY="sk-freeai-xxx"  # Your FreeAIAPIKey
export OPENAI_BASE_URL="https://freeaiapikey.com/v1"
```

### Step 3: Update Your Code (2 minutes)

Find all instances of OpenAI client initialization and add `base_url`:

**Python:**
```python
# Find this pattern in your code:
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Replace with:
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://freeaiapikey.com/v1")
)
```

**JavaScript:**
```javascript
// Find this:
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Replace with:
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: process.env.OPENAI_BASE_URL || 'https://freeaiapikey.com/v1'
});
```

### Step 4: Test (1 minute)

```bash
python your_script.py
```

Everything should work exactly the same!

### Step 5: Deploy (Optional)

Update your production environment variables and deploy. No code changes needed beyond Step 3.

---

## 🔧 Language-Specific Migrations

### Python

**Before:**
```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="")
```

**After:**
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://freeaiapikey.com/v1")
)

# Everything else stays the SAME!
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="")
```

### JavaScript / Node.js

**Before:**
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

const response = await client.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: 'Hello!' }]
});
```

**After:**
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: process.env.OPENAI_BASE_URL || 'https://freeaiapikey.com/v1'
});

// Everything else stays the SAME!
const response = await client.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: 'Hello!' }]
});
```

### TypeScript

**Before:**
```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!
});
```

**After:**
```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!,
  baseURL: process.env.OPENAI_BASE_URL || 'https://freeaiapikey.com/v1'
});
```

### cURL

**Before:**
```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

**After:**
```bash
curl https://freeaiapikey.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

---

## 🔄 Advanced Features Migration

### Streaming

**No changes needed!** Streaming works exactly the same:

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    stream=True  # This works exactly the same
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="")
```

### Function Calling

**No changes needed!** Function calling works exactly the same:

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    functions=[{
        "name": "get_weather",
        "description": "Get weather for a city",
        "parameters": {...}
    }],
    function_call="auto"
)
```

### Vision / Image Input

**No changes needed!** Vision capabilities work exactly the same:

```python
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {"type": "image_url", "image_url": {"url": "..."}}
        ]
    }]
)
```

### Embeddings

**Note**: For embeddings, use our dedicated embedding models or keep OpenAI for embeddings while using FreeAIAPIKey for chat.

---

## 🛠️ Framework Migrations

### LangChain

**Before:**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
```

**After:**
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base="https://freeaiapikey.com/v1"
)
```

### LlamaIndex

**Before:**
```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    model="gpt-4",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

**After:**
```python
from llama_index.llms.openai import OpenAI

llm = OpenAI(
    model="gpt-4",
    api_key=os.getenv("OPENAI_API_KEY"),
    api_base="https://freeaiapikey.com/v1"
)
```

### Vercel AI SDK

**Before:**
```javascript
import { OpenAIStream } from 'ai';

const response = await fetch('https://api.openai.com/v1/chat/completions', {...});
```

**After:**
```javascript
import { OpenAIStream } from 'ai';

const response = await fetch('https://freeaiapikey.com/v1/chat/completions', {
  headers: {
    'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
  },
  // ... rest same
});
```

---

## 💰 Cost Comparison After Migration

### Scenario: Startup with 10M tokens/month (GPT-5)

| Metric | OpenAI Direct | FreeAIAPIKey | Savings |
|--------|---------------|--------------|---------|
| **Monthly Cost** | $56.25 | $11.25 | **$45.00** |
| **Annual Cost** | $675.00 | $135.00 | **$540.00** |
| **Savings** | - | - | **80%** |

### Scenario: Indie Developer with 1M tokens/month (GPT-5)

| Metric | OpenAI Direct | FreeAIAPIKey | Savings |
|--------|---------------|--------------|---------|
| **Monthly Cost** | $5.63 | $1.13 | **$4.50** |
| **Annual Cost** | $67.50 | $13.50 | **$54.00** |
| **Savings** | - | - | **80%** |

**Calculate your savings**: [Cost Calculator](../tools/cost_calculator.py)

---

## ✅ Migration Checklist

- [ ] Sign up at [freeaiapikey.com](https://freeaiapikey.com)
- [ ] Copy your new API key
- [ ] Update environment variables
- [ ] Add `base_url` to OpenAI client initialization
- [ ] Test with a simple request
- [ ] Test streaming (if used)
- [ ] Test function calling (if used)
- [ ] Update production environment
- [ ] Deploy
- [ ] Monitor first week
- [ ] Celebrate your savings! 🎉

---

## 🆘 Troubleshooting

### "Invalid API key"
- Ensure you're using your FreeAIAPIKey (starts with different prefix)
- Check at https://freeaiapikey.com/dashboard
- Verify no extra spaces

### "Connection error"
- Check base URL is exactly: `https://freeaiapikey.com/v1`
- Verify internet connection
- Try with curl first

### "Model not found"
- Use exact model names: `gpt-4`, `gpt-3.5-turbo`
- Check available models at https://freeaiapikey.com/v1/models

### Different response format?
- Should be identical to OpenAI
- If differences found, report to support@freeaiapikey.com

---

## 🎁 Bonus: Try Other Models

Now that you're using FreeAIAPIKey, try other models with the same code:

```python
# Try Claude (85% cheaper than Anthropic direct)
response = client.chat.completions.create(
    model="claude-opus",
    messages=messages
)

# Try Gemini (80% cheaper than Google direct)
response = client.chat.completions.create(
    model="gemini-pro",
    messages=messages
)

# Try DeepSeek (90% cheaper)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages
)
```

**One key, all models!** 🔑

---

## 📞 Need Help?

- 💬 [Discord Community](https://discord.gg/freeaiapikey)
- 📧 support@freeaiapikey.com
- 📖 [Full Documentation](https://freeaiapikey.com/docs)

---

**Start saving 90% today**: [https://freeaiapikey.com](https://freeaiapikey.com) 🚀
