#!/usr/bin/env python3
"""Expand combined Adhikar 2 gatha cards into individual verse cards for samaysaar-ch3.html."""

from pathlib import Path

BASE = Path('/Users/thefounder/Projects/active/JainAwaken/scripture/Samaysaar')
FILE = BASE / 'samaysaar-ch3.html'
ADHIKAR = 2

def card(n, *, sk=None, tr, c1=None, c2=None, simple, tags):
    label = f'{ADHIKAR}.{n}'
    parts = []
    if sk:
        parts.append(f'<p class="sutra-sanskrit font-headline">{sk}</p>')
    parts.append(f'<p class="text-lg font-semibold text-on-surface leading-relaxed">{tr}</p>')
    if c1:
        parts.append(f'<p class="text-base text-on-surface-variant leading-relaxed">{c1}</p>')
    if c2:
        parts.append(f'<p class="text-base text-on-surface-variant leading-relaxed">{c2}</p>')
    parts.append(f'<p class="simple-explanation"><b>The simple version:</b> {simple}</p>')
    tag_html = ''.join(f'<span class="concept-tag">{t}</span>' for t in tags)
    parts.append(f'<div class="concept-tags">{tag_html}</div>')
    inner = '\n'.join(parts)
    return (f'<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="sutra-{n}">\n'
            f'<div class="flex items-start gap-6">\n'
            f'<span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{label}</span>\n'
            f'<div class="space-y-4 flex-1">\n'
            f'{inner}\n'
            f'</div>\n'
            f'</div>\n'
            f'</article>')

def sdiv(text):
    return f'<div class="section-divider"><span>{text}</span></div>'

def intro(text):
    return f'<p class="text-on-surface-variant text-base mb-8 max-w-3xl">{text}</p>'

# ── NEW GATHA SECTION (replaces from G76-79 grouped through G144) ─────────────

CARDS = []

# ── PART 2: G75–79 ────────────────────────────────────────────────────────────
# G75 already correct in HTML; we start from G76

CARDS.append(card(76,
    tr='The jñānī, knowing many kinds of pudgala-karma, does not transform into it (na pariṇamate) — does not become what it knows.',
    c1='The first of the three precise non-doings elaborated in G76–79. "Na pariṇamate" — the soul does not transform INTO karma. The jñānī\'s upayoga can be fully directed toward knowing karma — all its varieties, qualities, effects — yet there is no corresponding transformation of the jñānī\'s own being into karma-states. Think of the difference between a physician who studies a disease and a patient who contracts it. The jñānī studies karma without contracting it.',
    simple='Knowing karma fully — the jñānī does not become it. Knowing and becoming are completely separate.',
    tags=['Non-Transformation', 'Jñānī', 'Upayoga', 'Na Pariṇamate']))

CARDS.append(card(77,
    tr='Even knowing the soul\'s own many transformations (svaparyāya), the jñānī does not arise in the modes of other substances.',
    c1='The second non-doing. Even when knowing turns inward — toward the soul\'s own transformations, its rāgas and dveshas — the jñānī does not lose center. Knowing the inner states is different from being captured by them. The knowing remains as knowing, not collapsing into the state it observes. This is the subtlest non-doing: maintaining the seat of awareness even while observing one\'s own movements.',
    simple='Even knowing its own inner transformations — the jñānī stays as knower, not as what it knows.',
    tags=['Svaparyāya', 'Self-Observation', 'Jñānī', 'Para-Dravya']))

CARDS.append(card(78,
    tr='Knowing the infinite varieties of pudgala-karma fruit, the jñānī does not transform in them.',
    c1='The third non-doing. The jñānī witnesses the fruits of karma — pain, pleasure, the entire range of experience — knowing them as pudgala\'s transformations meeting the soul\'s awareness. This knowing produces no corresponding inner transformation. Experience happens; identification does not. The distinction between the witness of an experience and the one who is overwhelmed by it.',
    simple='Knowing all of karma\'s fruits — the jñānī remains untransformed by them.',
    tags=['Karma Fruits', 'Jñānī-Witness', 'Non-Identification']))

CARDS.append(card(79,
    sk='ण वि परिणमदि ण गिण्हदि उप्पज्जदि ण परदव्वपज्जाए।<br/>पोग्गलदव्वं पि तहा परिणमदि सएहिं भावेहिं।।७९।।',
    tr='Similarly, pudgala-dravya also transforms only by its own bhavas — it does not transform in the modes of the soul (para-dravya).',
    c1='G79 closes Part 2 by extending the same principle to pudgala. Just as the jñānī-soul does not transform into pudgala\'s modes — pudgala also does not transform into the soul\'s modes. The principle is symmetrical: <strong class="text-on-surface">each substance transforms only through its own svabhāva.</strong> This is the doctrine of svabhāva-pariṇāma (own-nature transformation) — one of the most foundational principles in Jain ontology.',
    c2='The revolutionary implication: no substance can actually do anything to another substance at the level of substance itself. They can serve as instrumental causes (nimittas) — conditions that occasion transformation. But the transformation happens from within, not from without. This demolishes the naive view that karma "does things" to the soul.',
    simple='Pudgala transforms by its own nature — not by invading the soul. And the soul transforms by its own nature — not by being pushed by pudgala.',
    tags=['Svabhāva-Pariṇāma', 'Para-Dravya', 'Mutual Non-Invasion']))

# ── PART 3: G80–84 ────────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 3 · Gathas 80–84 · Mutual Instrumental Causation'))
CARDS.append(intro('Gathas 80–84 present the doctrine of nimitta-naimittika — the most precise answer Jainism gives to the question of how soul and karma are related without the soul being karma\'s agent.'))

CARDS.append(card(80,
    sk='जीवपरिणामहेदुं कम्मत्तं पोग्गला परिणमंति।<br/>पोग्गलकम्मिणिमित्तं तहेव जीवो वि परिणमदि।।८०।।',
    tr='Pudgalas transform into karma-form due to the soul\'s transformation as cause; the soul also transforms due to pudgala-karma as instrumental cause.',
    c1='G80 states the doctrine of nimitta-naimittika (instrumental-instrumentalized) causation that underlies the entire Adhikar. Neither the soul nor pudgala acts on the other directly. The soul\'s transformation (its rāga, dvesha, moha) is <strong class="text-on-surface">nimitta</strong> — the occasion — for pudgalas to transform into karma-form. Karma\'s rise (udaya) is nimitta for the soul\'s transformation. Each is occasion for the other\'s transformation, while each transforms only through its own svabhāva.',
    c2='The Atmakhyati uses the crystal analogy: when a crystal is placed near a red flower, it appears red — but the redness does not actually enter the crystal. The crystal transforms through its own transparency, using the flower as nimitta. Remove the flower, the crystal is again pure. Soul and karma work exactly this way.',
    simple='Soul and karma mutually condition each other — but neither forces the other to transform. Each transforms by its own nature, using the other as occasion.',
    tags=['Nimitta-Naimittika', 'Instrumental Causation', 'Crystal Analogy']))

CARDS.append(card(81,
    sk='ण वि कुव्वदि कम्मगुणे जीवो कम्मं तहेव जीवगुणे।<br/>अण्णोण्णणिमित्तेण दु परिणामं जाण दोण्हं पि।।८१।।',
    tr='The soul does not produce karma\'s qualities; karma does not produce the soul\'s qualities. Know the transformation of both through mutual instrumental causation only.',
    c1='G81 sharpens G80 to its core principle. Production of qualities is strictly self-contained within each substance. The soul produces soul-qualities (consciousness, knowing, joy or suffering). Karma produces karma-qualities (the specific karmic conditions and their effects). Neither creates the other\'s qualities.',
    c2='What exists between them is nimitta-naimittika — occasion and occasioned. This is the Jain middle path between fatalism (karma determines who you are) and naive voluntarism (you act independently of conditions). You are never independent of conditions. But conditions never determine you absolutely. You transform yourself; conditions are occasion.',
    simple='The soul doesn\'t make karma\'s qualities; karma doesn\'t make the soul\'s qualities. They condition each other — but each produces only its own.',
    tags=['Mutual Non-Production', 'Nimitta-Naimittika', 'Substance Integrity']))

