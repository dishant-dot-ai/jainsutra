#!/usr/bin/env python3
"""Generate uttaradhyana-ch32.html — Pramādasthāna (Stations of Negligence)."""
import re, json
from pathlib import Path

BASE = Path('/Users/thefounder/Projects/active/JainAwaken/scripture/Aagama/uttaradhyana')

# ── Sutra data ────────────────────────────────────────────────────────────────
# Each: (id, num_label, prakrit, translation, commentary, simple, tags)
SUTRAS = [
    # ── Section 1-3: Eternal Happiness & Solitary Wandering ─────────────────
    ('sutra-1','32.1',
     'अच्छंतकालस्स समूलगस्स, सव्वस्स दुक्खस्स उ जो पमोक्खो ।\nतं भासओ मे पडिपुण्णचित्ता, सुणेह एगंतिहयं हियत्थं ॥३२.१॥',
     'O noble beings! Listen with complete, concentrated attention to this singular beneficial teaching I am about to declare — the means for complete liberation from all suffering along with its roots, which has continued since beginningless time.',
     'Lord Mahāvīra opens this chapter by calling the aspirant to full attention. The teaching he is about to give is not partial advice — it addresses the complete liberation from all suffering at its root. The word <em>egantihayam</em> means "singularly beneficial" — pointing beyond relative goods to the one path that leads unconditionally to liberation.',
     'Pay complete attention — what follows is the one teaching that cuts suffering at its root.',
     ['Liberation', 'Attention', 'Root of Suffering']),

    ('sutra-2','32.2',
     'णाणस्स सव्वस्स पगासणाए, अण्णाण मोहस्स विवज्जणाए ।\nरागस्स दोसस्स य संखएणं, एगंत सोक्खं समुवेइ मोक्खं ॥३२.२॥',
     'Through the complete illumination of knowledge, through the abandonment of ignorance and delusion, and through the utter destruction of attachment and aversion — one attains liberation: the singular supreme bliss.',
     'Three causes of liberation are given: (1) full illumination of knowledge — jñāna that reveals the nature of the self and reality; (2) abandonment of ignorance and moha — the root misperception that confuses self with non-self; (3) complete destruction of rāga and dvesha — the twin engines of karma accumulation. When all three are accomplished, moksha — ekānta-sukha, singular bliss — is attained.',
     'Knowledge + no-delusion + no-attachment/aversion = Liberation.',
     ['Knowledge', 'Moksha', 'Rāga-Dvesha']),

    ('sutra-3','32.3',
     'तस्सेसमग्गो गुरुविद्ध-सेवा, विवज्जणा बाल-जणस्स दूरा ।\nसज्झाय-एगंत-णिसेवणा य, सुतत्थ-संचिंतणया धिढ़ई य ॥३२.३॥',
     'The path to this liberation is: service to wise and elderly gurus; keeping far from the company of the ignorant; solitary, consistent scriptural study; and firm, constant contemplation of the meaning of scripture.',
     'Four pillars of the path: (1) <em>guru-sēvā</em> — serving knowledgeable, senior teachers; this transmits lineage wisdom directly. (2) <em>bāla-jana vivajjanā</em> — distancing from the ignorant, whose worldly thinking corrupts the spiritual atmosphere. (3) <em>svādhyāya ekānta-niṣēvanā</em> — solitary, consistent study of scripture. (4) <em>suta-artha-saṃcintanā</em> — deep, persistent contemplation of what has been studied. Together they build the unshakeable conviction needed for liberation.',
     'Four foundations: serve wise teachers, avoid the ignorant, study alone, contemplate deeply.',
     ['Guru-Service', 'Svādhyāya', 'Contemplation', 'Path']),

    ('sutra-4','32.4',
     'आहारमिच्छे मियमेसिणजोग्गं, सहायमिच्छे णिउणत्थबुद्धिं ।\nणिकेयमिच्छेज्ज विवेगजोग्गं, समाहिकामे समणे तवस्सी ॥३२.४॥',
     'A tapasvi monk seeking samādhi should seek properly measured and appropriate food, a sharp-minded and capable companion, and a suitable secluded dwelling place.',
     'Three requisites for a monk oriented toward samādhi: (1) measured, clean food — neither too much nor defiled, so the body does not distract the practice; (2) a wise, discerning companion — one who helps the practice rather than hindering it; (3) a secluded, suitable dwelling — free from disturbances. These three support the monk\'s inner life.',
     'A monk seeking inner peace needs measured food, a wise companion, and a solitary dwelling.',
     ['Ascetic Practice', 'Samādhi', 'Ekala-Vihāra']),

    ('sutra-5','32.5',
     'ण वा लभेज्ज णिउणं सहायं, गुणाहियं वा गुणओ समं वा ।\nएक्को वि पावाइ विवज्जयंतो, विहरेज्ज कामेसु असज्जमाणो ॥३२.५॥',
     'If a suitable companion of higher or equal virtues cannot be found, one should wander alone, abandoning sin and remaining completely unattached to sense pleasures.',
     'When an ideal companion is unavailable, solitary wandering is better than bad company. The condition is clear: one must actively avoid sins (<em>pāvāi vivajjayanto</em>) and remain unattached to sense pleasures (<em>kāmesu asajjamāno</em>). The monk\'s inner strength must substitute for external support. This is <em>ekala-vihāra</em> — a recognized and honored mode of the Jain monastic path.',
     'No suitable companion? Wander alone — but never wander into sin or sense attachment.',
     ['Ekala-Vihāra', 'Solitary Wandering', 'Ascetic Practice']),

    # ── Section 4-8: Origin of Suffering ─────────────────────────────────────
    ('sutra-6','32.6',
     'जहा य अंडप्पभवा बालागा, अंड बालागप्पभवं जहा य ।\nएमेव मोहायणं खु तण्हा, मोहं च तण्हायणं वयंति ॥३२.६॥',
     'Just as cranes are born from eggs and eggs arise from cranes — so too, delusion is the birthplace of craving and craving is the birthplace of delusion; they perpetually generate each other.',
     'This sutra presents the primordial feedback loop of suffering. Moha (delusion) generates tṛṣṇā (craving): delusion misidentifies the self with the world and thus desires what the world offers. Craving in turn feeds moha: chasing objects keeps one in the delusion that they can satisfy. Like eggs and birds, neither came first. The cycle is beginningless — which is why only a radical break (samyak-jñāna) can end it.',
     'Delusion breeds craving; craving breeds delusion. An ancient loop — only true knowledge breaks it.',
     ['Moha', 'Tṛṣṇā', 'Karma Chain', 'Root of Suffering']),

    ('sutra-7','32.7',
     'रागो दोसो वि य कम्मीयं, कम्मं च मोहप्पभवं वयंति ।\nकम्मं च जाईमरणस्स मूलं, दुक्खं च जाईमरणं वयंति ॥३२.७॥',
     'Attachment and aversion are karma\'s seed; karma arises from delusion. Karma is the root of birth and death; birth and death are suffering — so the wise declare.',
     'The causal chain is made explicit: moha → rāga-dvesha → karma → janma-maraṇa → dukha. Delusion is the seed; attachment and aversion are its flowering into karmic action; karma determines the cycle of births; births constitute suffering. There is no shortcut: the chain must be broken at its root — delusion — by right knowledge.',
     'Delusion → Attachment/Aversion → Karma → Birth-Death → Suffering. Break the chain at its root.',
     ['Karma Chain', 'Rāga-Dvesha', 'Saṃsāra', 'Root of Suffering']),

    ('sutra-8','32.8',
     'दुक्खं हयं जस्स ण होइ मोहो, मोहो हओ जस्स ण होइ तण्हा ।\nतण्हा हया जस्स ण होइ लोहो, लोहो हओ जस्स ण किंचणाइ ॥३२.८॥',
     'Suffering is destroyed for one without delusion; delusion is destroyed for one without craving; craving is destroyed for one without greed; greed is destroyed for one with no possessiveness — nothing to cling to.',
     'The chain of liberation runs exactly backward through the chain of bondage. Each liberation is conditional: no possessiveness → no greed; no greed → no craving; no craving → no delusion; no delusion → no suffering. This is why Jain practice emphasizes aparigraha (non-possessiveness) so fundamentally — it is the first domino that, when removed, dismantles the entire architecture of suffering.',
     'Non-possessiveness destroys greed; no greed destroys craving; no craving destroys delusion; no delusion destroys suffering.',
     ['Liberation', 'Aparigraha', 'Moha', 'Chain of Liberation']),

    # ── Section 9-11: Means to Destroy Passion ───────────────────────────────
    ('sutra-9','32.9',
     'रागं च दोसं च तहेव मोहं, उद्धत्तु कामेण समूल-जालं ।\nजे जे उवाया पडिवज्जयव्वा, ते कित्तइस्सामि अहाणुपुव्विं ॥३२.९॥',
     'To completely uproot — roots and all — the entire web of attachment, aversion, and delusion, I will now enumerate in order all the means to be adopted.',
     'Having diagnosed the disease in sutras 6–8, Lord Mahāvīra now promises the cure. The phrase <em>samūla-jālaṃ</em> (the root-and-all web) is significant: superficial trimming will not do. The rāga-dvesha-moha complex must be uprooted completely, and this requires systematic practice. What follows in the chapter is that enumeration.',
     'The web of attachment-aversion-delusion must be uprooted completely. Now the means will be described.',
     ['Rāga-Dvesha', 'Moha', 'Practice', 'Liberation Path']),

    ('sutra-10','32.10',
     'रसा पगामं ण णिसेवियव्वा, पायं रसा दित्तिकरा णराणं ।\nदित्तं च कामा समिभड्डवंति, दुमं जहा साउफलं व पक्खी ॥३२.१०॥',
     'Flavors and tastes should not be over-indulged; they generally inflame people. The inflamed are engulfed by sense desires, just as birds swarm upon a sweet-fruited tree.',
     'The first practical instruction targets the tongue — the most habitual sense attachment for most people. Over-indulgence in pleasant flavors creates inflammation of all the senses. The analogy is precise: a sweet-fruited tree does not have to seek the birds; they come on their own and are trapped by the sweetness. Similarly, once the tongue is inflamed, the senses pull the practitioner away from the path without deliberate effort.',
     'Don\'t over-indulge in tastes. Inflamed senses attract more desire, like birds swarming a sweet tree.',
     ['Sense Restraint', 'Rasa', 'Brahmacharya']),

    ('sutra-11','32.11',
     'जहा दवग्गि पउरिंधणे वणे, समारुओ णोवसमं उवेइ ।\nएविंदियग्गि वि पगाम-भोइणो, ण भंभयारिस्स हियाय कस्सइ ॥३२.११॥',
     'Just as a forest fire fed with abundant fuel does not calm down — similarly, the fire of the senses in one who over-indulges is not beneficial to any observer of brahmacharya.',
     'The forest fire analogy: the more fuel, the stronger the fire. The senses, when repeatedly indulged, do not become satisfied; they become more demanding. This is why ascetic traditions universally restrict sense pleasures — not from fear of the world, but from the direct observation that indulgence feeds the flame rather than quenching it. For a brahmacharya practitioner, this fire is particularly destructive.',
     'Feeding the senses is like feeding a fire: more fuel, more fire. Indulgence never leads to peace.',
     ['Sense Restraint', 'Brahmacharya', 'Fire Analogy']),

    # ── Section 12-20: Brahmacharya & Women ──────────────────────────────────
    ('sutra-12','32.12',
     'विवित्त-संजासण-जिंदियाणं, ओमसणणं दिमइदियाणं ।\nण रागसतु धरिसेइ चित्तं, पराइओ वाहिर-वोसहेहिं ॥३२.१२॥',
     'For one observing solitary seat and bed, eating little, and restraining the senses — attachment cannot overpower the mind, just as a disease is defeated by external medicine.',
     'Three protective practices: (1) vivikta-śayyā — solitary seat and bed, keeping the practitioner away from stimulating environments; (2) ōmaśanana — reduced eating, which directly reduces the fire of the senses; (3) indriya-restraint — disciplined non-engagement with sense objects. Together these three form the outer fortress of brahmacharya. Rāga cannot breach this fortification, just as medicine defeats disease from outside.',
     'Solitary seat, reduced eating, and sense-restraint form the outer fortress that attachment cannot breach.',
     ['Brahmacharya', 'Sense Restraint', 'Ascetic Practice']),

    ('sutra-13','32.13',
     'जहा बिरालावसहस्स मूले, ण मूसगाणं वसही पसत्था ।\nएमेव इत्थी-णिलयस्स मज्झे, ण भंभयारिस्स खमो णिवासो ॥३२.१३॥',
     'Just as it is unsuitable for mice to dwell near a cat\'s lair — similarly, it is not appropriate for an observer of brahmacharya to reside among women.',
     'The mouse-and-cat analogy makes the point through natural self-preservation logic. A mouse near a cat\'s dwelling is perpetually at risk; even the strongest mouse would eventually succumb to proximity. Similarly, even the most committed brahmacharya practitioner is not served by placing himself in a structurally high-risk environment. This is not a statement about women\'s moral character but about the monk\'s need to structure his environment in support of his vows.',
     'A mouse near a cat\'s home is always at risk. Similarly, living among women compromises brahmacharya.',
     ['Brahmacharya', 'Vivikta-Vāsa', 'Monastic Discipline']),

    ('sutra-14','32.14',
     'ण रूव-लावण्ण-विलास-हासं, ण जिंपयं इंगिय-पेहियव्वा ।\nइत्थीणं चित्तिंस णिवेसइत्ता, ददु ववस्से समणे तवस्सी ॥३२.१४॥',
     'A tapasvi monk should not fix his mind on women\'s beauty, grace, laughter, voice, or physical gestures — and should not engage in conversation with them.',
     'This sutra names the specific channels through which fascination enters: visual beauty, graceful movement, laughter, voice, and gestures. The monk must keep the mind from settling on any of these. This is not hatred of women — it is a recognition that these channels are specifically designed by biology to create attachment, and a monk committed to liberation must not let his mind rest there.',
     'Don\'t let the mind dwell on appearance, grace, laughter, voice, or gestures — these are attachment\'s entry points.',
     ['Brahmacharya', 'Monastic Discipline', 'Sense Control']),

    ('sutra-15','32.15',
     'अदंसणं चेव अपत्थणं च, अचिंतणं चेव अकित्तणं च ।\nइत्थी-जणस्सारिय-झाणजुग्गं, हियं सया बंभवए-रयाणं ॥३२.१५॥',
     'Not seeing, not desiring, not thinking about, and not praising women — this is the dhyāna-worthy conduct always beneficial for those devoted to brahmacharya.',
     'Four-fold protection for brahmacharya: (1) not looking (<em>adaṃsaṇa</em>); (2) not desiring (<em>apatthana</em>); (3) not thinking about (<em>acintana</em>); (4) not glorifying (<em>akittana</em>). The four levels move from outer to inner: looking can be controlled by the body; desiring by the will; thinking by the mind; but praising reveals that the fascination has already colored the speech and attitude. All four must be mastered for brahmacharya to be authentic.',
     'Four protections of brahmacharya: don\'t look, don\'t desire, don\'t think about, don\'t praise.',
     ['Brahmacharya', 'Monastic Discipline']),

    ('sutra-16','32.16',
     'कामं तु देवीहिं विभूसियाहिं, ण चाइया खोभइउं तिगुत्ता ।\nतहा वि एगंतिहयं तिं पच्चा, विवित्तवासो मुणीणं पसत्थो ॥३२.१६॥',
     'Even though triple-guarded monks cannot be disturbed by adorned goddesses — still, ultimately, solitary dwelling is the most beneficial and praiseworthy state for monks.',
     'The argument reaches its conclusion with an extreme case: even a monk who has reached the level of triple-gupta (triple restraint of body, speech, and mind) and cannot be disturbed even by adorned goddesses — even for him, solitary dwelling is recommended. This is not about weakness but about wisdom: why place yourself in a situation that demands constant vigilance when you could simply remove the stimulus? Vivikta-vāsa (solitary dwelling) is not a necessity of weakness but a sign of wisdom.',
     'Even the most advanced monk benefits from solitary dwelling — wisdom, not weakness, chooses simplicity.',
     ['Vivikta-Vāsa', 'Brahmacharya', 'Monastic Wisdom']),

    ('sutra-17','32.17',
     'मोक्खाभिकिंखिस्स उ माणवस्स, संसार-भीरुस्स ठियस्स धम्मे ।\nणेयारिस दुत्तरमिथ लोए, जिहित्थिओ बालमणोहराओ ॥३२.१७॥',
     'For a person yearning for liberation, fearful of samsāra, and established in dharma — there is nothing more difficult in this world than abandoning mind-captivating women.',
     'This is a frank acknowledgment of one of the hardest aspects of the monastic path. The text does not pretend it is easy. The fascination with women is described as <em>bālamanoharāo</em> — "captivating even for intelligent minds" — acknowledging the deep-seated biological and psychological pull that makes this renunciation so demanding. The honest naming of the difficulty is itself a teaching: know your enemy before you fight it.',
     'There is nothing harder for a liberation-seeker than renouncing women. Acknowledge the difficulty clearly.',
     ['Brahmacharya', 'Renunciation', 'Samsāra']),

    ('sutra-18','32.18',
     'एए य संगे समइक्कमित्ता, सुदुत्तरा चेव भवंति सेसा ।\nजहा महासागरे उत्तरित्ता, णई भवे अवि गंगासमाणा ॥३२.१८॥',
     'Once this greatest attachment is transcended, all remaining attachments become easy to overcome — just as after crossing the great ocean, even crossing a Gangā-like river becomes easy.',
     'The ocean-and-river analogy gives a liberating perspective. If the seeker can win this one hardest battle — the pull of romantic attachment — all other battles of renunciation become relatively manageable. This is encouraging: it suggests that the difficulty is not uniformly distributed. Master the hardest thing and the rest follows. The ocean (stri-sanga) crossed, the rivers (other attachments) are mere streams.',
     'Win the hardest battle — romantic attachment — and all other battles of renunciation become rivers after crossing an ocean.',
     ['Renunciation', 'Brahmacharya', 'Progressive Liberation']),

    ('sutra-19','32.19',
     'कामापुगिद्दिस्सपभवं खु दुक्खं, सव्वस्स लोगस्स सदेवगस्स ।\nजं काइयं माणसियं च किंच, तस्संतगं गच्छइ वीयरागो ॥३२.१९॥',
     'The suffering born of attachment to sense pleasures — whatever is physical or mental — for all worlds including the realms of gods — a vītarāgī (the dispassionate one) reaches its complete end.',
     'The scope is total: kāmabhoga-derived suffering covers all bodily and mental pain, and it afflicts everyone from human to divine realms. The only one who reaches its complete end (<em>taṃ-antaṃ gacchei</em>) is the vītarāgī — the one who has moved beyond rāga, who has no residual desire for sense pleasures. This is the destination the preceding sutras have been pointing toward.',
     'Only the dispassionate one — the vītarāgī — reaches the complete end of all suffering, bodily and mental.',
     ['Vītarāgī', 'Liberation', 'Kāmabhoga']),

    ('sutra-20','32.20',
     'जहा य किंपागफला मणोरमा, रसेण वण्णेण य भुज्जमाणा ।\nते खुडए जीविय पच्चमाणा, एओवमा कामगुणा विवागे ॥३२.२०॥',
     'Just as kimpāka fruits are charming in taste and color while being eaten, but destroy life in their digestion — such is the consequence of sense pleasures when they ripen as karma.',
     'Kimpāka (a poisonous fruit mentioned in Indian scriptures) appears beautiful and delicious but is fatal after consumption. Sense pleasures follow the same trajectory: attractive at the point of contact, devastating in their karmic aftermath. The "ripening" (vipāka) of the karma accumulated through sense-indulgence is the ripe fruit of suffering in future lives. The analogy is stark and complete.',
     'Sense pleasures are like kimpāka fruit — beautiful and sweet now, deadly in their ripening.',
     ['Kāmabhoga', 'Karma', 'Vipāka']),
]

