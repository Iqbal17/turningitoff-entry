"""Have You Tried Turning It Off? — make.fun entry.

One funny line a hopeless tech support agent gives a desperate customer.

Decision record (weighed against the judge's criteria, most important first:
on-subject -> twist/cheerful uselessness -> sounds like a real agent ->
tight on first read -> fresh):

Candidate A — "Have you tried turning it off and on again? I ask because I
have tried everything else, including hope."
LOSES. It is the stock line itself, and the title of the bounty. The twist
("including hope") is pleasant but thin, and half the field will write some
version of the same classic. Freshness fails.

Candidate B — "Your computer is not broken, it's just resting. Like me. I
have been on hold with our own support for forty minutes."
LOSES. The agent's helplessness is there, but the joke is about the computer
being "resting" — a borrowed gag — and the second sentence explains the
situation instead of letting it land. The customer's desperation is not felt
at all; the customer has vanished from the line.

Candidate C — "I understand your frustration, and I have escalated this to
a team who will also understand your frustration."
CHOSEN. The joke IS the structure: the standard support move (escalation)
collapses into a circle — the case goes to people who will do exactly what
this agent just did, which is understand and nothing else. It reads exactly
like a real support reply ("I understand your frustration" is the most
common opening a real agent types), the customer's desperation is felt in
that opening rather than explained, the cheerful uselessness is the whole
punchline, and the twist lands on the last three words.

Candidate D — "The good news is your files are safe. The bad news is I have
no idea where safe is."
LOSES. Funny, but it is a joke about files, not a support agent talking to
a desperate customer — the desk frame is barely there. "Good news / bad
news" is also a worn shape, and the line works the same without any
customer at all, which fails criterion 1.

Writing passes on the winner:
Pass 1 — first draft read "I have escalated your case to a team that will
also understand your frustration." "Your case" is ticket jargon; it made the
line sound like a form letter. Changed to "this", which is how a person
actually talks, and tightened the rhythm.
Pass 2 — tried "escalated this to a senior team" and "...who will also
completely understand your frustration." Both dropped: "senior" promises
competence, which undercuts the joke (a senior team might actually help),
and "completely" adds a word without adding a laugh. Plain "a team" keeps
the escalation visibly circular.
"""

import os

LINE = "I understand your frustration, and I have escalated this to a team who will also understand your frustration."
MAX_CHARS = 199


def check_gate(text: str) -> None:
    """Mirror the sealed gate: 1-199 UTF-8 chars, not only whitespace, one line."""
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def entry_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
