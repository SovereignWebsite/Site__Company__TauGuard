"""Builds the live pages (design 1) into site/. Run from the repository root: python3 -I docs/build/build.py"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
from css1 import CSS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def write(path, content):
    p = os.path.join(ROOT, "site", path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "site", "index.html")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(content)


def prop(*lines):
    return '<div class="prop-box"><p>' + PROPOSAL + " " + lines[0] + "</p>" + "".join(f"<p>{l}</p>" for l in lines[1:]) + "</div>"


# ====================================================== HOME
def home():
    s = Svg(900, 420, "TauGuard's governance core and RiskMandate's ABP on either side of one execution boundary",
            "On the left, TauGuard: advisory intelligence proposes, a deterministic governance core evaluates, and a decision of approve, review or block is made. On the right, RiskMandate: an agent behaviour policy records reach, mandate, the gap between them, and the barrier. Both meet at the execution boundary in the middle.")
    s.zone(10, 10, 400, 370, "TAUGUARD: what may happen")
    s.box(40, 46, 340, 64, ["Advisory intelligence"], cls="n", size=15, sub=["LLMs, ML, retrieval propose"])
    s.box(40, 150, 340, 64, ["Deterministic governance core"], cls="tg", size=15, sub=["purpose, authority, rules, admissibility"])
    s.box(40, 254, 340, 64, ["Decision"], cls="rv", size=15, sub=["APPROVE, REVIEW or BLOCK"])
    s.arrow(210, 112, 210, 148); s.arrow(210, 216, 210, 252)
    s.arrow(382, 286, 444, 286)
    s.zone(490, 10, 400, 370, "RISKMANDATE: what each agent may do")
    s.box(520, 46, 340, 50, ["Reach"], cls="rm", size=15, sub=["what the agent can actually do"])
    s.box(520, 118, 340, 50, ["Mandate"], cls="rm", size=15, sub=["what it was authorised to do"])
    s.box(520, 190, 340, 50, ["Gap"], cls="rm", size=15, sub=["the difference between the two"])
    s.box(520, 262, 340, 56, ["Barrier"], cls="rm", size=15, sub=["rule, review or technical control"])
    for y in (96, 168, 240): s.arrow(690, y + 2, 690, y + 20)
    s.arrow(518, 290, 456, 290)
    s.line(450, 24, 450, 372)
    s.text(450, 402, "EXECUTION BOUNDARY: consequence-bearing action sits behind it", 13, "middle", "b")
    body = f"""<h1>Two companies, one boundary</h1>
<p class="lede">TauGuard governs what may happen. RiskMandate writes down what each agent may do, and puts something in the way of the gap. Both are about the same place: the line between an agent's intent and its consequence.</p>
{s.render("TauGuard's governance core and RiskMandate's agent behaviour policy (ABP) either side of the same execution boundary. The drawing is ours; the terms are theirs.")}
<div class="grid">
<div class="card tg"><span class="tag tgt">TauGuard</span><h2>Governs what may happen</h2>
<p>TauGuard says: "Intelligence may propose. Deterministic governance evaluates admissibility. Execution occurs only when the governing conditions are satisfied."</p>{cite('governance')}</div>
<div class="card rm"><span class="tag rmt">RiskMandate</span><h2>Writes down what each agent may do</h2>
<p>RiskMandate says it can "tell you what each one can actually do, write down what you authorised it to do, and put something in the way of the difference."</p>{rcite(RM, 'riskmandate.ai')}</div>
</div>
<h2>Where to go</h2>
<ul>
<li><a href="/tauguard/">What TauGuard builds</a>: one company, several systems that are not one product.</li>
<li><a href="/architecture/">Their architecture, drawn</a>: the governance flow, ARCHONT's layers, TauMesh, TauDIL.</li>
<li><a href="/riskmandate/">RiskMandate</a>: the ABP, hooks, the SHarness boundary, and the summit figures with what was not done.</li>
<li><a href="/together/">Side by side</a>: five places the two meet.</li>
<li><a href="/workflows/">Four joint workflows</a> and <a href="/mvp/">a two-way MVP</a>, all proposals.</li>
<li><a href="/next/">What next</a>: TauGuard's own path, and where we could fit.</li>
</ul>
<p>The design of this site is not final: see the <a href="/designs/">design directions</a>.</p>"""
    return page("/", "", "A Sovereign Website proposal: what TauGuard builds, its architecture drawn, and how TauGuard and RiskMandate could work together.", body, mark="A proposal about TauGuard")


# ====================================================== TAUGUARD
def tauguard():
    s = Svg(900, 360, "TauGuard: one company, several systems, with the frameworks shown apart",
            "TauGuard Limited at the top. Below it four systems: ARCHONT GOS, TauDIL GOS with SYGON integrated, ROD which is in development, and IEL Guard. Separately, the five frameworks IFA, SFA, GFA, AGL and ALA, which TauGuard says are distinct from its products.")
    s.box(300, 10, 300, 44, ["TauGuard Limited"], cls="tg", size=15, sub=["the company"])
    xs = [10, 232, 454, 676]
    names = [(["ARCHONT GOS"], ["organisational state", "and change"], "tg"), (["TauDIL GOS"], ["intelligence governance", "SYGON integrated"], "tg"),
             (["ROD"], ["gamified PC security", "in development"], "n"), (["IEL Guard"], ["provable constraints", "on its own page"], "n")]
    for x, (a, b, c) in zip(xs, names):
        s.box(x, 100, 214, 84, a, cls=c, size=15, sub=b)
        s.arrow(x + 107, 84, x + 107, 98)
    s.line(117, 84, 783, 84, "dash"); s.line(450, 56, 450, 84, "dash")
    s.zone(10, 214, 880, 136, "FRAMEWORKS: shown apart from the systems, as TauGuard shows them")
    fx = [22, 196, 370, 544, 718]
    fn = [("IFA", "Intelligence From", "Architecture"), ("SFA", "Security From", "Architecture"), ("GFA", "Governance From", "Architecture"),
          ("AGL", "Authority Governed", "Learning"), ("ALA", "Admissible Learning", "Architecture")]
    for x, (a, b, c) in zip(fx, fn):
        s.box(x, 248, 160, 80, [a], cls="n", size=15, sub=[b, c])
    body = f"""<h1>What TauGuard builds</h1>
