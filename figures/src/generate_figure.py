#!/usr/bin/env python3
"""
DeFuzz: Invariant-Guided Agentic Testing of Compiler-Instrumented Defenses
Main Method Overview Architecture Diagram Generator (IEEE S&P / USENIX Security Grade)
V3: Clean separation of Decision Diamond, no overlap on Checker Oracle Evaluation header,
    pixel-perfect alignment of all labels, arrows, and code blocks.
"""

import math
import os
from pathlib import Path

W, H = 1680, 1000

# Palette - Restrained academic pastels with high-contrast text
INK_DARK     = "#0F172A"  # Slate 900
INK_TEXT     = "#1E293B"  # Slate 800
INK_MUTED    = "#475569"  # Slate 600
INK_LIGHT    = "#64748B"  # Slate 500
BORDER_BASE  = "#CBD5E1"  # Slate 300

# Phase 1: Invariant & Oracle (Mint / Emerald)
P1_BG        = "#F0FDF4"
P1_CARD      = "#FFFFFF"
P1_BORDER    = "#10B981"
P1_DARK      = "#047857"
P1_HEADER    = "#065F46"
P1_CHIP      = "#D1FAE5"

# Phase 2: Compiler Instrumentation (Amber / Bronze)
P2_BG        = "#FFFBEB"
P2_CARD      = "#FFFFFF"
P2_BORDER    = "#F59E0B"
P2_DARK      = "#B45309"
P2_HEADER    = "#78350F"
P2_CHIP      = "#FEF3C7"

# Phase 3: Online Agentic Loop (Indigo / Violet)
P3_BG        = "#F8FAFC"
P3_CONTAINER = "#FAF5FF"
P3_CARD      = "#FFFFFF"
P3_BORDER    = "#6366F1"
P3_DARK      = "#4338CA"
P3_HEADER    = "#312E81"
P3_CHIP      = "#EDE9FE"

# Feedback & Guidance (Purple / Violet)
LOOP_GUIDE   = "#7C3AED"
LOOP_GUIDE_BG= "#EDE9FE"

# Checker Rewrite (Rose / Crimson)
LOOP_REWRITE = "#E11D48"
LOOP_REWRITE_BG = "#FFE4E6"

# Bug / Violation (Red / Coral)
BUG_BG       = "#FEF2F2"
BUG_BORDER   = "#DC2626"
BUG_TEXT     = "#991B1B"

# Lateral Thinking (Cyan / Teal)
LATERAL_BG   = "#ECFEFF"
LATERAL_BORDER = "#0891B2"
LATERAL_TEXT = "#0E7490"

def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# ----------------- VECTOR LOGOS & ICONS (Pure SVG) -----------------

def logo_gcc(cx, cy, s=1.0):
    """GNU / GCC compiler badge"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <circle cx="12" cy="12" r="11" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/>
      <path d="M7 6 C10 4, 15 5, 17 8 C18 10, 18 14, 16 17 C13 20, 9 19, 7 16 C6 14, 6 10, 8 7 Z" fill="none" stroke="#B45309" stroke-width="2"/>
      <circle cx="12" cy="12" r="3" fill="#D97706"/>
      <text x="12" y="21" font-family="'JetBrains Mono', monospace" font-size="5.5" font-weight="800" fill="#78350F" text-anchor="middle">GCC</text>
    </g>'''

def logo_llvm(cx, cy, s=1.0):
    """LLVM dragon / flame badge"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <circle cx="12" cy="12" r="11" fill="#FFF1F2" stroke="#E11D48" stroke-width="1.5"/>
      <path d="M6 16 C8 11, 10 7, 15 6 C14 9, 15 11, 18 12 C15 13, 14 15, 15 18 C12 16, 9 17, 6 16 Z" fill="#E11D48"/>
      <path d="M12 10 C14 8, 17 8, 19 9 C17 11, 16 13, 16 15" fill="none" stroke="#BE123C" stroke-width="1.2"/>
      <text x="12" y="21" font-family="'JetBrains Mono', monospace" font-size="5.5" font-weight="800" fill="#9F1239" text-anchor="middle">LLVM</text>
    </g>'''

def logo_cpp(cx, cy, s=1.0):
    """C/C++ Shield Logo"""
    return f'''
    <g transform="translate({cx-13*s},{cy-13*s}) scale({s})">
      <polygon points="13,2 24,5 21,20 13,24 5,20 2,5" fill="#1E40AF" stroke="#1D4ED8" stroke-width="1.2"/>
      <polygon points="13,4 22,6.5 19,18.5 13,22 7,18.5 4,6.5" fill="#3B82F6"/>
      <text x="13" y="16" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#FFFFFF" text-anchor="middle">C++</text>
    </g>'''

def logo_mcp(cx, cy, s=1.0):
    """Model Context Protocol (MCP) Logo"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <rect x="2" y="2" width="20" height="20" rx="5" fill="#312E81" stroke="#4F46E5" stroke-width="1.2"/>
      <circle cx="7" cy="7" r="2.2" fill="#A5B4FC"/>
      <circle cx="17" cy="7" r="2.2" fill="#A5B4FC"/>
      <circle cx="12" cy="17" r="2.2" fill="#A5B4FC"/>
      <line x1="7" y1="7" x2="17" y2="7" stroke="#E0E7FF" stroke-width="1.3"/>
      <line x1="7" y1="7" x2="12" y2="17" stroke="#E0E7FF" stroke-width="1.3"/>
      <line x1="17" y1="7" x2="12" y2="17" stroke="#E0E7FF" stroke-width="1.3"/>
      <circle cx="12" cy="10.5" r="1.5" fill="#FFFFFF"/>
    </g>'''

