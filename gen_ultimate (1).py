import json, os

def mc(number, cluster, topic, text, options, correctIndex, correct_why, distractor_whys, stimulus=None):
    return {
        "id": f"u{number}", "number": number, "section": "I", "type": "mc", "marks": 1,
        "topic": topic, "syllabusArea": cluster, "stimulus": stimulus, "text": text,
        "options": options, "correctIndex": correctIndex,
        "rationale": {
            "correct": correct_why,
            "distractors": [{"index": i, "why": w} for i, w in distractor_whys]
        }
    }

CLUSTERS = [
    "Cluster 1: Changing Patterns of Religious Adherence (Statistics & Trends)",
    "Cluster 2: Causes \u2014 Immigration & Policy Change",
    "Cluster 3: Aboriginal Spiritualities & Their Contribution",
    "Cluster 4: Ecumenism & Interfaith Dialogue",
    "Cluster 5: Secularism, Non-Religion & Expressions of Spirituality",
    "Cluster 6: Synthesis, Evaluation & Impact on Australian Society",
]

QUESTIONS = []

# ---------------- CLUSTER 1 (Q1-5): Statistics & Trends ----------------
QUESTIONS.append(mc(1, CLUSTERS[0], "Reading a three-category trend table",
    "Which conclusion is best supported by the data above?",
    [
        'By 2021, "No Religion" had become the single largest category, overtaking Christianity.',
        'Since 1966, Australia has experienced simultaneous decline in Christian affiliation and growth in both non-religious identification and religious diversity.',
        "The data proves that religious belief has disappeared entirely from Australian society.",
        '"Other religions" grew faster than "No Religion" between 1966 and 2021 in percentage-point terms.'
    ], 1,
    "This is the only option that reflects the co-occurring trends shown without misreading the actual figures.",
    [(0, "A base-rate trap: at 44% vs 39% in this illustrative data, Christianity is still narrowly larger \u2014 the percentage GROWTH of 'No Religion' does not mean it has overtaken Christianity in size."),
     (2, "An absolute overreach the data does not support."),
     (3, '"No Religion" grew by roughly 38 percentage points versus roughly 9 for "Other religions" in this data \u2014 the reverse of what this option claims.')],
    stimulus={"type": "table", "headers": ["Category", "1966", "2021"],
        "rows": [["Christian", "~88%", "~44%"], ["No Religion", "~0.8%", "~39%"], ["Other religions", "~0.7%", "~10%"]],
        "caption": "Indicative figures based on general Census trends."}
))

QUESTIONS.append(mc(2, CLUSTERS[0], "Nominal vs practising adherence",
    "This distinction is most useful for explaining which apparent inconsistency in Australian religious statistics?",
    [
        "Why the number of people identifying as Christian in the Census remains higher than the number who regularly attend church services.",
        "Why immigration figures do not match Census religious affiliation figures.",
        "Why the Census undercounts the total Australian population.",
        "Why Aboriginal spiritualities are not included as a Census category."
    ], 0,
    "The nominal/practising distinction directly explains the gap between stated affiliation and actual attendance.",
    [(1, "Addresses a different, unrelated inconsistency."), (2, "Unrelated to this distinction."), (3, "Unrelated to this distinction \u2014 also factually questionable, since Census data can be cross-analysed by Indigenous status and religion.")],
    stimulus={"type": "text", "text": "Sociologists distinguish between 'nominal' and 'practising' religious adherents in analysing Census data."}
))

QUESTIONS.append(mc(3, CLUSTERS[0], "Largest denomination vs declining share",
    "This statement illustrates which important distinction in analysing Australia's religious statistics?",
    [
        "The difference between relative size (largest denomination) and proportional decline (a smaller share of the total population).",
        "The difference between Catholicism and Christianity as separate, unrelated religious traditions.",
        "The difference between Census data and government policy data, calculated using entirely different methods.",
        "The difference between Catholic immigrants and Catholic-born Australians, which cannot be measured in any Census."
    ], 0,
    "The statement is precisely an example of a group remaining largest in relative terms while declining in proportional terms.",
    [(1, "False \u2014 Catholicism is a Christian denomination, not a separate tradition."), (2, "Fabricates an irrelevant methodological distinction."), (3, "Fabricates an impossibility; this is not the distinction the statement illustrates.")],
    stimulus={"type": "text", "text": "Since the 1980s, Catholicism has remained Australia's largest single Christian denomination, though its share of the overall population has also declined."}
))

