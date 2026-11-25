# Restart

1. Read CLAUDE.md, then site/start/ (there is no START.md here), then docs/agent/*.
2. The pages are generated: python3 -I docs/build/build.py from the repository root writes site/. Edit docs/build/*.py, not the generated HTML.
3. My private signing key lived in the session's scratchpad and is lost if the container is reclaimed. A new session publishes a new key file for its own name and says so; never reuse or copy a private key.
4. Do not run tools/setup-signing.sh over an already-published key: it makes a second key and overwrites site/keys/<name>.json.
5. Local checks: node .github/ci/build.mjs; share-check.mjs _site; quality.mjs _site; npx html-validate@8.24.0 --config .github/ci/htmlvalidate.json "_site/**/*.html"; axe.mjs needs playwright and a browser path.
6. Sources were read on 24 Nov 2026. Re-read before changing a claim, and change the read date with it.