<p class="lede">One company, several systems that are not one product. Everything on this page is TauGuard's own description, read on {READ}, with the page it came from.</p>
{s.render("TauGuard's company, systems and frameworks as its public pages arrange them. Our drawing.")}
<h2>One company, multiple architectures</h2>
<p>TauGuard says it is "the company", and that its systems "are not interchangeable implementations of one product": "ARCHONT GOS and TauDIL GOS are separate products. TauDIL GOS is not a renamed ARCHONT GOS component, and ARCHONT GOS is not a replacement for TauDIL GOS."</p>{cite('systems')}
<div class="grid">
<div class="card tg"><h3>ARCHONT GOS</h3>
<p>A Governance Operating System for organisational state and change. TauGuard says it maintains "the governed relationship between purpose, authority, meaning, canonical knowledge, rules, evidence, dependencies, assessments, current state and operational consequence". It includes TauMesh and TauStamp.</p>{cite('archon')}</div>
<div class="card tg"><h3>TauDIL GOS</h3>
<p>A separate Governance Operating System for intelligent systems and intelligence-producing processes: deterministic intelligence governance, semantic coherence and semantic drift, "with SYGON integrated into the architecture".</p>{cite('taudil')}</div>
<div class="card tg"><h3>SYGON</h3>
<p>Described as a semantic governance layer that does not generate the answer. TauGuard's line: "When AI does not know, it should know not to invent." Its four steps: ground, context, evaluate, decide (allow or refuse).</p>{cite('sygon')}</div>
<div class="card"><h3>ROD</h3>
<p>Gamified PC security "designed to make protective behaviour visible, understandable and engaging". TauGuard says: "The system is under development." We say no more than that.</p>{cite('rod')}</div>
<div class="card"><h3>IEL Guard</h3>
<p>TauGuard's page says IEL Guard "enforces AI behavioral constraints with cryptographic proof", in three steps: define invariants, enforce on every action, anchor proof on-chain. The page states "100% action coverage" and "under 1ms enforcement latency" as figures; we have not tested either. TauGuard's own systems overview lists three systems and links IEL from its menu, so we show it as a fourth item and say so.</p>{cite('iel')}</div>
</div>
<h2>Frameworks, shown apart</h2>
<p>TauGuard says the frameworks "are distinct from TauGuard products. A framework establishes a research or architectural model; a system implements capabilities for a particular governed environment." It lists five: IFA (Intelligence From Architecture), SFA (Security From Architecture), GFA (Governance From Architecture), AGL (Authority Governed Learning) and ALA (Admissible Learning Architecture).</p>{cite('frameworks')}
<p>Its governance page also names GOM (Governance of Meaning), GUD (Governance Under Degradation) and TauMesh (topological governance) as "governance extensions".</p>{cite('governance')}
<p>IFA is published as "Core Specification v1.0".</p>{cite('ifa')}
<h2>What we have not said</h2>
<p>We name nobody at TauGuard. We use no TauGuard logo or branding. Where TauGuard states a number, we repeat it as its claim, not as something we checked.</p>"""
    return page("/tauguard/", "What TauGuard builds", "One company, several systems that are not one product: ARCHONT GOS, TauDIL GOS with SYGON, ROD and IEL Guard, with the frameworks shown apart.", body, mark="TauGuard")


# ====================================================== ARCHITECTURE
def architecture():
    # a) governance flow
    a = Svg(900, 220, "TauGuard's governance flow", "Six steps: input, meaning, evaluation, admissibility, decision, chronicle. The decision step has three outcomes: approve, review or block.")
    names = ["Input", "Meaning", "Evaluation", "Admissibility", "Decision", "Chronicle"]
    cl = {4: "rv", 5: "ok"}
    for i, nme in enumerate(names):
        x = 10 + i * 148
        a.box(x, 12, 124, 62, [nme], cls=cl.get(i, "tg"), size=14, sub=[f"step {i + 1}"])
        if i < 5: a.arrow(x + 126, 43, x + 146, 43)
    a.box(560, 138, 100, 46, ["APPROVE"], cls="ok", size=14); a.box(670, 138, 100, 46, ["REVIEW"], cls="rv", size=14); a.box(780, 138, 100, 46, ["BLOCK"], cls="wn", size=14)
    a.path("M 602 76 L 602 100 L 610 100 L 610 136"); a.path("M 602 100 L 720 100 L 720 136"); a.path("M 602 100 L 830 100 L 830 136")
    a.text(10, 125, "All required predicates satisfied: APPROVE.", 12); a.text(10, 145, "Constitutional conditions need governed human authority: REVIEW.", 12)
    a.text(10, 165, "Admissibility absent or a refusal condition triggered: BLOCK.", 12)
    a.text(10, 200, "Evidence and lineage are committed to the Chronicle.", 12)
    # b) three bands
    b = Svg(900, 330, "Advisory intelligence, deterministic governance core, execution boundary",
            "Three bands. Advisory intelligence (LLMs, ML, retrieval, recommendations) passes evidence and proposals down to the deterministic governance core, which passes a governed decision down to the execution boundary, where consequence-bearing operations happen.")
    b.box(10, 10, 880, 80, ["Advisory intelligence"], cls="n", size=16, sub=["LLMs, ML, retrieval, recommendations: they may propose"])
    b.box(10, 125, 880, 80, ["Deterministic governance core"], cls="tg", size=16, sub=["purpose, authority, rules, context, canonical knowledge, admissibility"])
    b.box(10, 240, 880, 80, ["Execution boundary"], cls="wn", size=16, sub=["consequence-bearing operation: if admissibility cannot be shown, it does not occur"])
    b.arrow(450, 92, 450, 123); b.arrow(450, 207, 450, 238)
    b.text(462, 112, "evidence / proposal", 12); b.text(462, 227, "governed decision", 12)
    # c) ARCHONT
    c = Svg(900, 400, "ARCHONT GOS: six layers and the execution seam",
            "Six layers from constitutional foundation to governance memory, with TauStamp. A vertical execution seam separates ARCHONT from operational reality: ERP, MES, AI systems, APIs, machines and human workflows.")
    layers = [("01 Constitutional foundation", "purpose, constraints, principles"), ("02 Authority and knowledge", "who may act, what governs, what supports"),
              ("03 Governed state", "current condition, not only history"), ("04 Dependency topology", "how a local change can propagate"),
              ("05 Standing and consequence", "what remains admissible now"), ("06 Governance memory", "TauStamp preserves lineage")]
    for i, (t, sub) in enumerate(layers):
        c.box(10, 10 + i * 62, 440, 52, [t], cls="tg" if i < 5 else "ok", size=14, sub=[sub])
        if i < 5: c.arrow(230, 63 + i * 62, 230, 71 + i * 62)
    c.line(520, 10, 520, 380, "bd"); c.text(520, 396, "EXECUTION SEAM", 13, "middle", "b")
    c.arrow(452, 288, 516, 288); c.arrow(524, 288, 588, 288)
    c.zone(590, 10, 300, 370, "OPERATIONAL REALITY")
    for i, t in enumerate(["ERP", "MES", "AI systems", "APIs", "Machines", "Human workflows"]):
        c.box(620, 40 + i * 54, 240, 42, [t], cls="n", size=14)
    # d) TauMesh
    d = Svg(900, 250, "TauMesh: five deltas and the change lifecycle",
            "Five delta dimensions: state, rule, evidence, dependency and version. Below, the lifecycle: change, delta, impact, invalidation, re-evaluation, new standing.")
    d.zone(6, 6, 888, 96, "TAUMESH: FIVE DELTAS")
    for i, t in enumerate(["Delta_state", "Delta_rule", "Delta_evidence", "Delta_dependency", "Delta_version"]):
        d.box(20 + i * 174, 40, 160, 46, [t], cls="tg", size=14)
    d.zone(6, 118, 888, 124, "CHANGE LIFECYCLE")
    for i, t in enumerate(["Change", "Delta", "Impact", "Invalidation", "Re-evaluation", "New Standing"]):
        d.box(20 + i * 144, 156, 118, 56, [t], cls="ok" if i == 5 else "n", size=14)
        if i < 5: d.arrow(140 + i * 144, 184, 162 + i * 144, 184)
    # e) TauDIL
    e = flow("TauDIL GOS: intelligence governance flow", "Intelligence input, then semantic coherence, then SYGON, then semantic drift.",
             [["Intelligence input", "~signals, context,", "~model output"], ["Semantic coherence", "~does meaning stay", "~inside governed bounds"], ["SYGON", "~integrated semantic", "~governance capability"], ["Semantic drift", "~meaningful movement", "~from governed state"]],
             cls_for={1: "tg", 2: "tg", 3: "rv"}, h=120)
    f7 = Svg(900, 440, "IFA's seven-layer constitutional stack", "Seven layers, top to bottom: probabilistic intelligence systems, semantic governance with SYGON, admissibility verification with AGL, a deterministic rule engine, execution authorisation with IEL, an immutable chronicle layer, and the IFA constitutional core.")
    lay = [("1 Probabilistic intelligence systems", "LLMs, ML models, autonomous agents", "n"), ("2 Semantic governance layer", "SYGON: coherence, drift, knowledge integrity", "tg"),
           ("3 Admissibility verification", "AGL: ALLOW, RESTRICT, DEFER or BLOCK", "tg"), ("4 Deterministic rule engine", "assessment rules and AI governance rules", "tg"),
           ("5 Execution authorisation", "IEL: authority chains, Merkle proof", "wn"), ("6 Immutable chronicle layer", "append-only, tamper-evident record", "ok"),
           ("7 Constitutional core", "IFA: the invariant foundation", "ok")]
    for i, (t, sub, col) in enumerate(lay):
        f7.box(10, 8 + i * 61, 880, 50, [t], cls=col, size=14, sub=[sub])
        if i < 6: f7.arrow(450, 59 + i * 61, 450, 68 + i * 61)
    body = f"""<h1>Their architecture, drawn</h1>
