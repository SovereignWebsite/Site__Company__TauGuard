"""Five structural design directions, built from the live pages' own content. Each is a prototype of the whole site on one page.
Called from build.py after the live pages are written, so figure ids stay unique."""
import os, re, html
from lib import NAME, NOTICE, FAMILY, head, picker
from css1 import CSS as BASE

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PAGES = [("home", "/"), ("tauguard", "/tauguard/"), ("architecture", "/architecture/"), ("riskmandate", "/riskmandate/"),
         ("together", "/together/"), ("workflows", "/workflows/"), ("mvp", "/mvp/"), ("next", "/next/")]
TITLES = {"home": "Two companies, one boundary", "tauguard": "What TauGuard builds", "architecture": "Their architecture, drawn", "riskmandate": "RiskMandate",
          "together": "Side by side", "workflows": "Four joint workflows", "mvp": "A two-way MVP", "next": "What next"}


def main_of(key):
    path = dict(PAGES)[key]
    f = os.path.join(ROOT, "site", path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "site", "index.html")
    s = open(f).read()
    m = re.search(r'<main id="main">\s*(?:<div class="mark">.*?</div>)?(.*?)</main>', s, re.S)
    return m.group(1)


def demote(s, by=1):
    """h1->h2 etc., so several pages can share one document."""
    for lvl in (4, 3, 2, 1):
        s = re.sub(rf"<h{lvl}(\s|>)", rf"<h{lvl + by}\1", s)
        s = re.sub(rf"</h{lvl}>", rf"</h{lvl + by}>", s)
    return s


def section(key, by=1, cls="sec", extra=""):
    return f'<section id="{key}" class="{cls}" aria-label="{html.escape(TITLES[key])}">{demote(main_of(key), by)}{extra}</section>'


NOTE = "Design direction {n} of five. The same content as the live site, arranged differently. Nothing here is TauGuard's own design."


