#!/usr/bin/env python3
"""DeFuzz — main method-overview figure.

Style: IEEE S&P academic, restrained pastel palette, iconography per node.
Renders one SVG (2:1) that can be converted to PDF via
    cairosvg method-overview.svg -o ../method-overview.pdf
or (preferred vector fidelity)
    inkscape --export-type=pdf method-overview.svg
"""
from __future__ import annotations
import os
import textwrap
from pathlib import Path

# ------------------------------------------------------------------------------
# Canvas
# ------------------------------------------------------------------------------
W, H = 1600, 920
OUT = Path(__file__).resolve().parent.parent / "method-overview.svg"

# ------------------------------------------------------------------------------
# Palette — restrained academic pastels + high-contrast text
# ------------------------------------------------------------------------------
INK       = "#1F2937"   # near-black text/borders
INK_SOFT  = "#4B5563"   # secondary text
GREY      = "#9CA3AF"   # tertiary / dashed
BG        = "#FFFFFF"

# Offline (invariant / oracle) — mint
MINT_BG   = "#E7F5EF"
MINT_LINE = "#0F766E"
MINT_TAG  = "#065F46"

# Instrument (compile & log) — amber
AMBER_BG  = "#FEF3C7"
AMBER_LINE= "#B45309"
AMBER_TAG = "#78350F"

# Agent (LLM loop) — violet
VIOLET_BG = "#EEE9FE"
VIOLET_LINE="#6D28D9"
VIOLET_TAG= "#4C1D95"

# Bug / violation — red
RED_BG    = "#FEE2E2"
RED_LINE  = "#B91C1C"
RED_TAG   = "#7F1D1D"

# Novelty band — soft neutral
BAND_BG   = "#F3F4F6"

# ------------------------------------------------------------------------------
# Utilities
# ------------------------------------------------------------------------------
def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def rect(x, y, w, h, fill=BG, stroke=INK, sw=1.4, rx=10, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{extra}/>'

def text(x, y, s, size=15, weight="normal", fill=INK, anchor="start", family="'Inter', 'Helvetica Neue', Arial, sans-serif", extra=""):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>{esc(s)}</text>'

def multiline(x, y, lines, size=13, weight="normal", fill=INK, anchor="start", lh=1.35, family="'Inter', 'Helvetica Neue', Arial, sans-serif"):
    out = []
    dy = 0
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i*size*lh}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(ln)}</text>')
    return "\n".join(out)

