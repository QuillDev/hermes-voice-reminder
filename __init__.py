"""Re-states the SOUL.md voice rules next to each user message.

SOUL.md sits at the top of the prompt and loses pull in long, tool-heavy
sessions. A one-line note in the current turn keeps it close to where the
reply is written. Hermes replays the exact bytes it sent on later turns, so
the prompt cache stays intact.
"""

REMINDER = (
    "Voice (SOUL.md), for this reply and final reports: all lowercase, "
    "plain short sentences. no bullets, bold, headers or tables unless the "
    "user asks. code, paths, IDs and URLs stay exact. lead with the answer, "
    "then cut it in half."
)


def _remind(**_kwargs):
    return {"context": REMINDER}


def register(ctx):
    ctx.register_hook("pre_llm_call", _remind)