CARDS.append(card(82,
    sk='एदेण कारणेण दु कत्ता आदा सएण भावेण।<br/>पोग्गलकम्मकदाणं ण दु कत्ता सव्वभावाणं।।८२।।',
    tr='For this reason, the soul is kartā (doer) by its own bhāva — but is NOT the kartā of all bhavas produced by pudgala-karma.',
    c1='The soul\'s kartā-status is not denied altogether. It IS kartā — of its own inner states. When it generates rāga, it is kartā of rāga. When it generates dvesha, it is kartā of dvesha. These inner states are within its legitimate kartā-ship.',
    c2='What the soul is NOT kartā of: the bhavas produced by pudgala-karma — jñānāvaraṇa (knowledge-obscuring karma), darśanāvaraṇa (perception-obscuring), etc. These are pudgala\'s own transformations, with the soul as nimitta but not as material cause. You are responsible for your inner states. You are not responsible for what karma does of its own accord.',
    simple='The soul is the doer of its own inner bhavas. It is not the doer of everything karma produces.',
    tags=['Kartā-Limitation', 'Svabhāva-Kartā', 'Responsibility']))

CARDS.append(card(83,
    sk='णिच्छयणयस्स एवं आदा अप्पाणमेव हि करेदि।<br/>वेदयदि पुणो तं चेव जाण अत्ता दु अत्ताणं।।८३।।',
    tr='From the niśchaya (ultimate) standpoint: the soul does only itself and experiences only itself. Know this — the soul (does) the soul.',
    c1='G83 ascends to the ultimate level. Seen from there, the soul\'s doing and experiencing are completely self-contained. It does its own bhavas. It experiences its own bhavas. Nothing external is actually done or experienced — only the soul\'s own transformation is real from this standpoint.',
    c2='The phrase <strong class="text-on-surface">"ātmā tu ātmānam"</strong> (the soul does the soul) is one of the most celebrated in Jain metaphysics: the soul is simultaneously the doer, the deed, and the done-to. Even in bondage, what the soul is truly experiencing is not karma — but itself in a certain state. Karma is the occasion; the experience is the soul\'s own transformation.',
    simple='From the ultimate standpoint: the soul does only itself, and experiences only itself. Nothing external is actually inside it.',
    tags=['Niśchaya-Naya', 'Ātmā tu Ātmānam', 'Self-Contained']))

CARDS.append(card(84,
    sk='ववहारस्स दु आदा पोग्गलकम्मं करेदि णेयिवहं।<br/>तं चेव पुणो वेयइ पोग्गलकम्मं अणेयिवहं।।८४।।',
    tr='From the vyavahāra (conventional) standpoint, the soul does many kinds of pudgala-karma and experiences those many kinds of pudgala-karma.',
    c1='G84 balances G83. Conventionally, it is said that the soul does karma and experiences karma. This is vyavahāra — valid for practical purposes. The language of ethical instruction and spiritual guidance operates here.',
    c2='The two views do not contradict each other. The niśchaya view is used for pure self-inquiry — the language of liberation. The vyavahāra view is used in teachings about karma\'s binding and shedding — the language of practical ethics. A teacher must know when to use which. A student must learn not to confuse them.',
    simple='Conventionally: the soul does karma and experiences karma. Valid, useful — but not the final word.',
    tags=['Vyavahāra-Naya', 'Conventional Standpoint', 'Dual Standpoints']))

# ── PART 4: G85–108 ────────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 4 · Gathas 85–108 · The Self-Constructs and the Two Faces of Doership'))
CARDS.append(intro('The longest section of the Adhikar addresses the mechanism of ajñāna-based doership — specifically the self-vikalpas ("I am anger," "I am this") — and systematically establishes the precise boundary between the soul\'s legitimate kartā-ship and false karma-doership.'))

CARDS.append(card(85,
    sk='जदि पोग्गलकम्मिमिणं कुव्वदि तं चेव वेदयदि आदा।<br/>दोकिरियाविदिरित्तो पसज्जदे सो जिणावमदं।।८५।।',
    tr='If the soul both does pudgala-karma AND experiences it — a problem of double-action (dvikrīyā) arises, which is rejected by the Jinas.',
    c1='If the soul both makes karma AND experiences it as purely its own product, a logical contradiction arises: karma cannot be both the soul\'s activity AND the object of its experience — that would mean the same substance is both agent and patient in the same transaction at the same metaphysical level. The Jinas reject this "dvikrīyā" (double-action) error.',
    c2='The resolution: the soul does karma in the conventional sense (vyavahāra) — useful for teaching. At the ultimate level (niśchaya), the soul does only itself. The two statements operate at different levels. The dvikrīyā problem only arises when someone tries to apply both simultaneously at the same level.',
    simple='The soul can\'t simultaneously be the maker and experiencer of karma in the same metaphysical sense — that leads to contradiction rejected by the Jinas.',
    tags=['Dvikrīyā-Dosha', 'Niśchaya vs Vyavahāra', 'Logical Refutation']))

CARDS.append(card(86,
    sk='जम्हा दु अत्तभावं पोग्गलभावं च दो वि कुव्वंति।<br/>तेण दु मिच्छादिट्ठी दोकिरियावादिणो हुंति।।८६।।',
    tr='Those who claim the soul does both its own bhāva AND pudgala\'s bhāva are mithyādṛṣṭis — holders of wrong view.',
    c1='G86 names the philosophical error directly: holding that the soul simultaneously produces both its own inner states AND the outer material transformation of pudgala into karma is mithyātva (wrong view). This violates the principle of substance-specificity: each substance produces only its own modes.',
    c2='A soul that could produce pudgala\'s modes would be identical to pudgala — destroying the entire distinction between consciousness and matter that is the foundation of Jain metaphysics. This is not a minor doctrinal error. It is a misidentification of the soul\'s very nature.',
    simple='Believing the soul makes both its own states AND karma\'s material transformations — that is wrong view.',
    tags=['Mithyādṛṣṭi', 'Dvikrīyā-Vāda', 'Substance Distinction']))

CARDS.append(card(87,
    sk='मिच्छत्तं पुण दुविहं जीवमजीवं तहेव अण्णाणं।<br/>अविरदि जोगो मोहो कोहादीया इमे भावा।।८७।।',
    tr='Mithyātva is twofold — jīva-type and ajīva-type. Similarly ajñāna, avirata, yoga, moha, and the krodhādi — these are the bhavas (inner states).',
    c1='A foundational classification: every bondage-related bhāva has two aspects — a soul-side manifestation and a matter-side manifestation. What we call "mithyātva" (wrong belief) has both an inner dimension (the soul\'s wrong perception) and an outer dimension (the karma-species of mithyātva-karma). They are distinct, even though they co-arise and mutually condition each other.',
    c2='This distinction is critical: even moha (delusion) and krodhādi (passions) have a soul-side face (upayoga perverted by karma\'s rise) and a matter-side face (the karmic matter that rose). Knowing which is which — which is your transformation, which is karma\'s transformation — is what the Adhikar has been building toward.',
    simple='Mithyātva, ajñāna, passion — each has a soul-side face and a matter-side face. Knowing which is which is the beginning of clarity.',
    tags=['Jīva-Ajīva Distinction', 'Mithyātva-Types', 'Bhāva Classification']))