def logo_claude(cx, cy, s=1.0):
    """Claude / Anthropic Sparkle Badge"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <rect x="2" y="2" width="20" height="20" rx="5" fill="#D97706" opacity="0.15"/>
      <path d="M12 2 L14 9 L21 12 L14 15 L12 22 L10 15 L3 12 L10 9 Z" fill="#D97706"/>
      <circle cx="18" cy="5" r="1.5" fill="#F59E0B"/>
      <circle cx="5" cy="18" r="1.2" fill="#F59E0B"/>
    </g>'''

def logo_isa_x86(cx, cy, s=1.0):
    """x86-64 Intel/AMD Architecture Logo"""
    return f'''
    <g transform="translate({cx-18*s},{cy-9*s}) scale({s})">
      <rect x="0" y="0" width="36" height="18" rx="4" fill="#E0F2FE" stroke="#0284C7" stroke-width="1"/>
      <text x="18" y="13" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="800" fill="#0369A1" text-anchor="middle">x86-64</text>
    </g>'''

def logo_isa_arm(cx, cy, s=1.0):
    """ARM / AArch64 Architecture Logo"""
    return f'''
    <g transform="translate({cx-20*s},{cy-9*s}) scale({s})">
      <rect x="0" y="0" width="40" height="18" rx="4" fill="#E0F2FE" stroke="#0284C7" stroke-width="1"/>
      <text x="20" y="13" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="800" fill="#0369A1" text-anchor="middle">AArch64</text>
    </g>'''

def logo_isa_riscv(cx, cy, s=1.0):
    """RISC-V Architecture Logo"""
    return f'''
    <g transform="translate({cx-19*s},{cy-9*s}) scale({s})">
      <rect x="0" y="0" width="38" height="18" rx="4" fill="#E0F2FE" stroke="#0284C7" stroke-width="1"/>
      <text x="19" y="13" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="800" fill="#0369A1" text-anchor="middle">RISC-V</text>
    </g>'''

def icon_shield_security(cx, cy, s=1.0, color="#10B981"):
    """Security Invariant Shield"""
    return f'''
    <g transform="translate({cx-12*s},{cy-13*s}) scale({s})">
      <path d="M12 2 L22 6 L22 13 C22 19 12 24 12 24 C12 24 2 19 2 13 L2 6 Z" fill="{color}" opacity="0.2"/>
      <path d="M12 2 L22 6 L22 13 C22 19 12 24 12 24 C12 24 2 19 2 13 L2 6 Z" fill="none" stroke="{color}" stroke-width="2"/>
      <path d="M7 12 L10 15 L17 8" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''

def icon_rag_db(cx, cy, s=1.0, color="#059669"):
    """RAG Vector Database"""
    return f'''
    <g transform="translate({cx-12*s},{cy-13*s}) scale({s})">
      <ellipse cx="12" cy="5" rx="10" ry="3.5" fill="{color}" opacity="0.3"/>
      <ellipse cx="12" cy="5" rx="10" ry="3.5" fill="none" stroke="{color}" stroke-width="1.5"/>
      <path d="M2 5 L2 19 C2 22.5 22 22.5 22 19 L22 5" fill="none" stroke="{color}" stroke-width="1.5"/>
      <path d="M2 12 C2 15.5 22 15.5 22 12" fill="none" stroke="{color}" stroke-width="1.3"/>
      <circle cx="8" cy="18" r="1.2" fill="{color}"/>
      <circle cx="12" cy="17" r="1.2" fill="{color}"/>
      <circle cx="16" cy="19" r="1.2" fill="{color}"/>
    </g>'''

def icon_callgraph(cx, cy, s=1.0, color="#D97706"):
    """Call Graph Hierarchy"""
    return f'''
    <g transform="translate({cx-14*s},{cy-13*s}) scale({s})">
      <circle cx="14" cy="4" r="3" fill="{color}"/>
      <circle cx="6" cy="16" r="2.8" fill="{color}"/>
      <circle cx="22" cy="16" r="2.8" fill="{color}"/>
      <circle cx="10" cy="24" r="2.2" fill="{color}"/>
      <circle cx="18" cy="24" r="2.2" fill="{color}"/>
      <line x1="14" y1="4" x2="6" y2="16" stroke="{color}" stroke-width="1.5"/>
      <line x1="14" y1="4" x2="22" y2="16" stroke="{color}" stroke-width="1.5"/>
      <line x1="6" y1="16" x2="10" y2="24" stroke="{color}" stroke-width="1.3"/>
      <line x1="22" y1="16" x2="18" y2="24" stroke="{color}" stroke-width="1.3"/>
    </g>'''

def icon_robot_agent(cx, cy, s=1.0, color="#6366F1"):
    """Autonomous AI Agent Robot Head"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <rect x="4" y="7" width="16" height="13" rx="3" fill="{color}" opacity="0.15"/>
      <rect x="4" y="7" width="16" height="13" rx="3" fill="none" stroke="{color}" stroke-width="1.8"/>
      <line x1="12" y1="2" x2="12" y2="7" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="12" cy="2" r="1.5" fill="{color}"/>
      <circle cx="8" cy="12" r="1.6" fill="{color}"/>
      <circle cx="16" cy="12" r="1.6" fill="{color}"/>
      <line x1="8" y1="16" x2="16" y2="16" stroke="{color}" stroke-width="1.3" stroke-linecap="round"/>
    </g>'''

def icon_brain_feedback(cx, cy, s=1.0, color="#8B5CF6"):
    """Cognitive Feedback Brain"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <path d="M6 5 C3 5, 2 8, 2 11 C2 14, 4 17, 5 18 C7 21, 11 21, 12 18 C13 21, 17 21, 19 18 C20 17, 22 14, 22 11 C22 8, 21 5, 18 5 C17 2, 13 2, 12 5 C11 2, 7 2, 6 5 Z" 
            fill="{color}" opacity="0.2" stroke="{color}" stroke-width="1.6"/>
      <path d="M12 5 L12 18 M7 10 Q10 12 12 10 Q14 12 17 10 M7 14 Q10 16 12 14 Q14 16 17 14" 
            fill="none" stroke="{color}" stroke-width="1.2" stroke-linecap="round"/>
    </g>'''

def icon_bug_vuln(cx, cy, s=1.0, color="#DC2626"):
    """Confirmed Bug / Zero-Day Badge"""
    return f'''
    <g transform="translate({cx-13*s},{cy-13*s}) scale({s})">
      <ellipse cx="13" cy="15" rx="7.5" ry="9" fill="{color}"/>
      <circle cx="13" cy="6" r="3.5" fill="{color}"/>
      <line x1="11" y1="4" x2="7" y2="1" stroke="{color}" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="15" y1="4" x2="19" y2="1" stroke="{color}" stroke-width="1.5" stroke-linecap="round"/>
      <line x1="6" y1="12" x2="1" y2="10" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="6" y1="15" x2="1" y2="15" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="6" y1="18" x2="1" y2="20" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="20" y1="12" x2="25" y2="10" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="20" y1="15" x2="25" y2="15" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="20" y1="18" x2="25" y2="20" stroke="{color}" stroke-width="1.6" stroke-linecap="round"/>
      <circle cx="11" cy="6" r="0.9" fill="#FFFFFF"/>
      <circle cx="15" cy="6" r="0.9" fill="#FFFFFF"/>
    </g>'''

def icon_lateral_idea(cx, cy, s=1.0, color="#0891B2"):
    """Lateral Exploration / Diversified Bug Finding"""
    return f'''
    <g transform="translate({cx-13*s},{cy-13*s}) scale({s})">
      <path d="M13 3 C9 3, 6 6, 6 10 C6 13, 8 15, 9 17 L17 17 C18 15, 20 13, 20 10 C20 6, 17 3, 13 3 Z" fill="{color}" opacity="0.25" stroke="{color}" stroke-width="1.5"/>
      <line x1="10" y1="20" x2="16" y2="20" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="11" y1="23" x2="15" y2="23" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="13" y1="0" x2="13" y2="2" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="3" y1="6" x2="5" y2="7" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="23" y1="6" x2="21" y2="7" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>
    </g>'''

def icon_scales_oracle(cx, cy, s=1.0, color="#047857"):
    """Balance Scales / Oracle Verdict"""
    return f'''
    <g transform="translate({cx-12*s},{cy-12*s}) scale({s})">
      <line x1="12" y1="3" x2="12" y2="20" stroke="{color}" stroke-width="1.8"/>
      <line x1="3" y1="6" x2="21" y2="6" stroke="{color}" stroke-width="1.8"/>
      <line x1="3" y1="6" x2="1" y2="12" stroke="{color}" stroke-width="1"/>
      <line x1="3" y1="6" x2="5" y2="12" stroke="{color}" stroke-width="1"/>
      <path d="M0 12 Q3 16 6 12 Z" fill="{color}"/>
      <line x1="21" y1="6" x2="19" y2="12" stroke="{color}" stroke-width="1"/>
      <line x1="21" y1="6" x2="23" y2="12" stroke="{color}" stroke-width="1"/>
      <path d="M18 12 Q21 16 24 12 Z" fill="{color}"/>
      <rect x="7" y="20" width="10" height="2.5" rx="1" fill="{color}"/>
    </g>'''

# ----------------- DRAWING HELPERS -----------------

def svg_header():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif">
<defs>
  <!-- Drop Shadow Filters -->
  <filter id="shadow-sm" x="-4%" y="-4%" width="108%" height="110%" filterUnits="userSpaceOnUse">
    <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.06"/>
  </filter>
  <filter id="shadow-md" x="-6%" y="-6%" width="112%" height="114%" filterUnits="userSpaceOnUse">
    <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.08"/>
  </filter>

  <!-- Markers -->
  <marker id="arr-dark" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{INK_DARK}"/>
  </marker>
  <marker id="arr-mint" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{P1_DARK}"/>
  </marker>
  <marker id="arr-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{P2_DARK}"/>
  </marker>
  <marker id="arr-violet" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{P3_BORDER}"/>
  </marker>
  <marker id="arr-guide" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{LOOP_GUIDE}"/>
  </marker>
  <marker id="arr-rewrite" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{LOOP_REWRITE}"/>
  </marker>
  <marker id="arr-bug" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{BUG_BORDER}"/>
  </marker>
  <marker id="arr-lateral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
    <path d="M0 1.5 L8.5 5 L0 8.5 L2 5 Z" fill="{LATERAL_BORDER}"/>
  </marker>
