"""Page furniture and inline-SVG helpers for the TauGuard and RiskMandate site.
Run: python3 -I docs/build/build.py   (from the repository root). Writes site/ pages and site/assets/site.css.
Plain British English, no em or en dashes, no scripts."""
import html

SITE = "https://tauguard.company.sovereignweb.site"
NAME = "TauGuard and RiskMandate: working together"
NOTICE = "A Sovereign Website proposal about TauGuard, built from TauGuard's public pages. Not TauGuard Limited's own site."
READ = "24 Nov 2026"

NAV = [("/", "Home"), ("/tauguard/", "TauGuard"), ("/architecture/", "Architecture"), ("/riskmandate/", "RiskMandate"),
       ("/together/", "Together"), ("/workflows/", "Workflows"), ("/mvp/", "MVP"), ("/next/", "Next")]

FAMILY = """<details class="family-credit">
  <summary>Sovereign Website</summary>
  <ul>
    <li><a href="/start/">Start here</a></li>
    <li><a href="/agents/">Use with your AI</a></li>
    <li class="family-gap"><a href="/admin/">How this site was made</a></li>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</details>"""

TG = "https://tauguard.ai/"
RM = "https://riskmandate.ai/"


def cite(page, label=None):
    """A source note for a TauGuard claim: the tauguard.ai page and the date it was read."""
    url = f"{TG}{page}.html"
    return f'<span class="src">Source: <a href="{url}">tauguard.ai/{page}.html</a>, read {READ}.</span>'


def rcite(url, label):
    return f'<span class="src">Source: <a href="{url}">{label}</a>, read {READ}.</span>'


def head(title, desc, path, css="/assets/site.css"):
    full = f"{title}: {NAME}" if title else NAME
    u = f"{SITE}{path}"
    img = f"{SITE}/assets/share/card-1200x630.jpg"
    e = html.escape
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(NAME)}">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{u}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{img}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(NAME)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(full)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{img}">
<link rel="canonical" href="{u}">
<link rel="stylesheet" href="{css}">
</head>
"""


def page(path, title, desc, body, mark="", css="/assets/site.css", extra_nav=""):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in NAV)
    return head(title, desc, path, css) + f"""<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
{picker(1)}
<header class="top">
  <a class="name" href="/">{NAME}</a>
  <nav class="own" aria-label="This site">{nav}</nav>
  <p class="notice" role="note">{NOTICE}</p>
</header>
<main id="main">
{f'<div class="mark">{mark}</div>' if mark else ''}
{body}
</main>
<footer>
<nav class="site-links" aria-label="About this site">
  <a href="/sources/">Sources</a>
  <a href="/designs/">Design directions</a>
  <a href="/start/">Start here</a>
  <a href="/agents/">Use with your AI</a>
  <a href="/admin/">How this site was made</a>
  <a href="/policy/">How this site is governed</a>