def arrow(x1, y1, x2, y2, color=INK, sw=1.8, dash=None, marker="url(#arrow)"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{d} marker-end="{marker}"/>'

def path(d, stroke=INK, sw=1.8, fill="none", dash=None, marker="url(#arrow)", extra=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    me = f' marker-end="{marker}"' if marker else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round"{da}{me}{extra}/>'

def circled_num(cx, cy, n, r=14, fill=INK, tcolor="#FFFFFF"):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'
            f'<text x="{cx}" y="{cy+5}" font-family="Inter, sans-serif" font-size="15" font-weight="700" '
            f'fill="{tcolor}" text-anchor="middle">{n}</text>')

# ------------------------------------------------------------------------------
# Iconography (inline SVG — no external assets required)
# ------------------------------------------------------------------------------
def icon_llm(cx, cy, s=1.0, color=MINT_TAG):
    """Sparkle / 4-point-star chat glyph (LLM)."""
    return f'''
    <g transform="translate({cx-16*s},{cy-16*s}) scale({s})">
      <path d="M16 0 L18.8 12.4 L31.2 15.3 L18.9 18.8 L15.9 31.4 L13.1 18.9 L0.6 15.6 L13.2 12.6 Z"
            fill="{color}" opacity="0.95"/>
      <circle cx="26" cy="6" r="2.6" fill="{color}" opacity="0.55"/>
      <circle cx="4" cy="26" r="1.8" fill="{color}" opacity="0.55"/>
    </g>'''

def icon_book(cx, cy, s=1.0, color=MINT_TAG):
    """Corpus / knowledge book."""
    return f'''
    <g transform="translate({cx-16*s},{cy-14*s}) scale({s})">
      <path d="M2 4 Q2 2 4 2 L14 2 Q16 2 16 4 L16 24 Q16 22 14 22 L4 22 Q2 22 2 24 Z" fill="{color}" opacity="0.9"/>
      <path d="M16 4 Q16 2 18 2 L28 2 Q30 2 30 4 L30 24 Q30 22 28 22 L18 22 Q16 22 16 24 Z" fill="{color}" opacity="0.7"/>
      <line x1="5" y1="8" x2="13" y2="8" stroke="#fff" stroke-width="1"/>
      <line x1="5" y1="12" x2="13" y2="12" stroke="#fff" stroke-width="1"/>
      <line x1="5" y1="16" x2="10" y2="16" stroke="#fff" stroke-width="1"/>
      <line x1="19" y1="8" x2="27" y2="8" stroke="#fff" stroke-width="1"/>
      <line x1="19" y1="12" x2="27" y2="12" stroke="#fff" stroke-width="1"/>
      <line x1="19" y1="16" x2="24" y2="16" stroke="#fff" stroke-width="1"/>
    </g>'''

def icon_shield(cx, cy, s=1.0, color=MINT_TAG):
    """Security invariant shield with check."""
    return f'''
    <g transform="translate({cx-14*s},{cy-14*s}) scale({s})">
      <path d="M14 1 L26 5 L26 14 Q26 22 14 27 Q2 22 2 14 L2 5 Z"
            fill="{color}" opacity="0.95"/>
      <path d="M8 14 L12.5 18.5 L20 10" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''

def icon_wrench(cx, cy, s=1.0, color=AMBER_TAG):
    """Wrench for MCP tool."""
    return f'''
    <g transform="translate({cx-14*s},{cy-14*s}) scale({s})">
      <path d="M22 2 A9 9 0 0 0 12 15 L1 26 L4 29 L15 18 A9 9 0 0 0 28 8 L22 14 L18 10 Z"
            fill="{color}" opacity="0.95"/>
    </g>'''

def icon_gear(cx, cy, s=1.0, color=AMBER_TAG):
    """Compiler / instrumentation gear."""
    teeth = ""
    import math
    for i in range(8):
        a = i * math.pi / 4
        x = 14 + 12.5*math.cos(a); y = 14 + 12.5*math.sin(a)
        teeth += f'<rect x="{x-2.6:.2f}" y="{y-2.6:.2f}" width="5.2" height="5.2" transform="rotate({i*45:.0f} {x:.2f} {y:.2f})" fill="{color}" opacity="0.9"/>'
    return f'''
    <g transform="translate({cx-14*s},{cy-14*s}) scale({s})">
      {teeth}
      <circle cx="14" cy="14" r="9.5" fill="{color}"/>
      <circle cx="14" cy="14" r="4" fill="#fff"/>
    </g>'''

def icon_tag(cx, cy, s=1.0, color=AMBER_TAG):
    """Tag / label for log ID."""
    return f'''
    <g transform="translate({cx-14*s},{cy-12*s}) scale({s})">
      <path d="M2 12 L14 2 L28 2 L28 16 L16 26 Z" fill="{color}" opacity="0.95"/>
      <circle cx="22" cy="8" r="2.4" fill="#fff"/>
    </g>'''

def icon_robot(cx, cy, s=1.0, color=VIOLET_TAG):
    """Agent robot head."""
    return f'''
    <g transform="translate({cx-16*s},{cy-16*s}) scale({s})">
      <rect x="4" y="8" width="24" height="20" rx="4" fill="{color}"/>
      <rect x="8" y="12" width="16" height="8" rx="2" fill="#fff"/>
      <circle cx="12" cy="16" r="1.8" fill="{color}"/>
      <circle cx="20" cy="16" r="1.8" fill="{color}"/>
      <rect x="14" y="22" width="4" height="4" rx="1" fill="#fff"/>
      <line x1="16" y1="4" x2="16" y2="8" stroke="{color}" stroke-width="2"/>
      <circle cx="16" cy="3.2" r="1.8" fill="{color}"/>
    </g>'''

def icon_brain(cx, cy, s=1.0, color=VIOLET_TAG):
    """Feedback brain."""
    return f'''
    <g transform="translate({cx-16*s},{cy-14*s}) scale({s})">
      <path d="M8 6 Q4 6 4 12 Q1 14 3 18 Q1 22 6 24 Q8 28 14 26 Q16 28 18 26 Q24 28 26 24 Q31 22 29 18 Q31 14 28 12 Q28 6 24 6 Q22 3 16 4 Q10 3 8 6 Z"
            fill="{color}" opacity="0.95"/>
      <path d="M16 6 L16 26 M10 12 Q13 14 16 12 Q19 14 22 12 M10 18 Q13 20 16 18 Q19 20 22 18"
            stroke="#fff" stroke-width="1.2" fill="none"/>
    </g>'''

def icon_bug(cx, cy, s=1.0, color=RED_TAG):
    """Confirmed violation / bug."""
    return f'''
    <g transform="translate({cx-14*s},{cy-14*s}) scale({s})">
      <ellipse cx="14" cy="16" rx="8" ry="10" fill="{color}"/>
      <path d="M14 6 L11 3 M14 6 L17 3" stroke="{color}" stroke-width="2" fill="none"/>
      <path d="M6 12 L2 10 M6 16 L1 16 M6 20 L2 22 M22 12 L26 10 M22 16 L27 16 M22 20 L26 22"
            stroke="{color}" stroke-width="2" fill="none"/>
      <circle cx="11" cy="12" r="1.4" fill="#fff"/>
      <circle cx="17" cy="12" r="1.4" fill="#fff"/>
    </g>'''

def icon_code(cx, cy, s=1.0, color=VIOLET_TAG):
    """C/C++ code block glyph."""
    return f'''
    <g transform="translate({cx-14*s},{cy-12*s}) scale({s})">
      <rect x="2" y="2" width="24" height="22" rx="3" fill="#fff" stroke="{color}" stroke-width="1.6"/>
      <path d="M9 8 L5 12 L9 16 M17 8 L21 12 L17 16 M14 8 L11 16"
            stroke="{color}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''

def icon_graph(cx, cy, s=1.0, color=AMBER_TAG):
    """Call-graph nodes."""
    return f'''
    <g transform="translate({cx-16*s},{cy-14*s}) scale({s})">
      <line x1="6" y1="6" x2="16" y2="14" stroke="{color}" stroke-width="1.6"/>
      <line x1="16" y1="14" x2="26" y2="6" stroke="{color}" stroke-width="1.6"/>
      <line x1="16" y1="14" x2="10" y2="24" stroke="{color}" stroke-width="1.6"/>
      <line x1="16" y1="14" x2="22" y2="24" stroke="{color}" stroke-width="1.6"/>
      <circle cx="6"  cy="6"  r="3.2" fill="{color}"/>
      <circle cx="16" cy="14" r="3.6" fill="{color}"/>
      <circle cx="26" cy="6"  r="3.2" fill="{color}"/>
      <circle cx="10" cy="24" r="3.2" fill="{color}"/>
      <circle cx="22" cy="24" r="3.2" fill="{color}"/>
    </g>'''

def icon_db(cx, cy, s=1.0, color=MINT_TAG):
    """RAG database cylinder."""
    return f'''
    <g transform="translate({cx-12*s},{cy-14*s}) scale({s})">
      <ellipse cx="12" cy="4" rx="10" ry="3.2" fill="{color}"/>
      <path d="M2 4 L2 22 Q2 25.2 12 25.2 Q22 25.2 22 22 L22 4" fill="{color}"/>
      <ellipse cx="12" cy="4" rx="10" ry="3.2" fill="#fff" opacity="0.35"/>
      <path d="M2 12 Q12 15.2 22 12 M2 18 Q12 21.2 22 18" stroke="#fff" stroke-width="1.2" fill="none"/>
    </g>'''

def chip(x, y, w, h, label, bg=None, tag=INK, sw=1):
    if bg is None: bg = "#FFFFFF"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{bg}" stroke="{tag}" stroke-width="{sw}"/>'
            f'<text x="{x+w/2}" y="{y+h/2+4.4}" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="{tag}" text-anchor="middle">{esc(label)}</text>')