CARDS.append(card('88–90',
    tr='(G88–90) Upayoga, ajñāna, and avirati belong to the jīva-side; pudgala-karma, yoga-karma, and the material form of mithyātva belong to the ajīva-side. Upayoga — the soul\'s knowing-mode — is threefold and pure in nature. Whatever bhāva upayoga generates, upayoga is the kartā of that bhāva.',
    c1='G88–90 complete the classification begun in G87. The jīva-side bhavas are those belonging to consciousness: upayoga (knowing), ajñāna (wrong knowing), avirati (non-restraint as inner state). These are the soul\'s own transformations — not karma, but what the soul does in response to karma.',
    c2='The pivotal statement of G90: upayoga IS the kartā of the bhavas it generates. Pure upayoga generates pure bhavas. Upayoga perverted by moha generates ajñāna, mithyātva, avirati. The quality of consciousness determines the quality of everything that flows from it. This is why the entire Samaysaar is ultimately about transforming the quality of upayoga.',
    simple='Soul-side: upayoga, ajñāna, avirati. Matter-side: karma-types, yoga-matter. The soul\'s knowing-mode (upayoga) is the producer of the soul\'s own inner states.',
    tags=['Jīva-Side Bhavas', 'Ajīva-Side Bhavas', 'Upayoga as Kartā']))

CARDS.append(card(91,
    sk='जं कुणिदि भावमादा कत्ता सो होदि तस्स भावस्स।<br/>कम्मत्तं परिणमदे तम्हि सयं पोग्गलं दव्वं।।९१।।',
    tr='Whatever bhāva the soul does, it is the kartā of that bhāva; and in that bhāva, pudgala-dravya itself spontaneously (svayam) transforms into karma-form.',
    c1='G91 gives the complete causal sequence with precision: <strong class="text-on-surface">Soul generates bhāva → Soul is kartā of that bhāva → Pudgala spontaneously transforms into karma, occasioned by that bhāva.</strong> The word "svayam" (spontaneously, by itself) is the key: pudgala transforms by its own nature when the soul\'s bhāva provides the occasion. Not because the soul forces it.',
    c2='This single verse contains the entire Jain theory of karma-causation: the soul is responsible for its own inner states; pudgala is responsible for its own material transformations. Neither does the other\'s job. Neither is innocent of its own.',
    simple='Soul generates bhāva → Soul is its doer → Pudgala spontaneously transforms into karma in response. Each does its own part.',
    tags=['Complete Causal Sequence', 'Svayam', 'Karma Formation']))

CARDS.append(card(92,
    sk='परमप्पाणं कुव्वं अप्पाणं पि य परं किरंतो सो।<br/>अण्णाणमओ जीवो कम्माणं कारगो होदि।।९२।।',
    tr='Making the supreme self (paramātmā) into "other," and making the self into "other" — the ajñāna-filled soul becomes the kartā of karmas.',
    c1='The mechanism of ajñāna-based kartā-ship, described with surgical precision. Two distortions happen simultaneously in the ajñānī: (1) Making the supreme self (the pure soul) into "other" — treating your deepest nature as foreign, unknown. (2) Making "other" (body, passions, possessions) into "self" — identifying with what you are not.',
    c2='These two reversals together constitute ajñāna. And this ajñāna IS what makes the soul the kartā of karmas. Not any metaphysical fact about the soul\'s nature — just this reversal. Which means: <strong class="text-on-surface">reversing the reversal IS liberation.</strong>',
    simple='Mistake your true self as "not me" and mistake what is not you as "me" — you make karma. That double reversal is ajñāna itself.',
    tags=['Ajñāna-Kartā', 'Double Reversal', 'Paramātmā']))

CARDS.append(card(93,
    sk='परमप्पाणमकुव्वं अप्पाणं पि य परं अकुव्वंतो।<br/>सो णाणमओ जीवो कम्माणमकारगो होदि।।९३।।',
    tr='Not making the supreme self into "other," not making the self into "other" — the jñāna-filled soul is the akartā (non-doer) of karmas.',
    c1='G93 is the exact reversal of G92. The jñānī does the opposite of both distortions: knows the true self as self, knows the not-self as not-self. This dual recognition — knowing the self as self, knowing the not-self as not-self — constitutes jñāna. And this jñāna alone makes the soul akartā of karma.',
    c2='Not through any external ritual or practice of renunciation. Not through austerity or vow. Through <strong class="text-on-surface">knowing correctly.</strong> The akartā-ship is built entirely on right knowing. This is the revolutionary claim of the Samaysaar: liberation is not a future achievement — it is a present recognition.',
    simple='The jñānī knows the true self as self and the not-self as not-self. That knowing alone makes the soul non-doer of karma.',
    tags=['Jñāna-Akartā', 'Right Knowing', 'Non-Doership']))

CARDS.append(card(94,
    sk='तिविहो एसुवओगो अप्पियप्पं करेदि कोहोऽहं।<br/>कत्ता तस्सुवओगस्सं होदि सो अत्तभावस्स।।९४।।',
    tr='Threefold upayoga creates self-vikalpas like "I am anger (krodhaḥ aham)"; the kartā of that upayoga becomes kartā of that bhāva.',
    c1='"I am anger," "I am pride," "I am deceit" — these self-vikalpas (self-constructions) are the practical mechanism of ajñāna-based bondage. The upayoga, perverted by mithyātva, generates these false self-statements. And whoever identifies as kartā of that upayoga — whoever says "I am angry" and means it as their very identity — becomes the kartā of that bhāva and binds karma through it.',
    c2='This is one of the most psychologically penetrating verses in the Samaysaar. Modern psychology would call this the difference between having an emotion and being an emotion. The Samaysaar calls the latter vicarious kartā-ship — the karmic identification that binds. The difference is not in the emotion itself but in who you take yourself to be when it arises.',
    simple='When upayoga generates "I am anger" and you identify with it — you become the doer of that bhāva. The emotion doesn\'t bind; the identity does.',
    tags=['Krodho\'ham', 'Self-Vikalpa', 'Upayoga-Identity']))

CARDS.append(card('95–97',
    tr='(G95–97) Even "I am dharma" or "I am righteous" — if not arising from genuine self-knowledge — is a bondage-producing self-vikalpa. G96: The foolish one makes other substances into self and through ignorance makes self into other. G97: For this reason the soul is called kartā by niśchaya-knowers; one who truly knows this is freed from all kartā-ship.',
    c1='G95 extends the self-vikalpa argument beyond obvious passions: even positive self-identifications — "I am righteous," "I am a renunciant," "I am spiritual" — if they arise from ego-attachment rather than pure self-knowledge, generate bondage. The form of the self-construction is less important than its source.',
    c2='G97\'s irony is exquisite: it is precisely because the soul IS the true kartā (of its own bhavas) that the knower of this — who understands what kartā-ship actually means — is freed from false kartā-ship. Understanding what you truly are responsible for (your inner bhavas) liberates you from the illusion of being responsible for everything else.',
    simple='Even "I am righteous" can bind if it\'s an ego-identity. True knowing of kartā-ship — what you\'re genuinely responsible for — liberates from false kartā-ship.',
    tags=['Dharma-Vikalpa', 'Ego-Identity', 'True Kartā-Ship']))

CARDS.append(card('98–100',
    tr='(G98–100) Soul doesn\'t make pots, cloth, or chariots — yoga (activity) and upayoga (knowing) are the producers in that conventional sense. If the soul were to do other substances, it would necessarily become tanmaya (identical with them); since it is not tanmaya, it is not their kartā.',
    c1='G98 raises the conventional examples of kartā-ship: a potter makes a pot, a weaver makes cloth. If the soul is called "karma\'s maker," what does that mean? G99 provides the logical refutation: if the soul actually produced karma-matter (a pudgala substance), it would have to become identical (tanmaya) with it — but it doesn\'t become pudgala. Therefore it is not the material maker of karma.',
    c2='G100 gives the precise definition: the soul does not make pot, cloth, or other substances as their material cause. Yoga (the activity of mind-speech-body) and upayoga (the knowing-mode) are the producers — in that limited conventional sense. The soul\'s role is initiating the occasion, not producing the matter.',
    simple='The soul can\'t make karma-matter without becoming identical to it — which it doesn\'t. So the soul is not karma\'s material maker.',
    tags=['Tanmaya Refutation', 'Karma-Maker Error', 'Yoga as Producer']))

