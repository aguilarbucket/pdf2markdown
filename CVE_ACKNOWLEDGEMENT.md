# CVE Acknowledgement and Security Disclaimer

Project: `pdf2markdown`  
Image reviewed: `alejandroromeroa/pdf2markdown:latest`  
Review date: 2026-06-17  
Scanner source: Docker Scout output provided by the maintainer.

## Summary

A Docker Scout scan reported vulnerabilities in the container image. The majority of the findings are inherited from the upstream base image and operating system packages used by the official Python image, rather than from application-specific source code.

The application itself is a small PDF-to-Markdown wrapper intended to convert user-supplied PDF files into Markdown using Python-based tooling. It does not intentionally provide authentication, multi-user isolation, tenant separation, persistent user storage, or public SaaS-grade security controls.

## Current Docker Scout Result

The scan reported:

- 35 total vulnerabilities
- 12 vulnerable packages
- 1 Critical
- 3 High
- 4 Medium
- 25 Low
- 2 Unspecified

Main affected packages reported by Docker Scout include:

- `perl`
- `wheel`
- `tar`
- `pam`
- `glibc`
- `util-linux`
- `systemd`
- `sqlite3`
- `coreutils`
- `apt`
- `shadow`
- `openssl`

## App-Adjudicable vs Base-Image Findings

### Likely inherited from base image / OS layer

The following findings appear to be inherited from the Debian/Python base image or standard OS packages:

- `perl`
- `tar`
- `pam`
- `glibc`
- `util-linux`
- `systemd`
- `sqlite3`
- `coreutils`
- `apt`
- `shadow`
- `openssl`

These packages are not part of the primary application logic and are generally introduced through the selected container base image and its dependency chain.

### Potentially app-adjacent / dependency-managed

The `wheel` package finding is considered app-adjacent because it is a Python packaging dependency and can usually be controlled through the Python dependency layer.

Reported issue:

- `wheel 0.45.1`
- `CVE-2026-24049`
- Docker Scout reported fixed version: `0.46.2`

Recommended action:

```dockerfile
RUN pip install --no-cache-dir --upgrade pip setuptools wheel==0.46.2
```

or pin it in the application dependency file if appropriate:

```txt
wheel==0.46.2
```

## Recommended Mitigations

The following mitigations are recommended before marking the image as production-ready:

1. Rebuild the image regularly from the latest supported base image.
2. Pin Python dependencies where practical.
3. Upgrade `wheel` to the fixed version reported by Docker Scout.
4. Consider testing `python:3.14-alpine` or another Alpine-based variant if all app dependencies compile and run correctly.
5. Run the container as a non-root user.
6. Avoid installing unnecessary OS packages.
7. Use `.dockerignore` to prevent copying local files, secrets, virtualenvs, caches, and test artifacts into the image.
8. Run Docker Scout or equivalent scanning on every release.
9. Treat PDF conversion as untrusted-file processing and avoid exposing the app directly to the public internet without authentication, file limits, and resource controls.

## Suggested Runtime Security Controls

When running this image, prefer a restricted runtime profile:

```bash
docker run --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges:true \
  --pids-limit=256 \
  --memory=512m \
  -p 8502:8502 \
  alejandroromeroa/pdf2markdown:latest
```

If the application requires temporary write access, mount a dedicated temporary directory:

```bash
docker run --rm \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=128m \
  --cap-drop=ALL \
  --security-opt=no-new-privileges:true \
  --pids-limit=256 \
  --memory=512m \
  -p 8502:8502 \
  alejandroromeroa/pdf2markdown:latest
```

## Known Limitations

This acknowledgement does not claim that the application is vulnerability-free. It only distinguishes between:

- vulnerabilities inherited from the base image or OS packages,
- vulnerabilities introduced by Python packaging dependencies,
- and vulnerabilities that would require source-code review to confirm.

A full application security review should also inspect:

- file upload handling,
- PDF parsing behavior,
- temporary file cleanup,
- path traversal protections,
- maximum upload size,
- memory/CPU limits,
- dependency pinning,
- and whether generated Markdown can contain unsafe embedded content.

## Maintainer Position

At the time of this review, most reported CVEs appear to be inherited from the selected official Python slim base image. The maintainer acknowledges these findings and intends to mitigate them through routine base-image refreshes, dependency upgrades, reduced image surface area, and runtime hardening.

The presence of inherited CVEs does not necessarily mean the application code directly invokes the vulnerable functionality. However, all scanner findings are tracked and should be reassessed after each rebuild and dependency update.

## Suggested Recheck Commands

```bash
docker build --pull --no-cache -t alejandroromeroa/pdf2markdown:latest .
docker scout cves alejandroromeroa/pdf2markdown:latest
docker scout recommendations alejandroromeroa/pdf2markdown:latest
```

For better base-image attribution:

```bash
docker buildx build \
  --provenance=mode=max \
  -t alejandroromeroa/pdf2markdown:latest .
```

## Disclaimer

This document is provided as a security acknowledgement and triage note. It is not a formal penetration test, compliance certification, legal warranty, or guarantee of exploitability/non-exploitability.

Users deploying this image are responsible for validating the image against their own threat model, environment, compliance requirements, and exposure level.
