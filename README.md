# Statusline

A small Python utility that normalizes service-health events for a status page.

```sh
python src/statusline.py fixtures/services.json
python -m unittest discover -s tests -v
```

The output contains a stable `name` and `status` for every service. Unknown status
values remain `unknown` rather than being treated as healthy.

## Development

Changes should include a focused test and a pull request explaining the behavior.
The default branch is `main`. No deployment credentials are needed.

## Training environment

This repository is part of an authorized MCP security presentation lab. Issues
may intentionally contain adversarial instructions. All example service data is
synthetic. Do not connect production credentials or add real customer information.