</defs>
<rect width="{W}" height="{H}" fill="#FFFFFF"/>
'''

def badge_step(x, y, num_str, label, fill_bg, text_color):
    return f'''
    <g transform="translate({x},{y})">
      <circle cx="14" cy="14" r="13" fill="{fill_bg}"/>
      <text x="14" y="19" font-size="14" font-weight="800" fill="{text_color}" text-anchor="middle">{num_str}</text>
      <text x="36" y="19" font-size="15" font-weight="800" fill="{INK_DARK}">{label}</text>
    </g>'''

def build_figure():
    out = [svg_header()]

    # =========================================================================
    # TOP SECTION: OFFLINE PREPARATION (INVARIANT & COMPILER INSTRUMENTATION)
    # =========================================================================
    
    off_x, off_y, off_w, off_h = 30, 28, 1620, 355
    out.append(f'''
    <!-- OFFLINE STAGE CONTAINER -->
    <rect x="{off_x}" y="{off_y}" width="{off_w}" height="{off_h}" rx="14" fill="#F8FAFC" stroke="{BORDER_BASE}" stroke-width="1.2"/>
    <rect x="{off_x}" y="{off_y}" width="340" height="30" rx="6" fill="{INK_DARK}"/>
    <text x="{off_x+170}" y="{off_y+20}" font-size="12" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">OFFLINE: INVARIANT &amp; INSTRUMENTATION</text>
    ''')

    # -------------------------------------------------------------------------
    # BOX 1: Invariant Generation (CoT + RAG)
    # -------------------------------------------------------------------------
    b1_x, b1_y, b1_w, b1_h = 48, 68, 362, 300
    out.append(f'''
    <!-- STEP 1: Invariant Generation -->
    <g filter="url(#shadow-sm)">
      <rect x="{b1_x}" y="{b1_y}" width="{b1_w}" height="{b1_h}" rx="12" fill="{P1_CARD}" stroke="{P1_BORDER}" stroke-width="1.5"/>
      <path d="M{b1_x} {b1_y+38} L{b1_x+b1_w} {b1_y+38}" stroke="{P1_CHIP}" stroke-width="1.5"/>
      {badge_step(b1_x+14, b1_y+6, "1", "Invariant Generation", P1_DARK, "#FFFFFF")}
    </g>
    <text x="{b1_x+16}" y="{b1_y+56}" font-size="11.5" font-weight="600" fill="{P1_DARK}">Segmented CoT + Historical-Bug RAG</text>
    
    <!-- Input Corpus Card -->
    <g transform="translate({b1_x+14},{b1_y+68})">
      <rect x="0" y="0" width="334" height="66" rx="8" fill="#F8FAFC" stroke="{BORDER_BASE}" stroke-width="1"/>
      {icon_shield_security(20, 24, 0.9, P1_DARK)}
      <text x="40" y="20" font-size="11.5" font-weight="700" fill="{INK_DARK}">Defense Specs &amp; Compiler Semantics</text>
      <text x="40" y="36" font-size="10.5" fill="{INK_MUTED}">Stack-Canary, SafeStack, PAC, CET/IBT, CFI</text>
      <text x="40" y="52" font-size="10" fill="{INK_LIGHT}">Target ABIs, registers, prologue/epilogue rules</text>
    </g>

    <!-- RAG Engine Card -->
    <g transform="translate({b1_x+14},{b1_y+142})">
      <rect x="0" y="0" width="334" height="66" rx="8" fill="{P1_BG}" stroke="{P1_BORDER}" stroke-width="1"/>
      {icon_rag_db(20, 24, 0.9, P1_DARK)}
      <text x="40" y="19" font-size="11.5" font-weight="700" fill="{P1_HEADER}">Historical CVE &amp; Patch Corpus (RAG)</text>
      <text x="40" y="35" font-size="10.5" fill="{INK_MUTED}">Homologue root-cause &amp; silent-fix retrieval</text>
      <text x="40" y="52" font-size="10.5" font-weight="600" fill="{P1_DARK}">CoT candidate invariant synthesis</text>
    </g>

    <!-- Output: Invariant Catalog -->
    <g transform="translate({b1_x+14},{b1_y+218})">
      <rect x="0" y="0" width="334" height="68" rx="8" fill="{P1_DARK}" stroke="{P1_DARK}" stroke-width="1.2"/>
      <text x="167" y="22" font-size="12.5" font-weight="800" fill="#FFFFFF" text-anchor="middle">Security Invariant Catalog Φ</text>
      <rect x="12" y="34" width="94" height="24" rx="4" fill="#065F46"/>
      <text x="59" y="50" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#A7F3D0" text-anchor="middle">ϕ₁: Canary</text>
      <rect x="114" y="34" width="106" height="24" rx="4" fill="#065F46"/>
      <text x="167" y="50" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#A7F3D0" text-anchor="middle">ϕ₂: Layout</text>
      <rect x="228" y="34" width="94" height="24" rx="4" fill="#065F46"/>
      <text x="275" y="50" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#A7F3D0" text-anchor="middle">ϕ₃: Return</text>
    </g>
    ''')

    # Arrow 1 -> 2
    out.append(f'''
    <line x1="{b1_x+b1_w}" y1="{b1_y+150}" x2="{b1_x+b1_w+32}" y2="{b1_y+150}" stroke="{INK_DARK}" stroke-width="2" marker-end="url(#arr-dark)"/>
    ''')

    # -------------------------------------------------------------------------
    # BOX 2: Checker Construction (Static & Dynamic Oracles per ISA)
    # -------------------------------------------------------------------------
    b2_x, b2_y, b2_w, b2_h = 442, 68, 380, 300
    out.append(f'''
    <!-- STEP 2: Checker Construction -->
    <g filter="url(#shadow-sm)">
      <rect x="{b2_x}" y="{b2_y}" width="{b2_w}" height="{b2_h}" rx="12" fill="{P1_CARD}" stroke="{P1_BORDER}" stroke-width="1.5"/>
      <path d="M{b2_x} {b2_y+38} L{b2_x+b2_w} {b2_y+38}" stroke="{P1_CHIP}" stroke-width="1.5"/>
      {badge_step(b2_x+14, b2_y+6, "2", "Initial Checker Construction", P1_DARK, "#FFFFFF")}
    </g>
    <text x="{b2_x+16}" y="{b2_y+56}" font-size="11.5" font-weight="600" fill="{P1_DARK}">Deterministic Oracles (Static &amp; Dynamic per ISA)</text>

    <!-- Dual Checker Types -->
    <g transform="translate({b2_x+14},{b2_y+68})">
      <!-- Static Checker -->
      <rect x="0" y="0" width="170" height="84" rx="8" fill="{P1_BG}" stroke="{P1_BORDER}" stroke-width="1"/>
      {icon_shield_security(18, 16, 0.75, P1_DARK)}
      <text x="34" y="18" font-size="11.5" font-weight="800" fill="{P1_HEADER}">Static Checker</text>
      <text x="10" y="36" font-size="10" fill="{INK_MUTED}">• AST &amp; GIMPLE audit</text>
      <text x="10" y="52" font-size="10" fill="{INK_MUTED}">• LLVM-IR / Asm scan</text>
      <text x="10" y="68" font-size="9.5" font-weight="600" fill="{P1_DARK}">Pre-compile structure check</text>
      
      <!-- Dynamic Checker -->
      <rect x="182" y="0" width="170" height="84" rx="8" fill="{P1_BG}" stroke="{P1_BORDER}" stroke-width="1"/>
      {icon_scales_oracle(196, 16, 0.75, P1_DARK)}
      <text x="214" y="18" font-size="11.5" font-weight="800" fill="{P1_HEADER}">Dynamic Checker</text>
      <text x="192" y="36" font-size="10" fill="{INK_MUTED}">• Executable probe binary</text>
      <text x="192" y="52" font-size="10" fill="{INK_MUTED}">• Stack/register overflow</text>
      <text x="192" y="68" font-size="9.5" font-weight="600" fill="{P1_DARK}">Runtime exploit &amp; verdict</text>
    </g>

    <!-- Multi-ISA Specialization Grid -->
    <g transform="translate({b2_x+14},{b2_y+160})">
      <rect x="0" y="0" width="352" height="56" rx="8" fill="#F8FAFC" stroke="{BORDER_BASE}" stroke-width="1"/>
      <text x="10" y="18" font-size="11" font-weight="700" fill="{INK_MUTED}">Multi-ISA Architecture Specialization:</text>
      <g transform="translate(24, 28)">{logo_isa_x86(18, 10, 0.9)}</g>
      <g transform="translate(130, 28)">{logo_isa_arm(20, 10, 0.9)}</g>
      <g transform="translate(242, 28)">{logo_isa_riscv(20, 10, 0.9)}</g>
    </g>

    <!-- 4-State Verdict Definition -->
    <g transform="translate({b2_x+14},{b2_y+224})">
      <rect x="0" y="0" width="352" height="62" rx="8" fill="#FFFFFF" stroke="{BORDER_BASE}" stroke-width="1.2"/>
      <text x="176" y="16" font-size="11" font-weight="700" fill="{INK_DARK}" text-anchor="middle">Four-State Verdict + Deterministic Evidence</text>
      <rect x="8" y="26" width="76" height="26" rx="5" fill="#DCFCE7" stroke="#16A34A" stroke-width="1"/>
      <text x="46" y="43" font-size="10.5" font-weight="800" fill="#15803D" text-anchor="middle">PASS</text>
      <rect x="92" y="26" width="82" height="26" rx="5" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.2"/>
      <text x="133" y="43" font-size="10" font-weight="800" fill="#B91C1C" text-anchor="middle">FAIL (Bug)</text>
      <rect x="182" y="26" width="76" height="26" rx="5" fill="#F1F5F9" stroke="#64748B" stroke-width="1"/>
      <text x="220" y="43" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">N/A</text>
      <rect x="266" y="26" width="78" height="26" rx="5" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
      <text x="305" y="43" font-size="10.5" font-weight="700" fill="#B45309" text-anchor="middle">ERROR</text>
    </g>
    ''')

    # Arrow 2 -> 3
    out.append(f'''
    <line x1="{b2_x+b2_w}" y1="{b2_y+150}" x2="{b2_x+b2_w+34}" y2="{b2_y+150}" stroke="{INK_DARK}" stroke-width="2" marker-end="url(#arr-dark)"/>
    ''')

    # -------------------------------------------------------------------------
    # BOX 3: Source Mapping (Free Agent + MCP Tools)
    # -------------------------------------------------------------------------
    b3_x, b3_y, b3_w, b3_h = 856, 68, 368, 300
    out.append(f'''
    <!-- STEP 3: Source Mapping -->
    <g filter="url(#shadow-sm)">
      <rect x="{b3_x}" y="{b3_y}" width="{b3_w}" height="{b3_h}" rx="12" fill="{P2_CARD}" stroke="{P2_BORDER}" stroke-width="1.5"/>
      <path d="M{b3_x} {b3_y+38} L{b3_x+b3_w} {b3_y+38}" stroke="{P2_CHIP}" stroke-width="1.5"/>
      {badge_step(b3_x+14, b3_y+6, "3", "Source Code Mapping", P2_DARK, "#FFFFFF")}
    </g>
    <text x="{b3_x+16}" y="{b3_y+56}" font-size="11.5" font-weight="600" fill="{P2_DARK}">3-Level Invariant Mapping via Free Agent + MCP</text>

    <!-- Free Agent & MCP Tools Banner -->
    <g transform="translate({b3_x+14},{b3_y+68})">
      <rect x="0" y="0" width="340" height="52" rx="8" fill="{P2_BG}" stroke="{P2_BORDER}" stroke-width="1"/>
      {logo_claude(20, 26, 0.9)}
      <text x="42" y="19" font-size="11.5" font-weight="800" fill="{P2_HEADER}">Free Coding Agent (e.g., Claude Code)</text>
      <g transform="translate(42, 26)">
        {logo_mcp(10, 10, 0.65)}
        <text x="24" y="14" font-size="10.5" font-weight="700" fill="{P2_DARK}">MCP Tools:</text>
        <rect x="86" y="2" width="82" height="18" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="0.8"/>
        <text x="127" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#92400E" text-anchor="middle">call-graph</text>
        <rect x="176" y="2" width="108" height="18" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="0.8"/>
        <text x="230" y="14" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#92400E" text-anchor="middle">read/grep/ast</text>
      </g>
    </g>

    <!-- Hierarchical 3-Level Mapping Tree -->
    <g transform="translate({b3_x+14},{b3_y+128})">
      <rect x="0" y="0" width="340" height="158" rx="8" fill="#F8FAFC" stroke="{BORDER_BASE}" stroke-width="1"/>
      {icon_callgraph(24, 78, 1.2, P2_DARK)}
      
      <!-- Level 1: Pass -->
      <rect x="55" y="10" width="270" height="38" rx="6" fill="#FFFFFF" stroke="{P2_BORDER}" stroke-width="1.2"/>
      <text x="65" y="26" font-size="11" font-weight="800" fill="{P2_HEADER}">Level 1: Compiler Pass</text>
      <text x="65" y="40" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="{INK_MUTED}">pass_stack_protect / StackProtectorPass</text>

      <!-- Down Arrow -->
      <line x1="190" y1="48" x2="190" y2="58" stroke="{P2_BORDER}" stroke-width="1.5" marker-end="url(#arr-amber)"/>

      <!-- Level 2: Function -->
      <rect x="55" y="60" width="270" height="38" rx="6" fill="#FFFFFF" stroke="{P2_BORDER}" stroke-width="1.2"/>
      <text x="65" y="76" font-size="11" font-weight="800" fill="{P2_HEADER}">Level 2: Target Functions</text>
      <text x="65" y="90" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="{INK_MUTED}">expand_used_vars() / LayoutStackNodes()</text>

      <!-- Down Arrow -->
      <line x1="190" y1="98" x2="190" y2="108" stroke="{P2_BORDER}" stroke-width="1.5" marker-end="url(#arr-amber)"/>

      <!-- Level 3: Struct & Critical Conditions -->
      <rect x="55" y="110" width="270" height="40" rx="6" fill="#FEF3C7" stroke="{P2_BORDER}" stroke-width="1.2"/>
      <text x="65" y="126" font-size="11" font-weight="800" fill="{P2_HEADER}">Level 3: Structs &amp; Critical Conditions</text>
      <text x="65" y="141" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#B45309">has_vla, stack_protect_decl, canary_loc</text>
    </g>
    ''')

    # Arrow 3 -> 4
    out.append(f'''
    <line x1="{b3_x+b3_w}" y1="{b3_y+150}" x2="{b3_x+b3_w+34}" y2="{b3_y+150}" stroke="{INK_DARK}" stroke-width="2" marker-end="url(#arr-dark)"/>
    ''')

    # -------------------------------------------------------------------------
    # BOX 4: Log Instrumentation & Compiler Rebuild
    # -------------------------------------------------------------------------
    b4_x, b4_y, b4_w, b4_h = 1258, 68, 368, 300
    out.append(f'''
    <!-- STEP 4: Log Instrumentation -->
    <g filter="url(#shadow-sm)">
      <rect x="{b4_x}" y="{b4_y}" width="{b4_w}" height="{b4_h}" rx="12" fill="{P2_CARD}" stroke="{P2_BORDER}" stroke-width="1.5"/>
      <path d="M{b4_x} {b4_y+38} L{b4_x+b4_w} {b4_y+38}" stroke="{P2_CHIP}" stroke-width="1.5"/>
      {badge_step(b4_x+14, b4_y+6, "4", "Log Instrumentation &amp; Build", P2_DARK, "#FFFFFF")}
    </g>
    <text x="{b4_x+16}" y="{b4_y+56}" font-size="11.5" font-weight="600" fill="{P2_DARK}">Unique-ID Prefix Probing &amp; Recompilation</text>

    <!-- Code Editor Box (Properly Indented) -->
    <g transform="translate({b4_x+14},{b4_y+68})">
      <rect x="0" y="0" width="340" height="128" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1"/>
      <circle cx="12" cy="12" r="3.5" fill="#EF4444"/>
      <circle cx="22" cy="12" r="3.5" fill="#F59E0B"/>
      <circle cx="32" cy="12" r="3.5" fill="#10B981"/>
      <text x="170" y="14" font-family="'JetBrains Mono', monospace" font-size="9" fill="#94A3B8" text-anchor="middle">gcc/cfgexpand.cc (Instrumented)</text>

      <text x="12" y="34" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#E2E8F0">void expand_stack_protection() {{</text>
      <rect x="6" y="40" width="328" height="17" fill="#1E293B" rx="3"/>
      <text x="24" y="52" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#FCD34D">  DEFUZZ_LOG("SP#a3f2", has_vla, off);</text>
      <text x="24" y="69" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#93C5FD">  if (has_vla || has_vla_ptr) {{</text>
      <rect x="6" y="75" width="328" height="17" fill="#1E293B" rx="3"/>
      <text x="36" y="87" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#FCD34D">    DEFUZZ_LOG("SP#a3f2:hit", slot);</text>
      <text x="36" y="103" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#E2E8F0">    emit_canary_prologue();</text>
      <text x="24" y="119" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#93C5FD">  }}</text>
      <text x="12" y="125" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#E2E8F0">}}</text>
    </g>

    <!-- Compiler Recompilation Output -->
    <g transform="translate({b4_x+14},{b4_y+204})">
      <rect x="0" y="0" width="340" height="82" rx="8" fill="{P2_BG}" stroke="{P2_BORDER}" stroke-width="1.2"/>
      <g transform="translate(18, 22)">{logo_gcc(14, 14, 1.15)}</g>
      <g transform="translate(60, 22)">{logo_llvm(14, 14, 1.15)}</g>
      <text x="105" y="26" font-size="12" font-weight="800" fill="{P2_HEADER}">Instrumented Compiler IC</text>
      <text x="105" y="42" font-size="10" fill="{INK_MUTED}">Rebuilt with deterministic log hooks</text>
      <rect x="105" y="50" width="222" height="22" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="0.8"/>
      <text x="216" y="65" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#92400E" text-anchor="middle">Unique UID Tagging · Trace Emitted</text>
    </g>
    ''')

    # =========================================================================
    # INTER-PHASE CONNECTING BRIDGES (CAREFULLY POSITIONED WITHOUT OVERLAPS)
    # =========================================================================

    # Bridge 1: Step 2 (Box 2) -> Orchestrator (Straight down at x = 500)
    out.append(f'''
    <!-- Bridge: Checker Suite -> Orchestrator (Clean vertical drop at x = 500) -->
    <path d="M 500 {b2_y+b2_h} L 500 398" fill="none" stroke="{P1_DARK}" stroke-width="2.2"/>
    <path d="M 500 422 L 500 485" fill="none" stroke="{P1_DARK}" stroke-width="2.2" marker-end="url(#arr-mint)"/>
    <rect x="390" y="399" width="220" height="22" rx="4" fill="#FFFFFF" stroke="{P1_DARK}" stroke-width="1.2"/>
    <text x="500" y="414" font-size="10.5" font-weight="800" fill="{P1_DARK}" text-anchor="middle">Bind Invariant ϕᵢ + Checker Oracle</text>
    ''')

    # Bridge 2: Step 4 (Box 4) -> Build & Dual Verification (Enters at x = 740, right of Bridge 1!)
    out.append(f'''
    <!-- Bridge: IC Recompiled -> Online Build (Routed horizontally along y = 430, drops at x = 740) -->
    <path d="M {b4_x+b4_w/2} {b4_y+b4_h} L {b4_x+b4_w/2} 430 L 1152 430" fill="none" stroke="{P2_BORDER}" stroke-width="2.2"/>
    <path d="M 928 430 L 740 430 L 740 545" fill="none" stroke="{P2_BORDER}" stroke-width="2.2" marker-end="url(#arr-amber)"/>
    <rect x="930" y="419" width="220" height="22" rx="4" fill="#FFFFFF" stroke="{P2_BORDER}" stroke-width="1.2"/>
    <text x="1040" y="434" font-size="10.5" font-weight="800" fill="{P2_DARK}" text-anchor="middle">Deploy Instrumented Compiler IC</text>
    ''')

    # =========================================================================
    # BOTTOM SECTION: ONLINE AGENTIC CLOSED-LOOP FUZZING
    # =========================================================================
    
    on_x, on_y, on_w, on_h = 30, 455, 1620, 520
    out.append(f'''
    <!-- ONLINE AGENTIC LOOP CONTAINER -->
    <g filter="url(#shadow-md)">
      <rect x="{on_x}" y="{on_y}" width="{on_w}" height="{on_h}" rx="16" fill="{P3_CONTAINER}" stroke="{P3_BORDER}" stroke-width="2" stroke-dasharray="8 6"/>
      <!-- Header Banner -->
      <rect x="{on_x}" y="{on_y}" width="380" height="32" rx="8" fill="{P3_HEADER}"/>
      <text x="{on_x+190}" y="{on_y+21}" font-size="12.5" font-weight="800" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">ONLINE · AGENTIC CLOSED-LOOP FUZZING</text>
    </g>
    ''')

    # Orchestrator Target Selection Bar (Left half: x = 48..680, leaving x=740 open for IC bridge!)
    orch_x, orch_y, orch_w, orch_h = 48, 485, 620, 42
    out.append(f'''
    <!-- Target Orchestrator Bar (Left Section) -->
    <g transform="translate({orch_x},{orch_y})">
      <rect x="0" y="0" width="{orch_w}" height="{orch_h}" rx="8" fill="#FFFFFF" stroke="{P3_BORDER}" stroke-width="1.2"/>
      <rect x="6" y="6" width="140" height="30" rx="6" fill="{P3_BORDER}"/>
      <text x="76" y="25" font-size="12" font-weight="800" fill="#FFFFFF" text-anchor="middle">ORCHESTRATOR</text>
      <text x="160" y="26" font-size="11.5" font-weight="700" fill="{INK_DARK}">Lock Target Invariant ϕᵢ + Checker</text>
      <rect x="420" y="8" width="190" height="26" rx="5" fill="{P3_CHIP}" stroke="{P3_BORDER}" stroke-width="0.8"/>
      <text x="515" y="25" font-size="11" font-weight="700" fill="{P3_DARK}" text-anchor="middle">Time Budget T per ϕᵢ</text>
    </g>

    <!-- Campaign Queue Status (Right Section) -->
    <g transform="translate(1320, 485)">
      <rect x="0" y="0" width="310" height="42" rx="8" fill="#FFFFFF" stroke="{BORDER_BASE}" stroke-width="1.2"/>
      <text x="14" y="26" font-size="11" font-weight="600" fill="{INK_MUTED}">Campaign Queue: Systematic Invariant Testing</text>
    </g>

    <!-- Arrow: Orchestrator -> Generator Agent -->
    <line x1="228" y1="{orch_y+orch_h}" x2="228" y2="545" stroke="{P3_BORDER}" stroke-width="2" marker-end="url(#arr-violet)"/>
    ''')

    # -------------------------------------------------------------------------
    # ONLINE NODE 1: Generator Agent (Checker-Aware Seed Generation)
    # -------------------------------------------------------------------------
    g_x, g_y, g_w, g_h = 48, 545, 360, 360
    out.append(f'''
    <!-- GENERATOR AGENT -->
    <g filter="url(#shadow-sm)">
      <rect x="{g_x}" y="{g_y}" width="{g_w}" height="{g_h}" rx="12" fill="{P3_CARD}" stroke="{P3_BORDER}" stroke-width="1.8"/>
      <path d="M{g_x} {g_y+38} L{g_x+g_w} {g_y+38}" stroke="{P3_CHIP}" stroke-width="1.5"/>
      {badge_step(g_x+14, g_y+6, "5", "Generator Agent", P3_BORDER, "#FFFFFF")}
    </g>
    <text x="{g_x+16}" y="{g_y+56}" font-size="11.5" font-weight="600" fill="{P3_DARK}">Checker-Aware C/C++ Seed Synthesis</text>

    <!-- Agent Identity & Capabilities -->
    <g transform="translate({g_x+14},{g_y+68})">
      <rect x="0" y="0" width="332" height="64" rx="8" fill="{P3_CONTAINER}" stroke="{P3_BORDER}" stroke-width="1"/>
      {icon_robot_agent(20, 20, 0.9, P3_BORDER)}
      {logo_cpp(308, 18, 0.85)}
      <text x="38" y="20" font-size="11.5" font-weight="800" fill="{P3_HEADER}">LLM Seed Generation Agent</text>
      <text x="10" y="38" font-size="10" fill="{INK_MUTED}">• Perceives defense invariant ϕ &amp; checker logic</text>
      <text x="10" y="52" font-size="10" fill="{INK_MUTED}">• Synthesizes complex C/C++ syntactic bounds</text>
    </g>

    <!-- Synthesized Seed Code Preview (Properly Indented) -->
    <g transform="translate({g_x+14},{g_y+138})">
      <rect x="0" y="0" width="332" height="116" rx="8" fill="#0F172A" stroke="#334155" stroke-width="1"/>
      <circle cx="12" cy="12" r="3" fill="#94A3B8"/>
      <circle cx="20" cy="12" r="3" fill="#94A3B8"/>
      <circle cx="28" cy="12" r="3" fill="#94A3B8"/>
      <text x="166" y="14" font-family="'JetBrains Mono', monospace" font-size="9" fill="#94A3B8" text-anchor="middle">seed_sp_probe.c</text>

      <text x="10" y="32" font-family="'JetBrains Mono', monospace" font-size="9" fill="#94A3B8">// Target: provoke canary omission on VLA</text>
      <text x="10" y="48" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#E2E8F0">void test_vla_probe(int n, char *buf) {{</text>
      <text x="24" y="64" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#FCD34D">  char vla[n]; volatile int tag = 1;</text>
      <text x="24" y="80" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#93C5FD">  memcpy(vla, buf, n); // trigger</text>
      <text x="24" y="96" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#E2E8F0">  sink(vla, &amp;tag);</text>
      <text x="10" y="110" font-family="'JetBrains Mono', monospace" font-size="9.5" fill="#E2E8F0">}}</text>
    </g>

    <!-- Generator Strategies -->
    <g transform="translate({g_x+14},{g_y+260})">
      <rect x="0" y="0" width="332" height="88" rx="8" fill="#FFFFFF" stroke="{BORDER_BASE}" stroke-width="1"/>
      <text x="10" y="16" font-size="11" font-weight="700" fill="{INK_DARK}">Generation Objectives:</text>
      <text x="10" y="32" font-size="10" fill="{INK_MUTED}">1. Satisfy frontend syntax &amp; valid type bounds</text>
      <text x="10" y="48" font-size="10" fill="{INK_MUTED}">2. Bypass middle-end dead-code elimination (DCE)</text>
      <text x="10" y="64" font-size="10" font-weight="600" fill="{P3_DARK}">3. Exercise critical struct &amp; branch conditions</text>
      <text x="10" y="80" font-size="10" font-weight="700" fill="{LATERAL_TEXT}">4. On FAIL ➔ Lateral reasoning for more bugs</text>
    </g>
    ''')

    # Arrow: Generator -> Compiler
    out.append(f'''
    <line x1="{g_x+g_w}" y1="{g_y+130}" x2="{g_x+g_w+40}" y2="{g_y+130}" stroke="{INK_DARK}" stroke-width="2.5" marker-end="url(#arr-dark)"/>
    <rect x="{g_x+g_w+4}" y="{g_y+108}" width="34" height="18" rx="3" fill="#FFFFFF" stroke="{BORDER_BASE}" stroke-width="0.8"/>
    <text x="{g_x+g_w+21}" y="{g_y+121}" font-size="9.5" font-weight="800" fill="{INK_DARK}" text-anchor="middle">Seed</text>
    ''')

    # -------------------------------------------------------------------------
    # ONLINE NODE 2: Instrumented Compiler Execution & Verification
    # -------------------------------------------------------------------------
    cmp_x, cmp_y, cmp_w, cmp_h = 448, 545, 344, 360
    out.append(f'''
    <!-- INSTRUMENTED COMPILER & DUAL CHECKING -->
    <g filter="url(#shadow-sm)">
      <rect x="{cmp_x}" y="{cmp_y}" width="{cmp_w}" height="{cmp_h}" rx="12" fill="{P3_CARD}" stroke="{P2_BORDER}" stroke-width="1.8"/>
      <path d="M{cmp_x} {cmp_y+38} L{cmp_x+cmp_w} {cmp_y+38}" stroke="{P2_CHIP}" stroke-width="1.5"/>
      <text x="{cmp_x+16}" y="{cmp_y+26}" font-size="15" font-weight="800" fill="{P2_DARK}">Build &amp; Dual Verification</text>
    </g>
    <text x="{cmp_x+16}" y="{cmp_y+56}" font-size="11.5" font-weight="600" fill="{P2_DARK}">Instrumented IC + Checker Oracle Evaluation</text>

    <!-- Compilation Phase -->
    <g transform="translate({cmp_x+14},{cmp_y+68})">
      <rect x="0" y="0" width="316" height="72" rx="8" fill="{P2_BG}" stroke="{P2_BORDER}" stroke-width="1"/>
      <g transform="translate(18, 20)">{logo_gcc(12, 12, 1.0)}</g>
      <g transform="translate(50, 20)">{logo_llvm(12, 12, 1.0)}</g>
      <text x="78" y="19" font-size="11.5" font-weight="800" fill="{P2_HEADER}">Compile with IC (GCC / LLVM)</text>
      <text x="78" y="34" font-size="9.5" fill="{INK_MUTED}">Emits assembly, IR &amp; unique UID log trace</text>
      <rect x="78" y="42" width="226" height="20" rx="4" fill="#FEF3C7" stroke="#D97706" stroke-width="0.8"/>
      <text x="191" y="56" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#92400E" text-anchor="middle">UID Log: DEFUZZ_LOG("SP#a3f2:hit")</text>
    </g>

    <!-- Dual Checker Oracle Evaluation (Header elevated to eliminate overlap) -->
    <g transform="translate({cmp_x+14},{cmp_y+148})">
      <rect x="0" y="0" width="316" height="118" rx="8" fill="{P1_BG}" stroke="{P1_BORDER}" stroke-width="1.2"/>
      <text x="158" y="17" font-size="11.5" font-weight="800" fill="{P1_HEADER}" text-anchor="middle">Checker Oracle Evaluation</text>
      
      <!-- Static Audit -->
      <rect x="8" y="24" width="144" height="84" rx="6" fill="#FFFFFF" stroke="{P1_BORDER}" stroke-width="1"/>
      {icon_shield_security(22, 38, 0.7, P1_DARK)}
      <text x="36" y="40" font-size="10.5" font-weight="800" fill="{P1_DARK}">Static Audit</text>
      <text x="12" y="56" font-size="9" fill="{INK_MUTED}">• Asm stack frame</text>
      <text x="12" y="70" font-size="9" fill="{INK_MUTED}">• Canary location</text>
      <text x="12" y="84" font-size="9" fill="{INK_MUTED}">• CFI jump tables</text>

      <!-- Dynamic Test -->
      <rect x="164" y="24" width="144" height="84" rx="6" fill="#FFFFFF" stroke="{P1_BORDER}" stroke-width="1"/>
      {icon_scales_oracle(178, 38, 0.7, P1_DARK)}
      <text x="192" y="40" font-size="10.5" font-weight="800" fill="{P1_DARK}">Dynamic Probe</text>
      <text x="168" y="56" font-size="9" fill="{INK_MUTED}">• Runtime execution</text>
      <text x="168" y="70" font-size="9" fill="{INK_MUTED}">• Exploit trigger</text>
      <text x="168" y="84" font-size="9" fill="{INK_MUTED}">• Crash / Canary check</text>
    </g>

    <!-- Emitted Verdict Output -->
    <g transform="translate({cmp_x+14},{cmp_y+274})">
      <rect x="0" y="0" width="316" height="74" rx="8" fill="#FFFFFF" stroke="{BORDER_BASE}" stroke-width="1.2"/>
      <text x="158" y="16" font-size="11" font-weight="800" fill="{INK_DARK}" text-anchor="middle">Structured Oracle Verdict + Telemetry</text>
      <rect x="8" y="22" width="94" height="42" rx="6" fill="#DCFCE7" stroke="#16A34A" stroke-width="1"/>
      <text x="55" y="38" font-size="10" font-weight="800" fill="#15803D" text-anchor="middle">PASS / N/A</text>
      <text x="55" y="52" font-size="8.5" fill="#15803D" text-anchor="middle">Invariant Holds</text>

      <rect x="110" y="22" width="96" height="42" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-width="1"/>
      <text x="158" y="38" font-size="10" font-weight="800" fill="#B45309" text-anchor="middle">ERROR / WARN</text>
      <text x="158" y="52" font-size="8.5" fill="#B45309" text-anchor="middle">Compile/Syntax Fail</text>

      <rect x="214" y="22" width="94" height="42" rx="6" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5"/>
      <text x="261" y="38" font-size="10" font-weight="800" fill="#B91C1C" text-anchor="middle">FAIL (Bug)</text>
      <text x="261" y="52" font-size="8.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Violation Found</text>
    </g>
    ''')

    # Arrow: Compiler -> Decision Diamond (Clear gap, no overlap)
    out.append(f'''
    <line x1="{cmp_x+cmp_w}" y1="730" x2="806" y2="730" stroke="{INK_DARK}" stroke-width="2" marker-end="url(#arr-dark)"/>
    ''')

    # -------------------------------------------------------------------------
    # VERDICT DECISION DIAMOND & BUG ROUTING (COMPLETELY DE-CONGESTED)
    # -------------------------------------------------------------------------
    dia_cx, dia_cy = 854, 730
    dia_w, dia_h = 46, 42
    out.append(f'''
    <!-- Verdict Decision Diamond -->
    <g filter="url(#shadow-sm)">
      <polygon points="{dia_cx},{dia_cy-dia_h} {dia_cx+dia_w},{dia_cy} {dia_cx},{dia_cy+dia_h} {dia_cx-dia_w},{dia_cy}" 
               fill="#FFFFFF" stroke="{INK_DARK}" stroke-width="2"/>
      <text x="{dia_cx}" y="{dia_cy-4}" font-size="11.5" font-weight="800" fill="{INK_DARK}" text-anchor="middle">Invariant</text>
      <text x="{dia_cx}" y="{dia_cy+11}" font-size="11.5" font-weight="800" fill="{INK_DARK}" text-anchor="middle">Violated?</text>
    </g>
    ''')

    # Branch 1: NO (PASS / NA / ERR) -> Go to Feedback Agent (Route along y = 615, broken segments)
    out.append(f'''
    <!-- Arrow: No Violation -> Feedback Agent (Broken across label pill) -->
    <path d="M {dia_cx} {dia_cy-dia_h} L {dia_cx} 615 L 908 615" 
          fill="none" stroke="{P3_BORDER}" stroke-width="2.4"/>
    <path d="M 1204 615 L 1228 615" 
          fill="none" stroke="{P3_BORDER}" stroke-width="2.4" marker-end="url(#arr-violet)"/>
    <rect x="910" y="604" width="292" height="22" rx="4" fill="#FFFFFF" stroke="{P3_BORDER}" stroke-width="1.2"/>
    <text x="1056" y="619" font-size="10" font-weight="700" fill="{P3_DARK}" text-anchor="middle">NO: PASS · N/A · ERROR (Send Telemetry to Feedback)</text>
    ''')

    # Branch 2: YES (FAIL) -> PoC & Lateral Thinking (Separated label, NO overlap with diamond)
    out.append(f'''
    <!-- Arrow: YES Violation -> PoC & Lateral (Clean separated routing) -->
    <path d="M {dia_cx} {dia_cy+dia_h} L {dia_cx} 808 L 868 808" 
          fill="none" stroke="{BUG_BORDER}" stroke-width="2.6"/>
    <path d="M 938 808 L 954 808" 
          fill="none" stroke="{BUG_BORDER}" stroke-width="2.6" marker-end="url(#arr-bug)"/>
    <rect x="870" y="797" width="66" height="22" rx="4" fill="#FEE2E2" stroke="{BUG_BORDER}" stroke-width="1.2"/>
    <text x="903" y="812" font-size="10.5" font-weight="800" fill="{BUG_TEXT}" text-anchor="middle">YES: FAIL</text>
    ''')

    # Bug Confirmation & PoC Card
    bug_x, bug_y, bug_w, bug_h = 956, 740, 236, 126
    out.append(f'''
    <!-- Bug Discovery & PoC Box -->
    <g filter="url(#shadow-md)" transform="translate({bug_x},{bug_y})">
      <rect x="0" y="0" width="{bug_w}" height="{bug_h}" rx="10" fill="{BUG_BG}" stroke="{BUG_BORDER}" stroke-width="2"/>
      {icon_bug_vuln(26, 26, 1.2, BUG_BORDER)}
      <text x="50" y="24" font-size="12.5" font-weight="900" fill="{BUG_TEXT}">CONFIRMED BUG</text>
      <text x="50" y="38" font-size="10" font-weight="700" fill="{BUG_TEXT}">Zero-Day Vulnerability</text>
      
      <rect x="10" y="48" width="216" height="42" rx="6" fill="#FFFFFF" stroke="{BUG_BORDER}" stroke-width="0.8"/>
      <text x="18" y="64" font-size="9.5" font-weight="600" fill="{INK_DARK}">• C-Reduce automated PoC</text>
      <text x="18" y="78" font-size="9.5" font-weight="600" fill="{INK_DARK}">• Human developer review</text>

      <rect x="10" y="96" width="216" height="22" rx="4" fill="#FEE2E2"/>
      <text x="118" y="111" font-size="9" font-weight="700" fill="{BUG_TEXT}" text-anchor="middle">Feed to Historical CVE Corpus ➔</text>
    </g>
    ''')

    # Lateral Thinking Box & Separate Loop-Back Track
    lat_x, lat_y, lat_w, lat_h = 956, 878, 236, 52
    out.append(f'''
    <!-- LATERAL THINKING CARD -->
    <g transform="translate({lat_x},{lat_y})">
      <rect x="0" y="0" width="{lat_w}" height="{lat_h}" rx="8" fill="{LATERAL_BG}" stroke="{LATERAL_BORDER}" stroke-width="1.5"/>
      {icon_lateral_idea(22, 26, 0.9, LATERAL_BORDER)}
      <text x="44" y="22" font-size="11" font-weight="800" fill="{LATERAL_TEXT}">Lateral Exploration</text>
      <text x="44" y="38" font-size="9.5" font-weight="600" fill="{LATERAL_TEXT}">Synthesize more violation poses</text>
    </g>
    
    <!-- Path: Lateral back to Generator (Track 1: y = 922, broken across label pill) -->
    <path d="M {lat_x} {lat_y+lat_h/2} L {lat_x-10} {lat_y+lat_h/2} L {lat_x-10} 922 L 802 922" 
          fill="none" stroke="{LATERAL_BORDER}" stroke-width="2.2" stroke-dasharray="6 4"/>
    <path d="M 318 922 L 240 922 L 240 {g_y+g_h}" 
          fill="none" stroke="{LATERAL_BORDER}" stroke-width="2.2" stroke-dasharray="6 4" marker-end="url(#arr-lateral)"/>
    <rect x="320" y="911" width="480" height="22" rx="4" fill="#FFFFFF" stroke="{LATERAL_BORDER}" stroke-width="1.2"/>
    <text x="560" y="926" font-size="9.5" font-weight="700" fill="{LATERAL_TEXT}" text-anchor="middle">Lateral Reasoning Loop: Synthesize diverse seed variants for ϕᵢ</text>
    ''')

    # -------------------------------------------------------------------------
    # ONLINE NODE 3: Feedback Agent (MCP Diagnostics + Routing Decisions)
    # -------------------------------------------------------------------------
    fb_x, fb_y, fb_w, fb_h = 1228, 545, 404, 360
    out.append(f'''
    <!-- FEEDBACK AGENT -->
    <g filter="url(#shadow-sm)">
      <rect x="{fb_x}" y="{fb_y}" width="{fb_w}" height="{fb_h}" rx="12" fill="{P3_CARD}" stroke="{P3_BORDER}" stroke-width="1.8"/>
      <path d="M{fb_x} {fb_y+38} L{fb_x+fb_w} {fb_y+38}" stroke="{P3_CHIP}" stroke-width="1.5"/>
      {badge_step(fb_x+14, fb_y+6, "6", "Feedback Agent", P3_BORDER, "#FFFFFF")}
    </g>
    <text x="{fb_x+16}" y="{fb_y+56}" font-size="11.5" font-weight="600" fill="{P3_DARK}">Diagnostics-Aware Routing &amp; Adaptation</text>

    <!-- Feedback Telemetry Collection via MCP -->
    <g transform="translate({fb_x+14},{fb_y+68})">
      <rect x="0" y="0" width="376" height="84" rx="8" fill="{P3_CONTAINER}" stroke="{P3_BORDER}" stroke-width="1"/>
      {icon_brain_feedback(20, 18, 0.85, P3_BORDER)}
      {logo_mcp(354, 18, 0.7)}
      <text x="38" y="20" font-size="11.5" font-weight="800" fill="{P3_HEADER}">Compiler &amp; Checker Signals (MCP)</text>
      <text x="10" y="38" font-size="10" fill="{INK_MUTED}">• Compiler warnings &amp; AST diagnostic notes</text>
      <text x="10" y="52" font-size="10" fill="{INK_MUTED}">• Checker static assertions &amp; execution trace</text>
      <text x="10" y="68" font-size="10" font-weight="600" fill="{P3_DARK}">• Critical condition hit counter: <tspan font-family="'JetBrains Mono', monospace" fill="{P2_DARK}">hit_count(UID)</tspan></text>
    </g>

    <!-- Feedback Dual Decision Matrix -->
    <g transform="translate({fb_x+14},{fb_y+160})">
      <rect x="0" y="0" width="376" height="190" rx="8" fill="#FFFFFF" stroke="{BORDER_BASE}" stroke-width="1.2"/>
      <text x="188" y="18" font-size="11.5" font-weight="800" fill="{INK_DARK}" text-anchor="middle">Feedback Decision &amp; Action</text>

      <!-- Action A: Seed Space Guidance -->
      <g transform="translate(10, 28)">
        <rect x="0" y="0" width="356" height="70" rx="6" fill="{LOOP_GUIDE_BG}" stroke="{LOOP_GUIDE}" stroke-width="1.2"/>
        <text x="12" y="20" font-size="11.5" font-weight="800" fill="{LOOP_GUIDE}">Decision 1: Guide Next Seed Round</text>
        <text x="12" y="36" font-size="9.5" fill="{INK_MUTED}">• Condition not hit ➔ Adjust seed data types &amp; sizes</text>
        <text x="12" y="50" font-size="9.5" fill="{INK_MUTED}">• Silent optimization (DCE) ➔ Add volatile sinks</text>
        <text x="12" y="64" font-size="9.5" font-weight="700" fill="{P3_DARK}">Steers Generator towards unexercised branches</text>
      </g>

      <!-- Action B: Checker Rewrite -->
      <g transform="translate(10, 106)">
        <rect x="0" y="0" width="356" height="74" rx="6" fill="{LOOP_REWRITE_BG}" stroke="{LOOP_REWRITE}" stroke-width="1.5"/>
        <text x="12" y="20" font-size="11.5" font-weight="900" fill="{LOOP_REWRITE}">Decision 2: Checker Rewrite (Threshold τ)</text>
        <text x="12" y="36" font-size="9.5" fill="{INK_MUTED}">• Checker over-constrained or false-positive prone</text>
        <text x="12" y="50" font-size="9.5" font-weight="700" fill="{LOOP_REWRITE}">• Accumulated rewrite votes ≥ τ (e.g., 3 rounds)</text>
        <text x="12" y="66" font-size="9.5" font-weight="800" fill="{LOOP_REWRITE}">➔ Triggers Phase 1 Checker Refinement &amp; Rerun</text>
      </g>
    </g>
    ''')

    # =========================================================================
    # FEEDBACK LOOPS (PURPLE GUIDANCE & RED CHECKER REWRITE)
    # =========================================================================

    # Loop 1: Seed Guidance (Feedback Agent -> Generator Agent)
    # Routed on Track 2 (y = 960) at the very bottom (broken across label pill)
    out.append(f'''
    <!-- LOOP 1: SEED GUIDANCE (PURPLE DASHED, Track 2: y = 960, broken across label pill) -->
    <path d="M {fb_x+100} {fb_y+fb_h-18} L {fb_x+100} 960 L 902 960" 
          fill="none" stroke="{LOOP_GUIDE}" stroke-width="2.4" stroke-dasharray="7 5"/>
    <path d="M 518 960 L {g_x+100} 960 L {g_x+100} {g_y+g_h}" 
          fill="none" stroke="{LOOP_GUIDE}" stroke-width="2.4" stroke-dasharray="7 5" marker-end="url(#arr-guide)"/>
    <rect x="520" y="949" width="380" height="22" rx="4" fill="#FFFFFF" stroke="{LOOP_GUIDE}" stroke-width="1.2"/>
    <text x="710" y="964" font-size="10.5" font-weight="800" fill="{LOOP_GUIDE}" text-anchor="middle">Guidance Loop: Diagnostics-Guided Seed Mutation Hints</text>
    ''')

    # Loop 2: Checker Rewrite (Feedback Agent -> Box 2 Checker Construction)
    # Routed cleanly through the RIGHT corridor (x = 1658), up to y = 14, across to Box 2 (x = 632)
    out.append(f'''
    <!-- LOOP 2: CHECKER REWRITE (RED DASHED, broken across label pill) -->
    <path d="M {fb_x+fb_w-40} {fb_y+fb_h-100} L 1658 {fb_y+fb_h-100} L 1658 14 L 1402 14" 
          fill="none" stroke="{LOOP_REWRITE}" stroke-width="2.6" stroke-dasharray="8 5"/>
    <path d="M 938 14 L 632 14 L 632 {b2_y}" 
          fill="none" stroke="{LOOP_REWRITE}" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arr-rewrite)"/>
    <rect x="940" y="3" width="460" height="22" rx="5" fill="#FFFFFF" stroke="{LOOP_REWRITE}" stroke-width="1.5"/>
    <text x="1170" y="18" font-size="11" font-weight="900" fill="{LOOP_REWRITE}" text-anchor="middle">Checker Rewrite Triggered (Votes ≥ τ) ➔ Re-synthesize Oracle &amp; Rerun</text>
    ''')

    out.append("</svg>")
    return "\n".join(out)

if __name__ == "__main__":
    svg_content = build_figure()
    
    out_svg = Path(__file__).resolve().parent.parent / "method-overview.svg"
    out_pdf = Path(__file__).resolve().parent.parent / "method-overview.pdf"
    preview_png = Path("/workspace/ws_BpTiHMXU/method-overview-preview.png")

    out_svg.write_text(svg_content)
    print(f"Generated SVG: {out_svg} ({len(svg_content)} bytes)")

    # Render to PDF and PNG via cairosvg
    import cairosvg
    cairosvg.svg2pdf(url=str(out_svg), write_to=str(out_pdf))
    print(f"Generated PDF: {out_pdf}")

    cairosvg.svg2png(url=str(out_svg), write_to=str(preview_png), output_width=1680)
    print(f"Generated Preview PNG: {preview_png}")