def shell(n, name, css, body, body_cls=""):
    p = f"/designs/{n}/"
    h = head(f"Design {n}, {name}", f"Design direction {n} of five for this proposal site: {name}.", p, css=f"/designs/{n}/style.css")
    return h + f"""<body class="{body_cls}">
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
{picker(n)}
<header class="top">
  <a class="name" href="/designs/">Design directions</a>
  <nav class="own" aria-label="Designs"><a href="/designs/">All five</a><a href="/">Live site</a></nav>
  <p class="notice" role="note">{NOTICE} <span class="dn">Design {n} of 5: {name}.</span></p>
</header>
<main id="main">
{body}
</main>
<footer>
<nav class="site-links" aria-label="About this site"><a href="/designs/">All directions</a><a href="/">Live site</a><a href="/start/">Start here</a></nav>
<p>{NOTICE}</p>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------- design-specific CSS (appended to the shared base)
COMMON = """.notice .dn{display:block;color:var(--muted);font-size:.85em;margin-top:.15rem}
@media (max-width:40rem){.notice{padding:.3rem .6rem;font-size:14px;line-height:1.35}.notice .dn{display:inline;margin-left:.3rem}}
section.sec{scroll-margin-top:1rem}"""

CSS2 = COMMON + """
:root{--accent:#1f5c8b;--tg:#1f5c8b}
@media (prefers-color-scheme:dark){:root{--accent:#8db8e6;--tg:#8db8e6}}
h1,h2{font-family:Georgia,'Times New Roman',serif;font-weight:700}
main{max-width:76rem;display:grid;grid-template-columns:13rem minmax(0,1fr);gap:0 2.5rem;align-items:start}
.index{position:sticky;top:1rem;font-size:.92rem;border-left:3px solid var(--accent);padding-left:.9rem}
.index strong{display:block;margin-bottom:.4rem}.index ol{list-style:none;margin:0;padding:0}.index li{margin:.3rem 0}.index a{text-decoration:none;font-weight:600}
.index a:hover,.index a:focus-visible{text-decoration:underline}
.content{min-width:0}.content .sec{padding-top:1rem;border-top:1px solid var(--line);margin-top:2rem}.content .sec:first-child{border-top:0;margin-top:0}
@media (max-width:50rem){main{display:block}.index{position:static;margin:.6rem 0;border-left:0;padding:0}.index strong{display:none}.index ol{display:flex;gap:.3rem 1.1rem;overflow-x:auto;white-space:nowrap;padding:.4rem 0}}"""

CSS3 = COMMON + """
:root{--accent:#444}
@media (prefers-color-scheme:dark){:root{--accent:#c8c8c8}}
h1,h2{letter-spacing:-.01em}
.ledger{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--line);border-radius:8px;overflow:hidden;margin:1rem 0}
.ledger>div{padding:0 1.2rem 1rem;min-width:0}.ledger>div:first-child{border-right:4px solid var(--warn)}
.ledger .band{margin:0 -1.2rem 1rem;padding:.6rem 1.2rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.85rem}
.ledger .l .band{background:var(--tg-bg);color:var(--tg)}.ledger .r .band{background:var(--rm-bg);color:var(--rm)}
.ledger h1{font-size:1.9rem}.ledger .fig svg{border:0}
.rule{display:flex;align-items:center;gap:.8rem;color:var(--warn);font-weight:700;font-size:.85rem;letter-spacing:.08em;text-transform:uppercase;margin:2rem 0 0}
.rule::before,.rule::after{content:"";flex:1;border-top:3px solid var(--warn)}
.full .sec{margin-top:1.5rem}
.glance{display:grid;grid-template-columns:1fr 6px 1fr;gap:0;margin:1rem 0;border:1px solid var(--line);border-radius:8px;overflow:hidden}
.glance>div{padding:.6rem .8rem;font-size:.9rem;color:var(--fg)}.glance .gl{background:var(--tg-bg)}.glance .gr{background:var(--rm-bg)}.glance .gb{background:var(--warn);padding:0}
.glance b{display:block;font-size:.75rem;letter-spacing:.08em;text-transform:uppercase}.glance .gl b{color:var(--tg)}.glance .gr b{color:var(--rm)}
@media (max-width:50rem){.ledger .l{border-left:8px solid var(--tg)}.ledger .r{border-left:8px solid var(--rm)}.ledger>div{padding-left:.8rem}.ledger .band{margin-left:-.8rem}}
@media (max-width:50rem){.ledger{grid-template-columns:1fr}.ledger>div:first-child{border-right:0;border-bottom:4px solid var(--warn)}}"""

CSS4 = COMMON + """
:root{--accent:#6a3d9a}
@media (prefers-color-scheme:dark){:root{--accent:#c9a6ec}}
.tabs>input{position:absolute;opacity:0;pointer-events:none}
.tabbar{display:flex;flex-wrap:nowrap;overflow-x:auto;gap:.4rem;margin:1rem 0 0;border-bottom:2px solid var(--line)}
.tabbar label{white-space:nowrap;flex:0 0 auto;padding:.55rem 1rem;border:1px solid var(--line);border-bottom:0;border-radius:8px 8px 0 0;cursor:pointer;color:var(--accent);font-weight:600;background:var(--panel)}
.tabbar label:hover{background:var(--bg)}
.panels>.panel{display:none;padding-top:.5rem}
#tab1:checked~.panels #p1,#tab2:checked~.panels #p2,#tab3:checked~.panels #p3,#tab4:checked~.panels #p4,#tab5:checked~.panels #p5,#tab6:checked~.panels #p6{display:block}
#tab6:checked~.tabbar label[for=tab6],#tab1:checked~.tabbar label[for=tab1],#tab2:checked~.tabbar label[for=tab2],#tab3:checked~.tabbar label[for=tab3],#tab4:checked~.tabbar label[for=tab4],#tab5:checked~.tabbar label[for=tab5]{background:var(--bg);color:var(--fg);border-color:var(--accent);border-bottom:2px solid var(--bg);margin-bottom:-2px}
#tab6:focus-visible~.tabbar label[for=tab6],#tab1:focus-visible~.tabbar label[for=tab1],#tab2:focus-visible~.tabbar label[for=tab2],#tab3:focus-visible~.tabbar label[for=tab3],#tab4:focus-visible~.tabbar label[for=tab4],#tab5:focus-visible~.tabbar label[for=tab5]{outline:3px solid var(--accent);outline-offset:2px}
.intro h1{margin-bottom:.4rem}.intro .lede{margin-bottom:.4rem}"""

CSS5 = COMMON + """
:root{--bg:#17181a;--fg:#eceff1;--muted:#b4babf;--accent:#f4f4f4;--line:#3a3d42;--panel:#212326;--tg:#9fc2ff;--tg-bg:#232b38;--rm:#e0b070;--rm-bg:#34291b;--ok:#9ad6b4;--ok-bg:#1f3028;--warn:#ff9a92;--warn-bg:#3a2224;--rev:#e8d28a;--rev-bg:#322d1a}
body{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:16px;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:32px 32px;background-position:-1px -1px}
body>*{position:relative}
h1,h2,h3{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.04em}h1{font-size:clamp(1.6rem,5vw,2.4rem)}h2{font-size:1.2rem}h3{font-size:1rem}
main,.top{max-width:70rem}
@media (max-width:40rem){.tiles{grid-template-columns:1fr 1fr;gap:.4rem}.tiles a{padding:.4rem .5rem;font-size:.85rem}.sheet{padding:.7rem .8rem 0}.sheet .tb{margin:1rem -.8rem 0;padding:.4rem .8rem}}
.notice{background:var(--panel)}
.tiles{display:grid;gap:.6rem;grid-template-columns:repeat(auto-fit,minmax(11rem,1fr));margin:1.2rem 0}
.tiles a{display:block;border:1px solid var(--accent);padding:.6rem .8rem;background:var(--panel);text-decoration:none;font-weight:700;color:var(--fg)}
.tiles a span{display:block;color:var(--accent);font-size:.8rem}
.tiles a:hover,.tiles a:focus-visible{background:var(--accent);color:var(--bg)}.tiles a:hover span,.tiles a:focus-visible span{color:var(--bg)}
.sheet{border:2px solid var(--accent);background:rgba(23,24,26,.94);margin:2rem 0;padding:1rem 1.2rem 0;position:relative}
.sheet .tb{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;border-top:1px solid var(--accent);margin:1.2rem -1.2rem 0;padding:.4rem 1.2rem;font-size:.8rem;color:var(--muted)}
.card,.prop-box,.fig svg,table{border-radius:0}.fig svg{background:var(--bg)}
footer,.family-credit{font-family:system-ui,sans-serif}"""


def d1():
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in [("/tauguard/", "TauGuard"), ("/architecture/", "Architecture"), ("/riskmandate/", "RiskMandate"), ("/together/", "Together"), ("/workflows/", "Workflows"), ("/mvp/", "MVP"), ("/next/", "Next")])
    return demote(main_of("home"), 0).split('<h2>Where to go</h2>')[0] + f'<h2>Where to go</h2><p>In this design each topic is its own page, reached from the top bar. These are the live pages:</p><nav class="site-links" aria-label="Live pages">{nav}</nav><p>Strongest for one answer at a time and for linking or printing a single page. Weakest at showing the whole proposal at once.</p>'


def build_designs():
    out = {}
    # 2 Atlas
    idx = "".join(f'<li><a href="#{k}">{TITLES[k]}</a></li>' for k, _ in PAGES)
    body2 = f'<nav class="index" aria-label="On this page"><strong>The whole proposal</strong><ol>{idx}</ol></nav><div class="content">' + \
        section("home", 0) + "".join(section(k, 1) for k, _ in PAGES[1:]) + "</div>"
    out[2] = ("Atlas", CSS2, body2, "")
    # 3 Ledger
    left = demote(main_of("tauguard"), 0)
    right = demote(main_of("riskmandate"), 0)
    left = re.sub(r'<h1>.*?</h1>', '<h1>What TauGuard builds</h1>', left, flags=re.S)
    glance = '<div class="glance" aria-hidden="true"><div class="gl"><b>TauGuard</b>what may happen</div><div class="gb"></div><div class="gr"><b>RiskMandate</b>what each agent may do</div></div>'
    h3 = demote(main_of("home"), 0).split('<h2>Where to go</h2>')[0]
    mm = re.search(r'<p class="lede">.*?</p>', h3, re.S)
    body3 = h3[:mm.end()] + glance + h3[mm.end():] + \
        f'<div class="ledger"><div class="l"><div class="band">TauGuard: what may happen</div>{demote(left, 1)}</div><div class="r"><div class="band">RiskMandate: what each agent may do</div>{demote(right, 1)}</div></div>' + \
        '<p class="rule">The boundary: where they meet</p><div class="full">' + "".join(section(k, 1) for k in ("together", "workflows", "mvp", "next")) + "</div>"
    out[3] = ("Ledger", CSS3, body3, "")
    # 4 Briefing tabs: first paragraph, then the tabs in one scrolling row, then the panels
    home = demote(main_of("home"), 0)
    m = re.search(r'<p class="lede">.*?</p>', home, re.S)
    head_part = home[:m.end()]
    overview = home[m.end():].split('<h2>Where to go</h2>')[0]
    sides = ('<div class="ledger"><div class="l"><div class="band">TauGuard says</div><p>Governs what may happen. Its core returns APPROVE, REVIEW or BLOCK. Refusal is terminal.</p></div>'
             '<div class="r"><div class="band">RiskMandate says</div><p>Writes down what each agent may do. An ABP describes and does not judge. Barriers are rule, review or technical.</p></div></div>')
    tabs = [("tab1", "Overview", None), ("tab2", "TauGuard", ["tauguard"]), ("tab3", "Architecture", ["architecture"]), ("tab4", "RiskMandate", ["riskmandate"]),
            ("tab5", "Side by side", ["together", "workflows"]), ("tab6", "MVP and next", ["mvp", "next"])]
    inputs = "".join(f'<input type="radio" name="tab" id="{t}"{" checked" if i == 0 else ""}>' for i, (t, _, _) in enumerate(tabs))
    bar = "".join(f'<label for="{t}">{n}</label>' for t, n, _ in tabs)
    def panel(i, ks):
        if ks is None:
            return f'<div class="panel" id="p{i + 1}">{overview}</div>'
        inner = "".join(section(k, 1) for k in ks)
        if ks[0] == "together":
            inner = sides + inner
        return f'<div class="panel" id="p{i + 1}">{inner}</div>'
    panels = "".join(panel(i, ks) for i, (_, _, ks) in enumerate(tabs))
    body4 = f'<div class="intro">{head_part}</div><div class="tabs">{inputs}<div class="tabbar" role="group" aria-label="Sections" tabindex="0">{bar}</div><div class="panels">{panels}</div></div>'
    out[4] = ("Briefing", CSS4, body4, "")
    # 5 Blueprint
    tiles = "".join(f'<a href="#{k}"><span>SHEET {i + 1}</span>{TITLES[k]}</a>' for i, (k, _) in enumerate(PAGES))
    sheets = "".join(
        f'<section id="{k}" class="sheet" aria-label="{html.escape(TITLES[k])}">{demote(main_of(k), 0 if i == 0 else 1)}<div class="tb"><span>SHEET {i + 1} OF {len(PAGES)}</span><span>PROPOSAL, NOT AGREED WITH TAUGUARD</span></div></section>'
        for i, (k, _) in enumerate(PAGES))
    body5 = f'<h1 class="sr" style="position:absolute;left:-999px">Drawing index</h1><nav class="tiles" aria-label="Drawing index">{tiles}</nav>' + sheets
    body5 = body5.replace('<h1 class="sr" style="position:absolute;left:-999px">Drawing index</h1>', '')
    out[5] = ("Blueprint", CSS5, body5, "bp")
    for n, (name, css, body, cls) in out.items():
        d = os.path.join(ROOT, "site", "designs", str(n))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "style.css"), "w").write(BASE + "\n" + css + "\n")
        page = shell(n, name, css, body, cls)
        if re.search("[—–]", page):
            raise SystemExit(f"dash in design {n}")
        open(os.path.join(d, "index.html"), "w").write(page)
        print("wrote design", n, len(page))
    # design 1 prototype page (the live design)
    d = os.path.join(ROOT, "site", "designs", "1"); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "style.css"), "w").write(BASE + "\n" + COMMON + "\n")
    open(os.path.join(d, "index.html"), "w").write(shell(1, "Paper (the live design)", "", d1(), ""))
    return out