QUESTIONS.append(mc(4, CLUSTERS[0], "Avoiding overgeneralisation about regional patterns",
    "Which explanation is most consistent with sociological understanding of this pattern, while avoiding overgeneralisation?",
    [
        "Rural Australians are inherently more intelligent and therefore more likely to hold religious beliefs.",
        "A combination of demographic factors (age profile, education, migration patterns) differing between metropolitan and regional areas likely contributes to this pattern, rather than a single simple cause.",
        "Regional areas have banned the Census category of 'No Religion.'",
        "This pattern proves that all rural Australians attend church weekly."
    ], 1,
    "This is the only option that offers a multi-causal, evidence-consistent explanation without stereotyping either group.",
    [(0, "An offensive, unsupported causal claim with no evidentiary basis."), (2, "Fabricates an impossible restriction \u2014 Census categories are uniform nationally."), (3, "An unsupported overreach not implied by the pattern.")],
    stimulus={"type": "text", "text": "Census data consistently shows higher rates of 'No Religion' responses in inner-metropolitan areas compared to outer-regional and rural areas of Australia."}
))

QUESTIONS.append(mc(5, CLUSTERS[0], "Identifying a limitation in a media claim",
    "Which of the following most directly identifies a limitation in the headline's reasoning?",
    [
        "The headline ignores that 'No Religion' growth occurs alongside continued religious diversity and a continued (if narrowly) larger Christian population, meaning the overall picture is more complex than simple 'death' of religion.",
        "The headline is correct because 'No Religion' is now the single most common Census response of any kind.",
        "The headline cannot be evaluated because Census data is entirely unreliable.",
        "The headline actually understates the decline, since religious affiliation has fallen to zero percent."
    ], 0,
    "This correctly identifies the headline's oversimplification without overcorrecting into an opposite false claim.",
    [(1, "As of the most recent Census, Christianity still narrowly exceeds 'No Religion' \u2014 this option asserts something not currently accurate."), (2, "An overreach that dismisses the data entirely rather than identifying a specific limitation."), (3, "An absurd, factually false claim.")],
    stimulus={"type": "text", "text": "A newspaper headline reads: 'Religion in Australia is Dying,' citing the rise in 'No Religion' Census responses as its only evidence."}
))

# ---------------- CLUSTER 2 (Q6-10): Immigration & Policy Change ----------------
QUESTIONS.append(mc(6, CLUSTERS[1], "Legislative end of the White Australia Policy",
    "The formal end of the White Australia Policy is most closely associated with which piece of Australian legislation/policy action?",
    [
        "The Migration Act amendments of 1966 and the Racial Discrimination Act 1975, which progressively dismantled race-based immigration restrictions.",
        "The Australian Constitution of 1901, which explicitly prohibited non-British migration from its inception.",
        "The 1967 Referendum, which was primarily concerned with immigration policy rather than Indigenous citizenship.",
        "The Multicultural Australia Act of 1955, which first introduced non-discriminatory immigration."
    ], 0,
    "This correctly identifies the actual, gradual legislative process that dismantled the White Australia Policy.",
    [(1, "Mischaracterises the Constitution's role and effect."), (2, "The 1967 Referendum concerned Indigenous citizenship and Census counting, not immigration policy \u2014 a frequently confused fact."), (3, "Fabricates an Act that does not exist.")]
))