# ── The 13-sutra pattern for each indriya group ───────────────────────────────
# We generate sutras 21-99 (six groups × 13 sutras + the shared sutra 21)
# Actually: 21 is shared intro, then groups 22-34 (eye), 35-47 (ear), etc.

INDRIYA_GROUPS = [
    # (start_num, sense_name, sense_obj, sense_organ, analogy_text, analogy_id)
    (22, 'Eye', 'form', 'eye',
     'like a fish, greedy for bait, pierced by a hook and meeting death',
     'fish-hook'),
    (35, 'Ear', 'sound', 'hearing',
     'like a deer, maddened by music, insatiable and meeting untimely death',
     'deer-music'),
    (48, 'Nose', 'smell', 'nose',
     'like serpents intensely attracted to medicinal fragrances, emerging from their lairs and being killed',
     'serpent-fragrance'),
    (61, 'Tongue', 'taste', 'tongue',
     'like a fish, greedy for bait, pierced by a hook and meeting death',
     'fish-hook-taste'),
    (74, 'Touch', 'touch', 'body',
     'like a buffalo intensely attached to cool water, seized by a crocodile',
     'buffalo-crocodile'),
    (87, 'Mind', 'mental states', 'mind',
     'like an elephant, maddened by desire for female elephants, struck down by hunters on the path',
     'elephant-hunters'),
]