<p class="lede">Six of TauGuard's own designs as diagrams. The words in the boxes are theirs; the drawings are ours, so check each against its source before relying on it.</p>
<h2>1. The governance flow</h2>
<p>TauGuard says every execution request "passes through a deterministic verification path": input (request, identity, context, evidence), meaning (governed semantic interpretation), evaluation (constitutional predicates execute), admissibility (authority and constraints verified), decision, and chronicle (evidence and lineage committed).</p>
{a.render("The governance flow.")}{cite('governance')}
<h2>2. Intelligence advises, the core decides, the boundary holds</h2>
<p>"Authority is not intelligence." Intelligence may propose; the deterministic core holds the decision; consequence sits behind the execution boundary. Of structural refusal (GOV-04) TauGuard says: "refusal is terminal rather than an invitation to retry around the constraint."</p>
{b.render("Three bands.")}{cite('governance')}
<h2>3. ARCHONT's six layers and its execution seam</h2>
<p>TauGuard says ARCHONT "governs the relationship between organizational authority and operational exchange. It does not need to replace every ERP, AI system, API, machine or workflow that performs operational work."</p>
{c.render("ARCHONT GOS, six layers and the seam to operational reality.")}{cite('architecture')}
<h2>4. TauMesh: five deltas and the lifecycle</h2>
<p>"A change is local in origin, but its consequences are determined by topology." A material change is evaluated through dependencies and can invalidate what was admissible before.</p>
{d.render("TauMesh inside ARCHONT.")}{cite('architecture')}
<h2>5. TauDIL's flow</h2>
<p>TauDIL separates generating intelligence from evaluating it. SYGON is "integrated into TauDIL GOS as part of its semantic governance capability stack".</p>
{e}{cite('taudil')}
<h2>6. IFA's seven-layer stack</h2>
<p>TauGuard's IFA page sets out "seven layers forming the constitutional execution stack. Every action passes through each layer in sequence." It places SYGON at layer 2, AGL at layer 3 and IEL at layer 5, and says the chronicle "is written before action, not after".</p>
{f7.render("IFA's constitutional stack.")}{cite('ifa')}
<div class="prop-box"><p><strong>Two decision vocabularies.</strong> The governance page gives three outcomes: APPROVE, REVIEW, BLOCK. The IFA page describes AGL's admission as four: ALLOW, RESTRICT, DEFER, BLOCK. We use the governance page's three throughout this site and have not worked out how the two relate. TauGuard should say which is current.</p></div>
<p>Not drawn here: the Governance Under Degradation states, G0 (integral) to G5 (recovery), on the governance page. We have not yet worked out what they mean for the workflows.</p>"""
    return page("/architecture/", "Their architecture, drawn", "Inline diagrams of TauGuard's governance flow, ARCHONT's six layers and execution seam, TauMesh's five deltas and TauDIL's flow, each with its source.", body, mark="Architecture")


# ====================================================== RISKMANDATE
def riskmandate():
    abp = flow("The ABP: reach, mandate, gap, barrier", "An agent behaviour policy records what an agent can do, what it was authorised to do, the gap between them, and the barrier that actually stands in the way.",
               [["Reach", "~what the agent", "~can actually do"], ["Mandate", "~what it was", "~authorised to do"], ["Gap", "~the difference", "~(also called delta)"], ["Barrier", "~rule, review or", "~technical control"]],
               cls_for={2: "wn"}, h=120)
    lad = flow("Three strengths of control", "Behaviour policy first, then hooks, then a boundary: SHarness.",
               [["Behaviour policy", "~start here", "~written down, given to the agent"], ["Hooks", "~stronger", "~checked on every call", "~3 of 12 held; 12 of 12 with a hook"], ["Boundary: SHarness", "~strongest", "~held by something the agent cannot reach", "~6 of 6 probes held, 25 Oct"]],
               cls_for={0: "rm", 1: "rm", 2: "rm"}, h=150)
    stats = [("191", "behaviour policies written for RiskMandate's own agents and published on three sites (some agents appear on two). Evidence: 94 + 54 + 43, read 16 Nov."),
             ("2,262", "agent runs, each with a report against its ABP. Evidence: the run reports, 6 to 16 Nov."),
             ("2,980", "actions logged as outside an agent's grant: seen, recorded, allowed."),
             ("1", "rule that failed and became a barrier the agent cannot remove. Evidence: the in-action record, 2 to 6 Nov."),
             ("94 of 109", "agents on the team's circuit on 10 November had a written ABP (the stand deck).")]
    cards = "".join(f'<div class="card rm"><span class="stat">{n}</span><p>{t}</p></div>' for n, t in stats)
    body = f"""<h1>RiskMandate</h1>