QUESTIONS.append(mc(7, CLUSTERS[1], "Refugee waves and specific traditions",
    "This wave of migration most directly contributed to growth in which religious tradition(s) in Australia?",
    [
        "Judaism and Sikhism",
        "Buddhism, alongside smaller growth in Vietnamese Catholic communities",
        "Hinduism exclusively",
        "Islam exclusively"
    ], 1,
    "Vietnamese migration included a Buddhist majority alongside a significant Catholic minority reflecting Vietnam's colonial religious history \u2014 the only option capturing this accurately.",
    [(0, "Unrelated traditions to this specific migration wave."), (2, "Excludes the correct traditions and misattributes this wave to an unrelated group."), (3, "Excludes the correct traditions and misattributes this wave to an unrelated group.")],
    stimulus={"type": "text", "text": "Between 1975 and 1985, Australia accepted a significant number of refugees from Vietnam, Cambodia and Laos."}
))

QUESTIONS.append(mc(8, CLUSTERS[1], "Skilled migration and South Asian traditions",
    "Since the 1990s, growth in Australia's Hindu and Sikh populations has been most closely linked to:",
    [
        "Migration and skilled visa pathways from India and Punjab.",
        "A large-scale religious conversion movement among Anglo-Australian Christians.",
        "Government-mandated resettlement quotas specifically for Hindu and Sikh refugees.",
        "The abolition of religious practice in India, forcing mass emigration."
    ], 0,
    "This is the well-documented, primary driver of this growth.",
    [(1, "A negligible phenomenon, not the primary driver of this scale of growth."), (2, "Fabricates a specific quota policy."), (3, "Fabricates a false premise \u2014 no such abolition occurred.")]
))

QUESTIONS.append(mc(9, CLUSTERS[1], "Immigration policy and religious diversity overall",
    "Which of the following most accurately describes the relationship between immigration policy and religious diversity in Australia since 1945?",
    [
        "Religious diversity increased only after 1945 because before this date Australia had no immigration at all.",
        "Immigration policy changes, particularly the shift from restrictive, race-based selection to a non-discriminatory points-based system, progressively enabled increased religious diversity from a broader range of source countries.",
        "Religious diversity has decreased since 1945 due to tightening immigration restrictions.",
        "Immigration policy has had no measurable effect on Australia's religious composition since 1945."
    ], 1,
    "This is the accurate, evidence-based account of the relationship between policy change and diversity.",
    [(0, "False premise \u2014 Australia had immigration before 1945, though heavily restricted and racially selective."), (2, "Reverses the actual trend \u2014 diversity increased, not decreased."), (3, "Contradicted by extensive evidence.")]
))

QUESTIONS.append(mc(10, CLUSTERS[1], "Evaluating a claim about legal vs political causes",
    "Which piece of evidence would most directly challenge this student's claim?",
    [
        "The existence of the Migration Act 1958.",
        "Specific refugee intakes (e.g. post-Vietnam War Indo-Chinese refugees, and later arrivals fleeing conflicts in the Middle East) that were directly triggered by global political events, not simply by legal policy change alone.",
        "The continued existence of religious diversity in Australia today.",
        "The declining share of Christian adherents recorded in the Census."
    ], 1,
    "This directly demonstrates that political events, not law alone, drove specific migration waves \u2014 challenging the student's 'purely legal' claim.",
    [(0, "A legal fact that does not address the role of global political events, so it does not challenge the claim."), (2, "Irrelevant to the specific causal claim being made."), (3, "A true but irrelevant fact that does not address the mechanism in question.")],
    stimulus={"type": "text", "text": "A student writes: 'Because Australia's immigration policy became non-discriminatory after 1973, religious diversity increased purely as a matter of law, with no role played by global political events.'"}
))

# ---------------- CLUSTER 3 (Q11-15): Aboriginal Spiritualities ----------------
QUESTIONS.append(mc(11, CLUSTERS[2], "Nature of the Dreaming",
    "Central to Aboriginal spirituality, the Dreaming (or Dreamtime) is best understood as:",
    [
        "A historical period that ended with British colonisation in 1788.",
        "An ongoing, living reality that connects Aboriginal peoples to land, ancestral beings, law and identity, rather than a fixed event confined to the past.",
        "A single, universal creation myth identical across all Aboriginal nations.",
        "A term used only in a secular, cultural sense with no spiritual dimension."
    ], 1,
    "This reflects the accurate, syllabus-consistent understanding of the Dreaming as ongoing and living.",
    [(0, "A very common misconception \u2014 treats the Dreaming as strictly historical, contradicting its ongoing nature."), (2, "False \u2014 there is enormous diversity across hundreds of distinct Aboriginal nations and language groups."), (3, "False \u2014 denies its central spiritual dimension entirely.")]
))

