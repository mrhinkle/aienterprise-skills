# Building the Chapter Map

The chapter map (reverse outline) comes before any judgment. It turns pacing and proportion problems from feelings into numbers.

## Columns

| Column | Fiction | Nonfiction |
|---|---|---|
| Ch | number | number |
| Title | as written | as written |
| Words | count | count |
| Running total | cumulative | cumulative |
| Anchor | POV character | one-sentence core claim |
| Contents | scenes, one line each | sections, one line each |
| Job | what it does for the whole | "After reading this, you will be able to..." |

## Word counts from a folder of Markdown chapters

```bash
total=0
for f in $(ls chapters/*.md | sort -V); do
  words=$(wc -w < "$f")
  total=$((total + words))
  title=$(grep -m1 '^# ' "$f" | sed 's/^# //')
  printf "%s\t%s\t%d\t%d\n" "$(basename "$f")" "$title" "$words" "$total"
done
```

For a single file split by headings:

```bash
awk '/^# /{if(t)print t"\t"w; t=$0; w=0; next}{w+=NF}END{print t"\t"w}' manuscript.md
```

For .docx, convert first (`pandoc manuscript.docx -t markdown -o manuscript.md`) and run the second command.

## What to look for in the finished table

- **Outliers.** A chapter at three times the median length, or a quarter of it.
- **Duplicate anchors.** Two chapters whose one-line summaries are the same sentence.
- **Vanishing POV.** A viewpoint character absent for a long stretch.
- **Back-loading.** The first usable framework or tactic appears past the halfway point.
- **Throat-clearing.** The first chapter's job is "sets up" or "introduces."

Put the finished map in the letter's chapter-by-chapter table, adding Job and Verdict.
