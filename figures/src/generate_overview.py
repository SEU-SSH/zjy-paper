#!/usr/bin/env python3
"""
Generate a high-prestige IEEE S&P / CCS style system overview diagram for DeFuzz
(Worktree branch: style/overview-v2):
- Refined Steel-Navy, Cool Slate, and Emerald academic palette (zero yellow fill).
- Crisp border layering over left-hand schematic wells.
- Domain-specific compiler-security mini-schematics inside every module card
  (spec-to-phi contract, call-graph DAG, 3-tier branch funnel + CFG diamond,
  stack frame layout, sandbox runtime trap, seed code block, 8-tooth compiler gear
  + check, and branch-flip guided mutation).
- Crisp sans-serif typography ('Helvetica Neue', Helvetica, Arial) with Plain Drawing
  conciseness (only 2 '&' across the entire diagram).
- Minimalist bot badge on LLM-assisted stages/agents; distinct rounded emerald capsule
  for 'Zero LLM in Adjudication'.
"""

import math
import os
import subprocess


def gear_svg(cx: float, cy: float, r_outer: float, r_inner: float, r_hole: float, hole_fill: str) -> str:
    """Return crisp 8-tooth gear SVG elements centered at (cx, cy)."""
    lines = []
    for i in range(8):
        angle = i * (math.pi / 4.0)
        x1 = cx + (r_inner - 0.3) * math.cos(angle)
        y1 = cy + (r_inner - 0.3) * math.sin(angle)
        x2 = cx + r_outer * math.cos(angle)
        y2 = cy + r_outer * math.sin(angle)
        lines.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="#1E293B" stroke-width="1.6" stroke-linecap="round"/>'
        )
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r_inner}" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.2"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r_hole}" fill="{hole_fill}" stroke="#1E293B" stroke-width="1.05"/>')
    return "\n    ".join(lines)


def generate_svg():
    W, H = 1100, 288
    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="background-color: #FFFFFF; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Crisp arrowheads -->
    <marker id="arr" viewBox="0 0 10 10" refX="8.2" refY="5" markerWidth="5.8" markerHeight="5.8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9.2 5 L 0 8.5 z" fill="#1E293B"/>
    </marker>
    <marker id="arr-indigo" viewBox="0 0 10 10" refX="8.2" refY="5" markerWidth="5.8" markerHeight="5.8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9.2 5 L 0 8.5 z" fill="#2563EB"/>
    </marker>
    <marker id="arr-crimson" viewBox="0 0 10 10" refX="8.2" refY="5" markerWidth="5.8" markerHeight="5.8" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9.2 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>

    <!-- Subtle academic card elevation -->
    <filter id="card-shadow" x="-4%" y="-6%" width="108%" height="116%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.2" stdDeviation="1.5" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>

    <!-- Minimalist vector bot icon (15x15) in deep steel-indigo -->
    <g id="bot-logo">
      <line x1="7.5" y1="1.2" x2="7.5" y2="3.4" stroke="#1E3A8A" stroke-width="1.2" stroke-linecap="round"/>
      <circle cx="7.5" cy="1.0" r="1.0" fill="#1E3A8A"/>
      <line x1="0.8" y1="7.8" x2="2.3" y2="7.8" stroke="#1E3A8A" stroke-width="1.2" stroke-linecap="round"/>
      <line x1="12.7" y1="7.8" x2="14.2" y2="7.8" stroke="#1E3A8A" stroke-width="1.2" stroke-linecap="round"/>
      <rect x="2.3" y="3.4" width="10.4" height="8.8" rx="2.1" fill="#EEF2FF" stroke="#1E3A8A" stroke-width="1.2"/>
      <circle cx="5.5" cy="7.2" r="1.0" fill="#1E3A8A"/>
      <circle cx="9.5" cy="7.2" r="1.0" fill="#1E3A8A"/>
      <line x1="5.4" y1="9.8" x2="9.6" y2="9.8" stroke="#1E3A8A" stroke-width="1.05" stroke-linecap="round"/>
    </g>
  </defs>
