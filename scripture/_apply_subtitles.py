#!/usr/bin/env python3
"""
Replace mirror-of-H1 H2 subtitles with real descriptive subtitles
for every Ramayana chapter (and any others that still mirror).
"""
from __future__ import annotations
import re
from pathlib import Path
from typing import Dict

ROOT = Path("/Users/thefounder/Projects/active/JainSutra/scripture")

# rel_path -> (old_h2_inner_text, new_h2_inner_text)
SUBTITLES: Dict[str, tuple] = {
    # Backstories
    "epics/ramayana/ramayana-backstory-1.html": (
        "Backstory 1 — Rakshasa Clan Origins",
        "Backstory 1 — How the lineage of so-called demons began — and why the Jain account inverts the Hindu telling",
    ),
    "epics/ramayana/ramayana-backstory-2.html": (
        "Backstory 2 — Chandanti & Abhayant's Past",
        "Backstory 2 — Two souls whose karmic ties stretch backward and forward across the Ramayana's most pivotal moments",
    ),
    "epics/ramayana/ramayana-backstory-3.html": (
        "Backstory 3 — Dasharatha & Ram's Past Lives",
        "Backstory 3 — The accumulated merit and unresolved karma that set the great king and his eldest son on their destined path",
    ),
    "epics/ramayana/ramayana-backstory-4.html": (
        "Backstory 4 — Ravana's Lineage Past",
        "Backstory 4 — The far-back lifetimes whose unfinished karma shaped the rise — and inevitable fall — of Lanka's king",
    ),
    "epics/ramayana/ramayana-backstory-5.html": (
        "Backstory 5 — Vanar Clan Origins",
        "Backstory 5 — Where the so-called monkey warriors really came from, and why their alliance with Ram was already written",
    ),
    "epics/ramayana/ramayana-backstory-6.html": (
        "Backstory 6 — Bharat & Suvarankanta's Past",
        "Backstory 6 — The earlier lives that bound Ram's brother to the queen who would one day exile him",
    ),
    "epics/ramayana/ramayana-backstory-7.html": (
        "Backstory 7 — The Elephant Bhuvnalankara's Past Lives",
        "Backstory 7 — The journey of a soul who became an elephant — and why this animal stood at the center of the kingdom's destiny",
    ),
    "epics/ramayana/ramayana-backstory-8.html": (
        "Backstory 8 — Principal Souls' Past",
        "Backstory 8 — The interlocking past lives of Ram, Vibhishana, Ravana, Kush, and Sita — laid out in one continuous arc",
    ),

    # Main chapters
    "epics/ramayana/ramayana-ch1.html": (
        "Chapter 1 — King Anjar's Moksha",
        "Chapter 1 — The king who chose liberation over comfort, setting the great lineage of Ayodhya in motion",
    ),
    "epics/ramayana/ramayana-ch2.html": (
        "Chapter 2 — Dasharatha's Household",
        "Chapter 2 — The three queens, the four sons, and the rare symmetry that defined the royal house before fate reshaped it",
    ),
    "epics/ramayana/ramayana-ch3.html": (
        "Chapter 3 — Narada's Devotion",
        "Chapter 3 — The wandering sage whose unwavering devotion makes him a constant witness across the unfolding story",
    ),
    "epics/ramayana/ramayana-ch4.html": (
        "Chapter 4 — Vibhishana Bound for Moksha",
        "Chapter 4 — Ravana's righteous brother — the rakshasa whose path to liberation was set long before the war",
    ),
    "epics/ramayana/ramayana-ch5.html": (
        "Chapter 5 — Kaikeyi's Swayamvar",
        "Chapter 5 — The contest where the queen-to-be chose her king — and the moment that planted the seed of a future exile",
    ),
    "epics/ramayana/ramayana-ch7.html": (
        "Chapter 7 — King Janaka's Concern",
        "Chapter 7 — The philosopher-king of Mithila weighing whose hands could be entrusted with his daughter's destiny",
    ),
    "epics/ramayana/ramayana-ch8.html": (
        "Chapter 8 — Janakpur's Bow",
        "Chapter 8 — The ancient weapon of Shiva and the test no ordinary man could pass",
    ),
    "epics/ramayana/ramayana-ch9.html": (
        "Chapter 9 — Sita's Swayamvar",
        "Chapter 9 — The day Ram lifted the bow no one else could — and chose his bride before the kingdoms of the earth",
    ),
    "epics/ramayana/ramayana-ch10.html": (
        "Chapter 10 — Sacred Trust of Character",
        "Chapter 10 — How a single act of integrity becomes the inheritance that outlives kingdoms",
    ),
    "epics/ramayana/ramayana-ch11.html": (
        "Chapter 11 — Dasharatha's Boon to Kaikeyi",
        "Chapter 11 — The promise made in gratitude that would, years later, exile a son and break a king",
    ),
    "epics/ramayana/ramayana-ch12.html": (
        "Chapter 12 — Ram & Sita's Vanvas",
        "Chapter 12 — The journey into the forest — when the rightful heir, his wife, and his brother chose dharma over the throne",
    ),
    "epics/ramayana/ramayana-ch13.html": (
        "Chapter 13 — Bharat's Coronation",
        "Chapter 13 — The reluctant king who refused his crown — and ruled in the name of an elder brother in exile",
    ),
    "epics/ramayana/ramayana-ch14.html": (
        "Chapter 14 — King's Grief in Ayodhya",
        "Chapter 14 — A father's collapse after the son he loved most is sent into the forest by the queen he could not refuse",
    ),
    "epics/ramayana/ramayana-ch15.html": (
        "Chapter 15 — Gokiran's Service",
        "Chapter 15 — The cowherd whose quiet service to wandering sages becomes the merit that bends the story's arc",
    ),
    "epics/ramayana/ramayana-ch16.html": (
        "Chapter 16 — Meeting Jatayu",
        "Chapter 16 — The encounter with the noble vulture-king whose final act of courage leaves the deepest mark on Ram",
    ),
    "epics/ramayana/ramayana-ch17.html": (
        "Chapter 17 — Sita's Abduction",
        "Chapter 17 — The moment Ravana takes what he was warned never to take — the act that brings the war to Lanka",
    ),
    "epics/ramayana/ramayana-ch19.html": (
        "Chapter 19 — Hanuman's Message to Sita",
        "Chapter 19 — The leap across the ocean and the messenger whose devotion alone could reach where armies could not",
    ),
}


def main():
    modified = 0
    for rel, (old, new) in SUBTITLES.items():
        f = ROOT / rel
        if not f.exists():
            print(f"  ! MISSING: {rel}"); continue
        src = f.read_text(encoding="utf-8")
        if old not in src:
            if new in src:
                print(f"  - {rel} (already updated)")
            else:
                print(f"  ? {rel} (old text not found)")
            continue
        new_src = src.replace(old, new, 1)
        f.write_text(new_src, encoding="utf-8")
        modified += 1
        print(f"  ✓ {rel}")
    print(f"\nUpdated {modified}/{len(SUBTITLES)} files.")


if __name__ == "__main__":
    main()
