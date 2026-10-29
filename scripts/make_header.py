"""Generates the stone-crack header SVGs (dark + light). Run: python scripts/make_header.py"""
from pathlib import Path

THEMES = {
    "dark": dict(bg="#0D1117", stone="#1A1E1A", stone2="#262B26", seam="#0A0D0A",
                 text="#E8EDE6", muted="#9AA39A", green="#5FD068", moss="#2E7D32"),
    "light": dict(bg="#F2F5F0", stone="#DCE1D8", stone2="#C9CFC4", seam="#AEB5A9",
                  text="#151A15", muted="#5B645B", green="#2E9E3E", moss="#2E7D32"),
}

# One jagged petrification crack running across the slab
CRACK = ("M0,182 L38,176 L61,186 L104,171 L119,178 L163,150 L181,158 L214,141 "
         "L247,147 L259,128 L301,136 L322,119 L337,125 L388,112 L403,121 L447,108 "
         "L472,114 L489,97 L533,109 L561,103 L578,118 L626,110 L668,121 L691,112 "
         "L739,129 L752,122 L806,138 L839,131 L861,144 L912,139 L948,151 L967,146 "
         "L1013,158 L1046,150 L1072,163 L1118,157 L1149,168 L1200,163")
BRANCHES = ["M259,128 L250,106 L261,91", "M578,118 L590,146 L583,166",
            "M861,144 L874,171 L866,188", "M119,178 L127,206 L118,226",
            "M489,97 L498,123 L491,139", "M1072,163 L1086,188", "M739,129 L733,104 L741,93"]

SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"


def svg(t):
    branches = "\n    ".join(f'<path d="{b}"/>' for b in BRANCHES)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340" role="img" aria-label="Shaurya Verma: Kingdom of Science, AGI division">
  <defs>
    <filter id="grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="7" result="n"/>
      <feColorMatrix in="n" type="saturate" values="0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.10"/></feComponentTransfer>
      <feComposite in2="SourceGraphic" operator="in"/>
    </filter>
    <filter id="glow" x="-10%" y="-50%" width="120%" height="200%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="slab" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{t['stone2']}"/><stop offset="1" stop-color="{t['stone']}"/>
    </linearGradient>
    <clipPath id="card"><rect x="0" y="0" width="1200" height="340" rx="18"/></clipPath>
    <style>
      .pulse {{ animation: pulse 3.2s ease-in-out infinite; }}
      .blink {{ animation: blink 1.1s steps(1) infinite; }}
      @keyframes pulse {{ 0%,100% {{ opacity: .55 }} 50% {{ opacity: 1 }} }}
      @keyframes blink {{ 50% {{ opacity: 0 }} }}
      @media (prefers-reduced-motion: reduce) {{ .pulse, .blink {{ animation: none }} }}
    </style>
  </defs>
  <g clip-path="url(#card)">
    <rect width="1200" height="340" fill="url(#slab)"/>
    <rect width="1200" height="340" fill="{t['text']}" filter="url(#grain)"/>
    <!-- faint chalkboard equations -->
    <g font-family="{MONO}" font-size="15" fill="{t['muted']}" opacity="0.35">
      <text x="905" y="250">∇·E = ρ/ε₀</text>
      <text x="960" y="282">H(X) = −Σ p log p</text>
      <text x="1010" y="314">CaCO₃ + HNO₃</text>
      <text x="845" y="226">P(goal | plan)</text>
    </g>
    <!-- the crack: dark seam + glowing green core -->
    <g fill="none" stroke-linejoin="miter" stroke-linecap="square">
      <path d="{CRACK}" stroke="{t['seam']}" stroke-width="7"/>
      <g stroke="{t['seam']}" stroke-width="4">
    {branches}
      </g>
      <g class="pulse" filter="url(#glow)" stroke="{t['green']}">
        <path d="{CRACK}" stroke-width="2.2"/>
        <g stroke-width="1.4">
    {branches}
        </g>
      </g>
    </g>
    <!-- title block -->
    <text x="64" y="72" font-family="{MONO}" font-size="15" letter-spacing="4" fill="{t['green']}">KINGDOM OF SCIENCE  //  AGI DIVISION</text>
    <text x="60" y="258" font-family="{SANS}" font-size="74" font-weight="800" letter-spacing="-1" fill="{t['text']}">Shaurya Verma</text>
    <text x="64" y="298" font-family="{MONO}" font-size="17" fill="{t['muted']}">bluber · founder @ SHV Groups · Eunoia Labs · IIT Madras ’29<tspan class="blink" fill="{t['green']}"> ▌</tspan></text>
    <!-- confidence stamp -->
    <g transform="translate(1136 58)" text-anchor="end" font-family="{MONO}">
      <text font-size="12" letter-spacing="3" fill="{t['muted']}">CONFIDENCE</text>
      <text y="26" font-size="20" font-weight="700" fill="{t['green']}">10,000,000,000%</text>
    </g>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="339" rx="18" fill="none" stroke="{t['seam']}"/>
</svg>
'''


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        (out / f"header-{name}.svg").write_text(svg(t), encoding="utf-8")
        print("wrote", out / f"header-{name}.svg")