CARDS.append(card('101–104',
    tr='(G101–104) The soul does not create karma\'s dravya (matter-substance) and its guṇas (qualities) — it is not their material maker. Karma\'s material qualities arise purely from pudgala\'s own transformative nature.',
    c1='G101–104 extend the argument from individual karma-types to the general principle. The soul does not produce karma\'s dravya (the material of karma) nor karma\'s guṇas (its specific qualities — the four parameters of prakṛti, pradeśa, sthiti, anubhāga). All of these belong entirely to pudgala\'s domain.',
    c2='The soul is the occasion (nimitta) for karma — not the material agent. Just as a lamp provides the occasion for shadows to form but does not produce the shadow-matter itself, the soul provides the occasion for pudgala to transform into karma without being karma\'s material cause.',
    simple='Karma\'s matter and qualities are all pudgala\'s own production. The soul provides the occasion; it doesn\'t make the material.',
    tags=['Karma-Dravya', 'Karma-Guṇas', 'Nimitta Only']))

CARDS.append(card('105–108',
    tr='(G105–108) "Karma done by the soul" — this is said only by upachāra (conventional metaphor), not ultimately. When warriors fight, people say "the king did the battle" — similarly by vyavahāra, "jñānāvaraṇādi was done by the soul." Just as a king is conventionally called "producer of subjects\' faults and virtues," the soul by vyavahāra is called "producer of dravya-qualities."',
    c1='G105 names the linguistic device: upachāra — conventional metaphor. "Karma done by the soul" is a useful shorthand, not a metaphysical claim. Like "the king fought the battle" — which is conventionally meaningful even though the king sat in his throne while soldiers did the actual fighting.',
    c2='G108\'s analogy closes the section elegantly: the king is called "producer of his subjects\' faults and virtues" not because he personally enacts each one, but because the kingdom operates in his context. Similarly the soul is called "producer of karma" not because it materially makes karma, but because karma arises in the context of the soul\'s bhāvas. Context ≠ causation.',
    simple='The soul\'s karma-doership is a conventional metaphor (upachāra), not ultimate fact. Each substance produces only its own transformations.',
    tags=['Upachāra', 'King Analogy', 'Vyavahāra Convention']))

# ── PART 5: G109–112 ─────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 5 · Gathas 109–112 · The Four Causes of Bondage'))
CARDS.append(intro('The Adhikar now gives the formal theory of bondage-causes — four general pratyayas and their thirteen specific varieties across the guṇasthānas — and establishes that these causes are themselves achetana (insentient), clarifying where exactly the soul\'s responsibility lies.'))

CARDS.append(card(109,
    sk='सामण्णपच्चया खलु चउरो भण्णंति बंधकत्तारो।<br/>मिच्छत्तं अविरमणं कसायजोगा य बोद्धव्वा।।१०९।।',
    tr='The four general causes (sāmānya-pratyaya) declared as the doers-of-bondage are: mithyātva (wrong belief), non-restraint (aviramana), kasāya (passions), and yoga (activity) — these are to be understood.',
    c1='The four general causes of bondage are foundational Jain karma-theory. Mithyātva (wrong belief) — the root distortion of perception. Aviramana (non-restraint) — continuing in actions that harm. Kasāya (the four passions: anger, pride, deceit, greed) — the emotional forces that intensify karma. Yoga (activity of mind, speech, body) — the mechanism through which karmic particles are attracted.',
    c2='"Sāmānya-pratyaya" means these are the general categories — like chapter headings. Each then has specific sub-varieties in the next gatha (thirteen varieties corresponding to the guṇasthānas).',
    simple='Four things cause karma to bind: wrong belief, non-restraint, passions, and activity. These are the roots of bondage.',
    tags=['Four Pratyayas', 'Mithyātva', 'Kasāya', 'Yoga', 'Aviramana']))

CARDS.append(card(110,
    sk='तेसिं पुणो वि य इमो भणिदो भेदो दु तेरसवियप्पो।<br/>मिच्छादिट्ठीआदी जाव सजोगिस्स चरमंतं।।११०।।',
    tr='Their further distinction is described as thirteen varieties — from the mithyādṛṣṭi (guṇasthāna 1) onwards through to the final moment of the sa-yogi Kevalī (guṇasthāna 13).',
    c1='The thirteen guṇasthānas (stages of spiritual development) correspond to the varying admixtures of the four causes of bondage. At mithyādṛṣṭi (guṇasthāna 1), all four causes operate at full force. As the soul progresses upward, one by one these causes are attenuated — first wrong belief falls away, then non-restraint reduces, then passions weaken.',
    c2='At the sa-yogi Kevalī stage (guṇasthāna 13), only the last trace remains — yoga (the subtle activity inherent in embodied existence). Even the omniscient Kevalī, until the final moment, binds trace karma through yoga alone. Only at the very last moment does yoga cease and complete liberation (moksha) is attained. Spiritual progress is thus measured by which bondage-causes are being progressively reduced.',
    simple='The thirteen spiritual stages map the progressive reduction of bondage-causes — from full wrong belief right through to the final moment before liberation.',
    tags=['Thirteen Guṇasthānas', 'Spiritual Progress', 'Sa-Yogi Kevalī']))

CARDS.append(card(111,
    sk='एदे अचेदणा खलु पोग्गलकम्मुदयसंभवा जम्हा।<br/>ते जदि करंति कम्मं ण वि तेसिं वेदगो आदा।।१११।।',
    tr='These four pratyayas are insentient (achetana) — they arise from the rise of pudgala-karma. If they alone do karma, the soul would not be their experiencer.',
    c1='A key philosophical argument. The four bondage-causes — mithyātva, avirati, kasāya, yoga — are not the soul\'s autonomous creations. They arise from the rise (udaya) of pudgala-karma. In that sense, they are achetana (insentient) — born from matter, not from the soul\'s pure consciousness.',
    c2='The argument follows: if these insentient pratyayas were the sole doers of karma, the soul would not experience the resulting karma. But the soul IS the experiencer of karma — that is undeniable. Therefore the soul\'s conscious engagement (upayoga) is part of what creates bondage. The insentient causes alone are not sufficient; the soul\'s conscious participation — even if only as occasion — is necessary for karma to bind.',
    simple='The four bondage-causes are themselves insentient — born from karma\'s rise. If they alone made karma, the soul wouldn\'t experience it. But it does — so the soul\'s conscious engagement is part of what creates bondage.',
    tags=['Achetana Pratyayas', 'Soul as Experiencer', 'Consciousness Required']))

CARDS.append(card(112,
    sk='गुणसंणिदा दु एदे कम्मं कुव्वंति पच्चया जम्हा।<br/>तम्हा जीवोऽकत्ता गुणा य कुव्वंति कम्माणि।।११२।।',
    tr='These pratyayas — as guṇas (the spiritual-stage attributes) — do karma; therefore the soul is akartā (non-doer), and the guṇas do the karmas.',
    c1='The guṇas here are the guṇasthāna-specific attributes — the specific forms that the four pratyayas take at each stage of spiritual development. From the niśchaya standpoint, the soul is akartā (non-doer) of karma; the guṇas — which are really the achetana pratyaya forces — are the actual karma-doers. The soul is their field, not their agent.',
    c2='This is the ultimate logical endpoint of G111\'s argument. The soul is not akartā in the sense of being inert or passive — it is very much alive, knowing, experiencing. But in terms of producing karma\'s material transformation — that belongs to the guṇas, the pratyayas, the achetana forces that operate through the soul\'s field. The soul is the occasion; not the efficient cause of karma-matter.',
    simple='The spiritual-stage attributes (guṇas) do karma — not the soul directly. The soul is non-doer in this technical but profound sense.',
    tags=['Guṇas as Karma-Doers', 'Niśchaya Akartā', 'Soul as Field']))