QUESTIONS.append(mc(12, CLUSTERS[2], "Inculturation in Christian ministries",
    "This development is best interpreted as evidence of:",
    [
        "The complete replacement of Christianity by Aboriginal spirituality within these communities.",
        "A form of inculturation, in which Aboriginal spiritual concepts and symbols are integrated within a Christian framework, reflecting the ongoing significance of Aboriginal spirituality for many Aboriginal Christians.",
        "A government requirement that all Christian churches include Aboriginal content.",
        "A rejection of Christian doctrine by Aboriginal-led ministries."
    ], 1,
    "This accurately names the process of integrating Aboriginal spirituality within Christian practice, rather than replacement or rejection.",
    [(0, "Overstates the relationship as replacement rather than integration."), (2, "Fabricates a government mandate."), (3, "Overstates the relationship as rejection rather than integration.")],
    stimulus={"type": "text", "text": "Since the 1970s, some Christian denominations in Australia have developed Aboriginal-led ministries and liturgical practices that incorporate Aboriginal symbols and spirituality."}
))

QUESTIONS.append(mc(13, CLUSTERS[2], "The Uluru Statement from the Heart",
    "The Uluru Statement from the Heart (2017) is most relevant to the study of Aboriginal spiritualities in Australia because it:",
    [
        "Formally established Aboriginal spiritualities as a legally recognised state religion.",
        "Articulated a connection between spiritual relationship to land and calls for constitutional recognition and political voice.",
        "Ended all forms of Aboriginal spiritual practice in favour of a single national Indigenous church.",
        "Was primarily a document about immigration policy reform."
    ], 1,
    "This correctly identifies the Statement's articulation of spiritual connection to land alongside its political and constitutional dimension.",
    [(0, "Fabricates a legal outcome that did not occur."), (2, "Absurd and false."), (3, "Misdirects to an entirely unrelated policy area.")]
))

QUESTIONS.append(mc(14, CLUSTERS[2], "Sacred sites vs institutional places of worship",
    "Which of the following most accurately distinguishes the concept of 'sacred sites' in Aboriginal spirituality from the concept of a 'church' or 'place of worship' in institutional religions?",
    [
        "Sacred sites are exclusively man-made structures, whereas churches are always natural landmarks.",
        "Sacred sites are typically tied to specific, often continuous connections with the Dreaming embedded in the natural landscape itself, whereas institutional places of worship are generally purpose-built structures separate from the surrounding landscape's inherent meaning.",
        "Sacred sites and churches serve identical religious functions with no meaningful conceptual difference.",
        "Sacred sites are legally classified as churches under Australian law."
    ], 1,
    "This correctly captures the genuine conceptual distinction between landscape-embedded sacred meaning and purpose-built worship structures.",
    [(0, "Reverses the actual, typical pattern for each concept."), (2, "Falsely collapses a genuine conceptual distinction."), (3, "Fabricates a legal classification that does not exist.")]
))

QUESTIONS.append(mc(15, CLUSTERS[2], "Challenging a claim about disappearance",
    "Which of the following most directly challenges this commentator's reasoning?",
    [
        "The Census does not ask detailed questions about spiritual practice beyond formal religious affiliation, and many Aboriginal Australians who identify as Christian also maintain an ongoing connection to Dreaming-based spirituality, land, and ceremony alongside their Christian identity.",
        "The commentator's claim is correct because Census self-identification is always a complete and accurate measure of spiritual practice.",
        "Aboriginal spiritualities cannot be discussed in relation to Census data at all.",
        "All Aboriginal Australians reject Christianity entirely, which disproves the commentator's premise."
    ], 0,
    "This directly challenges the claim by identifying the limits of Census data and the genuine coexistence of Christian identity with ongoing traditional spirituality.",
    [(1, "Endorses rather than challenges the flawed premise."), (2, "An overreach that avoids engaging with the claim."), (3, "Factually false \u2014 the majority of Aboriginal Australians do identify as Christian in the Census, making this an inaccurate overcorrection.")],
    stimulus={"type": "text", "text": "A commentator argues: 'Because most Aboriginal Australians identify as Christian in the Census, traditional Aboriginal spiritualities have effectively disappeared from contemporary Australian life.'"}
))