# Prakrit templates — sense-specific words
PRAKRIT_WORDS = {
    'Eye':   {'obj':'रूव', 'organ':'चक्खु', 'organ_acc':'चक्खुस्स', 'obj_acc':'रूवस्स',
              'anug':'रूवाणुगासाणुगए', 'anuvāen':'रूवाणुवाएण', 'pur':'रूवापुरत्तस्स',
              'atitte':'रूवे अतित्ते', 'virato':'रूवे विरत्तो', 'gao':'रूवम्मि गओ',
              'c3':'रागाउरे सीयजलावसण्णे, मच्छे जहा आमिसभोग-गिद्धे', 'num_word':'चक्खुरिंदिय'},
    'Ear':   {'obj':'सद्द', 'organ':'सोय', 'organ_acc':'सोयस्स', 'obj_acc':'सदस्स',
              'anug':'सद्दाणुगासाणुगए', 'anuvāen':'सद्दाणुवाएण', 'pur':'सद्दापुरत्तस्स',
              'atitte':'सद्दे अतित्ते', 'virato':'सद्दे विरत्तो', 'gao':'सद्दम्मि गओ',
              'c3':'रागाउरे हिरण-मिगे व मुढे, सद्दे अतित्ते समुवेइ मच्चुं', 'num_word':'सोतेंदिय'},
    'Nose':  {'obj':'गंध', 'organ':'घाण', 'organ_acc':'घाणस्स', 'obj_acc':'गंधस्स',
              'anug':'गंधाणुगासाणुगए', 'anuvāen':'गंधाणुवाएण', 'pur':'गंधापुरत्तस्स',
              'atitte':'गंधे अतित्ते', 'virato':'गंधे विरत्तो', 'gao':'गंधम्मि गओ',
              'c3':'रागाउरे ओसिहि-गंध-गिद्धे, सप्पे विलाओ विव णिक्खमंते', 'num_word':'घाणेंदिय'},
    'Tongue':{'obj':'रस', 'organ':'जिब्भा', 'organ_acc':'जिब्भाए', 'obj_acc':'रसस्स',
              'anug':'रसाणुगासाणुगए', 'anuvāen':'रसाणुवाएण', 'pur':'रसापुरत्तस्स',
              'atitte':'रसे अतित्ते', 'virato':'रसे विरत्तो', 'gao':'रसम्मि गओ',
              'c3':'रागाउरे बडिस-विभिण्णकाए, मच्छे जहा आमिसभोग-गिद्धे', 'num_word':'रसनेंदिय'},
    'Touch': {'obj':'फास', 'organ':'काय', 'organ_acc':'कायस्स', 'obj_acc':'फासस्स',
              'anug':'फासाणुगासाणुगए', 'anuvāen':'फासाणुवाएण', 'pur':'फासापुरत्तस्स',
              'atitte':'फासे अतित्ते', 'virato':'फासे विरत्तो', 'gao':'फासम्मि गओ',
              'c3':'रागाउरे सीयजलावसण्णे, मिहसे व गाहगहीए मरणे', 'num_word':'स्पर्शेंदिय'},
    'Mind':  {'obj':'भाव', 'organ':'मण', 'organ_acc':'मणस्स', 'obj_acc':'भावस्स',
              'anug':'भावाणुगासाणुगए', 'anuvāen':'भावाणुवाएण', 'pur':'भावापुरत्तस्स',
              'atitte':'भावे अतित्ते', 'virato':'भावे विरत्तो', 'gao':'भावम्मि गओ',
              'c3':'रागाउरे कामगुणेसु गिद्धे, करेणुमग्गाविहए व णागे', 'num_word':'मनोविजय'},
}

# Generate sutra 21 (shared intro for all indriya sections)
SUTRAS.append((
    'sutra-21','32.21',
    'जे इंदियाणं विसया मणुण्णा, ण तेसु भावं णिसिरे कयाइ ।\nण यामणुण्णेसु मणं पि कुज्जा, समाहिकामे समणे तवस्सी ॥३२.२१॥',
    'A tapasvi monk seeking samādhi should never develop attachment toward pleasant sense objects nor aversion toward unpleasant ones.',
    'This sutra is the master principle that governs the entire sense-indriya section (sutras 21–99). The tapasvi seeking samādhi must maintain complete equanimity: neither bhāva (deep settlement) toward the pleasant, nor mana (even mental movement) toward the unpleasant. The goal is not to force positive feelings toward everything, but to establish the mind in a place where it no longer swings with the pleasant-unpleasant pendulum.',
    'Don\'t settle into attachment for pleasant things; don\'t let the mind move toward unpleasant things either. Stay centered.',
    ['Equanimity', 'Sense Control', 'Samādhi']
))