# ── PART 6: G113–115 ─────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 6 · Gathas 113–115 · Soul and Auxiliary Conditions Are Not Identical'))

CARDS.append(card(113,
    sk='जह जीवस्स अणण्णुवओगो कोहो वि तह जिद अणण्णो।<br/>जीवस्साजीवस्स य एवमणण्णत्तमावण्णं।।११३।।',
    tr='Just as upayoga is non-separate (ananya) from the soul — if krodha (anger) were also non-separate — then soul and ajīva would become non-separate, which is a philosophical error.',
    c1='Someone might argue: "Upayoga is the soul\'s own — it is not separate from it. And krodha is upayoga in a certain mode — so krodha is also the soul itself." G113 exposes the error in this reasoning: if krodha were truly ananya (non-separate) from the soul in the same way upayoga is, then the soul and ajīva (matter) would become non-different.',
    c2='This collapses the fundamental distinction between consciousness and matter — the very distinction that all of Jain philosophy, and especially Adhikar 2, is built upon. Upayoga is ananya to the soul because it is the soul\'s defining characteristic. Krodha is different: it arises from karma (an ajīva substance). The source determines the category.',
    simple='If anger were as inseparable from the soul as upayoga is — then soul and matter would be identical. That\'s the error.',
    tags=['Ananya-Upayoga', 'Krodha-Anya', 'Soul-Matter Distinction']))

CARDS.append(card(114,
    sk='एविमह जो दु जीवो सो चेव दु णियमदो तहाऽजीवो।<br/>अयमेयते दोसो पच्चयणोकम्मकम्माणं।।११४।।',
    tr='In that case, whatever is the soul would necessarily be ajīva too — and this error extends to pratyaya (conditions), nokamma (physical-karma body), and karma as well.',
    c1='G114 extends the reductio ad absurdum of G113. If the soul were identical to krodha (which arises from ajīva), then the soul would simply BE ajīva. And if that same logic is applied to all the other conditions and karma-types that interact with the soul — pratyaya, nokamma, karma — all of them would be the soul. The entire distinction between soul and not-soul would collapse.',
    simple='If the soul were identical to anger (which comes from matter), then the soul would be matter — and the error spreads to all karma, all conditions, the entire physical-karma body.',
    tags=['Reductio Ad Absurdum', 'Jīva-Ajīva', 'Error Propagation']))

CARDS.append(card(115,
    sk='अह दे अण्णो कोहो अण्णुवओगप्पगो हवइ चेदा।<br/>जह कोहो तह पच्चय कम्मं णोकम्ममिव अण्णं।।११५।।',
    tr='But if krodha is "other" (anya) — and the soul is of the nature of upayoga as "other" — then just as krodha is other, so too pratyaya, karma, and nokamma are all other (separate from the soul).',
    c1='The resolution arrives clean and clear. Krodha IS anya — genuinely other than the soul. The soul IS of the nature of upayoga — consciousness. These are categorically different. And this distinction cleanly extends to all of karma, nokamma (the physical-karma body), and pratyaya (conditions) — all of which are anya to the soul.',
    c2='The soul is consciousness. Everything else is other. Not as ascetic ideology — as precise metaphysics. The line is not drawn by renunciation but by recognition. Krodha arises from karma; karma is ajīva; therefore krodha, for all its seeming intimacy, is structurally other than the soul.',
    simple='Anger is other than the soul. The soul is consciousness. Therefore all of karma, pratyaya, and physical-karma body are other — cleanly, categorically other.',
    tags=['Krodha-Anya', 'Ontological Separation', 'Consciousness vs Matter']))

# ── PART 7: G116–125 ─────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 7 · Gathas 116–125 · Each Substance Transforms Itself'))
CARDS.append(intro('A long and philosophically dense section responding to the Sāṃkhya school\'s view that the soul is entirely non-transforming (aparinami). Kundakunda proves that BOTH soul and pudgala are pariṇāmi (transforming) substances — and that each transforms only through its own svabhāva (own nature).'))

CARDS.append(card(116,
    sk='जीवे ण सयं बद्धूं ण सयं परिणमिदे कम्मभावेण।<br/>जिद पोग्गलदव्विमणं अप्परिणामी तदा होइदु।।११६।।',
    tr='If the soul is not bound to karma by itself and does not transform by itself in karma-form — then pudgala-dravya would be proved to be non-transforming (aparinami) as well.',
    c1='G116 opens a long argument (G116–125) directed at the Sāṃkhya school\'s position that the purusa (soul) is entirely aparinami (non-transforming) — that all transformation belongs to prakriti (matter). The Jain position: BOTH soul and pudgala are pariṇāmi (transforming) substances.',
    c2='The argument\'s structure is a chain of dilemmas. If the soul doesn\'t transform by itself, then by parallel reasoning, pudgala wouldn\'t transform by itself either — and then no transformation anywhere could be explained. The entire existence of samsāra (with its bondage, karma, liberation) requires BOTH soul and pudgala to be pariṇāmi substances.',
    simple='If the soul doesn\'t transform itself, pudgala can\'t transform either — and the Sāṃkhya problem collapses everything.',
    tags=['Aparinami Refutation', 'Sāṃkhya Debate', 'Pariṇāmi Soul']))

CARDS.append(card('117–120',
    tr='(G117–120) G117: If karmic varganās don\'t transform into karma-form by themselves, samsāra is impossible or Sāṃkhya follows. G118: The soul causes pudgala to transform into karma — but if pudgala doesn\'t transform by itself, how could the soul cause it? G119: If pudgala transforms by itself into karma — then saying "the soul transforms karma" is false. G120: By necessity, pudgala transformed into karma-form IS karma; pudgala transformed into jñānāvaraṇa-form IS jñānāvaraṇa.',
    c1='G117–120 form a tight logical chain, each gatha eliminating another escape route for the opponent. The cumulative argument forces a single conclusion: pudgala transforms into karma BY ITS OWN NATURE. The soul\'s state is the occasion (nimitta) — not the efficient or material cause.',
    c2='G120\'s punchline: each substance is definitively what its transformation says it is. Pudgala transformed into jñānāvaraṇa (knowledge-obscuring) karma simply IS that karma — by its own transformation. The soul didn\'t make it. This is what "svabhāva-pariṇāma" means in its most concrete application.',
    simple='Pudgala transforms into karma by its own nature. The soul\'s state is the occasion, not the maker. Each substance IS what its own transformation makes it.',
    tags=['Svabhāva-Pariṇāma', 'Sāṃkhya Refutation', 'Karmic Varganās']))

CARDS.append(card('121–124',
    tr='(G121–124) The same argument applied to the soul\'s transformation in krodhādi (anger etc.). G121: If the soul doesn\'t transform by itself in krodhādi, it would be non-transforming. G122: If the soul doesn\'t self-transform in anger-states, samsāra is impossible or Sāṃkhya follows. G123: If pudgala-anger could transform the soul, pudgala-anger would have to be the material cause — but it can\'t transform what doesn\'t first self-transform. G124: If the soul transforms into anger by itself — then saying "anger transforms the soul" is false.',
    c1='G121–124 mirror the G117–120 argument but now apply it to the soul\'s side. The conclusion: the soul transforms itself into anger-states. Not because karma forces it. Because of its own transformative nature responding to karma as occasion.',
    c2='This is simultaneously a refutation of fatalism (karma didn\'t force you into anger; you transformed into it) and an establishment of responsibility (your anger is your own transformation — which means you can transform differently). The revolutionary implication runs in both directions.',
    simple='The soul transforms itself into anger — karma doesn\'t do it to the soul. Which means: the soul can also transform itself out of it.',
    tags=['Soul Self-Transforms', 'Krodhādi', 'Responsibility']))

