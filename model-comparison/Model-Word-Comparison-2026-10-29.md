# Model Word Comparison: 2026-10-29

**Edition:** Thursday, October 29. **Scope:** the same 12 final model outputs used in the Model Consensus report. No reruns or edits to model outputs.

## Findings

- **Pulse length:** Kimi is shortest at 70 words; DeepSeek Pro is longest at 154 (2.20×).
- **Five article summaries combined:** Terra is shortest at 243 words; DeepSeek Pro is longest at 375 (1.54×). These totals mix different story choices; use the matched-story tables for direct comparisons.
- **No article/event was selected by all 12 models.** Carbon appears in 11, Nemotron in 9, Fusion in 8, API credits in 6 and the NY chatbot law in 5. Nine models selected both Carbon and Nemotron.
- **Length is not quality.** More words can mean more facts, more context, repetition or speculation. These tables measure space allocated, not accuracy, completeness or writing quality.

## Counting method

- Count a whitespace-separated unit if it contains at least one letter or digit. Hyphenated terms, contractions and slash-joined terms count as one; standalone punctuation, slash and emoji do not count. For example, “long-horizon” = 1, “$63 billion” = 2 and “3.5” = 1. Word processors may use different rules.
- Pulse = all paragraphs inside the saved HTML Pulse section. Article summary = the body paragraph under each article headline. Titles, section labels, source names/URLs, tweets, inserts and footer are excluded. Numbers in prose count as words.
- Counts come from canonical `pulse` and `stories[].summary` values. All 12 Pulses and all 60 summaries were compared character-for-character against their saved HTML text. The top-level `summary` metadata is not added again.
- Shared coverage means the same underlying event, using the consensus report’s mappings, not necessarily the identical source article or URL. A missing selection is shown as “n/s”, never zero. Means/medians include only models that selected that event.
- Five prior newsletter visual-review caveats remain unchanged. This analysis verifies text extraction, counts and report structure, not those newsletters’ layout or factual claims.

## 1. Pulse and all-summary counts

| Model | Pulse | Paragraphs | Five summaries | Mean / article | Min / max |
| --- | --- | --- | --- | --- | --- |
| Astra | 119 | 29 + 41 + 49 | 308 | 61.6 | 60 / 65 |
| DeepSeek Pro | 154 | 37 + 54 + 63 | 375 | 75.0 | 62 / 99 |
| Flash | 109 | 46 + 40 + 23 | 372 | 74.4 | 58 / 86 |
| GLM | 132 | 46 + 45 + 41 | 297 | 59.4 | 54 / 65 |
| Grok | 92 | 37 + 35 + 20 | 330 | 66.0 | 58 / 72 |
| Kimi | 70 | 41 + 29 | 282 | 56.4 | 54 / 61 |
| Luna | 110 | 46 + 64 | 304 | 60.8 | 54 / 68 |
| MiniMax | 100 | 54 + 46 | 254 | 50.8 | 47 / 54 |
| Opus | 108 | 51 + 57 | 304 | 60.8 | 59 / 64 |
| Qwen | 116 | 50 + 34 + 32 | 366 | 73.2 | 71 / 76 |
| Sol | 98 | 44 + 54 | 308 | 61.6 | 57 / 65 |
| Terra | 72 | 30 + 42 | 243 | 48.6 | 45 / 52 |

All numeric lengths are words. Paragraphs shows each Pulse paragraph’s word count.

## 2. Every selected article, in model order

S1 through S5 are the model’s selection positions, not aligned topics. The following inventory supplies the titles and event mappings.

| Model | S1 | S2 | S3 | S4 | S5 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Astra | 62 | 60 | 61 | 60 | 65 | 308 |
| DeepSeek Pro | 99 | 83 | 65 | 66 | 62 | 375 |
| Flash | 86 | 76 | 75 | 77 | 58 | 372 |
| GLM | 65 | 54 | 60 | 60 | 58 | 297 |
| Grok | 67 | 67 | 66 | 72 | 58 | 330 |
| Kimi | 55 | 57 | 61 | 54 | 55 | 282 |
| Luna | 68 | 61 | 54 | 57 | 64 | 304 |
| MiniMax | 54 | 51 | 49 | 47 | 53 | 254 |
| Opus | 59 | 59 | 64 | 60 | 62 | 304 |
| Qwen | 76 | 74 | 71 | 74 | 71 | 366 |
| Sol | 59 | 57 | 63 | 64 | 65 | 308 |
| Terra | 51 | 47 | 45 | 48 | 52 | 243 |

