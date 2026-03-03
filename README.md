# PyMaster

Quick Python recipes and solved snippets for competitive programming (`Codeforces`, `CSES`, `LeetCode`), optimized for **correctness and accuracy** over verbosity.

## Principles

- Keep solutions minimal and deterministic.
- Prefer proven templates over clever one-offs.
- Avoid unnecessary comments/noise in contest files.
- Keep experimental code separate from trusted recipes.

## Repository Layout

- `algo/` - core algorithm recipes (graph, string, search, etc.)
- `datastructure/` - reusable DS templates (DSU, Fenwick, Segment Tree, Trie, etc.)
- `math_and_pattern/` - math helpers and number/pattern basics
- `problems/` - cleaner problem-specific solutions (intended to be submission-ready)
- `z-problems/` - scratchpad, learning notes, drafts, alternates, and experiments
- `contest_template/` - starter template(s) for new contests

## Source-of-Truth Policy

To avoid drift and redundancy:

- Treat `algo/`, `datastructure/`, and `math_and_pattern/` as canonical recipe libraries.
- Treat `problems/` as canonical solved submissions.
- Treat `z-problems/` as non-canonical WIP/learning area.
- If the same idea exists in multiple files, keep one canonical version and mark/move the rest to `z-problems/`.

## Minimal Quality Bar (for canonical files)

- Correct for edge cases (empty/singleton/bounds/indexing).
- Consistent indexing policy per file (0-index or 1-index, not mixed).
- No debug prints in final recipe/solution paths.
- No broken examples in `__main__`.

## Current Workflow

1. Draft/experiment in `z-problems/`.
2. Once stable, promote to `algo/` or `datastructure/` (or `problems/` for a solved task).
3. Keep one final version; archive alternatives in `z-problems/`.

## Next Cleanup Pass (planned)

- Remove or consolidate duplicate implementations.
- Promote only validated versions to canonical folders.
- Standardize naming and indexing conventions.