CARDS.append(card(125,
    sk='कोहुवजुत्तो कोहो माणुवजुत्तो य माणमेवादा।<br/>माउवजुत्तो माया लोहुवजुत्तो हवदि लोहो।।१२५।।',
    tr='Soul engaged in krodha-upayoga IS krodha; engaged in māna-upayoga IS māna; engaged in māyā-upayoga IS māyā; engaged in lobha-upayoga IS lobha.',
    c1='The climax of the G116–125 argument. The soul IS what its upayoga is — at the moment of that engagement. Not as the soul\'s eternal nature — as its current transformation. The anger-karma is nimitta. The soul\'s own transformation IS the anger.',
    c2='This has profound implications: <strong class="text-on-surface">your anger is not what karma does to you — it is what you transform into when karma rises as occasion.</strong> And therefore it can change. By you. The path is not about removing karma — it is about changing the quality of upayoga. When upayoga stabilizes in jñāna-mode (knowing without identifying), the anger-transformation cannot arise even when anger-karma rises.',
    simple='Soul in anger-upayoga IS anger. Soul in pride-upayoga IS pride. What you engage with through knowing — you become.',
    tags=['Krodha-Upayoga', 'Soul\'s Transformation', 'Upayoga Determines']))

# ── PART 8: G126–131 ─────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 8 · Gathas 126–131 · The Knower vs the Ignorant — The Nature of Bhāvas'))

CARDS.append(card(126,
    sk='जं कुणिदे भावमादा कत्ता सो होदि तस्स कम्मस्स।<br/>णाणिस्स स णाणमओ अण्णाणमओ अणाणिस्स।।१२६।।',
    tr='Whatever bhāva the soul does, it is kartā of that karma. For the jñānī it is jñānamaya (knowledge-filled); for the ajñānī it is ajñānamaya (ignorance-filled).',
    c1='The same external action can be jñānamaya or ajñānamaya depending on the quality of consciousness from which it arises. This is not a moralistic judgment — it is a description of the actual nature of the act as produced by different qualities of upayoga. The jñānī\'s bhavas, arising from jñānamaya upayoga, are genuinely knowledge-filled. The ajñānī\'s bhavas, arising from ajñānamaya upayoga, are ignorance-filled — distorted by the fundamental reversal described in G92.',
    c2='The critical consequence: the jñānī\'s jñānamaya bhavas do not produce karma in the same way as the ajñānī\'s ajñānamaya bhavas. The inner quality of consciousness determines the karmic outcome — not the external act.',
    simple='The same action, done from jñāna, is jñānamaya. Done from ajñāna, it is ajñānamaya. The quality of consciousness transforms the nature of the deed.',
    tags=['Jñānamaya', 'Ajñānamaya', 'Quality of Consciousness']))

CARDS.append(card(127,
    sk='अण्णाणमओ भावो अणाणिणो कुणिदे तेण कम्माणि।<br/>णाणमओ णाणिस्स दु ण कुणिदे तम्हा दु कम्माणि।।१२७।।',
    tr='The ajñānī\'s bhāva is ajñānamaya — therefore it does karmas. The jñānī\'s bhāva is jñānamaya — therefore it does NOT do karmas.',
    c1='This is the core operational principle of the jñānī-ajñānī distinction: <strong class="text-on-surface">ajñānamaya doing = karma; jñānamaya doing = no karma.</strong> The jñānī\'s life may look similar to the ajñānī\'s externally — both breathe, eat, speak, move. But the jñānī\'s actions arise from jñānamaya upayoga and don\'t add to karma. The ajñānī\'s arise from ajñānamaya upayoga — they do.',
    c2='The Atmakhyati explains: the jñānī does not perform actions while treating rāga-dvesha as "mine" — as self-definition. Without that claiming, karma has no hook to attach to. The inner quality of consciousness is what determines the karmic outcome, not the external act. This is why external conformity to rules — without inner jñāna — cannot liberate.',
    simple='Ajñānamaya doing = karma. Jñānamaya doing = no karma. The outcome is determined by the quality of consciousness, not the external action.',
    tags=['Ajñāna Makes Karma', 'Jñāna No Karma', 'Key Principle']))

CARDS.append(card(128,
    sk='णाणमया भावाओ णाणमओ चेव जायदे भावो।<br/>जम्हा तम्हा णाणिस्स सव्वे भावा हु णाणमया।।१२८।।',
    tr='From jñānamaya bhāva, only jñānamaya bhāva arises; therefore all bhavas of the jñānī are truly jñānamaya.',
    c1='A profound statement about the self-reproducing nature of consciousness states. Jñāna generates jñāna. Once the jñānī\'s consciousness is established in jñānamaya bhāva, everything that arises from it — every thought, every perception, every response — is jñānamaya. Not because the jñānī is suppressing or controlling each impulse — but because <strong class="text-on-surface">the source is clean.</strong>',
    c2='The analogy given in G130: from gold come only gold-forms (earrings, bracelets). From iron come only iron-forms. The quality of the source material determines the quality of everything produced from it. Transform the source — and everything arising from it transforms.',
    simple='From knowing comes knowing. All of the jñānī\'s bhavas are jñānamaya — because they arise from jñānamaya consciousness.',
    tags=['Self-Reproducing Consciousness', 'Source Determines All', 'Jñāna Generates Jñāna']))

CARDS.append(card(129,
    sk='अण्णाणमया भावा अण्णाणो चेव जायदे भावो।<br/>जम्हा तम्हा भावा अण्णाणमया अणाणिस्स।।१२९।।',
    tr='From ajñānamaya bhavas, only ajñāna-bhāva arises; therefore all bhavas of the ajñānī are ajñānamaya.',
    c1='The mirror of G128. From ignorance, ignorance is reproduced. Every act of ajñāna generates more ajñāna. Every self-vikalpa deepens the groove of false identification. The ajñānī\'s entire inner life operates from a distorted source — and therefore everything arising from it perpetuates the distortion.',
    c2='This is both a warning and a revelation: the path of liberation is not about controlling individual bhavas one by one — it is about transforming the source. A single genuine recognition of the self-in-itself (samyak-darśana) shifts the source, and everything that arises from it begins to shift. Not by effort but by the changed quality of the source.',
    simple='From ignorance, ignorance is reproduced. All of the ajñānī\'s bhavas are ajñānamaya — generated from the same distorted source.',
    tags=['Ajñāna Generates Ajñāna', 'Source Transforms', 'Ajñānī']))

CARDS.append(card('130–131',
    tr='(G130–131) Just as from gold come only gold-forms (earrings, bracelets etc.); from iron come only iron-forms (bangles etc.) — similarly: the ajñānī\'s many bhavas are all ajñānamaya; the jñānī\'s bhavas are all jñānamaya.',
    c1='The substance analogy completes the principle. A goldsmith doesn\'t decide each earring will be golden — it\'s determined by the source material. Similarly, the jñānī doesn\'t control each bhāva individually to make it jñānamaya — it flows naturally from the jñānamaya source.',
    c2='The practical application: spiritual transformation is not a matter of managing individual thoughts and actions. It is a matter of transforming the source — the quality of the soul\'s upayoga. When the upayoga is firmly in jñāna-mode, all arising bhavas will reflect jñāna. This is the deepest argument for why self-knowledge — not behavioral reform alone — is the essential path.',
    simple='Like produces like: gold makes gold-forms, iron makes iron-forms. The jñānī\'s consciousness produces jñāna-bhavas; the ajñānī\'s produces ajñāna-bhavas.',
    tags=['Gold-Iron Analogy', 'Source Quality', 'Transformation']))