</nav>
<p>{NOTICE} Every statement about TauGuard cites the tauguard.ai page it came from and the date it was read. RiskMandate statements cite riskmandate.ai, as it states them. Anything marked Proposal is ours, not agreed with TauGuard and not built.</p>
A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Company__TauGuard">github.com/SovereignWebsite/Site__Company__TauGuard</a>.
</footer>
</body>
</html>
"""


# ---------- inline SVG helpers ----------
_N = [0]


class Svg:
    """A small drawing: boxes, arrows, labels, in a fixed viewBox. Text width is checked so nothing overflows."""

    def __init__(self, w, h, title, desc):
        self.w, self.h, self.title, self.desc, self.parts = w, h, title, desc, []
        _N[0] += 1
        self.n = _N[0]

    def _fit(self, lines, w, size):
        for ln in lines:
            if len(ln) * size * 0.56 > w - 14:
                raise ValueError(f"text too wide for box ({w}px, {size}px): {ln!r}")

    def box(self, x, y, w, h, lines, cls="n", size=14, sub=None):
        """lines: first is bold; sub: lines in smaller type."""
        sub = sub or []
        self._fit(lines, w, size)
        self._fit(sub, w, size - 2)
        n = len(lines) + len(sub)
        lh = size + 4
        top = y + (h - n * lh) / 2 + size
        t = []
        for i, ln in enumerate(lines):
            t.append(f'<text x="{x + w / 2}" y="{top + i * lh}" text-anchor="middle" class="b" font-size="{size}">{html.escape(ln)}</text>')
        for j, ln in enumerate(sub):
            t.append(f'<text x="{x + w / 2}" y="{top + (len(lines) + j) * lh}" text-anchor="middle" class="s" font-size="{size - 2}">{html.escape(ln)}</text>')
        self.parts.append(f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>{"".join(t)}</g>')

    def text(self, x, y, s, size=13, anchor="start", cls="s"):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{html.escape(s)}</text>')

    def arrow(self, x1, y1, x2, y2, cls="ar"):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" marker-end="url(#ah{self.n})"/>')

    def path(self, d, cls="ar", arrow=True):
        self.parts.append(f'<path d="{d}" class="{cls}" fill="none"{f" marker-end=\"url(#ah{self.n})\"" if arrow else ""}/>')

    def line(self, x1, y1, x2, y2, cls="bd"):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>')

    def zone(self, x, y, w, h, label, cls="zt"):
        self.parts.append(f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/><text x="{x + 12}" y="{y + 20}" class="zl" font-size="13">{html.escape(label)}</text></g>')

    def render(self, caption=""):
        defs = f'<defs><marker id="ah{self.n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="ahp"/></marker></defs>'
        svg = (f'<svg viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="t{self.n} d{self.n}" xmlns="http://www.w3.org/2000/svg">'
               f'<title id="t{self.n}">{html.escape(self.title)}</title><desc id="d{self.n}">{html.escape(self.desc)}</desc>{defs}{"".join(self.parts)}</svg>')
        cap = f"<figcaption>{caption}</figcaption>" if caption else ""
        return f'<figure class="fig" tabindex="0" aria-label="{html.escape(self.title)}. On a narrow screen this diagram scrolls sideways."><p class="swipe" aria-hidden="true">Swipe to see the whole drawing</p>{svg}{cap}</figure>'


def flow(title, desc, steps, cls_for=None, w=900, size=12, caption="", h=None):
    """A left-to-right row of boxes with arrows. A step is a string or a list: items starting with ~ are small print."""
    n = len(steps)
    gap = 26
    bw = (w - 20 - gap * (n - 1)) / n
    bh = 84
    s = Svg(w, h or bh + 24, title, desc)
    for i, st in enumerate(steps):
        x = 10 + i * (bw + gap)
        c = (cls_for or {}).get(i, "n")
        items = st if isinstance(st, list) else [st]
        main = [t for t in items if not t.startswith("~")]
        sub = [t[1:] for t in items if t.startswith("~")]
        s.box(x, 12, bw, bh, main, cls=c, size=size + 1, sub=sub)
        if i < n - 1:
            s.arrow(x + bw + 2, 12 + bh / 2, x + bw + gap - 3, 12 + bh / 2)
    return s.render(caption)


_T = [0]


def table(rows, head_cells, cls="tbl"):
    _T[0] += 1
    th = "".join(f"<th scope=\"col\">{c}</th>" for c in head_cells)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw" tabindex="0" role="region" aria-label="Table {_T[0]}. On a narrow screen it scrolls sideways."><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'




# ---------- the design picker: shown at the top of every page until the owner picks a design ----------
PICKER_ON = True
_R = lambda x, y, w, h, c: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" class="{c}"/>'
THUMBS = {
    1: "".join([_R(1, 1, 118, 74, "tp-bg"), _R(6, 6, 108, 5, "tp-fg"), _R(6, 16, 62, 7, "tp-ac"), _R(6, 28, 100, 3, "tp-fg"), _R(6, 34, 88, 3, "tp-fg"),
                _R(6, 42, 52, 26, "tp-tg"), _R(62, 42, 52, 26, "tp-rm")]),
    2: "".join([_R(1, 1, 118, 74, "tp-bg"), _R(6, 6, 24, 64, "tp-tg")] + [_R(9, 12 + i * 9, 18, 3, "tp-fg") for i in range(5)] +
               [_R(36, 6, 78, 10, "tp-ac"), _R(36, 20, 78, 22, "tp-fg"), _R(36, 46, 78, 10, "tp-fg"), _R(36, 60, 78, 10, "tp-fg")]),
    3: "".join([_R(1, 1, 118, 74, "tp-bg"), _R(6, 6, 52, 64, "tp-tg"), _R(62, 6, 52, 64, "tp-rm"), '<rect x="58" y="4" width="4" height="68" class="tp-bd"/>'] +
               [_R(10, 14 + i * 9, 40, 3, "tp-fg") for i in range(5)] + [_R(66, 14 + i * 9, 40, 3, "tp-fg") for i in range(5)]),
    4: "".join([_R(1, 1, 118, 74, "tp-bg"), _R(6, 6, 70, 7, "tp-ac"), _R(6, 18, 100, 3, "tp-fg")] +
               [_R(6 + i * 18, 27, 16, 8, "tp-ac" if i == 0 else "tp-tg") for i in range(6)] + [_R(6, 38, 108, 32, "tp-fg")]),
    5: "".join(['<rect x="1" y="1" width="118" height="74" rx="2" class="tp-dk"/>'] + [f'<line x1="{x}" y1="1" x2="{x}" y2="75" class="tp-gr"/>' for x in range(13, 120, 12)] +
               [f'<line x1="1" y1="{y}" x2="119" y2="{y}" class="tp-gr"/>' for y in range(13, 76, 12)] +
               [f'<rect x="{6 + i * 28}" y="6" width="24" height="10" class="tp-tl"/>' for i in range(4)] + ['<rect x="6" y="22" width="108" height="48" class="tp-sh"/>']),
}
DESIGNS = [(1, "Paper", "One page per topic"), (2, "Atlas", "All on one scroll"), (3, "Ledger", "Two columns"), (4, "Briefing", "Tabs, one topic at a time"), (5, "Blueprint", "Drawn like sheets")]


def picker(current=1):
    if not PICKER_ON:
        return ""
    items = []
    for n, name, note in DESIGNS:
        cur = ' aria-current="page"' if n == current else ""
        tag = "Live now" if n == 1 else "Preview"
        items.append(f'<li><a href="/designs/{n}/"{cur}><svg viewBox="0 0 120 76" aria-hidden="true" focusable="false">{THUMBS[n]}</svg>'
                     f'<span class="pn"><strong>{n} {name}</strong> <span class="pt">{tag}</span></span><span class="pd">{note}</span></a></li>')
    return (f'<nav class="picker" aria-label="Choose a design"><p class="ph"><strong>Choose a design.</strong> The owner has not picked yet; every page uses design 1 until then. '
            f'<a href="/designs/">About the five</a></p><ul>{"".join(items)}</ul></nav>')


PROPOSAL = '<span class="tag prop">Proposal</span>'