<p class="lede">RiskMandate's facts, as it states them, with its sources. We add nothing to the numbers and we repeat what it says was not done.</p>
<h2>The ABP</h2>
<p>An Agent Behaviour Policy "describes one AI agent in one deployment: everything it can do (the grant), what you actually authorised (the mandate), the gap between the two (the delta), and what really stands in the way of each thing (the barrier). It describes and it does not judge, so it carries no score."</p>
{abp}{rcite('https://riskmandate.ai/agent-behaviour-policy.html', 'riskmandate.ai/agent-behaviour-policy.html')}
<p>On its own team's pages the same four terms are Reach, Mandate, Gap and Barrier, and each barrier is labelled "a rule the agent keeps, a review by another agent or person, or a technical control the agent cannot change".</p>
{rcite('https://web-summit.sgit.ai/abp/in-action/', 'web-summit.sgit.ai/abp/in-action/')}
<h2>Policy, hooks, boundary</h2>
<p>RiskMandate lays out three strengths, "honestly, in order": a behaviour policy ("not the strongest control, but a lot of value for the money, today"), hooks ("the rule checked on every call, outside the model's say-so"), and a boundary, SHarness ("the rule enforced by something the agent cannot reach").</p>
{lad}{rcite(RM, 'riskmandate.ai')}
<p>The hook figure comes from a test on a chat-only agent whose rule was one line in the prompt. Told to ignore the rule, the line alone held 3 of 12 attacks; with a hook it held all 12, the hook blocking five. For SHarness RiskMandate says: "Six of six probes held on 25 October; nothing yet binds the agent itself."</p>
<p>SHarness turns an ABP into a policy "the Linux kernel holds on every process the agent starts". RiskMandate says it is "an early version" and marks parts as "design, not built". It also says: "We are still never in the request path."</p>
{rcite('https://riskmandate.ai/secure-harness.html', 'riskmandate.ai/secure-harness.html')}
<h2>The summit figures</h2>
<p>At Web Summit in November, RiskMandate counts "more than a hundred agents" on its own team, most with an ABP of their own.</p>
<div class="grid">{cards}</div>
{rcite(RM, 'riskmandate.ai')}
<h2>What was not done</h2>
<p>RiskMandate's own section, in its words: "Our summit ABPs were in observe mode by choice: gaps were logged and allowed, not blocked, apart from one call. Most were documented from each agent's brief and tools, not measured on it. Nobody outside the team has checked these counts. No customer is named, because none has agreed to be."</p>
{rcite(RM, 'riskmandate.ai, section 06')}
<p>That one call: the newsroom's developer agent tried to write a hold file that only the security agent writes and only the lead lifts. It was the one call blocked in 2,262 runs.</p>
{rcite('https://riskmandate.ai/', 'riskmandate.ai, situation of 6 Nov')}
<h2>The rule that failed</h2>
<p>On 2 November a conductor agent pushed to main, though "never push to main" was written down as a sentence. On 6 November main was protected and the sentence became a barrier. This is the example RiskMandate itself uses of a rule becoming a technical barrier.</p>
{rcite('https://web-summit.sgit.ai/abp/in-action/', 'web-summit.sgit.ai/abp/in-action/')}"""
    return page("/riskmandate/", "RiskMandate", "The agent behaviour policy, hooks and the SHarness boundary, and RiskMandate's summit figures with its sources and what it says was not done.", body, mark="RiskMandate")


# ====================================================== TOGETHER
def together():
    s = Svg(900, 400, "Five places RiskMandate and TauGuard meet", "Five rows pairing a RiskMandate term with a TauGuard term: ABP to executable constitution, the ABP gap to admissibility, hooks and SHarness to the execution boundary, run reports to Chronicle and TauStamp, and the rule that failed becoming a barrier to structural refusal.")
    rows = [("The ABP", "Executable constitution"), ("The ABP gap (delta)", "Admissibility"), ("Hooks and SHarness", "The execution boundary"),
            ("Run reports", "Chronicle and TauStamp"), ("The rule that failed became a barrier", "Structural refusal (GOV-04)")]
    s.text(200, 18, "RISKMANDATE", 13, "middle", "b"); s.text(700, 18, "TAUGUARD", 13, "middle", "b")
    for i, (l, r) in enumerate(rows):
        y = 28 + i * 72
        s.box(10, y, 380, 54, [l], cls="rm", size=15)
        s.box(510, y, 380, 54, [r], cls="tg", size=15)
        s.arrow(394, y + 27, 506, y + 27); s.text(450, y + 20, "we propose", 11, "middle")
    trows = [
        ["The ABP: what each agent may do (reach, mandate, gap, barrier)", "An executable constitution: rules that run, not documents. TauGuard: \"A narrative describes. An executable constitution determines.\"", "Different jobs. The ABP describes; the constitution decides. W1 asks whether a mandate can become predicates."],
        ["The gap: what an agent can do beyond its mandate", "Admissibility: whether an action is authorised under the governed state. If it cannot be shown, no execution.", "RiskMandate records the gap and, at the summit, allowed it. TauGuard would refuse it. That is the interesting difference."],
        ["Hooks (a rule checked on every call) and SHarness (held by something the agent cannot reach)", "The execution boundary: consequence-bearing action sits behind it.", "Both place enforcement outside the model. RiskMandate says it is never in the request path; TauGuard's core is active at the boundary. W1 and W4 depend on which."],
        ["Run reports: one per agent run, against its ABP", "Chronicle (evidence and lineage committed) and, in ARCHONT, TauStamp (governance memory for legitimacy replay).", "Both keep a record meant to be checked later by someone else. Whether one can feed the other is untested."],
        ["\"The rule that failed became a barrier\": a sentence, then a breach, then a control", "Structural refusal (GOV-04): where admissibility cannot be shown, refusal is terminal.", "RiskMandate arrived at a barrier after a failure; TauGuard starts from refusal. Same end state, different route."]]
    body = f"""<h1>Side by side</h1>