''')

    # Sober, high-prestige Steel-Navy + Cool Slate + Emerald academic palette
    stage_tint = "#F8FAFC"        # Subtle alabaster slate for dashed group backgrounds
    dashed_stroke = "#64748B"     # Refined cool slate dashed border

    llm_card_fill = "#FFFFFF"     # Crisp white card body
    llm_card_stroke = "#3B5998"   # Refined steel-navy border
    llm_well_fill = "#EEF2FF"     # Soft ice-indigo schematic well
    llm_well_div = "#C7D2FE"      # Subtle indigo divider

    orc_panel_fill = "#F1F5F9"    # Cool architectural slate panel for Step 3
    orc_hdr_fill = "#E2E8F0"      # Crisp header band for Step 3
    orc_stroke = "#334155"

    det_well_fill = "#F1F5F9"     # Cool slate well for deterministic checkers
    det_well_div = "#CBD5E1"
    det_stroke = "#475569"

    exec_fill = "#E8EEF5"         # Cool steel-slate for Compilation & Oracle Checking
    exec_well = "#DCE5F0"
    exec_stroke = "#1E293B"

    zllm_fill = "#DCFCE7"         # Emerald green capsule for Zero LLM
    zllm_stroke = "#15803D"
    zllm_text = "#14532D"

    text_color = "#0F172A"
    subtext_color = "#475569"
    edge_color = "#334155"

    # =========================================================================
    # 1. INPUT ICONS (Left Column — exact vertical alignment)
    # =========================================================================
    # Top Input icon: center y=48 (matches Step 1 card y=26..70, center y=48)
    svg.append(f'''
  <!-- Top Input: Specs, Docs and Patches -->
  <g transform="translate(14, 31)" filter="url(#card-shadow)">
    <path d="M 10 0 L 26 0 L 35 9 L 35 34 L 10 34 Z" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M 26 0 L 26 9 L 35 9 Z" fill="#E2E8F0" stroke="#1E293B" stroke-width="1.2" stroke-linejoin="round"/>
    <line x1="14" y1="13" x2="30" y2="13" stroke="#475569" stroke-width="1.15"/>
    <line x1="14" y1="18.5" x2="30" y2="18.5" stroke="#475569" stroke-width="1.15"/>
    <!-- Subtle +/- patch diff motif inside input doc -->
    <line x1="14" y1="24.5" x2="25" y2="24.5" stroke="#16A34A" stroke-width="1.4"/>
    <line x1="14" y1="28.5" x2="22" y2="28.5" stroke="#DC2626" stroke-width="1.4"/>
  </g>
  <text x="36.5" y="79" font-size="10" font-weight="500" fill="{text_color}" text-anchor="middle">Specs, Docs</text>
  <text x="36.5" y="91.5" font-size="10" font-weight="500" fill="{text_color}" text-anchor="middle">and Patches</text>

  <!-- Bottom Input icon: center y=134 (matches Card 2a y=115..153, center y=134) -->
  <g transform="translate(14, 118)" filter="url(#card-shadow)">
    <rect x="9" y="0" width="27" height="32" rx="3" fill="#FFFFFF"/>
    <path d="M 12 0 L 33 0 Q 36 0 36 3 L 36 7.5 L 9 7.5 L 9 3 Q 9 0 12 0 Z" fill="#E2E8F0"/>
    <line x1="9" y1="7.5" x2="36" y2="7.5" stroke="#1E293B" stroke-width="1"/>
    <rect x="9" y="0" width="27" height="32" rx="3" fill="none" stroke="#1E293B" stroke-width="1.3"/>
    <text x="22.5" y="23.5" font-family="Menlo, Monaco, 'Courier New', monospace" font-size="12" font-weight="700" fill="#1E293B" text-anchor="middle">&#123;&#125;</text>
  </g>
  <text x="36.5" y="164" font-size="10" font-weight="500" fill="{text_color}" text-anchor="middle">Compiler</text>
  <text x="36.5" y="176.5" font-size="10" font-weight="500" fill="{text_color}" text-anchor="middle">Source Code</text>
