# Intent Catalogue

**136 Intents in 134 families on the Telegraph network.**

Read straight from the node, so every kind below is the kind the network really scores that
Intent as. Regenerate with `python3 scripts/sync_catalog.py` and this script.

## What the network needs, by kind

| Kind | Evaluation material it is scored on |
|---|---|
| **deterministic** | **Truth sources**: free public APIs (no key) that answer the Intent's question. The network asks a few each epoch and checks miners against the middle answer. |
| **hybrid** | **Truth sources** for the checkable part and **question pairs** for the rest. |
| **judgment** | **Question pairs**: a real question with a better and a worse answer. |

Anyone can add material. It goes to the network through Anjoman:
[Evaluate](https://anjoman.ai/dashboard/eval). Every Intent name below opens that page with the Intent already chosen.
The format, the limits and the reasons a row is turned down: [Contribute Evaluation Data](https://anjoman.ai/docs/scoring/contribute-evaluation-data).

## Scoring modules: which families take one

A scoring module is registered on a **family**, never on a single Intent, and the
family's own kind decides which kind it takes. A family's module also scores only the
Intents of the family's own kind. So:

- A **judgment** or **hybrid** family takes an **evaluator adapter**. A better adapter can replace the one in place, so this is open work.
- A **deterministic** family takes a **comparator module**. A comparator has no model: it only has to compute the network's fixed comparison rule, so there is no better one to build.
- A **deterministic Intent under a judgment family** is scored by the network's own shared comparator. **Nothing registered on that family can score it**, so there is no module to build for it: one sent there waits as `pending` with `awaiting_compatible_material` and never goes live. The Contribute column says so per Intent.

How to build and register one: [Build an Evaluator Adapter](https://anjoman.ai/docs/scoring/build-a-scoring-module).

## No open Issue for your Intent?

You can still contribute. The network takes material for every Intent listed here,
whether or not a bounty exists for it. GitHub is where bounty work is claimed, proven
and approved; Anjoman is where the network receives the work and decides whether it
uses it. The Bounty column finds any open Issue that names the Intent.

## AI & Machine Learning

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`LLM_OUTPUT_EVALUATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LLM_OUTPUT_EVALUATION_GENERAL) | judgment | `LLM_OUTPUT_EVALUATION` (judgment) | question pairs · adapter on `LLM_OUTPUT_EVALUATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+LLM_OUTPUT_EVALUATION_GENERAL) |
| [`LANGUAGE_TRANSLATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LANGUAGE_TRANSLATION_GENERAL) | judgment | `LANGUAGE_TRANSLATION` (judgment) | question pairs · adapter on `LANGUAGE_TRANSLATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+LANGUAGE_TRANSLATION_GENERAL) |
| [`QUESTION_ANSWERING_GENERAL`](https://anjoman.ai/dashboard/eval?intent=QUESTION_ANSWERING_GENERAL) | judgment | `QUESTION_ANSWERING` (judgment) | question pairs · adapter on `QUESTION_ANSWERING` | [open](../../../issues?q=is%3Aissue+is%3Aopen+QUESTION_ANSWERING_GENERAL) |
| [`TEXT_SUMMARIZATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TEXT_SUMMARIZATION_GENERAL) | judgment | `TEXT_SUMMARIZATION` (judgment) | question pairs · adapter on `TEXT_SUMMARIZATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_SUMMARIZATION_GENERAL) |
| [`CHATBOT_CONVERSATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CHATBOT_CONVERSATION_GENERAL) | judgment | `CHATBOT_CONVERSATION` (judgment) | question pairs · adapter on `CHATBOT_CONVERSATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CHATBOT_CONVERSATION_GENERAL) |
| [`ENTITY_EXTRACTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=ENTITY_EXTRACTION_GENERAL) | judgment | `ENTITY_EXTRACTION` (judgment) | question pairs · adapter on `ENTITY_EXTRACTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+ENTITY_EXTRACTION_GENERAL) |
| [`SEMANTIC_SIMILARITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SEMANTIC_SIMILARITY_GENERAL) | judgment | `SEMANTIC_SIMILARITY` (judgment) | question pairs · adapter on `SEMANTIC_SIMILARITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SEMANTIC_SIMILARITY_GENERAL) |
| [`SENTIMENT_ANALYSIS_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SENTIMENT_ANALYSIS_GENERAL) | judgment | `SENTIMENT_ANALYSIS` (judgment) | question pairs · adapter on `SENTIMENT_ANALYSIS` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SENTIMENT_ANALYSIS_GENERAL) |
| [`SPEECH_TO_TEXT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SPEECH_TO_TEXT_GENERAL) | judgment | `SPEECH_TO_TEXT` (judgment) | question pairs · adapter on `SPEECH_TO_TEXT` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SPEECH_TO_TEXT_GENERAL) |
| [`TEXT_CLASSIFICATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TEXT_CLASSIFICATION_GENERAL) | judgment | `TEXT_CLASSIFICATION` (judgment) | question pairs · adapter on `TEXT_CLASSIFICATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_CLASSIFICATION_GENERAL) |
| [`EMBEDDING_GENERATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=EMBEDDING_GENERATION_GENERAL) | judgment | `EMBEDDING_GENERATION` (judgment) | question pairs · adapter on `EMBEDDING_GENERATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+EMBEDDING_GENERATION_GENERAL) |
| [`IMAGE_CAPTIONING_GENERAL`](https://anjoman.ai/dashboard/eval?intent=IMAGE_CAPTIONING_GENERAL) | judgment | `IMAGE_CAPTIONING` (judgment) | question pairs · adapter on `IMAGE_CAPTIONING` | [open](../../../issues?q=is%3Aissue+is%3Aopen+IMAGE_CAPTIONING_GENERAL) |
| [`KEYWORD_EXTRACTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=KEYWORD_EXTRACTION_GENERAL) | judgment | `KEYWORD_EXTRACTION` (judgment) | question pairs · adapter on `KEYWORD_EXTRACTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+KEYWORD_EXTRACTION_GENERAL) |
| [`TEXT_TO_SPEECH_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TEXT_TO_SPEECH_GENERAL) | judgment | `TEXT_TO_SPEECH` (judgment) | question pairs · adapter on `TEXT_TO_SPEECH` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_TO_SPEECH_GENERAL) |

### Details

**`LLM_OUTPUT_EVALUATION`** — judgment family · tier mandatory · H2 missions: Model Economy

Evaluates generative model responses against factual ground truth, citation fidelity, hallucination markers, and safety guardrails.

#### `LLM_OUTPUT_EVALUATION_GENERAL`

judgment · asks `task`, `output` · answers `rating`, `score`, `strengths`, `errors`

Query supplies a generative model's output and asks for it to be judged: factual fidelity, citation support, hallucination markers, tone or safety, usually against the prompt or a reference. Example: "Here is a model answer and its cited sources: rate it for factual accuracy, citation support and hallucination." → LLM_OUTPUT_EVALUATION_GENERAL. Not: "Was this paragraph written by an AI or a human?" (authorship detection, not quality) → AI_TEXT_DETECTION_GENERAL. Not: "Did the agent complete this task correctly?" (scoring an execution against a rubric) → TASK_EXECUTION_QUALITY_GENERAL.

Contribute question pairs · adapter on `LLM_OUTPUT_EVALUATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LLM_OUTPUT_EVALUATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LLM_OUTPUT_EVALUATION_GENERAL)

**`LANGUAGE_TRANSLATION`** — judgment family · tier existing · H2 missions: Consumer Platform, Personal Agent

Translates multilingual text between source and target language pairs preserving semantic intent and idiom.

#### `LANGUAGE_TRANSLATION_GENERAL`

judgment · asks `text`, `target_language` · answers `translation`, `target_language`, `source_language`, `brief`

Query supplies text and names a target language, asking for translation between two languages. Example: "Translate this sentence into French: 'Where is the nearest train station?'" → LANGUAGE_TRANSLATION_GENERAL. Not: "What does 'où' mean in French?" (asks about a single word's meaning, not a translation task) → CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `LANGUAGE_TRANSLATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LANGUAGE_TRANSLATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LANGUAGE_TRANSLATION_GENERAL)

**`QUESTION_ANSWERING`** — judgment family · tier existing · H2 missions: Institutional Markets, Legal, Consumer Platform, Personal Agent, Model Economy

Answers open-domain and context-bounded user queries with cited factual assertions and logical deductions.

#### `QUESTION_ANSWERING_GENERAL`

judgment

Answers open-domain and context-bounded user queries with cited factual assertions and logical deductions.

Contribute question pairs · adapter on `QUESTION_ANSWERING`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=QUESTION_ANSWERING_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+QUESTION_ANSWERING_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`TEXT_SUMMARIZATION`** — judgment family · tier existing · H2 missions: Personal Agent

Generates concise, factual executive summaries capturing primary themes of long-form source documents.

#### `TEXT_SUMMARIZATION_GENERAL`

judgment

Generates concise, factual executive summaries capturing primary themes of long-form source documents.

Contribute question pairs · adapter on `TEXT_SUMMARIZATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TEXT_SUMMARIZATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_SUMMARIZATION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`CHATBOT_CONVERSATION`** — judgment family · tier existing · H2 missions: —

Maintains multi-turn conversational context, tone alignment, and empathetic response delivery.

#### `CHATBOT_CONVERSATION_GENERAL`

judgment

Maintains multi-turn conversational context, tone alignment, and empathetic response delivery.

Contribute question pairs · adapter on `CHATBOT_CONVERSATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CHATBOT_CONVERSATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CHATBOT_CONVERSATION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`ENTITY_EXTRACTION`** — judgment family · tier existing · H2 missions: —

Extracts named entities (people, organizations, locations, dates) with character offsets from unstructured text.

#### `ENTITY_EXTRACTION_GENERAL`

judgment

Extracts named entities (people, organizations, locations, dates) with character offsets from unstructured text.

Contribute question pairs · adapter on `ENTITY_EXTRACTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=ENTITY_EXTRACTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+ENTITY_EXTRACTION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SEMANTIC_SIMILARITY`** — judgment family · tier existing · H2 missions: —

Calculates mathematical cosine similarity and semantic relatedness distance between pairs of sentences.

#### `SEMANTIC_SIMILARITY_GENERAL`

judgment

Calculates mathematical cosine similarity and semantic relatedness distance between pairs of sentences.

Contribute question pairs · adapter on `SEMANTIC_SIMILARITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SEMANTIC_SIMILARITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SEMANTIC_SIMILARITY_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SENTIMENT_ANALYSIS`** — judgment family · tier existing · H2 missions: —

Scores emotional valence, polarity (positive/negative/neutral), and subjective tone in textual messages.

#### `SENTIMENT_ANALYSIS_GENERAL`

judgment · asks `text` · answers `sentiment`, `score`, `reason`

Query supplies text and asks what sentiment or emotional tone it expresses. Example: "What's the sentiment of this review: 'The product broke after one day, terrible quality.'?" → SENTIMENT_ANALYSIS_GENERAL. Not: "What category does this review belong to: quality, shipping, or price?" (asks for a label/category, not emotional tone) → TEXT_CLASSIFICATION_GENERAL.

Contribute question pairs · adapter on `SENTIMENT_ANALYSIS`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SENTIMENT_ANALYSIS_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SENTIMENT_ANALYSIS_GENERAL)

**`SPEECH_TO_TEXT`** — judgment family · tier existing · H2 missions: —

Transcribes spoken audio streams into punctuated, timestamped text transcriptions with speaker diarization.

#### `SPEECH_TO_TEXT_GENERAL`

judgment

Transcribes spoken audio streams into punctuated, timestamped text transcriptions with speaker diarization.

Contribute question pairs · adapter on `SPEECH_TO_TEXT`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SPEECH_TO_TEXT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SPEECH_TO_TEXT_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`TEXT_CLASSIFICATION`** — judgment family · tier existing · H2 missions: —

Assigns predefined taxonomic category tags and topic hierarchies to incoming text documents.

#### `TEXT_CLASSIFICATION_GENERAL`

judgment · asks `text`, `categories` · answers `category`, `reason`, `confidence`

Query supplies text and asks for it to be assigned to one or more predefined categories or labels. Example: "Classify this support ticket as billing, technical, or account issue: 'I can't log into my account.'" → TEXT_CLASSIFICATION_GENERAL. Not: "Is this ticket written in a frustrated tone?" (asks about emotional tone, not a category label) → SENTIMENT_ANALYSIS_GENERAL.

Contribute question pairs · adapter on `TEXT_CLASSIFICATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TEXT_CLASSIFICATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_CLASSIFICATION_GENERAL)

**`EMBEDDING_GENERATION`** — judgment family · tier existing · H2 missions: —

Transforms input text strings into standardized high-dimensional float vector embeddings for retrieval systems.

#### `EMBEDDING_GENERATION_GENERAL`

judgment

Transforms input text strings into standardized high-dimensional float vector embeddings for retrieval systems.

Contribute question pairs · adapter on `EMBEDDING_GENERATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=EMBEDDING_GENERATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+EMBEDDING_GENERATION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`IMAGE_CAPTIONING`** — judgment family · tier existing · H2 missions: Consumer Platform, Autonomous Systems

Generates descriptive, contextual alt-text captions describing the primary subjects and scenes in image files.

#### `IMAGE_CAPTIONING_GENERAL`

judgment

Generates descriptive, contextual alt-text captions describing the primary subjects and scenes in image files.

Contribute question pairs · adapter on `IMAGE_CAPTIONING`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=IMAGE_CAPTIONING_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+IMAGE_CAPTIONING_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`KEYWORD_EXTRACTION`** — judgment family · tier existing · H2 missions: —

Extracts representative topical keywords, keyphrases, and n-grams from body text.

#### `KEYWORD_EXTRACTION_GENERAL`

judgment

Extracts representative topical keywords, keyphrases, and n-grams from body text.

Contribute question pairs · adapter on `KEYWORD_EXTRACTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=KEYWORD_EXTRACTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+KEYWORD_EXTRACTION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`TEXT_TO_SPEECH`** — judgment family · tier existing · H2 missions: —

Synthesizes natural-sounding spoken voice waveforms from text input with adjustable emotion and cadence.

#### `TEXT_TO_SPEECH_GENERAL`

judgment

Synthesizes natural-sounding spoken voice waveforms from text input with adjustable emotion and cadence.

Contribute question pairs · adapter on `TEXT_TO_SPEECH`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TEXT_TO_SPEECH_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_TO_SPEECH_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

## Blockchain & Web3

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`CROSS_CHAIN_STATE_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CROSS_CHAIN_STATE_VERIFY_GENERAL) | deterministic | `CROSS_CHAIN_STATE_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+CROSS_CHAIN_STATE_VERIFY_GENERAL) |
| [`EVENT_OUTCOME_RESOLUTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=EVENT_OUTCOME_RESOLUTION_GENERAL) | judgment | `EVENT_OUTCOME_RESOLUTION` (judgment) | question pairs · adapter on `EVENT_OUTCOME_RESOLUTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+EVENT_OUTCOME_RESOLUTION_GENERAL) |
| [`LIQUIDITY_DEPTH_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LIQUIDITY_DEPTH_VERIFY_GENERAL) | deterministic | `LIQUIDITY_DEPTH_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+LIQUIDITY_DEPTH_VERIFY_GENERAL) |
| [`ONCHAIN_METRIC_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=ONCHAIN_METRIC_VERIFY_GENERAL) | deterministic | `ONCHAIN_METRIC_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+ONCHAIN_METRIC_VERIFY_GENERAL) |
| [`WASH_TRADING_DETECTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=WASH_TRADING_DETECTION_GENERAL) | judgment | `WASH_TRADING_DETECTION` (judgment) | question pairs · adapter on `WASH_TRADING_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+WASH_TRADING_DETECTION_GENERAL) |
| [`ASSET_RESERVE_ATTESTATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=ASSET_RESERVE_ATTESTATION_GENERAL) | deterministic | `ASSET_RESERVE_ATTESTATION` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+ASSET_RESERVE_ATTESTATION_GENERAL) |
| [`CRYPTO_TRANSFER_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CRYPTO_TRANSFER_VERIFY_GENERAL) | deterministic | `CRYPTO_TRANSFER_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+CRYPTO_TRANSFER_VERIFY_GENERAL) |
| [`SMART_CONTRACT_AUDIT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SMART_CONTRACT_AUDIT_GENERAL) | judgment | `SMART_CONTRACT_AUDIT` (judgment) | question pairs · adapter on `SMART_CONTRACT_AUDIT` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SMART_CONTRACT_AUDIT_GENERAL) |
| [`CRYPTO_YIELD_RATE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CRYPTO_YIELD_RATE_GENERAL) | deterministic | `CRYPTO_YIELD_RATE` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+CRYPTO_YIELD_RATE_GENERAL) |
| [`TOKEN_TOTAL_SUPPLY_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TOKEN_TOTAL_SUPPLY_VERIFY_GENERAL) | deterministic | `TOKEN_TOTAL_SUPPLY_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+TOKEN_TOTAL_SUPPLY_VERIFY_GENERAL) |
| [`VALIDATOR_PERFORMANCE_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=VALIDATOR_PERFORMANCE_VERIFY_GENERAL) | deterministic | `VALIDATOR_PERFORMANCE_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+VALIDATOR_PERFORMANCE_VERIFY_GENERAL) |

### Details

**`CROSS_CHAIN_STATE_VERIFY`** — judgment family · tier mandatory · H2 missions: Stablecoin

Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.

#### `CROSS_CHAIN_STATE_VERIFY_GENERAL`

deterministic

Query asks whether a state root, Merkle-Patricia proof, block header or bridge message from one chain verifies against another. Requires two named chains and a specific proof, header or message. Example: "Verify that the LayerZero message with nonce 4412 from arbitrum executed on base and that the committed state root matches." → CROSS_CHAIN_STATE_VERIFY_GENERAL. Not: "How do cross-chain bridges work?" (conceptual, nothing supplied to verify) → CHAT_COMPLETION_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CROSS_CHAIN_STATE_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CROSS_CHAIN_STATE_VERIFY_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`EVENT_OUTCOME_RESOLUTION`** — judgment family · tier mandatory · H2 missions: Web3 Native & DeFi

Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.

#### `EVENT_OUTCOME_RESOLUTION_GENERAL`

judgment · asks `event` · answers `event`, `outcome`, `resolved_yes`, `winner`, `resolved_at`, `sources`

Query names a specific real-world event with a settled or settleable outcome (an election, a fixture, a flight, a contract condition) and asks what the outcome actually was, for a prediction market or conditional contract to resolve against. Requires a named, checkable event. Example: "Did flight UA328 on 2026-03-11 land before 18:00 local? Resolve this market." → EVENT_OUTCOME_RESOLUTION_GENERAL. Not: "Who do you think will win the election?" (asks for a prediction, not the resolution of a determinable event) → CHAT_COMPLETION_GENERAL. Not: "Who won the Lakers vs Celtics game last night?" (a plain sports result with no market to settle) → GAME_RESULT_GENERAL.

