# Model list

*Proposed 12 Nov 2026, to be selected once each model has been tested on my PC.*

**Proposal:** 5 models × 2 quantisation levels = **10 setups**, all chosen to fit on the desktop GPU (16 GB VRAM, about 13 GB free in the pilot). Sizes are approximate, from the Ollama library in November 2026.

| Family | Model | 4-bit | 8-bit | Role |
|---|---|---|---|---|
| Qwen 3.5 | `qwen3.5:9b` | ~6.6 GB ✓ | ~10 GB ✓ | Medium model |
| Qwen 3.5 | `qwen3.5:4b` | ~3 GB ✓ | ~5 GB ✓ | Small model |
| Gemma 4 | `gemma4:12b` | ~7.6 GB ✓ | ~13 GB ⚠️ | Medium model |
| Gemma 4 | `gemma4:e4b` | ~3–4 GB ✓ | ~5–6 GB ✓ | Small model |
| Llama 3.1 | `llama3.1:8b` | ~4.9 GB ✓ | ~8.5 GB ✓ | Older (2024), widely used reference point |

**Optional extra (could-have):** `gemma4:26b`, a mixture-of-experts model with about 4B parameters active per word. It is about 16 GB even at 4-bit, so it would run split between the GPU and system RAM (32 GB). It shows whether a much larger model is worth the slowdown.

**Why:**
- Each provider has a small and a medium model, so size can be compared within a family. This replaces the earlier "~8–9B and ~12–14B" idea, because the ~12–14B models in these families are the largest that fit.
- Llama 3.1 would add a third provider and an older baseline.
- 10 setups sit inside the planned 8–12, at roughly 35 hours of runs (14 timelines × 3 repeats × ~5 min), close to the estimate in risk R3.

**Ruled out:** `qwen3.5:27b` and `gemma4:31b` (17 GB or more even at 4-bit, too slow from system RAM for the full matrix), and models under about 3B parameters (too weak for the task).

**Before choosing**:
- [ ] Pull each model and run one timeline, check with `ollama ps` that it runs 100% on the GPU.
- [ ] Find the exact 8-bit tag names (usually like `qwen3.5:9b-q8_0`) on each model's Tags page
- [ ] Record each model's exact tag and digest (from `ollama list`) in the table below
- [ ] Check each model's licence (Gemma, Llama and Qwen use different terms)

**Frozen list** (to fill in once tested):

| Setup | Exact tag | Digest | Fits on GPU? | Time per timeline |
|---|---|---|---|---|
| | | | | |