<p class="lede">Five places where a RiskMandate idea and a TauGuard idea look like the same thing from two sides. The pairing is our proposal. Neither company has said it.</p>
{s.render("Our proposed mapping, RiskMandate on the left and TauGuard on the right.")}
{table(trows, ["RiskMandate says", "TauGuard says", "Our reading (a proposal)"])}
<span class="src">Sources: {cite('governance')[len('<span class="src">'):-len('</span>')]} {rcite(RM, 'riskmandate.ai')[len('<span class="src">'):-len('</span>')]} {cite('architecture')[len('<span class="src">'):-len('</span>')]}</span>
<h2>Where they differ</h2>
<ul>
<li><strong>Describe or decide.</strong> An ABP "describes and does not judge". TauGuard's core returns APPROVE, REVIEW or BLOCK.</li>
<li><strong>In the path or beside it.</strong> RiskMandate: "We are still never in the request path." TauGuard: governance is "active at the execution boundary rather than reconstructed afterwards".</li>
<li><strong>Observed or proven.</strong> RiskMandate's summit counts were observed in observe mode and "nobody outside the team has checked" them. TauGuard says its mechanisms can be examined "within their stated scope" and publishes a simulator for ARCHONT.</li>
</ul>
<p>These differences are why the pairing could be useful. They are also the first things TauGuard may want to correct.</p>"""
    return page("/together/", "Side by side", "Five places RiskMandate and TauGuard meet: ABP to executable constitution, gap to admissibility, hooks to the execution boundary, run reports to Chronicle, a failed rule to structural refusal.", body, mark="Together")


# ====================================================== WORKFLOWS
def workflows():
    # W1
    w1 = flow("W1: an ABP becomes predicates in TauGuard's core", "An ABP row becomes a predicate; an agent's consequence-bearing call is evaluated by the core; the decision is approve, review or block; the decision goes to the Chronicle and the run report.",
              [["ABP row", "~reach, mandate,", "~gap, barrier"], ["Predicate", "~one per mandate", "~row"], ["Agent call", "~consequence-", "~bearing"], ["Core decides", "~G(E, S, C)"], ["Decision", "~APPROVE, REVIEW", "~or BLOCK"], ["Record", "~Chronicle and", "~run report"]],
              cls_for={0: "rm", 1: "pr", 3: "tg", 4: "rv", 5: "ok"}, h=120)
    # W2
    w2 = Svg(900, 300, "W2: the Sovereign Website change chain under ARCHONT", "Six steps: brief, sites review, Factory request, security, decision, merge. ARCHONT holds each as governed state. TauStamp keeps lineage. Our provenance graph feeds evidence in.")
    w2.zone(6, 6, 888, 150, "ARCHONT GOS (proposed): each step is governed state; Standing decides what may proceed")
    for i, t in enumerate(["Brief", "Sites review", "Factory request", "Security", "Decision", "Merge"]):
        w2.box(20 + i * 146, 56, 120, 64, [t], cls="pr", size=12)
        if i < 5: w2.arrow(142 + i * 146, 88, 164 + i * 146, 88)
    w2.box(40, 206, 330, 70, ["Provenance graph"], cls="rm", size=15, sub=["our evidence feed: who did what, signed"])
    w2.box(530, 206, 330, 70, ["TauStamp"], cls="tg", size=15, sub=["lineage: why each step was admissible"])
    w2.arrow(205, 204, 205, 160); w2.arrow(690, 160, 690, 204)
    # W3
    w3 = Svg(900, 330, "W3: PrompTugal News under TauDIL and SYGON", "An article's claims go to TauDIL for a semantic coherence check with SYGON. If coherent, the article goes to the newsroom's existing gate and then release. If not, refusal is terminal. Semantic drift is reported either way.")
    for i, (t, sub, c) in enumerate([("Article", "its claims listed", "n"), ("TauDIL check", "semantic coherence", "pr"), ("SYGON", "authorised knowledge", "pr"), ("Newsroom gate", "the existing one", "n"), ("Release", "published", "ok")]):
        x = 10 + i * 178
        w3.box(x, 20, 150, 74, [t], cls=c, size=14, sub=[sub])
        if i < 4: w3.arrow(x + 152, 57, x + 176, 57)
    w3.box(190, 170, 330, 56, ["Refusal is terminal"], cls="wn", size=14, sub=["the article is not retried around it (GOV-04)"])
    w3.box(560, 170, 330, 56, ["Drift report"], cls="tg", size=14, sub=["semantic movement reported over time"])
    w3.path("M 265 96 L 265 168", "ar")
    w3.path("M 441 96 L 441 130 L 725 130 L 725 168")
    w3.text(280, 140, "not coherent", 12)
    w3.text(560, 124, "reported either way", 12)
    w3.text(10, 280, "The newsroom's own gate stays. TauDIL adds a check before it, never instead of it.", 13)
    w3.text(10, 302, "Until TauGuard says otherwise we do not know that TauDIL can read an article.", 13)
    # W4
    w4 = flow("W4: TauGuard's own agents under RiskMandate ABPs", "A TauGuard agent works under an ABP that RiskMandate writes; its calls go to TauGuard's core, which acts as the boundary; effects happen only after approval.",
              [["TauGuard agent", "~if it runs any"], ["ABP", "~RiskMandate writes", "~reach, mandate, gap"], ["Call", "~consequence-", "~bearing"], ["TauGuard core", "~is the boundary"], ["Effect", "~or a refusal"]],
              cls_for={1: "rm", 3: "tg", 4: "ok"}, h=120)
    body = f"""<h1>Four joint workflows</h1>
