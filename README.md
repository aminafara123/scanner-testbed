# scanner-testbed

A deliberately vulnerable repo I built to evaluate security scanners. Nothing here runs anywhere. Every issue is planted on purpose so I can see what a scanner catches, what it misses, how it ranks severity, and how much noise it produces.

Do not reuse any code from this repo. It is broken by design.

## Planted issues

**Vulnerable dependencies (SCA)**
- requirements.txt pins old Python packages with known CVEs (pyyaml 5.1, requests 2.19.1, jinja2 2.10, urllib3 1.24.1, flask 0.12.2)
- package.json pins old npm packages with known CVEs (lodash 4.17.15, minimist 1.2.0, axios 0.21.0, express 4.16.0)

**Code issues (SAST)**
- SQL built by string concatenation from user input
- eval() on a request parameter
- MD5 used for password hashing
- Flask debug mode on and bound to 0.0.0.0

**Secrets detection**
- config.py contains credential-shaped strings. They are the official AWS documentation example keys and made-up passwords, not real credentials

**Infrastructure as code (IaC)**
- main.tf has a public-read S3 bucket with no encryption and a security group open to the world on SSH

**Container**
- Dockerfile uses an outdated base image, runs as root, and pipes curl into a shell

## Why

I wanted to compare scanner findings against a known list of planted problems instead of trusting marketing pages. If a scanner misses something on this list or buries it under noise, that tells me more than any feature table.