Contribute question pairs · adapter on `EVENT_OUTCOME_RESOLUTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=EVENT_OUTCOME_RESOLUTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+EVENT_OUTCOME_RESOLUTION_GENERAL)

**`LIQUIDITY_DEPTH_VERIFY`** — judgment family · tier mandatory · H2 missions: Exchange, Stablecoin, Institutional Markets, Asset Management, Web3 Native & DeFi

Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.

#### `LIQUIDITY_DEPTH_VERIFY_GENERAL`

deterministic · asks `pool`, `chain` · answers `liquidity_usd`

Query names a market, pair or pool and asks for order book depth, bid-ask spread, or the slippage a stated trade size would incur at a point in time. Example: "What is the bid-ask depth and expected slippage on a 50 ETH sell into the WETH/USDC pool on base right now?" → LIQUIDITY_DEPTH_VERIFY_GENERAL. Not: "How much total value is locked in that pool?" (a TVL total, not depth at a size) → TVL_LOOKUP_GENERAL. Not: "Which venue should I route this trade through?" (a routing decision) → OPTIMAL_EXECUTION_ROUTE_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LIQUIDITY_DEPTH_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LIQUIDITY_DEPTH_VERIFY_GENERAL)

**`ONCHAIN_METRIC_VERIFY`** — judgment family · tier mandatory · H2 missions: Exchange, Asset Management, Web3 Native & DeFi

Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.

#### `ONCHAIN_METRIC_VERIFY_GENERAL`

deterministic · asks `address`, `block` · answers `balance_gwei`, `address`, `block`, `chain`

Query asks for a specific value read from a blockchain node at a stated block height or 'latest': an event log field, gas consumed, a contract view or storage value, a contract-held token balance. The block or 'latest' anchor is what distinguishes it. Example: "At block 21000000 on ethereum, what amount did the Transfer log in tx 0xabc... carry, and how much gas did that tx use?" → ONCHAIN_METRIC_VERIFY_GENERAL. Not: "What was the status of transaction 0xabc...?" (a transaction lookup, not a named metric at a height) → ONCHAIN_TX_LOOKUP_GENERAL. Not: "What is the balance of vitalik.eth?" (a plain wallet balance) → WALLET_BALANCE_CHECK_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=ONCHAIN_METRIC_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+ONCHAIN_METRIC_VERIFY_GENERAL)

**`WASH_TRADING_DETECTION`** — judgment family · tier mandatory · H2 missions: Exchange, Asset Management, Web3 Native & DeFi

Analyzes DEX transaction graphs and circular transfer loops between affiliated wallets to identify artificial trade volume.

#### `WASH_TRADING_DETECTION_GENERAL`

judgment · asks `subject` · answers `subject`, `verdict`, `wash_volume_pct`, `signals`, `summary`

Query names a token, pool or set of wallets and asks whether its trading volume is artificial: circular transfers, self-dealing loops, round trips between affiliated addresses. Example: "Is volume on token 0x8335...913 on base wash traded? Check for circular transfers between affiliated wallets." → WASH_TRADING_DETECTION_GENERAL. Not: "What is the 24h trading volume of token 0x8335...913?" (asks for the volume figure itself, no manipulation judgment) → FINANCIAL_DATA_GENERAL.

Contribute question pairs · adapter on `WASH_TRADING_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WASH_TRADING_DETECTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WASH_TRADING_DETECTION_GENERAL)

**`ASSET_RESERVE_ATTESTATION`** — judgment family · tier mandatory · H2 missions: Stablecoin, Mining & Power, Asset Management

Verifies cryptographic proof-of-reserves and custodial bank confirmations backing stablecoins and tokenized assets.

#### `ASSET_RESERVE_ATTESTATION_GENERAL`

deterministic · asks `asset` · answers `attested_reserve`, `asset`, `block`, `source`

Query names a stablecoin, tokenized asset or custodian and asks whether attested reserves back the circulating supply, cross-checking on-chain balances against a custodian or proof-of-reserves feed. Example: "Do the attested reserves behind USDC cover its circulating supply as of the latest proof-of-reserves report?" → ASSET_RESERVE_ATTESTATION_GENERAL. Not: "What is USDC trading at?" (a price) → CRYPTO_PRICE_USD. Not: "How much USDC does this address hold?" (one address's balance) → WALLET_BALANCE_CHECK_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=ASSET_RESERVE_ATTESTATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+ASSET_RESERVE_ATTESTATION_GENERAL)

**`CRYPTO_TRANSFER_VERIFY`** — judgment family · tier existing · H2 missions: Web3 Native & DeFi

Verifies on-chain transaction status, gas fee burn, sender/recipient addresses, and block confirmations.

#### `CRYPTO_TRANSFER_VERIFY_GENERAL`

deterministic

Verifies on-chain transaction status, gas fee burn, sender/recipient addresses, and block confirmations.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CRYPTO_TRANSFER_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CRYPTO_TRANSFER_VERIFY_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SMART_CONTRACT_AUDIT`** — judgment family · tier existing · H2 missions: Exchange, Web3 Native & DeFi

Inspects bytecode and smart contract source code for reentrancy, access control, and integer overflows.

#### `SMART_CONTRACT_AUDIT_GENERAL`

judgment

Inspects bytecode and smart contract source code for reentrancy, access control, and integer overflows.

Contribute question pairs · adapter on `SMART_CONTRACT_AUDIT`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SMART_CONTRACT_AUDIT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SMART_CONTRACT_AUDIT_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`CRYPTO_YIELD_RATE`** — judgment family · tier existing · H2 missions: Asset Management

Tracks annualized percentage yields (APY), staking reward rates, and lending pool yields across DeFi protocols.

#### `CRYPTO_YIELD_RATE_GENERAL`

deterministic · asks `project`, `symbol`, `chain` · answers `supply_apy`

Tracks annualized percentage yields (APY), staking reward rates, and lending pool yields across DeFi protocols.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CRYPTO_YIELD_RATE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CRYPTO_YIELD_RATE_GENERAL)

**`TOKEN_TOTAL_SUPPLY_VERIFY`** — judgment family · tier existing · H2 missions: Exchange

Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.

#### `TOKEN_TOTAL_SUPPLY_VERIFY_GENERAL`

deterministic · asks `token` · answers `total_supply`

Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TOKEN_TOTAL_SUPPLY_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TOKEN_TOTAL_SUPPLY_VERIFY_GENERAL)

Not usable in an on-chain job yet: number field "total_supply" has no decimals.

**`VALIDATOR_PERFORMANCE_VERIFY`** — judgment family · tier mandatory · H2 missions: Mining & Power, Asset Management

Tracks consensus voting uptime, proposed block rates, slashing penalties, and staking APR for network validators.

#### `VALIDATOR_PERFORMANCE_VERIFY_GENERAL`

deterministic · asks `validator_index` · answers `effective_balance`

Query names a validator, index or staking operator on a proof-of-stake network and asks for its uptime, attestation or proposal rate, slashing history or staking yield. Example: "What is the attestation effectiveness and uptime of validator index 412903 over the last 30 days, and has it ever been slashed?" → VALIDATOR_PERFORMANCE_VERIFY_GENERAL. Not: "What is the current gas price on ethereum?" (network fee level) → GAS_PRICE_GENERAL. Not: "What does a unit of hashrate earn today?" (proof-of-work mining economics) → MINING_HASHPRICE_VERIFY_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=VALIDATOR_PERFORMANCE_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+VALIDATOR_PERFORMANCE_VERIFY_GENERAL)

## Climate & Weather

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`AIR_QUALITY_INDEX_GENERAL`](https://anjoman.ai/dashboard/eval?intent=AIR_QUALITY_INDEX_GENERAL) | deterministic | `AIR_QUALITY_INDEX` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+AIR_QUALITY_INDEX_GENERAL) |
| [`WEATHER_FORECAST_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=WEATHER_FORECAST_VERIFY_GENERAL) | judgment | `WEATHER_FORECAST_VERIFY` (judgment) | question pairs · adapter on `WEATHER_FORECAST_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+WEATHER_FORECAST_VERIFY_GENERAL) |

### Details

**`AIR_QUALITY_INDEX`** — judgment family · tier existing · H2 missions: —

Aggregates particulate matter (PM2.5/PM10), ground ozone, and composite AQI metrics from monitoring stations.

#### `AIR_QUALITY_INDEX_GENERAL`

deterministic

Aggregates particulate matter (PM2.5/PM10), ground ozone, and composite AQI metrics from monitoring stations.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=AIR_QUALITY_INDEX_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+AIR_QUALITY_INDEX_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`WEATHER_FORECAST_VERIFY`** — judgment family · tier mandatory · H2 missions: Conflict Intelligence, Resources & Agriculture, Commodities, Autonomous Systems, Mining & Power

Reconciles localized Doppler radar feeds, barometric pressure, wind gusts, and severe weather alert bulletins.

#### `WEATHER_FORECAST_VERIFY_GENERAL`

judgment · asks `location`, `date` · answers `location`, `date`, `temp_max_c`, `temp_min_c`, `precipitation_mm`, `condition`

Query supplies a previously issued forecast and asks whether it verified against what was actually observed. Requires both a forecast claim and a past window to check it against. Example: "Yesterday's forecast called for 12 mm of rain in Lisbon: what did stations actually record, and did the forecast verify?" → WEATHER_FORECAST_VERIFY_GENERAL. Not: "What is the forecast for Lisbon over the next 24 hours?" (asking for a forecast, not scoring one) → WEATHER_FORECAST_GENERAL. Not: "What is the temperature in Lisbon right now?" (current conditions) → WEATHER_CHECK_TEMPERATURE.

Contribute question pairs · adapter on `WEATHER_FORECAST_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WEATHER_FORECAST_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WEATHER_FORECAST_VERIFY_GENERAL)

## Commerce & Procurement

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`COMMERCE_PURCHASE_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=COMMERCE_PURCHASE_VERIFY_GENERAL) | judgment | `COMMERCE_PURCHASE_VERIFY` (judgment) | question pairs · adapter on `COMMERCE_PURCHASE_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+COMMERCE_PURCHASE_VERIFY_GENERAL) |
| [`LIVE_SHELF_PRICE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LIVE_SHELF_PRICE_GENERAL) | deterministic | `LIVE_SHELF_PRICE` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+LIVE_SHELF_PRICE_GENERAL) |
| [`SKU_IN_STOCK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SKU_IN_STOCK_GENERAL) | deterministic | `SKU_IN_STOCK` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+SKU_IN_STOCK_GENERAL) |
| [`PURCHASE_ORDER_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=PURCHASE_ORDER_VERIFY_GENERAL) | judgment | `PURCHASE_ORDER_VERIFY` (judgment) | question pairs · adapter on `PURCHASE_ORDER_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+PURCHASE_ORDER_VERIFY_GENERAL) |
| [`VENDOR_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=VENDOR_VERIFY_GENERAL) | judgment | `VENDOR_VERIFY` (judgment) | question pairs · adapter on `VENDOR_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+VENDOR_VERIFY_GENERAL) |
| [`PRODUCT_AUTHENTICITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=PRODUCT_AUTHENTICITY_GENERAL) | judgment | `PRODUCT_AUTHENTICITY` (judgment) | question pairs · adapter on `PRODUCT_AUTHENTICITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+PRODUCT_AUTHENTICITY_GENERAL) |
| [`RETURN_POLICY_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=RETURN_POLICY_VERIFY_GENERAL) | judgment | `RETURN_POLICY_VERIFY` (judgment) | question pairs · adapter on `RETURN_POLICY_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+RETURN_POLICY_VERIFY_GENERAL) |
| [`SHIP_RATE_ETA_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SHIP_RATE_ETA_GENERAL) | judgment | `SHIP_RATE_ETA` (judgment) | question pairs · adapter on `SHIP_RATE_ETA` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SHIP_RATE_ETA_GENERAL) |

### Details

**`COMMERCE_PURCHASE_VERIFY`** — judgment family · tier mandatory · H2 missions: Consumer Automation

Verifies the authenticity, item line totals, and payment authorization for a completed e-commerce purchase transaction.

#### `COMMERCE_PURCHASE_VERIFY_GENERAL`

judgment · asks `order_id`, `merchant` · answers `order_id`, `verified`, `status`, `amount`, `currency`

Query supplies an order id, receipt or payment reference and asks whether that purchase genuinely exists and matches stated line items, totals and payment authorization. Example: "Verify order 114-3941-8820: does the merchant show these three line items, a $148.20 total and an authorized payment?" → COMMERCE_PURCHASE_VERIFY_GENERAL. Not: "Is the card ending 4242 valid and active?" (an instrument check with no order) → PAYMENT_METHOD_VERIFY_GENERAL. Not: "Can I still return this order?" (policy eligibility) → RETURN_POLICY_VERIFY_GENERAL.

Contribute question pairs · adapter on `COMMERCE_PURCHASE_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=COMMERCE_PURCHASE_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+COMMERCE_PURCHASE_VERIFY_GENERAL)

**`LIVE_SHELF_PRICE`** — judgment family · tier mandatory · H2 missions: Consumer Platform, Consumer Automation

Fetches and verifies current live shelf or retail listing prices across online merchant catalogs and marketplaces.

#### `LIVE_SHELF_PRICE_GENERAL`

deterministic · asks `product`, `store` · answers `price`, `currency`, `product`, `store`, `date`

Query names a retail product, SKU or listing and asks what it currently sells for at one or more merchants. Example: "What is the current listed price of the Sony WH-1000XM5 at Amazon and Walmart right now?" → LIVE_SHELF_PRICE_GENERAL. Not: "What is Sony's share price?" (an equity quote) → STOCK_PRICE_US_EQUITY. Not: "Is that model actually in stock?" (availability, not price) → SKU_IN_STOCK_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LIVE_SHELF_PRICE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LIVE_SHELF_PRICE_GENERAL)

**`SKU_IN_STOCK`** — judgment family · tier mandatory · H2 missions: Consumer Platform, Consumer Automation

Confirms real-time stock availability, quantities, and warehouse fulfillment readiness for a given SKU.

#### `SKU_IN_STOCK_GENERAL`

deterministic

Query names a product, SKU or listing and asks whether it is purchasable right now, in what quantity, or at which location. Example: "Is SKU B09XS7JWHH in stock for delivery to 94107 today, and how many units are left?" → SKU_IN_STOCK_GENERAL. Not: "What does that SKU cost?" (a price, not availability) → LIVE_SHELF_PRICE_GENERAL. Not: "How many units of that SKU sit in bin 14C of our fulfilment centre?" (internal warehouse counts) → WAREHOUSE_INVENTORY_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SKU_IN_STOCK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SKU_IN_STOCK_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`PURCHASE_ORDER_VERIFY`** — judgment family · tier mandatory · H2 missions: —

Reconciles enterprise purchase orders with procurement approval workflows, vendor quotas, and budget allocations.

#### `PURCHASE_ORDER_VERIFY_GENERAL`

judgment · asks `po_number`, `vendor` · answers `po_number`, `verified`, `status`, `amount`, `vendor`

Query names a purchase order and asks whether it exists in the ERP with the stated vendor, amounts, approvals and budget allocation. Example: "Does PO-2231 exist for vendor Acme at $42,000, approved, and within the Q3 budget line?" → PURCHASE_ORDER_VERIFY_GENERAL. Not: "Do the invoice, the PO and the goods receipt all tie out?" (a multi-document reconciliation) → INVOICE_LEDGER_RECONCILE_GENERAL. Not: "Is Acme a legitimate supplier to onboard?" (vendor due diligence) → VENDOR_VERIFY_GENERAL.

Contribute question pairs · adapter on `PURCHASE_ORDER_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=PURCHASE_ORDER_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+PURCHASE_ORDER_VERIFY_GENERAL)

**`VENDOR_VERIFY`** — judgment family · tier mandatory · H2 missions: —

Audits vendor tax identifiers, compliance credentials, banking details, and sanctions list clearance.

#### `VENDOR_VERIFY_GENERAL`

judgment · asks `vendor`, `vat_number` · answers `vendor`, `vat_number`, `valid`, `registered_name`, `registered_address`

Query names a supplier and asks whether it checks out for onboarding or payment: tax identifiers, registration, banking details, certifications and sanctions clearance, as one combined verdict. Example: "Verify vendor Acme Ltd before onboarding: tax ID, bank account ownership, ISO certification and sanctions clearance." → VENDOR_VERIFY_GENERAL. Not: "Does this name hit the OFAC list?" (a sanctions screen alone) → SANCTIONS_SCREENING_MATCH_GENERAL. Not: "Is this PO approved and in budget?" (a purchase order record) → PURCHASE_ORDER_VERIFY_GENERAL.

Contribute question pairs · adapter on `VENDOR_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=VENDOR_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+VENDOR_VERIFY_GENERAL)

**`PRODUCT_AUTHENTICITY`** — judgment family · tier mandatory · H2 missions: Consumer Platform, Consumer Automation

Validates product provenance, serial numbers, and manufacturer anti-counterfeit records against authorized registries.

#### `PRODUCT_AUTHENTICITY_GENERAL`

judgment · asks `product` · answers `product`, `verdict`, `authentic`, `evidence`

Query supplies a serial number, barcode, GTIN or product identifier and asks whether the item is genuine according to the manufacturer or an authorized registry. Example: "Is serial 8F2K-99213 a genuine unit in the brand registry, and does GTIN 00012345600012 resolve to this product?" → PRODUCT_AUTHENTICITY_GENERAL. Not: "Is this photo of the product AI-generated?" (media forensics) → MEDIA_FORENSIC_VERIFY_GENERAL. Not: "Is this certificate of authenticity document genuine?" (document integrity) → DOCUMENT_AUTHENTICITY_GENERAL.

Contribute question pairs · adapter on `PRODUCT_AUTHENTICITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=PRODUCT_AUTHENTICITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+PRODUCT_AUTHENTICITY_GENERAL)

**`RETURN_POLICY_VERIFY`** — judgment family · tier mandatory · H2 missions: —

Validates order return eligibility, restocking fees, and merchant policy constraints based on purchase timestamp and category.

#### `RETURN_POLICY_VERIFY_GENERAL`

judgment · asks `retailer` · answers `retailer`, `return_window_days`, `conditions`, `verified`, `sources`

Query supplies an order or purchase context and asks whether it can still be returned under the merchant's policy, and at what cost. Example: "This item shipped 40 days ago and was opened: is it still returnable under this merchant's policy, and what restocking fee applies?" → RETURN_POLICY_VERIFY_GENERAL. Not: "Verify order 114-3941-8820 exists with these line items and total." (order existence) → COMMERCE_PURCHASE_VERIFY_GENERAL.

Contribute question pairs · adapter on `RETURN_POLICY_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=RETURN_POLICY_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+RETURN_POLICY_VERIFY_GENERAL)

**`SHIP_RATE_ETA`** — judgment family · tier mandatory · H2 missions: Resources & Agriculture, Commodities, Personal Agent

Calculates and verifies carrier shipping rates, service tiers, and estimated delivery dates for specified zip codes.

#### `SHIP_RATE_ETA_GENERAL`

judgment · asks `origin`, `destination`, `weight_kg` · answers `carrier`, `rate`, `currency`, `transit_days`, `eta`

