#!/usr/bin/env python3
"""Translate transliterated Sanskrit terms in section dividers to English."""

from pathlib import Path

BASE = Path('/Users/thefounder/Projects/active/JainAwaken/scripture/Samaysaar')

# (old_span_content, new_span_content) — exact matches
REPLACEMENTS = [
    # ch3 (Adhikar 2)
    ("Part 1 · Gathas 69–74 · The Root of Bondage — Ajñāna",
     "Part 1 · Gathas 69–74 · The Root of Bondage — Ignorance"),
    ("Part 2 · Gathas 75–79 · The Jñānī as Akartā",
     "Part 2 · Gathas 75–79 · The Knower as Non-Doer"),
    ("Part 4 · Gathas 85–108 · The Self-Vikalpas and the Two Faces of Doership",
     "Part 4 · Gathas 85–108 · The Self-Constructs and the Two Faces of Doership"),
    ("Part 6 · Gathas 113–115 · Soul and Pratyaya Are Not Identical",
     "Part 6 · Gathas 113–115 · Soul and Auxiliary Conditions Are Not Identical"),
    ("Part 8 · Gathas 126–131 · Jñānī vs Ajñānī — The Nature of Bhāvas",
     "Part 8 · Gathas 126–131 · The Knower vs the Ignorant — The Nature of Inner States"),
    ("Part 10 · Gathas 137–142 · Distinctness of Soul and Pudgala Transformations",
     "Part 10 · Gathas 137–142 · Distinctness of Soul and Matter Transformations"),
    ("Part 11 · Gathas 143–144 · Beyond Both Standpoints — Samayasāra",
     "Part 11 · Gathas 143–144 · Beyond Both Standpoints — The Self-Essence"),

    # ch4 (Adhikar 3)
    ("Part 3 · Gatha 150 · Rāgī Binds, Virāgī is Freed",
     "Part 3 · Gatha 150 · The Attached Binds, The Detached is Freed"),
    ("Part 4 · Gatha 151 · Paramārtha — The Only Path to Nirvāṇa",
     "Part 4 · Gatha 151 · Ultimate Truth — The Only Path to Liberation"),
    ("Part 5 · Gathas 152–153 · Bāla-Tapa and Bāla-Vrata",
     "Part 5 · Gathas 152–153 · Foolish Austerity and Childish Vows"),
    ("Part 6 · Gatha 154 · The Error of Puṇya-Seeking",
     "Part 6 · Gatha 154 · The Error of Merit-Seeking"),
    ("Part 7 · Gatha 155 · Ratnatraya — The Real Moksha Path",
     "Part 7 · Gatha 155 · The Three Jewels — The Real Path to Liberation"),
    ("Part 8 · Gatha 156 · Jñāna as the Sole Cause of Moksha",
     "Part 8 · Gatha 156 · Knowledge as the Sole Cause of Liberation"),

    # ch5 (Adhikar 4)
    ("Part 1 · Gathas 164–165 · What Is Āsrava?",
     "Part 1 · Gathas 164–165 · What Is Karmic Influx?"),
    ("Part 2 · Gatha 166 · Jñānī Has No Āsrava-Bandha",
     "Part 2 · Gatha 166 · The Knower Has No Karmic Influx or Bondage"),
    ("Part 3 · Gatha 167 · The Law — Rāgī Bhāva Binds, Jñāna Bhāva Doesn't",
     "Part 3 · Gatha 167 · The Law — Attachment-State Binds, Knowledge-State Doesn't"),
    ("Part 4 · Gatha 168 · When Karma-Bhāva Falls, It Does Not Return",
     "Part 4 · Gatha 168 · When the Karmic State Falls, It Does Not Return"),
    ("Part 5 · Gatha 169 · Previously Bound Pratyayas — Like Clods of Earth",
     "Part 5 · Gatha 169 · Previously Bound Conditions — Like Clods of Earth"),
    ("Part 6 · Gathas 170–172 · The Paradox — Why Jñānī Is Abandha Despite Ongoing Karma",
     "Part 6 · Gathas 170–172 · The Paradox — Why the Knower Remains Unbounded Despite Ongoing Karma"),
    ("Part 7 · Gathas 173–176 · The Samyag-Dṛṣṭi and Previously Bound Karma",
     "Part 7 · Gathas 173–176 · The Right-Seeing Soul and Previously Bound Karma"),
    ("Part 8 · Gathas 177–178 · Rāga-Dveṣa-Moha Absent in Samyag-Dṛṣṭi",
     "Part 8 · Gathas 177–178 · Attachment, Aversion, and Delusion Absent in the Right-Seeing Soul"),
    ("Part 9 · Gathas 179–180 · The Digestive Fire — When the Jñānī Slips",
     "Part 9 · Gathas 179–180 · The Digestive Fire — When the Knower Slips"),

    # ch6 (Adhikar 5)
    ("Part 1 · Gathas 181–182 · Bheda-Vijñāna: Consciousness Is Consciousness Alone",
     "Part 1 · Gathas 181–182 · Discriminative Knowledge: Consciousness Is Consciousness Alone"),
    ("Part 2 · Gatha 183 · When Bheda-Vijñāna Arises",
     "Part 2 · Gatha 183 · When Discriminative Knowledge Arises"),
    ("Part 3 · Gatha 184 · The Gold-Fire Analogy — Jñānitva Is Indestructible",
     "Part 3 · Gatha 184 · The Gold-Fire Analogy — The Knower's Nature Is Indestructible"),
    ("Part 4 · Gatha 185 · Jñānī vs. Ajñānī — The Fundamental Difference",
     "Part 4 · Gatha 185 · The Knower vs. The Ignorant — The Fundamental Difference"),
    ("Part 7 · Gatha 190 · The Four Causes of Āsrava",
     "Part 7 · Gatha 190 · The Four Causes of Karmic Influx"),

    # ch7 (Adhikar 6)
    ("Part 1 · G193–G194 · What Is Nirjarā?",
     "Part 1 · G193–G194 · What Is Karma-Shedding?"),
    ("Part 4 · G198–G200 · I Am Jñāyaka-Bhāva — Rāga Is Not My Svabhāva",
     "Part 4 · G198–G200 · I Am the Knowing State — Attachment Is Not My Own Nature"),
    ("Part 5 · G201–G202 · Even a Paramāṇu of Rāgādi = Self-Ignorance",
     "Part 5 · G201–G202 · Even an Atom of Attachment = Self-Ignorance"),
    ("Part 6 · G203–G206 · Grasp the Stable Single Jñāna-Bhāva",
     "Part 6 · G203–G206 · Grasp the Stable Single Knowledge-State"),
    ("Part 7 · G207–G209 · The Self's Only Parigraha Is the Self",
     "Part 7 · G207–G209 · The Self's Only Possession Is the Self"),
    ("Part 8 · G210–G214 · Jñānī as Knower, Not Possessor",
     "Part 8 · G210–G214 · The Knower as Knower, Not Possessor"),
    ("Part 9 · G215–G216 · Viyoga-Buddhi — Detachment at All Three Times",
     "Part 9 · G215–G216 · Detachment-Understanding — At All Three Times"),
    ("Part 10 · G217–G219 · Gold and Iron — Svabhāva Determines Stainability",
     "Part 10 · G217–G219 · Gold and Iron — Own Nature Determines Stainability"),
    ("Part 14 · G229–G236 · Eight Qualities of Samyag-Darśana",
     "Part 14 · G229–G236 · Eight Qualities of Right Vision"),

    # ch8 (Adhikar 7)
    ("Part 1 · G237–G241 · The Oil-Smeared Man: Rāga Is the Cause",
     "Part 1 · G237–G241 · The Oil-Smeared Man: Attachment Is the Cause"),
    ("Part 2 · G242–G246 · The Man Without Oil: Samyag-Dṛṣṭi Does Not Bind",
     "Part 2 · G242–G246 · The Man Without Oil: Right Vision Does Not Bind"),
    ("Part 3 · G247–G258 · Three Mithyā-Adhyavasāyas: I Kill, I Give Life, I Make Happy",
     "Part 3 · G247–G258 · Three False Mental Resolutions: I Kill, I Give Life, I Make Happy"),
    ("Part 4 · G259–G262 · Adhyavasāna Alone Is Bandha — Niścaya Summary",
     "Part 4 · G259–G262 · Passionate Determination Alone Is Bondage — Ultimate Standpoint Summary"),
    ("Part 5 · G263–G265 · The Vastu Is Not the Cause",
     "Part 5 · G263–G265 · The Object Is Not the Cause"),
    ("Part 6 · G266–G267 · Mūḍha-Mati Is Purposeless",
     "Part 6 · G266–G267 · The Deluded Mind Is Purposeless"),
    ("Part 7 · G268–G272 · Soul Makes All Bhāvas; Adhyavasāna Defined",
     "Part 7 · G268–G272 · Soul Makes All Inner States; Passionate Determination Defined"),
    ("Part 8 · G273–G277 · Abhavya, Vyavahāra, and Niścaya Descriptions",
     "Part 8 · G273–G277 · Non-Liberatable Soul, Conventional, and Ultimate Standpoint Descriptions"),
    ("Part 9 · G278–G287 · Crystal Analogy, Jñānī Akāraka, Adhaḥkarma",
     "Part 9 · G278–G287 · Crystal Analogy, The Knower as Non-Doer, Lower Karma"),

    # ch9 (Adhikar 8)
    ("Part 2 · G293–G295 · Virāga + Prajñā-Chedana = Moksha",
     "Part 2 · G293–G295 · Dispassion + Wisdom-Cutting = Liberation"),
    ("Part 3 · G296–G300 · How Ātmā Is Grasped: I Am Cetā · Draṣṭā · Jñātā",
     "Part 3 · G296–G300 · How the Soul Is Grasped: I Am the Conscious One · Seer · Knower"),
    ("Part 4 · G301–G305 · The Criminal and the Innocent: Sāparādha and Nirāparādha Soul",
     "Part 4 · G301–G305 · The Criminal and the Innocent: Guilty Soul and Innocent Soul"),
    ("Part 5 · G306–G307 · Viṣa-Kumbha and Amṛta-Kumbha",
     "Part 5 · G306–G307 · The Poison Pot and the Nectar Pot"),

    # ch10 (Adhikar 9)
    ("Part 1 · G308–G315 · Ananya-Pariṇāma: Soul and Its Modifications Are Non-Separate",
     "Part 1 · G308–G315 · Non-Separate Transformation: Soul and Its Modifications Are One"),
    ("Part 2 · G316–G323 · Jñānī Does Not Experience; Only Knows",
     "Part 2 · G316–G323 · The Knower Does Not Experience; Only Knows"),
    ("Part 3 · G324–G348 · Para-Dravya Is Not Mine; The Four-Way Mithyātva Logic",
     "Part 3 · G324–G348 · External Substance Is Not Mine; The Four-Way Wrong-Belief Logic"),
    ("Part 4 · G349–G365 · The Śilpī and Seṭikā Analogies",
     "Part 4 · G349–G365 · The Craftsman and Merchant Analogies"),
    ("Part 5 · G366–G382 · Jñāna Outside Para-Dravya; Rāga Is Own Pariṇāma",
     "Part 5 · G366–G382 · Knowledge Outside External Substance; Attachment Is Own Transformation"),
    ("Part 6 · G383–G389 · Niścaya-Cāritra: The Three Kalpas",
     "Part 6 · G383–G389 · Ultimate Conduct: The Three Modes"),
    ("Part 7 · G390–G403 · Jñāna Is Distinct from All Dravyas; The Summit",
     "Part 7 · G390–G403 · Knowledge Is Distinct from All Substances; The Summit"),
    ("Part 8 · G405–G415 · Jñāna Has No Body; Liṅga Is Not Mokṣa-Mārga",
     "Part 8 · G405–G415 · Knowledge Has No Body; External Symbol Is Not the Path to Liberation"),

    # ch11 (Adhikar 10)
    ("Section 1 — The Jñānamātra Declaration",
     "Section 1 — The Pure-Knowledge-Alone Declaration"),
    ("Section 2 — The 47 Śaktis: Ātmā Lacks Nothing",
     "Section 2 — The 47 Powers: The Soul Lacks Nothing"),
    ("Section 3 — Syādvāda: The 14 Bhaṅgas of Jñāna (Kalaśas 247–263)",
     "Section 3 — Conditional Predication: The 14 Propositions of Knowledge (Verses 247–263)"),
    ("Section 4 — Upāya-Upeya: Ātmā as Path and Goal (Kalaśas 266–268)",
     "Section 4 — Means and Goal: The Soul as Path and Goal (Verses 266–268)"),
    ("Section 5 — Jñāna–Jñeya–Jñātṛ Are One Vastu (Kalaśa 271)",
     "Section 5 — Knowledge–Knowable–Knower Are One Substance (Verse 271)"),
    ("Section 6 — The Meca/Ameca Dialectic: Anekāntatva of Ātmā (Kalaśas 272–274)",
     "Section 6 — The Pure/Impure Dialectic: Many-Sidedness of the Soul (Verses 272–274)"),
    ("Section 7 — Victory of Caitanya-Camatkāra (Kalaśa 275)",
     "Section 7 — Victory of the Wonder of Consciousness (Verse 275)"),
    ("Section 8 — Amṛtacandra's Blessing and the Final Colophon (Kalaśas 276–278)",
     "Section 8 — Amṛtacandra's Blessing and the Final Colophon (Verses 276–278)"),
]

files = [f'samaysaar-ch{i}.html' for i in range(2, 12)]

total_changed = 0
for filename in files:
    fp = BASE / filename
    if not fp.exists():
        continue
    html = fp.read_text(encoding='utf-8')
    changed = 0
    for old, new in REPLACEMENTS:
        if old in html:
            html = html.replace(old, new)
            changed += 1
    if changed:
        fp.write_text(html, encoding='utf-8')
        print(f'{filename}: {changed} replacements')
        total_changed += changed

print(f'\nTotal: {total_changed} section dividers updated.')