''')

    # =========================================================================
    # 2. STEP 1: Security Invariant Extraction (x=94..328, y=26..70, center y=48)
    #    Left well schematic: Doc/Diff -> Shield Contract Φ
    # =========================================================================
    svg.append(f'''
  <!-- Step 1: Security Invariant Extraction -->
  <g transform="translate(94, 26)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="234" height="44" rx="4" fill="{llm_card_fill}"/>
    <path d="M 4 0 L 42 0 L 42 44 L 4 44 Q 0 44 0 40 L 0 4 Q 0 0 4 0 Z" fill="{llm_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="44" stroke="{llm_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="234" height="44" rx="4" fill="none" stroke="{llm_card_stroke}" stroke-width="1.25"/>
    <!-- Mini-schematic: Rule lines -> Shield Φ -->
    <rect x="6" y="12" width="11" height="19" rx="1.5" fill="#FFFFFF" stroke="#3B5998" stroke-width="1"/>
    <line x1="8.5" y1="16.5" x2="14.5" y2="16.5" stroke="#3B5998" stroke-width="1"/>
    <line x1="8.5" y1="20.5" x2="14.5" y2="20.5" stroke="#16A34A" stroke-width="1.15"/>
    <line x1="8.5" y1="24.5" x2="13" y2="24.5" stroke="#3B5998" stroke-width="1"/>
    <line x1="18.5" y1="21.5" x2="22" y2="21.5" stroke="#3B5998" stroke-width="1.1"/>
    <path d="M 29.5 11.5 L 36.5 14.2 L 36.5 21.5 C 36.5 26.2 33.2 29.5 29.5 31.2 C 25.8 29.5 22.5 26.2 22.5 21.5 L 22.5 14.2 Z" fill="#FFFFFF" stroke="#1E3A8A" stroke-width="1.15"/>
    <text x="29.5" y="24" font-size="8.5" font-weight="700" fill="#1E3A8A" text-anchor="middle">&#934;</text>

    <text x="128" y="18.5" font-size="10.6" font-weight="700" fill="{text_color}" text-anchor="middle">Security Invariant Extraction</text>
    <text x="128" y="33" font-size="9.3" font-weight="400" fill="{subtext_color}" text-anchor="middle">CoT + RAG</text>
    <use href="#bot-logo" x="213" y="5"/>
  </g>
  <line x1="51" y1="48" x2="92" y2="48" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
''')

    # =========================================================================
    # 3. STEP 2: Compiler Source Mapping (x=84..338, y=100..246, center x=211)
    #    Card 2a schematic: Call-Graph DAG
    #    Card 2b schematic: 3-tier Hierarchy / CFG Branch Diamond
    # =========================================================================
    svg.append(f'''
  <!-- Step 2: Compiler Source Mapping Container -->
  <g>
    <rect x="84" y="100" width="254" height="146" rx="8" fill="{stage_tint}" stroke="{dashed_stroke}" stroke-width="1.25" stroke-dasharray="5,3.5"/>
    <use href="#bot-logo" x="132" y="222"/>
    <text x="221" y="234" font-size="10.8" font-weight="700" fill="#0F172A" text-anchor="middle">Compiler Source Mapping</text>
  </g>

  <!-- Card 2a: Call-Graph Analysis (x=96..326, y=115..153, center y=134) -->
  <g transform="translate(96, 115)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="230" height="38" rx="4" fill="{llm_card_fill}"/>
    <path d="M 4 0 L 42 0 L 42 38 L 4 38 Q 0 38 0 34 L 0 4 Q 0 0 4 0 Z" fill="{llm_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="38" stroke="{llm_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="230" height="38" rx="4" fill="none" stroke="{llm_card_stroke}" stroke-width="1.2"/>
    <!-- Mini-schematic: Directed Call-Graph DAG with highlighted path -->
    <line x1="21" y1="9" x2="12" y2="19" stroke="#94A3B8" stroke-width="1.1"/>
    <line x1="21" y1="9" x2="30" y2="19" stroke="#2563EB" stroke-width="1.35"/>
    <line x1="12" y1="19" x2="12" y2="29" stroke="#94A3B8" stroke-width="1.1"/>
    <line x1="30" y1="19" x2="23" y2="29" stroke="#2563EB" stroke-width="1.35"/>
    <line x1="30" y1="19" x2="35" y2="29" stroke="#94A3B8" stroke-width="1.1"/>
    <circle cx="21" cy="9" r="2.6" fill="#2563EB"/>
    <circle cx="12" cy="19" r="2.4" fill="#FFFFFF" stroke="#64748B" stroke-width="1.1"/>
    <circle cx="30" cy="19" r="2.6" fill="#2563EB"/>
    <circle cx="12" cy="29" r="2.2" fill="#FFFFFF" stroke="#64748B" stroke-width="1.1"/>
    <circle cx="23" cy="29" r="2.5" fill="#1D4ED8"/>
    <circle cx="35" cy="29" r="2.2" fill="#FFFFFF" stroke="#64748B" stroke-width="1.1"/>

    <text x="136" y="23" font-size="10.6" font-weight="700" fill="{text_color}" text-anchor="middle">Call-Graph Analysis</text>
  </g>

  <!-- Card 2b: Hierarchical Branch Mapping (x=96..326, y=167..209) -->
  <g transform="translate(96, 167)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="230" height="42" rx="4" fill="{llm_card_fill}"/>
    <path d="M 4 0 L 42 0 L 42 42 L 4 42 Q 0 42 0 38 L 0 4 Q 0 0 4 0 Z" fill="{llm_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="42" stroke="{llm_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="230" height="42" rx="4" fill="none" stroke="{llm_card_stroke}" stroke-width="1.2"/>
    <!-- Mini-schematic: 3-level Funnel -> CFG Branch Diamond -->
    <rect x="9" y="6.5" width="24" height="5" rx="1" fill="#93C5FD" stroke="#1E3A8A" stroke-width="0.9"/>
    <rect x="13" y="14" width="16" height="5" rx="1" fill="#60A5FA" stroke="#1E3A8A" stroke-width="0.9"/>
    <line x1="21" y1="19" x2="21" y2="22.5" stroke="#1E3A8A" stroke-width="1"/>
    <polygon points="21,22.5 27.5,28 21,33.5 14.5,28" fill="#FFFFFF" stroke="#1E3A8A" stroke-width="1.15"/>
    <line x1="27.5" y1="28" x2="34" y2="35" stroke="#2563EB" stroke-width="1.35"/>
    <line x1="14.5" y1="28" x2="9" y2="35" stroke="#94A3B8" stroke-width="1"/>

    <text x="136" y="17.5" font-size="10.5" font-weight="700" fill="{text_color}" text-anchor="middle">Hierarchical Branch Mapping</text>
    <text x="136" y="31.5" font-size="9.2" font-weight="400" fill="{subtext_color}" text-anchor="middle">Pass &#8594; Function &#8594; Branch</text>
  </g>

  <line x1="51" y1="134" x2="94" y2="134" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <line x1="211" y1="70" x2="211" y2="113" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="218" y="92" font-size="9.4" font-weight="500" fill="{edge_color}">Invariants</text>
  <line x1="211" y1="153" x2="211" y2="165" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
''')

    # =========================================================================
    # 4. STEP 3: Programmatic Oracle Construction (x=386..628, y=26..246)
    #    3a schematic: Stack Frame Layout [Buf | Can | RA]
    #    3b schematic: Sandbox + Trap Pulse
    #    3c: Emerald Rounded Capsule with Shield-Check emblem
    # =========================================================================
    svg.append(f'''
  <!-- Step 3: Programmatic Oracle Construction Container -->
  <g filter="url(#card-shadow)">
    <rect x="386" y="26" width="242" height="220" rx="8" fill="{orc_panel_fill}"/>
    <path d="M 394 26 L 620 26 Q 628 26 628 34 L 628 70 L 386 70 L 386 34 Q 386 26 394 26 Z" fill="{orc_hdr_fill}"/>
    <line x1="386" y1="70" x2="628" y2="70" stroke="#CBD5E1" stroke-width="1.1"/>
    <rect x="386" y="26" width="242" height="220" rx="8" fill="none" stroke="{orc_stroke}" stroke-width="1.3"/>
    <text x="500" y="45.5" font-size="10.8" font-weight="700" fill="{text_color}" text-anchor="middle">Programmatic Oracle Construction</text>
    <text x="500" y="60" font-size="9.3" font-weight="400" fill="{subtext_color}" text-anchor="middle">Formally Validated Checkers</text>
    <use href="#bot-logo" x="607" y="31"/>
  </g>

  <!-- 3a: Static Audit Checkers (Stack Frame Layout schematic) -->
  <g transform="translate(397, 84)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="220" height="38" rx="4" fill="#FFFFFF"/>
    <path d="M 4 0 L 42 0 L 42 38 L 4 38 Q 0 38 0 34 L 0 4 Q 0 0 4 0 Z" fill="{det_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="38" stroke="{det_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="220" height="38" rx="4" fill="none" stroke="{det_stroke}" stroke-width="1.15"/>
    <!-- Mini-schematic: Stack slots [Buf | Canary | RA] -->
    <rect x="8" y="6" width="26" height="8" rx="1" fill="#FFFFFF" stroke="#475569" stroke-width="1"/>
    <rect x="8" y="15" width="26" height="8" rx="1" fill="#DCFCE7" stroke="#15803D" stroke-width="1"/>
    <rect x="8" y="24" width="26" height="8" rx="1" fill="#E2E8F0" stroke="#475569" stroke-width="1"/>
    <line x1="13" y1="19" x2="29" y2="19" stroke="#15803D" stroke-width="1.15" stroke-dasharray="2,1.5"/>

    <text x="131" y="23" font-size="10.5" font-weight="700" fill="{text_color}" text-anchor="middle">Static Audit Checkers</text>
  </g>

  <!-- 3b: Dynamic Sandbox Checkers (Sandbox + Runtime Trap Pulse schematic) -->
  <g transform="translate(397, 134)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="220" height="38" rx="4" fill="#FFFFFF"/>
    <path d="M 4 0 L 42 0 L 42 38 L 4 38 Q 0 38 0 34 L 0 4 Q 0 0 4 0 Z" fill="{det_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="38" stroke="{det_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="220" height="38" rx="4" fill="none" stroke="{det_stroke}" stroke-width="1.15"/>
    <!-- Mini-schematic: Isolated Sandbox Box + Signal Trap Waveform -->
    <rect x="7.5" y="7" width="27" height="24" rx="2.5" fill="#FFFFFF" stroke="#475569" stroke-width="1.1" stroke-dasharray="3,2"/>
    <polyline points="10.5,21 15.5,21 18,12.5 21.5,26.5 24,18 27,21 31.5,21" fill="none" stroke="#0F766E" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round"/>

    <text x="131" y="23" font-size="10.5" font-weight="700" fill="{text_color}" text-anchor="middle">Dynamic Sandbox Checkers</text>
  </g>

  <!-- 3c: Distinct Rounded Emerald Capsule for Zero LLM in Adjudication -->
  <g transform="translate(403, 190)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="208" height="32" rx="16" fill="{zllm_fill}" stroke="{zllm_stroke}" stroke-width="1.4"/>
    <!-- Deterministic Shield-Check Emblem -->
    <path d="M 26 8 L 32.5 10.5 L 32.5 16.3 C 32.5 20.3 29.6 23.1 26 24.5 C 22.4 23.1 19.5 20.3 19.5 16.3 L 19.5 10.5 Z" fill="#FFFFFF" stroke="#15803D" stroke-width="1.25"/>
    <polyline points="23.2,16.3 25.2,18.3 29,14" fill="none" stroke="#15803D" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="115" y="20" font-size="10.6" font-weight="700" fill="{zllm_text}" text-anchor="middle">Zero LLM in Adjudication</text>
  </g>

  <line x1="328" y1="48" x2="384" y2="48" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="357" y="40.5" font-size="9.4" font-weight="500" fill="{edge_color}" text-anchor="middle">Invariants</text>
''')

    # =========================================================================
    # 5. STEP 4: Agentic Directed Fuzzing (x=686..956, y=14..246, center x=821)
    #    4a schematic: C Seed Code Block
    #    4b schematic: 8-tooth Compiler Gear + Deterministic Verdict Check
    #    4c schematic: Branch Flip Mutation Motif
    # =========================================================================
    gear_markup = gear_svg(15.5, 19.0, 7.2, 5.0, 2.0, exec_well)

    svg.append(f'''
  <!-- Step 4: Agentic Directed Fuzzing Container -->
  <g>
    <rect x="686" y="14" width="270" height="232" rx="8" fill="{stage_tint}" stroke="{dashed_stroke}" stroke-width="1.25" stroke-dasharray="5,3.5"/>
    <text x="821" y="234" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Agentic Directed Fuzzing</text>
  </g>

  <!-- Top Card: Targeted Seed Synthesis (x=697..945, y=27..69) -->
  <g transform="translate(697, 27)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="248" height="42" rx="4" fill="{llm_card_fill}"/>
    <path d="M 4 0 L 42 0 L 42 42 L 4 42 Q 0 42 0 38 L 0 4 Q 0 0 4 0 Z" fill="{llm_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="42" stroke="{llm_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="248" height="42" rx="4" fill="none" stroke="{llm_card_stroke}" stroke-width="1.2"/>
    <!-- Mini-schematic: Synthesized Seed Code Snippet -->
    <rect x="8" y="8" width="26" height="26" rx="2" fill="#FFFFFF" stroke="#3B5998" stroke-width="1.1"/>
    <line x1="12" y1="14" x2="24" y2="14" stroke="#64748B" stroke-width="1.2"/>
    <line x1="15" y1="19.5" x2="30" y2="19.5" stroke="#2563EB" stroke-width="1.4"/>
    <line x1="15" y1="25" x2="27" y2="25" stroke="#2563EB" stroke-width="1.4"/>
    <line x1="12" y1="29.5" x2="19" y2="29.5" stroke="#64748B" stroke-width="1.2"/>

    <text x="136" y="17.5" font-size="10.6" font-weight="700" fill="{text_color}" text-anchor="middle">Targeted Seed Synthesis</text>
    <text x="136" y="31.5" font-size="9.3" font-weight="400" fill="{subtext_color}" text-anchor="middle">Generator Agent</text>
    <use href="#bot-logo" x="227" y="5"/>
  </g>

  <!-- Middle Card: Compilation & Oracle Checking (x=697..945, y=96..134, center y=115) -->
  <g transform="translate(697, 96)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="248" height="38" rx="4" fill="{exec_fill}"/>
    <path d="M 4 0 L 42 0 L 42 38 L 4 38 Q 0 38 0 34 L 0 4 Q 0 0 4 0 Z" fill="{exec_well}"/>
    <line x1="42" y1="0" x2="42" y2="38" stroke="#CBD5E1" stroke-width="1"/>
    <rect x="0" y="0" width="248" height="38" rx="4" fill="none" stroke="{exec_stroke}" stroke-width="1.25"/>
    <!-- Mini-schematic: 8-tooth Compiler Gear + Binary Verdict Check -->
    {gear_markup}
    <polyline points="26,20 29.2,23.2 35.8,14.8" fill="none" stroke="#15803D" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>

    <text x="145" y="23" font-size="10.6" font-weight="700" fill="{text_color}" text-anchor="middle">Compilation &amp; Oracle Checking</text>
  </g>

  <!-- Bottom Card: Guided Seed Mutation (x=697..945, y=161..203) -->
  <g transform="translate(697, 161)" filter="url(#card-shadow)">
    <rect x="0" y="0" width="248" height="42" rx="4" fill="{llm_card_fill}"/>
    <path d="M 4 0 L 42 0 L 42 42 L 4 42 Q 0 42 0 38 L 0 4 Q 0 0 4 0 Z" fill="{llm_well_fill}"/>
    <line x1="42" y1="0" x2="42" y2="42" stroke="{llm_well_div}" stroke-width="1"/>
    <rect x="0" y="0" width="248" height="42" rx="4" fill="none" stroke="{llm_card_stroke}" stroke-width="1.2"/>
    <!-- Mini-schematic: Branch Flip / Guided Mutation Path -->
    <circle cx="11.5" cy="21" r="2.5" fill="#1E3A8A"/>
    <path d="M 14 21 L 20.5 21 L 31 11.5" fill="none" stroke="#94A3B8" stroke-width="1.15" stroke-dasharray="2,1.5"/>
    <path d="M 20.5 21 L 31 30.5" fill="none" stroke="#2563EB" stroke-width="1.5"/>
    <circle cx="32" cy="11" r="2.2" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1"/>
    <circle cx="32" cy="31" r="2.6" fill="#2563EB"/>
    <path d="M 27.5 15.5 A 7.5 7.5 0 0 1 27.5 25.5" fill="none" stroke="#2563EB" stroke-width="1.15"/>
    <polyline points="25.7,24.2 27.6,26.1 29.3,23.9" fill="none" stroke="#2563EB" stroke-width="1.15" stroke-linecap="round" stroke-linejoin="round"/>

    <text x="136" y="17.5" font-size="10.6" font-weight="700" fill="{text_color}" text-anchor="middle">Guided Seed Mutation</text>
    <text x="136" y="31.5" font-size="9.3" font-weight="400" fill="{subtext_color}" text-anchor="middle">Feedback Agent</text>
    <use href="#bot-logo" x="227" y="5"/>
  </g>

  <!-- Arrows entering Step 4 -->
  <line x1="628" y1="48" x2="695" y2="48" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="657" y="40.5" font-size="9.4" font-weight="500" fill="{edge_color}" text-anchor="middle">Invariants</text>

  <line x1="628" y1="115" x2="695" y2="115" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="657" y="107.5" font-size="9.4" font-weight="500" fill="{edge_color}" text-anchor="middle">Checkers</text>

  <!-- Internal Fuzzing Flow -->
  <line x1="821" y1="69" x2="821" y2="94" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="828" y="85" font-size="9.4" font-weight="500" fill="{edge_color}">Seeds</text>

  <line x1="781" y1="134" x2="781" y2="159" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="774" y="150" font-size="9.2" font-weight="500" fill="{edge_color}" text-anchor="end">Branch Traces</text>

  <line x1="861" y1="161" x2="861" y2="136" stroke="#2563EB" stroke-width="1.25" marker-end="url(#arr-indigo)"/>
  <text x="868" y="150" font-size="9.2" font-weight="600" fill="#1D4ED8">Mutated Seeds</text>
''')

    # =========================================================================
    # 6. BOTTOM CONNECTOR: Call Graph & Mapped Branches (Step 2 -> Step 4)
    # =========================================================================
    svg.append(f'''
  <path d="M 211 246 L 211 268 L 821 268 L 821 248" fill="none" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="516" y="262" font-size="9.5" font-weight="500" fill="{edge_color}" text-anchor="middle">Call Graph &amp; Mapped Branches</text>
''')

    # =========================================================================
    # 7. OUTPUT (Far Right): Silent Defense Bugs (icon height=38 at y=96..134, center y=115)
    # =========================================================================
    svg.append(f'''
  <line x1="945" y1="115" x2="1000" y2="115" stroke="#DC2626" stroke-width="1.3" marker-end="url(#arr-crimson)"/>
  <text x="972.5" y="107" font-size="9.4" font-weight="700" fill="#DC2626" text-anchor="middle">FAIL</text>

  <g transform="translate(1002, 96)" filter="url(#card-shadow)">
    <path d="M 12 0 L 26 0 L 35 9 L 35 38 L 12 38 Z" fill="#FEF2F2" stroke="#991B1B" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M 26 0 L 26 9 L 35 9 Z" fill="#FECACA" stroke="#991B1B" stroke-width="1.2" stroke-linejoin="round"/>
    <ellipse cx="23.5" cy="22.5" rx="4.5" ry="5.5" fill="#DC2626"/>
    <circle cx="23.5" cy="15.5" r="2.4" fill="#DC2626"/>
    <line x1="16.5" y1="19.5" x2="30.5" y2="19.5" stroke="#DC2626" stroke-width="1.15"/>
    <line x1="15.5" y1="23.5" x2="31.5" y2="23.5" stroke="#DC2626" stroke-width="1.15"/>
    <line x1="16.5" y1="27.5" x2="30.5" y2="27.5" stroke="#DC2626" stroke-width="1.15"/>
    <line x1="21.5" y1="13.5" x2="19.5" y2="10.5" stroke="#DC2626" stroke-width="1.15"/>
    <line x1="25.5" y1="13.5" x2="27.5" y2="10.5" stroke="#DC2626" stroke-width="1.15"/>
  </g>
  <text x="1025.5" y="149" font-size="10.5" font-weight="700" fill="{text_color}" text-anchor="middle">Silent Defense</text>
  <text x="1025.5" y="161.5" font-size="10.5" font-weight="700" fill="{text_color}" text-anchor="middle">Bugs</text>
''')

    svg.append('</svg>')
    return "".join(svg)


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    svg_content = generate_svg()
    svg_path = os.path.join(base_dir, "figures", "method-overview.svg")
    pdf_path = os.path.join(base_dir, "figures", "method-overview.pdf")
    png_path = os.path.join(base_dir, "figures", "method-overview.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {svg_path}")

    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, svg_path], check=True)
    print(f"Generated {pdf_path}")
    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-d", "300", "-p", "300", "-o", png_path, svg_path], check=True)
    print(f"Generated {png_path}")


if __name__ == "__main__":
    main()
