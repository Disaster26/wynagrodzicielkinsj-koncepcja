import os, math
d = os.path.dirname(os.path.abspath(__file__))
r = lambda f: open(os.path.join(d, f), encoding='utf-8').read()

HEART = 'M0 34C-30 14-46-6-44-22-42-36-30-44-18-42-9-41-3-35 0-28 3-35 9-41 18-42 30-44 42-36 44-22 46-6 30 14 0 34Z'
FLAME = 'M-16-38C-20-50-12-56-10-66-6-58-4-52-2-60 0-70 4-74 6-80 8-70 6-62 10-56 12-62 16-64 18-70 22-58 18-48 16-38Z'


def tarcza():
    """Tarcza 24 godzin z sercem, jak na znaku Zgromadzenia."""
    p = []
    for i in range(24):
        a = math.radians(i * 15 - 90)
        # promienie od serca
        x1, y1 = 70 * math.cos(a), 70 * math.sin(a)
        x2, y2 = 150 * math.cos(a), 150 * math.sin(a)
        p.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
        # kreska godziny
        x3, y3 = 162 * math.cos(a), 162 * math.sin(a)
        x4, y4 = 170 * math.cos(a), 170 * math.sin(a)
        p.append(f'<line class="t" x1="{x3:.1f}" y1="{y3:.1f}" x2="{x4:.1f}" y2="{y4:.1f}"/>')
    nums = []
    for i in range(24):
        h = 24 if i == 0 else i
        a = math.radians(i * 15 - 90)
        x, y = 188 * math.cos(a), 188 * math.sin(a) + 6
        nums.append(f'<text x="{x:.1f}" y="{y:.1f}">{h}</text>')
    return f'''<svg class="tarcza" viewBox="-215 -215 430 430" role="img" aria-label="Tarcza 24 godzin z Najświętszym Sercem Jezusa, jak na znaku Zgromadzenia">
<circle r="208" class="o"/><circle r="176" class="o2"/>
<g class="pr">{''.join(p)}</g>
<g class="nr">{''.join(nums)}</g>
<g transform="translate(0 14) scale(1.25)"><path class="pl" d="{FLAME}"/><path class="se" d="{HEART}"/><rect class="kr" x="-2.2" y="-98" width="4.4" height="20" rx="1"/><rect class="kr" x="-7.5" y="-92" width="15" height="4.2" rx="1"/></g>
</svg>'''


def promienie():
    """Promienie za tekstem pierwszego ekranu."""
    p = []
    for i in range(48):
        a = math.radians(i * 7.5)
        r1 = 120
        r2 = 900 if i % 2 == 0 else 640
        p.append(f'<line x1="{r1*math.cos(a):.0f}" y1="{r1*math.sin(a):.0f}" x2="{r2*math.cos(a):.0f}" y2="{r2*math.sin(a):.0f}"/>')
    return f'<svg class="promienie" viewBox="-900 -900 1800 1800" aria-hidden="true" preserveAspectRatio="xMidYMid slice"><g>{"".join(p)}</g></svg>'


def znak():
    """Maly znak: serce z promieniami (separator sekcji)."""
    p = []
    for i in range(24):
        a = math.radians(i * 15 - 90)
        p.append(f'<line x1="{30*math.cos(a):.1f}" y1="{30*math.sin(a):.1f}" x2="{(46 if i%2==0 else 40)*math.cos(a):.1f}" y2="{(46 if i%2==0 else 40)*math.sin(a):.1f}"/>')
    return f'<symbol id="znak" viewBox="-50 -50 100 100"><g class="zp">{"".join(p)}</g><path class="zs" transform="translate(0 2) scale(.52)" d="{HEART}"/></symbol>'


s = r('src.html')
s = s.replace('{{TARCZA}}', tarcza())
s = s.replace('{{PROMIENIE}}', promienie())
s = s.replace('{{ZNAK}}', znak())
s = s.replace('{{BADGE_STYLE}}', r('badge_style.part').replace('<style>', '').replace('</style>', '').strip())
s = s.replace('{{BADGE_LINK}}', r('badge_link.part').strip())
open(os.path.join(d, 'index.html'), 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(s))
