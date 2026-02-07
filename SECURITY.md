# Security Policy

## Reporting Security Vulnerabilities

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: **security@freeaiapikey.com**

We will respond within 24 hours and work with you to understand and resolve the issue.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Security Measures

### Data Privacy
- **No long-term data storage**: Prompts and responses are not retained
- **Temporary caching only**: Data cached for minutes, not days
- **No training on user data**: Your data is never used to train models
- **No third-party sharing**: Your data stays yours

### API Security
- HTTPS/TLS encryption for all API calls
- API key authentication required
- Rate limiting on authentication endpoints
- Regular security audits

### Infrastructure
- 99.9% uptime with redundant systems
- Automatic failover
- DDoS protection
- Regular penetration testing

## Best Practices for Users

### API Key Security
- Never commit API keys to public repositories
- Use environment variables for API keys
- Rotate keys regularly
- Use different keys for different environments

### Example: Secure API Key Usage

```python
import os
from openai import OpenAI

# Good: Using environment variable
client = OpenAI(
    api_key=os.getenv("FREEAI_API_KEY"),
    base_url="https://freeaiapikey.com/v1"
)

# Bad: Hardcoding API key
client = OpenAI(
    api_key="sk-abc123",  # ❌ Never do this!
    base_url="https://freeaiapikey.com/v1"
)
```

### Environment File (.env)
```bash
# .env
FREEAI_API_KEY=your-api-key-here
```

```bash
# .gitignore
.env
*.key
```

## Compliance

### GDPR
- Data minimization (no storage)
- Right to be forgotten (nothing to delete!)
- Transparency in data processing

### Other Standards
- SOC 2 Type II (in progress)
- ISO 27001 (planned)

## Security Updates

Security updates will be announced via:
- Email to all users
- Website security page
- Status page: https://status.freeaiapikey.com

## Contact

For security concerns:
- Email: security@freeaiapikey.com
- PGP Key: [Available upon request]

For general support:
- Website: https://freeaiapikey.com

---

Thank you for helping keep FreeAIAPIKey secure!
