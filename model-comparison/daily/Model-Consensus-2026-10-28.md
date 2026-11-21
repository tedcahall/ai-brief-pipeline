# Model-selection consensus review (corrected, full 12-model cohort)

## Overall consensus selection ranking

**100 points possible: headline 5 + five stories × 9 (45) + ten tweets × 5 (50).** Higher is better. This is selection agreement, not factual accuracy or editorial quality. Speed is reported separately and does not break score ties.

| Rank | Model | Score | Headline | Stories | Tweets | Time |
|---|---|---|---|---|---|---|
| 1 | Grok | 90 | 5 | 5/5 → 45 | 8/10 → 40 | 28m 45s |
| 2 | DeepSeek Pro | 85 | 0 | 5/5 → 45 | 8/10 → 40 | 17m 12s |
| 2 | Qwen | 85 | 5 | 5/5 → 45 | 7/10 → 35 | 15m 57s |
| 2 | Sol | 85 | 5 | 5/5 → 45 | 7/10 → 35 | 18m 04s |
| 5 | Opus | 81 | 5 | 4/5 → 36 | 8/10 → 40 | 7m 29s |
| 6 | Flash | 80 | 0 | 5/5 → 45 | 7/10 → 35 | 20m 15s |
| 7 | Astra | 76 | 5 | 4/5 → 36 | 7/10 → 35 | 11m 56s |
| 7 | GLM | 76 | 0 | 4/5 → 36 | 8/10 → 40 | 3m 38s |
| 9 | Kimi | 75 | 0 | 5/5 → 45 | 6/10 → 30 | 12m 08s |
| 10 | MiniMax | 62 | 5 | 3/5 → 27 | 6/10 → 30 | 8m 38s |
| 11 | Luna | 60 | 0 | 5/5 → 45 | 3/10 → 15 | 7m 46s |
| 12 | Terra | 47 | 5 | 3/5 → 27 | 3/10 → 15 | 3m 58s |

### How the score is assembled

1. Freeze the shared-X/web-archive cohort: twelve models, one selected run each. Each model contributes one vote per unique event or tweet, including to its own reference consensus.
2. Headline: 5 points for the most-selected underlying event; 0 otherwise. Joint leaders would each qualify. The headline vote counts are shown in the ranked headline union; this is an agreement bonus, not a truth judgment.
3. Stories: count selections with at least the fifth-highest vote count; award 9 per unique match, maximum five matches / 45 points.
4. Tweets: count exact IDs with at least the tenth-highest vote count; award 5 per unique match, maximum ten matches / 50 points.
5. Add the three components. Equal totals share a rank. No ordering bonus, speed adjustment, or fractional credit.

**Cutoff-tie treatment:** 6 stories qualify at 6 votes or more; 10 tweets qualify at 5 votes or more. The eligible pools can exceed five and ten, but each model still selects only five stories and ten tweets.

**Change from the earlier report:** All counts and cutoff eligibility were recomputed over twelve models. Every cutoff tie receives full credit; display-order tie-breaks do not affect scoring. Original model artifacts are unchanged.

**Audit trail:** Ranked unions show every vote and eligible item; report cards show each model’s arithmetic and matching selections; the appendix preserves the original ordered selections.

## Scope and scoring

**12 models using Wednesday, October 28 inputs, one selected run each; 60 story selections and 120 tweet selections.** The ranked lists below are the full unions, not just the winners.

- Selected the latest completed, non-blocked HTML-producing attempt per model from the handoff. Included `review_required` runs with reported passing deterministic checks; this does not certify visual quality. Earlier attempts, crashes, timeouts, and original blocked Luna are excluded.
- This supersedes the earlier 10-model and mixed-input reports. Kimi and Opus now use the same edition and byte-identical saved X/web archives as the other ten. All consensus sets, scores and ranks were recalculated; no other models were rerun.
- Luna is the authorized one-off retry using the adjusted tweet-display protocol. Kimi and Opus are the newly authorized reruns; the other ten selected artifacts are unchanged. Identical ancillary inputs and prompts across all twelve are not established; see the audit below.
- “Correct” means agreement with this cohort’s consensus, not verified truth or editorial quality. Each model has one vote per event or tweet. Models are included in their own consensus; this is not leave-one-out scoring.
- Headlines and stories are manually grouped by the underlying news event, regardless of URL or phrasing. Tweet identity is the numeric status ID; distinct posts about the same story remain distinct.
- Popularity rank uses model count only; ties share a rank. Every item tied at the fifth-story or tenth-tweet cutoff is eligible for full credit. Counts are capped at five story matches and ten tweet matches. Average selected position, then stable key, controls display order only—not credit. **★** marks all scoring-eligible items.
- Speed ranks use worker-reported whole-run elapsed time, not scheduler time or inference latency. Fractions are omitted. Different tool work and Luna’s protocol mean these are observed run speeds, not controlled model benchmarks.

## Selected runs

| Model label | Model / attempt | Edition | Worker status | Worker elapsed |
|---|---|---|---|---|
| Flash | deepseek-v4-1-flash-1017 | 2026-10-28 | complete_local | 20m 15s |
| DeepSeek Pro | deepseek-v4-pro | 2026-10-28 | complete_local | 17m 12s |
| GLM | glm-5-3 | 2026-10-28 | complete_local | 3m 38s |
| Sol | gpt-6-1-sol | 2026-10-28 | complete_local | 18m 04s |
| Terra | gpt-6-1-terra | 2026-10-28 | review_required | 3m 58s |
| Astra | gpt-6-astra | 2026-10-28 | review_required | 11m 56s |
| Luna | gpt-6-luna-oneoff-14773 | 2026-10-28 | review_required | 7m 46s |
| Grok | grok-4-7 | 2026-10-28 | complete_local | 28m 45s |
| MiniMax | minimax-m3-1-flash | 2026-10-28 | complete_local | 8m 38s |
| Qwen | qwen-3-8-max-0902 | 2026-10-28 | complete_local | 15m 57s |
| Kimi | kimi-k3-1-pro | 2026-10-28 | review_required | 12m 08s |
| Opus | opus-5-5 | 2026-10-28 | complete_local | 7m 29s |