Query names an origin, destination and parcel and asks what carriers would charge and when they would deliver. The shipment has not been sent yet. Example: "What do UPS, FedEx and DHL charge for a 2 kg parcel from 94107 to 10001, and what delivery dates do they quote?" → SHIP_RATE_ETA_GENERAL. Not: "Where is my parcel right now?" (tracking a shipment already in transit) → PACKAGE_STATUS_GENERAL. Not: "Will any carrier even take a lithium-battery shipment on that lane?" (coverage and restrictions) → CARRIER_SERVICEABILITY_GENERAL.

Contribute question pairs · adapter on `SHIP_RATE_ETA`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SHIP_RATE_ETA_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SHIP_RATE_ETA_GENERAL)

## Cybersecurity

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`VULNERABILITY_TRIAGE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=VULNERABILITY_TRIAGE_GENERAL) | judgment | `VULNERABILITY_TRIAGE` (judgment) | question pairs · adapter on `VULNERABILITY_TRIAGE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+VULNERABILITY_TRIAGE_GENERAL) |
| [`EMAIL_SECURITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=EMAIL_SECURITY_GENERAL) | judgment | `EMAIL_SECURITY` (judgment) | question pairs · adapter on `EMAIL_SECURITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+EMAIL_SECURITY_GENERAL) |
| [`MALWARE_DETECTION_HASH`](https://anjoman.ai/dashboard/eval?intent=MALWARE_DETECTION_HASH) | hybrid | `MALWARE_DETECTION` (hybrid) | truth sources and question pairs · adapter on `MALWARE_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+MALWARE_DETECTION_HASH) |
| [`THREAT_INTELLIGENCE_INDICATOR`](https://anjoman.ai/dashboard/eval?intent=THREAT_INTELLIGENCE_INDICATOR) | hybrid | `THREAT_INTELLIGENCE` (hybrid) | truth sources and question pairs · adapter on `THREAT_INTELLIGENCE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+THREAT_INTELLIGENCE_INDICATOR) |
| [`THREAT_IP_REPUTATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=THREAT_IP_REPUTATION_GENERAL) | judgment | `THREAT_IP_REPUTATION` (judgment) | question pairs · adapter on `THREAT_IP_REPUTATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+THREAT_IP_REPUTATION_GENERAL) |
| [`URL_SAFE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=URL_SAFE_GENERAL) | judgment | `URL_SAFE` (judgment) | question pairs · adapter on `URL_SAFE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+URL_SAFE_GENERAL) |
| [`DNS_RECORD_LOOKUP_GENERAL`](https://anjoman.ai/dashboard/eval?intent=DNS_RECORD_LOOKUP_GENERAL) | deterministic | `DNS_RECORD_LOOKUP` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+DNS_RECORD_LOOKUP_GENERAL) |
| [`PORT_SCAN_AUDIT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=PORT_SCAN_AUDIT_GENERAL) | deterministic | `PORT_SCAN_AUDIT` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+PORT_SCAN_AUDIT_GENERAL) |

### Details

**`VULNERABILITY_TRIAGE`** — judgment family · tier mandatory · H2 missions: Model Economy, Web3 Native & DeFi

Ranks and categorizes detected vulnerabilities by CVSS score, active exploit availability, and asset criticality.

#### `VULNERABILITY_TRIAGE_GENERAL`

judgment · asks `cve_id` · answers `cvss_base_score`

Query supplies a set of already-detected vulnerabilities or CVEs and asks how to rank or prioritise them, by CVSS, known exploitation in the wild, and how critical the affected asset is. Example: "Rank these 12 findings on an internet-facing payments service by exploitability and business impact." → VULNERABILITY_TRIAGE_GENERAL. Not: "What is the CVSS score and affected version range of CVE-2024-3094?" (a single record lookup, nothing to rank) → CVE_LOOKUP_CVSS. Not: "Scan this repo and tell me what is vulnerable." (finding the issues in the first place) → SECURITY_REVIEW_GENERAL.

Contribute question pairs · adapter on `VULNERABILITY_TRIAGE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=VULNERABILITY_TRIAGE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+VULNERABILITY_TRIAGE_GENERAL)

**`EMAIL_SECURITY`** — judgment family · tier mandatory · H2 missions: —

Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.

#### `EMAIL_SECURITY_GENERAL`

judgment · asks `domain`, `record_type` · answers `lookup_ok`

Query supplies a domain or an email message and asks about mail authentication and spoofing: SPF, DKIM and DMARC records, header anomalies, malicious attachments. Example: "Does example.com publish valid SPF, DKIM and DMARC records, and do these message headers indicate spoofing?" → EMAIL_SECURITY_GENERAL. Not: "Is the link inside that email on a blocklist?" (URL reputation) → URL_SAFE_GENERAL. Not: "Is the attached binary malicious?" (a file verdict) → MALWARE_DETECTION_HASH.

Contribute question pairs · adapter on `EMAIL_SECURITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=EMAIL_SECURITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+EMAIL_SECURITY_GENERAL)

**`MALWARE_DETECTION`** — hybrid family · tier mandatory · H2 missions: —

Scans file hashes and binaries against multi-engine antivirus definitions and sandbox behavioral detonation traces.

#### `MALWARE_DETECTION_HASH`

hybrid · asks `indicator` · answers `malicious`

Query supplies a file hash (SHA-256, SHA-1 or MD5) and asks whether the file is malicious according to antivirus engines or known-malware databases. Example: "Is SHA-256 275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f flagged as malware?" → MALWARE_DETECTION_HASH. Not: "Is this URL on a phishing blocklist?" → URL_SCAN_VERDICT.

Contribute truth sources and question pairs · adapter on `MALWARE_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=MALWARE_DETECTION_HASH) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+MALWARE_DETECTION_HASH)

**`THREAT_INTELLIGENCE`** — hybrid family · tier mandatory · H2 missions: —

Aggregates indicators of compromise (IOCs), malicious IP ranges, and adversary tactics from global security feeds.

#### `THREAT_INTELLIGENCE_INDICATOR`

hybrid · asks `indicator` · answers `malicious`

Query supplies an IP address, domain or other indicator and asks whether it is malicious or reported in threat-intelligence feeds. Example: "Is 185.220.101.4 reported as malicious in threat intelligence feeds?" → THREAT_INTELLIGENCE_INDICATOR. Not: "Where is 185.220.101.4 located?" → IP_GEOLOCATION_GENERAL. Not: scanning a URL for safety → URL_SCAN_VERDICT. Not: whether a file hash is malware → MALWARE_DETECTION_HASH.

Contribute truth sources and question pairs · adapter on `THREAT_INTELLIGENCE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=THREAT_INTELLIGENCE_INDICATOR) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+THREAT_INTELLIGENCE_INDICATOR)

**`THREAT_IP_REPUTATION`** — judgment family · tier existing · H2 missions: —

Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.

#### `THREAT_IP_REPUTATION_GENERAL`

judgment

Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.

Contribute question pairs · adapter on `THREAT_IP_REPUTATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=THREAT_IP_REPUTATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+THREAT_IP_REPUTATION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`URL_SAFE`** — judgment family · tier mandatory · H2 missions: Consumer Platform, Consumer Automation

Checks target URLs against live threat feeds, DNS blocklists, phishing databases, and domain reputation monitors.

#### `URL_SAFE_GENERAL`

judgment · asks `url` · answers `url`, `verdict`, `detections`, `summary`

Query supplies a URL or domain and asks whether it is listed as malicious across live threat feeds, DNS blocklists, phishing databases or domain reputation services, with the sources that flagged it. Example: "Check https://login-secure-update.example.com against threat feeds and DNS blocklists: is it listed for phishing, and by which engines?" → URL_SAFE_GENERAL. Not: "Is this link safe to click?" (a single general safe/unsafe verdict on one URL) → URL_SCAN_VERDICT. Not: "Is example.com's TLS certificate valid?" (certificate detail) → SSL_VERIFICATION_CERT.

Contribute question pairs · adapter on `URL_SAFE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=URL_SAFE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+URL_SAFE_GENERAL)

**`DNS_RECORD_LOOKUP`** — judgment family · tier existing · H2 missions: —

Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.

#### `DNS_RECORD_LOOKUP_GENERAL`

deterministic · asks `name`, `record_type` · answers `has_record`

Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=DNS_RECORD_LOOKUP_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+DNS_RECORD_LOOKUP_GENERAL)

**`PORT_SCAN_AUDIT`** — judgment family · tier existing · H2 missions: —

Identifies open network service ports, banner disclosures, and listening daemon protocols on specified hosts.

#### `PORT_SCAN_AUDIT_GENERAL`

deterministic

Identifies open network service ports, banner disclosures, and listening daemon protocols on specified hosts.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=PORT_SCAN_AUDIT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+PORT_SCAN_AUDIT_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

## Energy & Infrastructure

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`CLOUD_RESOURCE_USAGE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CLOUD_RESOURCE_USAGE_GENERAL) | judgment | `CLOUD_RESOURCE_USAGE` (judgment) | question pairs · adapter on `CLOUD_RESOURCE_USAGE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CLOUD_RESOURCE_USAGE_GENERAL) |
| [`DATACENTER_TELEMETRY_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=DATACENTER_TELEMETRY_VERIFY_GENERAL) | judgment | `DATACENTER_TELEMETRY_VERIFY` (judgment) | question pairs · adapter on `DATACENTER_TELEMETRY_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+DATACENTER_TELEMETRY_VERIFY_GENERAL) |
| [`GRID_POWER_PRICE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=GRID_POWER_PRICE_GENERAL) | deterministic | `GRID_POWER_PRICE` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+GRID_POWER_PRICE_GENERAL) |
| [`MINING_HASHPRICE_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=MINING_HASHPRICE_VERIFY_GENERAL) | deterministic | `MINING_HASHPRICE_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+MINING_HASHPRICE_VERIFY_GENERAL) |

### Details

**`CLOUD_RESOURCE_USAGE`** — judgment family · tier existing · H2 missions: —

Audits virtual machine and container compute utilization, memory pressure, and network throughput metrics.

#### `CLOUD_RESOURCE_USAGE_GENERAL`

judgment

Audits virtual machine and container compute utilization, memory pressure, and network throughput metrics.

Contribute question pairs · adapter on `CLOUD_RESOURCE_USAGE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CLOUD_RESOURCE_USAGE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CLOUD_RESOURCE_USAGE_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`DATACENTER_TELEMETRY_VERIFY`** — judgment family · tier mandatory · H2 missions: Autonomous Systems, Mining & Power

Audits rack power usage effectiveness (PUE), server thermal telemetry, and backup generator readiness metrics.

#### `DATACENTER_TELEMETRY_VERIFY_GENERAL`

judgment · asks `facility` · answers `facility`, `power_kw`, `temperature_c`, `pue`, `observed_at`

Query asks for facility or rack telemetry at a named site: power usage effectiveness, power draw, inlet and thermal readings, cooling or backup generator readiness. Example: "What is the current PUE and rack inlet temperature in hall 2, and is the backup generator in ready state?" → DATACENTER_TELEMETRY_VERIFY_GENERAL. Not: "Is device 44's sensor payload signed correctly and in calibration?" (edge device telemetry integrity) → SENSOR_TELEMETRY_VERIFY_GENERAL.

Contribute question pairs · adapter on `DATACENTER_TELEMETRY_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=DATACENTER_TELEMETRY_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+DATACENTER_TELEMETRY_VERIFY_GENERAL)

**`GRID_POWER_PRICE`** — judgment family · tier mandatory · H2 missions: Resources & Agriculture, Autonomous Systems, Mining & Power

Ingests real-time nodal marginal locational prices (LMP) and day-ahead electricity spot rates from regional grid operators.

#### `GRID_POWER_PRICE_GENERAL`

deterministic · asks `node_or_zone`, `interval_start` · answers `lmp_usd_per_mwh`, `node_or_zone`, `market`, `interval_start`, `currency`

Query names a grid, node, hub or region and asks for electricity prices from the operator: locational marginal price, day-ahead or real-time spot rates. Example: "What is the current locational marginal price at the ERCOT Houston hub, and what did day-ahead settle at?" → GRID_POWER_PRICE_GENERAL. Not: "What is a token or commodity trading at?" (market instrument prices) → CRYPTO_PRICE_USD or FINANCIAL_DATA_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=GRID_POWER_PRICE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+GRID_POWER_PRICE_GENERAL)

**`MINING_HASHPRICE_VERIFY`** — judgment family · tier mandatory · H2 missions: Mining & Power

Calculates instantaneous proof-of-work mining revenue per unit of hashing power based on block rewards and network difficulty.

#### `MINING_HASHPRICE_VERIFY_GENERAL`

deterministic · asks `block_height` · answers `hashprice_sats_per_ph_day`, `block_height`, `hashrate_eh_s`, `hashprice_usd_per_ph_day`

Query asks what a unit of hashing power currently earns on a proof-of-work network, derived from block reward, fees and network difficulty. Example: "What is Bitcoin hashprice per PH/s per day at current difficulty and fee levels?" → MINING_HASHPRICE_VERIFY_GENERAL. Not: "What is Bitcoin trading at?" (an asset quote) → CRYPTO_PRICE_USD. Not: "What is power costing at that hub?" (electricity prices) → GRID_POWER_PRICE_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=MINING_HASHPRICE_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+MINING_HASHPRICE_VERIFY_GENERAL)

## Enterprise Operations

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`B2B_IDENTITY_ENRICHMENT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=B2B_IDENTITY_ENRICHMENT_GENERAL) | judgment | `B2B_IDENTITY_ENRICHMENT` (judgment) | question pairs · adapter on `B2B_IDENTITY_ENRICHMENT` | [open](../../../issues?q=is%3Aissue+is%3Aopen+B2B_IDENTITY_ENRICHMENT_GENERAL) |
| [`CONTRACT_OBLIGATION_AUDIT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CONTRACT_OBLIGATION_AUDIT_GENERAL) | judgment | `CONTRACT_OBLIGATION_AUDIT` (judgment) | question pairs · adapter on `CONTRACT_OBLIGATION_AUDIT` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CONTRACT_OBLIGATION_AUDIT_GENERAL) |
| [`DOCUMENT_AUTHENTICITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=DOCUMENT_AUTHENTICITY_GENERAL) | judgment | `DOCUMENT_AUTHENTICITY` (judgment) | question pairs · adapter on `DOCUMENT_AUTHENTICITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+DOCUMENT_AUTHENTICITY_GENERAL) |
| [`INVOICE_LEDGER_RECONCILE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=INVOICE_LEDGER_RECONCILE_GENERAL) | judgment | `INVOICE_LEDGER_RECONCILE` (judgment) | question pairs · adapter on `INVOICE_LEDGER_RECONCILE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+INVOICE_LEDGER_RECONCILE_GENERAL) |
| [`API_HEALTH_CHECK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=API_HEALTH_CHECK_GENERAL) | deterministic | `API_HEALTH_CHECK` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+API_HEALTH_CHECK_GENERAL) |
| [`CUSTOMER_TICKET_RESOLUTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CUSTOMER_TICKET_RESOLUTION_GENERAL) | judgment | `CUSTOMER_TICKET_RESOLUTION` (judgment) | question pairs · adapter on `CUSTOMER_TICKET_RESOLUTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CUSTOMER_TICKET_RESOLUTION_GENERAL) |
| [`SERVER_UPTIME_MONITOR_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SERVER_UPTIME_MONITOR_GENERAL) | deterministic | `SERVER_UPTIME_MONITOR` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+SERVER_UPTIME_MONITOR_GENERAL) |
| [`SLA_COMPLIANCE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SLA_COMPLIANCE_GENERAL) | judgment | `SLA_COMPLIANCE` (judgment) | question pairs · adapter on `SLA_COMPLIANCE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SLA_COMPLIANCE_GENERAL) |

### Details

**`B2B_IDENTITY_ENRICHMENT`** — judgment family · tier mandatory · H2 missions: Institutional Markets, Personal Agent

Enriches business entity records with corporate tax IDs, headquarters addresses, executive listings, and domain validation.

#### `B2B_IDENTITY_ENRICHMENT_GENERAL`

judgment · asks `company` · answers `company`, `domain`, `employee_count`, `industry`, `headquarters`

Query supplies a partial business record - a domain, brand or work email - and asks for it to be filled out with firmographic fields: legal entity, tax id, headquarters, headcount, industry, executives, domain validity. Example: "Enrich acme.io: legal entity name, tax ID, HQ address, employee count and CEO." → B2B_IDENTITY_ENRICHMENT_GENERAL. Not: "Is Acme Ltd incorporated, and who is its registered agent?" (the official register record itself) → CORPORATE_REGISTRY_LOOKUP_GENERAL.

Contribute question pairs · adapter on `B2B_IDENTITY_ENRICHMENT`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=B2B_IDENTITY_ENRICHMENT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+B2B_IDENTITY_ENRICHMENT_GENERAL)

**`CONTRACT_OBLIGATION_AUDIT`** — judgment family · tier mandatory · H2 missions: Legal

Parses and verifies legal contract milestone deliverables, payment terms, and vendor performance commitments.

#### `CONTRACT_OBLIGATION_AUDIT_GENERAL`

judgment · asks `contract` · answers `verdict`, `obligations`, `clauses`, `summary`

Query supplies contract text and asks what obligations it creates - deliverables, milestones, payment terms, performance commitments - or whether those have been met. Example: "Extract every deliverable, due date and payment milestone from this MSA and flag the ones already overdue." → CONTRACT_OBLIGATION_AUDIT_GENERAL. Not: "Is this signed PDF genuine and unaltered?" (integrity of the artifact, not the terms inside it) → DOCUMENT_AUTHENTICITY_GENERAL. Not: "Does this invoice tie out against the PO?" (ledger reconciliation) → INVOICE_LEDGER_RECONCILE_GENERAL.

Contribute question pairs · adapter on `CONTRACT_OBLIGATION_AUDIT`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CONTRACT_OBLIGATION_AUDIT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CONTRACT_OBLIGATION_AUDIT_GENERAL)

**`DOCUMENT_AUTHENTICITY`** — judgment family · tier mandatory · H2 missions: Stablecoin, Institutional Markets, Legal, Commodities

Validates digital certificate signatures, notarizations, tamper-evident seals, and document checksum integrity.

#### `DOCUMENT_AUTHENTICITY_GENERAL`

judgment · asks `document` · answers `document`, `authentic`, `verdict`, `evidence`

Query supplies a document plus its signature, seal or timestamp data and asks whether it is genuine and unaltered: certificate chain, notarization, tamper-evident seal, checksum. Example: "Verify the digital signature and notarization seal on this PDF and tell me whether the content changed after signing." → DOCUMENT_AUTHENTICITY_GENERAL. Not: "Is this image AI-generated or spliced?" (media forensics) → MEDIA_FORENSIC_VERIFY_GENERAL. Not: "What obligations does this contract create?" (reading the contents) → CONTRACT_OBLIGATION_AUDIT_GENERAL.

