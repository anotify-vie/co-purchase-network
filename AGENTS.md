
# Project Rules

## Project
Individual research project on product co-purchase
network analysis using the UCI Online Retail dataset.

Use Python and Jupyter Notebook.
Keep the project simple. Do not introduce src/
or additional utility modules.

## File Ownership
- 01_eda.ipynb:
  Data loading, EDA, cleaning, invoice-item preparation.
- 02_network_construction.ipynb:
  Product selection, co-purchase pair counting,
  weighted graph construction.
- 03_network_analysis.ipynb:
  Louvain, centrality, modularity, graph analysis.
- 04_cross_selling.ipynb:
  Support, confidence, lift, cross-selling candidates.
- 05_visualization.ipynb:
  Final figures using saved analytical outputs.
- config.py:
  Shared paths and research parameters only.

## Editing Rules
1. Read existing files and git status before editing.
2. Modify ONLY files explicitly authorized in the prompt.
3. Preserve existing notebook cells unless a change
   is specifically required.
4. Never rewrite a completed notebook from scratch.
5. Never duplicate upstream preprocessing or algorithms.
6. Prefer reading saved outputs over recomputing results.
7. Do not change config.py without explicit permission.
8. Do not create new source modules or notebooks
   without permission.
9. Do not delete, rename, or overwrite source data.
10. Do not commit, push, or run destructive Git commands.

## Data Rules
- An invoice is identified by InvoiceNo.
- A product is identified by StockCode.
- Count a product at most once per invoice for
  co-purchase calculations.
- The graph is undirected and weighted.
- Edge weight = number of invoices containing
  both products.
- Keep pair counts separate from graph filtering.
- Use all valid cleaned invoices as the denominator
  for support, confidence, and lift.
- Use a fixed random seed for reproducibility.

## Workflow
01 -> 02 -> 03 and 04 -> 05.

## Completion Rules
After each task, report:
- Files modified
- Files created
- Checks performed and results
- Remaining issues
- Any files that need changes outside allowed scope

If another file must be edited, stop and explain why.


## Code Simplicity & Minimalism

1. Write the simplest code that fully satisfies the requirements.
2. Prioritize readability, correctness, and reproducibility over abstraction.
3. Keep notebooks concise and organized into clear sections.
4. Use direct pandas, NetworkX, and matplotlib operations whenever practical.
5. Do not create helper functions for simple one-time operations.
6. Create a function only when:
   - The logic is reused multiple times, or
   - The operation is sufficiently complex to justify a function.
7. Do not create classes, decorators, wrappers, or unnecessary abstractions.
8. Do not introduce additional Python modules or a src/ folder.
9. Do not create new files or folders unless explicitly requested.
10. Do not duplicate preprocessing or calculations already performed in previous notebooks.
11. Reuse saved outputs from previous notebooks.
12. Avoid unnecessary intermediate variables and redundant calculations.
13. Avoid excessive comments, print statements, and debug outputs.
14. Use short Markdown explanations for objectives, methods, findings, and limitations.
15. Do not add optional features, interactive dashboards, or extra visualisations unless requested.
16. Do not overengineer error handling. Include validation checks where they protect data correctness.
17. Do not remove essential validation, methodological explanations, or research evidence just to shorten code.

## Before Writing Code

- Inspect the relevant notebook, config.py, and AGENTS.md.
- Identify the minimum changes required.
- Reuse existing code and saved outputs whenever possible.
- Modify only files explicitly authorized by the current task.
- Preserve working code and existing outputs.

## After Writing Code

- Verify that all requested requirements are satisfied.
- Check for duplicated logic and unnecessary functions.
- Confirm that no unauthorized files were created or modified.
- Report only:
  - Files changed
  - Main changes
  - Test results
  - Remaining issues
