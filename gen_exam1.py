import json, os

EXAM = {
    "id": "exam1",
    "title": "Practice Examination 1",
    "subtitle": "Studies of Religion",
    "essay_topic": "Genetic Engineering",
    "questions": [

        # ================= SECTION I (20 marks): Q1-11 =================
        {
            "id": "q1", "number": 1, "section": "I", "type": "mc", "marks": 1,
            "topic": "Intergenerational transmission of religious identity",
            "syllabusArea": "Changing patterns of religious adherence in Australia since 1945",
            "stimulus": {"type": "text", "text": "A 2019 survey found that among Australians raised in a religious household, only 46% still identified with that same religion by age 30, compared to 81% in 1966 (indicative figures)."},
            "text": "Which of the following best explains the trend shown above?",
            "options": [
                "Religious households have become less common since 1966.",
                "Declining intergenerational transmission of religious identity reflects broader patterns of secularisation, individual choice, and reduced institutional authority over personal belief.",
                "The survey proves that religious upbringing has no influence on adult belief whatsoever.",
                "All Australians raised religious now actively reject religion by adulthood."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This correctly links the statistic to well-documented sociological explanations for weakening transmission of religious identity across generations.",
                "distractors": [
                    {"index": 0, "why": "Addresses household prevalence, not the retention rate the statistic actually measures."},
                    {"index": 2, "why": "An overreach \u2014 46% retention still shows meaningful influence, not 'no influence whatsoever.'"},
                    {"index": 3, "why": "An overreach \u2014 46% still retain their upbringing's religion, so 'all' reject is false."}
                ]
            }
        },
        {
            "id": "q2", "number": 2, "section": "I", "type": "mc", "marks": 1,
            "topic": "Chaplaincy as an institutional response",
            "syllabusArea": "Impact of changing patterns of religious adherence on Australian society",
            "stimulus": None,
            "text": "Since 1945, one significant institutional response to Australia's changing religious landscape has been:",
            "options": [
                "The complete abolition of chaplaincy services in hospitals, prisons and schools.",
                "The expansion and diversification of chaplaincy services to include multi-faith provision, reflecting a more religiously diverse population.",
                "A legal requirement that all chaplains be ordained Anglican clergy.",
                "The replacement of all chaplaincy services with purely secular counselling, eliminating any religious component."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This accurately reflects the genuine, documented diversification of chaplaincy provision.",
                "distractors": [
                    {"index": 0, "why": "The opposite of what has occurred \u2014 chaplaincy services continue and have diversified."},
                    {"index": 2, "why": "Fabricates a legal requirement that does not exist."},
                    {"index": 3, "why": "An overreach \u2014 religious chaplaincy continues alongside, not replaced by, secular counselling options."}
                ]
            }
        },
        {
            "id": "q3", "number": 3, "section": "I", "type": "mc", "marks": 1,
            "topic": "Sikh community growth and visibility",
            "syllabusArea": "Changing patterns of religious adherence in Australia since 1945",
            "stimulus": None,
            "text": "The growing visibility of Sikh communities in Australia since the 1990s, including public Vaisakhi celebrations, is most directly linked to:",
            "options": [
                "Increased skilled and family migration from Punjab, India.",
                "A government program requiring Sikh migration to fill agricultural labour shortages exclusively.",
                "The complete disappearance of Sikh religious practice in India, forcing emigration.",
                "Conversion of Anglo-Australian Christians to Sikhism."
            ],
            "correctIndex": 0,
            "rationale": {
                "correct": "This is the well-documented, primary driver of this growth.",
                "distractors": [
                    {"index": 1, "why": "Fabricates a specific exclusive government program that did not exist."},
                    {"index": 2, "why": "A false premise \u2014 no such disappearance occurred."},
                    {"index": 3, "why": "A negligible phenomenon, not the primary or plausible driver of population-scale growth."}
                ]
            }
        },
        {
            "id": "q4", "number": 4, "section": "I", "type": "mc", "marks": 1,
            "topic": "The National Apology and Aboriginal spiritualities",
            "syllabusArea": "Contribution of Aboriginal spiritualities to the Australian religious landscape",
            "stimulus": None,
            "text": "The National Apology to the Stolen Generations (2008) is most relevant to the study of Aboriginal spiritualities because it:",
            "options": [
                "Legally reinstated pre-colonial Aboriginal law as the sole legal system in Australia.",
                "Publicly acknowledged historical harms, including disruption to spiritual and cultural connection to land and community caused by forced removal policies.",
                "Ended all Christian missionary activity among Aboriginal communities.",
                "Was primarily a statement about immigration policy."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This accurately reflects the Apology's acknowledgement of disrupted spiritual and cultural connection, which is directly relevant to this syllabus area.",
                "distractors": [
                    {"index": 0, "why": "Fabricates a legal outcome that did not occur."},
                    {"index": 2, "why": "Fabricated and false."},
                    {"index": 3, "why": "Misdirects to an entirely unrelated policy area."}
                ]
            }
        },
        {
            "id": "q5", "number": 5, "section": "I", "type": "mc", "marks": 1,
            "topic": "Civil religion",
            "syllabusArea": "Non-religious and religious expressions of spirituality",
            "stimulus": None,
            "text": "Sociologists sometimes describe rituals such as the Anzac Day dawn service as an expression of 'civil religion.' This term refers to:",
            "options": [
                "A formally organised religious denomination recognised by the Australian government.",
                "Shared, quasi-religious national rituals and symbols that foster collective identity and meaning, distinct from formal, organised religious traditions.",
                "A synonym for Christianity as practised in Australia.",
                "A legal requirement for all citizens to attend national ceremonies."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the standard sociological definition of civil religion as distinct from organised religious tradition.",
                "distractors": [
                    {"index": 0, "why": "Fabricates a formal status civil religion does not have."},
                    {"index": 2, "why": "Civil religion is explicitly distinguished from an organised tradition like Christianity, even where it borrows symbols."},
                    {"index": 3, "why": "Fabricates a legal attendance requirement that does not exist."}
                ]
            }
        },
        {
            "id": "q6", "number": 6, "section": "I", "type": "mc", "marks": 1,
            "topic": "Growth of independent congregations",
            "syllabusArea": "Changing patterns of religious adherence in Australia since 1945",
            "stimulus": None,
            "text": "The growth of independent, non-denominational Christian congregations in Australia since the 1980s is best explained by:",
            "options": [
                "A government ban on denominational Christianity.",
                "A preference among some adherents for congregations not formally affiliated with traditional denominational structures, often emphasising informal worship style and community.",
                "The complete disappearance of denominational Christianity.",
                "A legal requirement that new churches be non-denominational."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This reflects the genuine, documented preference driving this trend.",
                "distractors": [
                    {"index": 0, "why": "Fabricates a government ban that does not exist."},
                    {"index": 2, "why": "An overreach \u2014 denominational Christianity continues to exist alongside independent congregations."},
                    {"index": 3, "why": "Fabricates a legal requirement that does not exist."}
                ]
            }
        },
        {
            "id": "q7", "number": 7, "section": "I", "type": "mc", "marks": 1,
            "topic": "Pathways to religious identity: born-into vs conversion",
            "syllabusArea": "Non-religious and religious expressions of spirituality",
            "stimulus": None,
            "text": "When analysing religious adherence statistics, distinguishing between those 'born into' a tradition and those who 'convert' to it as adults is most useful for:",
            "options": [
                "Determining which religious tradition is 'true.'",
                "Understanding different pathways to religious identity and the different social and personal factors that shape belonging to a tradition.",
                "Proving that all religious identity in Australia is inherited rather than chosen.",
                "Establishing legal citizenship requirements based on religion."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the genuine sociological purpose of the distinction \u2014 understanding pathways to identity, not adjudicating theological truth.",
                "distractors": [
                    {"index": 0, "why": "A category error \u2014 sociological analysis does not adjudicate theological truth claims."},
                    {"index": 2, "why": "Self-contradicting \u2014 the very distinction being drawn shows both inherited and chosen pathways exist."},
                    {"index": 3, "why": "Fabricates an entirely unrelated legal claim."}
                ]
            }
        },
        {
            "id": "q8", "number": 8, "section": "I", "type": "mc", "marks": 1,
            "topic": "Multi-faith representation at public ceremonies",
            "syllabusArea": "Impact of changing patterns of religious adherence on Australian society",
            "stimulus": None,
            "text": "The inclusion of multi-faith prayers and representatives at public ceremonies such as Anzac Day services or state memorial events since the late 20th century reflects:",
            "options": [
                "A legal requirement under the Australian Constitution.",
                "An institutional response acknowledging Australia's increasing religious diversity within traditionally Christian-dominated public ritual.",
                "The complete removal of Christian content from all public ceremonies.",
                "A rejection of civic and national identity by religious minorities."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This accurately frames multi-faith inclusion as an institutional response to diversity, without overstating the change.",
                "distractors": [
                    {"index": 0, "why": "Fabricates a constitutional requirement that does not exist."},
                    {"index": 2, "why": "An overreach \u2014 Christian content typically continues alongside, not replaced by, multi-faith inclusion."},
                    {"index": 3, "why": "Illogical \u2014 participation in shared ceremonies reflects inclusion, not rejection, of civic identity."}
                ]
            }
        },
        {
            "id": "q9", "number": 9, "section": "I", "type": "mc", "marks": 1,
            "topic": "Evaluating claims about religion's public visibility",
            "syllabusArea": "Impact of changing patterns of religious adherence on Australian society",
            "stimulus": {"type": "quote", "text": "Because church attendance has declined, religion no longer has any visible presence in Australian public life.", "attribution": "A commentator (fictional, written for this examination)"},
            "text": "Which of the following most directly challenges this claim?",
            "options": [
                "The continued existence of religious buildings across Australia.",
                "The ongoing presence of multi-faith representation at major public ceremonies, religious voices in policy debate (e.g. the 2018 Religious Freedom Review), and visible religious institutions such as schools and chaplaincies.",
                "The historical fact that church attendance was higher in the past.",
                "The existence of the Australian Bureau of Statistics Census."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This directly demonstrates ongoing, active public visibility of religion, which is exactly what the claim denies.",
                "distractors": [
                    {"index": 0, "why": "A passive, static fact that does not directly demonstrate active public presence."},
                    {"index": 2, "why": "Confirms the premise (decline) rather than challenging the conclusion (no visible presence)."},
                    {"index": 3, "why": "Irrelevant to the question of public visibility."}
                ]
            }
        },
        {
            "id": "q10", "number": 10, "section": "I", "type": "mc", "marks": 1,
            "topic": "Synthesis: religion's ongoing significance in public life",
            "syllabusArea": "Overview: adherence, diversity and responses since 1945",
            "stimulus": None,
            "text": "Which of the following best evaluates the overall significance of religion in Australian public life since 1945, considering both decline and continuity?",
            "options": [
                "Religion has become entirely irrelevant to Australian public life.",
                "While formal religious authority and mainline Christian adherence have declined, religion continues to shape Australian public life through multiculturalism policy, interfaith and ecumenical engagement, Aboriginal spiritual traditions, and public ritual, alongside a growing non-religious and non-institutional cohort.",
                "Religion's significance in Australian public life has remained completely static since 1945.",
                "Religion's significance can only be measured through Census religious affiliation figures."
            ],
            "correctIndex": 1,
            "rationale": {
                "correct": "This is the only option that holds both decline and continuity together without an absolute overreach.",
                "distractors": [
                    {"index": 0, "why": "An absolute overreach not supported by the evidence."},
                    {"index": 2, "why": "An absolute overreach in the opposite direction, also unsupported."},
                    {"index": 3, "why": "Reductive \u2014 significance is also evidenced through policy, ceremony and institutions, not Census figures alone."}
                ]
            }
        },
        {
            "id": "q11", "number": 11, "section": "I", "type": "written", "marks": 10,
            "topic": "Interfaith cooperation and social cohesion",
            "syllabusArea": "Responses to religious diversity in Australia since 1945",
            "stimulus": {"type": "quote",
                "text": "During the bushfires, our mosque became a donation point for blankets and food, run jointly with the local Anglican parish and a Sikh gurdwara collective providing free meals to evacuees. Nobody asked what you believed before you were given a meal.",
                "attribution": "Extract from a community radio interview, 2020 (written for this examination)"},
            "text": "Using the source and your own knowledge, analyse the ways in which religious diversity has contributed to social cohesion in Australia since 1945. (10 marks)",
            "criteria": [
                "Accurately interprets the source: practical, unconditional interfaith solidarity and cooperation during a shared crisis.",
                "Links the source to the broader ecumenical and interfaith movement in Australia (e.g. bodies such as the NCCA and APRO).",
                "Notes that immigration-driven diversity itself provided the very institutions (mosque, gurdwara) now cooperating with longer-established Christian parishes.",
                "Explains the role of multicultural policy in supporting an environment where such cooperation can occur.",
                "Sustains an analytical, well-structured response using accurate terminology throughout."
            ],
            "bandGuide": [
                {"range": "9\u201310", "label": "Sophisticated response integrating the source with detailed, accurate own knowledge across multiple dimensions of cohesion."},
                {"range": "7\u20138", "label": "Sound response with good detail; may integrate source and own knowledge slightly less fully."},
                {"range": "5\u20136", "label": "Adequate but more general response; relies more heavily on the source than independent knowledge."},
                {"range": "1\u20134", "label": "Basic, list-like, or largely descriptive response with limited analysis."}
            ]
        },

        # ================= SECTION II (15 marks): Q12-14 — Judaism =================
        {
            "id": "q12", "number": 12, "section": "II", "type": "written", "marks": 5,
            "topic": "Significant person \u2014 Hillel the Elder",
            "syllabusArea": "Significant people in Judaism",
            "stimulus": None,
            "text": "Outline the significance of Hillel the Elder for the development of Jewish thought and practice. (5 marks)",
            "criteria": [
                "Identifies Hillel as an early rabbinic sage (active around the turn of the era).",
                "Refers to his founding of the House of Hillel, a major school of legal interpretation.",
                "Notes the contrast with the House of Shammai and how their debates shaped rabbinic methodology.",
                "Refers to his ethic of reciprocal, compassionate treatment of others as a foundational rabbinic teaching.",
                "Explains his ongoing significance for later halakhic methodology and Jewish thought."
            ],
            "bandGuide": [
                {"range": "5", "label": "Accurate, well-developed outline covering his school of interpretation, the contrast with Shammai, and his ethical teaching, with clear present-day relevance."},
                {"range": "3\u20134", "label": "Accurate but partial outline; may name Hillel's school without explaining its ongoing significance."},
                {"range": "1\u20132", "label": "Minimal or largely inaccurate detail."},
                {"range": "0", "label": "No relevant response."}
            ]
        },
        {
            "id": "q13", "number": 13, "section": "II", "type": "written", "marks": 5,
            "topic": "Ethical teaching and practice \u2014 Teshuvah and Yom Kippur",
            "syllabusArea": "Core ethical teachings and practices of Judaism",
            "stimulus": None,
            "text": "Explain how the concept of Teshuvah (repentance/return) is expressed through the observance of Yom Kippur. (5 marks)",
            "criteria": [
                "Defines Teshuvah accurately (sincere repentance and moral realignment, a 'turning back' toward God and right conduct).",
                "Defines Yom Kippur accurately (the Day of Atonement, involving fasting, prayer and communal confession).",
                "Explains the link: Yom Kippur provides a structured, annual communal practice for enacting Teshuvah.",
                "Notes the preparatory period (the Ten Days of Repentance between Rosh Hashanah and Yom Kippur).",
                "Gives a specific contemporary example (e.g. personal reconciliation with others before Yom Kippur, synagogue services)."
            ],
            "bandGuide": [
                {"range": "5", "label": "Precise definitions, a clear explanatory link, and a specific contemporary example."},
                {"range": "3\u20134", "label": "Sound explanation of both concepts with a link established, though example may be generic."},
                {"range": "1\u20132", "label": "Defines one concept accurately but the link to the other is weak or assumed rather than explained."},
                {"range": "0", "label": "No relevant response."}
            ]
        },
        {
            "id": "q14", "number": 14, "section": "II", "type": "written", "marks": 5,
            "topic": "Variants \u2014 Orthodox and Reform Judaism on gender and communal prayer",
            "syllabusArea": "Variants within Judaism",
            "stimulus": {"type": "dual_quote", "quotes": [
                {"label": "Orthodox authority", "text": "Separate seating (mechitza) during prayer preserves kavanah (spiritual focus) and reflects distinct, complementary roles for men and women in communal worship."},
                {"label": "Reform authority", "text": "Egalitarian seating and full participation of women in leading prayer reflects a core commitment to equality that we believe is consistent with, not opposed to, Jewish values."}
            ]},
            "text": "Using the sources and your own knowledge, evaluate the extent to which Orthodox and Reform Judaism differ in their approach to gender and communal prayer. (5 marks)",
            "criteria": [
                "Accurately explains the Orthodox rationale: mechitza, distinct roles, spiritual focus and tradition.",
                "Accurately explains the Reform rationale: egalitarianism and full participation of women in worship leadership.",
                "Evaluates the degree of difference: a shared value of meaningful, focused communal prayer, but a genuine difference in theology of gender roles and practice.",
                "Reaches a reasoned, non-absolute conclusion rather than simply asserting the traditions are identical or entirely opposed.",
                "Integrates both sources explicitly rather than treating them as separate, unconnected quotes."
            ],
            "bandGuide": [
                {"range": "5", "label": "Sustained evaluation weighing a shared value of focused prayer against genuine theological and structural differences, using both sources."},
                {"range": "3\u20134", "label": "Sound comparison of both positions but with a less developed or more asserted-than-argued evaluation."},
                {"range": "1\u20132", "label": "Describes one or both positions with little genuine evaluation of the extent of difference."},
                {"range": "0", "label": "No relevant response."}
            ]
        },

        # ================= SECTION III (15 marks): Q15 — Islamic Bioethics (Genetic Engineering) =================
        {
            "id": "q15", "number": 15, "section": "III", "type": "written", "marks": 15,
            "topic": "Bioethics \u2014 Genetic Engineering",
            "syllabusArea": "Islamic bioethics: genetic engineering",
            "stimulus": None,
            "text": "Assess the significance of Islamic teachings in shaping adherents' responses to the issue of genetic engineering, referring to relevant sources of authority and at least one contemporary case study. (15 marks)",
            "criteria": [
                "Explains the concept of khalifa (human stewardship/trusteeship over creation) as a basis for permitting beneficial scientific advancement.",
                "Explains the principle of maslaha (public interest/benefit) supporting therapeutic genetic interventions, such as gene therapy for treating disease.",
                "Explains caution or prohibition around non-therapeutic genetic modification, 'designer' enhancement, and human cloning, grounded in concerns about human dignity, altering God's creation, and preserving lineage (nasab).",
                "References a contemporary source of authority, such as Islamic Fiqh Academy (OIC) resolutions on genetic engineering and cloning, or relevant fatwas from recognised institutions.",
                "Distinguishes somatic gene therapy (generally more readily accepted) from germline or reproductive genetic modification (treated with far greater caution).",
                "Incorporates a contemporary case study or example, such as international fatwas issued in response to animal cloning (e.g. Dolly the sheep, 1996) or contemporary debate over CRISPR gene-editing technology.",
                "Sustains an evaluative argument about the actual significance of these teachings in shaping real practice, regulation and adherent decision-making, rather than simply listing rules."
            ],
            "bandGuide": [
                {"range": "12\u201315", "label": "Sophisticated, well-integrated response synthesising khalifa, maslaha, the somatic/germline distinction, a named contemporary source of authority, and a case study, with sustained evaluation of significance."},
                {"range": "7\u201311", "label": "Sound response addressing several sources of authority accurately, but may lack full integration or a developed case study."},
                {"range": "1\u20136", "label": "Basic or generalised response; may name relevant terms without explaining or applying them."},
                {"range": "0", "label": "No relevant response."}
            ]
        }
    ]
}

out_path = os.path.join(os.path.dirname(__file__), "exam1.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(EXAM, f, ensure_ascii=False, indent=2)

print("Wrote", out_path, "-", len(EXAM["questions"]), "questions")
