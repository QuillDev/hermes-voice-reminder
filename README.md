# voice-reminder

A [Hermes Agent](https://github.com/NousResearch/hermes-agent) plugin that restates the Voice rules from `SOUL.md` next to every user message.

`SOUL.md` sits at the top of the prompt and loses pull in long, tool-heavy sessions. This plugin adds a one-line note to each turn through the `pre_llm_call` hook, so the voice rules sit right where the reply is written. Hermes replays the exact bytes it sent on later turns, so the prompt cache stays intact.

Edit `REMINDER` in `__init__.py` to match your own `SOUL.md`.

## Install

Copy this directory to `~/.hermes/plugins/voice-reminder` and add it to `plugins.enabled` in `~/.hermes/config.yaml`:

```yaml
plugins:
  enabled:
    - voice-reminder
```

Then restart the gateway.
