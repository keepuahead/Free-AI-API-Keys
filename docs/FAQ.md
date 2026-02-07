# Frequently Asked Questions (FAQ)

Common questions about FreeAIAPIKey.com and affordable AI API access.

---

## 💰 Pricing & Billing

### How is FreeAIAPIKey so much cheaper?

We're a **team of developers** building for the community, not a profit-maximizing corporation. Our mission is to make AI accessible to everyone.

**How we keep prices low:**

1. **Community-First Mission** - We're non-profit focused on impact, not profit margins
2. **Bulk Purchasing Power** - We negotiate enterprise-level rates and pass savings to you
3. **Smart Cache System** - Intelligent caching reduces redundant API calls by 40-60%
4. **Efficient Infrastructure** - Optimized routing and minimal overhead
5. **Developer Community Support** - Donations and community contributions help us maintain low costs
6. **Lean Operations** - No corporate bloat, just developers helping developers

You get the **same premium models** at prices that **make sense for indie hackers and startups**.

---

### Is there a free tier?

**Yes!** You get **$2 in free credit** when you sign up. No credit card required.

**$2 lasts a LONG time because we're so cheap:**
- ~8,000 GPT-5 input tokens
- ~1,000 GPT-5 output tokens
- ~3,333 Claude Sonnet messages
- ~10,000 DeepSeek code completions
- Testing all our supported models multiple times
- Building a small prototype completely free

---

### Do I need a credit card?

**Not to start!**

- Sign up: No credit card required
- Use $2 free credit: No credit card required
- Add more funds: Credit card required

You only need a card when you want to add funds beyond the free $2.

---

### What's the pricing after the free credit?

**Pay-as-you-go** with no subscriptions or minimums.

Example pricing (per 1M tokens):
- GPT-5: $0.25 input / $2 output (80% off OpenAI)
- Claude Opus 4.5: $1 input / $5 output (80% off Anthropic)
- Claude Sonnet 4.5: $0.60 input / $3 output (80% off Anthropic)
- Gemini 3: $0.40 input / $2.50 output (80% off Google)
- DeepSeek V3.2: $0.20 input / $0.30 output (60-67% off)
- Kimi K2.5: $0.25 input / $1 output (71-72% off)

[Full pricing details →](../MODEL_PRICING.md)

---

### Are there any hidden fees?

**Absolutely not.**

What you see is what you pay:
- ✅ No setup fees
- ✅ No monthly fees
- ✅ No minimum spend
- ✅ No overage fees
- ✅ No API call fees

Just simple per-token pricing.

---

### Can I set spending limits?

**Yes!** Set daily, weekly, or monthly spending limits in your dashboard to control costs.

---

## 🔧 Technical

### Do I need to change my code?

**Almost nothing! Just change the URL:**

```python
# Before (OpenAI)
base_url = "https://api.openai.com/v1"

# After (FreeAIAPIKey - 80% cheaper!)
base_url = "https://freeaiapikey.com/v1"
```

Everything else stays exactly the same.

---

### Is this reliable for production?

**Yes!**

- **99.9% uptime SLA**
- Redundant systems and failover
- Many startups run production workloads
- Real-time status monitoring

---

### What about rate limits?

**No rate limits!**

Unlike other providers, we don't throttle your usage. Scale as much as you need.

Fair use policy applies (no abuse), but you won't hit arbitrary limits.

---

### Which models are supported?

Current models:
- ✅ GPT-5 (OpenAI)
- ✅ Claude Opus 4.5 (Anthropic)
- ✅ Claude Sonnet 4.5 (Anthropic)
- ✅ Gemini 3 (Google)
- ✅ DeepSeek V3.2 (DeepSeek)
- ✅ Kimi K2.5 (Moonshot AI)

[View all models →](https://freeaiapikey.com/models)

---

### Do you support streaming?

**Yes!** Full streaming support with Server-Sent Events (SSE).

```python
response = client.chat.completions.create(
    model="gpt-5",
    messages=messages,
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="")
```

---

### Do you support function calling?

**Yes!** Function calling (tools) works across all supported models.

```python
response = client.chat.completions.create(
    model="gpt-5",
    messages=messages,
    functions=[{
        "name": "get_weather",
        "parameters": {...}
    }],
    function_call="auto"
)
```

---

### What about embeddings?

**Coming soon!** We're adding embedding models to our lineup.

For now, you can use FreeAIAPIKey for chat/completions and keep your existing embedding provider.

---

### Do you support image generation?

**Not yet**, but it's on our roadmap (DALL-E, Midjourney, Stable Diffusion).

---

### Can I use this with LangChain/LlamaIndex/etc?

**Yes!** Any tool that works with OpenAI's API works with us.

Just point it to our base URL:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-5",
    openai_api_key="your-freeai-key",
    openai_api_base="https://freeaiapikey.com/v1"
)
```

[See all integrations →](./integrations.md)

---

### What tools are compatible?

Compatible with:
- ✅ n8n
- ✅ Claude Desktop / Claude Code
- ✅ LangChain
- ✅ LlamaIndex
- ✅ Vercel AI SDK
- ✅ Continue.dev
- ✅ Flowise
- ✅ Dify
- ✅ OpenWebUI
- ✅ LibreChat
- ✅ Any OpenAI-compatible tool

**Just change the base URL to `https://freeaiapikey.com/v1`**

---

## 🔒 Privacy & Security

### Is my data private?

**Absolutely!**