<p class="lede">Each one is drawn, and each one is a proposal. None is agreed with TauGuard and none is built. Each says what it would take from TauGuard that we do not know it has.</p>
<h2>W1. An ABP becomes predicates in TauGuard's core</h2>
{prop("RiskMandate writes an agent's ABP. TauGuard's core would evaluate each consequence-bearing call against predicates derived from it, and return APPROVE, REVIEW or BLOCK. Decisions go to the Chronicle and into the agent's run report.")}
{w1}
<p>What we know: TauGuard's governance page describes constitutional predicates, the three decisions and the Chronicle. RiskMandate's ABP lists the mandate row by row. What we do not know: whether a mandate row can be written as a predicate the core accepts, and how an outside agent's call reaches the core.</p>{cite('governance')}
<h2>W2. The Sovereign Website change chain under ARCHONT</h2>
{prop("The chain a site change goes through, as sites.a described it on 24 Nov 2026: brief, sites review, Factory request, security, decision, merge. ARCHONT would hold each step as governed state. TauStamp would keep the lineage. Our provenance graph would be the evidence feed.")}
{w2.render("W2 as proposed.")}
<p>What we know: ARCHONT is described as maintaining governed state and TauStamp as preserving "governed lineage so that legitimacy can be reconstructed". What we do not know: how evidence from outside gets into ARCHONT, or whether the simulator TauGuard publishes can take it.</p>{cite('archon')}
<h2>W3. PrompTugal News under TauDIL and SYGON</h2>
{prop("Before an article reaches the newsroom's own gate, TauDIL checks the semantic coherence of its claims, with SYGON. A refusal is terminal. Drift is reported. The newsroom's gate stays as it is.")}
{w3.render("W3 as proposed.")}
<p>What we know: SYGON's page says that where governance cannot establish an acceptable result, "the system can refuse rather than invent", and TauDIL's page offers an interactive demo. What we do not know: whether TauDIL can take news text, or what a coherence check needs as its "authorised knowledge".</p>{cite('sygon')}
<h2>W4. TauGuard's own agents under RiskMandate ABPs</h2>
{prop("If TauGuard runs AI agents, RiskMandate would write an ABP for each, and TauGuard's core would be the boundary that stops what the ABP says should not happen. TauGuard's public pages do not say whether it runs agents; this workflow assumes it might.")}
{w4}
<p>This one is the plainest test of the whole idea: a governance company holding its own agents to its own boundary, with an outside party writing the policy. RiskMandate's caveat applies: its SHarness boundary has six of six probes held and nothing yet binds the agent itself.</p>{rcite('https://riskmandate.ai/', 'riskmandate.ai')}"""
    return page("/workflows/", "Four joint workflows", "Four proposed joint workflows between TauGuard and RiskMandate, each drawn: an ABP as predicates, the Sovereign Website change chain under ARCHONT, PrompTugal News under TauDIL, and TauGuard's own agents.", body, mark="Workflows")