Contribute question pairs · adapter on `DOCUMENT_AUTHENTICITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=DOCUMENT_AUTHENTICITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+DOCUMENT_AUTHENTICITY_GENERAL)

**`INVOICE_LEDGER_RECONCILE`** — judgment family · tier mandatory · H2 missions: —

Performs automated 3-way matching between invoice line items, purchase orders, and receiving dock receipts.

#### `INVOICE_LEDGER_RECONCILE_GENERAL`

judgment · asks `invoice`, `ledger` · answers `reconciled`, `discrepancy`, `explanation`

Query supplies invoices, purchase orders and receipts and asks whether they reconcile: three-way match on line items, quantities, tax and totals, and which entries do not tie out. Example: "Three-way match invoice INV-8841 against PO-2231 and the goods receipt, and list the mismatched lines." → INVOICE_LEDGER_RECONCILE_GENERAL. Not: "Does PO-2231 exist with the approved amount and budget?" (the purchase order on its own) → PURCHASE_ORDER_VERIFY_GENERAL.

Contribute question pairs · adapter on `INVOICE_LEDGER_RECONCILE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=INVOICE_LEDGER_RECONCILE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+INVOICE_LEDGER_RECONCILE_GENERAL)

**`API_HEALTH_CHECK`** — judgment family · tier existing · H2 missions: —

Verifies REST/GraphQL API responsiveness, JSON schema payload structure, and HTTP status codes.

#### `API_HEALTH_CHECK_GENERAL`

deterministic

Verifies REST/GraphQL API responsiveness, JSON schema payload structure, and HTTP status codes.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=API_HEALTH_CHECK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+API_HEALTH_CHECK_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`CUSTOMER_TICKET_RESOLUTION`** — judgment family · tier mandatory · H2 missions: —

Analyzes helpdesk support interactions, resolution accuracy, agent action compliance, and customer satisfaction outcomes.

#### `CUSTOMER_TICKET_RESOLUTION_GENERAL`

judgment · asks `ticket` · answers `resolved`, `resolution`, `steps`, `sources`, `brief`

Query supplies a support conversation or ticket and asks how well it was handled: whether the issue was actually resolved, whether policy was followed, likely customer satisfaction. Example: "Here is a support thread: was the customer's issue resolved, and did the agent follow refund policy?" → CUSTOMER_TICKET_RESOLUTION_GENERAL. Not: "Was the first response inside the 4-hour SLA?" (a timing threshold) → SLA_COMPLIANCE_GENERAL.

Contribute question pairs · adapter on `CUSTOMER_TICKET_RESOLUTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CUSTOMER_TICKET_RESOLUTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CUSTOMER_TICKET_RESOLUTION_GENERAL)

**`SERVER_UPTIME_MONITOR`** — judgment family · tier existing · H2 missions: Consumer Automation

Monitors synthetic HTTP/HTTPS endpoint availability, handshake latency, and uptime status from multiple edge regions.

#### `SERVER_UPTIME_MONITOR_GENERAL`

deterministic

Monitors synthetic HTTP/HTTPS endpoint availability, handshake latency, and uptime status from multiple edge regions.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SERVER_UPTIME_MONITOR_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SERVER_UPTIME_MONITOR_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SLA_COMPLIANCE`** — judgment family · tier mandatory · H2 missions: Mining & Power, Consumer Automation

Measures operational response and resolution turnaround against contractually agreed enterprise service level agreements.

#### `SLA_COMPLIANCE_GENERAL`

judgment · asks `service`, `period` · answers `service`, `uptime_pct`, `sla_target_pct`, `compliant`, `period`

Query asks whether measured response time, resolution time or uptime met a stated service level threshold over a period. Example: "Did the API hold 99.9% uptime last month and meet the 4-hour resolution SLA on P1 incidents?" → SLA_COMPLIANCE_GENERAL. Not: "Was the customer satisfied with how that ticket was handled?" (quality of the interaction) → CUSTOMER_TICKET_RESOLUTION_GENERAL.

Contribute question pairs · adapter on `SLA_COMPLIANCE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SLA_COMPLIANCE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SLA_COMPLIANCE_GENERAL)

## Financial / Transactional

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`OPTIMAL_EXECUTION_ROUTE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=OPTIMAL_EXECUTION_ROUTE_GENERAL) | judgment | `OPTIMAL_EXECUTION_ROUTE` (judgment) | question pairs · adapter on `OPTIMAL_EXECUTION_ROUTE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+OPTIMAL_EXECUTION_ROUTE_GENERAL) |
| [`FRAUD_RISK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=FRAUD_RISK_GENERAL) | judgment | `FRAUD_RISK` (judgment) | question pairs · adapter on `FRAUD_RISK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+FRAUD_RISK_GENERAL) |
| [`PAYMENT_METHOD_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=PAYMENT_METHOD_VERIFY_GENERAL) | deterministic | `PAYMENT_METHOD_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+PAYMENT_METHOD_VERIFY_GENERAL) |
| [`TRANSACTION_RISK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TRANSACTION_RISK_GENERAL) | judgment | `TRANSACTION_RISK` (judgment) | question pairs · adapter on `TRANSACTION_RISK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TRANSACTION_RISK_GENERAL) |
| [`FX_NOW_CAD`](https://anjoman.ai/dashboard/eval?intent=FX_NOW_CAD) | deterministic | `FX_NOW` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+FX_NOW_CAD) |
| [`FX_NOW_EUR`](https://anjoman.ai/dashboard/eval?intent=FX_NOW_EUR) | deterministic | `FX_NOW` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+FX_NOW_EUR) |
| [`FX_NOW_SEK`](https://anjoman.ai/dashboard/eval?intent=FX_NOW_SEK) | deterministic | `FX_NOW` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+FX_NOW_SEK) |
| [`CREDIT_SCORE_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CREDIT_SCORE_VERIFY_GENERAL) | judgment | `CREDIT_SCORE_VERIFY` (judgment) | question pairs · adapter on `CREDIT_SCORE_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CREDIT_SCORE_VERIFY_GENERAL) |
| [`CURRENCY_EXCHANGE_CONVERT`](https://anjoman.ai/dashboard/eval?intent=CURRENCY_EXCHANGE_CONVERT) | deterministic | `CURRENCY_EXCHANGE` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+CURRENCY_EXCHANGE_CONVERT) |
| [`LOAN_INTEREST_RATE_QUOTE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LOAN_INTEREST_RATE_QUOTE_GENERAL) | deterministic | `LOAN_INTEREST_RATE_QUOTE` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+LOAN_INTEREST_RATE_QUOTE_GENERAL) |

### Details

**`OPTIMAL_EXECUTION_ROUTE`** — judgment family · tier mandatory · H2 missions: —

Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.

#### `OPTIMAL_EXECUTION_ROUTE_GENERAL`

judgment · asks `pair` · answers `amount_out`

Query asks for the best venue or multi-hop path to execute a stated trade size, judged on slippage, fees and market impact. Requires both an asset pair and a size. Example: "What is the best route to swap 250,000 USDC into WETH on base right now, minimising slippage and fees?" → OPTIMAL_EXECUTION_ROUTE_GENERAL. Not: "What is WETH trading at?" (a quote, no execution decision) → CRYPTO_PRICE_USD. Not: "How deep is that pool at a 50 ETH size?" (measuring depth, not choosing a route) → LIQUIDITY_DEPTH_VERIFY_GENERAL.

Contribute question pairs · adapter on `OPTIMAL_EXECUTION_ROUTE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=OPTIMAL_EXECUTION_ROUTE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+OPTIMAL_EXECUTION_ROUTE_GENERAL)

**`FRAUD_RISK`** — judgment family · tier mandatory · H2 missions: Stablecoin

Computes real-time behavioral fraud probability scores using device fingerprinting, IP geolocation, and transaction context.

#### `FRAUD_RISK_GENERAL`

judgment · asks `subject` · answers `risk_level`, `risk_score`, `signals`, `summary`

Query supplies actor context - device fingerprint, IP, email, signup or session behaviour - and asks for a forward-looking probability that the actor is fraudulent. There is no ground truth at query time; the answer is a score. Example: "Score the fraud risk of this signup: IP 45.83.x.x, headless browser fingerprint, disposable email domain." → FRAUD_RISK_GENERAL. Not: "Is this specific transaction from 0xabc... fraudulent?" (an assessment of one concrete thing that already happened) → FRAUD_DETECTION_GENERAL. Not: "Where is IP 45.83.x.x located?" (a plain geolocation lookup) → IP_GEOLOCATION_GENERAL.

Contribute question pairs · adapter on `FRAUD_RISK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FRAUD_RISK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FRAUD_RISK_GENERAL)

**`PAYMENT_METHOD_VERIFY`** — judgment family · tier mandatory · H2 missions: Stablecoin

Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.

#### `PAYMENT_METHOD_VERIFY_GENERAL`

deterministic · asks `bin` · answers `network`, `issuing_bank`, `issuing_country`, `valid`, `card_type`

Query supplies a card BIN, payment token, bank account or routing number and asks whether it is valid, active and issued by the stated institution. Example: "Is BIN 411111 a valid Visa, which issuer does it belong to, and is routing number 021000021 an active ACH route?" → PAYMENT_METHOD_VERIFY_GENERAL. Not: "Does this $2,400 purchase look like it will charge back?" (a risk score on a transaction) → TRANSACTION_RISK_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=PAYMENT_METHOD_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+PAYMENT_METHOD_VERIFY_GENERAL)

**`TRANSACTION_RISK`** — judgment family · tier mandatory · H2 missions: Stablecoin, Mining & Power

Evaluates cardholder spending velocity, merchant categorization codes, and chargeback history to score transaction risk.

#### `TRANSACTION_RISK_GENERAL`

judgment · asks `transaction` · answers `risk_level`, `risk_score`, `signals`, `summary`

Query supplies payment-transaction context - amount, merchant category, cardholder velocity, chargeback history - and asks for a risk or chargeback probability score on authorising it. Example: "Score the chargeback risk of a $2,400 electronics purchase on a card that made 6 attempts in 10 minutes." → TRANSACTION_RISK_GENERAL. Not: "Is this card number valid and active?" (instrument validity) → PAYMENT_METHOD_VERIFY_GENERAL. Not: "Score this signup's device and IP." (account and device level, not a payment authorisation) → FRAUD_RISK_GENERAL.

Contribute question pairs · adapter on `TRANSACTION_RISK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TRANSACTION_RISK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TRANSACTION_RISK_GENERAL)

**`FX_NOW`** — deterministic family · tier mandatory · H2 missions: Stablecoin, Institutional Markets, Commodities, Personal Agent

Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.

#### `FX_NOW_CAD`

deterministic · asks `currency` · answers `rate`

Query asks for the live institutional mid-market rate between the US dollar and the Canadian dollar (USD/CAD or CAD/USD), as a market data point with no amount to convert. Example: "What is the current USD/CAD mid-market rate?" → FX_NOW_CAD. Not: a pair without both USD and CAD (another FX_NOW_ intent). Not: "How much is 100 USD in CAD?" (a conversion of a stated amount for a user).

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FX_NOW_CAD) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FX_NOW_CAD)

#### `FX_NOW_EUR`

deterministic · asks `currency` · answers `rate`

Query asks for the live institutional mid-market rate between the US dollar and the euro (USD/EUR or EUR/USD), as a market data point with no amount to convert. Example: "What is the current EUR/USD mid-market rate?" → FX_NOW_EUR. Not: a pair without both USD and EUR (another FX_NOW_ intent). Not: "How much is 100 USD in EUR?" (a conversion of a stated amount for a user).

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FX_NOW_EUR) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FX_NOW_EUR)

#### `FX_NOW_SEK`

deterministic · asks `currency` · answers `rate`

Query asks for the live institutional mid-market rate between the US dollar and the Swedish krona (USD/SEK or SEK/USD), as a market data point with no amount to convert. Example: "What is the current USD/SEK mid-market rate?" → FX_NOW_SEK. Not: a pair without both USD and SEK (another FX_NOW_ intent). Not: "How much is 100 USD in SEK?" (a conversion of a stated amount for a user).

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FX_NOW_SEK) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FX_NOW_SEK)

**`CREDIT_SCORE_VERIFY`** — judgment family · tier existing · H2 missions: —

Validates consumer credit bureau score ranges, adverse factors, and debt-to-income benchmarks.

#### `CREDIT_SCORE_VERIFY_GENERAL`

judgment

Validates consumer credit bureau score ranges, adverse factors, and debt-to-income benchmarks.

Contribute question pairs · adapter on `CREDIT_SCORE_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CREDIT_SCORE_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CREDIT_SCORE_VERIFY_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`CURRENCY_EXCHANGE`** — deterministic family · tier existing · H2 missions: —

Calculates fiat currency conversion rates and mid-market spot pricing across global currency pairs.

#### `CURRENCY_EXCHANGE_CONVERT`

deterministic · asks `from_currency`, `to_currency`, `amount` · answers `converted_amount`

Query asks to convert a stated amount between two currencies at today's rate. Example: "What is 100 USD in EUR right now?" → CURRENCY_EXCHANGE_CONVERT. Not: the bare rate with no amount to convert (FX_NOW_EUR, FX_NOW_CAD, FX_NOW_SEK). Not: a single asset's price with no second currency → CRYPTO_PRICE_USD or STOCK_PRICE_US_EQUITY.

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CURRENCY_EXCHANGE_CONVERT) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CURRENCY_EXCHANGE_CONVERT)

Not usable in an on-chain job yet: number field "converted_amount" has no decimals.

**`LOAN_INTEREST_RATE_QUOTE`** — judgment family · tier existing · H2 missions: —

Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.

#### `LOAN_INTEREST_RATE_QUOTE_GENERAL`

deterministic · asks `rate` · answers `rate_pct`

Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LOAN_INTEREST_RATE_QUOTE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LOAN_INTEREST_RATE_QUOTE_GENERAL)

Not usable in an on-chain job yet: number field "rate_pct" has no decimals.

## Geospatial & Remote Sensing

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`SATELLITE_IMAGERY_ANALYSIS_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SATELLITE_IMAGERY_ANALYSIS_GENERAL) | judgment | `SATELLITE_IMAGERY_ANALYSIS` (judgment) | question pairs · adapter on `SATELLITE_IMAGERY_ANALYSIS` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SATELLITE_IMAGERY_ANALYSIS_GENERAL) |

### Details

**`SATELLITE_IMAGERY_ANALYSIS`** — judgment family · tier mandatory · H2 missions: Conflict Intelligence, Resources & Agriculture, Autonomous Systems

Processes multispectral satellite feeds for land use changes, crop vegetation indexes, and infrastructure monitoring.

#### `SATELLITE_IMAGERY_ANALYSIS_GENERAL`

judgment · asks `location`, `question` · answers `location`, `findings`, `capture_date`, `summary`, `brief`

Query names or supplies satellite or aerial imagery over an area and asks what it shows: land use change, vegetation index, construction, infrastructure or damage. Example: "From the latest Sentinel-2 pass over this bounding box, has cropland vegetation index dropped since last month?" → SATELLITE_IMAGERY_ANALYSIS_GENERAL. Not: "Is this photo AI-generated?" (authenticity of a single image) → MEDIA_AUTHENTICITY_CHECK_GENERAL.

Contribute question pairs · adapter on `SATELLITE_IMAGERY_ANALYSIS`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SATELLITE_IMAGERY_ANALYSIS_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SATELLITE_IMAGERY_ANALYSIS_GENERAL)

## IoT & Telemetry

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`SENSOR_TELEMETRY_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SENSOR_TELEMETRY_VERIFY_GENERAL) | judgment | `SENSOR_TELEMETRY_VERIFY` (judgment) | question pairs · adapter on `SENSOR_TELEMETRY_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SENSOR_TELEMETRY_VERIFY_GENERAL) |

### Details

**`SENSOR_TELEMETRY_VERIFY`** — judgment family · tier mandatory · H2 missions: Resources & Agriculture, Autonomous Systems, Mining & Power

Validates edge sensor heartbeat signals, cryptographic payload integrity, and calibration threshold bounds.

#### `SENSOR_TELEMETRY_VERIFY_GENERAL`

judgment · asks `sensor`, `metric` · answers `sensor`, `metric`, `value`, `unit`, `observed_at`

Query names an IoT device, MQTT topic or sensor feed and asks whether its readings are live, within calibration bounds and cryptographically intact. Example: "Is device 44 on this MQTT topic still reporting, are its readings within calibration range, and does the payload HMAC verify?" → SENSOR_TELEMETRY_VERIFY_GENERAL. Not: "What is the PUE of the data hall?" (facility-level metrics) → DATACENTER_TELEMETRY_VERIFY_GENERAL.

Contribute question pairs · adapter on `SENSOR_TELEMETRY_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SENSOR_TELEMETRY_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SENSOR_TELEMETRY_VERIFY_GENERAL)

## Legal & Compliance

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`KYC_BIOMETRIC_LIVENESS_GENERAL`](https://anjoman.ai/dashboard/eval?intent=KYC_BIOMETRIC_LIVENESS_GENERAL) | judgment | `KYC_BIOMETRIC_LIVENESS` (judgment) | question pairs · adapter on `KYC_BIOMETRIC_LIVENESS` | [open](../../../issues?q=is%3Aissue+is%3Aopen+KYC_BIOMETRIC_LIVENESS_GENERAL) |
| [`SANCTIONS_SCREENING_MATCH_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SANCTIONS_SCREENING_MATCH_GENERAL) | judgment | `SANCTIONS_SCREENING_MATCH` (judgment) | question pairs · adapter on `SANCTIONS_SCREENING_MATCH` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SANCTIONS_SCREENING_MATCH_GENERAL) |
| [`CORPORATE_REGISTRY_LOOKUP_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CORPORATE_REGISTRY_LOOKUP_GENERAL) | deterministic | `CORPORATE_REGISTRY_LOOKUP` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+CORPORATE_REGISTRY_LOOKUP_GENERAL) |
| [`REGULATORY_FILING_MONITOR_GENERAL`](https://anjoman.ai/dashboard/eval?intent=REGULATORY_FILING_MONITOR_GENERAL) | deterministic | `REGULATORY_FILING_MONITOR` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+REGULATORY_FILING_MONITOR_GENERAL) |

### Details

**`KYC_BIOMETRIC_LIVENESS`** — judgment family · tier mandatory · H2 missions: —

Verifies user selfie liveness video capture against government photo IDs to prevent spoofing fraud.

#### `KYC_BIOMETRIC_LIVENESS_GENERAL`

judgment · asks `session` · answers `live`, `liveness_score`, `face_match`, `verdict`

Query supplies a selfie, liveness capture or video plus an identity document and asks whether the subject is a live human matching that document rather than a mask, print or replay. Requires actual media. Example: "Here is a selfie video and a passport scan: is this a live capture of the document holder, or a spoof?" → KYC_BIOMETRIC_LIVENESS_GENERAL. Not: "Is this photo AI-generated?" (media authenticity with no identity document to match against) → MEDIA_AUTHENTICITY_CHECK_GENERAL.

Contribute question pairs · adapter on `KYC_BIOMETRIC_LIVENESS`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=KYC_BIOMETRIC_LIVENESS_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+KYC_BIOMETRIC_LIVENESS_GENERAL)

**`SANCTIONS_SCREENING_MATCH`** — judgment family · tier mandatory · H2 missions: Exchange, Stablecoin, Institutional Markets, Legal, Conflict Intelligence, Commodities

