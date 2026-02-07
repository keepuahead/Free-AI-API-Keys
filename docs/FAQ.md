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

This is enough for:
- ~6,000 GPT-4 requests (150 tokens each)
- ~20,000 GPT-3.5 requests
- Testing all our supported models
- Building a small prototype

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
- GPT-4: $3 (input) / $6 (output) - **90% off OpenAI**
- Claude Opus: $2.25 / $11.25 - **85% off Anthropic**
- Claude Sonnet: $0.45 / $2.25 - **85% off Anthropic**
- Gemini Pro: $0.70 / $2.10 - **80% off Google**

[Full pricing →](https://freeaiapikey.com/pricing)

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

**Almost nothing!**

Just change the `base_url`:

```python
# Before (OpenAI)
client = OpenAI(api_key="sk-...")

# After (FreeAIAPIKey)
client = OpenAI(
    api_key="sk-...",
    base_url="https://freeaiapikey.com/v1"  # ← Only this!
)
```

Everything else stays exactly the same.

---

### Is this reliable for production?

**Yes!**

- **99.9% uptime SLA**
- Redundant systems and failover
- Many startups run production workloads
- Real-time status monitoring
- Automatic provider fallback

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
- ✅ DeepSeek v3.2 (DeepSeek)
- ✅ Kimi K2.5 (Moonshot AI)

[View all models →](https://freeaiapikey.com/models)

---

### Do you support streaming?

**Yes!** Full streaming support with Server-Sent Events (SSE).

```python
response = client.chat.completions.create(
    model="gpt-4",
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
    model="gpt-4",
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
    model="gpt-4",
    openai_api_key="your-freeai-key",
    openai_api_base="https://freeaiapikey.com/v1"
)
```

[See all integrations →](../docs/integrations.md)

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

### What about data residency?

Currently, data is processed in US-based data centers. EU regions coming soon.

---

## 🚀 Getting Started

### How do I get started?

**3 simple steps:**

1. Sign up at [freeaiapikey.com](https://freeaiapikey.com) (30 seconds)
2. Copy your API key ($2 free credit included)
3. Change your base URL to `https://freeaiapikey.com/v1`

[Quick start guide →](https://freeaiapikey.com/docs/quickstart)

---

### How long does setup take?

**5 minutes or less.**

Most developers are making API calls within 2 minutes of signing up.

---

### Can I test before committing?

**Yes!** Use your $2 free credit to test all models risk-free. No credit card required.

---

### What if it doesn't work for me?

You lose nothing! 

- No credit card required to test
- Only $2 of free credit at risk
- Cancel anytime
- No contracts or commitments

---

## 💼 Business & Enterprise

### Is this suitable for enterprises?

**Yes!** Many companies use us in production.

For enterprise needs:
- Custom pricing for high volume ($10K+/month)
- Dedicated support
- SLA guarantees
- Compliance discussions

Contact us: enterprise@freeaiapikey.com

---

### Can I get an invoice?

**Yes!** We provide invoices for all payments. Available in your dashboard.

---

### Do you offer custom pricing?

For usage over $10,000/month, contact us for custom rates: enterprise@freeaiapikey.com

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
| Price | 80-90% cheaper | Full price |
| Models | 6+ providers | OpenAI only |
| Rate Limits | None | Yes |
| Free Credit | $2 | Trial only |
| Credit Card | Not required | Required |

[Full comparison →](./comparisons/provider-comparison.md)

---

### How do you compare to OpenRouter?

| Feature | FreeAIAPIKey | OpenRouter |
|---------|--------------|------------|
| Price | 80-90% off | ~10% off |
| Models | 6 major models | 100+ models |
| Rate Limits | None | Tiered |
| Complexity | Simple | More complex |

Choose FreeAIAPIKey for cost savings on major models. Choose OpenRouter for variety.

---

### Why not just use the official APIs?

**Three reasons:**

1. **Cost** - Save 80-90% (thousands per year)
2. **Convenience** - One key for all models
3. **No limits** - Scale without throttling

Unless you need official enterprise support, FreeAIAPIKey is better.

---

## 🐛 Troubleshooting

### "Invalid API key" error

**Solutions:**
1. Check your key at https://freeaiapikey.com/dashboard
2. Ensure no extra spaces in the key
3. Verify the key is active (not revoked)
4. Make sure you're using `Authorization: Bearer YOUR_KEY`

---

### "Model not found" error

**Solutions:**
1. Use exact model names: `gpt-4`, `claude-opus`, `gemini-pro`
2. Check available models: https://freeaiapikey.com/v1/models
3. Verify your spelling (case-sensitive)

---

### "Connection refused" error

**Solutions:**
1. Check base URL is exactly: `https://freeaiapikey.com/v1`
2. Verify internet connection
3. Try with curl first to isolate the issue
4. Check if you need to configure a proxy

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
4. Contact us if persistent

---

### Different response quality?

You should get identical responses to direct API calls. If you notice differences:

1. Check you're using the same model version
2. Verify temperature and other parameters match
3. Report to support@freeaiapikey.com

---

## 🤝 Community & Support

### How do I get help?

**Three ways:**

1. 💬 [Discord Community](https://discord.gg/freeaiapikey) - Fastest response
2. 📧 Email: support@freeaiapikey.com - 24-48 hour response
3. 📖 [Documentation](https://freeaiapikey.com/docs) - Self-service

---

### Is there phone support?

Not currently. We're a small team of developers. Best support is through Discord or email.

---

### Can I request features?

**Yes!** Join our Discord and post in #feature-requests. We build what the community asks for.

---

### How do I report bugs?

1. Discord: Post in #bug-reports
2. GitHub: Open an issue
3. Email: support@freeaiapikey.com

Include:
- Error message
- Code snippet
- Model used
- Timestamp

---

## 🌍 General

### Who built this?

**A team of developers** who were tired of paying $200-300/month for AI APIs while building side projects.

Built with ❤️ by developers, for developers. We're a community-focused team making AI accessible to everyone.

---

### Is this a scam? Too good to be true?

**Not a scam!** Here's why it's legitimate:

- ✅ Thousands of developers use us daily
- ✅ $2 free credit to test risk-free
- ✅ No credit card required to try
- ✅ Transparent pricing
- ✅ Active community
- ✅ Real cost savings (try the calculator!)

The low prices come from volume aggregation and smart routing, not from cutting corners.

---

### How do you make money?

We take a small margin from the volume discounts we negotiate. You still save 80-90%, and we make enough to keep the lights on.

It's a win-win.

---

### What's your uptime?

**99.9%** with redundant systems.

Check real-time status: https://status.freeaiapikey.com

---

### Where are you located?

Operated globally with infrastructure in multiple regions. Founder is based in [Location].

---

### Can I invest/partner?

Not currently seeking investment. For partnerships, email: partnerships@freeaiapikey.com

---

### How can I support the project?

**Ways to help:**
- ⭐ Star our GitHub repo
- 🐦 Share on Twitter
- 💬 Tell fellow developers
- 📝 Write about your experience
- 🤝 Help others in Discord

---

## 📝 Still Have Questions?

**Ask us:**
- 💬 [Discord](https://discord.gg/freeaiapikey)
- 📧 support@freeaiapikey.com
- 🐦 [@freeaiapikey](https://twitter.com/freeaiapikey)

**Or try it risk-free:**
👉 [Get $2 Free →](https://freeaiapikey.com)

---

*Last updated: February 2025*