# ── PART 9: G132–136 ─────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 9 · Gathas 132–136 · The Four Rises and Their Nature'))

CARDS.append(card(132,
    sk='अण्णाणस्स स उदओ जा जीवाणं अतच्चउवलद्धी।<br/>मिच्छत्तस्स दु उदओ जीवस्स असद्दहाणतं।।१३२।।',
    tr='The rise (udaya) of ajñāna in jīvas is the non-attainment of true reality; the rise of mithyātva is non-faith in the soul.',
    c1='G132 begins the experiential description of the four bondage-causes from the inside. What does it feel like when ajñāna rises? The soul simply does not recognize reality as it is — it sees wrongly, interprets wrongly, misses what is actually present. Not active rejection — just absence of true seeing.',
    c2='What does it feel like when mithyātva rises? Not just passive non-seeing but active orientation away from truth — the soul turned in the wrong direction, rejecting or dismissing right understanding when it appears. Two distinct failures: missing truth (ajñāna) versus rejecting truth (mithyātva).',
    simple='Ajñāna\'s rise = missing truth. Mithyātva\'s rise = rejecting truth. Two different experiential flavors of the same fundamental problem.',
    tags=['Ajñāna-Udaya', 'Mithyātva-Udaya', 'Experiential Description']))

CARDS.append(card(133,
    sk='उदओ असंजमस्स दु जं जीवाणं हवेइ अविरमणं।<br/>जो दु कलुसोवओगो जीवाणं सो कसाउदओ।।१३३।।',
    tr='The rise of asaṃyama (non-restraint) is the concretely non-restraining behavior of jīvas; the impure (kaluśa) upayoga of jīvas is the rise of kasāya.',
    c1='The rise of asaṃyama manifests as concrete action: harming, speaking falsely, taking what is not given, sensory indulgence, storage and possessiveness. The non-restraint is visible and external.',
    c2='The rise of kasāya is entirely internal: the upayoga becomes kalusha — murky, defiled, clouded. The word "kalusha" is precisely chosen: it does not mean the upayoga is destroyed or absent — it means it is no longer clear. Like a muddy stream versus a clear one. Kasāya\'s rise is the muddying of the knowing-capacity itself.',
    simple='Non-restraint\'s rise = concrete harmful actions. Passion\'s rise = murky/clouded upayoga. One is visible externally; one is felt internally.',
    tags=['Asaṃyama-Udaya', 'Kasāya-Udaya', 'Kaluśa-Upayoga']))

CARDS.append(card(134,
    sk='तं जाण जोगउदयं जो जीवाणं तु चित्तुच्छाहो।<br/>सोहणमसोहणं वा कायव्वो विरदिभावो वा।।१३४।।',
    tr='Know that yoga-rise is the inner enthusiasm or initiative of jīvas — whether pure or impure — or even the state of viradibhāva (the initiation of renunciation).',
    c1='Yoga-rise is the soul\'s sheer inner initiative — its readiness to act. This is subtler than the other three rises. Pure yoga-rise is the energy behind constructive, even holy action. Impure yoga-rise is restlessness and agitation. Both are yoga.',
    c2='The remarkable inclusion: even viradibhāva (the impulse toward renunciation, the energy of spiritual practice itself) is a form of yoga-rise. This shows yoga is entirely neutral as a category — neither inherently binding nor liberating. What matters is the quality of consciousness directing it. Even the energy of renunciation, if not directed by jñāna, can produce karma.',
    simple='Yoga\'s rise is inner energy and initiative — pure, impure, or even the energy of renunciation. Yoga itself is neutral; what matters is the consciousness behind it.',
    tags=['Yoga-Udaya', 'Initiative', 'Viradibhāva', 'Yoga is Neutral']))

CARDS.append(card('135–136',
    tr='(G135–136) Among these instrumental causes, the kārmika-varganā-matter transforms in eight forms — jñānāvaraṇa, darśanāvaraṇa, etc. When that kārmika-varganā-matter is bound to the living soul, at that time the soul becomes instrumental cause for its transformations.',
    c1='G135–136 complete the four-rise picture by showing what happens materially when the four rises operate. The kārmika-varganā (karma-grade pudgala particles) adhere to the soul and transform into the eight types of karma — the material of bondage. But the causation is nimitta (instrumental), not upādāna (material).',
    c2='The soul is the nimitta — the occasion, the living field in which this transformation happens. Pudgala does the actual material transformation by its own svabhāva when the soul\'s bhāvas provide the occasion. Mithyātva-rise, karma\'s transformation into bondage-form, and the soul\'s own ajñānamaya transformation all happen simultaneously — each by its own nature, in mutual nimitta-naimittika relationship.',
    simple='When the four rises operate, karma-grade matter transforms into the eight karma-types in the soul\'s field. Soul is the occasion; pudgala does the material transformation.',
    tags=['Kārmika-Varganā', 'Eight Karma Types', 'Nimitta']))

# ── PART 10: G137–142 ────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 10 · Gathas 137–142 · Distinctness of Soul and Matter Transformations'))

CARDS.append(card(137,
    sk='जइ जीवेण सह चिय पोग्गलदव्वस्स कम्मपरिणामो।<br/>एवं पोग्गलजीवा हु दो वि कम्मत्तमावण्णा।।१३७।।',
    tr='If the karma-transformation of pudgala-dravya happens together WITH the soul — then both pudgala and the soul would become karma.',
    c1='G137 opens Part 10 with a crisp logical argument against the view that soul and pudgala jointly transform into karma. If they truly transformed together, both would be karma. But the soul does not become karma. Therefore they do not transform jointly.',
    c2='This is the argument from identity: co-transformation implies co-identity. If A and B jointly become C, then both A and B are C. Since the soul is manifestly not karma (it is consciousness, not matter), the soul and pudgala cannot jointly transform into karma. Each transforms by its own nature, separately.',
    simple='If soul and pudgala jointly became karma, both would be karma. Since only pudgala becomes karma, they transform separately.',
    tags=['Joint-Transformation Refuted', 'Soul ≠ Karma', 'Separate Transformation']))

CARDS.append(card(138,
    sk='एक्कस्स दु परिणामो पोग्गलदव्वस्स कम्मभावेण।<br/>ता जीवभावहेदूहिं विणा कम्मस्स परिणामो।।१३८।।',
    tr='Karma-transformation belongs to pudgala-dravya alone; therefore, the transformation of karma happens without the jīva-bhāva as its material cause.',
    c1='Pudgala transforms into karma by its own nature (svabhāva). The soul\'s bhāva is nimitta (occasion) — not upādāna kāraṇa (material cause). The material cause of karma is pudgala alone. This protects both the soul\'s integrity (it doesn\'t become karma) and pudgala\'s integrity (it transforms according to its own nature, not because the soul does something to it).',
    c2='The phrase "viṇā jīva-bhāva-hetūhiṃ" (without jīva-bhāva as cause) is precise: without the soul\'s bhāvas as MATERIAL cause. The soul\'s bhāvas are still the nimitta (occasion). But occasion is categorically different from material causation.',
    simple='Only pudgala becomes karma — and it does so by its own nature. The soul\'s state is the occasion, not the material cause.',
    tags=['Pudgala Alone Transforms', 'Upādāna vs Nimitta', 'Karma Causation']))