# ---------------- CLUSTER 4 (Q16-20): Ecumenism & Interfaith Dialogue ----------------
QUESTIONS.append(mc(16, CLUSTERS[3], "Defining ecumenism",
    "Which of the following best defines 'ecumenism' as it applies to religious life in Australia since 1945?",
    [
        "The pursuit of unity and cooperation among different Christian denominations.",
        "The pursuit of unity among all world religions regardless of tradition.",
        "A legally binding merger of all Christian churches into one organisation.",
        "The rejection of denominational identity altogether in favour of secularism."
    ], 0,
    "This is the standard, precise definition of ecumenism as intra-Christian cooperation.",
    [(1, "Confuses ecumenism with interfaith dialogue."), (2, "Fabricates a legal merger that has never occurred."), (3, "Unrelated and false \u2014 ecumenism does not involve secularism.")]
))

QUESTIONS.append(mc(17, CLUSTERS[3], "Gradual development of ecumenical cooperation",
    "This history is best used as evidence for which point about the ecumenical movement in Australia?",
    [
        "Ecumenical cooperation has been immediate, complete, and without historical development or change over time.",
        "Ecumenical cooperation has developed gradually, with the scope of denominational participation changing and expanding over time.",
        "The Catholic Church has never participated in any form of ecumenical activity in Australia.",
        "The ecumenical movement was established as a direct response to the 1967 Referendum."
    ], 1,
    "This is directly supported by the stimulus, which describes gradual, changing participation over decades.",
    [(0, "Directly contradicted by the stimulus, which shows gradual change over time."), (2, "Directly contradicted by the stimulus, which describes eventual full Catholic membership."), (3, "Fabricates an unrelated causal/chronological link.")],
    stimulus={"type": "text", "text": "Formed in 1946, the Australian Council of Churches (predecessor to today's National Council of Churches in Australia) brought together a range of Protestant and Orthodox denominations, with the Catholic Church joining fully as a member only decades later."}
))

QUESTIONS.append(mc(18, CLUSTERS[3], "Interfaith dialogue vs ecumenism",
    "Interfaith dialogue in Australia differs from ecumenism most significantly in that it:",
    [
        "Involves engagement between entirely distinct religious traditions, rather than cooperation within a single tradition.",
        "Is legally regulated in a way ecumenism is not.",
        "Focuses only on shared meals and social events with no discussion of belief.",
        "Has completely replaced ecumenism as the dominant form of religious cooperation since 2000."
    ], 0,
    "This correctly names the key distinguishing feature: cross-tradition engagement versus intra-Christian cooperation.",
    [(1, "Fabricates a legal distinction that does not exist."), (2, "Trivialises and misdescribes the substantive nature of interfaith dialogue."), (3, "An overreach \u2014 ecumenism continues to operate alongside interfaith dialogue.")]
))

QUESTIONS.append(mc(19, CLUSTERS[3], "Countering a claim of symbolic ineffectiveness",
    "Which of the following would most directly counter this criticism?",
    [
        "The number of religious traditions represented at an interfaith event.",
        "Documented instances where interfaith consultation directly informed specific government policies, such as anti-discrimination protections or multicultural service provision.",
        "The frequency with which interfaith events are reported in the media.",
        "The personal religious beliefs of individual dialogue participants."
    ], 1,
    "This is the only option that demonstrates concrete policy impact, directly countering the 'merely symbolic' criticism.",
    [(0, "Describes scale of participation, not concrete impact."), (2, "Describes media coverage, not concrete impact."), (3, "Irrelevant to institutional or policy impact.")],
    stimulus={"type": "text", "text": "Some critics argue that interfaith dialogue initiatives in Australia are largely symbolic and produce little concrete social change."}
))