def make_indriya_sutras(start, sense, sense_obj, sense_organ, analogy, w):
    """Generate the 13 sutras for one sense group."""
    senses_title = f'{sense}-Sense Victory'
    su = []
    n = start  # starts at 22, 35, 48, 61, 74, or 87

    # A: organ grasps object; equanimity = vītarāgī
    obj_cap = sense_obj.capitalize()
    organ_cap = sense_organ.capitalize()
    prakrit_A = f'{w["organ_acc"]} {w["obj"]}ं गहणं वयंति, तं रागहेउं तु मणुण्णमाहु ।\nतं दोसहेउं अमणुण्णमाहु, समो य जो तेसु स वीयरागो ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_A,
        f'{obj_cap} is said to be what the {sense_organ} grasps; pleasant {sense_obj} is called the cause of attachment, unpleasant {sense_obj} the cause of aversion. One who maintains equanimity toward both is called vītarāgī.',
        f'Each sense organ has its corresponding object. The {sense_organ} is drawn to {sense_obj} and through it develops either rāga (when pleasant) or dvesha (when unpleasant). Both responses bind karma. The vītarāgī — the dispassionate one — maintains equanimity (sama) toward both pleasant and unpleasant {sense_obj}. This equanimity is not indifference; it is freedom from reactive bondage.',
        f'Pleasant {sense_obj} → attachment; unpleasant {sense_obj} → aversion. The vītarāgī stays equanimous to both.',
        ['Equanimity', 'Vītarāgī', sense_organ.capitalize() + '-Sense']))
    n += 1

    # B: reciprocal — object grasped by organ; organ grasps object
    prakrit_B = f'{w["obj_acc"]} {w["organ"]}ं गहणं वयंति, {w["organ_acc"]} {w["obj"]}ं गहणं वयंति ।\nरागस्स हेउं समणुण्णमाहु, दोसस्स हेउं अमणुण्णमाहु ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_B,
        f'The {sense_organ} grasps {sense_obj}; {sense_obj} is grasped by the {sense_organ}. Pleasant [{sense_obj}] is said to be the cause of attachment; unpleasant [{sense_obj}] the cause of aversion.',
        f'This sutra restates the same truth from both directions — the organ and its object are mutually defining. They do not exist in isolation: the eye constitutes forms as visible; forms constitute the eye as seeing. This mutual dependence means neither is inherently pleasant or unpleasant — the quality arises from the rāga-dvesha projection of the mind. Understanding this is the beginning of freedom from sense-bondage.',
        f'Neither {sense_organ} nor {sense_obj} is the problem; the problem is the rāga-dvesha projection onto them.',
        ['Sense Mechanism', 'Rāga-Dvesha']))
    n += 1

    # C: intensely attached → untimely destruction (analogy)
    prakrit_C = f'{w["obj"]}ेसु जो गिद्धिमुवेइ तिव्वं, अकालियं पावइ से विणासं ।\n{w["c3"]} ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_C,
        f'One who develops intense attachment to {sense_obj} meets untimely destruction — {analogy}.',
        f'The analogy is drawn from nature to show the fatal logic of sense attachment. The animal\'s attachment is so strong that it overrides the survival instinct — it cannot see the trap because the desired object blinds it. A practitioner caught in intense sensory craving is in the same situation: the pleasure overrides the perception of danger.',
        f'Intense attachment to {sense_obj} leads to untimely destruction — {analogy}.',
        ['Sense Attachment', 'Danger', 'Analogy']))
    n += 1

    # D: intensely aversive → immediate suffering; no fault in object
    prakrit_D = f'जे याविं दोसं समुवेइ तिव्वं, तंसिक्खणे से उ उवेइ दुक्खं ।\nदुदंत-दोसेण सएण जंतु, ण किंचि {w["obj"]}ं अवरज्झइ से ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_D,
        f'One who develops intense aversion to unpleasant {sense_obj} experiences immediate suffering within that very moment — the being is harmed by its own intense aversion; there is no fault in the {sense_obj} itself.',
        f'Aversion is as binding as attachment. The text makes a precise philosophical point: the {sense_obj} itself carries no fault (<em>na kiṃci... aparajjhai se</em>). The fault lies entirely in the dvesha (aversion) generated by the mind. The suffering comes not from the unpleasant stimulus but from the reactive rejection of it. This is why equanimity — not avoidance — is the goal.',
        f'Aversion creates its own suffering immediately. The {sense_obj} is not at fault — your reactive rejection is.',
        ['Dvesha', 'Equanimity', 'Non-Fault']))
    n += 1

    # E: extremely attached to beautiful, aversive to ugly → crushing suffering; vīrāgī unaffected
    prakrit_E = f'एगंतरते रुद्रूरिस {w["obj"]}े, अतालिसे से कुणइ पओसं ।\nदुक्खस्स संपीलमुवेइ बाले, ण लिप्पइ तेण मुणी विरागो ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_E,
        f'Extremely attached to beautiful {sense_obj} and aversive to unpleasant {sense_obj}, the ignorant person experiences the crushing weight of suffering; but the detached muni is not stained by it.',
        f'The same {sense_obj} — the same world — produces crushing suffering in the ignorant person and leaves the vīrāgī muni completely unstained. The difference is entirely internal: one mind is entangled in rāga-dvesha, the other has renounced both. The world does not need to change; only the mind\'s relationship to it needs to change.',
        f'The same world crushes the attached; the detached muni remains unstained. It\'s about the mind, not the world.',
        ['Vītarāgī', 'Muni', 'Detachment']))
    n += 1

    # F: sense-āsakt jīva harms others
    prakrit_F = f'{w["anug"]} य जीवे, चराचरे हिंसइ णेगरूवे ।\nचित्तेहिं ते परितावेइ बाले, पीलेइ अत्तदुगुरू किलिट्ठु ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_F,
        f'A being captivated by {sense_obj}-attachment harms mobile and stationary beings in many ways; the deluded one torments others with various intentions and oppresses them.',
        f'Sense attachment is not a private matter — it generates violence toward others. The person attached to {sense_obj} will injure, deceive, steal, and exploit to obtain or protect their objects of attachment. The affliction spreads outward: what started as inner craving becomes outer himsa. This is why the Jain tradition links ahimsa so directly to non-attachment.',
        f'{sense_obj.capitalize()}-attachment generates harm to others. Inner craving becomes outer violence.',
        ['Hiṃsā', 'Attachment', 'Ahimsa']))
    n += 1

    # G: from sense possession — no happiness anywhere
    prakrit_G = f'{w["anuvāen"]} परिग्गहेण, उप्पायणे रक्खण-सिण्णओगे ।\nवए विओगे य कहं सुहं से, संभोगकाले य अतित्तलाभे ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_G,
        f'From {sense_obj}-based possession — earning it, protecting it, using it — spending and losing it: how can there be any happiness? Even at the time of enjoyment, insatiable dissatisfaction is its only fruit.',
        f'The full lifecycle of sense-based possession is mapped: earning → protecting → using → losing. At every stage there is anxiety, effort, or grief. Even the brief window of enjoyment does not bring satisfaction — only insatiety. The rhetorical question "how can there be happiness?" is not answered because the life cycle of possession makes the answer obvious.',
        f'Earning, protecting, using, losing sense-objects: where in this cycle is there actual happiness?',
        ['Aparigraha', 'Possession', 'Suffering']))
    n += 1

    # H: insatiable → dissatisfied → steals
    prakrit_H = f'{w["atitte"]} य परिग्गहम्मि, सत्तोवसत्तो ण उवेइ तुट्टिं ।\nअतुट्टिदोसेण दुही परस्स, लोभाविले आययई अदत्तं ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_H,
        f'Insatiable regarding {sense_obj} and its possessions, intensely attached, one finds no satisfaction. Miserable from dissatisfaction and maddened by greed, one takes what has not been given.',
        f'The chain from attachment to theft: insatiability → suffering from dissatisfaction → greed → taking what is not given. Adattādāna (taking the non-given) — the Jain term for stealing — arises from a chain that begins with the simple fact of non-satisfaction in sense pleasures. The attachment never finds its full object; greed is the engine; theft is the inevitable exit.',
        f'Insatiability → dissatisfaction → greed → stealing. Attachment to {sense_obj} ends in theft.',
        ['Adattādāna', 'Greed', 'Suffering']))
    n += 1

    # I: craving-driven thief → maya, lies; still not freed
    prakrit_I = f'तण्हाभिभूयस्स अदत्तहारिणो, {w["obj"]}े अतित्तस्स परिग्गहे य ।\nमायामुसं वड्डुइ लोभदोसा, तत्थावि दुक्खा ण विमुच्चइ से ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_I,
        f'For one overcome by craving, insatiable regarding {sense_obj} and taking what is not given — greed\'s fault causes deceit and falsehood to grow; and even then, one is not freed from suffering.',
        f'Theft generates its own miserable consequences: to steal, one must deceive; to cover the theft, one must lie. The entire web of māyā (deceit) and mṛṣā (falsehood) grows from the root of greed. And even after all this effort and moral degradation, the person is still not freed from suffering — because the root (tṛṣṇā) is untouched.',
        f'Craving → stealing → deceit → lies. And even then, still not freed from suffering.',
        ['Māyā', 'Mṛṣā', 'Karma']))
    n += 1

    # J: suffering before, during, after lying
    prakrit_J = f'मोसस्स पच्छा य पुरत्थओ य, पओगकाले य दुही दुरंते ।\nएवं अदत्ताणि समाययंतो, {w["obj"]}े अतित्तो दुहिओ अणिस्सो ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_J,
        f'Painful before lying, during the act of lying, and painful afterward too — one who wrongfully takes things, insatiable in {sense_obj}, becomes wretched and without shelter.',
        f'The temporal completeness of suffering from falsehood: before (anticipation and guilt), during (the act), and after (remorse and consequences). There is no window of genuine peace. The insatiable person is described as <em>duṛante anissō</em> — wretched and without refuge. This is the portrait of attachment taken to its final stage: a person trapped in their own craving with nowhere to rest.',
        f'Before lying, while lying, after lying — suffering in all three. Attachment to {sense_obj} leaves no shelter.',
        ['Mṛṣā', 'Suffering', 'No-Refuge']))
    n += 1

    # K: attached person — what happiness?
    prakrit_K = f'{w["pur"]} णरस्स एवं, कत्तो सुहं होज्ज कयाइ किंचि ।\nतत्थोवभोगे वि किलेसदुक्खं, णिव्वत्तइ जस्स कएण दुक्खं ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_K,
        f'How can there ever be any happiness for a person insatiable in {sense_obj}? Even in the very enjoyment, intense afflicting suffering is generated — through which karma is accumulated that brings more suffering.',
        f'The rhetorical question "how can there be happiness?" is the summary verdict. And even the momentary enjoyment is not neutral: it generates intense (kilesa) karma through the very act of enjoying. The enjoyment thus seeds more future suffering. This is the profound teaching on vipāka — the ripening of karmic seeds planted by sense-indulgence.',
        f'Even the moment of {sense_obj}-enjoyment creates karma that generates future suffering. There is no escape within the system.',
        ['Karma', 'Kilesa', 'Vipāka']))
    n += 1

    # L: unpleasant form/object version — suffering succession
    prakrit_L = f'एमेव {w["gao"]} पओसं, उवेइ दुक्खोह परंपराओ ।\nपदुट्ठचित्तो य चिणाइ कम्म, जं से पुणो होइ दुहं विवागे ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_L,
        f'In the same way, one who develops aversion to unpleasant {sense_obj} also receives a succession of sufferings, and with a defiled mind accumulates karma that again becomes suffering in its ripening.',
        f'The parallel case: aversion to unpleasant {sense_obj} is just as karmic as attachment to pleasant {sense_obj}. Both bind. Both accumulate. Both ripen into suffering. The defiled mind (<em>paduṭṭha-citta</em>) is the key: whether defiled by rāga or by dvesha, it generates karma. Equanimity — the absence of both — is the only way out.',
        f'Aversion to unpleasant {sense_obj} also generates karma and suffering. Both rāga and dvesha bind equally.',
        ['Dvesha', 'Karma', 'Vipāka']))
    n += 1

    # M: detached person — free from grief, lotus analogy
    prakrit_M = f'{w["virato"]} मणुओ विसोगो, एएण दुक्खोह परंपरेण ।\nण लिप्पइ भवमज्झे वि संतो, जलेण वा पोक्खरिणी पलासं ॥३२.{n}॥'
    su.append((f'sutra-{n}', f'32.{n}', prakrit_M,
        f'A person detached from {sense_obj} is free from grief and not touched by this succession of sufferings — even while remaining in worldly existence, just as a lotus leaf is untouched by water.',
        f'The lotus analogy is one of the most beloved in Indian spiritual literature. The lotus leaf is fully in the water — submerged in the same world — yet not wetted by it. The vītarāgī lives in the same world as everyone else but is not caught by it. This is not withdrawal from life; it is the mastery of the mind\'s relationship to sense experience. The suffering chain simply does not attach to one whose mind does not attach.',
        f'Detached from {sense_obj}, one lives in the world like a lotus in water — present, but untouched.',
        ['Vītarāgī', 'Lotus Analogy', 'Detachment', 'Liberation']))
    n += 1

    return su

