"""Rewrites the counter line in README.md. Run daily by .github/workflows/counter.yml."""
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

# The day I decided to build a machine that thinks alongside people (age 14).
# Change this to the exact date if you remember it.
START = datetime(2020, 1, 1, tzinfo=timezone(timedelta(hours=5, minutes=30)))
SENKU = 117_354_893_870  # fan-wiki count at revival

readme = Path(__file__).resolve().parent.parent / "README.md"
secs = int((datetime.now(timezone.utc) - START).total_seconds())
pct = secs / SENKU * 100

line = (f"⏱️ **{secs:,}** seconds counted since I decided, at 14, to build a machine that thinks "
        f"alongside us. Senku counted {SENKU:,}. I'm at **{pct:.2f}%**. Catching up.")

text = readme.read_text(encoding="utf-8")
new = re.sub(r"(<!-- COUNTER:START -->).*?(<!-- COUNTER:END -->)",
             lambda m: f"{m.group(1)}\n{line}\n{m.group(2)}", text, flags=re.S)
if new != text:
    readme.write_text(new, encoding="utf-8")
print(line)
