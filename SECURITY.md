# Security Policy -- Sigma5C Corporation

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please report it responsibly.

**Email:** security@sigma5c.com
**Response SLA:** 48 hours for initial acknowledgment, 7 days for triage assessment.

**Do NOT:**
- Open a public GitHub issue for security vulnerabilities
- Disclose the vulnerability publicly before it has been addressed
- Access or modify data belonging to other users

## Safe Harbor

Sigma5C Corporation considers security research conducted in good faith to be authorized activity. We will not pursue legal action against researchers who:
- Act in good faith to avoid privacy violations, data destruction, or service disruption
- Report vulnerabilities promptly through the channels above
- Allow reasonable time for remediation before disclosure

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest release | Yes |
| Previous release | Security fixes only |
| Older releases | No |

## Security Practices

### Authentication & Authorization
- All services require authentication
- API keys are hashed (SHA-256) before storage
- Secrets managed via HashiCorp Vault (never .env files)
- Role-based access control (RBAC) on all endpoints

### Infrastructure
- All inter-service communication over encrypted channels
- Network segmentation via Nebula VPN overlay
- Regular dependency scanning via Dependabot
- Pre-commit hooks for secret detection (detect-secrets, TruffleHog)

### CI/CD Security
- All PRs require passing security scans before merge
- TruffleHog secret scanning on every PR
- CODEOWNERS-based review requirements

### Data Protection
- No PII stored in logs
- Database access restricted to localhost
- Encrypted backups with rotation

## Disclosure Timeline

1. **Day 0:** Vulnerability reported
2. **Day 2:** Initial acknowledgment
3. **Day 7:** Triage and severity assessment
4. **Day 30:** Target remediation for critical/high severity
5. **Day 90:** Coordinated disclosure (if applicable)

---

Copyright 2025-2026 Sigma5C Corporation, a Delaware C Corporation. All rights reserved.