## 1. Ranked headline union

| Popularity rank | Underlying headline story | Models | Selected by |
|---|---|---|---|
| 1 | Google DeepMind Genie 4 world model | 7/12 | Sol, Terra, Astra, Grok, MiniMax, Qwen, Opus |
| 2 | OpenAI AI-generated scientific results / proof claims | 5/12 | Flash, DeepSeek Pro, GLM, Luna, Kimi |

## 2. Ranked Top-5 story union

| Popularity rank | Consensus set | Underlying story | Models | Selected by |
|---|---|---|---|---|
| 1 | ★ | Google DeepMind Genie 4 world model | 12/12 | Flash, DeepSeek Pro, GLM, Sol, Terra, Astra, Luna, Grok, MiniMax, Qwen, Kimi, Opus |
| 2 | ★ | OpenAI AI-generated scientific results / proof claims | 10/12 | Flash, DeepSeek Pro, GLM, Sol, Astra, Luna, Grok, Qwen, Kimi, Opus |
| 2 | ★ | Anthropic drug-development research and Mithril Medicine | 10/12 | Flash, DeepSeek Pro, GLM, Sol, Astra, Luna, Grok, Qwen, Kimi, Opus |
| 4 | ★ | Liquid AI LFM3 open-weight model family | 9/12 | DeepSeek Pro, Sol, Terra, Astra, Luna, Grok, MiniMax, Qwen, Kimi |
| 5 | ★ | Artificial Analysis Intelligence Index v5 | 6/12 | Flash, DeepSeek Pro, GLM, MiniMax, Qwen, Kimi |
| 5 | ★ | Oracle Cloud adds Google TPUs | 6/12 | Flash, Sol, Terra, Luna, Grok, Opus |
| 7 |  | InclusionAI / Ant Ling-3.1-flash-1019 weights | 3/12 | Terra, Astra, MiniMax |
| 8 |  | Microsoft MAI-Image-2.7-Preview | 1/12 | MiniMax |
| 8 |  | Baidu Unlimited OCR 2 | 1/12 | Terra |
| 8 |  | Broadcom / Anthropic $63 billion compute financing | 1/12 | Opus |
| 8 |  | Cognition FrontierCode 2.0 benchmark | 1/12 | GLM |

### Story-grouping decisions

- OpenAI’s ETH-focused story and broader math/CS/physics announcement are one event: the same scientific-results release. This does not endorse the claims.
- Anthropic’s drug-development partnerships, internal discovery work and Mithril acquisition are grouped as the same research announcement.
- Oracle’s combined TPU/OpenAI-chip article counts once for the Oracle TPU announcement shared with the other models; its extra chip angle gets no second vote.
- Ling’s model-card and news coverage are one weights release. Artificial Analysis’s article and announcement tweet are one index release.
- Kimi’s new ordered mappings are scientific proofs, Genie 4, LFM3, Intelligence Index v5, drug research. Opus’s are Genie 4, scientific proofs, Oracle TPUs, drug research, and the new $63B Broadcom/Anthropic financing event. These mappings were inspected from the new canonical stories, not reused from their older editions.
- Opus’s science story includes an Anthropic ETH angle but leads with the same OpenAI release and URL; it receives one science-event vote. Its $63B financing story is a separate infrastructure financing event, not drug research or an IPO.

## 3. Ranked selected-tweet union

Excerpts identify the saved selected posts; they are not newly verified news summaries. Each linked ID is exact. ★ marks all tweets eligible for scoring, including every cutoff tie; each model can earn credit for at most ten unique tweets.