QUESTIONS.append(mc(20, CLUSTERS[3], "Synthesising ecumenism and interfaith dialogue",
    "Considering both ecumenism and interfaith dialogue together, which statement best captures their combined significance in Australia since 1945?",
    [
        "Both movements have been entirely ineffective and have had no impact on Australian religious or social life.",
        "Both movements represent distinct but related responses to increasing complexity in Australia's religious landscape \u2014 one addressing division within Christianity, the other addressing relationships across different religious traditions \u2014 together contributing to social cohesion.",
        "Ecumenism has replaced interfaith dialogue entirely, making the latter unnecessary today.",
        "Interfaith dialogue emerged only because ecumenism had already completely failed."
    ], 1,
    "This is the only option that accurately captures both movements as distinct, related and ongoing.",
    [(0, "Contradicted by evidence of policy and social influence."), (2, "False \u2014 both continue to operate distinctly today."), (3, "Fabricates a false causal claim based on a false premise.")]
))

# ---------------- CLUSTER 5 (Q21-25): Secularism, Non-Religion & Spirituality ----------------
QUESTIONS.append(mc(21, CLUSTERS[4], "Secularism vs atheism",
    "Which of the following best defines 'secularism' as distinct from 'atheism'?",
    [
        "Secularism is the belief that no god exists, while atheism is a political principle of separating religion from government.",
        "Secularism is a principle concerning the relationship between religious institutions and the state, while atheism is a personal belief position denying the existence of god(s).",
        "Secularism and atheism are identical terms that can always be used interchangeably.",
        "Secularism refers only to Christian denominations, while atheism refers only to non-Christian religions."
    ], 1,
    "This is the precise, standard distinction between a political/legal principle and a personal belief position.",
    [(0, "Reverses the two definitions."), (2, "Falsely collapses two distinct concepts."), (3, "Both terms are entirely misdefined and irrelevant to religious traditions.")]
))

QUESTIONS.append(mc(22, CLUSTERS[4], "Private spirituality without institutional affiliation",
    "This pattern is most usefully explained using which sociological concept?",
    [
        "Ecumenism",
        "The distinction between institutional religious affiliation and personal/private spirituality (e.g. 'believing without belonging' or non-institutional spirituality)",
        "Denominational switching",
        "The White Australia Policy"
    ], 1,
    "This is the only concept that directly explains private spiritual belief or practice without formal religious affiliation.",
    [(0, "A real syllabus concept, but concerns Christian denominational cooperation, not this pattern."), (2, "A real syllabus concept, but concerns movement between denominations, not this pattern."), (3, "A real syllabus concept, but concerns immigration policy, not this pattern.")],
    stimulus={"type": "text", "text": "Some Australians who report 'No Religion' in the Census nonetheless report engaging in practices such as meditation, mindfulness, or belief in a 'higher power' or 'spirit' without formal religious affiliation."}
))

QUESTIONS.append(mc(23, CLUSTERS[4], "New Age practices as non-institutional spirituality",
    "The growth of 'New Age' practices such as yoga, astrology and alternative healing in Australia since the 1960s and 70s is best understood as:",
    [
        "Evidence that Eastern religious traditions such as Hinduism and Buddhism have become the dominant religions of Australia.",
        "An example of non-institutional spirituality, often blending elements from multiple traditions without requiring formal religious affiliation or membership.",
        "A government-sponsored cultural program with no connection to personal belief.",
        "A phenomenon entirely unrelated to broader changes in Australia's religious landscape since 1945."
    ], 1,
    "This correctly identifies New Age practice as a form of non-institutional, blended spirituality.",
    [(0, "Overreach \u2014 borrowing elements from these traditions does not make them 'dominant.'"), (2, "Fabricates a government sponsorship link."), (3, "False \u2014 it is directly connected to broader secularisation and pluralisation trends.")]
))

