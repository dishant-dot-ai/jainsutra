#!/usr/bin/env python3
"""
Remove transliterated Sanskrit/Prakrit terms from Samaysaar chapter body text.
Format: English (transliterated) for important terms; plain English for common ones.
Preserves sutra-sanskrit paragraphs (the original Prakrit verses).
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

BASE = Path('/Users/thefounder/Projects/active/JainSutra/scripture/Samaysaar')

# ─── REPLACEMENT TABLE ────────────────────────────────────────────────────────
# Order matters: longer/more specific phrases FIRST to avoid partial matches.
# Format: (old_text, new_text)  — case-sensitive; variants added for caps/lowercase.
# Sutra-sanskrit paragraphs are SKIPPED entirely.

REPLACEMENTS = [
    # ── COMPOUND PHRASES (longest first) ─────────────────────────────────────
    ("cetā-draṣṭā-jñātā",          "conscious one, seer, and knower (cetā-draṣṭā-jñātā)"),
    ("jñātā-draṣṭā-cetā",          "knower, seer, and conscious one (jñātā-draṣṭā-cetā)"),
    ("jñātā-draṣṭā",               "knower-seer (jñātā-draṣṭā)"),
    ("draṣṭā-jñātā",               "seer-knower (draṣṭā-jñātā)"),
    ("rāga-dveṣa-moha",            "attachment, aversion, and delusion (rāga-dveṣa-moha)"),
    ("Rāga-Dveṣa-Moha",            "Attachment, Aversion, and Delusion"),
    ("rāga-dveṣa",                 "attachment and aversion (rāga-dveṣa)"),
    ("prajñā-chedana",             "wisdom-cutting (prajñā-chedana)"),
    ("Prajñā-Chedana",             "Wisdom-Cutting (prajñā-chedana)"),
    ("karma-vimokṣaṇa",            "karma-liberation (karma-vimokṣaṇa)"),
    ("karma-pariṇāmas",            "karmic transformations"),
    ("karma-pariṇāma",             "karmic transformation (karma-pariṇāma)"),
    ("karma-bandha",               "karma-bondage (karma-bandha)"),
    ("karma-kāya",                 "karma-body"),
    ("karma-udaya",                "karma-rising (karma-udaya)"),
    ("ātma-ārādhana",              "self-worship (ātma-ārādhana)"),
    ("ātma-sākṣātkāra",            "self-realization (ātma-sākṣātkāra)"),
    ("ātma-jñāna",                 "self-knowledge (ātma-jñāna)"),
    ("ātma-svabhāva",              "soul's own nature (ātma-svabhāva)"),
    ("bhāva-āsrava",               "inner karmic influx (bhāva-āsrava)"),
    ("kartā-bhāva",                "doer-belief (kartā-bhāva)"),
    ("Kartā-Bhāva",                "Doer-Belief (kartā-bhāva)"),
    ("jñāna-bhāva",                "knowledge-state (jñāna-bhāva)"),
    ("Jñāna-Bhāva",                "Knowledge-State (jñāna-bhāva)"),
    ("jñāyaka-bhāva",              "knowing state (jñāyaka-bhāva)"),
    ("Jñāyaka-Bhāva",              "Knowing State (jñāyaka-bhāva)"),
    ("karma-bhāva",                "karmic state (karma-bhāva)"),
    ("niścaya-naya",               "ultimate standpoint (niścaya-naya)"),
    ("niścaya-cāritra",            "ultimate right-conduct (niścaya-cāritra)"),
    ("vyavahāra-naya",             "conventional standpoint (vyavahāra-naya)"),
    ("samyag-dṛṣṭi",               "right-seeing soul (samyag-dṛṣṭi)"),
    ("Samyag-Dṛṣṭi",               "Right-Seeing Soul (samyag-dṛṣṭi)"),
    ("samyag-darśana",             "right vision (samyag-darśana)"),
    ("Samyag-Darśana",             "Right Vision (samyag-darśana)"),
    ("para-ātmavādin",             "one who misidentifies the self (para-ātmavādin)"),
    ("para-ātmavādins",            "those who misidentify the self (para-ātmavādins)"),
    ("niścayadaḥ",                 "from the ultimate standpoint (niścayadaḥ)"),
    ("viṣa-kumbha",                "poison-pot (viṣa-kumbha)"),
    ("Viṣa-Kumbha",                "Poison-Pot (viṣa-kumbha)"),
    ("amṛta-kumbha",               "nectar-pot (amṛta-kumbha)"),
    ("Amṛta-Kumbha",               "Nectar-Pot (amṛta-kumbha)"),
    ("apratikramaṇa",              "non-return (apratikramaṇa)"),
    ("Apratikramaṇa",              "Non-Return (apratikramaṇa)"),
    ("pratikramaṇa",               "return from transgression (pratikramaṇa)"),
    ("Pratikramaṇa",               "Return from Transgression (pratikramaṇa)"),
    ("pratisaraṇa",                "reflection (pratisaraṇa)"),
    ("bheda-vijñāna",              "discriminative knowledge (bheda-vijñāna)"),
    ("Bheda-Vijñāna",              "Discriminative Knowledge (bheda-vijñāna)"),
    ("para-dravya",                "external substance (para-dravya)"),
    ("Para-Dravya",                "External Substance (para-dravya)"),
    ("ananya-pariṇāma",            "non-separate transformation (ananya-pariṇāma)"),
    ("jñāna-jñeya-jñātṛ",          "knowledge, knowable, and knower (jñāna-jñeya-jñātṛ)"),
    ("upāya-upeya",                "means and goal (upāya-upeya)"),
    ("jñānamātra",                 "pure knowledge alone (jñānamātra)"),
    ("rāga-bhāva",                 "attachment-state (rāga-bhāva)"),
    ("sneha-bhāva",                "oiliness-attachment (sneha-bhāva)"),
    ("Sneha-Bhāva",                "Oiliness-Attachment (sneha-bhāva)"),
    ("mithyā-adhyavasāya",         "false mental resolution (mithyā-adhyavasāya)"),
    ("mithyā-adhyavasāyas",        "false mental resolutions (mithyā-adhyavasāyas)"),
    ("mithyā-dṛṣṭi",               "wrong-seeing soul (mithyā-dṛṣṭi)"),
    ("apagata-rādha",              "departed from self-abidance (apagata-rādha)"),
    ("sāparādha",                  "transgressing soul (sāparādha)"),
    ("Sāparādha",                  "Transgressing Soul"),
    ("nirāparādha",                "innocent soul (nirāparādha)"),
    ("Nirāparādha",                "Innocent Soul (nirāparādha)"),
    ("aparādhin",                  "guilty one (aparādhin)"),
    ("nirabhaya",                  "fearless (nirabhaya)"),
    ("svalakṣaṇas",                "own characteristics (svalakṣaṇas)"),
    ("svalakṣaṇa",                 "own characteristic (svalakṣaṇa)"),
    ("anekāntatva",                "many-sidedness (anekāntatva)"),
    ("syādvāda",                   "conditional predication (syādvāda)"),
    ("viyoga-buddhi",              "detachment-understanding (viyoga-buddhi)"),
    ("caitanya-camatkāra",         "wonder of consciousness (caitanya-camatkāra)"),
    ("amogha-jñāna",               "unfailing knowledge (amogha-jñāna)"),
    ("bāla-tapa",                  "foolish austerity (bāla-tapa)"),
    ("Bāla-Tapa",                  "Foolish Austerity"),
    ("bāla-vrata",                 "childish vow (bāla-vrata)"),
    ("Bāla-Vrata",                 "Childish Vow"),
    ("ratnatraya",                 "Three Jewels (ratnatraya)"),
    ("Ratnatraya",                 "Three Jewels (ratnatraya)"),
    ("puṇya-karma",                "merit-karma"),
    ("puṇya",                      "merit (puṇya)"),
    ("Puṇya",                      "Merit"),
    ("rajo-bandha",                "dust-bondage analogy (rajo-bandha)"),

    # ── SINGLE TECHNICAL TERMS ────────────────────────────────────────────────
    # Knower / Knowledge cluster
    ("Jñānī",      "the knower (jñānī)"),
    ("jñānī",      "the knower (jñānī)"),
    ("Ajñānī",     "the ignorant (ajñānī)"),
    ("ajñānī",     "the ignorant (ajñānī)"),
    ("Jñāna",      "knowledge (jñāna)"),
    ("jñāna",      "knowledge (jñāna)"),
    ("Jñātā",      "the knower (jñātā)"),
    ("jñātā",      "the knower (jñātā)"),
    ("jñātṛtva",   "knower-nature (jñātṛtva)"),
    ("Jñātṛtva",   "Knower-Nature (jñātṛtva)"),
    ("Draṣṭā",     "the seer (draṣṭā)"),
    ("draṣṭā",     "the seer (draṣṭā)"),
    ("Cetā",       "the conscious one (cetā)"),
    ("cetā",       "the conscious one (cetā)"),
    ("Ajñāna",     "ignorance (ajñāna)"),
    ("ajñāna",     "ignorance (ajñāna)"),
    ("Budha",      "the wise one (budha)"),

    # Soul / Self cluster
    ("Ātmā",       "soul (ātmā)"),
    ("ātmā",       "soul (ātmā)"),
    ("Ātma",       "self"),
    ("ātma",       "self"),
    ("Śuddha",     "pure (śuddha)"),
    ("śuddha",     "pure (śuddha)"),
    ("Śuddhatā",   "purity (śuddhatā)"),
    ("śuddhatā",   "purity (śuddhatā)"),
    ("Jīva",       "soul (jīva)"),
    ("jīva",       "soul (jīva)"),
    ("Ajīva",      "non-soul (ajīva)"),
    ("ajīva",      "non-soul (ajīva)"),

    # Attachment / passion cluster
    ("Rāga",       "attachment (rāga)"),
    ("rāga",       "attachment (rāga)"),
    ("Rāgī",       "the attached (rāgī)"),
    ("rāgī",       "the attached (rāgī)"),
    ("Rāgādi",     "attachment and passions (rāgādi)"),
    ("rāgādi",     "attachment and passions (rāgādi)"),
    ("Dveṣa",      "aversion (dveṣa)"),
    ("dveṣa",      "aversion (dveṣa)"),
    ("Moha",       "delusion (moha)"),
    ("moha",       "delusion (moha)"),
    ("Virāga",     "dispassion (virāga)"),
    ("virāga",     "dispassion (virāga)"),
    ("Virāgī",     "the dispassionate (virāgī)"),
    ("virāgī",     "the dispassionate (virāgī)"),
    ("Sneha",      "oiliness-attachment (sneha)"),
    ("sneha",      "oiliness-attachment (sneha)"),

    # Liberation / bondage cluster
    ("Moksha",     "liberation (moksha)"),
    ("moksha",     "liberation (moksha)"),
    ("Mokṣa",      "liberation (mokṣa)"),
    ("mokṣa",      "liberation (mokṣa)"),
    ("Mukti",      "liberation (mukti)"),
    ("mukti",      "liberation (mukti)"),
    ("Nirvāṇa",    "final liberation (nirvāṇa)"),
    ("nirvāṇa",    "final liberation (nirvāṇa)"),
    ("Bandha",     "bondage (bandha)"),
    ("bandha",     "bondage (bandha)"),
    ("Nirjarā",    "karma-shedding (nirjarā)"),
    ("nirjarā",    "karma-shedding (nirjarā)"),
    ("Āsrava",     "karmic influx (āsrava)"),
    ("āsrava",     "karmic influx (āsrava)"),
    ("Samvara",    "karmic stoppage (samvara)"),
    ("samvara",    "karmic stoppage (samvara)"),

    # Standpoint cluster
    ("Niścaya",    "ultimate standpoint (niścaya)"),
    ("niścaya",    "ultimate standpoint (niścaya)"),
    ("Vyavahāra",  "conventional standpoint (vyavahāra)"),
    ("vyavahāra",  "conventional standpoint (vyavahāra)"),
    ("Paramārtha", "ultimate truth (paramārtha)"),
    ("paramārtha", "ultimate truth (paramārtha)"),

    # Doer / action cluster
    ("Kartā",      "doer (kartā)"),
    ("kartā",      "doer (kartā)"),
    ("Akartā",     "non-doer (akartā)"),
    ("akartā",     "non-doer (akartā)"),
    ("Mamakāra",   "possessive sense (mamakāra)"),
    ("mamakāra",   "possessive sense (mamakāra)"),
    ("Cintana",    "contemplation (cintana)"),
    ("cintana",    "contemplation (cintana)"),
    ("Chedana",    "cutting (chedana)"),
    ("chedana",    "cutting (chedana)"),
    ("Chinditvā",  "having cut (chinditvā)"),
    ("chinditvā",  "having cut (chinditvā)"),
    ("Vikalpas",   "mental constructs (vikalpas)"),
    ("vikalpas",   "mental constructs (vikalpas)"),

    # Matter / substance cluster
    ("Pudgala",    "matter (pudgala)"),
    ("pudgala",    "matter (pudgala)"),
    ("Dravya",     "substance (dravya)"),
    ("dravya",     "substance (dravya)"),
    ("Dravyas",    "substances (dravyas)"),
    ("dravyas",    "substances (dravyas)"),
    ("Paramāṇu",   "atom (paramāṇu)"),
    ("paramāṇu",   "atom (paramāṇu)"),
    ("Jaḍatā",     "inertness (jaḍatā)"),
    ("jaḍatā",     "inertness (jaḍatā)"),

    # Karma technical terms
    ("Prakṛti",    "karmic-type (prakṛti)"),
    ("prakṛti",    "karmic-type (prakṛti)"),
    ("Pradeśa",    "karmic-quantum (pradeśa)"),
    ("pradeśa",    "karmic-quantum (pradeśa)"),
    ("Sthiti",     "karmic-duration (sthiti)"),
    ("sthiti",     "karmic-duration (sthiti)"),
    ("Anubhāga",   "fruition-intensity (anubhāga)"),
    ("anubhāga",   "fruition-intensity (anubhāga)"),
    ("Udaya",      "karmic rising (udaya)"),
    ("udaya",      "karmic rising (udaya)"),
    ("Nokamma",    "physical-karma body"),
    ("nokamma",    "physical-karma body"),

    # Transformation / state cluster
    ("Pariṇāmas",  "transformations (pariṇāmas)"),
    ("pariṇāmas",  "transformations (pariṇāmas)"),
    ("Pariṇāma",   "transformation (pariṇāma)"),
    ("pariṇāma",   "transformation (pariṇāma)"),
    ("Svabhāva",   "own nature (svabhāva)"),
    ("svabhāva",   "own nature (svabhāva)"),
    ("Bhāvas",     "inner states (bhāvas)"),
    ("bhāvas",     "inner states (bhāvas)"),
    ("Bhāva",      "inner state (bhāva)"),
    ("bhāva",      "inner state (bhāva)"),
    ("Upayoga",    "conscious knowing (upayoga)"),
    ("upayoga",    "conscious knowing (upayoga)"),
    ("Caitanya",   "consciousness (caitanya)"),
    ("caitanya",   "consciousness (caitanya)"),

    # Wisdom / knowledge cluster
    ("Prajñā",     "wisdom (prajñā)"),
    ("prajñā",     "wisdom (prajñā)"),
    ("Viveka",     "discrimination (viveka)"),
    ("viveka",     "discrimination (viveka)"),
    ("Śaktis",     "powers (śaktis)"),
    ("śaktis",     "powers (śaktis)"),

    # Wrong belief / error cluster
    ("Mithyātva",      "wrong belief (mithyātva)"),
    ("mithyātva",      "wrong belief (mithyātva)"),
    ("Mithyā",         "false (mithyā)"),
    ("mithyā",         "false (mithyā)"),
    ("Adhyavasāna",    "passionate determination (adhyavasāna)"),
    ("adhyavasāna",    "passionate determination (adhyavasāna)"),
    ("Adhyavasāyas",   "mental resolutions (adhyavasāyas)"),
    ("adhyavasāyas",   "mental resolutions (adhyavasāyas)"),

    # Practice cluster
    ("Pratyayas",  "auxiliary conditions (pratyayas)"),
    ("pratyayas",  "auxiliary conditions (pratyayas)"),
    ("Pratyaya",   "auxiliary condition (pratyaya)"),
    ("pratyaya",   "auxiliary condition (pratyaya)"),
    ("Parigraha",  "possession (parigraha)"),
    ("parigraha",  "possession (parigraha)"),
    ("Nindā",      "self-censure (nindā)"),
    ("nindā",      "self-censure (nindā)"),
    ("Garhā",      "confession (garhā)"),
    ("garhā",      "confession (garhā)"),
    ("Śuddhi",     "purification (śuddhi)"),
    ("śuddhi",     "purification (śuddhi)"),
    ("Ārādhana",   "self-abidance (ārādhana)"),
    ("ārādhana",   "self-abidance (ārādhana)"),
    ("Aparādha",   "transgression (aparādha)"),
    ("aparādha",   "transgression (aparādha)"),
    ("Sādhana",    "spiritual practice (sādhana)"),
    ("sādhana",    "spiritual practice (sādhana)"),
    ("Āvaśyaka",   "essential duty (āvaśyaka)"),
    ("āvaśyaka",   "essential duty (āvaśyaka)"),

    # Other technical terms
    ("Saṃsāra",    "cycle of existence (saṃsāra)"),
    ("saṃsāra",    "cycle of existence (saṃsāra)"),
    ("Nānātva",    "mutual distinctness (nānātva)"),
    ("nānātva",    "mutual distinctness (nānātva)"),
    ("Mamakāra",   "possessive sense (mamakāra)"),
    ("mamakāra",   "possessive sense (mamakāra)"),
    ("Kevali",     "omniscient one (kevali)"),
    ("kevali",     "omniscient one (kevali)"),
    ("Siddha",     "liberated soul (siddha)"),
    ("Ācarya",     "teacher (ācarya)"),
    ("ācarya",     "teacher (ācarya)"),
    ("Sarvena",    "completely (sarvena)"),
    ("sarvena",    "completely (sarvena)"),
    ("Kāla",       "time (kāla)"),
    ("kāla",       "time (kāla)"),
    ("Kalpas",     "modes (kalpas)"),
    ("kalpas",     "modes (kalpas)"),
]

# ── CONCEPT TAG REPLACEMENTS (simpler — just translate the label) ─────────────
CONCEPT_TAG_REPLACEMENTS = [
    ("Jñāna ≠ Moksha",              "Knowledge ≠ Liberation"),
    ("Tīvra-Manda",                  "Intense-Mild Gradient"),
    ("Karma-Smeara",                 "Karma-Smeared State"),
    ("Yoga ≠ Sufficient",            "External Practice ≠ Sufficient"),
    ("Chinditvā Required",           "Decisive Cutting Required"),
    ("Prakṛti-Pradeśa-Sthiti-Anubhāga", "Four Dimensions of Karma"),
    ("Śuddhatā",                     "Purity"),
    ("Cintana ≠ Chedana",            "Contemplation ≠ Cutting"),
    ("Chedana = Moksha",             "Cutting = Liberation"),
    ("Sarvena Mukti",                "Complete Liberation"),
    ("Decisive Prajñā",              "Decisive Wisdom"),
    ("Virāga",                       "Dispassion"),
    ("Svabhāva-Jñāna",               "Knowledge of Own Nature"),
    ("Karma-Vimokṣaṇa",              "Karma-Liberation"),
    ("Prajñā-Chedana",               "Wisdom-Cutting"),
    ("Svalakṣaṇa",                   "Own Characteristic"),
    ("Nānātva",                      "Mutual Distinctness"),
    ("Caitanya vs Jaḍatā",           "Consciousness vs Inertness"),
    ("Ontological Distinction",      "Ontological Distinction"),
    ("Bandha-Chhedana",              "Bondage-Cutting"),
    ("Ātma-Graha",                   "Self-Grasping"),
    ("Śuddha Ātmā",                  "Pure Soul"),
    ("Prajñā as Instrument",         "Wisdom as Instrument"),
    ("Svayam-Vedyatā",               "Self-Known Nature"),
    ("Ātma-Graha by Jñāna",          "Self-Grasping by Knowledge"),
    ("Cetā",                         "The Conscious One"),
    ("Niścaya-Recognition",          "Ultimate Recognition"),
    ("Para-Bhāva",                   "Other-State"),
    ("Draṣṭā",                       "The Seer"),
    ("Witness-Nature",               "Witness Nature"),
    ("Jñātā",                        "The Knower"),
    ("Jñātṛtva",                     "Knower-Nature"),
    ("Mamakāra",                     "Possessive Sense"),
    ("Budha (Wise One)",             "The Wise One"),
    ("Kartā-Bhāva",                  "Doer-Belief"),
    ("Sāparādha vs Nirāparādha",     "Guilty vs Innocent Soul"),
    ("Spiritual Fear as Symptom",    "Spiritual Fear as Symptom"),
    ("Ārādhana",                     "Self-Abidance"),
    ("Apagata-Rādha",                "Departed from Self-Abidance"),
    ("Constant Ātma-Abidance",       "Constant Self-Abidance"),
    ("Aparādhin",                    "The Guilty One"),
    ("Nirāparādha",                  "The Innocent One"),
    ("Pratikramaṇa",                 "Return from Transgression"),
    ("Nindā-Garhā",                  "Self-Censure and Confession"),
    ("Kartā-Bhāva = Poison",         "Doer-Belief = Poison"),
    ("Viṣa-Kumbha",                  "The Poison Pot"),
    ("Apratikramaṇa",                "Non-Return"),
    ("Amṛta-Kumbha",                 "The Nectar Pot"),
    ("Jñātā Abidance = Nectar",      "Knower-Abidance = Nectar"),
    ("No Kartā = No Transgressor",   "No Doer = No Transgressor"),
    ("Adhyavasāna",                  "Passionate Determination"),
    ("Upayoga",                      "Conscious Knowing"),
    ("Svabhāva",                     "Own Nature"),
    ("Rāga",                         "Attachment"),
    ("Rāgādi",                       "Attachment and Passions"),
    ("Nirjarā",                      "Karma-Shedding"),
    ("Āsrava",                       "Karmic Influx"),
    ("Pudgala",                      "Matter"),
    ("Pariṇāma",                     "Transformation"),
    ("Prajñā",                       "Wisdom"),
    ("Moksha",                       "Liberation"),
    ("Bandha",                       "Bondage"),
    ("Bhāva",                        "Inner State"),
    ("Bhāvas",                       "Inner States"),
    ("Mithyātva",                    "Wrong Belief"),
    ("Niścaya",                      "Ultimate Standpoint"),
    ("Vyavahāra",                    "Conventional Standpoint"),
    ("Samyag-Dṛṣṭi",                 "Right-Seeing Soul"),
    ("Samyag-Darśana",               "Right Vision"),
    ("Rāgī Bhāva",                   "Attachment-State"),
    ("Jñānī",                        "The Knower"),
    ("Ajñānī",                       "The Ignorant"),
    ("Jñāna",                        "Knowledge"),
    ("Ātmā",                         "Soul"),
    ("Dveṣa",                        "Aversion"),
    ("Moha",                         "Delusion"),
    ("Paramāṇu",                     "Atom"),
    ("Parigraha",                    "Possession"),
    ("Śuddha",                       "Pure"),
    ("Caitanya",                     "Consciousness"),
    ("Jaḍatā",                       "Inertness"),
    ("Pratyaya",                     "Auxiliary Condition"),
    ("Pratyayas",                    "Auxiliary Conditions"),
    ("Saṃsāra",                      "Cycle of Existence"),
    ("Paramārtha",                   "Ultimate Truth"),
    ("Virāgī",                       "The Dispassionate"),
    ("Sneha = Rāga",                 "Oiliness = Attachment"),
    ("Yoga ≠ Bandha Cause",          "External Practice ≠ Bondage Cause"),
    ("Niścaya Verdict",              "Ultimate Standpoint Verdict"),
    ("Karma-Udaya",                  "Karmic Rising"),
    ("Bhāva-Āsrava",                 "Inner Karmic Influx"),
    ("Jñāna as Antidote",            "Knowledge as Antidote"),
    ("Aparādha",                     "Transgression"),
    ("Mithyā-Adhyavasāyas",          "False Mental Resolutions"),
]


SKIP_CLASSES = {'sutra-sanskrit'}  # don't touch Prakrit verse paragraphs

def is_in_skip_element(tag):
    """Return True if tag is inside a sutra-sanskrit paragraph."""
    parent = tag.parent
    while parent:
        if isinstance(parent, Tag):
            cls = parent.get('class', [])
            if 'sutra-sanskrit' in cls:
                return True
            if parent.name in ('style', 'script'):
                return True
        parent = parent.parent
    return False


def apply_replacements_to_text(text, replacements):
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
    return text


def fix_double_parens(text):
    """
    If a replacement created e.g. "knowledge (jñāna) (jñāna)" or
    "the knower (jñānī) (jñānī)", collapse duplicates.
    Also collapse "liberation (moksha) (moksha)".
    """
    # Pattern: "word (term) (term)" → "word (term)"
    text = re.sub(r'\(([^)]+)\)\s*\(\1\)', r'(\1)', text)
    return text


def process_file(filepath):
    html = filepath.read_text(encoding='utf-8')

    # ── 1. Fix concept tags first (simple string replacement) ─────────────
    for old, new in CONCEPT_TAG_REPLACEMENTS:
        if old in html:
            # Only replace inside concept-tag spans
            html = html.replace(
                f'<span class="concept-tag">{old}</span>',
                f'<span class="concept-tag">{new}</span>'
            )

    # ── 2. Process body text via BeautifulSoup ────────────────────────────
    soup = BeautifulSoup(html, 'html.parser')

    for text_node in soup.find_all(string=True):
        if isinstance(text_node, Comment):
            continue
        if is_in_skip_element(text_node):
            continue

        original = str(text_node)
        modified = apply_replacements_to_text(original, REPLACEMENTS)
        modified = fix_double_parens(modified)

        if modified != original:
            text_node.replace_with(NavigableString(modified))

    result = str(soup)
    filepath.write_text(result, encoding='utf-8')


if __name__ == '__main__':
    files = [f'samaysaar-ch{i}.html' for i in range(1, 12)] + ['samaysaar-poorvarang.html']
    for filename in files:
        fp = BASE / filename
        if not fp.exists():
            continue
        print(f'Processing {filename}...')
        process_file(fp)
        print(f'  ✓ Done')
    print('\nAll files updated.')
