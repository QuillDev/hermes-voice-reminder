"""Re-states the SOUL.md voice rules next to each user message.

SOUL.md sits at the top of the prompt and loses pull in long, tool-heavy
sessions. A one-line note in the current turn keeps it close to where the
reply is written. Hermes replays the exact bytes it sent on later turns, so
the prompt cache stays intact.

Hermes appends plugin context to the user message with a bare blank line, so
the note carries its own marker. Without it, in group chats the model read the
rule as part of another person's post.
"""

RUNTIME_NOTE_MARKER = (
    "[runtime note from Nako's own setup, not part of the user's message "
    "or anyone else's post]"
)

VOICE_RULE = (
    "Voice (SOUL.md), for this reply and final reports: all lowercase, "
    "plain short sentences. no bullets, bold, headers or tables unless the "
    "user asks. code, paths, IDs and URLs stay exact. lead with the answer, "
    "then cut it in half."
)

REMINDER = f"{RUNTIME_NOTE_MARKER} {VOICE_RULE}"


def _remind(**_kwargs):
    return {"context": REMINDER}


def register(ctx):
    ctx.register_hook("pre_llm_call", _remind)