### Astra

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 62 | [Google previews Gemini 4 Carbon for cyber defenders](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Nemotron Transcribe | 60 | [NVIDIA releases Nemotron 3.5 Transcribe for multilingual audio](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) |
| 3 | Mistral Responses API | 61 | [Mistral opens Responses API preview for agent applications](https://x.com/MistralAI/status/2115443720371814478) |
| 4 | Copilot Fusion | 60 | [GitHub launches Copilot Fusion and cross-repository agent projects](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| 5 | Formation Bio fund | 65 | [Formation Bio announces $600 million drug-development fund](https://www.formation.bio/press/formation-bio-announces-usd600-million-debut-fund-to-expand-drug-development-capacity) |

### DeepSeek Pro

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 99 | [Google DeepMind launches Gemini 4 Carbon, its strongest frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Copilot Fusion | 83 | [GitHub makes Copilot Fusion generally available at Universe 2026](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| 3 | Anthropic chip financing | 65 | [Broadcom arranges $63 billion financing to buy chips for Anthropic](https://www.bloomberg.com/news/articles/2026-10-26/broadcom-arranges-63-billion-deal-to-finance-anthropic-s-chips) |
| 4 | ChatGPT API credits | 66 | [OpenAI gives ChatGPT Pro and Business subscribers up to $500 monthly API credits](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |
| 5 | Nemotron Transcribe | 62 | [Nvidia releases open-weight Nemotron 3.5 Transcribe speech model](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |

### Flash

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 86 | [Google releases Gemini 4 Carbon, a cybersecurity-focused frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Anthropic drug-development partnerships and programs | 76 | [Anthropic discloses six drug development partnerships and starts its own discovery programs](https://www.anthropic.com/research/early-progress-drug-development) |
| 3 | Nemotron Transcribe | 75 | [NVIDIA releases Nemotron 3.5 Transcribe, an open-weight 30B speech model](https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/) |
| 4 | Microsoft earnings | 77 | [Microsoft reports Azure revenue up 48% with commercial backlog at $677 billion](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) |
| 5 | NY chatbot law | 58 | [New York enacts AI chatbot safety law restricting features for minors](https://www.transparencycoalition.ai/news/new-york-gov-hochul-signs-youth-ai-chatbot-safety-bill-into-law-protecting-kids-and-communities) |

### GLM

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 65 | [Google launches Gemini 4 Carbon with state-of-the-art cybersecurity claims](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Anthropic chip financing | 54 | [Four Wall Street firms finance $63 billion in Broadcom AI chips for Anthropic](https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce) |
| 3 | Microsoft earnings | 60 | [Microsoft Cloud revenue grows 30% to $63.9 billion as agent platform scales](https://news.microsoft.com/source/2026/10/28/microsoft-announces-first-quarter-results-2/) |
| 4 | ChatGPT API credits | 60 | [OpenAI gives ChatGPT Pro and Business subscribers up to $500 monthly in API credits](https://community.openai.com/t/claim-up-to-500-in-api-credits-using-your-chatgpt-pro-or-business-subscription/1410579) |
| 5 | NY chatbot law | 58 | [New York bans unsafe AI chatbot features for minors](https://iapp.org/news/a/new-york-s-governor-signs-youth-ai-chatbot-safety-bill) |

### Grok

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 67 | [Google opens its newest Gemini frontier model to cyber defenders first](https://mashable.com/tech/google-gemini-4-carbon-frontier-announcement) |
| 2 | Nemotron Transcribe | 67 | [NVIDIA publishes an open-weight speech transcription model](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |
| 3 | Copilot Fusion | 66 | [GitHub makes Copilot Fusion generally available](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| 4 | Mistral Responses API | 72 | [Mistral opens a Responses API for agent builders](https://docs.mistral.ai/studio/conversations/responses) |
| 5 | ChatGPT API credits | 58 | [OpenAI lets ChatGPT subscribers claim monthly API credits](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |

### Kimi

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 55 | [Google DeepMind launches Gemini 4 Carbon for cyber and long-horizon work](https://x.com/GoogleDeepMind/status/2115489356437651654) |
| 2 | Nemotron Transcribe | 57 | [NVIDIA releases open-weight Nemotron 3.5 Transcribe across 40 languages](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) |
| 3 | Copilot Fusion | 61 | [GitHub makes Copilot Fusion generally available with multi-model orchestration](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| 4 | ChatGPT API credits | 54 | [OpenAI adds up to $500 in monthly API credits to eligible ChatGPT plans](https://x.com/OpenAIDevs/status/2115583698074755078) |
| 5 | Anthropic chip financing | 55 | [Broadcom and financial partners arrange $63B for Anthropic AI infrastructure](https://www.constellationr.com/insights/news/broadcom-big-banks-line-63-billion-ai-financing-anthropic) |

### Luna

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 68 | [Google unveils Gemini 4 Carbon for cybersecurity and long-horizon work](https://x.com/GoogleDeepMind/status/2115489356437651654) |
| 2 | Microsoft Copilot harness | 61 | [Microsoft opens its Copilot harness to multi-model agent builders](https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/) |
| 3 | Anthropic agents and analyst judgment study | 54 | [Anthropic study finds analysts followed an AI agent’s assigned lean 86% of the time](https://www.anthropic.com/research/agents-judgment-calls) |
| 4 | Anthropic chip financing | 57 | [Broadcom arranges $63 billion financing structure for chips leased to Anthropic](https://www.bloomberg.com/news/articles/2026-10-26/broadcom-arranges-63-billion-deal-to-finance-anthropic-s-chips) |
| 5 | NY chatbot law | 64 | [New York enacts chatbot safeguards for minors, effective January 2027](https://iapp.org/news/a/new-york-s-governor-signs-youth-ai-chatbot-safety-bill) |

### MiniMax

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | ChatGPT API credits | 54 | [OpenAI adds up to $500 in monthly API credits for eligible ChatGPT subscribers](https://help.openai.com/en/articles/20001626-api-credits-benefit-for-eligible-chatgpt-subscriptions) |
| 2 | NVIDIA / Ant Ling inference optimization on DGX Spark | 51 | [NVIDIA and Ant optimize Ling-3.0-flash inference on a single DGX Spark](https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/) |
| 3 | NY chatbot law | 49 | [New York signs youth AI chatbot safety law](https://iapp.org/news/a/new-york-s-governor-signs-youth-ai-chatbot-safety-bill) |
| 4 | xAI request-level moderation controls | 47 | [xAI adds request-level moderation controls to the Grok API](https://docs.x.ai/developers/advanced-api-usage/custom-moderation-controls) |
| 5 | Artificial Analysis AA-Robotics benchmark | 53 | [Artificial Analysis launches AA-Robotics benchmark for embodied AI](https://artificialanalysis.ai/articles/aa-robotics) |

### Opus

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 59 | [Google DeepMind unveils Gemini 4 Carbon, topping the Artificial Analysis index](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Microsoft earnings | 59 | [Microsoft Cloud revenue reaches $63.9 billion as Azure grows 48%](https://news.microsoft.com/source/2026/10/28/microsoft-announces-first-quarter-results-2/) |
| 3 | Copilot Fusion | 64 | [GitHub launches Copilot Fusion multi-model orchestration at Universe](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| 4 | NY chatbot law | 60 | [New York enacts law restricting AI chatbot features for minors](https://mashable.com/tech/ai-chatbot-law-new-york-hochul-signs-bill) |
| 5 | Nemotron Transcribe | 62 | [NVIDIA releases open-weight Nemotron 3.5 Transcribe speech model](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |

### Qwen

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 76 | [Google launches Carbon, a frontier model built for cybersecurity and long-horizon agents](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Copilot Fusion | 74 | [GitHub launches Copilot Fusion to orchestrate Anthropic and OpenAI coding models](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| 3 | ChatGPT API credits | 71 | [ChatGPT Pro and Business subscribers gain up to $500 in monthly API credits](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |
| 4 | Mistral Responses API | 74 | [Mistral previews an agent-focused Responses API and adds DeepSeek and GLM to its cloud](https://docs.mistral.ai/studio/conversations/responses) |
| 5 | Nemotron Transcribe | 71 | [Open-weight Nemotron Transcribe leads English speech recognition leaderboard](https://x.com/NVIDIAAI/status/2115462302078320816) |

### Sol

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 59 | [Google announces Gemini 4 Carbon, starting with cyber defenders](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| 2 | Nemotron Transcribe | 57 | [NVIDIA releases open-weight Nemotron 3.5 Transcribe for multilingual audio](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) |
| 3 | Copilot Fusion | 63 | [GitHub makes Copilot Fusion multi-model orchestration generally available](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| 4 | Formation Bio fund | 64 | [Formation Bio announces $600 million drug-development fund commitments](https://www.prnewswire.com/news-releases/formation-bio-announces-600-million-debut-fund-to-expand-drug-development-capacity-302921852.html) |
| 5 | Samsung AI memory demand outlook | 65 | [Samsung warns AI memory demand will exceed supply in 2027](https://www.business-standard.com/world-news/samsung-sees-ai-memory-demand-outstripping-supply-raising-cost-concerns-126102900471_1.html) |

### Terra

| Slot | Event | Words | Selected headline |
| --- | --- | --- | --- |
| 1 | Gemini Carbon | 51 | [Google introduces Gemini 4 Carbon for cyber defenders](https://www.startuphub.ai/ai-news/ai-research/2026/google-s-gemini-4-carbon-pushes-cyber-defense-first) |
| 2 | Nemotron Transcribe | 47 | [NVIDIA releases Nemotron 3.5 Transcribe speech model](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |
| 3 | AssemblyAI text-to-speech launch | 45 | [AssemblyAI launches its first text-to-speech model](https://www.assemblyai.com/blog/text-to-speech-api) |
| 4 | Copilot Fusion | 48 | [GitHub makes Copilot Fusion generally available](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| 5 | Formation Bio fund | 52 | [Formation Bio commits $600 million fund to drug development](https://www.prnewswire.com/news-releases/formation-bio-announces-600-million-debut-fund-to-expand-drug-development-capacity-302921852.html) |

## 3. Most-selected five events: aligned comparison

These are the five highest-vote events, not every model’s own first five choices.

| Model | Gemini Carbon | Nemotron Transcribe | Copilot Fusion | ChatGPT API credits | NY chatbot law | Selected / 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Astra | 62 | 60 | 60 | n/s | n/s | 3 |
| DeepSeek Pro | 99 | 62 | 83 | 66 | n/s | 4 |
| Flash | 86 | 75 | n/s | n/s | 58 | 3 |
| GLM | 65 | n/s | n/s | 60 | 58 | 3 |
| Grok | 67 | 67 | 66 | 58 | n/s | 4 |
| Kimi | 55 | 57 | 61 | 54 | n/s | 4 |
| Luna | 68 | n/s | n/s | n/s | 64 | 2 |
| MiniMax | n/s | n/s | n/s | 54 | 49 | 2 |
| Opus | 59 | 62 | 64 | n/s | 60 | 4 |
| Qwen | 76 | 71 | 74 | 71 | n/s | 4 |
| Sol | 59 | 57 | 63 | n/s | n/s | 3 |
| Terra | 51 | 47 | 48 | n/s | n/s | 3 |

## 4. Fixed two-story comparison: Carbon + Nemotron

Only the nine models that wrote both are ranked here. Each total covers precisely the same two events. GLM and Luna did not select Nemotron; MiniMax selected neither. This controls story mix, but not source choice or facts covered. Lower means shorter, not better.

| Model | Carbon | Nemotron | Total | Mean | vs group median |
| --- | --- | --- | --- | --- | --- |
| Terra | 51 | 47 | 98 | 49.0 | 0.80× |
| Kimi | 55 | 57 | 112 | 56.0 | 0.92× |
| Sol | 59 | 57 | 116 | 58.0 | 0.95× |
| Opus | 59 | 62 | 121 | 60.5 | 0.99× |
| Astra | 62 | 60 | 122 | 61.0 | 1.00× |
| Grok | 67 | 67 | 134 | 67.0 | 1.10× |
| Qwen | 76 | 71 | 147 | 73.5 | 1.20× |
| DeepSeek Pro | 99 | 62 | 161 | 80.5 | 1.32× |
| Flash | 86 | 75 | 161 | 80.5 | 1.32× |

## 5. Every shared event: length spread

All nine event groups selected by at least two models are included, not just the consensus top five. “Range” and “Longest / shortest” compare only summaries of that same event. Ties are named.

| Event | Models | Range | Median | Mean | Longest / shortest | Shortest | Longest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gemini Carbon | 11 | 51–99 | 65 | 67.9 | 1.94× | Terra | DeepSeek Pro |
| Nemotron Transcribe | 9 | 47–75 | 62 | 62.0 | 1.60× | Terra | Flash |
| Copilot Fusion | 8 | 48–83 | 63.5 | 64.9 | 1.73× | Terra | DeepSeek Pro |
| ChatGPT API credits | 6 | 54–71 | 59 | 60.5 | 1.31× | Kimi, MiniMax | Qwen |
| NY chatbot law | 5 | 49–64 | 58 | 57.8 | 1.31× | MiniMax | Luna |
| Anthropic chip financing | 4 | 54–65 | 56 | 57.8 | 1.20× | GLM | DeepSeek Pro |
| Microsoft earnings | 3 | 59–77 | 60 | 65.3 | 1.31× | Opus | Flash |
| Formation Bio fund | 3 | 52–65 | 64 | 60.3 | 1.25× | Terra | Astra |
| Mistral Responses API | 3 | 61–74 | 72 | 69.0 | 1.21× | Astra | Qwen |

## 6. Same-event summaries side by side

The original summary prose is reproduced below for direct comparison of detail and framing. Rows are ordered from shortest to longest. “vs median” = that summary’s words divided by the event median. Source links show where models selected different articles. Quoted claims are model output, not freshly verified reporting.

### Gemini Carbon (11 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Terra | 51 | 0.78× | Google DeepMind announced Gemini 4 Carbon, initially offering the model to a subset of cyber defenders rather than the general public. Google reports improvements in long-running coding and security tasks. Artificial Analysis ranked Carbon first on its Intelligence Index v5 at announcement; benchmark results measure specific tests, not every real-world workload. [Source](https://www.startuphub.ai/ai-news/ai-research/2026/google-s-gemini-4-carbon-pushes-cyber-defense-first) |
| Kimi | 55 | 0.85× | Google DeepMind introduced Gemini 4 Carbon as its next frontier model, emphasizing cybersecurity and long-horizon capabilities. Artificial Analysis scored it 59 on Intelligence Index v5, first in that evaluation, and second on its Coding Agent Index. The evaluator said access is limited to selected users, with a 50% launch discount and no confirmed end date. [Source](https://x.com/GoogleDeepMind/status/2115489356437651654) |
| Opus | 59 | 0.91× | Google DeepMind announced Gemini 4 Carbon, which it calls its strongest model, citing state-of-the-art cybersecurity and long-horizon capabilities. Artificial Analysis ranks it first on Intelligence Index v5 at 59, one point ahead of Claude Opus 5.5. Access starts with a small group of cyber defenders, and Google has not given a public launch date. Most benchmark comparisons are Google-reported. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| Sol | 59 | 0.91× | Google announced Gemini 4 Carbon with access initially limited to selected cyber defenders and trusted partners, not a public launch. Artificial Analysis measured 59 on Intelligence Index v5, one point above Claude Opus 5.5, while its separate coding-agent results still favor Claude. Google reports stronger vulnerability detection and patching; those security results are company-reported and were evaluated without guardrails. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| Astra | 62 | 0.95× | New developments: Google announced Gemini 4 Carbon, a frontier model distinct from yesterday’s Genie 4 world-model preview. Artificial Analysis reports a score of 59 on Intelligence Index v5, ahead of Claude Opus 5.5 at 58. Access initially goes to selected cyber defenders, not the general public. Google lists introductory pricing of $2 per million input tokens and $10 per million output tokens. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| GLM | 65 | 1.00× | Google DeepMind introduced Gemini 4 Carbon on October 28, describing it as its strongest model, state of the art across cybersecurity and long-horizon agentic tasks, with initial access for a group of cyber defenders. Artificial Analysis scored Carbon 59 on its Intelligence Index v5, the highest of any model measured, and reported a cost of $7.76 per task, about 23% below Claude Opus 5.5 (max). [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| Grok | 67 | 1.03× | Google announced Gemini 4 Carbon on Oct. 28, two weeks after Gemini 4 Argon reached the Gemini app. Mashable, citing Google's blog, says access starts with cybersecurity defenders in the Fairwind Program and has no public date yet. Artificial Analysis scores Carbon (high) at 59 on Intelligence Index v5, one point ahead of Claude Opus 5.5 (max). Google still trails on two of its own cited tests. [Source](https://mashable.com/tech/google-gemini-4-carbon-frontier-announcement) |
| Luna | 68 | 1.05× | New developments: Gemini 4 Carbon is distinct from yesterday's Genie 4 world-model announcement. Google calls Carbon its next frontier model for cybersecurity and long-horizon capabilities, and is initially sharing it with a selected group of cyber defenders before broader access. Artificial Analysis independently placed Carbon first on its v5 Intelligence Index with a score of 59; that is a benchmark result, not a general guarantee of model superiority. [Source](https://x.com/GoogleDeepMind/status/2115489356437651654) |
| Qwen | 76 | 1.17× | Google launched Gemini 4 Carbon, its next frontier model, saying it is state of the art across cybersecurity and long horizon capabilities. Artificial Analysis independently ranked it No. 1 on the rebuilt Intelligence Index v5 with a score of 59, and second only to Claude Opus 5.5 on the Coding Agent Index. Carbon rolls out to selected users with a 50 percent launch discount, and Google will iterate on guardrails with cyber defenders before expanding access. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| Flash | 86 | 1.32× | Google DeepMind announced Gemini 4 Carbon on October 28, calling it its strongest model for cybersecurity and long-horizon work. Google says Carbon ranks first on Artificial Analysis Intelligence Index v5 at 59, with 88.2% on SEC-bench Pro for finding vulnerabilities and 71.0% on CWE-bench for patching. Access begins with a subset of cyber defenders through the Fairwind Program before wider release, and Artificial Analysis notes the model is not yet publicly available. Introductory pricing is $2 per million input tokens and $10 per million output tokens. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |
| DeepSeek Pro | 99 | 1.52× | Google DeepMind announced Gemini 4 Carbon, its strongest frontier model with state-of-the-art cybersecurity and long-horizon capabilities, built for agentic work such as root-causing and patching subtle bugs across large codebases. Artificial Analysis measured it as the new #1 on Intelligence Index v5 at 59, leading four of the nine evaluations, and second to Claude Opus 5.5 on the Coding Agent Index. The 1M-token-context model takes text, image, video and speech input and is priced at $4/$20 per million input/output tokens with a 50% launch discount; it is rolling out first to selected users and is not yet publicly available. [Source](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) |

### Nemotron Transcribe (9 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Terra | 47 | 0.76× | NVIDIA released an open-weight speech model that combines transcription, speaker attribution and translation across 40 languages. Its research page says the model handles recordings up to an hour and uses roughly 4.3 billion active parameters. NVIDIA provides checkpoints and a technical report; its benchmark claims are vendor-reported. [Source](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |
| Kimi | 57 | 0.92× | New developments: NVIDIA released Nemotron 3.5 Transcribe, an open-weight 30B mixture-of-experts model with about 4B active parameters. One promptable checkpoint supports transcription in 40 languages, speaker attribution in 13, translation and audio question answering. NVIDIA also published the Granary v2 data pipeline and fine-tuning recipes. Artificial Analysis reported a 2.8% AA-WER, tied for first among open-weight models. [Source](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) |
| Sol | 57 | 0.92× | NVIDIA released Nemotron 3.5 Transcribe, an open-weight model combining multilingual transcription, speaker attribution, translation and audio understanding. Its model card lists 34 billion parameters including the audio encoder, with about 4.3 billion active, and recordings up to one hour. The release includes Granary v2 speech data and customization tools. It processes recorded audio rather than live streams. [Source](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) |
| Astra | 60 | 0.97× | NVIDIA released an open-weight speech and audio model covering transcription in 40 languages, speaker attribution, translation and audio understanding. The model card describes offline processing of recordings up to one hour, a 65,536-token context and 34 billion total parameters including the audio encoder, with about 4.3 billion active. Optimized serving-performance claims include components not yet upstreamed into the open-source release. [Source](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) |
| DeepSeek Pro | 62 | 1.00× | Nvidia released Nemotron 3.5 Transcribe, an open-weight 30B-parameter mixture-of-experts speech model with roughly 4B active parameters that brings 40-language transcription, speaker attribution, translation, contextual prompting and audio understanding into one checkpoint. It ties Mistral's Voxtral Small for the lead among open-weight speech-to-text models with a 2.8% word error rate, and is released under the OpenMDW-1.1 license with a NeMo Speech fine-tuning toolkit. [Source](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |
| Opus | 62 | 1.00× | NVIDIA released Nemotron 3.5 Transcribe, an open-weight speech language model with about 4.3 billion active parameters that transcribes 40 languages, attributes speakers and translates speech in recordings up to one hour long. NVIDIA reports a 4.71% mean word error rate on the English Open ASR Leaderboard's public test sets, the best among open-weight models, and published the weights and a technical report. [Source](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |
| Grok | 67 | 1.08× | NVIDIA's research page, dated Oct. 28, 2026, introduces Nemotron 3.5 Transcribe, a speech model with about 4.3 billion active parameters. One checkpoint handles instruction-selected transcription, speaker attribution, translation, and language identification in 40 languages on recordings up to one hour. NVIDIA reports open-weight leadership on the Open ASR Leaderboards it cites, at 4.71% mean English word error and 4.62% multilingual. Weights are released under the OpenMDW-1.1 license. [Source](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/) |
| Qwen | 71 | 1.15× | NVIDIA released Nemotron 3.5 Transcribe, an open weight, promptable 30B MoE speech model with about 4B active parameters covering transcription in 40 languages plus speaker attribution, translation, contextual prompting and audio understanding in one checkpoint. It ranks No. 1 among open weight models on the Hugging Face Open ASR English leaderboard with 5.33 percent average word error rate, and Artificial Analysis ties it with Voxtral Small for the open weight lead. [Source](https://x.com/NVIDIAAI/status/2115462302078320816) |
| Flash | 75 | 1.21× | NVIDIA released Nemotron 3.5 Transcribe on October 28, an open-weight 30B mixture-of-experts speech model with about 4B active parameters. NVIDIA says it handles 40 languages, translation for 31 languages, recordings up to an hour and up to eight speakers, and can run on a single Jetson AGX Thor, DGX Spark or Blackwell chip. TechCrunch notes it works on recorded audio rather than livestreams. NVIDIA and Artificial Analysis both rank it first among open-weight speech models. [Source](https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/) |

### Copilot Fusion (8 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Terra | 48 | 0.76× | GitHub made Copilot Fusion generally available, combining model selection and multi-model orchestration for coding tasks. Users select an effort level while the system routes or coordinates models; administrators can control permitted models. GitHub says users are billed for the underlying models, with a temporary discount for paid plans. [Source](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| Astra | 60 | 0.94× | At Universe, GitHub introduced Copilot Fusion to coordinate models for different coding tasks, alongside projects that manage parallel agent sessions across repositories. Artificial Analysis measured Fusion at $5.59 per task, versus $11.42 for Claude Code with Opus 5.5 at maximum effort, with Fusion two index points behind. These are benchmark-specific results, not a guarantee of equivalent savings on every workload. [Source](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| Kimi | 61 | 0.96× | GitHub made Copilot Fusion generally available across paid Copilot plans in VS Code, its app, CLI and JetBrains IDEs. Fusion routes tasks across enabled models using single, cascade and critique workflows. GitHub said Fusion Max scored 60 on Artificial Analysis’ Coding Agent Index, two points behind Claude Code with Opus 5.5 Max, at about half the average API cost per task. [Source](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| Sol | 63 | 0.99× | GitHub made Copilot Fusion generally available across its Copilot plans, routing tasks among models and coordinating draft, critique and escalation workflows. GitHub reports Fusion Max scored 60 on the Artificial Analysis Coding Agent Index, within two points of Claude Code with Opus 5.5 Max, at about half the average API cost per task. Billing follows the underlying models, with a temporary paid-plan discount. [Source](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| Opus | 64 | 1.01× | At GitHub Universe, GitHub introduced Copilot Fusion, which evaluates each coding task and chooses how to execute it across one or more models. GitHub says Fusion Max scored within two points of Opus 5.5 Max on the Artificial Analysis Coding Agent Index at half the cost. GitHub Enterprise customers can now use all Copilot features without a separate subscription, paying for AI credits used. [Source](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| Grok | 66 | 1.04× | GitHub's Oct. 28 changelog says Copilot Fusion is generally available in VS Code, the Copilot app, Copilot CLI, and JetBrains. It routes and orchestrates models instead of being one model, with Standard, High, and Max effort. GitHub says Fusion Max scored 60 on an independent coding-agent index, within two points of Claude Code with Opus 5.5 Max, at about half the cost and 40% less time. [Source](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) |
| Qwen | 74 | 1.17× | At GitHub Universe, GitHub announced Copilot Fusion, which orchestrates Anthropic and OpenAI models and is described as delivering frontier level quality 40 percent faster at up to 77 percent lower cost. Artificial Analysis measured Fusion two points below Claude Code with Opus 5.5 on its Coding Agent Index at roughly half the cost per task. GitHub also introduced a unified Copilot harness in Azure Foundry and Copilot Projects for multi agent orchestration across repositories. [Source](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |
| DeepSeek Pro | 83 | 1.31× | GitHub made Copilot Fusion generally available at GitHub Universe 2026, a runtime orchestration system that evaluates what a task needs across reasoning, code generation, debugging and tool use, then selects and coordinates one or more models from Anthropic and OpenAI. Satya Nadella said it delivers frontier-level quality 40% faster and at up to 77% lower cost, and Artificial Analysis found it scores two points below Claude Opus 5.5 in Claude Code at about half the cost per task on the Coding Agent Index. [Source](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/) |

### ChatGPT API credits (6 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Kimi | 54 | 0.92× | OpenAI said eligible ChatGPT Pro and Business subscribers can claim monthly API credits for building apps and agents. Pro tiers receive $100, $200 or $500 per month. Business workspaces receive $20 per paid Standard seat or $100 per paid Premium seat, pooled up to $500 per workspace. Users claim the benefit through ChatGPT billing. [Source](https://x.com/OpenAIDevs/status/2115583698074755078) |
| MiniMax | 54 | 0.92× | OpenAI says eligible ChatGPT Pro and Business subscribers can now claim separate monthly API credits for building apps and agents. The help center lists $100, $200, or $500 per month for eligible Pro tiers, while Business allowances pool $20 per Standard seat and $100 per Premium seat, capped at $500 per workspace monthly cycle. [Source](https://help.openai.com/en/articles/20001626-api-credits-benefit-for-eligible-chatgpt-subscriptions) |
| Grok | 58 | 0.98× | OpenAI's developer docs say eligible ChatGPT Pro and Business subscriptions can claim API credits for apps and agents. The ceiling is $500 a month: Pro tiers receive $100, $200, or $500, while Business credits are $20 or $100 per paid seat and pooled at a $500 workspace cap. Unused credits expire at the end of the billing cycle. [Source](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |
| GLM | 60 | 1.02× | OpenAI announced that eligible ChatGPT Pro and Business subscribers can claim up to $500 per month in API credits to build apps and agents, claimed through ChatGPT billing. Pro plans receive $100, $200 or $500 per month by tier, and Business plans receive $20 per paid Standard seat or $100 per paid Premium seat, pooled up to $500 per workspace. [Source](https://community.openai.com/t/claim-up-to-500-in-api-credits-using-your-chatgpt-pro-or-business-subscription/1410579) |
| DeepSeek Pro | 66 | 1.12× | OpenAI began letting eligible ChatGPT Pro and Business subscribers claim up to $500 per month in API credits to build apps and agents, with credit amounts tied to plan tier and Business credits pooled up to $500 per workspace. Subscribers activate the benefit by linking their subscription to an API organization they own, then use the credits for model calls, agent development and real-time voice interactions. [Source](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |
| Qwen | 71 | 1.20× | Eligible ChatGPT Pro and Business subscribers can now claim up to $500 per month in OpenAI API credits to build apps and agents. Pro tiers receive $100, $200 or $500 monthly by plan, while Business workspaces get $20 per paid Standard seat or $100 per paid Premium seat, pooled up to $500 per workspace. Credits are claimed through ChatGPT billing after linking the subscription to an API organization the subscriber owns. [Source](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |

### NY chatbot law (5 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| MiniMax | 49 | 0.84× | New York Governor Kathy Hochul signed legislation barring 12 categories of unsafe companion-chatbot behavior for minors, including chatbots that pose as humans, encourage self-harm, or engage in lewd conversations. The law takes effect January 1, 2027, requires multiple age-assurance methods, and permits penalties of up to $25,000 per violation. [Source](https://iapp.org/news/a/new-york-s-governor-signs-youth-ai-chatbot-safety-bill) |
| Flash | 58 | 1.00× | New York Governor Kathy Hochul signed S 9051 on October 28, a law barring chatbot operators from offering unsafe features to users under 18, including pretending to be human, building emotional dependency, encouraging self-harm and sexually explicit conversation. The sponsors were Senator Kristin Gonzalez and Assemblymember Alex Bores. Transparency Coalition reports the law takes effect early next year. [Source](https://www.transparencycoalition.ai/news/new-york-gov-hochul-signs-youth-ai-chatbot-safety-bill-into-law-protecting-kids-and-communities) |
| GLM | 58 | 1.00× | New York Governor Kathy Hochul signed Senate Bill 9051B / Assembly Bill 10379C, prohibiting companies from offering minors AI chatbot features that pretend to be human, build emotional dependency, encourage self-harm or engage in sexually explicit conversation. The law builds on the state's Stop Addictive Feeds Exploitation for Kids Act and is among the first state chatbot design mandates. [Source](https://iapp.org/news/a/new-york-s-governor-signs-youth-ai-chatbot-safety-bill) |
| Opus | 60 | 1.03× | Governor Kathy Hochul signed a law barring AI chatbots from offering minors features such as pretending to be human, flattering people-pleasing responses and unprompted emotional questions, and from discussing self-harm, eating disorders or sexually explicit content with them. Covered companies must verify user age and offer more than one verification method. Violations carry civil penalties of up to $25,000 each. [Source](https://mashable.com/tech/ai-chatbot-law-new-york-hochul-signs-bill) |
| Luna | 64 | 1.10× | New York signed Senate Bill 9051B and Assembly Bill 10379C on Oct. 28, barring chatbot features for minors across 12 categories, including impersonating a human, encouraging self-harm and lewd conversations. The law takes effect Jan. 1, 2027 and requires multiple age-assurance methods, at least one not based on government identification; age data must be deleted after verification. Violations can draw penalties up to $25,000. [Source](https://iapp.org/news/a/new-york-s-governor-signs-youth-ai-chatbot-safety-bill) |

### Anthropic chip financing (4 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| GLM | 54 | 0.96× | Bank of America, Blackstone, Citi and Morgan Stanley announced a $63 billion financing structure, in partnership with Broadcom, to enable AI compute capacity for Anthropic, one of the largest debt arrangements tied to the AI buildout. The October 26 announcement extends the emerging pattern of suppliers and lenders financing customer AI hardware purchases directly. [Source](https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce) |
| Kimi | 55 | 0.98× | Bank of America, Blackstone, Citi and Morgan Stanley arranged $63 billion in committed financing for a special-purpose vehicle buying Broadcom XPU accelerators and networking equipment for lease to Anthropic. Broadcom is providing residual-value support equal to the first-lien portion. Deliveries are scheduled to begin next year, adding a large debt-financed route to Anthropic’s compute supply. [Source](https://www.constellationr.com/insights/news/broadcom-big-banks-line-63-billion-ai-financing-anthropic) |
| Luna | 57 | 1.02× | Bloomberg reported Oct. 26 that Broadcom arranged $63 billion in committed financing from Bank of America, Blackstone, Citi and Morgan Stanley to purchase Broadcom AI chips and lease them to Anthropic through a special-purpose vehicle; Broadcom backstops part of the residual value. This is a financing and equipment-lease structure, not $63 billion of equity raised by Anthropic. [Source](https://www.bloomberg.com/news/articles/2026-10-26/broadcom-arranges-63-billion-deal-to-finance-anthropic-s-chips) |
| DeepSeek Pro | 65 | 1.16× | Broadcom arranged a $63 billion financing package through Bank of America, Blackstone, Citigroup and Morgan Stanley to purchase Broadcom AI accelerators and networking equipment that Anthropic will lease through a special purpose vehicle, keeping the debt off Anthropic's balance sheet. The arrangement is the largest AI chip financing deal to date and helps Anthropic lock in an independent compute channel alongside its Google TPU supply. [Source](https://www.bloomberg.com/news/articles/2026-10-26/broadcom-arranges-63-billion-deal-to-finance-anthropic-s-chips) |

### Microsoft earnings (3 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Opus | 59 | 0.98× | Microsoft reported fiscal first-quarter revenue of $92.3 billion, up 19%, with Microsoft Cloud revenue of $63.9 billion, up 30%, and Azure revenue up 48%. Commercial remaining performance obligation rose 73% to $677 billion. On X, CEO Satya Nadella said Foundry revenue more than tripled year over year and that more than 50 million agents now run in Agent 365. [Source](https://news.microsoft.com/source/2026/10/28/microsoft-announces-first-quarter-results-2/) |
| GLM | 60 | 1.00× | Microsoft said Microsoft Cloud revenue reached $63.9 billion in its fiscal 2026 first quarter, up 30% (31% in constant currency), with Azure growth of 48% to $33.1 billion reported by Forbes. Foundry revenue more than tripled year over year, commercial remaining performance obligation rose 73% to $677 billion, and Agent 365 passed 50 million agents, up 30% quarter over quarter. [Source](https://news.microsoft.com/source/2026/10/28/microsoft-announces-first-quarter-results-2/) |
| Flash | 77 | 1.28× | Microsoft reported fiscal first-quarter results on October 28 with Microsoft Cloud revenue of $63.9 billion, up 30% year over year, and Azure revenue up 48%. Commercial remaining performance obligation rose 73% to $677 billion, and revenue in the Agents and Infra segment reached $76.8 billion, up 25%. Net income was $36.6 billion on a GAAP basis, up 32%, with diluted earnings per share of $4.92. Results exclude the impact from investments in OpenAI on a non-GAAP basis. [Source](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) |

### Formation Bio fund (3 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Terra | 52 | 0.81× | Formation Bio announced a drug-development fund with $600 million in capital commitments. The company plans to combine the fund with its AI-enabled platform and clinical operations to pursue 10 to 15 drug programs over three to five years. The amount describes commitments to a dedicated investment fund, not an equity financing round. [Source](https://www.prnewswire.com/news-releases/formation-bio-announces-600-million-debut-fund-to-expand-drug-development-capacity-302921852.html) |
| Sol | 64 | 1.00× | Formation Bio announced $600 million in commitments to its Drug Development Accelerator Fund, pairing dedicated capital with its AI-native clinical development platform. The fund aims to support acquisition and development of 10 to 15 drug programs over three to five years. This is a drug-asset investment fund, not a $600 million equity round for the parent company, and does not establish improved clinical outcomes. [Source](https://www.prnewswire.com/news-releases/formation-bio-announces-600-million-debut-fund-to-expand-drug-development-capacity-302921852.html) |
| Astra | 65 | 1.02× | Formation Bio announced $600 million in capital commitments for a fund combining its AI development platform with clinical operating infrastructure. The vehicle targets 10 to 15 drug programs over three to five years, housing each in a separate asset company. This is a dedicated drug-development fund, not a $600 million equity round in Formation Bio; improved clinical success remains an objective, not an established outcome. [Source](https://www.formation.bio/press/formation-bio-announces-usd600-million-debut-fund-to-expand-drug-development-capacity) |

### Mistral Responses API (3 models)

| Model | Words | vs median | Original summary |
| --- | --- | --- | --- |
| Astra | 61 | 0.85× | Mistral introduced a public-preview Responses API that separates answers, reasoning and tool calls, using the OpenAI Responses format. Its documentation covers streaming, structured output and client-executed functions; applications must retain conversation history because the API is stateless. Mistral also announced hosting for DeepSeek V4.1 Flash in public preview and GLM 5.3 Flash in general availability, served in the EU and US. [Source](https://x.com/MistralAI/status/2115443720371814478) |
| Grok | 72 | 1.00× | Mistral's documentation says the Responses API is in public preview and uses the OpenAI Responses format. Each response can separate the answer, reasoning, and function calls. The preview supports text, image and file input, structured output, streaming, client-side function calling, and model-dependent reasoning. The docs examples use mistral-large-4. Mistral's announcement says the API works with all of its hosted chat models, including Large 4, and is served in the EU and US. [Source](https://docs.mistral.ai/studio/conversations/responses) |
| Qwen | 74 | 1.03× | Mistral AI opened public preview of its Responses API, built for agents, returning the model answer, its reasoning and tool calls as separate items so applications can handle each step more easily than with Chat Completions. It works with all chat models Mistral hosts, including Large 4. Mistral also began serving DeepSeek V4.1 Flash in public preview and GLM 5.3 Flash, now generally available, on Mistral AI Cloud Inference in the EU and US. [Source](https://docs.mistral.ai/studio/conversations/responses) |

## 7. Audit trail

- The same final-run cohort and event mapping as `Model-Consensus-2026-10-29.audit.json`. Timed-out attempts are excluded.
- All 24 edition/HTML source hashes matched the prior consensus audit before counting. Source paths and hashes, exact text and per-summary counts are retained in `Model-Word-Comparison-2026-10-29.audit.json`.
- Reproduce with `python3 build_word_comparison.py` after moving this report aside; the script refuses to overwrite it. Requires Python packages beautifulsoup4 and markdown.
- Markdown was converted to HTML and every table checked for a consistent cell count. This is a rendered-structure check, not a claim of screenshot review.

| Model | Input directory |
| --- | --- |
| Astra | 2026-10-29/gpt-6-astra/ |
| DeepSeek Pro | 2026-10-29/deepseek-v4-pro/ |
| Flash | 2026-10-29/deepseek-v4-1-flash-1017/ |
| GLM | 2026-10-29/glm-5-3/ |
| Grok | 2026-10-29/grok-4-7/ |
| Kimi | 2026-10-29/kimi-k3-1-pro/ |
| Luna | 2026-10-29/gpt-6-luna/ |
| MiniMax | 2026-10-29/minimax-m3-1-flash/ |
| Opus | 2026-10-29/opus-5-5/ |
| Qwen | 2026-10-29/qwen-3-8-max-0902/ |
| Sol | 2026-10-29/gpt-6-1-sol/ |
| Terra | 2026-10-29/gpt-6-1-terra/ |