Screens counterparties and beneficial owners against OFAC, EU, and UN consolidated financial sanctions lists.

#### `SANCTIONS_SCREENING_MATCH_GENERAL`

judgment · asks `name` · answers `name`, `matched`, `matches`, `lists`, `match_score`

Query supplies a person, company or wallet and asks whether it appears on OFAC, EU, UN or other consolidated sanctions lists, including near-matches on spelling or transliteration. Example: "Screen 'Ivan Petrov, DOB 1974, Cyprus' against the OFAC SDN and EU consolidated lists and report matches with confidence." → SANCTIONS_SCREENING_MATCH_GENERAL. Not: "Should we onboard this supplier?" (a full vendor check of tax IDs, banking and certifications, of which sanctions is one part) → VENDOR_VERIFY_GENERAL.

Contribute question pairs · adapter on `SANCTIONS_SCREENING_MATCH`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SANCTIONS_SCREENING_MATCH_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SANCTIONS_SCREENING_MATCH_GENERAL)

**`CORPORATE_REGISTRY_LOOKUP`** — judgment family · tier mandatory · H2 missions: Institutional Markets, Legal, Asset Management

Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.

#### `CORPORATE_REGISTRY_LOOKUP_GENERAL`

deterministic · asks `company`, `jurisdiction` · answers `legal_name`, `registration_id`, `active`, `jurisdiction`, `registered_address`, `incorporated`

Query names a company and asks for its official register record: incorporation status, company number, registered address or agent, directors, beneficial owners. Example: "What is the incorporation status and registered agent for UK company number 12345678?" → CORPORATE_REGISTRY_LOOKUP_GENERAL. Not: "Fill out this company record with its tax ID, headcount and executive contacts." (commercial enrichment beyond the register) → B2B_IDENTITY_ENRICHMENT_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CORPORATE_REGISTRY_LOOKUP_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CORPORATE_REGISTRY_LOOKUP_GENERAL)

**`REGULATORY_FILING_MONITOR`** — judgment family · tier mandatory · H2 missions: Legal, Asset Management

Parses statutory regulatory filings, 10-K/10-Q disclosures, and disclosure updates from financial oversight portals.

#### `REGULATORY_FILING_MONITOR_GENERAL`

deterministic · asks `entity`, `period` · answers `entity`, `filing_count`, `filings`, `urls`

Query names an issuer, ticker or regulator and asks whether a specific statutory filing has appeared, or for what it contains: 10-K, 10-Q, 8-K, exchange disclosures. Example: "Has Tesla filed its latest 10-Q on SEC EDGAR, on what date was it accepted, and what did it disclose about margins?" → REGULATORY_FILING_MONITOR_GENERAL. Not: "What is Tesla's P/E ratio?" (market data, not the filing) → FINANCIAL_DATA_GENERAL. Not: "Is Tesla Inc registered and who are its directors?" (a company register record) → CORPORATE_REGISTRY_LOOKUP_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=REGULATORY_FILING_MONITOR_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+REGULATORY_FILING_MONITOR_GENERAL)

## Logistics

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`CARRIER_SERVICEABILITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CARRIER_SERVICEABILITY_GENERAL) | judgment | `CARRIER_SERVICEABILITY` (judgment) | question pairs · adapter on `CARRIER_SERVICEABILITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CARRIER_SERVICEABILITY_GENERAL) |
| [`DELIVERY_WINDOW_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=DELIVERY_WINDOW_VERIFY_GENERAL) | judgment | `DELIVERY_WINDOW_VERIFY` (judgment) | question pairs · adapter on `DELIVERY_WINDOW_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+DELIVERY_WINDOW_VERIFY_GENERAL) |
| [`PACKAGE_STATUS_GENERAL`](https://anjoman.ai/dashboard/eval?intent=PACKAGE_STATUS_GENERAL) | deterministic | `PACKAGE_STATUS` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+PACKAGE_STATUS_GENERAL) |
| [`SHIPMENT_DELAY_RISK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SHIPMENT_DELAY_RISK_GENERAL) | judgment | `SHIPMENT_DELAY_RISK` (judgment) | question pairs · adapter on `SHIPMENT_DELAY_RISK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SHIPMENT_DELAY_RISK_GENERAL) |
| [`WAREHOUSE_INVENTORY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=WAREHOUSE_INVENTORY_GENERAL) | judgment | `WAREHOUSE_INVENTORY` (judgment) | question pairs · adapter on `WAREHOUSE_INVENTORY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+WAREHOUSE_INVENTORY_GENERAL) |

### Details

**`CARRIER_SERVICEABILITY`** — judgment family · tier mandatory · H2 missions: —

Evaluates freight and courier delivery coverage, weight limits, and hazardous material restrictions for target routes.

#### `CARRIER_SERVICEABILITY_GENERAL`

judgment · asks `carrier`, `area` · answers `carrier`, `area`, `serviceable`, `services`

Query asks whether a carrier will carry a given shipment on a given lane at all: coverage, weight and dimension limits, hazardous material restrictions. Example: "Will any carrier take a 68 kg lithium-battery shipment from 94107 to rural 59718, and under what restrictions?" → CARRIER_SERVICEABILITY_GENERAL. Not: "What would that shipment cost and when would it land?" (rates and ETA on a lane already known serviceable) → SHIP_RATE_ETA_GENERAL.

Contribute question pairs · adapter on `CARRIER_SERVICEABILITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CARRIER_SERVICEABILITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CARRIER_SERVICEABILITY_GENERAL)

**`DELIVERY_WINDOW_VERIFY`** — judgment family · tier mandatory · H2 missions: Consumer Platform, Consumer Automation

Confirms driver dispatch route scheduling, customer delivery appointment slots, and signature requirements.

#### `DELIVERY_WINDOW_VERIFY_GENERAL`

judgment · asks `carrier`, `route` · answers `carrier`, `transit_days_max`, `transit_days_min`, `route`, `is_estimate`

Query asks what delivery appointment window, route slot or signature requirement a dispatch system has committed for a stop or order. Example: "What appointment window is scheduled for order 8841 on tomorrow's route, and does it require a signature?" → DELIVERY_WINDOW_VERIFY_GENERAL. Not: "Where is the parcel right now?" (carrier scan events) → PACKAGE_STATUS_GENERAL.

Contribute question pairs · adapter on `DELIVERY_WINDOW_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=DELIVERY_WINDOW_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+DELIVERY_WINDOW_VERIFY_GENERAL)

**`PACKAGE_STATUS`** — judgment family · tier mandatory · H2 missions: —

Tracks real-time parcel checkpoint milestones, courier custody transfers, and delivery progress across logistics carriers.

#### `PACKAGE_STATUS_GENERAL`

deterministic

Query supplies a tracking number or shipment reference and asks where the parcel is and what its latest carrier scan events are. Example: "Where is tracking number 1Z999AA10123456784 now, and what was the last scan event?" → PACKAGE_STATUS_GENERAL. Not: "What would it cost to ship this and when would it arrive?" (a quote for a parcel not yet sent) → SHIP_RATE_ETA_GENERAL. Not: "What appointment window did dispatch commit for this stop?" (the dispatch schedule) → DELIVERY_WINDOW_VERIFY_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=PACKAGE_STATUS_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+PACKAGE_STATUS_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SHIPMENT_DELAY_RISK`** — judgment family · tier mandatory · H2 missions: —

Assesses predictive delay risk based on customs processing times, port congestion, weather conditions, and transport nodes.

#### `SHIPMENT_DELAY_RISK_GENERAL`

judgment · asks `shipment` · answers `risk_level`, `delay_probability`, `factors`, `summary`

Query names a shipment, container or lane in transit and asks for the forward-looking probability that it arrives late, weighing customs, port congestion, weather and carrier performance. The answer is a risk score; the truth only arrives later. Example: "What is the delay risk on this container arriving Rotterdam next week, given customs backlog and port congestion?" → SHIPMENT_DELAY_RISK_GENERAL. Not: "Where is the container right now?" (current position or status) → VESSEL_TELEMETRY_VERIFY_GENERAL or PACKAGE_STATUS_GENERAL.

Contribute question pairs · adapter on `SHIPMENT_DELAY_RISK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SHIPMENT_DELAY_RISK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SHIPMENT_DELAY_RISK_GENERAL)

**`WAREHOUSE_INVENTORY`** — judgment family · tier mandatory · H2 missions: Autonomous Systems

Audits bin and pallet level stock counts, pick-and-pack allocations, and replenishment thresholds in fulfillment centers.

#### `WAREHOUSE_INVENTORY_GENERAL`

judgment · asks `sku`, `warehouse` · answers `sku`, `warehouse`, `quantity`, `as_of`

Query asks for stock counts inside a fulfilment centre: bin or pallet quantities, allocations to open orders, replenishment thresholds. Internal, not what a shopper sees. Example: "How many units of SKU A-9912 are in bin 14C, and how many are already allocated to open orders?" → WAREHOUSE_INVENTORY_GENERAL. Not: "Is that SKU in stock at the retailer right now?" (merchant-facing availability) → SKU_IN_STOCK_GENERAL.

Contribute question pairs · adapter on `WAREHOUSE_INVENTORY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WAREHOUSE_INVENTORY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WAREHOUSE_INVENTORY_GENERAL)

## Logistics & Maritime

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`LIVE_PORT_CONGESTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LIVE_PORT_CONGESTION_GENERAL) | judgment | `LIVE_PORT_CONGESTION` (judgment) | question pairs · adapter on `LIVE_PORT_CONGESTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+LIVE_PORT_CONGESTION_GENERAL) |
| [`VESSEL_TELEMETRY_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=VESSEL_TELEMETRY_VERIFY_GENERAL) | deterministic | `VESSEL_TELEMETRY_VERIFY` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+VESSEL_TELEMETRY_VERIFY_GENERAL) |

### Details

**`LIVE_PORT_CONGESTION`** — judgment family · tier mandatory · H2 missions: Conflict Intelligence, Resources & Agriculture, Commodities

Measures commercial container port vessel queue wait times, berth occupancy ratios, and dwell day averages.

#### `LIVE_PORT_CONGESTION_GENERAL`

judgment · asks `port` · answers `port`, `vessels_waiting`, `wait_hours`, `congestion_level`, `as_of`

Query names a seaport or terminal and asks how congested it is: vessels waiting at anchor, berth occupancy, average dwell time. Example: "How many container vessels are at anchor off Long Beach, and what is average berth dwell time this week?" → LIVE_PORT_CONGESTION_GENERAL. Not: "Where is vessel IMO 9321483 right now?" (one ship's position) → VESSEL_TELEMETRY_VERIFY_GENERAL.

Contribute question pairs · adapter on `LIVE_PORT_CONGESTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LIVE_PORT_CONGESTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LIVE_PORT_CONGESTION_GENERAL)

**`VESSEL_TELEMETRY_VERIFY`** — judgment family · tier mandatory · H2 missions: Stablecoin, Conflict Intelligence, Resources & Agriculture, Commodities

Ingests maritime AIS positioning transponder data to track vessel speed, draft, bunker fuel burn, and nautical headings.

#### `VESSEL_TELEMETRY_VERIFY_GENERAL`

deterministic

Query names a vessel by name, MMSI or IMO and asks for its AIS-reported position, speed, heading, draft or declared destination. Example: "What is the current AIS position, speed and draft of MMSI 636019825?" → VESSEL_TELEMETRY_VERIFY_GENERAL. Not: "How backed up is the port it is heading into?" (port-level congestion) → LIVE_PORT_CONGESTION_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=VESSEL_TELEMETRY_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+VESSEL_TELEMETRY_VERIFY_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

## Macroeconomics & Finance

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`MACRO_ECONOMIC_INDICATOR_GENERAL`](https://anjoman.ai/dashboard/eval?intent=MACRO_ECONOMIC_INDICATOR_GENERAL) | deterministic | `MACRO_ECONOMIC_INDICATOR` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+MACRO_ECONOMIC_INDICATOR_GENERAL) |

### Details

**`MACRO_ECONOMIC_INDICATOR`** — judgment family · tier mandatory · H2 missions: Institutional Markets, Conflict Intelligence, Commodities, Mining & Power, Asset Management

Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.

#### `MACRO_ECONOMIC_INDICATOR_GENERAL`

deterministic · asks `indicator`, `country`, `year` · answers `rate_pct`

Query names a published macroeconomic statistic for a country or region - policy rate, CPI, unemployment, GDP - and asks for its released value or latest print. Example: "What was the latest US CPI year-over-year print, and what is the current federal funds target range?" → MACRO_ECONOMIC_INDICATOR_GENERAL. Not: "What is EUR/USD right now?" (a live market rate) → one of FX_NOW_EUR, FX_NOW_CAD, FX_NOW_SEK. Not: "What is Apple's revenue growth this quarter?" (company fundamentals) → FINANCIAL_DATA_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=MACRO_ECONOMIC_INDICATOR_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+MACRO_ECONOMIC_INDICATOR_GENERAL)

## Software / Engineering

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`CODE_PATCH_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CODE_PATCH_VERIFY_GENERAL) | judgment | `CODE_PATCH_VERIFY` (judgment) | question pairs · adapter on `CODE_PATCH_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CODE_PATCH_VERIFY_GENERAL) |
| [`CODE_REVIEW_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CODE_REVIEW_GENERAL) | judgment | `CODE_REVIEW` (judgment) | question pairs · adapter on `CODE_REVIEW` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CODE_REVIEW_GENERAL) |
| [`SECURITY_REVIEW_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SECURITY_REVIEW_GENERAL) | judgment | `SECURITY_REVIEW` (judgment) | question pairs · adapter on `SECURITY_REVIEW` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SECURITY_REVIEW_GENERAL) |
| [`CODE_GENERATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CODE_GENERATION_GENERAL) | judgment | `CODE_GENERATION` (judgment) | question pairs · adapter on `CODE_GENERATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CODE_GENERATION_GENERAL) |
| [`REGRESSION_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=REGRESSION_VERIFY_GENERAL) | judgment | `REGRESSION_VERIFY` (judgment) | question pairs · adapter on `REGRESSION_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+REGRESSION_VERIFY_GENERAL) |
| [`TASK_EXECUTION_QUALITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TASK_EXECUTION_QUALITY_GENERAL) | judgment | `TASK_EXECUTION_QUALITY` (judgment) | question pairs · adapter on `TASK_EXECUTION_QUALITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TASK_EXECUTION_QUALITY_GENERAL) |
| [`GRAMMAR_SPELL_CHECK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=GRAMMAR_SPELL_CHECK_GENERAL) | judgment | `GRAMMAR_SPELL_CHECK` (judgment) | question pairs · adapter on `GRAMMAR_SPELL_CHECK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+GRAMMAR_SPELL_CHECK_GENERAL) |

### Details

**`CODE_PATCH_VERIFY`** — judgment family · tier mandatory · H2 missions: Model Economy

Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.

#### `CODE_PATCH_VERIFY_GENERAL`

judgment · asks `patch` · answers `conclusion`, `passed`, `commit`, `pipeline`

Query supplies a patch, commit or branch and asks for a mechanical verdict: does it build, does the suite pass, is the named defect fixed, does anything regress. Example: "Apply this patch, run the build and test suite in a sandbox, and report whether it exits zero with the defect fixed and no regressions." → CODE_PATCH_VERIFY_GENERAL. Not: "Is this patch a sound approach?" (a judgment about the change) → CODE_REVIEW_GENERAL. Not: "Run the full suite against build 4412 and tell me what broke since the last green run." (regression sweep of an existing build, not verification of one patch) → REGRESSION_VERIFY_GENERAL.

Contribute question pairs · adapter on `CODE_PATCH_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CODE_PATCH_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CODE_PATCH_VERIFY_GENERAL)

**`CODE_REVIEW`** — judgment family · tier mandatory · H2 missions: Model Economy

Evaluates source code pull requests against internal architectural patterns, maintainability standards, and syntax rules.

#### `CODE_REVIEW_GENERAL`

judgment · asks `code` · answers `verdict`, `findings`, `summary`

Query supplies source code, a diff or a pull request and asks for a review of design, maintainability, readability or architectural fit. The output is an opinion, not a build result. Example: "Review this pull request for maintainability and whether it fits our service architecture: <diff>." → CODE_REVIEW_GENERAL. Not: "Does this patch compile and pass the test suite?" (a mechanical build/test verdict) → CODE_PATCH_VERIFY_GENERAL. Not: "Does this code leak secrets or pull vulnerable dependencies?" (a security scan) → SECURITY_REVIEW_GENERAL.

Contribute question pairs · adapter on `CODE_REVIEW`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CODE_REVIEW_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CODE_REVIEW_GENERAL)

**`SECURITY_REVIEW`** — judgment family · tier mandatory · H2 missions: Exchange, Model Economy, Web3 Native & DeFi

Scans codebase dependencies, API endpoints, and configuration files for common CVEs, secrets leakage, and misconfigurations.

#### `SECURITY_REVIEW_GENERAL`

judgment · asks `target` · answers `verdict`, `vulnerability_count`, `issues`, `summary`

Query supplies code, dependencies, endpoints or configuration and asks for security findings with severity: known CVEs in dependencies, leaked credentials, misconfiguration, injection-prone patterns. Example: "Scan this repository's dependencies and config for known CVEs, committed secrets and misconfigurations, with severities." → SECURITY_REVIEW_GENERAL. Not: "Is this code well structured and readable?" (a quality opinion with no security question) → CODE_REVIEW_GENERAL. Not: "What is the severity of CVE-2024-3094?" (one CVE record, no codebase supplied) → CVE_LOOKUP_CVSS.

Contribute question pairs · adapter on `SECURITY_REVIEW`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SECURITY_REVIEW_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SECURITY_REVIEW_GENERAL)

**`CODE_GENERATION`** — judgment family · tier existing · H2 missions: Personal Agent, Model Economy

Generates executable, type-safe code snippets and algorithms meeting specified functional specifications.

#### `CODE_GENERATION_GENERAL`

judgment

Generates executable, type-safe code snippets and algorithms meeting specified functional specifications.

Contribute question pairs · adapter on `CODE_GENERATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CODE_GENERATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CODE_GENERATION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`REGRESSION_VERIFY`** — judgment family · tier mandatory · H2 missions: Model Economy

Runs automated test suite executions to confirm backward compatibility across modified service APIs and libraries.

#### `REGRESSION_VERIFY_GENERAL`

judgment · asks `change` · answers `regression_found`, `verdict`, `failing_tests`, `summary`

Query asks for an automated test suite to be run against a build, service or API and for the resulting pass/fail set, to confirm previously working behaviour still works. Example: "Run the end-to-end suite against build 4412 of the checkout API and report which tests fail versus the last green run." → REGRESSION_VERIFY_GENERAL. Not: "Does this patch build and fix the defect?" (verifying one specific patch) → CODE_PATCH_VERIFY_GENERAL. Not: "Did the service meet its uptime target last month?" (an SLA threshold) → SLA_COMPLIANCE_GENERAL.

Contribute question pairs · adapter on `REGRESSION_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=REGRESSION_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+REGRESSION_VERIFY_GENERAL)