# ====================================================== MVP
def mvp():
    s = Svg(900, 400, "The two-way MVP", "Two lanes. Ours: a keeper's push to dev asks TauGuard and acts only after APPROVE. Theirs: one PrompTugal News article runs through TauDIL before release. Both are measured.")
    s.zone(6, 6, 888, 130, "OURS: a keeper's push to dev acts only after a TauGuard APPROVE")
    for i, (t, c) in enumerate([("Keeper push", "n"), ("Ask TauGuard", "pr"), ("Decision", "rv"), ("Push or stop", "n"), ("Decision kept", "ok")]):
        x = 20 + i * 174
        s.box(x, 44, 140, 66, [t], cls=c, size=14, sub=["3 outcomes"] if i == 2 else None)
        if i < 4: s.arrow(x + 142, 77, x + 172, 77)
    s.zone(6, 152, 888, 130, "THEIRS: one PrompTugal News article runs through TauDIL before release")
    for i, (t, c) in enumerate([("Article", "n"), ("TauDIL", "pr"), ("Drift report", "tg"), ("Newsroom gate", "n"), ("Release", "ok")]):
        x = 20 + i * 174
        s.box(x, 190, 140, 66, [t], cls=c, size=14, sub=["coherence, SYGON"] if i == 1 else None)
        if i < 4: s.arrow(x + 142, 223, x + 172, 223)
    s.box(150, 310, 600, 72, ["Measured"], cls="rm", size=15, sub=["decisions, correct and false blocks, added latency, published"])
    body = f"""<h1>A two-way MVP</h1>
<p class="lede">One small thing that works in both directions, so each side learns what the other's design does under real use.</p>
{prop("All of this is a proposal. Nothing here is agreed with TauGuard or built. The first thing we need from TauGuard is an endpoint or a demo we can call, and we do not assume it exists.")}
{s.render("The MVP in two lanes.")}
<h2>Ours: a keeper's push to dev</h2>
<p>One of our agents, proposed as a keeper pushing to <code>dev</code>, acts only after a TauGuard APPROVE. REVIEW holds it for a person. BLOCK stops it, and the stop is final for that attempt. We chose this because the repository already has a rule that keepers push to <code>dev</code> only and a signing check, so we can compare TauGuard's decision with what the existing checks would have done.</p>
<h2>Theirs: one article through TauDIL</h2>
<p>One PrompTugal News article has its claims checked for semantic coherence by TauDIL, with SYGON, before the newsroom's own gate. We keep the gate. We see whether TauDIL's check agrees with it, and whether it reports drift.</p>
<h2>What we would measure</h2>
{table([["Decisions", "How many calls or claims were decided, and how each came out."], ["Correct and false blocks", "A block is correct if a person, looking later, agrees. A false block is one they overturn."], ["Added latency", "The time the check added to the push or the article."], ["Published", "What actually went out, and whether anything wrong did."]], ["Measure", "Meaning"])}
<h2>What we need from TauGuard</h2>
<ul>
<li>An endpoint or demo for an outside call. We do not assume one exists. TauGuard's pages offer a downloadable ARCHONT simulator and a TauDIL interactive demo; neither is known to take our input.</li>
<li>A statement of what TauGuard will agree to publish. We publish nothing about TauGuard's results without it.</li>
<li>Its own view of whether the two measurements are fair to its design.</li>
</ul>
{cite('partners')}
<p>Its partners page says pilots are "subject to technical qualification, scope, security requirements, commercial terms, data considerations and a mutually agreed written pilot agreement". This MVP is smaller than a pilot and would not replace one.</p>"""
    return page("/mvp/", "A two-way MVP", "A proposed two-way MVP: a keeper's push to dev acts only after a TauGuard APPROVE, and one PrompTugal News article runs through TauDIL before release. Measured, and not assumed.", body, mark="MVP")


# ====================================================== NEXT
def nxt():
    steps = [["1 Introduce", "~qualified contact"], ["2 Evaluate", "~architecture,", "~requirements, fit"], ["3 Pilot", "~defined scope,", "~measurable aims"], ["4 Validate", "~evidence, results,", "~assessment"], ["5 Scale", "~commercial", "~agreement"]]
    f = flow("TauGuard's commercial pathway", "Introduce, evaluate, pilot, validate, scale, as TauGuard's partners page sets them out.", steps, h=120)
    body = f"""<h1>What next</h1>
<p class="lede">TauGuard publishes its own path for working with others. We start from it, not from ours.</p>
<h2>TauGuard's path</h2>
<p>TauGuard's partners page sets out "From introduction to deployment" in five steps and says its objective is "to convert credible technical mechanisms into independently evaluated, commercially relevant deployments while keeping claims aligned with the evidence available."</p>
{f}{cite('partners')}
<p>The page names six kinds of contact, though it introduces them as "five ways": investors, sales channels, independent sales professionals, pilot deployment companies, strategic partners and enterprise evaluators.</p>
<h2>Where we could fit</h2>
{prop("We are not investors or sellers. The nearest fits are the enterprise evaluator and the strategic partner, and then, if TauGuard wished, a small pilot.")}
{table([["Introduce", "This site is a way in: it shows we have read the pages and what we would like to test. sites.a reviews it before TauGuard sees it."], ["Evaluate", "The architecture drawings on this site are an outside reading of its design. We would like TauGuard to correct them."], ["Pilot", "The MVP is smaller than a pilot. It could be a first step toward one."], ["Validate", "The measures on the MVP page are ours to propose. TauGuard would decide what counts as evidence."], ["Scale", "Not for us to say."]], ["TauGuard's step", "Where we could fit (a proposal)"])}
<h2>What happens now</h2>
<p>Dinis Cruz decides whether and when this site is shown to TauGuard, and what from any meeting goes into it. Until TauGuard agrees, no TauGuard person is named here and no TauGuard branding is used.</p>"""
    return page("/next/", "What next", "TauGuard's own path from introduction to scale, taken from its partners page, and where a Sovereign Website and RiskMandate proposal could fit.", body, mark="Next")



