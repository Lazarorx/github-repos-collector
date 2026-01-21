# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

We take the security of GitHub Repos Collector seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please do NOT:

- Open a public GitHub issue
- Post about it on social media
- Share the vulnerability with others until it has been addressed

### Please DO:

1. **Email us directly** at [your-email@example.com] with:
   - Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
   - Full paths of source file(s) related to the manifestation of the issue
   - The location of the affected source code (tag/branch/commit or direct URL)
   - Any special configuration required to reproduce the issue
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the issue, including how an attacker might exploit it

2. **Allow time for a fix** - We will acknowledge your email within 48 hours and will send a more detailed response within 7 days indicating the next steps in handling your report.

3. **Coordinated disclosure** - After the initial reply to your report, we will keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

## Security Update Process

1. The security report is received and assigned to a primary handler
2. The problem is confirmed and a list of affected versions is determined
3. Code is audited to find any similar problems
4. Fixes are prepared for all supported releases
5. New versions are released and announcements are made

## Comments on this Policy

If you have suggestions on how this process could be improved, please submit a pull request or open an issue to discuss.

## Known Security Considerations

### API Rate Limiting

This tool uses the GitHub API without authentication by default. This means:
- Rate limit: 60 requests per hour per IP address
- Consider using a GitHub token for higher limits (5000 requests/hour)
- The tool does not currently support authentication (feature request welcome)

### Data Privacy

- This tool only accesses public GitHub data
- No personal information is collected or stored
- Cache files are stored locally and contain only public repository information
- Exported files contain only public repository metadata

### Dependencies

We regularly update dependencies to patch security vulnerabilities. You can check for outdated dependencies:

```bash
pip list --outdated
```

To update all dependencies:

```bash
pip install --upgrade -r requirements.txt
```

## Security Best Practices for Users

1. **Keep the tool updated** - Always use the latest version
2. **Review exported data** - Before sharing exported files, review their contents
3. **Secure your environment** - Use virtual environments to isolate dependencies
4. **Monitor API usage** - Be aware of GitHub API rate limits
5. **Validate inputs** - Be cautious when using data from untrusted sources

## Acknowledgments

We would like to thank the following individuals for responsibly disclosing security issues:

- (No reports yet)

---

**Last Updated:** January 20, 2026