# Generate all indriya groups
for (start, sense, sense_obj, sense_organ, analogy, _) in INDRIYA_GROUPS:
    w = PRAKRIT_WORDS[sense]
    group_sutras = make_indriya_sutras(start, sense, sense_obj, sense_organ, analogy, w)
    SUTRAS.extend(group_sutras)

# ── Sutras 100-108: Detachment and Liberation ────────────────────────────────
SUTRAS.extend([
    ('sutra-100','32.100',
     'एविंदियत्था य मणस्स अत्था, दुक्खस्स हेउं मणुयस्स रागिणो ।\nते चेव थोवं पि कयाइ दुक्खं, ण वीयरागस्स करेंति किंचि ॥३२.१००॥',
     'Sense objects and mental objects are the cause of suffering for the passionate person; these very same objects do not cause even a trace of suffering to the dispassionate one.',
     'The most radical statement of the chapter: the objects themselves are neutral. The same form, sound, smell, taste, touch, and mental state that plunges a passionate person into chains of suffering causes not even a particle of suffering to the vītarāgī. Reality is the same; the mind\'s relationship to it is different. This is the core Jain teaching: liberation is an inner event, not an outer one.',
     'The same world: causes suffering in the passionate, causes nothing in the dispassionate. Liberation is an inner event.',
     ['Vītarāgī', 'Liberation', 'Inner Freedom']),

    ('sutra-101','32.101',
     'ण कामभोगा समयं उवेंति, ण याविं भोगा विगई उवेंति ।\nजे तप्पओसी य परिग्गही य, सो तेसु मोहा विगई उवेइ ॥३२.१०१॥',
     'Sense pleasures do not produce satisfaction by themselves, nor do they produce dissatisfaction by themselves. It is the one who is attached to and possessive of them who, because of delusion about them, experiences dissatisfaction.',
     'A precise philosophical clarification: kāmabhoga are phenomenologically neutral regarding satisfaction. They neither produce nor prevent satisfaction on their own. The variable is the mind\'s relationship: attachment + possession + delusion = dissatisfaction. This means satisfaction is not found by changing or acquiring objects; it is found by transforming the mind\'s attachment to them.',
     'Pleasures don\'t produce dissatisfaction — your attachment and possession of them do.',
     ['Kāmabhoga', 'Moha', 'Satisfaction']),

    ('sutra-102','32.102',
     'कोहं च माणं च तहेव मायं, लोभं दुगुंछ अरई रई च ।\nहासं भयं सोग पुमित्थियेयं, णपुंसवेयं विविहे य भावे ॥३२.१०२॥',
     '[Attached to sense pleasures, one acquires:] Anger, pride, deceit, greed, disgust, disinterest, desire, laughter, fear, grief, male and female passions, eunuch-states, and various other mental conditions —',
     'The list of mental states generated by sense attachment is comprehensive. The four kaṣāyas (anger, pride, deceit, greed) head the list, but the damage extends to emotional states (disgust, disinterest, desire, laughter, fear, grief) and even to gender-specific passions. Kāmabhoga does not only produce obvious attachment; it generates the entire spectrum of afflicted mental states.',
     'Sense attachment generates: anger, pride, deceit, greed, fear, grief, and many other mental afflictions.',
     ['Kaṣāya', 'Kāmabhoga', 'Mental Afflictions']),

    ('sutra-103','32.103',
     'आवज्जइ एवमणेगरूवे, एवं विहे कामगुणेसु सत्तो ।\nअण्णे य एयप्पभवे विसेसे, कारुण्णदीणे हिरिमे वइस्से ॥३२.१०३॥',
     '— and many other such states arise in one attached to sense pleasures: compassionlessness, wretchedness, shame, and servitude — all born from these same roots.',
     'The list from sutra 102 continues here. The final items — compassionlessness, wretchedness, shame, and servitude — describe the social and psychological degeneration that follows from full immersion in kāmabhoga. The person becomes incapable of genuine compassion (kāruṇya); falls into despair (dīna); loses dignity (hirī) and becomes enslaved (vaissa) to their cravings. This is the full portrait of what sense-attachment does to a human being over time.',
     'Sense attachment ultimately produces compassionlessness, wretchedness, shame, and servitude.',
     ['Kāmabhoga', 'Degeneration', 'Compassion']),

    ('sutra-104','32.104',
     'कप्पं ण इच्छिज्ज सहायलिच्छु, पच्छाणुतावे ण तवप्पभावं ।\nएवं वियारे अमियप्पयारे, आवज्जइ इंदियचोरवस्से ॥३२.१०४॥',
     'A monk should not desire help from a companion, should not regret past actions, and should not desire the power of austerities to bear fruit. In this way, one with unlimited desires falls captive to the thieving senses.',
     'Three subtle forms of desire that compromise the monk: (1) desire for a companion\'s help — dependency on others; (2) regret for past actions — mental clinging to the past; (3) desire for the fruits of austerities — even spiritual practice becomes tainted by desire for reward. These "unlimited desires" (amiya-ppayāra) open the door to the "thieving senses" (indiya-coravasse) — desires that steal the practitioner\'s spiritual capital.',
     'Even these desires compromise the monk: needing help, regretting the past, wanting the fruits of practice.',
     ['Monastic Discipline', 'Indriya-Control', 'Desire']),

    ('sutra-105','32.105',
     'तओ से जायंति पओयणाइं, णिमज्जिउं मोहमहण्णवम्मि ।\nसुहेसिणो दुक्ख-विणोयणट्ठा, तप्पच्चयं उज्जमए य रागी ॥३२.१०५॥',
     'Then arise in such a person the desires — to dive into the great ocean of delusion; the passionate one, pleasure-seeking and wanting to banish pain, makes effort for those very causes.',
     'Once the door of desire opens, the flood begins. The person wanting pleasure and seeking to avoid pain makes effort in the very directions that increase delusion. This is the great irony: the passionate person is effortful — but their effort runs exactly in the wrong direction, diving deeper into the ocean of moha rather than swimming out of it.',
     'Desire leads to effort — but effort toward pleasure dives deeper into the ocean of delusion.',
     ['Moha', 'Desire', 'Wrong Effort']),

    ('sutra-106','32.106',
     'विवरज्जमाणस्स य इंदियत्था, सद्दाइया तावयप्पगारा ।\nण तस्स सव्वे वि मणुण्णयं वा, णिव्वत्तयंति अमणुण्णयं वा ॥३२.१०६॥',
     'For one who is completely detached — sounds and all other sense objects of every kind — none of these, for that person, can produce either pleasure or displeasure.',
     'The mirror image of sutra 100, stated from the object\'s perspective. The sound, form, smell, taste, touch, and mental state have no power to produce pleasure or displeasure in the one who is vīrarāgī. The objects are present; the reactions are absent. This is the complete picture of liberation-in-life: the world runs its full course, but the liberated mind moves through it like light through glass — passing through without being refracted.',
     'For the detached one, no sense object can produce pleasure or displeasure. Objects are present; reactions are absent.',
     ['Vītarāgī', 'Equanimity', 'Liberation-in-Life']),

    ('sutra-107','32.107',
     'एवं सं संकप्प-विकप्पणासु, संजायइ समयमुवडुत्तस्स ।\nअत्थे य संकप्पओ तओ से, पहीयए कामगुणेसु तण्हा ॥३२.१०७॥',
     'In this way, in one established in equanimity with thoughts and counter-thoughts destroyed, craving for sense pleasures is thereafter completely annihilated.',
     'Saṃkalpa (thought/intention) and vikalpa (counter-thought/doubt) are the two primary movements of the reactive mind. When both are destroyed — when the mind ceases its endless pendulum between "I want this" and "I don\'t want that" — samata (equanimity) arises. And with genuine equanimity, the craving for sense pleasures is not suppressed but annihilated: it no longer has a foothold to stand on.',
     'When thought-reactions and counter-thought-reactions both cease, genuine equanimity arises — and craving is annihilated.',
     ['Equanimity', 'Saṃkalpa', 'Nirvāṇa']),

    ('sutra-108','32.108',
     'स वीयरागो कय-सव्विकच्चो, खवेइ णाणावरणं खणेणं ।\nतहेव जं दंसणमावरेइ, जं चंतरायं पकरेइ कम्म ॥३२.१०८॥',
     'That dispassionate one, having fulfilled all duties, destroys in an instant the knowledge-obscuring karma, the vision-obscuring karma, and the obstructing karma.',
     'The chapter culminates with the moment of omniscience. The vītarāgī who has completed all duties and traversed the path of sense-mastery destroys in a single instant (khaṇena) three types of karma: jñānāvaraṇa (knowledge-obscuring), darśanāvaraṇa (vision/right-view-obscuring), and antarāya (obstructing karma). The destruction is simultaneous and instantaneous — the dawn does not arrive gradually but all at once. This is the promise and the destination of the entire chapter.',
     'The dispassionate one, duties fulfilled, destroys knowledge-obscuring, vision-obscuring, and obstructing karma in an instant.',
     ['Omniscience', 'Liberation', 'Karma-Destruction', 'Khaṇa']),
])