def sources():
    T = "https://tauguard.ai/"
    rows = [
     ["tauguard.ai/systems.html", "The systems and the one-company statement. Home (home.html) serves the same text.", "Read in full"],
     ["tauguard.ai/governance.html", "The governance flow, three decisions, GOV-01 to GOV-06, the extensions (IFA, GOM, GUD, AGL, SFA, TauMesh), GUD states.", "Read in full"],
     ["tauguard.ai/architecture.html", "ARCHONT's architecture, six layers, TauMesh, execution seam, TauStamp.", "Read in full"],
     ["tauguard.ai/archon.html", "ARCHONT GOS, its flow, TauMesh deltas, the simulator.", "Read in full"],
     ["tauguard.ai/taudil.html", "TauDIL GOS, its flow, SYGON's place in it, the interactive demo.", "Read in full"],
     ["tauguard.ai/sygon.html", "SYGON's four steps and its deliberate boundary.", "Read in full, from its first section"],
     ["tauguard.ai/frameworks.html", "The five frameworks and how they differ from products.", "Read in full"],
     ["tauguard.ai/ifa.html", "IFA specification, the seven-layer stack, AGL's four-way admission.", "Read to the comparison table. The live dashboard figures at the end were not used."],
     ["tauguard.ai/iel.html", "IEL Guard's claims and its three steps.", "Read to the use cases. Code samples and the pricing section were not used. No price appears on this site."],
     ["tauguard.ai/rod.html", "ROD: gamified PC security, in development.", "Read in full"],
     ["tauguard.ai/partners.html", "The commercial pathway and the opportunities.", "Read in full"],
     ["tauguard.ai/about.html", "The company statement. It names people; this site names none of them.", "Read in full"],
     ["tauguard.ai/robots.txt", "It allows crawling.", "Read"]]
    notread = "tauguard.ai/sfa.html, gfa.html, agl.html, ala.html, industries.html, research_lab.html and contact.html were downloaded and not read. Nothing on this site relies on them beyond the names and one-line descriptions on the frameworks page."
    rrows = [
     ["riskmandate.ai/", "The summit figures, the ladder, the situations, what was not done.", "Read in full"],
     ["riskmandate.ai/agent-behaviour-policy.html", "What an ABP is: grant, mandate, delta, barrier.", "Read to the list of capabilities. The sixteen example policies were not read."],
     ["riskmandate.ai/secure-harness.html", "SHarness: what runs today and what is design only.", "Read to the animations. Not read beyond."],
     ["web-summit.sgit.ai/abp/in-action/", "Reach, mandate, gap, barrier; the three barrier kinds; the rule that failed.", "Read the opening and the scoreboard"],
     ["web-summit.sgit.ai/abp/", "The explorer phase: policies observe and block nothing yet.", "Read the opening"]]
    notopened = "RiskMandate links the run reports, the stand deck, the counting notes and a GitHub run report as evidence for its figures. We did not open them. Its figures on this site are repeated as it states them."
    def row(r, base):
        u = base + r[0].split("/", 1)[1] if r[0].startswith("tauguard.ai") else "https://" + r[0]
        if r[0].startswith("tauguard.ai"): u = "https://" + r[0]
        return [f'<a href="{u}">{r[0]}</a>', r[1], r[2]]
    body = f"""<h1>Sources</h1>
<p class="lede">Every page we read, what we used it for, how much of it we read, and the date: {READ}.</p>
<h2>TauGuard</h2>
{table([row(r, T) for r in rows], ["Page", "Used for", "How much we read, on " + READ])}
<p>{notread}</p>
<h2>RiskMandate</h2>
{table([row(r, "") for r in rrows], ["Page", "Used for", "How much we read, on " + READ])}
<p>{notopened}</p>
<h2>Not sources</h2>
<p>Nothing from any meeting with TauGuard is on this site. The change chain in W2 is described as sites.a gave it. Every joint workflow, the MVP and the mapping on the side-by-side page are our proposals and say so.</p>"""
    return page("/sources/", "Sources", "Every tauguard.ai and riskmandate.ai page this proposal draws on, what it was used for, how much was read and when.", body, mark="Sources")


def designs_index():
    ds = [(1, "Paper", "The live design. One page per topic, a top bar, long-form reading with diagrams in the flow.", "Best for one answer at a time, and for printing or linking a single page. Weakest at showing the whole proposal at once."),
          (2, "Atlas", "The whole proposal on one scrolling page with a sticky index on the left.", "Best for seeing how the parts connect and for searching with the browser. Weakest on a phone, where the index folds away, and for linking to one topic."),
          (3, "Ledger", "TauGuard on the left, RiskMandate on the right, a red boundary line between them, and the joint material below it.", "Best for showing the idea of the whole proposal in the layout itself. Weakest where long diagrams must fit half a page."),
          (4, "Briefing", "A short opening, then five tabs, one topic showing at a time. No script: the tabs are plain form controls and CSS.", "Best for a visitor with five minutes who wants to choose. Weakest for printing and for search, since hidden tabs are not on the page."),
          (5, "Blueprint", "Dark, monospaced, drawn like a set of engineering sheets with an index of tiles and a title block on each sheet.", "Best for a technical reader and for making the diagrams the centre. Weakest for long reading, and furthest from TauGuard's own look, which we are not copying.")]
    cards = "".join(f'<div class="card both"><span class="tag okt">{"Live now" if n == 1 else "Prototype"}</span><h2>{n}. {nme}</h2><p>{d}</p><p>{c}</p><p><a href="/designs/{n}/">Open design {n}</a></p></div>' for n, nme, d, c in ds)
    body = f"""<h1>Design directions</h1>
<p class="lede">Five structural directions for this site. They differ in how the content is arranged and navigated, not only in colour. Every prototype carries the same content as the live pages.</p>
<p>The live pages stay on design 1 until the owner picks. Review round 1 is open: sites.a and design.b (through a.maestro) are asked to look at all five. A recommendation follows the second round.</p>
<div class="grid">{cards}</div>
<h2>What each review looks at</h2>
<ul><li>Does the structure make the proposal easier or harder to take in?</li><li>Do the diagrams stay legible on a phone?</li><li>Is the "not TauGuard's own site" notice still plain?</li><li>Does it avoid copying TauGuard's look, logo or branding?</li><li>Does it pass the pipeline's accessibility and validity checks?</li></ul>
<p>Recommendation: none yet.</p>"""
    return page("/designs/", "Design directions", "Five structural design directions for this proposal site. The live pages use one until the owner picks.", body, mark="Design")


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "site", "assets"), exist_ok=True)
    open(os.path.join(ROOT, "site", "assets", "site.css"), "w").write(CSS)
    for path, fn in [("/", home), ("/tauguard/", tauguard), ("/architecture/", architecture), ("/riskmandate/", riskmandate), ("/together/", together),
                     ("/workflows/", workflows), ("/mvp/", mvp), ("/next/", nxt), ("/designs/", designs_index), ("/sources/", sources)]:
        out = fn()
        if re.search("[—–]|&mdash;|&ndash;", out):
            raise SystemExit(f"dash in {path}")
        write(path, out)
        print("wrote", path, len(out))
    import designs
    designs.build_designs()