**`TASK_EXECUTION_QUALITY`** — judgment family · tier mandatory · H2 missions: Personal Agent, Autonomous Systems

Benchmarks automated job or agent execution outputs against gold-standard rubrics and expected schema constraints.

#### `TASK_EXECUTION_QUALITY_GENERAL`

judgment · asks `task`, `result` · answers `verdict`, `reason`, `score`

Query supplies an agent or job's actual output together with the task it was given, and asks how well it was executed against a rubric or an expected schema. Example: "Here is the task spec and the agent's output: score it against this rubric and the required JSON schema." → TASK_EXECUTION_QUALITY_GENERAL. Not: "Book me a flight and reserve a hotel." (a request to perform the task) → TASK_COMPLETION_GENERAL. Not: "Rate this model answer for factual accuracy and hallucination." (judging generative content itself) → LLM_OUTPUT_EVALUATION_GENERAL.

Contribute question pairs · adapter on `TASK_EXECUTION_QUALITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TASK_EXECUTION_QUALITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TASK_EXECUTION_QUALITY_GENERAL)

**`GRAMMAR_SPELL_CHECK`** — judgment family · tier existing · H2 missions: —

Detects typographical, orthographic, punctuation, and grammatical syntax errors with correction offsets.

#### `GRAMMAR_SPELL_CHECK_GENERAL`

judgment

Detects typographical, orthographic, punctuation, and grammatical syntax errors with correction offsets.

Contribute question pairs · adapter on `GRAMMAR_SPELL_CHECK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=GRAMMAR_SPELL_CHECK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+GRAMMAR_SPELL_CHECK_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

## Travel & Mobility

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`TRAVEL_DISRUPTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TRAVEL_DISRUPTION_GENERAL) | deterministic | `TRAVEL_DISRUPTION` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+TRAVEL_DISRUPTION_GENERAL) |
| [`FARE_RULE_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=FARE_RULE_VERIFY_GENERAL) | judgment | `FARE_RULE_VERIFY` (judgment) | question pairs · adapter on `FARE_RULE_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+FARE_RULE_VERIFY_GENERAL) |
| [`FLIGHT_AVAILABILITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=FLIGHT_AVAILABILITY_GENERAL) | judgment | `FLIGHT_AVAILABILITY` (judgment) | question pairs · adapter on `FLIGHT_AVAILABILITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+FLIGHT_AVAILABILITY_GENERAL) |
| [`HOTEL_AVAILABILITY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=HOTEL_AVAILABILITY_GENERAL) | judgment | `HOTEL_AVAILABILITY` (judgment) | question pairs · adapter on `HOTEL_AVAILABILITY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+HOTEL_AVAILABILITY_GENERAL) |
| [`ROUTE_ETA_GENERAL`](https://anjoman.ai/dashboard/eval?intent=ROUTE_ETA_GENERAL) | judgment | `ROUTE_ETA` (judgment) | question pairs · adapter on `ROUTE_ETA` | [open](../../../issues?q=is%3Aissue+is%3Aopen+ROUTE_ETA_GENERAL) |
| [`TRAVEL_TRANSIT_LOCK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TRAVEL_TRANSIT_LOCK_GENERAL) | judgment | `TRAVEL_TRANSIT_LOCK` (judgment) | question pairs · adapter on `TRAVEL_TRANSIT_LOCK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TRAVEL_TRANSIT_LOCK_GENERAL) |

### Details

**`TRAVEL_DISRUPTION`** — judgment family · tier mandatory · H2 missions: Consumer Automation

Detects and monitors flight delays, cancellations, gate shifts, and weather-driven travel disruptions in real time.

#### `TRAVEL_DISRUPTION_GENERAL`

deterministic · asks `route_or_flight` · answers `route_or_flight`, `disrupted`, `status`, `delay_minutes`, `reason`

Query names a flight, route or airport and asks about current operational disruption: delays, cancellations, gate changes, ground stops. Example: "Is DL404 delayed today, and is there an FAA ground stop at ATL?" → TRAVEL_DISRUPTION_GENERAL. Not: "Are there seats left on DL404 tomorrow?" (bookable inventory) → FLIGHT_AVAILABILITY_GENERAL. Not: "Will a storm hit Atlanta tomorrow?" (weather at a location, no flight operations) → STORM_ALERT_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TRAVEL_DISRUPTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TRAVEL_DISRUPTION_GENERAL)

**`FARE_RULE_VERIFY`** — judgment family · tier mandatory · H2 missions: —

Inspects fare terms, baggage allowances, cancellation penalties, and change fee stipulations for booked travel tickets.

#### `FARE_RULE_VERIFY_GENERAL`

judgment · asks `fare` · answers `fare`, `refundable`, `change_fee`, `rules`

Query names a ticket, fare or booking and asks what its rules permit: baggage allowance, change fees, cancellation penalties, refundability. Example: "For this booked fare, what checked baggage is included and what is the change fee to move the date?" → FARE_RULE_VERIFY_GENERAL. Not: "What seats are available on that route?" (inventory) → FLIGHT_AVAILABILITY_GENERAL. Not: "Can I return this purchase?" (a retail return policy) → RETURN_POLICY_VERIFY_GENERAL.

Contribute question pairs · adapter on `FARE_RULE_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FARE_RULE_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FARE_RULE_VERIFY_GENERAL)

**`FLIGHT_AVAILABILITY`** — judgment family · tier mandatory · H2 missions: —

Queries real-time airline schedule networks, cabin seat inventories, and booking fare class statuses.

#### `FLIGHT_AVAILABILITY_GENERAL`

judgment · asks `flight`, `date` · answers `flight`, `date`, `available`, `price`, `currency`

Query names a route or flight and dates and asks what seats, cabins or fare classes are bookable. Example: "What economy seats are available on SFO-JFK next Tuesday morning, and in which fare classes?" → FLIGHT_AVAILABILITY_GENERAL. Not: "Is my flight delayed today?" (operational disruption) → TRAVEL_DISRUPTION_GENERAL. Not: "What baggage allowance does that fare include?" (fare terms) → FARE_RULE_VERIFY_GENERAL.

Contribute question pairs · adapter on `FLIGHT_AVAILABILITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FLIGHT_AVAILABILITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FLIGHT_AVAILABILITY_GENERAL)

**`HOTEL_AVAILABILITY`** — judgment family · tier mandatory · H2 missions: —

Confirms room inventory, nightly rates, amenities, and cancellation policies across hospitality property management systems.

#### `HOTEL_AVAILABILITY_GENERAL`

judgment · asks `hotel`, `check_in`, `nights` · answers `hotel`, `check_in`, `available`, `price_per_night`, `currency`

Query names a property, city and dates and asks what rooms are available, at what nightly rate and under what cancellation terms. Example: "What king rooms are open at this Austin property for March 3-5, at what nightly rate, and are they refundable?" → HOTEL_AVAILABILITY_GENERAL. Not: "Is my reservation still being held?" (an existing booking lock) → TRAVEL_TRANSIT_LOCK_GENERAL.

Contribute question pairs · adapter on `HOTEL_AVAILABILITY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=HOTEL_AVAILABILITY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+HOTEL_AVAILABILITY_GENERAL)

**`ROUTE_ETA`** — judgment family · tier mandatory · H2 missions: Resources & Agriculture, Autonomous Systems

Computes multimodal routing itineraries, live traffic transit times, and turn-by-turn arrival estimations.

#### `ROUTE_ETA_GENERAL`

judgment · asks `origin`, `destination` · answers `duration`

Query names an origin and destination and asks for travel time, distance or the route itself under current traffic or transit conditions. Example: "How long is the drive from downtown Chicago to O'Hare right now, and which route is fastest?" → ROUTE_ETA_GENERAL. Not: "When will my parcel arrive?" (a carrier's delivery estimate) → PACKAGE_STATUS_GENERAL or SHIP_RATE_ETA_GENERAL.

Contribute question pairs · adapter on `ROUTE_ETA`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=ROUTE_ETA_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+ROUTE_ETA_GENERAL)

**`TRAVEL_TRANSIT_LOCK`** — judgment family · tier mandatory · H2 missions: —

Verifies and confirms fare holds, ticket reservation guarantees, and transit seat locking mechanisms.

#### `TRAVEL_TRANSIT_LOCK_GENERAL`

judgment · asks `booking` · answers `route`, `locked`, `price`, `currency`, `expires_at`

Query asks whether a fare hold, seat lock or booking guarantee currently exists and is still valid, naming a PNR, record locator or reservation reference. Example: "Is PNR X4RT9Z still holding two seats on the 09:15 departure, and when does the fare hold expire?" → TRAVEL_TRANSIT_LOCK_GENERAL. Not: "What seats are available on that flight?" (open inventory, nothing held) → FLIGHT_AVAILABILITY_GENERAL. Not: "What does that fare charge to change dates?" (fare terms) → FARE_RULE_VERIFY_GENERAL.

Contribute question pairs · adapter on `TRAVEL_TRANSIT_LOCK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TRAVEL_TRANSIT_LOCK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TRAVEL_TRANSIT_LOCK_GENERAL)

## Trust & Safety

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`MEDIA_FORENSIC_VERIFY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=MEDIA_FORENSIC_VERIFY_GENERAL) | judgment | `MEDIA_FORENSIC_VERIFY` (judgment) | question pairs · adapter on `MEDIA_FORENSIC_VERIFY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+MEDIA_FORENSIC_VERIFY_GENERAL) |
| [`PLAGIARISM_DETECTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=PLAGIARISM_DETECTION_GENERAL) | judgment | `PLAGIARISM_DETECTION` (judgment) | question pairs · adapter on `PLAGIARISM_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+PLAGIARISM_DETECTION_GENERAL) |
| [`SOCIAL_BOT_DETECTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SOCIAL_BOT_DETECTION_GENERAL) | judgment | `SOCIAL_BOT_DETECTION` (judgment) | question pairs · adapter on `SOCIAL_BOT_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+SOCIAL_BOT_DETECTION_GENERAL) |

### Details

**`MEDIA_FORENSIC_VERIFY`** — judgment family · tier mandatory · H2 missions: Conflict Intelligence, Consumer Platform

Detects AI deepfake artifacts, EXIF metadata manipulation, and generative audio/video synthesis in media uploads.

#### `MEDIA_FORENSIC_VERIFY_GENERAL`

judgment · asks `media_url` · answers `verdict`, `findings`, `confidence`, `summary`

Query supplies an image, audio or video file and asks for forensic analysis of manipulation: generative artifacts, splices, EXIF and metadata inconsistency, synthetic speech. Requires actual media. Example: "Run forensics on this audio clip: is the voice synthetic, and does the file metadata match the claimed capture date?" → MEDIA_FORENSIC_VERIFY_GENERAL. Not: "Is the face in this video a deepfake?" (face swap specifically) → DEEPFAKE_DETECTION_GENERAL. Not: "Is this photo real or AI-generated?" (the broad authenticity question) → MEDIA_AUTHENTICITY_CHECK_GENERAL.

Contribute question pairs · adapter on `MEDIA_FORENSIC_VERIFY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=MEDIA_FORENSIC_VERIFY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+MEDIA_FORENSIC_VERIFY_GENERAL)

**`PLAGIARISM_DETECTION`** — judgment family · tier existing · H2 missions: —

Detects verbatim text duplication, disguised paraphrasing, and uncredited citations across corpus databases.

#### `PLAGIARISM_DETECTION_GENERAL`

judgment

Detects verbatim text duplication, disguised paraphrasing, and uncredited citations across corpus databases.

Contribute question pairs · adapter on `PLAGIARISM_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=PLAGIARISM_DETECTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+PLAGIARISM_DETECTION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SOCIAL_BOT_DETECTION`** — judgment family · tier mandatory · H2 missions: Exchange, Consumer Platform

Classifies social media user accounts by post frequency anomalies, follower graph clusters, and coordinated inauthentic behavior.

#### `SOCIAL_BOT_DETECTION_GENERAL`

judgment · asks `account` · answers `account`, `verdict`, `bot_score`, `signals`

Query names a social account or a set of accounts and asks whether they are automated or coordinated: posting cadence anomalies, follower-graph clustering, inauthentic behaviour. There is no authoritative label; the answer is an inference. Example: "Is @handle a bot? Check posting cadence, follower-graph clustering and coordination with other accounts." → SOCIAL_BOT_DETECTION_GENERAL. Not: "What are people saying about the iPhone launch on X?" (a platform search) → TWITTER_SEARCH_GENERAL.