CARDS.append(card('139–140',
    tr='(G139–140) G139: If the soul and karma together had rāgādi (attachment-anger etc.) transformations — both would be rāgādi. But karma cannot be rāgī (attached). G140: Rāgādi transformation belongs to the soul alone; therefore the soul\'s rāgādi transformation happens without karma-rise as its material cause.',
    c1='G139–140 apply the G137–138 argument in the reverse direction — now to the soul\'s transformation in rāgādi. Just as only pudgala becomes karma (not the soul), only the soul becomes rāgī (attached). Karma cannot experience attachment. Karma is insentient; attachment requires consciousness.',
    c2='Therefore rāga is the soul\'s own transformation, with karma\'s rise as nimitta only. This is simultaneously a statement of <strong class="text-on-surface">non-determinism</strong> (karma can\'t force you into attachment — you transform yourself into it) and of <strong class="text-on-surface">responsibility</strong> (your attachment is categorically your own transformation, not something done to you).',
    simple='Only the soul becomes attached — karma can\'t feel attachment. The soul\'s rāga is its own transformation, with karma as occasion only.',
    tags=['Rāgādi as Soul-Transformation', 'Non-Determinism', 'Responsibility']))

CARDS.append(card(141,
    sk='जीवे कम्मं बद्धं पुट्ठं चेद ववहारणयभणिदं।<br/>सुद्धणयस्स दु जीवे अबद्धपुट्ठं हवदि कम्मं।।१४१।।',
    tr='That karma is "bound and touched" in the soul — this is the vyavahāra-naya\'s statement. From the śuddha-naya\'s perspective, karma is "unbound and untouched" in the soul.',
    c1='G141 presents two valid views without contradiction. <strong class="text-on-surface">Vyavahāra:</strong> Karma IS bound to the soul — this is the language of practical teaching about bondage, shedding karma, and the process of liberation. <strong class="text-on-surface">Śuddha-naya (pure standpoint):</strong> At the level of the soul\'s actual nature, karma never touches it. The soul is anādi-śuddha (pure from the beginningless).',
    c2='Both are true at their respective levels. Neither is false. The vyavahāra view is appropriate for ethical instruction and practical spiritual guidance. The śuddha-naya view is appropriate for pure self-inquiry. The error is applying one level\'s description to the other\'s domain.',
    simple='Conventionally: karma binds the soul. From the pure standpoint: karma never actually touches the soul. Both are true at their respective levels.',
    tags=['Vyavahāra', 'Śuddha-Naya', 'Karma Bound vs Unbound']))

CARDS.append(card(142,
    sk='कम्मं बद्धमबद्धं जीवे एवं तु जाण णयपक्खं।<br/>पक्खादिक्कंतो पुण भण्णिदे जो सो समयसारो।।१४२।।',
    tr='"Karma is bound in the soul" or "karma is not bound in the soul" — know these as naya-standpoints. But the one who is described as beyond all standpoints — THAT is the Samayasāra.',
    c1='G142 is the philosophical pivot of Adhikar 2 — and in a sense, of the entire Samaysaar. Both statements ("karma is bound" and "karma is not bound") are standpoints — useful lenses that capture partial truth. But the Samayasāra is what is beyond both. Not a third opinion. Not a superior standpoint. <strong class="text-on-surface">The direct experience of what the soul actually is, prior to any lens.</strong>',
    c2='"Samayasāra" means the essence of the soul\'s own time/nature — the pure self, directly known, without the mediation of any naya (standpoint). To reach it, one must transcend ALL naya-pakshas — not by rejecting them as useless (they are essential tools) but by not getting captured by any of them. The soul that rests in itself, beyond all standpoints, is the Samayasāra.',
    simple='"Karma binds" and "karma doesn\'t bind" — both are standpoints. The Samayasāra itself is beyond all standpoints.',
    tags=['Naya-Standpoints', 'Samayasāra Defined', 'Beyond Standpoints']))

# ── PART 11: G143–144 ────────────────────────────────────────────────────────

CARDS.append(sdiv('Part 11 · Gathas 143–144 · Beyond Both Standpoints — The Self-Essence'))
CARDS.append(intro('The final two gathas name the destination — and reveal that the destination is not a state to be achieved but a direct seeing of what the soul already is, when no standpoint mediates the seeing.'))

CARDS.append(card(143,
    sk='दोण्ह वि णयाण भणिदं जाणिदे णवरं तु समयपिडिबद्धो।<br/>ण दु णयपक्खं गिण्हिदे किंचि वि णयपक्खपरिहीणो।।१४३।।',
    tr='The one who is firmly bound to Samayasāra knows the statements of both nayas — but does not take any naya-standpoint; being free from all naya-standpoints.',
    c1='The samayapraribaddha (Samayasāra-bound soul) is not ignorant of the nayas — this is not anti-intellectualism. They know both the vyavahāra and śuddha-naya statements thoroughly. Understanding is complete. But understanding does not become attachment to a position. They move through both frameworks without being captured by either.',
    c2='The Atmakhyati compares this to a Kevalī: the omniscient being sees and knows everything — all standpoints, all perspectives simultaneously — but is not captured by any of them. The Kevalī abides in direct experience of reality, which no standpoint fully describes. The samyak-dṛṣṭi does the same at a more modest level: uses nayas as tools, isn\'t imprisoned by them.',
    simple='The Samayasāra-oriented soul knows both standpoints — but doesn\'t take sides with either. Tools, not cages.',
    tags=['Samayapraribaddha', 'Naya-Paksha-Rahita', 'Kevalī Analogy']))

CARDS.append(card(144,
    sk='सम्मदंसणणाणं एसो लहिदे ति णवरि ववदेसं।<br/>सव्वणयपक्खरहिदो भणिदो जो सो समयसारो।।१४४।।',
    tr='This alone obtains the designation "samyak-darśana and samyak-jñāna." The one described as free from all naya-standpoints — THAT is Samayasāra.',
    c1='The final gatha of Adhikar 2 is a revelation: samyak-darśana (right perception) and samyak-jñāna (right knowledge) are not two separate things acquired through separate practices. They are the same reality — the direct experience of the soul in its purity, beyond all standpoints.',
    c2='"Sarvnaya-paksha-rahito" — freed from all standpoints. Not a blank mind. A fully luminous, knowing consciousness that sees itself directly — without the mediation of even the most refined philosophical framework. The Samayasāra is not a book. Not a doctrine. It is <strong class="text-on-surface">the soul itself</strong> — as it truly is, when seen without any naya overlay. This is what all 76 gathas of Adhikar 2 have been pointing toward from the very first verse.',
    simple='Free from all standpoints — that alone obtains the names "right perception" and "right knowledge." That pure knowing IS Samayasāra.',
    tags=['Samyak-Darśana', 'Samyak-Jñāna', 'Sarvnaya-Paksha-Rahita', 'Samayasāra']))

# ── BUILD NEW HTML SECTION ───────────────────────────────────────────────────

NEW_SECTION = '\n\n'.join(CARDS)

# ── PATCH FILE ───────────────────────────────────────────────────────────────

html = FILE.read_text(encoding='utf-8')

# Markers: replace from "<!-- G75-79 grouped -->" through "<!-- Navigation to next/prev -->"
START_MARKER = '<!-- G75-79 grouped -->'
END_MARKER   = '<!-- Navigation to next/prev -->'

si = html.find(START_MARKER)
ei = html.find(END_MARKER)

if si == -1 or ei == -1:
    print(f'ERROR: markers not found (si={si}, ei={ei})')
    exit(1)

new_html = html[:si] + NEW_SECTION + '\n\n' + html[ei:]
FILE.write_text(new_html, encoding='utf-8')
print('Done. Wrote expanded ch3 with individual verse cards.')
print(f'  Replaced {ei - si} chars with {len(NEW_SECTION)} chars')
print(f'  Total cards/sections generated: {len(CARDS)}')