# Sort all sutras by sutra number
SUTRAS.sort(key=lambda x: int(x[1].split('.')[1]))

# ── Section dividers ──────────────────────────────────────────────────────────
# id: (insert_before_sutra_num, text)
DIVIDERS = {
    1:  'Part I — Means for Eternal Happiness · Sutras 1–5',
    4:  'Part II — Solitary Wandering',
    6:  'Part III — The Chain of Suffering · Origin & Breaking',
    9:  'Part IV — Means to Destroy Attachment, Aversion, Delusion · Sutras 9–11',
    12: 'Part V — Brahmacharya · Renouncing Women\'s Company · Sutras 12–20',
    21: 'Part VI — Five-Sense Victory · Introduction · Sutra 21',
    22: 'Part VII — Eye-Sense Victory · Rūpa · Sutras 22–34',
    35: 'Part VIII — Ear-Sense Victory · Shabda · Sutras 35–47',
    48: 'Part IX — Nose-Sense Victory · Gandha · Sutras 48–60',
    61: 'Part X — Tongue-Sense Victory · Rasa · Sutras 61–73',
    74: 'Part XI — Touch-Sense Victory · Sparsha · Sutras 74–86',
    87: 'Part XII — Mind Victory · Bhāva · Sutras 87–99',
    100: 'Part XIII — Detachment from Sense Objects · Its Fruit · Sutras 100–108',
}

# ── Load SEARCH_INDEX from ch31 and add ch32 ─────────────────────────────────
ch31_html = (BASE / 'uttaradhyana-ch31.html').read_text(encoding='utf-8')
m = re.search(r'var SEARCH_INDEX = (\[.*?\]);', ch31_html, re.DOTALL)
search_index = json.loads(m.group(1))

# Build ch32 search entries
ch32_sutras_search = [{'id': 'hero', 'num': 'C32', 'title': 'Pramādasthāna — Stations of Negligence · 108 Sutras'}]
for sid, snum, sprakrit, strans, *_ in SUTRAS:
    short = strans[:80].rstrip()
    ch32_sutras_search.append({'id': sid, 'num': snum, 'title': short})

ch32_entry = {
    'file': 'uttaradhyana-ch32.html',
    'num': 'C32',
    'title': 'Uttaradhyayana Sutra Chapter 32: Pramādasthāna',
    'sutras': ch32_sutras_search
}

# Insert ch32 between ch31 (index 29) and ch33 (index 30)
search_index.insert(30, ch32_entry)
search_index_json = json.dumps(search_index, ensure_ascii=False, separators=(',',':'))