QUESTIONS.append(mc(24, CLUSTERS[4], "Secularisation as a broader process",
    "Which of the following best distinguishes 'secularisation' (a social process) from the simple numerical growth of the 'No Religion' Census category?",
    [
        "They are identical; the Census figure is a complete and sufficient measure of secularisation.",
        "Secularisation is a broader theoretical concept describing declining social significance and authority of religious institutions, of which Census 'No Religion' figures are one piece of evidence among several.",
        "Secularisation refers only to government policy, while the Census figure refers only to individual belief, with no overlap between the two.",
        "The Census figure is a religious concept, while secularisation is a purely legal one."
    ], 1,
    "This correctly frames secularisation as the broader concept, with the Census figure as one indicator among several.",
    [(0, "Oversimplifies a multidimensional concept to a single statistic."), (2, "Draws a false dichotomy that mischaracterises both terms."), (3, "Both terms are mischaracterised.")]
))

QUESTIONS.append(mc(25, CLUSTERS[4], "Challenging an overreaching claim about rationality",
    "Which piece of evidence most directly undermines this commentator's reasoning?",
    [
        "Evidence that many Australians who select 'No Religion' continue to report belief in a spirit, higher power, or engage in non-institutional spiritual practices.",
        "The overall increase in the raw number of people selecting 'No Religion' between Census years.",
        "The decline in weekly church attendance among Christian denominations.",
        "The growth in the number of religious traditions represented in Australia."
    ], 0,
    "This directly shows that many 'No Religion' respondents retain spiritual beliefs, undermining the claim that they have rejected 'all forms' of such belief.",
    [(1, "True but does not address the specific overreach about rejecting all spiritual belief."), (2, "True but does not address the specific overreach about rejecting all spiritual belief."), (3, "True but does not address the specific overreach about rejecting all spiritual belief.")],
    stimulus={"type": "text", "text": "A commentator claims: 'The rise of \"No Religion\" responses proves that Australians have become entirely rational and rejected all forms of supernatural or spiritual belief.'"}
))

# ---------------- CLUSTER 6 (Q26-30): Synthesis, Evaluation & Impact ----------------
QUESTIONS.append(mc(26, CLUSTERS[5], "Religious diversity and national identity",
    "Which of the following best evaluates the overall relationship between religious diversity and Australian national identity since 1945?",
    [
        "Religious diversity has completely dissolved any coherent sense of Australian national identity.",
        "Religious diversity has become one important element within an evolving, multicultural conception of Australian identity, alongside continuing debate about its place in public life.",
        "Australian national identity has remained entirely unchanged by religious diversity since 1945.",
        "Religious diversity has been legally excluded from any official definition of Australian identity."
    ], 1,
    "This is the only balanced, evidence-consistent evaluation that avoids absolute claims.",
    [(0, "An absolute overreach not supported by evidence."), (2, "An absolute overreach in the opposite direction, also unsupported."), (3, "Fabricates a legal exclusion that does not exist.")]
))

QUESTIONS.append(mc(27, CLUSTERS[5], "Challenging a claim of unrelated trends",
    "Which of the following most directly challenges this view?",
    [
        "Both trends occurred in the same broad post-1945 period, sharing common underlying social contexts such as urbanisation, secularisation, and changing immigration policy, even though their specific causes differ.",
        "Mainline Christian decline caused all subsequent immigration to Australia.",
        "Religious diversity through immigration directly caused the decline of mainline Christian denominations.",
        "The two trends cannot be discussed together under any circumstances."
    ], 0,
    "This directly challenges the 'unconnected' claim by showing shared social context, without overstating direct causation in either direction.",
    [(1, "Asserts a false, overly strong causal claim not supported by evidence."), (2, "Asserts a false, overly strong causal claim not supported by evidence."), (3, "Overreaches in the opposite direction, refusing any connection at all.")],
    stimulus={"type": "text", "text": "A historian argues that 'the decline of mainline Christian denominations' and 'the rise of religious diversity through immigration' are best understood as two separate, unconnected phenomena."}
))

