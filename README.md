# Git-Secret

## Requirements

- git
- [github-cli](https://cli.github.com/)
- `SECRET_KEY` environment variable or `.key` file in the root of the repository (optional)
> You can generate a secret key automatically by leaving the `SECRET_KEY` environment variable empty. It will be stored in the `.key` file.

## Usage

```bash
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add     Add a new secret
  delete  Delete a secret by ID
  edit    Edit a secret by ID
  list    List all secrets
  show    Show a secret by ID
```

## TODO

- [ ] Add configuration file (yaml)
	- [ ] Change repo path
	- [ ] Change secret key
- [ ] Create packages (PIP, AUR, COPR)
- [ ] Add tests