| Popularity rank | Consensus set | Tweet ID | Author | Saved text excerpt | Models | Selected by |
|---|---|---|---|---|---|---|
| 1 | ★ | [2115128329003303107](https://x.com/i/status/2115128329003303107) | @liquidai | Introducing 𝙻𝙵𝙼𝟹: our new generation of Liquid Foundation Models. With a new tri-hybrid architecture and new multimodal encoders, the LFM3 family is the ideal model suite for specialize… | 11/12 | Flash, DeepSeek Pro, GLM, Sol, Terra, Astra, Grok, MiniMax, Qwen, Kimi, Opus |
| 2 | ★ | [2115265133467635877](https://x.com/i/status/2115265133467635877) | @ArtificialAnlys | Announcing Artificial Analysis Intelligence Index v5, featuring 2 new benchmarks and 3 upgrades. For the first time, the majority of the Index is built on private datasets The Artificia… | 10/12 | Flash, DeepSeek Pro, GLM, Sol, Astra, Grok, MiniMax, Qwen, Kimi, Opus |
| 2 | ★ | [2115178675050307942](https://x.com/i/status/2115178675050307942) | @AnthropicAI | Over the past few months, Anthropic scientists have engaged in deep research partnerships with six organizations developing new medicines. We've also begun drug discovery efforts of our… | 10/12 | Flash, DeepSeek Pro, GLM, Sol, Astra, Grok, MiniMax, Qwen, Kimi, Opus |
| 2 | ★ | [2115062200687878157](https://x.com/i/status/2115062200687878157) | @AntLingAGI | Now open source: Ling-3.1-flash-1019. 44 on the Artificial Analysis Intelligence Index v4.3.2, up from 41 for Ling-3.1-flash. Also releasing Ling-3.1-flash-base, an open foundation for … | 10/12 | DeepSeek Pro, GLM, Sol, Terra, Astra, Luna, Grok, MiniMax, Qwen, Opus |
| 5 | ★ | [2114837059462627533](https://x.com/i/status/2114837059462627533) | @gdb | Announcing three major scientific discoveries, one each in mathematics (harmonic analysis), computer science (complexity theory), and physics (quantum field theory). AI starting to help… | 8/12 | DeepSeek Pro, GLM, Sol, Astra, Luna, Grok, Qwen, Opus |
| 6 | ★ | [2115132488775524793](https://x.com/i/status/2115132488775524793) | @cognition | Introducing FrontierCode 2.0: our new coding benchmark that measures a model’s ability to go beyond the spec. Most coding evals measure a model’s ability to write code that meets a spec… | 7/12 | Flash, DeepSeek Pro, GLM, Grok, MiniMax, Qwen, Opus |
| 7 | ★ | [2115135061293203537](https://x.com/i/status/2115135061293203537) | @reflection_ai | We ran ~1.3 billion sandboxes in our largest RL run for Beam - spanning RL training, evaluation, and ablations. With evals and other RL experiments running, the fleet peaked at 883,006 … | 6/12 | Flash, DeepSeek Pro, Astra, MiniMax, Kimi, Opus |
| 7 | ★ | [2115207004293853358](https://x.com/i/status/2115207004293853358) | @AnthropicAI | We're expanding our partnership with @USGSA. Under a new OneGov agreement, we are bringing Claude to federal, state, local, tribal, and territorial governments at 40% off.  | 6/12 | Flash, GLM, Sol, Luna, Grok, Opus |
| 9 | ★ | [2115114030503166385](https://x.com/i/status/2115114030503166385) | @GoogleDeepMind | Here’s what’s new with Genie 4: 🔵 Photorealism: Built on Gemini Omni for lifelike detail across spaces and subjects 🔵 Advanced physics: Aerodynamics, collisions, and people who move nat… | 5/12 | Sol, Terra, Astra, Grok, Kimi |
| 9 | ★ | [2115126872455475476](https://x.com/i/status/2115126872455475476) | @SemiAnalysis_ | BREAKING NEWS🚨: NVIDIA just submitted its first Rubin NVL72 Kimi K3 submission, and it can reach over 850 tok/s/user, even at 2.8 Trillion parameters, with over 3x higher throughput on … | 5/12 | Flash, DeepSeek Pro, GLM, Qwen, Kimi |
| 11 |  | [2115114028338962672](https://x.com/i/status/2115114028338962672) | @GoogleDeepMind | This is Genie 4, our most realistic and interactive world model yet. 🌐 Explore dynamic environments in real time to see how the scene responds, sounds, and how the people in it move, re… | 4/12 | Flash, MiniMax, Qwen, Opus |
| 11 |  | [2115120550230020113](https://x.com/i/status/2115120550230020113) | @reflection_ai | We ran ~1.3 billion sandboxes in our largest RL run for Beam - spanning RL training, evaluation, and ablations. With evals and other RL experiments running, the fleet peaked at 883,006 … | 4/12 | Sol, Terra, Grok, Qwen |
| 11 |  | [2115099284224008200](https://x.com/i/status/2115099284224008200) | @mustafasuleyman | MAI-Image is now the #2 image edit model in the world! ... once again beating Google, Meta, xAI, and GPT-Image-2.5-Flare. Try it today on MAI Playground. Links below 👇  | 4/12 | GLM, Luna, MiniMax, Qwen |
| 14 |  | [2115232001275924722](https://x.com/i/status/2115232001275924722) | @demishassabis | Very excited to share Genie 4, our incredible interactive world model, bringing together real-time physics, reasoning, and audio! Simulations within simulations, makes you wonder just h… | 3/12 | DeepSeek Pro, GLM, Luna |
| 14 |  | [2115097540320506069](https://x.com/i/status/2115097540320506069) | @ArtificialAnlys | Microsoft's MAI-Image-2.7-Preview takes #2 on AA-Image-Editing v2.1, close behind OpenAI's GPT Image 2.5 Sunburst (max) and a clear step up from MAI-Image-2.6 MAI-Image-2.7-Preview is M… | 3/12 | Terra, Kimi, Opus |
| 14 |  | [2115204127013929072](https://x.com/i/status/2115204127013929072) | @ArtificialAnlys | Cartesia Managed Agents scores an Elo of 1115 on the Artificial Analysis Speech Agent Arena, 98 points above Cartesia's earlier voice agent product, Cartesia Line, with Task Success Rat… | 3/12 | Sol, Terra, Astra |
| 17 |  | [2115233234732917055](https://x.com/i/status/2115233234732917055) | @vllm_project | 🎉 Spark-X2.6-1.7B from @SparkLLM is out — a compact on-device agent model with 1M native context and controllable thinking (none/low/high), nearly matching its 4B sibling on SWE-Verifie… | 2/12 | Luna, MiniMax |
| 17 |  | [2115101113666134276](https://x.com/i/status/2115101113666134276) | @arena | Exciting news: MAI-Image-2.7-Preview from @MicrosoftAI just landed at #3 overall in the Image Edit Arena with 1470 pts! That puts Microsoft AI at #2 among labs. This release is a +45 pt… | 2/12 | Sol, Astra |
| 17 |  | [2115156635954090345](https://x.com/i/status/2115156635954090345) | @dair_ai | Must-read paper from Microsoft Research and Georgia Tech. This one has lots of great insights. They used 163,487 Reddit posts about AI agents and surveyed 73 experienced agent users to … | 2/12 | Terra, MiniMax |
| 17 |  | [2115129110930628859](https://x.com/i/status/2115129110930628859) | @mustafasuleyman | Our cyber models are getting really strong. MAI Cyber model in our security harness has doubled user adoption to 50% in the last 30 days. We also made it 20% more token efficient withou… | 2/12 | Flash, DeepSeek Pro |
| 21 |  | [2114839833134674351](https://x.com/i/status/2114839833134674351) | @TheRundownAI | NEW: OpenAI says its AI just made three major discoveries in math, computer science, and physics. 1. Local smoothing + Kakeya conjectures (math): proved in every dimension. A 35-year-ol… | 1/12 | Kimi |
| 21 |  | [2115128330848751659](https://x.com/i/status/2115128330848751659) | @liquidai | LFM3 is our most capable generation of foundation models yet, built for specialization and on-device deployment. Here’s what’s new:... | 1/12 | Luna |
| 21 |  | [2114945367712366718](https://x.com/i/status/2114945367712366718) | @sgl_project | Congrats to @Baidu_Inc on Unlimited OCR 2! An entire book parsed in a single request, with decode latency and memory staying flat across hundreds of pages 👀 Proud to be the recommended … | 1/12 | Terra |
| 21 |  | [2115265177046389089](https://x.com/i/status/2115265177046389089) | @ArtificialAnlys | Cost varies widely among the leading models. Claude Opus 5.5 (max) costs $10.04 per Intelligence Index task, GPT-6 Astra (max) $6.24 and GPT-6.1 Sol (max) $1.27. GPT-6.1 Sol (max) score… | 1/12 | Luna |
| 21 |  | [2115265171233120627](https://x.com/i/status/2115265171233120627) | @ArtificialAnlys | Open weights models fall further behind in v5. The leader, Kimi K3.1 Pro (weights not yet released), scores 46, 12 points behind the leader, compared with a 3-point gap in v4.3. Of mode… | 1/12 | Terra |
| 21 |  | [2115155299334246584](https://x.com/i/status/2115155299334246584) | @ArtificialAnlys | Ling 3.1 Flash 1019, an open weights model and successor to Ling 3.1 Flash, scores 44 on the Artificial Analysis Intelligence Index v4.3, up from 41 @AntLingAGI has released Ling 3.1 Fl… | 1/12 | Kimi |
| 21 |  | [2115101219119325606](https://x.com/i/status/2115101219119325606) | @dair_ai | Great paper from Alibaba and Cornell on verification in coding-agent harnesses. (bookmark it) If you build agent harnesses, this one is worth your time. They find that a separate review… | 1/12 | Terra |
| 21 |  | [2115132493259321443](https://x.com/i/status/2115132493259321443) | @cognition | FrontierCode 2.0 separates model tiers more clearly than FrontierCode 1.1. It also ranks them differently: on DeepSWE v1.1, Muse Wonder 1.0 and Gemini 4 Argon score highest, but on Fron… | 1/12 | Luna |
| 21 |  | [2115171788812669225](https://x.com/i/status/2115171788812669225) | @GeminiApp | With Google SynthID detection in Gemini, anyone can easily check if an image, video, or audio file was made with AI from Google. Just ask Gemini, “Is this AI generated?," so you can nav… | 1/12 | Flash |
| 21 |  | [2115175550465507710](https://x.com/i/status/2115175550465507710) | @SemiAnalysis_ | Anthropic’s S-1 shows inference revenue per megawatt nearly quadrupling in a year. “Inference revenue per megawatt went from sixteen million last year to sixty plus currently, across th… | 1/12 | Kimi |
| 21 |  | [2115196931979014345](https://x.com/i/status/2115196931979014345) | @a16z | Databricks CEO Ali Ghodsi says if frontier models stopped advancing, it wouldn't matter for most orgs because enterprise AI is bottlenecked on context, not intelligence:... | 1/12 | Luna |
| 21 |  | [2115232805416468826](https://x.com/i/status/2115232805416468826) | @vllm_project | 🎉 Spark-X2.6-1.7B from @SparkLLM is out — a compact on-device agent model with 1M native context and controllable thinking (none/low/high), nearly matching its 4B sibling on SWE-Verifie… | 1/12 | Grok |
| 21 |  | [2115334343870787975](https://x.com/i/status/2115334343870787975) | @sgl_project | SGLang has Day-0 support for Spark-X2.6-1.7B from @SparkLLM, a compact on-device model that stays close to Spark-X2.6-4B with less than half the parameters. > Stronger coding, agentic, … | 1/12 | Astra |

**Stories cutoff:** 6 model votes. A tie crosses the cutoff; all tied items receive equal full-credit eligibility. Average selected position is shown for transparency only. 2 item(s) have the cutoff vote count.

| Item | Votes | Mean selected position | Included |
|---|---|---|---|
| Artificial Analysis Intelligence Index v5 | 6 | 4.00 | Yes |
| Oracle Cloud adds Google TPUs | 6 | 4.17 | Yes |

**Tweets cutoff:** 5 model votes. No count tie crosses the cutoff. 2 item(s) have the cutoff vote count.

## 4. Model report cards

Scores below use the 12-model consensus above. Rows are ordered fastest first.

| Speed rank | Model | Popular headline? | Top-5 stories matched | Top-10 tweets matched | Worker elapsed |
|---|---|---|---|---|---|
| 1 | GLM | No | 4/5 | 8/10 | 3m 38s |
| 2 | Terra | Yes | 3/5 | 3/10 | 3m 58s |
| 3 | Opus | Yes | 4/5 | 8/10 | 7m 29s |
| 4 | Luna | No | 5/5 | 3/10 | 7m 46s |
| 5 | MiniMax | Yes | 3/5 | 6/10 | 8m 38s |
| 6 | Astra | Yes | 4/5 | 7/10 | 11m 56s |
| 7 | Kimi | No | 5/5 | 6/10 | 12m 08s |
| 8 | Qwen | Yes | 5/5 | 7/10 | 15m 57s |
| 9 | DeepSeek Pro | No | 5/5 | 8/10 | 17m 12s |
| 10 | Sol | Yes | 5/5 | 7/10 | 18m 04s |
| 11 | Flash | No | 5/5 | 7/10 | 20m 15s |
| 12 | Grok | Yes | 5/5 | 8/10 | 28m 45s |

### GLM — speed #1

- **Overall: 76/100 — selection rank #7.** Headline 0 × 5 = 0; stories 4 × 9 = 36; tweets 8 × 5 = 40.
- **Headline:** OpenAI announces three AI-produced scientific discoveries in math, computer science and physics
- **Most popular headline selected:** No.
- **Stories:** 4/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Artificial Analysis Intelligence Index v5.
- **Eligible stories not selected (alternatives, not additional penalties):** Liquid AI LFM3 open-weight model family; Oracle Cloud adds Google TPUs.
- **Tweets:** 8/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115132488775524793, 2115207004293853358, 2115126872455475476.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115135061293203537, 2115114030503166385.
- **Speed:** #1/12, 3m 38s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/glm-5-3`.

### Terra — speed #2

- **Overall: 47/100 — selection rank #12.** Headline 1 × 5 = 5; stories 3 × 9 = 27; tweets 3 × 5 = 15.
- **Headline:** Google DeepMind unveils Genie 4 interactive world model
- **Most popular headline selected:** Yes.
- **Stories:** 3/5 matched. Matches: Google DeepMind Genie 4 world model; Liquid AI LFM3 open-weight model family; Oracle Cloud adds Google TPUs.
- **Eligible stories not selected (alternatives, not additional penalties):** OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Artificial Analysis Intelligence Index v5.
- **Tweets:** 3/10 matched. Matched IDs: 2115128329003303107, 2115062200687878157, 2115114030503166385.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115265133467635877, 2115178675050307942, 2114837059462627533, 2115132488775524793, 2115135061293203537, 2115207004293853358, 2115126872455475476.
- **Speed:** #2/12, 3m 58s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/gpt-6-1-terra`.

### Opus — speed #3

- **Overall: 81/100 — selection rank #5.** Headline 1 × 5 = 5; stories 4 × 9 = 36; tweets 8 × 5 = 40.
- **Headline:** Google DeepMind unveils Genie 4 world model with native audio and real-time steering
- **Most popular headline selected:** Yes.
- **Stories:** 4/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Oracle Cloud adds Google TPUs.
- **Eligible stories not selected (alternatives, not additional penalties):** Liquid AI LFM3 open-weight model family; Artificial Analysis Intelligence Index v5.
- **Tweets:** 8/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115132488775524793, 2115135061293203537, 2115207004293853358.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115114030503166385, 2115126872455475476.
- **Speed:** #3/12, 7m 29s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/opus-5-5`.

### Luna — speed #4

- **Overall: 60/100 — selection rank #11.** Headline 0 × 5 = 0; stories 5 × 9 = 45; tweets 3 × 5 = 15.
- **Headline:** OpenAI Publishes AI-Generated Work on Major Math and Computing Conjectures
- **Most popular headline selected:** No.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family; Oracle Cloud adds Google TPUs.
- **Eligible stories not selected (alternatives, not additional penalties):** Artificial Analysis Intelligence Index v5.
- **Tweets:** 3/10 matched. Matched IDs: 2115062200687878157, 2114837059462627533, 2115207004293853358.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115132488775524793, 2115135061293203537, 2115114030503166385, 2115126872455475476.
- **Speed:** #4/12, 7m 46s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/gpt-6-luna-oneoff-14773`.

### MiniMax — speed #5

- **Overall: 62/100 — selection rank #10.** Headline 1 × 5 = 5; stories 3 × 9 = 27; tweets 6 × 5 = 30.
- **Headline:** Google DeepMind releases Genie 4 world model with native audio and real-time steering
- **Most popular headline selected:** Yes.
- **Stories:** 3/5 matched. Matches: Google DeepMind Genie 4 world model; Liquid AI LFM3 open-weight model family; Artificial Analysis Intelligence Index v5.
- **Eligible stories not selected (alternatives, not additional penalties):** OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Oracle Cloud adds Google TPUs.
- **Tweets:** 6/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2115132488775524793, 2115135061293203537.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2114837059462627533, 2115207004293853358, 2115114030503166385, 2115126872455475476.
- **Speed:** #5/12, 8m 38s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/minimax-m3-1-flash`.

### Astra — speed #6

- **Overall: 76/100 — selection rank #7.** Headline 1 × 5 = 5; stories 4 × 9 = 36; tweets 7 × 5 = 35.
- **Headline:** Google previews Genie 4 with native audio and real-time world steering
- **Most popular headline selected:** Yes.
- **Stories:** 4/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family.
- **Eligible stories not selected (alternatives, not additional penalties):** Artificial Analysis Intelligence Index v5; Oracle Cloud adds Google TPUs.
- **Tweets:** 7/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115135061293203537, 2115114030503166385.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115132488775524793, 2115207004293853358, 2115126872455475476.
- **Speed:** #6/12, 11m 56s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/gpt-6-astra`.

### Kimi — speed #7

- **Overall: 75/100 — selection rank #9.** Headline 0 × 5 = 0; stories 5 × 9 = 45; tweets 6 × 5 = 30.
- **Headline:** OpenAI Releases AI-Generated Proofs Across Math, Computer Science and Physics
- **Most popular headline selected:** No.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family; Artificial Analysis Intelligence Index v5.
- **Eligible stories not selected (alternatives, not additional penalties):** Oracle Cloud adds Google TPUs.
- **Tweets:** 6/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115135061293203537, 2115114030503166385, 2115126872455475476.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115062200687878157, 2114837059462627533, 2115132488775524793, 2115207004293853358.
- **Speed:** #7/12, 12m 08s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/kimi-k3-1-pro`.

### Qwen — speed #8

- **Overall: 85/100 — selection rank #2.** Headline 1 × 5 = 5; stories 5 × 9 = 45; tweets 7 × 5 = 35.
- **Headline:** Google DeepMind launches Genie 4, a real-time interactive world model
- **Most popular headline selected:** Yes.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family; Artificial Analysis Intelligence Index v5.
- **Eligible stories not selected (alternatives, not additional penalties):** Oracle Cloud adds Google TPUs.
- **Tweets:** 7/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115132488775524793, 2115126872455475476.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115135061293203537, 2115207004293853358, 2115114030503166385.
- **Speed:** #8/12, 15m 57s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/qwen-3-8-max-0902`.

### DeepSeek Pro — speed #9

- **Overall: 85/100 — selection rank #2.** Headline 0 × 5 = 0; stories 5 × 9 = 45; tweets 8 × 5 = 40.
- **Headline:** OpenAI announces three major scientific discoveries in math, computer science and physics
- **Most popular headline selected:** No.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family; Artificial Analysis Intelligence Index v5.
- **Eligible stories not selected (alternatives, not additional penalties):** Oracle Cloud adds Google TPUs.
- **Tweets:** 8/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115132488775524793, 2115135061293203537, 2115126872455475476.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115207004293853358, 2115114030503166385.
- **Speed:** #9/12, 17m 12s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/deepseek-v4-pro`.

### Sol — speed #10

- **Overall: 85/100 — selection rank #2.** Headline 1 × 5 = 5; stories 5 × 9 = 45; tweets 7 × 5 = 35.
- **Headline:** Google DeepMind previews Genie 4 with native audio and live world steering
- **Most popular headline selected:** Yes.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family; Oracle Cloud adds Google TPUs.
- **Eligible stories not selected (alternatives, not additional penalties):** Artificial Analysis Intelligence Index v5.
- **Tweets:** 7/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115207004293853358, 2115114030503166385.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115132488775524793, 2115135061293203537, 2115126872455475476.
- **Speed:** #10/12, 18m 04s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/gpt-6-1-sol`.

### Flash — speed #11

- **Overall: 80/100 — selection rank #6.** Headline 0 × 5 = 0; stories 5 × 9 = 45; tweets 7 × 5 = 35.
- **Headline:** OpenAI says its models produced proofs in math, computer science and physics
- **Most popular headline selected:** No.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Artificial Analysis Intelligence Index v5; Oracle Cloud adds Google TPUs.
- **Eligible stories not selected (alternatives, not additional penalties):** Liquid AI LFM3 open-weight model family.
- **Tweets:** 7/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115132488775524793, 2115135061293203537, 2115207004293853358, 2115126872455475476.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115062200687878157, 2114837059462627533, 2115114030503166385.
- **Speed:** #11/12, 20m 15s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/deepseek-v4-1-flash-1017`.

### Grok — speed #12

- **Overall: 90/100 — selection rank #1.** Headline 1 × 5 = 5; stories 5 × 9 = 45; tweets 8 × 5 = 40.
- **Headline:** Google DeepMind announces Genie 4 world model
- **Most popular headline selected:** Yes.
- **Stories:** 5/5 matched. Matches: Google DeepMind Genie 4 world model; OpenAI AI-generated scientific results / proof claims; Anthropic drug-development research and Mithril Medicine; Liquid AI LFM3 open-weight model family; Oracle Cloud adds Google TPUs.
- **Eligible stories not selected (alternatives, not additional penalties):** Artificial Analysis Intelligence Index v5.
- **Tweets:** 8/10 matched. Matched IDs: 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2114837059462627533, 2115132488775524793, 2115207004293853358, 2115114030503166385.
- **Eligible tweet IDs not selected (alternatives, not additional penalties):** 2115135061293203537, 2115126872455475476.
- **Speed:** #12/12, 28m 45s.
- **Evidence directory:** `briefs/model-tests/2026-10-28/grok-4-7`.

## 5. Audit appendix: original selections

Original ordered selections and event mappings used in the counts.

### Flash

**Original headline:** OpenAI says its models produced proofs in math, computer science and physics

1. [OpenAI says its models produced proofs in math, computer science and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
2. [Google DeepMind unveils Genie 4 with native audio and real-time steering](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
3. [Anthropic reports early preclinical drug-development results with Claude](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**
4. [Oracle puts Google TPUs and OpenAI's Jalapeno chip on its cloud](https://www.cnbc.com/2026/10/27/oracle-openai-chatgpt-codex-google-tpus.html) → **Oracle Cloud adds Google TPUs**
5. [Artificial Analysis Intelligence Index v5 widens the open-weights gap](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) → **Artificial Analysis Intelligence Index v5**

**Tweet IDs in selected order:** 2115114028338962672, 2115178675050307942, 2115265133467635877, 2115128329003303107, 2115132488775524793, 2115126872455475476, 2115207004293853358, 2115135061293203537, 2115129110930628859, 2115171788812669225.

### DeepSeek Pro

**Original headline:** OpenAI announces three major scientific discoveries in math, computer science and physics

1. [OpenAI announces three major scientific discoveries in math, computer science and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
2. [Google DeepMind launches Genie 4 interactive world model](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
3. [Liquid AI open-sources LFM3, six 2B-class foundation models on one backbone](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
4. [Artificial Analysis launches Intelligence Index v5, widening the open-weight gap](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) → **Artificial Analysis Intelligence Index v5**
5. [Anthropic reports early drug-discovery results with six partner organizations](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**

**Tweet IDs in selected order:** 2114837059462627533, 2115232001275924722, 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115062200687878157, 2115132488775524793, 2115126872455475476, 2115135061293203537, 2115129110930628859.

### GLM

**Original headline:** OpenAI announces three AI-produced scientific discoveries in math, computer science and physics

1. [OpenAI announces three AI-produced scientific discoveries in math, computer science and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
2. [Google DeepMind announces Genie 4, a real-time interactive world model with native audio](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
3. [Artificial Analysis Intelligence Index v5 finds open weights models falling further behind](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) → **Artificial Analysis Intelligence Index v5**
4. [Anthropic reports early progress using Claude in drug development](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**
5. [Cognition launches FrontierCode 2.0, a merge-judgment coding benchmark topped at 45%](https://cognition.com/blog/frontier-code-2.0) → **Cognition FrontierCode 2.0 benchmark**

**Tweet IDs in selected order:** 2114837059462627533, 2115265133467635877, 2115232001275924722, 2115178675050307942, 2115132488775524793, 2115126872455475476, 2115128329003303107, 2115062200687878157, 2115099284224008200, 2115207004293853358.

### Sol

**Original headline:** Google DeepMind previews Genie 4 with native audio and live world steering

1. [Google DeepMind previews Genie 4 with native audio and live world steering](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [Liquid AI releases six open-weight LFM3 models for specialized on-device AI](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
3. [OpenAI opens AI-generated science claims to independent examination](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
4. [Anthropic expands drug-development research and acquires Mithril Medicine](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**
5. [Oracle plans Google TPU access on OCI beginning in 2027](https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/) → **Oracle Cloud adds Google TPUs**

**Tweet IDs in selected order:** 2115114030503166385, 2115128329003303107, 2114837059462627533, 2115062200687878157, 2115178675050307942, 2115265133467635877, 2115101113666134276, 2115120550230020113, 2115204127013929072, 2115207004293853358.

### Terra

**Original headline:** Google DeepMind unveils Genie 4 interactive world model

1. [Google DeepMind unveils Genie 4 interactive world model](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [Liquid AI releases LFM3 small multimodal model family](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
3. [Ant releases Ling 3.1 Flash 1019 model weights](https://www.orcarouter.ai/blog/ling-3-1-flash-1019-open-weights) → **InclusionAI / Ant Ling-3.1-flash-1019 weights**
4. [Baidu releases Unlimited OCR 2 for long-document parsing](https://huggingface.co/baidu/Unlimited-OCR-2) → **Baidu Unlimited OCR 2**
5. [Oracle plans to offer Google TPUs in its cloud](https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/) → **Oracle Cloud adds Google TPUs**

**Tweet IDs in selected order:** 2115114030503166385, 2115128329003303107, 2115062200687878157, 2114945367712366718, 2115265171233120627, 2115097540320506069, 2115156635954090345, 2115120550230020113, 2115101219119325606, 2115204127013929072.

### Astra

**Original headline:** Google previews Genie 4 with native audio and real-time world steering

1. [Google previews Genie 4 with native audio and real-time world steering](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [Liquid AI releases LFM3 open-weight models for on-device multimodal AI](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
3. [InclusionAI releases Ling-3.1-flash-1019 and its base model](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019) → **InclusionAI / Ant Ling-3.1-flash-1019 weights**
4. [OpenAI releases scientific proof claims for academic scrutiny](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
5. [Anthropic details drug-development partnerships and acquires Mithril Medicine](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**

**Tweet IDs in selected order:** 2115114030503166385, 2115128329003303107, 2115062200687878157, 2114837059462627533, 2115265133467635877, 2115178675050307942, 2115101113666134276, 2115135061293203537, 2115204127013929072, 2115334343870787975.

### Luna

**Original headline:** OpenAI Publishes AI-Generated Work on Major Math and Computing Conjectures

1. [OpenAI Publishes AI-Generated Work on Major Math and Computing Conjectures](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
2. [Google DeepMind introduces Genie 4 for real-time interactive world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
3. [Liquid AI releases six-model LFM3 family for multimodal and on-device use](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
4. [Anthropic reports early drug-development work and begins in-house discovery](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**
5. [Oracle to offer Google TPUs through OCI, expanding hyperscale AI compute choice](https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/) → **Oracle Cloud adds Google TPUs**

**Tweet IDs in selected order:** 2115232001275924722, 2115128330848751659, 2114837059462627533, 2115265177046389089, 2115233234732917055, 2115062200687878157, 2115099284224008200, 2115207004293853358, 2115132493259321443, 2115196931979014345.

### Grok

**Original headline:** Google DeepMind announces Genie 4 world model

1. [Google DeepMind announces Genie 4 world model](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [Liquid AI releases open-weight LFM3 model family](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
3. [Oracle and Google to offer TPUs on Oracle Cloud](https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/) → **Oracle Cloud adds Google TPUs**
4. [OpenAI publishes model results for outside verification](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
5. [Anthropic reports early Claude drug-development results](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**

**Tweet IDs in selected order:** 2115114030503166385, 2115128329003303107, 2114837059462627533, 2115178675050307942, 2115265133467635877, 2115132488775524793, 2115062200687878157, 2115120550230020113, 2115207004293853358, 2115232805416468826.

### MiniMax

**Original headline:** Google DeepMind releases Genie 4 world model with native audio and real-time steering

1. [Google DeepMind releases Genie 4 world model with native audio and real-time steering](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [Liquid AI ships LFM3 open-weight family for on-device multimodal agents](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
3. [Microsoft's MAI-Image-2.7-Preview lands at number two on image editing leaderboards](https://x.com/mustafasuleyman/status/2115099284224008200) → **Microsoft MAI-Image-2.7-Preview**
4. [InclusionAI open-sources Ling-3.1-flash-1019 with 1M token context](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019) → **InclusionAI / Ant Ling-3.1-flash-1019 weights**
5. [Artificial Analysis puts 60 percent of Intelligence Index v5 behind private test sets](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) → **Artificial Analysis Intelligence Index v5**

**Tweet IDs in selected order:** 2115265133467635877, 2115114028338962672, 2115128329003303107, 2115178675050307942, 2115062200687878157, 2115233234732917055, 2115132488775524793, 2115135061293203537, 2115156635954090345, 2115099284224008200.

### Qwen

**Original headline:** Google DeepMind launches Genie 4, a real-time interactive world model

1. [Google DeepMind launches Genie 4, a real-time interactive world model](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [OpenAI announces three scientific discoveries in math, computer science and physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
3. [Artificial Analysis launches Intelligence Index v5 with mostly private benchmarks](https://x.com/ArtificialAnlys/status/2115265133467635877) → **Artificial Analysis Intelligence Index v5**
4. [Anthropic announces drug-discovery partnerships with six medicine developers](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**
5. [Liquid AI releases LFM3, an open family of on-device multimodal models](https://liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**

**Tweet IDs in selected order:** 2115114028338962672, 2114837059462627533, 2115265133467635877, 2115178675050307942, 2115128329003303107, 2115132488775524793, 2115126872455475476, 2115099284224008200, 2115120550230020113, 2115062200687878157.

### Kimi

**Original headline:** OpenAI Releases AI-Generated Proofs Across Math, Computer Science and Physics

1. [OpenAI Releases AI-Generated Proofs Across Math, Computer Science and Physics](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
2. [Google DeepMind Introduces Genie 4 With Native Audio and Real-Time Steering](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
3. [Liquid AI Launches Six Open-Weight LFM3 Models for On-Device Agents](https://www.liquid.ai/blog/lfm3) → **Liquid AI LFM3 open-weight model family**
4. [Artificial Analysis Overhauls Intelligence Index With Mostly Private Evaluations](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) → **Artificial Analysis Intelligence Index v5**
5. [Anthropic Expands Claude Research Into Drug Discovery and Life Sciences](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**

**Tweet IDs in selected order:** 2114839833134674351, 2115114030503166385, 2115128329003303107, 2115265133467635877, 2115178675050307942, 2115155299334246584, 2115135061293203537, 2115097540320506069, 2115126872455475476, 2115175550465507710.

### Opus

**Original headline:** Google DeepMind unveils Genie 4 world model with native audio and real-time steering

1. [Google DeepMind unveils Genie 4 world model with native audio and real-time steering](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) → **Google DeepMind Genie 4 world model**
2. [OpenAI says its models disproved the Exponential Time Hypothesis, with Anthropic reporting a separate Claude result](https://openai.com/index/building-scientific-understanding-with-academic-communities/) → **OpenAI AI-generated scientific results / proof claims**
3. [Oracle to offer Google TPUs and OpenAI's Jalapeño chip on its cloud](https://www.cnbc.com/2026/10/27/oracle-openai-chatgpt-codex-google-tpus.html) → **Oracle Cloud adds Google TPUs**
4. [Anthropic details drug-development partnerships and starts its own drug discovery programs](https://www.anthropic.com/research/early-progress-drug-development) → **Anthropic drug-development research and Mithril Medicine**
5. [Banks and Blackstone arrange $63 billion to finance Broadcom chips leased to Anthropic](https://www.prnewswire.com/news-releases/bank-of-america-blackstone-citi-and-morgan-stanley-announce-landmark-63-billion-financing-structure-to-enable-ai-compute-capacity-in-partnership-with-broadcom-302919849.html) → **Broadcom / Anthropic $63 billion compute financing**

**Tweet IDs in selected order:** 2115114028338962672, 2114837059462627533, 2115265133467635877, 2115178675050307942, 2115132488775524793, 2115207004293853358, 2115128329003303107, 2115062200687878157, 2115135061293203537, 2115097540320506069.

## Verification

- 12 distinct selected models; every selected HTML exists.
- Exactly 60 story selections; 11 unique story groups.
- Exactly 120 tweet selections; 33 distinct IDs; every selected ID appears in that run’s rendered HTML.
- 2 distinct headline groups; headline lead URL matches the first story for every selected run.
- Count conservation: headline votes = 12, story votes = 60, tweet votes = 120. No duplicate event or tweet votes within a model.
- Inputs: saved canonical edition, headline.json, run.json and HTML for each listed directory. Original evidence was not modified. Companion local analysis-inputs-12-models-14824.json retains mappings and SHA256 input fingerprints.
- Validation scope: selection extraction, grouping review, arithmetic and Markdown structure. This is not a fresh source-fidelity or visual-quality certification of the newsletters.

## Cohort and protocol audit

- Independently rehashed all 24 local X/web source copies: all match the required frozen archives. All twelve recorded editions and model attributions match their selected runs; required artifacts exist and saved deterministic validator outcomes were inspected.
- X SHA-256: `951596dc50640a41ea128c0e6d87927d68b039682a403d237dba5ef810708403`.
- Web SHA-256: `875409635787a8c68376199f8ada94485b62e8caac33efb35e72efe2626d23b3`.
- Kimi: intended run `1b31655b-50c7-4085-bfb3-35bfd387339e`, first action 23:17:46Z, end 23:29:54Z; Opus: intended run `8ae2a099-b1ba-4d25-8064-72f215905217`, first action 23:17:31Z, end 23:25:00Z. Both starts follow the authorized launch thresholds. Terminal artifact statuses are review_required and complete_local respectively, with expected model routes and no fallback reported.
- Scheduler get/runs for other jobs is unavailable in this scheduled turn (the automation tool is restricted to the current job). Intended attempt identity and completion are verified from each run record and completion artifacts, not an independent scheduler receipt.
- Both reruns recorded template SHA-256 `84ec7b7f1be5217a85ff1a7c86404f39081ea43c3b0ddf58f5512aecd3b80922`. The original ten do not establish a common recorded template hash; identical prompts across all twelve are not claimed.
- Ancillary copies differ: two VIP file hashes and several history-file hashes. The table below records actual byte hashes (prefixes; full hashes in companion JSON). These may include serialization/metadata differences; they are not assumed semantically identical. Opus explicitly records six history-index dates, with the earliest date absent from the index but its historical files present. Kimi records seven retained history dates.
- Luna uses the authorized adjusted tweet-display normalization protocol. Worker source-reading paths, history handling and preview methods also differ. This is a shared-X/web-evidence selection comparison, not a fully controlled model benchmark.
- Kimi, Terra, Astra and Luna retain review_required status. Kimi had no browser visual preview; Opus generated a screenshot but did not inspect it visually. No visual-quality certification is inferred from complete_local or consensus scores.
- Luna’s run record retains a stale validators.pending=true field alongside detailed passing validation_outcomes; this report uses those final detailed outcomes, not the stale placeholder.

| Model | VIP SHA-256 prefix | History SHA-256 prefix |
|---|---|---|
| Flash | 37dc1a9f4fe0 | 50f92ecad12c |
| DeepSeek Pro | 37dc1a9f4fe0 | a7e50e4905b1 |
| GLM | 3128d57004cc | a7e50e4905b1 |
| Sol | 37dc1a9f4fe0 | e948f6d6cbdb |
| Terra | 3128d57004cc | e948f6d6cbdb |
| Astra | 3128d57004cc | a7e50e4905b1 |
| Luna | 3128d57004cc | e948f6d6cbdb |
| Grok | 37dc1a9f4fe0 | cf124c5d2cf2 |
| MiniMax | 3128d57004cc | e948f6d6cbdb |
| Qwen | 37dc1a9f4fe0 | a7e50e4905b1 |
| Kimi | 3128d57004cc | e948f6d6cbdb |
| Opus | 3128d57004cc | a7e50e4905b1 |