QUESTIONS.append(mc(28, CLUSTERS[5], "Evaluating the effectiveness of Australia's responses",
    "Considering the syllabus topic as a whole, which of the following best describes the relationship between Australia's response to religious diversity and its effectiveness in maintaining social cohesion?",
    [
        "These responses have been entirely and uniformly successful, eliminating all religious tension in Australia.",
        "These responses have made a significant, if partial and ongoing, contribution to social cohesion, coexisting with continuing challenges and debates.",
        "These responses have had no effect whatsoever on Australian social cohesion.",
        "These responses were abandoned after the 1970s and no longer exist today."
    ], 1,
    "This is the only balanced, evidence-consistent evaluation that avoids absolute claims.",
    [(0, "An absolute overreach not supported by evidence."), (2, "Contradicted by extensive evidence of policy and social impact."), (3, "Factually false \u2014 such responses continue today.")]
))

QUESTIONS.append(mc(29, CLUSTERS[5], "Identifying the central argument of a synthesis extract",
    "Which of the following best captures the central argument of this extract?",
    [
        "Religion in Australia since 1945 is best understood through a single dominant trend of decline.",
        "Religion in Australia since 1945 is best understood as a set of interconnected, coexisting trends \u2014 denominational decline, immigration-driven diversity, Aboriginal spiritual continuity, and rising non-affiliation \u2014 rather than any single narrative.",
        "Religion in Australia since 1945 has been defined solely by conflict between different religious traditions.",
        "Religion in Australia since 1945 can only be understood by focusing exclusively on Aboriginal spiritualities."
    ], 1,
    "This directly reflects the extract's framing of multiple threads held together at once.",
    [(0, "Reduces the extract's multi-threaded argument to a single trend, contradicted by the text."), (2, "Introduces a conflict framing entirely absent from the extract."), (3, "Overreaches into an exclusive focus the extract does not support.")],
    stimulus={"type": "quote",
        "text": "To understand religion in Australia since 1945, one must hold together several threads at once: the steady thinning of mainline Christian congregations; the arrival, generation after generation, of new communities bringing Buddhist, Hindu, Muslim, Sikh and Jewish life to Australian cities and towns; the quiet but significant persistence of Aboriginal spiritual traditions, sometimes within and sometimes alongside Christian practice; and, running through all of this, an increasingly visible cohort who claim no religion at all, even as many of them continue to search for meaning in their own way.",
        "attribution": "Extract from an academic commentary, 2020 (written for this examination)"}
))

QUESTIONS.append(mc(30, CLUSTERS[5], "Final synthesis: the most defensible overall conclusion",
    "Which of the following is the most defensible overall conclusion about religion and belief systems in Australia since 1945, consistent with the evidence typically presented in this topic?",
    [
        "Australia has undergone a simple, linear process of becoming entirely non-religious.",
        "Australia has undergone a complex process involving simultaneous decline in some traditional forms of Christian adherence, substantial growth in religious diversity through immigration, ongoing significance of Aboriginal spiritualities, growth in both institutional and non-institutional forms of spirituality, and evolving social and political responses aimed at maintaining cohesion amid this diversity.",
        "Australia's religious landscape has remained essentially unchanged since 1945, with only minor statistical fluctuations.",
        "All change in Australia's religious landscape since 1945 can be attributed to a single cause: immigration policy."
    ], 1,
    "This is the only conclusion that reflects the full, multi-causal, multi-threaded picture built throughout the topic.",
    [(0, "An oversimplified, false single-trajectory claim."), (2, "Contradicted by extensive evidence of substantial change."), (3, "Reduces a multi-causal picture to a single cause, ignoring secularisation and generational change.")]
))

EXAM = {
    "id": "ultimate",
    "title": "Ultimate Multiple Choice Paper",
    "subtitle": "Section I only \u2014 Religion in Australia Post 1945",
    "essay_topic": None,
    "clusters": CLUSTERS,
    "questions": QUESTIONS
}

out_path = os.path.join(os.path.dirname(__file__), "ultimate.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(EXAM, f, ensure_ascii=False, indent=2)

print("Wrote", out_path, "-", len(EXAM["questions"]), "questions")