# ── HTML builder ──────────────────────────────────────────────────────────────
def escape(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def render_sutra(sid, snum, prakrit, translation, commentary, simple, tags):
    tag_html = ''.join(f'<span class="concept-tag">{t}</span>' for t in tags)
    prak_escaped = prakrit.replace('\n', '<br/>')
    return f'''<article class="sutra-card p-8 rounded-xl mb-6 transition-all duration-300" id="{sid}">
<div class="flex items-start gap-6">
<span class="font-headline font-bold text-primary text-2xl flex-shrink-0 pt-1">{snum}</span>
<div class="space-y-4 flex-1">
<p class="sutra-sanskrit font-headline">{prak_escaped}</p>
<p class="text-lg font-semibold text-on-surface leading-relaxed">{translation}</p>
<p class="text-base text-on-surface-variant leading-relaxed">{commentary}</p>
<p class="simple-explanation"><b>The simple version:</b> {simple}</p>
<div class="concept-tags">{tag_html}</div>
</div>
</div>
</article>'''

def render_divider(text, divider_id=None):
    id_attr = f' id="{divider_id}"' if divider_id else ''
    return f'''<div class="section-divider"{id_attr}>
<span>{text}</span>
</div>'''

# ── Build sutra section HTML ──────────────────────────────────────────────────
sutra_html_parts = []
for entry in SUTRAS:
    sid, snum, *rest = entry
    num = int(snum.split('.')[1])
    if num in DIVIDERS:
        did = f'section-{num}'
        sutra_html_parts.append(render_divider(DIVIDERS[num], did))
    sutra_html_parts.append(render_sutra(sid, snum, *rest))
sutra_html = '\n'.join(sutra_html_parts)

# ── Full HTML ─────────────────────────────────────────────────────────────────
HTML = f'''<!DOCTYPE html>
<html class="light" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Uttaradhyayana Sutra Chapter 32: Pramādasthāna | JainAwaken.org</title>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&amp;family=Noto+Serif:ital,wght@0,400;0,700;1,400&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
  tailwind.config = {{
  darkMode: "class",
  theme: {{
    extend: {{
      colors: {{
        "on-tertiary-fixed-variant": "#35437e","on-secondary-fixed-variant": "#4a4642","secondary-container": "#e6ded9","primary-fixed-dim": "#e6c364","surface-bright": "#fef9f1","tertiary-fixed": "#dde1ff","surface": "#fef9f1","primary-fixed": "#ffe08f","surface-container-low": "#f8f3eb","secondary-fixed": "#e9e1dc","outline-variant": "#d0c5b2","outline": "#7e7665","inverse-on-surface": "#f5f0e8","on-background": "#1d1c17","on-secondary": "#ffffff","on-tertiary-container": "#2e3b77","error": "#ba1a1a","on-error": "#ffffff","on-primary-fixed-variant": "#584400","surface-dim": "#ded9d2","surface-container-high": "#ece8e0","primary": "#755b00","on-primary-container": "#503d00","inverse-surface": "#32302b","secondary": "#625d59","error-container": "#ffdad6","tertiary-fixed-dim": "#b9c3ff","on-secondary-container": "#67625e","on-primary": "#ffffff","on-primary-fixed": "#241a00","on-error-container": "#93000a","surface-tint": "#755b00","secondary-fixed-dim": "#ccc5c0","surface-variant": "#e7e2da","surface-container-lowest": "#ffffff","on-tertiary-fixed": "#041451","surface-container-highest": "#e7e2da","primary-container": "#c9a84c","inverse-primary": "#e6c364","on-surface-variant": "#4d4637","tertiary": "#4d5a98","background": "#fef9f1","on-tertiary": "#ffffff","on-surface": "#1d1c17","tertiary-container": "#9ba8eb","surface-container": "#f2ede5","on-secondary-fixed": "#1e1b18"
      }},
      fontFamily: {{ "headline": ["Noto Serif", "serif"], "body": ["Inter", "sans-serif"], "label": ["Inter", "sans-serif"] }},
      borderRadius: {{"DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem"}},
    }},
  }},
}}
</script>
<style>
   html {{ scroll-behavior: smooth; }}
.burnished-gradient {{ background: radial-gradient(circle at center, #755b00, #c9a84c); }}
.sutra-card {{ border: 1px solid rgba(201,168,76,0.25); border-left: 3px solid #c9a84c; background: white; }}
.sutra-sanskrit {{ font-size: 1.35rem; line-height: 2; color: #503d00; }}
.simple-explanation {{ margin-top: 1rem; padding-top: 1rem; border-top: 1px dashed rgba(201,168,76,0.3); font-family: 'Inter', sans-serif; font-size: 1.2rem; line-height: 1.85; color: #4d4637; }}
.sutra-card p.text-base {{ font-size: 1.2rem; line-height: 1.85; }}
.simple-explanation b {{ color: #1d1c17; font-weight: 600; }}
.sutra-card p.text-base {{ font-size: 1.2rem; line-height: 1.85; }}
.sutra-card p.text-lg {{ font-size: 1.2rem; line-height: 1.85; }}
.concept-tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 1rem; }}
.concept-tag {{ display: inline-block; border: 1px solid #C9A84C; background: transparent; color: #1d1c17; font-family: 'Inter', sans-serif; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; border-radius: 100px; padding: 4px 13px; font-weight: 500; }}
.nav-button {{ position: fixed; bottom: 24px; z-index: 100; background: transparent; border: 1px solid rgba(201,168,76,0.35); color: rgba(201,168,76,0.6); transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; transform: translateY(20px); }}
.nav-button.visible {{ opacity: 1; pointer-events: auto; transform: translateY(0); }}
.nav-button:hover {{ border-color: #C9A84C; color: #C9A84C; }}
.glass-nav {{ background: rgba(248, 247, 246, 0.85); backdrop-filter: blur(20px); }}
.section-divider {{ margin: 2rem 0 1.5rem; display: flex; align-items: center; gap: 1rem; }}
.section-divider span {{ font-family: 'Noto Serif', serif; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.2em; color: #755b00; font-weight: 600; white-space: nowrap; }}
.section-divider::before, .section-divider::after {{ content: ''; flex: 1; height: 1px; background: rgba(201,168,76,0.3); }}
.foundation-badge {{ display: inline-block; background: rgba(201,168,76,0.12); border: 1px solid rgba(201,168,76,0.35); color: #755b00; font-family: 'Inter', sans-serif; font-size: 10px; text-transform: uppercase; letter-spacing: 0.15em; border-radius: 4px; padding: 3px 10px; font-weight: 600; margin-top: 0.25rem; margin-bottom: 0.25rem; }}
@media (max-width: 768px) {{ .nav-button {{ bottom: 16px; }} .nav-button.left-btn {{ left: 12px !important; }} .nav-button.right-btn {{ right: 12px !important; }} .sutra-sanskrit {{ font-size: 1.15rem; }} }}

    #search-dropdown {{ position:absolute; top:calc(100% + 8px); left:0; min-width:400px; max-width:520px; background:#fff; border-radius:8px; box-shadow:0 8px 32px rgba(0,0,0,0.13); border:1px solid rgba(201,168,76,0.25); overflow:hidden; display:none; z-index:1000; max-height:420px; overflow-y:auto; }}
    .search-section-label {{ padding:8px 16px 4px; font-family:'Inter',sans-serif; font-size:9px; text-transform:uppercase; letter-spacing:0.12em; color:#C9A84C; font-weight:700; border-top:1px solid #f0ebe3; }}
    .search-section-label:first-child {{ border-top:none; }}
    .search-result-item {{ display:flex; align-items:baseline; gap:10px; padding:9px 16px; text-decoration:none; cursor:pointer; border:none; background:none; width:100%; text-align:left; transition:background 0.15s; }}
    .search-result-item:hover {{ background:#fef9f1; }}
    .search-result-num {{ font-family:'Noto Serif',serif; font-size:11px; color:#C9A84C; font-weight:700; flex-shrink:0; }}
    .search-result-title {{ font-family:'Inter',sans-serif; font-size:12px; color:#1d1c17; line-height:1.4; }}
    .search-no-results {{ padding:16px; color:#7e7665; font-family:'Inter',sans-serif; font-size:12px; text-align:center; }}

#breadcrumb {{ transition: opacity 0.4s ease, transform 0.4s ease; }}
.hero-primary-text {{ transition: color 0.5s ease; }}
.hero-primary-text:hover {{ color: #4d5a98 !important; }}
.nav-button:hover {{ border-color: #4d5a98 !important; color: #4d5a98 !important; }}
    #main-nav a {{ text-decoration: none; }}
    .nav-link {{ text-decoration: none; }}
</style>
</head>
<body class="text-on-surface font-body selection:bg-primary-container selection:text-on-primary-container bg-white">
<nav class="glass-nav fixed top-0 w-full z-50 transition-all duration-500 border-b border-[#C9A84C]/10" id="main-nav">
<div class="flex justify-between items-center px-6 md:px-12 py-5 max-w-screen-2xl mx-auto">
<div class="flex items-center gap-12">
<a href="../../../index-v4.html#hero">
<span class="text-2xl font-headline text-primary tracking-tighter font-bold">JainAwaken.org</span>
</a>
<div class="hidden md:flex gap-10 items-center font-headline tracking-[0.1em] uppercase text-xs font-semibold">
<a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../index-v4.html#foundations">Fundamentals</a>
<a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../fundamentals/navkar-mantra-v4.html">Navkar</a>
<a class="text-on-surface/80 hover:text-primary transition-colors duration-300" href="../../../fundamentals/meditations.html">Meditations</a>
<a class="text-primary font-semibold hover:text-primary transition-colors duration-300 underline underline-offset-4 decoration-primary/40" href="../aagama-index.html">Sacred Texts</a>
</div>
</div>
<div class="flex items-center gap-8">
<div class="relative group hidden lg:block">
<span class="nav-search-icon material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-outline text-sm transition-colors duration-500">search</span>
<input class="nav-search bg-surface-container-low border-none rounded-full py-2 pl-10 pr-6 text-sm font-label placeholder:italic transition-all duration-300 w-48 focus:w-72 focus:ring-1 focus:ring-primary/20" id="search-input" placeholder="Explore Wisdom..." type="text"/>
</div>
<a class="burnished-gradient text-on-primary px-8 py-2.5 rounded-full font-headline uppercase text-[10px] font-bold tracking-[0.2em] hover:opacity-90 transition-all shadow-sm" href="../../../fundamentals/donate-v4.html">Donate</a>
</div>
</div>
</nav>
<main class="pt-40">
<!-- Hero -->
<section class="max-w-screen-2xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-8 md:gap-16 items-center mb-40" id="hero">
<div class="col-span-12 lg:col-span-5 flex flex-col gap-10 order-2 lg:order-1">
<div id="breadcrumb" class="flex items-center gap-2 text-xs font-label text-outline uppercase tracking-widest">
<a href="../aagama-index.html" class="hover:text-primary transition-colors">Sacred Texts</a>
<span>·</span>
<a href="uttaradhyana-index.html" class="hover:text-primary transition-colors">Uttaradhyayana</a>
<span>·</span>
<span class="text-primary">Chapter 32</span>
</div>
<div class="flex flex-col gap-3">
<span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Uttaradhyayana Sutra · Chapter 32</span>
<h1 class="text-4xl md:text-5xl font-headline font-bold text-on-surface leading-tight tracking-tighter">
Stations of Negligence
<span class="block text-primary font-normal hero-primary-text">प्रमादस्थान</span>
</h1>
</div>
<h2 class="text-xl md:text-2xl font-headline text-on-surface-variant leading-relaxed font-light">
The Six Abodes of Spiritual Negligence — and How to Conquer Them
</h2>
<p class="text-xl text-on-surface-variant leading-relaxed opacity-90 max-w-lg font-light">
In this profound chapter, Lord Mahāvīra identifies the five sense organs and the mind as the six "stations of negligence" — the places where spiritual heedlessness takes hold. With systematic precision he shows how attachment and aversion arising through each sense organ generate the entire chain of suffering, and how complete equanimity and detachment lead to liberation in an instant.
</p>
</div>
<div class="col-span-12 lg:col-span-7 order-1 lg:order-2 flex flex-col items-center justify-center gap-0">
<div class="w-full max-w-2xl aspect-[4/3] rounded-xl overflow-hidden bg-surface-container flex items-center justify-center border border-outline-variant/30">
<img alt="Stations of Negligence" class="w-full h-full object-cover grayscale-[0.1] hover:grayscale-0 transition-all duration-1000" onerror="this.style.display=&apos;none&apos;; this.nextElementSibling.style.display=&apos;flex&apos;" src="../../../assets/ch32-hero.jpg"/>
<div class="hidden w-full h-full items-center justify-center flex-col gap-4 p-8">
<span class="font-headline text-5xl text-primary/30">🪷</span>
<p class="text-center font-headline text-on-surface/40 text-sm">Image: Stations of Negligence</p>
</div>
</div>
<div class="mt-8 text-center">
<p class="font-headline text-2xl md:text-3xl text-primary leading-relaxed">
अच्छंतकालस्स समूलगस्स,<br/>सव्वस्स दुक्खस्स उ जो पमोक्खो
</p>
<p class="mt-3 text-base text-on-surface-variant italic font-light leading-relaxed">
"Listen with complete attention to this singular beneficial teaching — the means for complete liberation from all suffering along with its roots, which has continued since beginningless time."
</p>
</div>
</div>
</section>
<!-- About -->
<section class="bg-[#f2f1f0] py-24 border-y border-primary/5">
<div class="max-w-screen-xl mx-auto px-6 md:px-12 grid grid-cols-12 gap-12 md:gap-20">
<div class="col-span-12 lg:col-span-4">
<span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">About This Chapter</span>
<h3 class="text-4xl font-headline font-bold text-on-surface leading-tight tracking-tight mt-4">Pramādasthāna</h3>
</div>
<div class="col-span-12 lg:col-span-8 space-y-6">
<p class="text-lg leading-relaxed text-on-surface-variant">
<span class="text-primary font-semibold">Pramādasthāna</span> — the thirty-second chapter — is the "Stations of Negligence." <em>Pramāda</em> means spiritual heedlessness or negligence; <em>sthāna</em> means station or abode. The chapter identifies the five sense organs (eye, ear, nose, tongue, skin) and the mind as the six stations where negligence habitually takes root — and systematically dismantles each one.
</p>
<p class="text-lg leading-relaxed text-on-surface-variant">
The chapter's architecture is one of the most systematic in the Uttaradhyayana Sūtra. After establishing the chain from delusion to craving to karma to suffering (sutras 1–8), and prescribing the means to destroy it (9–20), it generates a complete grid of sense-mastery: six sense organs × thirteen sutras each = 78 sutras of parallel teaching (21–99), culminating in a majestic nine-sutra conclusion on detachment and instantaneous liberation (100–108).
</p>
<div class="flex gap-8 items-center pt-4 flex-wrap">
<div class="flex flex-col gap-1">
<span class="text-3xl font-headline font-bold text-primary">108</span>
<span class="text-xs uppercase tracking-widest text-on-surface-variant font-semibold">Sutras</span>
</div>
<div class="w-px h-12 bg-outline-variant hidden md:block"></div>
<div class="flex flex-col gap-1">
<span class="text-3xl font-headline font-bold text-primary">6</span>
<span class="text-xs uppercase tracking-widest text-on-surface-variant font-semibold">Senses + Mind</span>
</div>
<div class="w-px h-12 bg-outline-variant hidden md:block"></div>
<div class="flex flex-col gap-1">
<span class="text-3xl font-headline font-bold text-primary">Moksha</span>
<span class="text-xs uppercase tracking-widest text-on-surface-variant font-semibold">Ultimate Goal</span>
</div>
</div>
<div class="pt-6 border-t border-outline-variant/40">
<p class="text-xs uppercase tracking-[0.15em] text-primary font-semibold font-label mb-4">Chapter Structure</p>
<div class="grid grid-cols-1 md:grid-cols-2 gap-3">
<div class="flex items-center gap-3">
<span class="w-7 h-7 rounded-full bg-surface-container flex items-center justify-center text-xs font-bold text-on-surface-variant font-label flex-shrink-0">I</span>
<span class="text-lg text-on-surface font-body">Eternal Happiness &amp; Solitary Wandering</span>
</div>
<div class="flex items-center gap-3">
<span class="w-7 h-7 rounded-full bg-surface-container flex items-center justify-center text-xs font-bold text-on-surface-variant font-label flex-shrink-0">II</span>
<span class="text-lg text-on-surface font-body">The Chain of Suffering — Origin &amp; Breaking</span>
</div>
<div class="flex items-center gap-3">
<span class="w-7 h-7 rounded-full bg-surface-container flex items-center justify-center text-xs font-bold text-on-surface-variant font-label flex-shrink-0">III</span>
<span class="text-lg text-on-surface font-body">Brahmacharya &amp; Renouncing Women's Company</span>
</div>
<div class="flex items-center gap-3">
<span class="w-7 h-7 rounded-full bg-surface-container flex items-center justify-center text-xs font-bold text-on-surface-variant font-label flex-shrink-0">IV</span>
<span class="text-lg text-on-surface font-body">Five-Sense Victory — Eye, Ear, Nose, Tongue, Touch</span>
</div>
<div class="flex items-center gap-3">
<span class="w-7 h-7 rounded-full bg-surface-container flex items-center justify-center text-xs font-bold text-on-surface-variant font-label flex-shrink-0">V</span>
<span class="text-lg text-on-surface font-body">Mind Victory — Mastery of Mental States</span>
</div>
<div class="flex items-center gap-3">
<span class="w-7 h-7 rounded-full bg-surface-container flex items-center justify-center text-xs font-bold text-on-surface-variant font-label flex-shrink-0">VI</span>
<span class="text-lg text-on-surface font-body">Detachment and Instantaneous Liberation</span>
</div>
</div>
</div>
</div>
</div>
</section>
<!-- Sutras -->
<section class="max-w-screen-xl mx-auto px-6 md:px-12 py-24">
<div class="mb-16">
<span class="text-primary font-headline italic tracking-[0.2em] text-sm uppercase font-semibold">Adhyayana 32</span>
<h3 class="text-5xl font-headline font-bold text-on-surface leading-tight tracking-tight mt-4">The 108 Sutras</h3>
<p class="text-lg text-on-surface-variant mt-4 max-w-2xl">Each sutra is presented with the original Prakrit, English translation, and a simplified commentary.</p>
</div>
{sutra_html}
</section>
</main>
<a class="nav-button left-btn flex items-center gap-3 px-4 py-2 rounded-lg font-headline font-bold text-xs tracking-wide" href="uttaradhyana-ch31.html" style="left:24px">
← Ch. 31
</a>
<a class="nav-button right-btn flex items-center gap-3 px-4 py-2 rounded-lg font-headline font-bold text-xs tracking-wide" href="uttaradhyana-ch33.html" style="right:24px">
Ch. 33 →
</a>
<script>
   window.addEventListener('scroll', () => {{
  const bc = document.getElementById('breadcrumb');
  const hero = document.querySelector('main > section');
  if (bc && hero) {{
    const past = window.scrollY > hero.offsetHeight * 0.75;
    bc.style.opacity = past ? '0' : '1';
    bc.style.transform = past ? 'translateY(-6px)' : 'translateY(0)';
    bc.style.pointerEvents = past ? 'none' : 'auto';
  }}
  const visible = window.scrollY > 300;
  document.querySelectorAll('.nav-button').forEach(b => b.classList.toggle('visible', visible));
}});
  </script>
<script>
(function () {{
  var SEARCH_INDEX = {search_index_json};
  function initSearch() {{
    var input = document.getElementById("search-input");
    if (!input) return;
    var wrapper = input.closest(".relative");
    if (!wrapper) return;
    var dropdown = document.getElementById("search-dropdown");
    if (!dropdown) {{
      dropdown = document.createElement("div");
      dropdown.id = "search-dropdown";
      wrapper.appendChild(dropdown);
    }}
    var currentFile = (location.pathname.split("/").pop() || location.href.split("/").pop() || "").replace(/[?#].*$/, "");
    function highlight(text, query) {{
      if (!query) return text;
      return text.replace(new RegExp("(" + query.replace(/[.*+?^${{}}()|[\\]\\\\]/g, "\\\\$&") + ")", "gi"), "<mark style='background:#fff3c4;color:inherit;border-radius:2px;'>$1</mark>");
    }}
    function search(query) {{
      if (query.length < 2) {{ dropdown.style.display = "none"; return; }}
      var q = query.toLowerCase();
      var currentMatches = [];
      var otherMatches = [];
      SEARCH_INDEX.forEach(function (chapter) {{
        var matches = (chapter.sutras || []).filter(function (s) {{
          return (s.title && s.title.toLowerCase().includes(q)) ||
                 (s.num && String(s.num).toLowerCase().includes(q)) ||
                 (chapter.title && chapter.title.toLowerCase().includes(q));
        }}).slice(0, 5);
        if (!matches.length) return;
        var isCurrent = chapter.file === currentFile;
        (isCurrent ? currentMatches : otherMatches).push({{ chapter: chapter, matches: matches }});
      }});
      var html = "";
      if (currentMatches.length) {{
        html += "<div class='search-section-label'>This Chapter</div>";
        currentMatches.forEach(function (r) {{
          r.matches.forEach(function (s) {{
            if (!s.id) return;
            html += "<button class='search-result-item' data-local='true' data-id='" + s.id + "'>"
                  + "<span class='search-result-num'>" + s.num + "</span>"
                  + "<span class='search-result-title'>" + highlight(s.title, query) + "</span></button>";
          }});
        }});
      }}
      otherMatches.slice(0, 8).forEach(function (r) {{
        html += "<div class='search-section-label'>" + r.chapter.title + "</div>";
        r.matches.forEach(function (s) {{
          var link = r.chapter.file + (s.id ? "#" + s.id : "");
          html += "<a class='search-result-item' href='" + link + "'>"
                + "<span class='search-result-num'>" + s.num + "</span>"
                + "<span class='search-result-title'>" + highlight(s.title, query) + "</span></a>";
        }});
      }});
      if (!html) html = "<div class='search-no-results'>No results for &ldquo;" + query + "&rdquo;</div>";
      dropdown.innerHTML = html;
      dropdown.style.display = "block";
      dropdown.querySelectorAll("[data-local='true']").forEach(function (btn) {{
        btn.addEventListener("click", function () {{
          var el = document.getElementById(this.dataset.id);
          if (el) {{
            el.scrollIntoView({{ behavior: "smooth", block: "center" }});
            el.style.outline = "2px solid #C9A84C";
            el.style.outlineOffset = "4px";
            setTimeout(function () {{ el.style.outline = ""; el.style.outlineOffset = ""; }}, 2000);
          }}
          dropdown.style.display = "none";
          input.value = "";
        }});
      }});
    }}
    input.addEventListener("input", function () {{ search(this.value.trim()); }});
    input.addEventListener("keydown", function (e) {{ if (e.key === "Escape") {{ dropdown.style.display = "none"; input.value = ""; }} }});
    document.addEventListener("click", function (e) {{ if (!wrapper.contains(e.target)) dropdown.style.display = "none"; }});
  }}
  document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", initSearch) : initSearch();
}})();
</script>
</body>
</html>'''

out = BASE / 'uttaradhyana-ch32.html'
out.write_text(HTML, encoding='utf-8')
print(f"Written: {out}")
print(f"File size: {out.stat().st_size:,} bytes")
print(f"Total sutras: {len(SUTRAS)}")