Contribute question pairs · adapter on `SOCIAL_BOT_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SOCIAL_BOT_DETECTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SOCIAL_BOT_DETECTION_GENERAL)

## Not yet categorised

| Intent | Kind | Family | Contribute | Bounty |
|---|---|---|---|---|
| [`ACADEMIC_SEARCH_GENERAL`](https://anjoman.ai/dashboard/eval?intent=ACADEMIC_SEARCH_GENERAL) | judgment | `ACADEMIC_SEARCH` (judgment) | question pairs · adapter on `ACADEMIC_SEARCH` | [open](../../../issues?q=is%3Aissue+is%3Aopen+ACADEMIC_SEARCH_GENERAL) |
| [`AGENT_TASK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=AGENT_TASK_GENERAL) | judgment | `AGENT_TASK` (judgment) | question pairs · adapter on `AGENT_TASK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+AGENT_TASK_GENERAL) |
| [`AI_TEXT_DETECTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=AI_TEXT_DETECTION_GENERAL) | judgment | `AI_TEXT_DETECTION` (judgment) | question pairs · adapter on `AI_TEXT_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+AI_TEXT_DETECTION_GENERAL) |
| [`CHAT_COMPLETION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CHAT_COMPLETION_GENERAL) | judgment | `CHAT_COMPLETION` (judgment) | question pairs · adapter on `CHAT_COMPLETION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CHAT_COMPLETION_GENERAL) |
| [`CONTENT_EXTRACTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CONTENT_EXTRACTION_GENERAL) | judgment | `CONTENT_EXTRACTION` (judgment) | question pairs · adapter on `CONTENT_EXTRACTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CONTENT_EXTRACTION_GENERAL) |
| [`CONTENT_MODERATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CONTENT_MODERATION_GENERAL) | judgment | `CONTENT_MODERATION` (judgment) | question pairs · adapter on `CONTENT_MODERATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CONTENT_MODERATION_GENERAL) |
| [`CONTENT_VERIFICATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=CONTENT_VERIFICATION_GENERAL) | judgment | `CONTENT_VERIFICATION` (judgment) | question pairs · adapter on `CONTENT_VERIFICATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+CONTENT_VERIFICATION_GENERAL) |
| [`CRYPTO_PRICE_USD`](https://anjoman.ai/dashboard/eval?intent=CRYPTO_PRICE_USD) | deterministic | `CRYPTO_PRICE` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+CRYPTO_PRICE_USD) |
| [`CVE_LOOKUP_CVSS`](https://anjoman.ai/dashboard/eval?intent=CVE_LOOKUP_CVSS) | deterministic | `CVE_LOOKUP` (hybrid) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+CVE_LOOKUP_CVSS) |
| [`DEEPFAKE_DETECTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=DEEPFAKE_DETECTION_GENERAL) | judgment | `DEEPFAKE_DETECTION` (judgment) | question pairs · adapter on `DEEPFAKE_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+DEEPFAKE_DETECTION_GENERAL) |
| [`FACT_CHECK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=FACT_CHECK_GENERAL) | judgment | `FACT_CHECK` (judgment) | question pairs · adapter on `FACT_CHECK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+FACT_CHECK_GENERAL) |
| [`FINANCIAL_DATA_GENERAL`](https://anjoman.ai/dashboard/eval?intent=FINANCIAL_DATA_GENERAL) | deterministic | `FINANCIAL_DATA` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+FINANCIAL_DATA_GENERAL) |
| [`FRAUD_DETECTION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=FRAUD_DETECTION_GENERAL) | judgment | `FRAUD_DETECTION` (judgment) | question pairs · adapter on `FRAUD_DETECTION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+FRAUD_DETECTION_GENERAL) |
| [`GAME_RESULT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=GAME_RESULT_GENERAL) | deterministic | `GAME_RESULT` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+GAME_RESULT_GENERAL) |
| [`GAS_PRICE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=GAS_PRICE_GENERAL) | deterministic | `GAS_PRICE` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+GAS_PRICE_GENERAL) |
| [`IMAGE_VERIFICATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=IMAGE_VERIFICATION_GENERAL) | judgment | `IMAGE_VERIFICATION` (judgment) | question pairs · adapter on `IMAGE_VERIFICATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+IMAGE_VERIFICATION_GENERAL) |
| [`IP_GEOLOCATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=IP_GEOLOCATION_GENERAL) | deterministic | `IP_GEOLOCATION` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+IP_GEOLOCATION_GENERAL) |
| [`LANGUAGE_GENERATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=LANGUAGE_GENERATION_GENERAL) | judgment | `LANGUAGE_GENERATION` (judgment) | question pairs · adapter on `LANGUAGE_GENERATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+LANGUAGE_GENERATION_GENERAL) |
| [`MEDIA_AUTHENTICITY_CHECK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=MEDIA_AUTHENTICITY_CHECK_GENERAL) | judgment | `MEDIA_AUTHENTICITY_CHECK` (judgment) | question pairs · adapter on `MEDIA_AUTHENTICITY_CHECK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+MEDIA_AUTHENTICITY_CHECK_GENERAL) |
| [`NEWS_HEADLINES_GENERAL`](https://anjoman.ai/dashboard/eval?intent=NEWS_HEADLINES_GENERAL) | judgment | `NEWS_HEADLINES` (judgment) | question pairs · adapter on `NEWS_HEADLINES` | [open](../../../issues?q=is%3Aissue+is%3Aopen+NEWS_HEADLINES_GENERAL) |
| [`NEWS_SEARCH_GENERAL`](https://anjoman.ai/dashboard/eval?intent=NEWS_SEARCH_GENERAL) | judgment | `NEWS_SEARCH` (judgment) | question pairs · adapter on `NEWS_SEARCH` | [open](../../../issues?q=is%3Aissue+is%3Aopen+NEWS_SEARCH_GENERAL) |
| [`ONCHAIN_TX_LOOKUP_GENERAL`](https://anjoman.ai/dashboard/eval?intent=ONCHAIN_TX_LOOKUP_GENERAL) | deterministic | `ONCHAIN_TX_LOOKUP` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+ONCHAIN_TX_LOOKUP_GENERAL) |
| [`RESEARCH_QUERY_GENERAL`](https://anjoman.ai/dashboard/eval?intent=RESEARCH_QUERY_GENERAL) | judgment | `RESEARCH_QUERY` (judgment) | question pairs · adapter on `RESEARCH_QUERY` | [open](../../../issues?q=is%3Aissue+is%3Aopen+RESEARCH_QUERY_GENERAL) |
| [`RESEARCH_SYNTHESIS_GENERAL`](https://anjoman.ai/dashboard/eval?intent=RESEARCH_SYNTHESIS_GENERAL) | judgment | `RESEARCH_SYNTHESIS` (judgment) | question pairs · adapter on `RESEARCH_SYNTHESIS` | [open](../../../issues?q=is%3Aissue+is%3Aopen+RESEARCH_SYNTHESIS_GENERAL) |
| [`SPORTS_SCORE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=SPORTS_SCORE_GENERAL) | deterministic | `SPORTS_SCORE` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+SPORTS_SCORE_GENERAL) |
| [`SSL_VERIFICATION_CERT`](https://anjoman.ai/dashboard/eval?intent=SSL_VERIFICATION_CERT) | deterministic | `SSL_VERIFICATION` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+SSL_VERIFICATION_CERT) |
| [`STOCK_PRICE_US_EQUITY`](https://anjoman.ai/dashboard/eval?intent=STOCK_PRICE_US_EQUITY) | deterministic | `STOCK_PRICE` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+STOCK_PRICE_US_EQUITY) |
| [`STORM_ALERT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=STORM_ALERT_GENERAL) | judgment | `STORM_ALERT` (judgment) | question pairs · adapter on `STORM_ALERT` | [open](../../../issues?q=is%3Aissue+is%3Aopen+STORM_ALERT_GENERAL) |
| [`TASK_COMPLETION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TASK_COMPLETION_GENERAL) | judgment | `TASK_COMPLETION` (judgment) | question pairs · adapter on `TASK_COMPLETION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TASK_COMPLETION_GENERAL) |
| [`TELEGRAPH_KNOWLEDGE_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TELEGRAPH_KNOWLEDGE_GENERAL) | judgment | `TELEGRAPH_KNOWLEDGE` (judgment) | question pairs · adapter on `TELEGRAPH_KNOWLEDGE` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TELEGRAPH_KNOWLEDGE_GENERAL) |
| [`TEXT_AUTHENTICITY_CHECK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TEXT_AUTHENTICITY_CHECK_GENERAL) | judgment | `TEXT_AUTHENTICITY_CHECK` (judgment) | question pairs · adapter on `TEXT_AUTHENTICITY_CHECK` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_AUTHENTICITY_CHECK_GENERAL) |
| [`TEXT_GENERATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TEXT_GENERATION_GENERAL) | judgment | `TEXT_GENERATION` (judgment) | question pairs · adapter on `TEXT_GENERATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_GENERATION_GENERAL) |
| [`TOKEN_HOLDER_COUNT_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TOKEN_HOLDER_COUNT_GENERAL) | deterministic | `TOKEN_HOLDER_COUNT` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+TOKEN_HOLDER_COUNT_GENERAL) |
| [`TVL_LOOKUP_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TVL_LOOKUP_GENERAL) | deterministic | `TVL_LOOKUP` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+TVL_LOOKUP_GENERAL) |
| [`TWITTER_SEARCH_GENERAL`](https://anjoman.ai/dashboard/eval?intent=TWITTER_SEARCH_GENERAL) | judgment | `TWITTER_SEARCH` (judgment) | question pairs · adapter on `TWITTER_SEARCH` | [open](../../../issues?q=is%3Aissue+is%3Aopen+TWITTER_SEARCH_GENERAL) |
| [`URL_SCAN_VERDICT`](https://anjoman.ai/dashboard/eval?intent=URL_SCAN_VERDICT) | hybrid | `URL_SCAN` (hybrid) | truth sources and question pairs · adapter on `URL_SCAN` | [open](../../../issues?q=is%3Aissue+is%3Aopen+URL_SCAN_VERDICT) |
| [`VIDEO_VERIFICATION_GENERAL`](https://anjoman.ai/dashboard/eval?intent=VIDEO_VERIFICATION_GENERAL) | judgment | `VIDEO_VERIFICATION` (judgment) | question pairs · adapter on `VIDEO_VERIFICATION` | [open](../../../issues?q=is%3Aissue+is%3Aopen+VIDEO_VERIFICATION_GENERAL) |
| [`WALLET_BALANCE_CHECK_GENERAL`](https://anjoman.ai/dashboard/eval?intent=WALLET_BALANCE_CHECK_GENERAL) | deterministic | `WALLET_BALANCE_CHECK` (judgment) | truth sources · no module (see above) | [open](../../../issues?q=is%3Aissue+is%3Aopen+WALLET_BALANCE_CHECK_GENERAL) |
| [`WEATHER_CHECK_TEMPERATURE`](https://anjoman.ai/dashboard/eval?intent=WEATHER_CHECK_TEMPERATURE) | deterministic | `WEATHER_CHECK` (deterministic) | truth sources · comparator already live | [open](../../../issues?q=is%3Aissue+is%3Aopen+WEATHER_CHECK_TEMPERATURE) |
| [`WEATHER_FORECAST_GENERAL`](https://anjoman.ai/dashboard/eval?intent=WEATHER_FORECAST_GENERAL) | judgment | `WEATHER_FORECAST` (judgment) | question pairs · adapter on `WEATHER_FORECAST` | [open](../../../issues?q=is%3Aissue+is%3Aopen+WEATHER_FORECAST_GENERAL) |
| [`WEB_SEARCH_GENERAL`](https://anjoman.ai/dashboard/eval?intent=WEB_SEARCH_GENERAL) | judgment | `WEB_SEARCH` (judgment) | question pairs · adapter on `WEB_SEARCH` | [open](../../../issues?q=is%3Aissue+is%3Aopen+WEB_SEARCH_GENERAL) |

### Details

**`ACADEMIC_SEARCH`** — judgment family · tier network · H2 missions: —

#### `ACADEMIC_SEARCH_GENERAL`

judgment · asks `query` · answers `answer`, `paper_titles`, `dois`, `total_matches`, `brief`

Query asks to search scholarly papers, journals or academic literature specifically, rather than the general web. Example: "Find peer-reviewed papers on CRISPR gene editing published in the last two years." → ACADEMIC_SEARCH_GENERAL. Not: "What is CRISPR gene editing?" (general knowledge question, not a request to search scholarly literature) → CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `ACADEMIC_SEARCH`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=ACADEMIC_SEARCH_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+ACADEMIC_SEARCH_GENERAL)

**`AGENT_TASK`** — judgment family · tier network · H2 missions: —

#### `AGENT_TASK_GENERAL`

judgment · asks `task` · answers `result`, `status`, `steps`, `sources`, `brief`

Query asks about autonomous AI agent behavior specifically (tool use, taking actions, multi-step autonomy) as distinct from a standard chatbot, or is itself a request requiring autonomous multi-step action. Example: "How does an AI agent decide when to call a tool versus answering directly?" → AGENT_TASK_GENERAL. Not: "Book me a flight and then reserve a hotel." (a concrete multi-step task to execute, not a question about agent behavior) → TASK_COMPLETION_GENERAL.

Contribute question pairs · adapter on `AGENT_TASK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=AGENT_TASK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+AGENT_TASK_GENERAL)

**`AI_TEXT_DETECTION`** — judgment family · tier network · H2 missions: —

#### `AI_TEXT_DETECTION_GENERAL`

judgment · asks `text` · answers `verdict`, `ai_likelihood`, `cues`

Query provides a specific block of text and asks whether it was written by an AI or a human. The user must supply actual text content to analyze — a question that merely asks about AI detection conceptually (without providing text to analyze) is not this intent. Example: "Here's a paragraph: '...'. Was this written by an AI or a human?" → AI_TEXT_DETECTION_GENERAL. Not: "How do AI text detectors work?" (asks about the method conceptually, no text supplied to analyze) → CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `AI_TEXT_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=AI_TEXT_DETECTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+AI_TEXT_DETECTION_GENERAL)

**`CHAT_COMPLETION`** — judgment family · tier network · H2 missions: —

#### `CHAT_COMPLETION_GENERAL`

judgment · asks `message` · answers `reply`, `verdict`, `brief`

General knowledge, reasoning, explanation, or conversational question answerable directly without live data, external sources, or specialized tooling. This is the default/general-purpose intent when nothing more specific clearly fits — e.g. 'explain what X does.' Example: "Why is the sky blue?" → CHAT_COMPLETION_GENERAL. Not: "What's the current price of Bitcoin?" (needs live, external data) → CRYPTO_PRICE_USD or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `CHAT_COMPLETION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CHAT_COMPLETION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CHAT_COMPLETION_GENERAL)

**`CONTENT_EXTRACTION`** — judgment family · tier network · H2 missions: —

#### `CONTENT_EXTRACTION_GENERAL`

judgment · asks `content`, `fields` · answers `title`, `content`, `url`, `entities`, `brief`

Query supplies unstructured content and asks for specific structured fields to be pulled out of it. Example: "Here's a receipt (as text): '...', extract the merchant name, date, and total amount." → CONTENT_EXTRACTION_GENERAL. Not: "What sentiment does this receipt's review comment express?" (asks for a judgment, not structured fields pulled out) → SENTIMENT_ANALYSIS_GENERAL.

Contribute question pairs · adapter on `CONTENT_EXTRACTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CONTENT_EXTRACTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CONTENT_EXTRACTION_GENERAL)

**`CONTENT_MODERATION`** — judgment family · tier network · H2 missions: —

#### `CONTENT_MODERATION_GENERAL`

judgment · asks `text` · answers `verdict`, `flagged`, `categories`, `reason`

Query is itself asking to classify, flag, or moderate a specific piece of provided content, OR asks how automated content moderation works as a method/technique — not merely a question that mentions moderation as an unrelated concept. Example: "Does this comment violate community guidelines: 'You're an idiot and should quit.'?" or "How do automated moderation systems detect hate speech?" → CONTENT_MODERATION_GENERAL. Not: "Should platforms moderate more content?" (an opinion/policy question that only mentions moderation as a topic) → CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `CONTENT_MODERATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CONTENT_MODERATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CONTENT_MODERATION_GENERAL)

**`CONTENT_VERIFICATION`** — judgment family · tier network · H2 missions: —

#### `CONTENT_VERIFICATION_GENERAL`

judgment · asks `content` · answers `verdict`, `confidence`, `answer`, `evidence`

Query asks whether a specific piece of supplied content is genuine and unaltered, covering provenance and integrity generally rather than media forensics specifically. Example: "Here's the text of a press release: '...'. Is this the genuine, unaltered version the company issued, or has it been tampered with?" or "Here's a copy of a contract clause: '...'. Is this the original wording, or has it been altered?" → CONTENT_VERIFICATION_GENERAL. Not: "Is this image a deepfake?" (media-specific forensics question) → DEEPFAKE_DETECTION_GENERAL.

Contribute question pairs · adapter on `CONTENT_VERIFICATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CONTENT_VERIFICATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CONTENT_VERIFICATION_GENERAL)

**`CRYPTO_PRICE`** — deterministic family · tier network · H2 missions: —

#### `CRYPTO_PRICE_USD`

deterministic · asks `symbol` · answers `price_usd`

Query names a cryptocurrency asset and asks for its CURRENT price in US dollars. Example: "What is the current price of Ethereum (ETH) in USD?" → CRYPTO_PRICE_USD. Not: "How much ETH does 0x6872...de hold?" (a balance, not a price) → WALLET_BALANCE_CHECK_GENERAL. Not: market cap or 24h volume (broader market data) → FINANCIAL_DATA_GENERAL.

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CRYPTO_PRICE_USD) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CRYPTO_PRICE_USD)

Not usable in an on-chain job yet: number field "price_usd" has no decimals.

**`CVE_LOOKUP`** — hybrid family · tier network · H2 missions: —

#### `CVE_LOOKUP_CVSS`

deterministic · asks `cve_id` · answers `cve_id`, `cvss_score`, `severity`, `description`, `published`, `references`

Query supplies a CVE identifier and asks for its CVSS severity score. Example: "What is the CVSS score of CVE-2021-44228?" → CVE_LOOKUP_CVSS. Not: "What are the most dangerous vulnerabilities this year?" (no CVE identifier) → WEB_SEARCH_GENERAL. Not: ranking a set of findings → VULNERABILITY_TRIAGE_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=CVE_LOOKUP_CVSS) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+CVE_LOOKUP_CVSS)

**`DEEPFAKE_DETECTION`** — judgment family · tier network · H2 missions: —

#### `DEEPFAKE_DETECTION_GENERAL`

judgment · asks `media_url` · answers `verdict`, `confidence`, `evidence`, `summary`

Query includes an actual image or video URL/reference and specifically asks whether it is a deepfake or whether a face/person in it has been synthetically generated or swapped. Requires real attached media — the word 'deepfake' alone with no media reference does not qualify. Example: "Here's a video URL: [link]. Is the face in this a deepfake?" → DEEPFAKE_DETECTION_GENERAL. Not: "What is a deepfake and how are they made?" (conceptual question, no media referenced) → CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `DEEPFAKE_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=DEEPFAKE_DETECTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+DEEPFAKE_DETECTION_GENERAL)

**`FACT_CHECK`** — judgment family · tier network · H2 missions: —

#### `FACT_CHECK_GENERAL`

judgment · asks `claim` · answers `claim`, `verdict`, `reasoning`, `sources`

Query supplies a specific claim or statement and asks whether it is true, with supporting evidence. A general knowledge question is CHAT_COMPLETION_GENERAL — this intent requires a checkable claim. Example: "Is it true that drinking coffee stunts your growth? Verify this claim." → FACT_CHECK_GENERAL. Not: "Does coffee have any health effects?" (open-ended question, not a specific claim to verify) → CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `FACT_CHECK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FACT_CHECK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FACT_CHECK_GENERAL)

**`FINANCIAL_DATA`** — judgment family · tier network · H2 missions: —

#### `FINANCIAL_DATA_GENERAL`

deterministic · asks `asset` · answers `asset`, `market_cap_usd`, `volume_24h_usd`, `metrics`, `as_of`

Query asks for market data, company fundamentals, or financial statistics beyond a single quoted price. Example: "Give the market cap and 24h trading volume for token X on base." or "What is Apple's P/E ratio and revenue growth this quarter?" → FINANCIAL_DATA_GENERAL. Not: "What is the price of token X?" or "What is Apple's share price?" alone (single quoted price) → CRYPTO_PRICE_USD or STOCK_PRICE_US_EQUITY.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FINANCIAL_DATA_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FINANCIAL_DATA_GENERAL)

**`FRAUD_DETECTION`** — judgment family · tier network · H2 missions: —

#### `FRAUD_DETECTION_GENERAL`

judgment · asks `subject` · answers `subject`, `verdict`, `risk_score`, `signals`, `summary`

Query asks how likely a specific entity, transaction or action is to be fraudulent. Example: "How likely is it that this transaction from 0xabc123... is fraudulent?" or "Does this email asking me to wire money to a new account look like a scam?" → FRAUD_DETECTION_GENERAL. Not: "What is the status of transaction 0xabc123...?" (asks for transaction details, not a fraud likelihood judgment) → ONCHAIN_TX_LOOKUP_GENERAL.

Contribute question pairs · adapter on `FRAUD_DETECTION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=FRAUD_DETECTION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+FRAUD_DETECTION_GENERAL)

**`GAME_RESULT`** — judgment family · tier network · H2 missions: —

#### `GAME_RESULT_GENERAL`

deterministic · asks `game` · answers `winner`, `home_team`, `away_team`, `home_score`, `away_score`, `date`

Query names a specific completed sports fixture or competition and asks for its final outcome or winner. Distinct from an in-progress or live score, which is SPORTS_SCORE_GENERAL. Example: "Who won the Lakers vs Celtics game last night?" → GAME_RESULT_GENERAL. Not: "What's the current score in the Lakers vs Celtics game right now?" (still in progress) → SPORTS_SCORE_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=GAME_RESULT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+GAME_RESULT_GENERAL)

**`GAS_PRICE`** — judgment family · tier network · H2 missions: —

#### `GAS_PRICE_GENERAL`

deterministic · asks `chain` · answers `chain`, `gas_price_gwei`, `transfer_fee_usd`, `as_of`

Query asks for the current or recent transaction fee level on a named blockchain network. Distinct from the price of that chain's token, which is CRYPTO_PRICE_USD. Example: "What is the current gas price in Gwei on the Ethereum network?" or informally "Polygon fees felt high yesterday, what are they at now?" → GAS_PRICE_GENERAL. Not: a question with a similar 'it was X yesterday, what about now' shape but no blockchain network named → not GAS_PRICE_GENERAL (a network name like Polygon/Ethereum/Base is not a weather location, don't route this to WEATHER_FORECAST_GENERAL).

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=GAS_PRICE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+GAS_PRICE_GENERAL)

**`IMAGE_VERIFICATION`** — judgment family · tier network · H2 missions: —

#### `IMAGE_VERIFICATION_GENERAL`

judgment · asks `image_url` · answers `verdict`, `confidence`, `evidence`, `summary`

Query includes an actual image URL/reference and asks whether it has been digitally manipulated, edited, or spliced (distinct from asking if it's AI-generated outright — that's MEDIA_AUTHENTICITY_CHECK_GENERAL). Requires real attached media. Example: "Here's an image URL: [link]. Has this photo been edited or spliced?" → IMAGE_VERIFICATION_GENERAL. Not: "Here's an image URL: [link]. Is this AI-generated?" (asks if it's AI-generated outright, not edited/spliced) → MEDIA_AUTHENTICITY_CHECK_GENERAL.

Contribute question pairs · adapter on `IMAGE_VERIFICATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=IMAGE_VERIFICATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+IMAGE_VERIFICATION_GENERAL)

**`IP_GEOLOCATION`** — judgment family · tier network · H2 missions: —

#### `IP_GEOLOCATION_GENERAL`

deterministic

Query supplies an IP address and asks where it is located geographically. For abuse history, use THREAT_INTELLIGENCE_INDICATOR. Example: "Where is the IP address 8.8.8.8 located?" → IP_GEOLOCATION_GENERAL. Not: "Has the IP address 8.8.8.8 been flagged for abuse?" (asks about reputation/abuse history, not location) → IP_REPUTATION (if registered) or CHAT_COMPLETION_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=IP_GEOLOCATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+IP_GEOLOCATION_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`LANGUAGE_GENERATION`** — judgment family · tier network · H2 missions: —

#### `LANGUAGE_GENERATION_GENERAL`

judgment · asks `prompt`, `target` · answers `text`, `target`, `brief`

Query asks about how language generation works as a capability or technique, or requests free-form natural-language output from a described prompt. Prefer CHAT_COMPLETION_GENERAL for ordinary conversational questions. Example: "Explain how transformer-based language generation models decide the next word." → LANGUAGE_GENERATION_GENERAL. Not: "Write me a short poem about autumn." (an ordinary request for produced text) → TEXT_GENERATION_GENERAL.

Contribute question pairs · adapter on `LANGUAGE_GENERATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=LANGUAGE_GENERATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+LANGUAGE_GENERATION_GENERAL)

**`MEDIA_AUTHENTICITY_CHECK`** — judgment family · tier network · H2 missions: —

#### `MEDIA_AUTHENTICITY_CHECK_GENERAL`

judgment · asks `media_url` · answers `verdict`, `confidence`, `evidence`, `summary`

Query includes an actual image or video URL/reference and asks broadly whether it is authentic, real, or AI-generated. Words like 'authentic,' 'real,' 'validity,' or 'genuine' alone, with no actual media attached, do NOT qualify. Example: "Here's an image URL: [link]. Is this photo real or AI-generated?" → MEDIA_AUTHENTICITY_CHECK_GENERAL. Not: "What is the technical validity of X's claims?" (uses 'validity' but has no media reference at all) → WEB_SEARCH_GENERAL or CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `MEDIA_AUTHENTICITY_CHECK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=MEDIA_AUTHENTICITY_CHECK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+MEDIA_AUTHENTICITY_CHECK_GENERAL)