# ------------------------------------------------------------------------------
# Compose SVG
# ------------------------------------------------------------------------------
parts = []
parts.append(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Inter, Helvetica Neue, Arial, sans-serif">
<defs>
  <!-- Arrowheads -->
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 L2 5 Z" fill="{INK}"/>
  </marker>
  <marker id="arrow-mint" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 L2 5 Z" fill="{MINT_LINE}"/>
  </marker>
  <marker id="arrow-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 L2 5 Z" fill="{AMBER_LINE}"/>
  </marker>
  <marker id="arrow-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 L2 5 Z" fill="{VIOLET_LINE}"/>
  </marker>
  <marker id="arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 L2 5 Z" fill="{RED_LINE}"/>
  </marker>
  <marker id="arrow-grey" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 0 L10 5 L0 10 L2 5 Z" fill="{GREY}"/>
  </marker>
  <!-- Subtle drop-shadow for panels -->
  <filter id="soft" x="-5%" y="-5%" width="110%" height="115%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="1.2"/>
    <feOffset dx="0" dy="1" result="off"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.15"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
''')

# ---------------- Title & lane labels ---------------------------
# Lane label (left)
parts.append(f'<g transform="translate(28,60)">'
             f'<rect x="0" y="0" width="16" height="260" rx="4" fill="{MINT_LINE}" opacity="0.88"/>'
             f'<text x="8" y="130" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" '
             f'text-anchor="middle" transform="rotate(-90 8 130)" letter-spacing="3">OFFLINE  ·  INVARIANT KNOWLEDGE</text>'
             f'</g>')

parts.append(f'<g transform="translate(28,470)">'
             f'<rect x="0" y="0" width="16" height="330" rx="4" fill="{VIOLET_LINE}" opacity="0.92"/>'
             f'<text x="8" y="170" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" '
             f'text-anchor="middle" transform="rotate(-90 8 170)" letter-spacing="3">ONLINE  ·  AGENTIC FUZZING LOOP</text>'
             f'</g>')

# Top-row bounding hint (subtle band)
parts.append(rect(60, 60, W-90, 260, fill=MINT_BG, stroke="none", rx=14, extra=' opacity="0.35"'))

# Bottom-row novelty band (dashed border, "Agentic Fuzzing Loop")
parts.append(rect(60, 470, W-90, 330, fill=VIOLET_BG, stroke=VIOLET_LINE, sw=1.6, rx=16, dash="8 6", extra=' opacity="0.9"'))

# ============================ TOP ROW — 4 offline stages ============================
# Layout: 4 boxes evenly spaced within x=[70..1550], y=[80..300]
top_y = 80; top_h = 240
box_w = 330; gap = (W - 90 - 60 - 4*box_w) / 3
xs = []
x0 = 70
for i in range(4):
    xs.append(x0 + i*(box_w + gap))

# ---------- ① Invariant Generation ----------
x, y = xs[0], top_y
parts.append(rect(x, y, box_w, top_h, fill="#FFFFFF", stroke=MINT_LINE, sw=1.8, rx=12, extra=' filter="url(#soft)"'))
parts.append(circled_num(x+22, y+22, "1", r=15, fill=MINT_LINE))
parts.append(text(x+46, y+27, "Invariant Generation", size=17, weight="700", fill=INK))
parts.append(text(x+46, y+46, "corpus-grounded CoT + historical-bug RAG", size=12, fill=INK_SOFT))

# Inside icons
parts.append(icon_book(x+50, y+95, s=1.0, color=MINT_TAG))
parts.append(text(x+82, y+92, "Compiler source · ABI/ISA specs", size=12, weight="600", fill=INK))
parts.append(text(x+82, y+108, "prior CVEs / silent-fix commits", size=11, fill=INK_SOFT))

parts.append(icon_db(x+56, y+145, s=1.0, color=MINT_TAG))
parts.append(text(x+82, y+142, "RAG retrieval  →  root-cause probes", size=12, weight="600", fill=INK))
parts.append(text(x+82, y+158, "segmented CoT  →  candidate invariants", size=11, fill=INK_SOFT))

# Output pill "Invariant Catalog"
parts.append(rect(x+40, y+185, box_w-80, 36, fill=MINT_BG, stroke=MINT_LINE, sw=1.4, rx=18))
parts.append(text(x+box_w/2, y+208, "Invariant Catalog  ϕ₁, ϕ₂, …, ϕₙ", size=13, weight="700", fill=MINT_TAG, anchor="middle"))

# ---------- ② Checker Construction ----------
x, y = xs[1], top_y
parts.append(rect(x, y, box_w, top_h, fill="#FFFFFF", stroke=MINT_LINE, sw=1.8, rx=12, extra=' filter="url(#soft)"'))
parts.append(circled_num(x+22, y+22, "2", r=15, fill=MINT_LINE))
parts.append(text(x+46, y+27, "Checker Construction", size=17, weight="700", fill=INK))
parts.append(text(x+46, y+46, "invariant  →  initial oracle (per ISA)", size=12, fill=INK_SOFT))

# Two checker cards
card_y = y+76
# Static
parts.append(rect(x+22, card_y, 140, 62, fill=MINT_BG, stroke=MINT_LINE, sw=1.2, rx=8))
parts.append(icon_shield(x+42, card_y+18, s=0.7, color=MINT_LINE))
parts.append(text(x+65, card_y+16, "Static", size=13, weight="700", fill=MINT_TAG))
parts.append(text(x+65, card_y+32, "AST/IR audit", size=11, fill=INK_SOFT))
parts.append(text(x+34, card_y+52, "pre-compile scan", size=11, fill=INK_SOFT))
# Dynamic
parts.append(rect(x+168, card_y, 140, 62, fill=MINT_BG, stroke=MINT_LINE, sw=1.2, rx=8))
parts.append(icon_shield(x+188, card_y+18, s=0.7, color=MINT_LINE))
parts.append(text(x+211, card_y+16, "Dynamic", size=13, weight="700", fill=MINT_TAG))
parts.append(text(x+211, card_y+32, "runtime probe", size=11, fill=INK_SOFT))
parts.append(text(x+178, card_y+52, "verdict at exec.", size=11, fill=INK_SOFT))

# Verdict states
parts.append(text(x+box_w/2, y+164, "four-state verdict + evidence", size=12, weight="600", fill=INK, anchor="middle"))
states = [("PASS","#059669"),("FAIL","#DC2626"),("N/A","#6B7280"),("ERR","#B45309")]
sw = 55; sx = x+ (box_w - sw*4 - 8*3)/2
for i,(s,c) in enumerate(states):
    parts.append(rect(sx+i*(sw+8), y+176, sw, 20, fill="#FFFFFF", stroke=c, sw=1.3, rx=10))
    parts.append(text(sx+i*(sw+8)+sw/2, y+191, s, size=11, weight="700", fill=c, anchor="middle"))

# ISA chips
isa_y = y+210
parts.append(text(x+22, isa_y, "target ISA:", size=11, weight="600", fill=INK_SOFT))
for i,(lbl) in enumerate(["x86-64","AArch64","RISC-V"]):
    parts.append(chip(x+96+i*76, isa_y-14, 68, 18, lbl, bg=MINT_BG, tag=MINT_TAG))

# ---------- ③ Source Mapping ----------
x, y = xs[2], top_y
parts.append(rect(x, y, box_w, top_h, fill="#FFFFFF", stroke=AMBER_LINE, sw=1.8, rx=12, extra=' filter="url(#soft)"'))
parts.append(circled_num(x+22, y+22, "3", r=15, fill=AMBER_LINE))
parts.append(text(x+46, y+27, "Source Mapping", size=17, weight="700", fill=INK))
parts.append(text(x+46, y+46, "invariant  →  compiler impl. sites", size=12, fill=INK_SOFT))

# Call-graph glyph
parts.append(icon_graph(x+60, y+118, s=1.1, color=AMBER_TAG))
# Chain: Pass → Fn → Struct/Cond
chain_x = x+118; chain_y=y+82
labels = ["Pass", "Function", "Struct + Cond."]
for i,ln in enumerate(labels):
    yy = chain_y+i*30
    parts.append(rect(chain_x, yy, 170, 22, fill=AMBER_BG, stroke=AMBER_LINE, sw=1.2, rx=6))
    parts.append(text(chain_x+85, yy+15, ln, size=12, weight="700", fill=AMBER_TAG, anchor="middle"))
    if i<len(labels)-1:
        parts.append(arrow(chain_x+85, yy+22, chain_x+85, yy+30-2, color=AMBER_LINE, sw=1.4, marker="url(#arrow-amber)"))

# MCP tool chip
parts.append(icon_wrench(x+40, y+200, s=0.7, color=AMBER_TAG))
parts.append(text(x+60, y+197, "MCP tools:", size=11, weight="700", fill=AMBER_TAG))
parts.append(chip(x+128, y+188, 76, 18, "call-graph", bg=AMBER_BG, tag=AMBER_TAG))
parts.append(chip(x+210, y+188, 100, 18, "file · grep · ast", bg=AMBER_BG, tag=AMBER_TAG))
parts.append(text(x+60, y+215, "free coding agent  (e.g., Claude Code)", size=10.5, fill=INK_SOFT))

# ---------- ④ Log Instrumentation ----------
x, y = xs[3], top_y
parts.append(rect(x, y, box_w, top_h, fill="#FFFFFF", stroke=AMBER_LINE, sw=1.8, rx=12, extra=' filter="url(#soft)"'))
parts.append(circled_num(x+22, y+22, "4", r=15, fill=AMBER_LINE))
parts.append(text(x+46, y+27, "Log Instrumentation", size=17, weight="700", fill=INK))
parts.append(text(x+46, y+46, "unique-ID probes at critical sites", size=12, fill=INK_SOFT))

# Illustration: code with tags
code_x = x+22; code_y = y+74
parts.append(rect(code_x, code_y, box_w-44, 92, fill="#0F172A", stroke=AMBER_LINE, sw=1.4, rx=8))
# code lines
lines_code = [
    ("void  emit_stack_prot ( ) {", "#E5E7EB"),
    ('  DEFUZZ_TAG(\"SPGuard#a3f2\");', "#FCD34D"),
    ("  build_canary(&frame);", "#93C5FD"),
    ('  DEFUZZ_TAG(\"SPGuard#a3f2:hit\");', "#FCD34D"),
    ("  emit_epilogue_check();  }", "#E5E7EB"),
]
for i,(ln,c) in enumerate(lines_code):
    parts.append(f'<text x="{code_x+12}" y="{code_y+18+i*16}" font-family="JetBrains Mono, monospace" font-size="11" fill="{c}">{esc(ln)}</text>')

# Tag & recompile row
parts.append(icon_tag(x+52, y+188, s=0.72, color=AMBER_TAG))
parts.append(text(x+78, y+186, "unique log-ID prefix  ·  optional trace fields", size=11, weight="600", fill=INK))
parts.append(icon_gear(x+52, y+215, s=0.72, color=AMBER_TAG))
parts.append(text(x+78, y+213, "recompile  →  instrumented compiler  I𝒞", size=11, weight="600", fill=INK))

# Arrows between top boxes (horizontal)
for i in range(3):
    x1 = xs[i]+box_w
    x2 = xs[i+1]
    y_mid = top_y + top_h/2
    parts.append(arrow(x1+4, y_mid, x2-6, y_mid, color=INK_SOFT, sw=1.8))

# Row-label chevron on top-right: transition to online loop
# ============================ BOTTOM ROW — online loop ============================
bot_y = 495; bot_h = 290

# Layout: 3 cards + verdict + bug output
# ⑤ Generator (left), Instrumented Compiler (middle-left), Verdict (middle), ⑥ Feedback (right)

# widths chosen for a balanced flow across 60..W-30
gx = 74
gen_w = 320; comp_w = 220; ver_w = 150; fb_w = 320
gap2 = ((W - 30 - gx) - (gen_w+comp_w+ver_w+fb_w)) / 3
gen_x = gx
comp_x = gen_x + gen_w + gap2
ver_x = comp_x + comp_w + gap2
fb_x = ver_x + ver_w + gap2

# ---------- ⑤ Generator Agent ----------
x, y = gen_x, bot_y
parts.append(rect(x, y, gen_w, bot_h, fill="#FFFFFF", stroke=VIOLET_LINE, sw=1.8, rx=12, extra=' filter="url(#soft)"'))
parts.append(circled_num(x+22, y+22, "5", r=15, fill=VIOLET_LINE))
parts.append(text(x+46, y+27, "Generator Agent", size=17, weight="700", fill=INK))
parts.append(text(x+46, y+46, "checker-aware C/C++ seed synthesis", size=12, fill=INK_SOFT))

parts.append(icon_robot(x+60, y+108, s=1.5, color=VIOLET_LINE))
parts.append(icon_llm(x+112, y+82, s=0.55, color=VIOLET_TAG))

# Bullets
bullet_x = x+130; bullet_y = y+90
bullets = [
    ("perceive locked invariant + checker", ""),
    ("propose seed satisfying build & ISA", ""),
    ("on FAIL  →  lateral variant burst", ""),
]
for i,(b,_) in enumerate(bullets):
    parts.append(f'<circle cx="{bullet_x}" cy="{bullet_y-4+i*22}" r="3" fill="{VIOLET_LINE}"/>')
    parts.append(text(bullet_x+10, bullet_y+i*22, b, size=12, fill=INK))

# Seed sample
seed_y = y+188
parts.append(rect(x+22, seed_y, gen_w-44, 76, fill="#0F172A", stroke=VIOLET_LINE, sw=1.4, rx=8))
seed_lines = [
    ("// seed for ϕ (SP-Guard, x86-64)", "#94A3B8"),
    ("void t() { char b[8]; volatile int n=argc*7;", "#E5E7EB"),
    ("  memcpy(b, argv[1], n);  // provoke canary", "#93C5FD"),
    ('  __asm__("nop");  return sink(b); }', "#FCD34D"),
]
for i,(ln,c) in enumerate(seed_lines):
    parts.append(f'<text x="{x+34}" y="{seed_y+16+i*15}" font-family="JetBrains Mono, monospace" font-size="10.5" fill="{c}">{esc(ln)}</text>')

# ---------- Instrumented Compiler node (external) ----------
x, y = comp_x, bot_y + 40
parts.append(rect(x, y, comp_w, bot_h - 80, fill="#F9FAFB", stroke=INK_SOFT, sw=1.6, rx=12, extra=' filter="url(#soft)"'))
parts.append(icon_gear(x+comp_w/2, y+58, s=1.5, color=AMBER_LINE))
parts.append(text(x+comp_w/2, y+108, "Instrumented Compiler", size=14, weight="700", fill=INK, anchor="middle"))
parts.append(text(x+comp_w/2, y+126, "(gcc / clang, log-tagged)", size=11, fill=INK_SOFT, anchor="middle"))

# Verdict pill under compiler
parts.append(rect(x+22, y+150, comp_w-44, 46, fill=BG, stroke=INK, sw=1.4, rx=8))
parts.append(text(x+comp_w/2, y+167, "Execute · Collect", size=12, weight="700", fill=INK, anchor="middle"))
parts.append(text(x+comp_w/2, y+184, "checker verdict + trace", size=11, fill=INK_SOFT, anchor="middle"))

# ---------- Verdict diamond ----------
x, y = ver_x + ver_w/2, bot_y + bot_h/2
# Diamond
d = f"M {x-ver_w/2} {y} L {x} {y-70} L {x+ver_w/2} {y} L {x} {y+70} Z"
parts.append(path(d, stroke=INK, sw=1.8, fill="#FFFFFF", marker=""))
parts.append(text(x, y-4, "Violation?", size=14, weight="700", fill=INK, anchor="middle"))
parts.append(text(x, y+14, "FAIL + evidence", size=11, fill=INK_SOFT, anchor="middle"))

# ---------- ⑥ Feedback Agent ----------
x, y = fb_x, bot_y
parts.append(rect(x, y, fb_w, bot_h, fill="#FFFFFF", stroke=VIOLET_LINE, sw=1.8, rx=12, extra=' filter="url(#soft)"'))
parts.append(circled_num(x+22, y+22, "6", r=15, fill=VIOLET_LINE))
parts.append(text(x+46, y+27, "Feedback Agent", size=17, weight="700", fill=INK))
parts.append(text(x+46, y+46, "diagnostics-aware routing", size=12, fill=INK_SOFT))

parts.append(icon_brain(x+60, y+108, s=1.4, color=VIOLET_LINE))
parts.append(icon_llm(x+112, y+82, s=0.55, color=VIOLET_TAG))

# Diagnostics box
diag_y = y+80
parts.append(rect(x+130, diag_y, fb_w-152, 86, fill=VIOLET_BG, stroke=VIOLET_LINE, sw=1.2, rx=8))
parts.append(text(x+140, diag_y+18, "Signals (via MCP):", size=11, weight="700", fill=VIOLET_TAG))
sig_lines = [
    ("· compiler diagnostics + warnings", INK),
    ("· checker verdict & static evidence", INK),
    ("· critical-condition hit counter", INK),
]
for i,(t,c) in enumerate(sig_lines):
    parts.append(text(x+140, diag_y+36+i*16, t, size=11, fill=c))

# Decision fork
dec_y = y+186
parts.append(rect(x+22, dec_y, fb_w-44, 82, fill=BG, stroke=VIOLET_LINE, sw=1.4, rx=8))
parts.append(text(x+fb_w/2, dec_y+18, "Decide", size=12, weight="700", fill=INK, anchor="middle"))

# Left branch: guide
parts.append(rect(x+34, dec_y+28, 130, 40, fill=VIOLET_BG, stroke=VIOLET_LINE, sw=1.2, rx=6))
parts.append(text(x+99, dec_y+45, "guide next round", size=11, weight="700", fill=VIOLET_TAG, anchor="middle"))
parts.append(text(x+99, dec_y+60, "(seed-space hint)", size=10, fill=INK_SOFT, anchor="middle"))

# Right branch: rewrite checker
parts.append(rect(x+fb_w-34-130, dec_y+28, 130, 40, fill=RED_BG, stroke=RED_LINE, sw=1.2, rx=6))
parts.append(text(x+fb_w-99, dec_y+45, "rewrite checker", size=11, weight="700", fill=RED_TAG, anchor="middle"))
parts.append(text(x+fb_w-99, dec_y+60, "(if votes ≥ τ)", size=10, fill=INK_SOFT, anchor="middle"))

# ============================ Connectors in loop ============================
# ⑤ → Instrumented Compiler   (seed)
parts.append(arrow(gen_x+gen_w+4, bot_y+bot_h/2, comp_x-6, bot_y+bot_h/2, color=INK, sw=2.2))
parts.append(text((gen_x+gen_w+comp_x)/2, bot_y+bot_h/2-10, "C/C++ seed", size=11.5, weight="700", fill=INK, anchor="middle"))

# Compiler → Verdict
parts.append(arrow(comp_x+comp_w+4, bot_y+bot_h/2, ver_x+2, bot_y+bot_h/2, color=INK, sw=2.2))
parts.append(text((comp_x+comp_w+ver_x)/2, bot_y+bot_h/2-10, "verdict", size=11.5, weight="700", fill=INK_SOFT, anchor="middle"))

# Verdict → ⑥ (top-right, PASS/NA path via ⑥)
parts.append(arrow(ver_x+ver_w-2, bot_y+bot_h/2, fb_x-6, bot_y+bot_h/2, color=INK, sw=2.2))
parts.append(text((ver_x+ver_w+fb_x)/2, bot_y+bot_h/2-10, "PASS · N/A · ERR", size=11.5, weight="700", fill=INK_SOFT, anchor="middle"))

# ⑥ → ⑤ next-round guidance (dashed loop-back at bottom, spanning the panel; label on the LEFT
#     half of the curve so it doesn't collide with the FAIL curve on the right).
p1x = fb_x + 99
p2x = gen_x + gen_w - 40
py1 = bot_y + bot_h - 4
py_dip = bot_y + bot_h + 28
parts.append(path(f"M {p1x} {py1} C {p1x} {py_dip+14} {p2x} {py_dip+14} {p2x} {py1}",
                  stroke=VIOLET_LINE, sw=2, fill="none", dash="8 6", marker="url(#arrow-violet)"))
parts.append(text((p1x+p2x)/2 - 180, py_dip+12, "guide next round  ·  lateral exploration on FAIL",
                  size=12, weight="700", fill=VIOLET_TAG, anchor="middle"))

# ⑥ → ② rewrite checker (red arrow routed via FAR RIGHT then across TOP MARGIN, well above content)
# Start from top-right of ⑥ (rewrite branch), go right off card, up to y=~30, then across to ② top-center down.
r_start_x = fb_x + fb_w - 42
r_start_y = bot_y + 4                            # near top of ⑥ card
u_x = W - 40                                     # right margin lane
u_top = 22                                       # top corridor above title
r_end_x = xs[1] + box_w/2 + 40                   # slightly right of ② center to avoid title overlap
r_end_y = top_y - 4                              # just above ② top edge

# Right-side vertical rise, then top-horizontal, then drop into ② top
parts.append(path(
    f"M {r_start_x} {r_start_y} "
    f"L {u_x} {r_start_y} "
    f"L {u_x} {u_top} "
    f"L {r_end_x} {u_top} "
    f"L {r_end_x} {r_end_y}",
    stroke=RED_LINE, sw=2.4, fill="none", dash="10 6", marker="url(#arrow-red)"))
# Label on top corridor
parts.append(text((u_x + r_end_x)/2, u_top - 6, "rewrite checker  (Σ votes ≥ τ)",
                  size=12.5, weight="700", fill=RED_TAG, anchor="middle"))

# Verdict → FAIL → 🐞  (FAIL is routed to the FAR RIGHT to keep the loop-back label uncluttered)
bug_w = 224; bug_h = 66
bug_x = W - 60 - bug_w
bug_y = bot_y + bot_h + 26            # slightly below the loop panel, above the legend area
parts.append(rect(bug_x, bug_y, bug_w, bug_h, fill=RED_BG, stroke=RED_LINE, sw=1.8, rx=10))
parts.append(icon_bug(bug_x+34, bug_y+bug_h/2, s=0.95, color=RED_LINE))
parts.append(text(bug_x+70, bug_y+22, "Confirmed", size=13, weight="700", fill=RED_TAG))
parts.append(text(bug_x+70, bug_y+40, "PoC + potential zero-day", size=11, fill=INK_SOFT))
parts.append(text(bug_x+70, bug_y+55, "human review  ·  regressed corpus", size=10.5, fill=INK_SOFT))

# FAIL red arrow: from the RIGHT tip of the verdict diamond, hooking DOWN-RIGHT into the bug box
fx0 = ver_x + ver_w + 2                # right vertex of diamond
fy0 = bot_y + bot_h/2                  # middle of diamond
fx1 = bug_x - 4                        # left edge of bug box
fy1 = bug_y + bug_h/2                  # middle of bug box
# Cubic curve going right, then down
parts.append(path(f"M {fx0} {fy0} C {fx0+180} {fy0} {fx1-180} {fy1} {fx1} {fy1}",
                  stroke=RED_LINE, sw=2.4, fill="none", marker="url(#arrow-red)"))
# Label on the curve
parts.append(text((fx0+fx1)/2 - 20, (fy0+fy1)/2 - 6, "FAIL + evidence",
                  size=12, weight="700", fill=RED_TAG, anchor="middle"))

# ============================ Vertical bridge: ② → ⑤ (checker) and ④ → compiler ============================
# ② → ⑤ (locked ϕ + checker suite): mint curve, LEFT-oriented
c_start_x = xs[1] + 60
c_start_y = top_y + top_h + 4
c_end_x   = gen_x + gen_w/2
c_end_y   = bot_y - 4
parts.append(path(f"M {c_start_x} {c_start_y} C {c_start_x} {c_start_y+80} {c_end_x} {c_end_y-80} {c_end_x} {c_end_y}",
                  stroke=MINT_LINE, sw=2.2, fill="none", marker="url(#arrow-mint)"))
mid_c_x = (c_start_x + c_end_x)/2 - 30
mid_c_y = (c_start_y + c_end_y)/2
parts.append(rect(mid_c_x-6, mid_c_y-14, 138, 34, fill="#FFFFFF", stroke=MINT_LINE, sw=1.1, rx=6))
parts.append(text(mid_c_x+63, mid_c_y-1, "locked  ϕ  ·  checker", size=11.5, weight="700", fill=MINT_TAG, anchor="middle"))
parts.append(text(mid_c_x+63, mid_c_y+14, "(orchestrator picks)", size=10, fill=INK_SOFT, anchor="middle"))

# ④ → Compiler (instrumented I𝒞): amber curve, RIGHT-oriented, into top of compiler node
b_start_x = xs[3] + box_w/2
b_start_y = top_y + top_h + 4
b_end_x   = comp_x + comp_w/2
b_end_y   = bot_y + 40 - 4
parts.append(path(f"M {b_start_x} {b_start_y} C {b_start_x} {b_start_y+80} {b_end_x} {b_end_y-80} {b_end_x} {b_end_y}",
                  stroke=AMBER_LINE, sw=2.2, fill="none", marker="url(#arrow-amber)"))
mid_b_x = (b_start_x + b_end_x)/2 - 12
mid_b_y = (b_start_y + b_end_y)/2 - 8
parts.append(rect(mid_b_x-6, mid_b_y-14, 158, 34, fill="#FFFFFF", stroke=AMBER_LINE, sw=1.1, rx=6))
parts.append(text(mid_b_x+73, mid_b_y-1, "instrumented compiler  I𝒞", size=11.5, weight="700", fill=AMBER_TAG, anchor="middle"))
parts.append(text(mid_b_x+73, mid_b_y+14, "(gcc / clang, log-tagged)", size=10, fill=INK_SOFT, anchor="middle"))

# Orchestrator note — floated as a small caption inside the gap on the right (below top row)
orch_x = W - 260; orch_y = 400
parts.append(rect(orch_x, orch_y, 210, 46, fill="#FFFFFF", stroke=INK_SOFT, sw=1.2, rx=8, dash="4 4"))
parts.append(text(orch_x+105, orch_y+18, "Orchestrator", size=12, weight="700", fill=INK, anchor="middle"))
parts.append(text(orch_x+105, orch_y+34, "locks one ϕ  ·  equal time budget", size=10.5, fill=INK_SOFT, anchor="middle"))

# Big title at top — pushed down a bit so the red top-corridor label sits cleanly above it
parts.append(text(W/2, 55, "DeFuzz: Invariant-Guided Agentic Testing of Compiler-Instrumented Defenses",
                  size=20, weight="700", fill=INK, anchor="middle"))

# Legend (bottom-left corner to avoid the centered bug PoC card)
lg_x = 60; lg_y = H - 55
parts.append(rect(lg_x, lg_y, 340, 42, fill="#FFFFFF", stroke=INK_SOFT, sw=1, rx=8))
def swatch(x, y, color, label, tw=90):
    return f'<rect x="{x}" y="{y}" width="14" height="14" rx="3" fill="{color}"/><text x="{x+20}" y="{y+12}" font-family="Inter" font-size="10.5" fill="{INK}">{label}</text>'
parts.append(swatch(lg_x+12, lg_y+8, MINT_LINE, "invariant / oracle"))
parts.append(swatch(lg_x+12, lg_y+24, AMBER_LINE, "compiler instrumentation"))
parts.append(swatch(lg_x+180, lg_y+8, VIOLET_LINE, "LLM agent"))
parts.append(swatch(lg_x+180, lg_y+24, RED_LINE, "violation / rewrite"))

parts.append("</svg>")

svg = "\n".join(parts)
OUT.write_text(svg)
print(f"Wrote {OUT}  ({len(svg)} bytes, {svg.count(chr(10))} lines)")
