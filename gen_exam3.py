import json, os

EXAM = {
    "id": "exam3",
    "title": "Practice Examination 3",
    "subtitle": "Studies of Religion",
    "essay_topic": "Abortion",
    "questions": [

        # ================= SECTION I (20 marks): Q1-11 =================
        {
            "id": "q1", "number": 1, "section": "I", "type": "mc", "marks": 1,
            "topic": "Long-run decline in Christian affiliation",
            "syllabusArea": "Changing patterns of religious adherence in Australia since 1945",
            "stimulus": {"type": "table",
                "headers": ["Year", "% identifying as Christian"],
                "rows": [["1947", "88%"], ["1976", "78%"], ["2001", "68%"], ["2021", "44%"]],
                "caption": "Indicative figures based on general Census trends."},
            "text": "Which of the following best accounts for the overall trend shown in the table, without overstating the evidence?",
            "options": [
                "Christianity has become entirely extinct in Australian religious life.",
                "A combination of secularisation, growth in 'No Religion' responses, and increased religious diversity through immigration has reduced Christianity's overall population share, even as it remains the largest single religious grouping.",
                "The government has legally reclassified Christian denominations as non-religious organisations.",
                "The decline is due solely to a decrease in the number of Christian church buildings available for worship."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This captures the genuinely multi-causal, non-absolute explanation consistent with the data.",
                "distractors": [
                    {"index": 0, "why": "An absurd overreach \u2014 44% is a decline in share, not extinction, and Christianity remains the largest single tradition."},
                    {"index": 2, "why": "Fabricates a legal reclassification that has never occurred."},
                    {"index": 3, "why": "Reduces a complex, multi-causal social trend to an implausible single physical-infrastructure cause."}
                ]
            }
        },
        {
            "id": "q2", "number": 2, "section": "I", "type": "mc", "marks": 1,
            "topic": "Refugee migration and Buddhism's growth",
            "syllabusArea": "Changing patterns of religious adherence in Australia since 1945",
            "stimulus": None,
            "text": "The significant growth of Buddhism as a religious tradition in Australia during the late 1970s and 1980s is most directly linked to:",
            "options": [
                "The abolition of Buddhist temples across Asia, forcing global migration to Australia.",
                "The arrival of refugees from Vietnam and other parts of Indo-China following the Vietnam War.",
                "A wave of religious conversion among Anglo-Australian Christians.",
                "Government-sponsored programs actively recruiting Buddhist migrants to fill labour shortages."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the standard, well-documented explanation for the scale of Buddhist population growth in this period.",
                "distractors": [
                    {"index": 0, "why": "Fabricates a cause with no historical basis."},
                    {"index": 2, "why": "A real but minor phenomenon \u2014 not the primary driver of growth at this scale."},
                    {"index": 3, "why": "Fabricates a specific government recruitment program that did not exist."}
                ]
            }
        },
        {
            "id": "q3", "number": 3, "section": "I", "type": "mc", "marks": 1,
            "topic": "Tolerance vs dialogue",
            "syllabusArea": "Responses to religious diversity in Australia since 1945",
            "stimulus": None,
            "text": "Within responses to religious diversity, which of the following best distinguishes 'tolerance' from 'dialogue' as levels of interfaith engagement?",
            "options": [
                "Tolerance requires active theological exchange between traditions, while dialogue requires only passive coexistence.",
                "Tolerance involves peaceful coexistence without necessarily requiring engagement, while dialogue involves active, ongoing communication and exchange of understanding between traditions.",
                "Tolerance and dialogue are identical concepts used interchangeably in the study of interfaith relations.",
                "Dialogue is a legal requirement in Australia, whereas tolerance is not recognised in any Australian legislation."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This correctly identifies dialogue as the more active, engaged level, distinct from mere tolerance.",
                "distractors": [
                    {"index": 0, "why": "Reverses the definitions of the two terms."},
                    {"index": 2, "why": "Falsely collapses two distinct concepts into one."},
                    {"index": 3, "why": "Fabricates a legal requirement that does not exist."}
                ]
            }
        },
        {
            "id": "q4", "number": 4, "section": "I", "type": "mc", "marks": 1,
            "topic": "Aboriginal spiritualities and reconciliation",
            "syllabusArea": "Contribution of Aboriginal spiritualities to the Australian religious landscape",
            "stimulus": None,
            "text": "Since 1945, the ongoing significance of the Dreaming for Aboriginal peoples has been increasingly acknowledged in Australian public life through:",
            "options": [
                "The complete conversion of all Aboriginal Australians to traditional pre-colonial spiritual practice, abandoning Christianity entirely.",
                "Public reconciliation initiatives, such as acknowledgement of country protocols and recognition of ongoing spiritual connection to land in national discussions including the Uluru Statement from the Heart (2017).",
                "A legal ban on any public reference to Aboriginal spirituality in government proceedings.",
                "The formal declaration of Aboriginal spiritualities as Australia's constitutionally established national religion."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This reflects genuine, documented public acknowledgement without overstating the situation.",
                "distractors": [
                    {"index": 0, "why": "Overreach \u2014 many Aboriginal Australians hold both Christian and traditional spiritual beliefs, rather than 'abandoning' one for the other."},
                    {"index": 2, "why": "The opposite has occurred \u2014 public acknowledgement has increased, not been banned."},
                    {"index": 3, "why": "Fabricated \u2014 Australia has no constitutionally established national religion of any kind."}
                ]
            }
        },
        {
            "id": "q5", "number": 5, "section": "I", "type": "mc", "marks": 1,
            "topic": "Contemporary religious freedom debate",
            "syllabusArea": "Impact of changing patterns of religious adherence on Australian society",
            "stimulus": None,
            "text": "The 2018 Religious Freedom Review (the 'Ruddock Review'), commissioned by the Australian Government, is best understood as evidence of:",
            "options": [
                "Australia's abandonment of any legal protections for religious belief.",
                "An ongoing public and political engagement with how increasing religious diversity intersects with existing law, particularly regarding freedom of religious belief and expression.",
                "The introduction of a single, uniform national religion in Australia.",
                "A legally binding requirement for all Australians to disclose their religious affiliation."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This accurately frames the review as part of continuing debate about religious diversity and law, not a radical departure.",
                "distractors": [
                    {"index": 0, "why": "The opposite is true \u2014 the review concerned strengthening or clarifying protections, not abandoning them."},
                    {"index": 2, "why": "Fabricated \u2014 no such outcome occurred."},
                    {"index": 3, "why": "Fabricated \u2014 no such requirement exists in Australian law."}
                ]
            }
        },
        {
            "id": "q6", "number": 6, "section": "I", "type": "mc", "marks": 1,
            "topic": "Lebanese migration and Islam's growth",
            "syllabusArea": "Changing patterns of religious adherence in Australia since 1945",
            "stimulus": None,
            "text": "Significant growth in Australia's Muslim population during the 1970s is most closely associated with:",
            "options": [
                "Migration from Lebanon, partly linked to the Lebanese Civil War (1975\u20131990).",
                "A large-scale conversion movement among Anglo-Australian Christians.",
                "Government legislation requiring increased Muslim migration quotas specifically.",
                "The complete cessation of migration from all non-Muslim-majority countries."
            ],
            "correctIndex": 0,
            "rationale": {
                "correct": "This is the standard, well-documented historical explanation for this specific wave of growth.",
                "distractors": [
                    {"index": 1, "why": "A real but minor phenomenon, not the primary driver of growth at this scale."},
                    {"index": 2, "why": "Fabricates a specific quota policy that did not exist."},
                    {"index": 3, "why": "Fabricated and illogical \u2014 migration from many countries continued throughout this period."}
                ]
            }
        },
        {
            "id": "q7", "number": 7, "section": "I", "type": "mc", "marks": 1,
            "topic": "Secularism vs secularisation",
            "syllabusArea": "Non-religious and religious expressions of spirituality",
            "stimulus": None,
            "text": "Which of the following best distinguishes 'secularism' from 'secularisation' in the context of Australian society since 1945?",
            "options": [
                "Secularism refers to a political and legal principle of separating religion from state institutions, while secularisation refers to the broader social process of declining religious authority and participation.",
                "Secularism and secularisation both refer exclusively to the legal separation of church and state, with no meaningful difference between them.",
                "Secularisation is a term used only in reference to government policy, while secularism refers only to individual belief.",
                "Secularism refers to the growth of religious diversity, while secularisation refers to the decline of religious diversity."
            ],
            "correctIndex": 0,
            "rationale": {
                "correct": "This is the standard, precise distinction between a legal/political principle and a broader social process.",
                "distractors": [
                    {"index": 1, "why": "Falsely collapses two distinct concepts into one."},
                    {"index": 2, "why": "Reverses and misapplies the scope of each term."},
                    {"index": 3, "why": "Both terms are misdefined; neither concerns religious diversity directly."}
                ]
            }
        },
        {
            "id": "q8", "number": 8, "section": "I", "type": "mc", "marks": 1,
            "topic": "Evaluating claims about interfaith tension",
            "syllabusArea": "Responses to religious diversity in Australia since 1945",
            "stimulus": {"type": "quote", "text": "The rise of religious diversity in Australia has had a uniformly positive effect on interfaith relations, with no significant tensions.", "attribution": "A student's claim (written for this examination)"},
            "text": "Which of the following would most directly challenge this student's claim?",
            "options": [
                "The existence of formal interfaith dialogue bodies such as the NCCA and APRO.",
                "Documented incidents of religiously motivated discrimination or social tension reported alongside efforts at interfaith cooperation.",
                "The overall increase in the number of religious traditions represented in Australia since 1945.",
                "Government funding for multicultural community events."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the only option that directly evidences tension, challenging the 'uniformly positive... no significant tensions' claim.",
                "distractors": [
                    {"index": 0, "why": "Describes a positive development consistent with the student's claim, rather than challenging it."},
                    {"index": 2, "why": "Describes diversity increasing, which does not by itself address the presence or absence of tension."},
                    {"index": 3, "why": "Describes a positive, supportive development rather than evidence of tension."}
                ]
            }
        },
        {
            "id": "q9", "number": 9, "section": "I", "type": "mc", "marks": 1,
            "topic": "Assimilation to multiculturalism",
            "syllabusArea": "Responses to religious diversity in Australia since 1945",
            "stimulus": None,
            "text": "Australian government policy toward migrant religious and cultural groups shifted significantly between the 1950s and the 1970s. This shift is best described as a movement from:",
            "options": [
                "Multiculturalism to assimilation.",
                "Assimilation (expecting migrants to adopt Anglo-Australian culture and religion) to multiculturalism (recognising and supporting cultural and religious diversity).",
                "A single unified national religion to religious pluralism enforced by international law.",
                "Compulsory religious conversion to compulsory secularism."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the accepted historical account of the policy shift across these decades.",
                "distractors": [
                    {"index": 0, "why": "Reverses the actual chronological direction of the policy shift."},
                    {"index": 2, "why": "Fabricates an 'international law' enforcement mechanism that does not exist."},
                    {"index": 3, "why": "Fabricates compulsion in both directions that does not reflect actual policy."}
                ]
            }
        },
        {
            "id": "q10", "number": 10, "section": "I", "type": "mc", "marks": 1,
            "topic": "Synthesis and historical generalisation",
            "syllabusArea": "Overview: adherence, diversity and responses since 1945",
            "stimulus": None,
            "text": "Which of the following is the most historically accurate generalisation about religion in Australia since 1945?",
            "options": [
                "Religious change in Australia has followed a single, simple trajectory from religious to non-religious.",
                "Religious change in Australia reflects multiple, sometimes overlapping trajectories: declining mainline Christian adherence, growing religious diversity through immigration, rising numbers reporting no religion, and evolving institutional responses such as multiculturalism and interfaith dialogue.",
                "Religious change in Australia has been driven entirely by government legislation rather than by demographic or social factors.",
                "Religious change in Australia since 1945 has had no discernible pattern and cannot be meaningfully generalised."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the only option that reflects the genuinely multi-threaded, evidence-based picture of religious change.",
                "distractors": [
                    {"index": 0, "why": "Oversimplifies a complex, multi-directional set of trends into a single false trajectory."},
                    {"index": 2, "why": "Overstates legislative causation, ignoring demographic and immigration drivers."},
                    {"index": 3, "why": "Denies any pattern exists, contradicted by substantial, well-documented trends."}
                ]
            }
        },
        {
            "id": "q11", "number": 11, "section": "I", "type": "written", "marks": 10,
            "topic": "Immigration and the establishment of minority traditions",
            "syllabusArea": "Impact of changing patterns of religious adherence on Australian society",
            "stimulus": {"type": "quote",
                "text": "We arrived with almost nothing after 1979. For the first ten years, we held ceremonies in a rented hall above a shop. Now there is a proper temple, and on Vesak our neighbours \u2014 Christian, Muslim, people of no religion \u2014 come to watch the lantern ceremony. My grandchildren speak more English than Vietnamese, but they still light incense. That, to me, is what survival looks like.",
                "attribution": "Extract from an oral history interview with a Buddhist community elder, 2020 (written for this examination)"},
            "text": "Using the source and your own knowledge, analyse the impact of post-1945 immigration on the establishment and adaptation of minority religious traditions in Australia. (10 marks)",
            "criteria": [
                "Accurately interprets the source: refugee settlement, gradual institution-building, and intergenerational adaptation alongside religious continuity.",
                "Links the source to specific immigration history (post-1975 Indo-Chinese refugee intake following the Vietnam War).",
                "Explains the broader pattern of institution-building nationally (temples, mosques, gurdwaras moving from informal to established premises).",
                "Explains the interfaith/multicultural dimension (neighbours of other or no religion attending Vesak as evidence of goodwill and coexistence).",
                "Discusses intergenerational change as a genuine nuance (language shift alongside retention of religious practice).",
                "Sustains an analytical, well-structured response integrating source and own knowledge throughout."
            ],
            "bandGuide": [
                {"range": "9\u201310", "label": "Sophisticated response integrating the source with detailed, accurate own knowledge across settlement, institution-building and intergenerational change."},
                {"range": "7\u20138", "label": "Sound response with good detail; may integrate source and own knowledge slightly less fully."},
                {"range": "5\u20136", "label": "Adequate but more general response; relies more heavily on the source than independent knowledge."},
                {"range": "1\u20134", "label": "Basic, list-like, or largely descriptive response with limited analysis."}
            ]
        },

        # ================= SECTION II (15 marks): Q12-14 — Judaism =================
        {
            "id": "q12", "number": 12, "section": "II", "type": "written", "marks": 5,
            "topic": "Significant person \u2014 Abraham",
            "syllabusArea": "Significant people in Judaism",
            "stimulus": None,
            "text": "Outline the significance of Abraham as a founding figure in Judaism. (5 marks)",
            "criteria": [
                "Identifies Abraham as the founding patriarch with whom God establishes the covenant (Brit).",
                "Refers to the covenant's key elements: promise of land and descendants, in exchange for faithfulness.",
                "Refers to Abraham as a model of faith and obedience, foundational to Jewish self-understanding as the covenant people.",
                "Explains his ongoing significance in Jewish liturgy and theology (e.g. reference in daily prayer such as the Amidah).",
                "Explains his significance as the first of the three patriarchs, foundational to Jewish identity as a people descended from him."
            ],
            "bandGuide": [
                {"range": "5", "label": "Accurate, well-developed outline covering the covenant, patriarchal status, and ongoing theological/liturgical significance."},
                {"range": "3\u20134", "label": "Accurate but partial outline; may describe the covenant without fully explaining its ongoing significance."},
                {"range": "1\u20132", "label": "Minimal or largely inaccurate detail."},
                {"range": "0", "label": "No relevant response."}
            ]
        },
        {
            "id": "q13", "number": 13, "section": "II", "type": "written", "marks": 5,
            "topic": "Ethical teaching and practice \u2014 Pikuach Nefesh",
            "syllabusArea": "Core ethical teachings and practices of Judaism",
            "stimulus": None,
            "text": "Explain how the ethical principle of Pikuach Nefesh (the preservation of life) is expressed through Jewish practice today. (5 marks)",
            "criteria": [
                "Defines Pikuach Nefesh accurately (the principle that preserving human life overrides almost all other commandments).",
                "Explains a specific practical expression (e.g. permission to break Shabbat restrictions, such as travelling or using a phone, to save a life or seek urgent medical care).",
                "Explains the broader ethical weight this principle gives to Jewish medical ethics and decision-making today.",
                "Gives a specific contemporary example (e.g. Jewish hospitals or medical ethics committees applying this principle).",
                "Uses accurate terminology and expresses a coherent explanatory chain from principle to practice."
            ],
            "bandGuide": [
                {"range": "5", "label": "Precise definition, a clear practical example, and explanation of its broader contemporary ethical significance."},
                {"range": "3\u20134", "label": "Sound explanation of the principle with at least one accurate practical example."},
                {"range": "1\u20132", "label": "States the principle but with little or no accurate practical application."},
                {"range": "0", "label": "No relevant response."}
            ]
        },
        {
            "id": "q14", "number": 14, "section": "II", "type": "written", "marks": 5,
            "topic": "Variants \u2014 Orthodox and Reform Judaism on intermarriage",
            "syllabusArea": "Variants within Judaism",
            "stimulus": {"type": "dual_quote", "quotes": [
                {"label": "Orthodox authority", "text": "Marriage is only recognised within the community when both partners are Jewish according to halakha; conversion, not accommodation, is the pathway for a non-Jewish partner."},
                {"label": "Reform authority", "text": "Many Reform communities today welcome interfaith families, recognising that exclusion risks losing families from Jewish life altogether, while still encouraging Jewish education and practice within the home."}
            ]},
            "text": "Using the sources and your own knowledge, evaluate the extent to which Orthodox and Reform Judaism differ in their approach to intermarriage. (5 marks)",
            "criteria": [
                "Accurately explains the Orthodox position: halakhic requirement for both partners to be Jewish, with conversion as the pathway.",
                "Accurately explains the Reform position: an inclusion-oriented, pastoral approach prioritising ongoing engagement with Jewish life.",
                "Evaluates the degree of difference: a shared underlying concern for Jewish continuity and identity, but differing strategies (boundary-maintenance vs inclusion).",
                "Reaches a reasoned, non-absolute conclusion rather than simply asserting the traditions are identical or entirely opposed.",
                "Integrates both sources explicitly rather than treating them as separate, unconnected quotes."
            ],
            "bandGuide": [
                {"range": "5", "label": "Sustained evaluation weighing a shared concern for continuity against genuinely different strategies, using both sources."},
                {"range": "3\u20134", "label": "Sound comparison of both positions but with a less developed or more asserted-than-argued evaluation."},
                {"range": "1\u20132", "label": "Describes one or both positions with little genuine evaluation of the extent of difference."},
                {"range": "0", "label": "No relevant response."}
            ]
        },

        # ================= SECTION III (15 marks): Q15 — Islamic Bioethics (Abortion) =================
        {
            "id": "q15", "number": 15, "section": "III", "type": "written", "marks": 15,
            "topic": "Bioethics \u2014 Abortion",
            "syllabusArea": "Islamic bioethics: abortion",
            "stimulus": None,
            "text": "Assess the significance of Islamic teachings in shaping adherents' responses to the issue of abortion, referring to relevant sources of authority and at least one contemporary case study. (15 marks)",
            "criteria": [
                "Explains the Qur'anic and Sharia principle of the sanctity of life as a foundation for the general prohibition of abortion.",
                "Explains the concept of ensoulment (ruh) and the commonly cited view that this occurs at a defined point after conception (traditionally around 120 days), which shapes distinctions in permissibility before and after this point.",
                "Explains variation between schools of law (madhhabs) \u2014 for example, relatively greater flexibility in the Hanafi school for permitting abortion before ensoulment under necessity, contrasted with generally stricter Maliki positions.",
                "References a contemporary source of authority, such as Islamic Fiqh Academy resolutions permitting therapeutic abortion in cases of serious threat to the mother's life or severe fetal abnormality, within defined limits.",
                "Incorporates a contemporary case study or example (e.g. debate over legal reform addressing abortion in cases of rape or fetal abnormality in a Muslim-majority context).",
                "Sustains an evaluative argument about the actual significance of these teachings in shaping real adherent decisions and legal frameworks, rather than simply listing positions."
            ],
            "bandGuide": [
                {"range": "12\u201315", "label": "Sophisticated, well-integrated response synthesising sanctity of life, ensoulment, madhhab variation, a named contemporary source of authority, and a case study, with sustained evaluation of significance."},
                {"range": "7\u201311", "label": "Sound response addressing several sources of authority accurately, but may lack full integration or a developed case study."},
                {"range": "1\u20136", "label": "Basic or generalised response; may name relevant terms without explaining or applying them."},
                {"range": "0", "label": "No relevant response."}
            ]
        }
    ]
}

out_path = os.path.join(os.path.dirname(__file__), "exam3.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(EXAM, f, ensure_ascii=False, indent=2)

print("Wrote", out_path, "-", len(EXAM["questions"]), "questions")