**`NEWS_HEADLINES`** — judgment family · tier network · H2 missions: —

#### `NEWS_HEADLINES_GENERAL`

judgment · asks `topic` · answers `topic`, `headlines`, `urls`, `window`, `top_headline`

Query asks for current news headlines for a topic or region, as a list rather than full articles. Example: "Give me today's top headlines about the tech industry." → NEWS_HEADLINES_GENERAL. Not: "Give me a detailed article about the latest tech industry merger." (wants full article content, not a headline list) → NEWS_SEARCH_GENERAL.

Contribute question pairs · adapter on `NEWS_HEADLINES`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=NEWS_HEADLINES_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+NEWS_HEADLINES_GENERAL)

**`NEWS_SEARCH`** — judgment family · tier network · H2 missions: —

#### `NEWS_SEARCH_GENERAL`

judgment · asks `query` · answers `answer`, `result_count`, `sources`, `brief`

Query asks for news articles or coverage matching a topic, entity or time period. Prefer NEWS_HEADLINES_GENERAL when the user wants a headline list rather than article results. Example: "Find recent articles covering the merger between company X and company Y." → NEWS_SEARCH_GENERAL. Not: "Just give me the top headlines about company X." (wants a headline list, not article coverage) → NEWS_HEADLINES_GENERAL.

Contribute question pairs · adapter on `NEWS_SEARCH`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=NEWS_SEARCH_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+NEWS_SEARCH_GENERAL)

**`ONCHAIN_TX_LOOKUP`** — judgment family · tier network · H2 missions: —

#### `ONCHAIN_TX_LOOKUP_GENERAL`

deterministic · asks `tx_hash`, `chain` · answers `tx_hash`, `status`, `from`, `to`, `block_number`, `value_eth`

Query supplies a transaction hash or names a specific on-chain transaction and asks for its details, status or effects. Requires an actual transaction reference, not a general question about how transactions work. Example: "What was the status and gas used of transaction 0xabc123...?" → ONCHAIN_TX_LOOKUP_GENERAL. Not: a question about a wallet's overall balance → WALLET_BALANCE_CHECK_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=ONCHAIN_TX_LOOKUP_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+ONCHAIN_TX_LOOKUP_GENERAL)

**`RESEARCH_QUERY`** — judgment family · tier network · H2 missions: —

#### `RESEARCH_QUERY_GENERAL`

judgment · asks `question` · answers `answer`, `source_count`, `sources`, `brief`

Query asks a research question and expects an answer supported by citations to sources. Example: "What does the evidence say about the health effects of intermittent fasting? Cite your sources." → RESEARCH_QUERY_GENERAL. Not: "Summarize everything known about intermittent fasting across all major studies." (wants a broad multi-source synthesis, not a cited answer to one question) → RESEARCH_SYNTHESIS_GENERAL.

Contribute question pairs · adapter on `RESEARCH_QUERY`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=RESEARCH_QUERY_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+RESEARCH_QUERY_GENERAL)

**`RESEARCH_SYNTHESIS`** — judgment family · tier network · H2 missions: —

#### `RESEARCH_SYNTHESIS_GENERAL`

judgment · asks `question` · answers `answer`, `source_count`, `sources`, `brief`

Query asks to gather findings across multiple sources and synthesise them into a combined answer or summary, rather than returning a single fact or a list of links. Example: "Summarize what the latest studies say about coffee's effect on longevity, across multiple sources." → RESEARCH_SYNTHESIS_GENERAL. Not: "What's one study that looked at coffee and longevity?" (wants a single source/fact, not a synthesis) → RESEARCH_QUERY_GENERAL or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `RESEARCH_SYNTHESIS`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=RESEARCH_SYNTHESIS_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+RESEARCH_SYNTHESIS_GENERAL)

**`SPORTS_SCORE`** — judgment family · tier network · H2 missions: —

#### `SPORTS_SCORE_GENERAL`

deterministic

Query names a specific sports fixture, team or competition and asks for the current or most recent score. Distinct from asking who ultimately won a finished event, which is GAME_RESULT_GENERAL. Example: "What's the current score in the Lakers vs Celtics game right now?" → SPORTS_SCORE_GENERAL. Not: "Who won the Lakers vs Celtics game last night?" (event already concluded, asks for final outcome) → GAME_RESULT_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SPORTS_SCORE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SPORTS_SCORE_GENERAL)

Not usable in an on-chain job yet: the intent has no response format.

**`SSL_VERIFICATION`** — deterministic family · tier network · H2 missions: —

#### `SSL_VERIFICATION_CERT`

deterministic · asks `host` · answers `certificate_valid`

Query supplies a hostname and asks whether its TLS/SSL certificate is currently valid and trusted. Example: "Is the SSL certificate for example.com valid?" → SSL_VERIFICATION_CERT. Not: "Is example.com a safe site to visit?" (general safety judgment) → URL_SCAN_VERDICT.

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=SSL_VERIFICATION_CERT) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+SSL_VERIFICATION_CERT)

**`STOCK_PRICE`** — deterministic family · tier network · H2 missions: —

#### `STOCK_PRICE_US_EQUITY`

deterministic · asks `ticker` · answers `price_usd`

Query names a US-listed equity or its ticker and asks for the CURRENT share price in US dollars. A company mentioned in passing does not qualify. Example: "What is the current share price of Apple (AAPL)?" → STOCK_PRICE_US_EQUITY. Not: "Apple just released a new iPhone, will sales be strong?" (company named, no price asked) → CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL. Not: a historical price on a past date.

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=STOCK_PRICE_US_EQUITY) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+STOCK_PRICE_US_EQUITY)

Not usable in an on-chain job yet: number field "price_usd" has no decimals.

**`STORM_ALERT`** — judgment family · tier network · H2 missions: —

#### `STORM_ALERT_GENERAL`

judgment · asks `location`, `window_hours` · answers `location`, `risk_score`, `risk_level`, `peak_gust_kmh`, `precipitation_mm`, `window`

Query names a specific, resolvable location and asks specifically about active or upcoming storm systems, high winds, or disruption risk from severe weather there — not general current conditions. Example: "Is there a hurricane warning in effect for Miami, Florida right now?" → STORM_ALERT_GENERAL. Not: a question with no resolvable location, even if it uses risk/disruption-sounding words like 'high,' 'surge,' or 'glitch' → do not route to STORM_ALERT_GENERAL just on word-shape; use CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `STORM_ALERT`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=STORM_ALERT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+STORM_ALERT_GENERAL)

**`TASK_COMPLETION`** — judgment family · tier network · H2 missions: —

#### `TASK_COMPLETION_GENERAL`

judgment · asks `task` · answers `result`, `status`, `steps`, `brief`

Query asks about what makes an AI agent effective at completing multi-step tasks, or is itself a request to complete a defined multi-step task end-to-end. Example: "Book me a flight to New York and then reserve a hotel near the airport for those dates." → TASK_COMPLETION_GENERAL. Not: "How do AI agents decide which tool to call?" (asks about agent behavior/mechanics, not a request to perform a task) → AGENT_TASK_GENERAL.

Contribute question pairs · adapter on `TASK_COMPLETION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TASK_COMPLETION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TASK_COMPLETION_GENERAL)

**`TELEGRAPH_KNOWLEDGE`** — judgment family · tier network · H2 missions: —

#### `TELEGRAPH_KNOWLEDGE_GENERAL`

judgment · asks `question` · answers `answer`, `knowledge_topic`, `sources`, `brief`

Query asks about Telegraph, Telegraph protocol, its products, or ecosystem — including Alexandria (flagship intelligence layer), the Explorer (leaderboard, live feed, signal search), Hackathon, WASM/miner registration, intents, the Miner YAML Registry (integrate.telegraphprotocol.com), current miners or their details, and any applications built on Telegraph (TruthWire, TrustFilter, ScholarGuard, ReviewRadar). Also covers protocol fundamentals like tokenomics, architecture, documentation, earning, and how the system works. Also covers any question where the user addresses the assistant directly as "you" (e.g. "what can you do", "who are you", "how can I use you") — the assistant is Telegraph. Use this for ANY question related to Telegraph, its products, platforms, ecosystem, or the assistant itself, rather than routing to general CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL. Example: "What can you do?" or "How do I register a miner on Telegraph?" → TELEGRAPH_KNOWLEDGE_GENERAL. Not: "What can an AI agent do in general?" (asks about AI agents generically, not about Telegraph or the assistant itself) → AGENT_TASK_GENERAL or CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `TELEGRAPH_KNOWLEDGE`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TELEGRAPH_KNOWLEDGE_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TELEGRAPH_KNOWLEDGE_GENERAL)

**`TEXT_AUTHENTICITY_CHECK`** — judgment family · tier network · H2 missions: —

#### `TEXT_AUTHENTICITY_CHECK_GENERAL`

judgment · asks `text` · answers `verdict`, `reasons`, `confidence`

Query supplies a block of text and asks whether it is genuine, original, or machine-generated. Where the user explicitly asks about AI authorship, prefer AI_TEXT_DETECTION_GENERAL. Example: "Here's an essay: '...'. Is this original writing or was it copied/plagiarized from somewhere else?" → TEXT_AUTHENTICITY_CHECK_GENERAL. Not: "Here's a paragraph: '...'. Was this written by an AI or a human?" (explicitly asks about AI authorship) → AI_TEXT_DETECTION_GENERAL.

Contribute question pairs · adapter on `TEXT_AUTHENTICITY_CHECK`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TEXT_AUTHENTICITY_CHECK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_AUTHENTICITY_CHECK_GENERAL)

**`TEXT_GENERATION`** — judgment family · tier network · H2 missions: —

#### `TEXT_GENERATION_GENERAL`

judgment · asks `prompt` · answers `text`, `title`, `brief`

Query asks for free-form written output for a described task — drafting, rewriting, summarising or composing text. Prefer CHAT_COMPLETION_GENERAL when the user simply wants an answer rather than produced text. Example: "Write a short poem about autumn." or "Rewrite this paragraph to sound more formal." → TEXT_GENERATION_GENERAL. Not: "What makes a good poem?" (wants an answer/explanation, not produced text) → CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `TEXT_GENERATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TEXT_GENERATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TEXT_GENERATION_GENERAL)

**`TOKEN_HOLDER_COUNT`** — judgment family · tier network · H2 missions: —

#### `TOKEN_HOLDER_COUNT_GENERAL`

deterministic · asks `token`, `chain` · answers `token`, `chain`, `holders_count`, `token_symbol`

Query names a specific token or contract address and asks how many distinct addresses hold it. Not a request for the token's price, supply or market data. Example: "How many distinct holder addresses does the ERC-20 token contract 0x8335...913 on base have?" → TOKEN_HOLDER_COUNT_GENERAL. Not: "How much ETH does 0x6872...de hold on ethereum?" (one address's own balance, not a headcount of holders) → WALLET_BALANCE_CHECK_GENERAL. Not: "How deep is this token's own trading liquidity in DEX pools? Give this token's pool liquidity in USD." (a liquidity/TVL question, not a holder count, even though it names a token contract) → TVL_LOOKUP_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TOKEN_HOLDER_COUNT_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TOKEN_HOLDER_COUNT_GENERAL)

**`TVL_LOOKUP`** — judgment family · tier network · H2 missions: —

#### `TVL_LOOKUP_GENERAL`

deterministic · asks `protocol` · answers `protocol_or_chain`, `tvl_usd`, `chain_tvl_usd`, `as_of`

Query names a specific DeFi protocol, pool or chain and asks for the total value locked in it. Distinct from a token's market capitalisation. Example: "For the token at contract 0x8335...913 on base, how deep is its own trading liquidity in DEX pools (e.g. Uniswap)? Give this token's pool liquidity in USD." → TVL_LOOKUP_GENERAL. Not: a question asking how many addresses hold a token → TOKEN_HOLDER_COUNT_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TVL_LOOKUP_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TVL_LOOKUP_GENERAL)

**`TWITTER_SEARCH`** — judgment family · tier network · H2 missions: —

#### `TWITTER_SEARCH_GENERAL`

judgment · asks `query` · answers `answer`, `posts`, `authors`, `urls`, `brief`

Query asks to search posts, accounts or discussion on X/Twitter specifically. A question that merely mentions Twitter as a topic does not qualify — the user must want results from the platform. Example: "What are people saying about the new iPhone launch on X/Twitter?" → TWITTER_SEARCH_GENERAL. Not: "Is Twitter/X profitable as a company?" (Twitter is the subject, not the source to search) → CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `TWITTER_SEARCH`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=TWITTER_SEARCH_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+TWITTER_SEARCH_GENERAL)

**`URL_SCAN`** — hybrid family · tier network · H2 missions: —

#### `URL_SCAN_VERDICT`

hybrid · asks `url` · answers `safe`

Query supplies a URL and asks whether it is safe to visit, or whether it is a phishing or malware page. Example: "Is this URL safe to click: http://example.com/offer?" → URL_SCAN_VERDICT. Not: "Is example.com's SSL certificate valid?" (certificate details only) → SSL_VERIFICATION_CERT. Not: a file hash → MALWARE_DETECTION_HASH.

Contribute truth sources and question pairs · adapter on `URL_SCAN`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=URL_SCAN_VERDICT) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+URL_SCAN_VERDICT)

**`VIDEO_VERIFICATION`** — judgment family · tier network · H2 missions: —

#### `VIDEO_VERIFICATION_GENERAL`

judgment · asks `video_url` · answers `verdict`, `confidence`, `evidence`, `summary`

Query references an actual video file or URL and asks to verify its authenticity, origin, or whether it has been edited/deepfaked. The mere word 'video' in an unrelated question does not qualify — requires a real attached video. Example: "Here's a video URL: [link]. Can you verify its origin and whether it's been edited?" → VIDEO_VERIFICATION_GENERAL. Not: "What's the best video editing software?" (mentions 'video' but no actual video referenced to verify) → CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL.

Contribute question pairs · adapter on `VIDEO_VERIFICATION`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=VIDEO_VERIFICATION_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+VIDEO_VERIFICATION_GENERAL)

**`WALLET_BALANCE_CHECK`** — judgment family · tier network · H2 missions: —

#### `WALLET_BALANCE_CHECK_GENERAL`

deterministic · asks `address`, `chain`, `token` · answers `address`, `chain`, `balance`, `token_symbol`, `as_of`

Query names a specific blockchain address or ENS name and asks for its current native-coin or token balance on a named chain. A question that merely mentions a wallet without asking what it holds does not qualify. Example: "What is the balance of vitalik.eth on ethereum?" or "How much ETH does 0x6872...de hold on ethereum?" → WALLET_BALANCE_CHECK_GENERAL. ('How much does address X hold' is a balance question about that one address, even though it uses the word 'hold.') Not: "How many holders does USDC have on ethereum?" (asks about the token's holder population, not one address's own holdings) → TOKEN_HOLDER_COUNT_GENERAL.

Contribute truth sources · no module (see above). [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WALLET_BALANCE_CHECK_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WALLET_BALANCE_CHECK_GENERAL)

**`WEATHER_CHECK`** — deterministic family · tier network · H2 missions: —

#### `WEATHER_CHECK_TEMPERATURE`

deterministic · asks `location` · answers `temperature_c`

Query names a specific, resolvable city and asks for the CURRENT air temperature there. Example: "What is the temperature in London right now?" → WEATHER_CHECK_TEMPERATURE. Not: a forecast for a future window (WEATHER_FORECAST_GENERAL). Not: a question with no resolvable location.

Contribute truth sources · comparator already live. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WEATHER_CHECK_TEMPERATURE) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WEATHER_CHECK_TEMPERATURE)

**`WEATHER_FORECAST`** — judgment family · tier network · H2 missions: —

#### `WEATHER_FORECAST_GENERAL`

judgment · asks `location`, `window_hours` · answers `location`, `when`, `temp_max_c`, `temp_min_c`, `precipitation_probability_pct`, `condition`

Query names a specific, resolvable location and asks for FUTURE weather conditions over a stated time window (e.g. 'next 24 hours'), not current conditions. Example: "What is the 24-hour weather forecast for Reykjavik, Iceland, including temperature, precipitation probability, and wind speed?" → WEATHER_FORECAST_GENERAL. Not: "Polygon fees felt high yesterday. What are they at now?" (no location, this is a blockchain network fee question, not weather) → GAS_PRICE_GENERAL. Not: "Will the US GPS glitch recur this year?" or "Will .name domain sales surge?" (no resolvable location, no weather content) → CHAT_COMPLETION_GENERAL or WEB_SEARCH_GENERAL. A 'yesterday vs now' or 'will X happen' sentence shape alone is NOT evidence of a weather question. The location and the atmospheric/fee/subject-matter content are what matter, not the tense.

Contribute question pairs · adapter on `WEATHER_FORECAST`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WEATHER_FORECAST_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WEATHER_FORECAST_GENERAL)

**`WEB_SEARCH`** — judgment family · tier network · H2 missions: —

#### `WEB_SEARCH_GENERAL`

judgment · asks `query` · answers `answer`, `sources`, `brief`

Query needs current, live, or externally-sourced information not reliably answerable from static/training knowledge — general 'what is the current price of Bitcoin' questions that need up-to-date grounding. Example: "What's the latest news on the Fed's interest rate decision?" → WEB_SEARCH_GENERAL. Not: "Explain what an interest rate is." (answerable from general knowledge, no live data needed) → CHAT_COMPLETION_GENERAL.

Contribute question pairs · adapter on `WEB_SEARCH`. [Add it on Anjoman](https://anjoman.ai/dashboard/eval?intent=WEB_SEARCH_GENERAL) · [open bounties](../../../issues?q=is%3Aissue+is%3Aopen+WEB_SEARCH_GENERAL)

## Names the network does not serve

These are in this catalogue and in the mission map, but the node serves no Intent
under them. Some are a different spelling of a name the network does use. Renaming
or dropping one is a protocol-team decision, so they are listed, not guessed at.

| Name | Tier | H2 missions |
|---|---|---|
| `CRYPTO_PRICE_LOOKUP` | existing | Asset Management |
| `FACT_CHECKING` | existing | Legal, Conflict Intelligence, Consumer Platform |
| `GAS_PRICE_ESTIMATION` | existing | — |
| `INTENT_CLASSIFICATION` | existing | — |
| `SSL_CERTIFICATE_VERIFY` | existing | — |
| `STOCK_PRICE_QUOTE` | existing | Asset Management |
| `TOXICITY_MODERATION` | existing | — |
| `URL_CONTENT_EXTRACTION` | existing | Personal Agent |
| `WEATHER_CURRENT` | existing | — |
| `WEB_SEARCH_QUERY` | existing | Institutional Markets, Legal, Conflict Intelligence, Commodities, Personal Agent, Model Economy |