- ✅ **No long-term data storage** - Prompts and responses aren't retained
- ✅ **Temporary caching only** - Minutes, not days
- ✅ **No training on your data** - Your data is never used to train models
- ✅ **No third-party sharing** - Your data stays yours
- ✅ **GDPR compliant** - Privacy by design

---

### Do you store my API calls?

**No.** We don't log or store:
- Your prompts
- AI responses
- Conversation history
- Request content

Only temporary caching for performance (cleared within minutes).

---

### Is this secure for sensitive data?

**Yes.** Many users process sensitive data through our API.

However, if you have specific compliance requirements (HIPAA, SOC 2, etc.), contact us to discuss enterprise options.

---

## 🚀 Getting Started

### How do I get started?

**3 simple steps:**

1. Sign up at [freeaiapikey.com](https://freeaiapikey.com) (30 seconds)
2. Copy your API key ($2 free credit included)
3. **Change your base URL to `https://freeaiapikey.com/v1`**

That's it!

---

### How long does setup take?

**30 seconds or less.**

Just change the base URL in your code. No other changes needed.

---

### Can I test before committing?

**Yes!** Use your $2 free credit to test all models risk-free. No credit card required.

With our low prices, $2 lasts a long time - thousands of API calls!

---

## 💼 Business & Enterprise

### Is this suitable for enterprises?

**Yes!** Many companies use us in production.

For enterprise needs:
- Custom pricing for high volume ($10K+/month)
- Dedicated support
- SLA guarantees
- Compliance discussions

Contact us through our website for enterprise inquiries.

---

### Can I get an invoice?

**Yes!** We provide invoices for all payments. Available in your dashboard.

---

### Do you offer custom pricing?

For usage over $10,000/month, contact us for custom rates through our website.

---

### Is there a team/organization plan?

**Coming soon!** Team accounts with:
- Shared billing
- Usage analytics
- Member management
- API key permissions

---

## 🆚 Comparison

### How do you compare to OpenAI Direct?

| Feature | FreeAIAPIKey | OpenAI Direct |
|---------|--------------|---------------|
| Price | 80% cheaper | Full price |
| Models | 6 providers | OpenAI only |
| Rate Limits | None | Yes |
| Free Tier | $2 | Trial only |
| Credit Card | Not required | Required |
| Setup | Just change URL | Standard |

[Full comparison →](../comparisons/provider-comparison.md)

---

### How do you compare to Anthropic Direct?

| Feature | FreeAIAPIKey | Anthropic Direct |
|---------|--------------|------------------|
| Price | 80% cheaper for Claude | Full price |
| Flexibility | Switch models instantly | Claude only |
| Rate Limits | None | Yes |
| Setup | Just change URL | Standard |

---

### Why not just use the official APIs?

**Three reasons:**

1. **Cost** - Save 80% (hundreds or thousands per year)
2. **Convenience** - One key for all models, just change URL
3. **No limits** - Scale without throttling

Unless you need official enterprise support, FreeAIAPIKey is better.

---

## 🐛 Troubleshooting

### "Invalid API key"

**Solutions:**
1. Check your key at https://freeaiapikey.com/dashboard
2. Ensure no extra spaces in the key
3. Verify the key is active (not revoked)
4. Make sure you're using `Authorization: Bearer YOUR_KEY`

---

### "Model not found"

**Solutions:**
1. Use exact model names: `gpt-5`, `claude-opus-4.5`, `gemini-3`
2. Check available models at https://freeaiapikey.com/v1/models
3. Verify your spelling (case-sensitive)

---

### "Connection refused"

**Solutions:**
1. Check base URL is exactly: `https://freeaiapikey.com/v1`
2. Verify internet connection
3. Try with curl first to isolate the issue

---

### Slow responses?

**Possible causes:**
1. Model is temporarily overloaded (rare)
2. Large request size
3. Network latency

**Solutions:**
1. Try a different model
2. Use streaming for better UX
3. Check your internet connection

---

### Different response quality?

You should get identical responses to direct API calls. If you notice differences:

1. Check you're using the same model version
2. Verify temperature and other parameters match
3. Contact us through our website if issues persist

---

## 🌍 General

### Who built this?

**A team of developers** who were tired of paying $200-300/month for AI APIs while building side projects.

Built with ❤️ by developers, for developers. We're a community-focused team making AI accessible to everyone.

---

### Is this a scam? Too good to be true?

**Not a scam!** Here's why it's legitimate:

- ✅ Thousands of developers use us daily
- ✅ $2 free credit to test risk-free (no card needed)
- ✅ Transparent pricing
- ✅ Real cost savings (try the calculator!)
- ✅ Just change your URL - that's it!

The low prices come from volume aggregation and smart caching, not from cutting corners.

---

### How do you make money?

We take a small margin from the volume discounts we negotiate. You still save 80%, and we make enough to keep the lights on.

It's a win-win.

---

### What's your uptime?

**99.9%** with redundant systems.

Check real-time status: https://status.freeaiapikey.com

---

### Can I invest/partner?

Not currently seeking investment. For partnerships, contact us through our website.

---

### How can I support the project?

**Ways to help:**
- ⭐ Star our GitHub repo
- 🐦 Share on Twitter
- 💬 Tell fellow developers
- 📝 Write about your experience

---

## 📝 Still Have Questions?

**Contact us:**
- 🌐 Website: https://freeaiapikey.com
- 💬 GitHub Issues: Open an issue on this repo

---

**Ready to save 80% on AI APIs?**

👉 [Get $2 Free Credit →](https://freeaiapikey.com)

Just change your URL and start saving instantly!

---

*Last updated: February 2025*
