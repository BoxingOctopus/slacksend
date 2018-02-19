# slacksend
Send arbitrary messages to Slack via incoming webhook

## Usage

### Config File
Slacksend expects a config file (stored either in `$HOME/.slacksend/config.toml`
or `$PWD/config.toml`)

An example of this config file can be found in `config.toml.example`

### Command Line Reference

```
Usage: slacksend [OPTIONS]

  Send Message to Slack via Incoming Webhook

Options:
  -t, --token TEXT     Slack Webhook Token
  -u, --username TEXT  Username to Post as on Slack
  -c, --channel TEXT   Channel to Post Message to on Slack
  -m, --message TEXT   Message to Post
  -r, --rot13          Send message ROT13 Encoded
  -b, --base64         Send message Base64 Encoded
  --help               Show this message and exit.
  ```

