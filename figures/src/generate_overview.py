#!/usr/bin/env python3
"""
Generate a publication-grade academic system architecture overview diagram
for DeFuzz:
- Aesthetic: Handcrafted academic vector diagram with crisp typography.
- Color Scheme: Bright, soft luminous pastel yellow (#FEF9C3).
- Subtext Constraint: At most ONE line of subtext per card, 3-4 words max, zero visual clutter.
- Precision Layout: Zero arrow/text overlaps, perfectly balanced inter-component gaps.
"""

import subprocess
import os

def generate_svg():
    W, H = 1080, 285
    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="background-color: #FFFFFF; font-family: 'Times New Roman', Times, 'Nimbus Roman No9 L', serif;">
  <defs>
    <!-- Sharp, crisp arrow markers -->
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#1E293B"/>
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#B45309"/>
    </marker>
  </defs>
''')

    # Color Palette: Bright Soft Pastel Yellow with Crisp Charcoal Borders
    card_fill = "#FEF9C3"       # Bright, soft luminous pastel yellow (Tailwind yellow-100)
    card_stroke = "#1E293B"     # Crisp dark slate/charcoal border
    card_sw = "1.2"
    
    subcard_fill = "#FFFFFF"    # Pure crisp white for interior cards
    subcard_stroke = "#475569"  # Slate-600 fine border
    
    exec_fill = "#F1F5F9"       # High-contrast cool slate for execution node
    exec_stroke = "#1E293B"     # Dark slate border
    
    dashed_stroke = "#1D4ED8"   # Royal blue dashed container
    dashed_sw = "1.3"
    
    text_color = "#0F172A"      # Crisp high-contrast black/slate
    subtext_color = "#475569"   # Refined readable slate-gray (3-4 words max)

    # =========================================================================
    # 1. INPUT ICONS (Left Column)
    # =========================================================================
    # Top Input: Compiler Corpora
    svg.append(f'''
  <!-- Top Input: Compiler Corpora -->
  <g transform="translate(20, 30)">
    <path d="M 12 0 L 26 0 L 34 8 L 34 30 L 12 30 Z" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M 26 0 L 26 8 L 34 8 Z" fill="#E2E8F0" stroke="#1E293B" stroke-width="1.2" stroke-linejoin="round"/>
    <line x1="16" y1="12" x2="30" y2="12" stroke="#1E293B" stroke-width="1.1"/>
    <line x1="16" y1="17" x2="30" y2="17" stroke="#1E293B" stroke-width="1.1"/>
    <line x1="16" y1="22" x2="25" y2="22" stroke="#1E293B" stroke-width="1.1"/>
    <text x="23" y="44" font-size="12" fill="{text_color}" text-anchor="middle">Compiler</text>
    <text x="23" y="57" font-size="12" fill="{text_color}" text-anchor="middle">Corpora</text>
  </g>
''')

    # Bottom Input: Compiler Source Code
    svg.append(f'''
  <!-- Bottom Input: Compiler Source Code -->
  <g transform="translate(20, 130)">
    <rect x="10" y="0" width="26" height="28" rx="2" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.3"/>
    <text x="23" y="19" font-family="'Courier New', monospace" font-size="14" font-weight="bold" fill="#1E293B" text-anchor="middle">&#123;&#125;</text>
    <text x="23" y="42" font-size="12" fill="{text_color}" text-anchor="middle">Compiler</text>
    <text x="23" y="55" font-size="12" fill="{text_color}" text-anchor="middle">Source Code</text>
  </g>
''')

    # =========================================================================
    # 2. STEP 1: Security Invariant Generation (Top Left Card)
    # =========================================================================
    # Box: x=106, y=30, w=182, h=38
    svg.append(f'''
  <!-- Step 1: Security Invariant Extraction -->
  <g transform="translate(106, 30)">
    <rect x="0" y="0" width="182" height="38" rx="2" fill="{card_fill}" stroke="{card_stroke}" stroke-width="{card_sw}"/>
    <text x="91" y="16" font-size="12" font-weight="bold" fill="{text_color}" text-anchor="middle">Security Invariant Extraction</text>
    <text x="91" y="29" font-size="10.5" fill="{subtext_color}" text-anchor="middle">Hybrid CoT &amp; RAG</text>
  </g>
''')

    # Arrow from Corpora to Invariant Extraction
    svg.append('''
  <line x1="56" y1="45" x2="104" y2="45" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
''')

    # =========================================================================
    # 3. STEP 2: Compiler Source Mapping (Bottom Middle-Left Dashed Box)
    # =========================================================================
    svg.append(f'''
  <!-- Step 2: Compiler Source Mapping Container -->
  <g>
    <rect x="98" y="100" width="220" height="146" rx="10" fill="none" stroke="{dashed_stroke}" stroke-width="{dashed_sw}" stroke-dasharray="5,4"/>
    <text x="208" y="238" font-size="12" font-weight="bold" fill="#0F172A" text-anchor="middle">Compiler Source Mapping</text>
  </g>
''')

    # Cards inside Step 2:
    # 2a: Pass & Function Localization
    # 2b: Decision Branch & AST Slicing
    svg.append(f'''
  <!-- Card 2a: Pass & Function Localization -->
  <g transform="translate(110, 114)">
    <rect x="0" y="0" width="196" height="36" rx="2" fill="{card_fill}" stroke="{card_stroke}" stroke-width="{card_sw}"/>
    <text x="98" y="15" font-size="11.5" font-weight="bold" fill="{text_color}" text-anchor="middle">Pass &amp; Function Localization</text>
    <text x="98" y="28" font-size="10" fill="{subtext_color}" text-anchor="middle">Defense Hook Identification</text>
  </g>

  <!-- Card 2b: Decision Branch & AST Slicing -->
  <g transform="translate(110, 168)">
    <rect x="0" y="0" width="196" height="36" rx="2" fill="{card_fill}" stroke="{card_stroke}" stroke-width="{card_sw}"/>
    <text x="98" y="15" font-size="11.5" font-weight="bold" fill="{text_color}" text-anchor="middle">Decision Branch &amp; AST Slicing</text>
    <text x="98" y="28" font-size="10" fill="{subtext_color}" text-anchor="middle">Gating Predicate Extraction</text>
  </g>
''')

    # Arrows inside Step 2:
    # Source Code -> Card 2a
    svg.append('''
  <line x1="56" y1="132" x2="108" y2="132" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
''')
    # Step 1 -> Card 2a (Invariants): Arrow at x=197, text padded to the right (x=205)
    svg.append('''
  <line x1="197" y1="68" x2="197" y2="112" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="205" y="92" font-size="10" font-style="italic" fill="#1E293B">Invariants</text>
''')
    # Card 2a -> Card 2b: Arrow at x=208, text with text-anchor="end" at x=202 (NO OVERLAP!)
    svg.append('''
  <line x1="208" y1="150" x2="208" y2="166" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="202" y="160" font-size="9.5" font-style="italic" fill="#1E293B" text-anchor="end">Pass Context</text>
''')

    # =========================================================================
    # 4. STEP 3: Programmatic Oracle Construction (Center Column Container)
    # =========================================================================
    # Box: x=354, y=28, w=220, h=218, rx=10
    svg.append(f'''
  <!-- Step 3: Programmatic Oracle Construction Container -->
  <g>
    <rect x="354" y="28" width="220" height="218" rx="10" fill="{card_fill}" stroke="{card_stroke}" stroke-width="{card_sw}"/>
    <text x="464" y="48" font-size="12" font-weight="bold" fill="{text_color}" text-anchor="middle">Programmatic Oracle Construction</text>
    <text x="464" y="61" font-size="10" fill="{subtext_color}" text-anchor="middle">Deterministic Multi-ISA Checkers</text>
    <line x1="366" y1="68" x2="562" y2="68" stroke="#E2E8F0" stroke-width="1"/>
  </g>
''')

    # Sub-cards inside Oracle Construction (Clean single-line subtext):
    svg.append(f'''
  <!-- 3a: Static Audit Checkers (Subtext: 4 words) -->
  <g transform="translate(364, 76)">
    <rect x="0" y="0" width="200" height="38" rx="2" fill="{subcard_fill}" stroke="{subcard_stroke}" stroke-width="1"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="{text_color}" text-anchor="middle">Static Audit Checkers</text>
    <text x="100" y="29" font-size="10" fill="{subtext_color}" text-anchor="middle">DWARF &amp; Binary Patterns</text>
  </g>

  <!-- 3b: Dynamic Sandbox Checkers (Subtext: 4 words) -->
  <g transform="translate(364, 126)">
    <rect x="0" y="0" width="200" height="38" rx="2" fill="{subcard_fill}" stroke="{subcard_stroke}" stroke-width="1"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="{text_color}" text-anchor="middle">Dynamic Sandbox Checkers</text>
    <text x="100" y="29" font-size="10" fill="{subtext_color}" text-anchor="middle">QEMU &amp; Runtime Traces</text>
  </g>

  <!-- 3c: Multi-ISA Verification (Subtext: 3 words) -->
  <g transform="translate(364, 176)">
    <rect x="0" y="0" width="200" height="38" rx="2" fill="{subcard_fill}" stroke="{subcard_stroke}" stroke-width="1"/>
    <text x="100" y="16" font-size="11" font-weight="bold" fill="#1D4ED8" text-anchor="middle">Zero LLM in Adjudication</text>
    <text x="100" y="29" font-size="10" fill="{text_color}" text-anchor="middle">x86-64 &#8226; AArch64 &#8226; RISC-V</text>
  </g>
''')

    # Arrow from Step 1 (Invariants) -> Step 3 (Oracles)
    svg.append('''
  <line x1="288" y1="48" x2="352" y2="48" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="320" y="41" font-size="10" font-style="italic" fill="#1E293B" text-anchor="middle">Invariants</text>
''')

    # Arrow from Step 2b (Decision Branch & Predicates) -> Step 3 (Oracles)
    # Balanced gap: x=318 to x=354 (36px). Vertical line at x=336.
    # Label "Predicates" floats above horizontal segment entering Step 3 (NO OVERLAP!)
    svg.append('''
  <path d="M 306 186 L 336 186 L 336 145 L 352 145" fill="none" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="336" y="137" font-size="9.5" font-style="italic" fill="#1E293B" text-anchor="middle">Predicates</text>
''')

    # =========================================================================
    # 5. STEP 4: Agentic Directed Fuzzing (Right Dashed Box)
    # =========================================================================
    # Dashed box begins at x=626, leaving 52px gap from Step 3 (574 to 626)
    svg.append(f'''
  <!-- Step 4: Agentic Directed Fuzzing Container -->
  <g>
    <rect x="626" y="14" width="268" height="246" rx="10" fill="none" stroke="{dashed_stroke}" stroke-width="{dashed_sw}" stroke-dasharray="5,4"/>
    <text x="760" y="244" font-size="12.5" font-weight="bold" fill="#0F172A" text-anchor="middle">Agentic Directed Fuzzing</text>
  </g>
''')

    # Cards inside Step 4 (Each with single-line 3-4 word subtext):
    # Top: Generator Agent (x=638, y=32, w=244, h=36)
    # Middle: Compiler Build (x=638, y=94, w=244, h=40)
    # Bottom: Adaptive Feedback Agent (x=638, y=162, w=244, h=36)
    svg.append(f'''
  <!-- Top Card: Generator Agent -->
  <g transform="translate(638, 32)">
    <rect x="0" y="0" width="244" height="36" rx="2" fill="{card_fill}" stroke="{card_stroke}" stroke-width="{card_sw}"/>
    <text x="122" y="15" font-size="11.5" font-weight="bold" fill="{text_color}" text-anchor="middle">Generator Agent</text>
    <text x="122" y="28" font-size="10" fill="{subtext_color}" text-anchor="middle">Anti-DCE Seed Synthesis</text>
  </g>

  <!-- Middle Card: Compiler Build & Oracle Evaluation (Cool Slate Grey) -->
  <g transform="translate(638, 94)">
    <rect x="0" y="0" width="244" height="40" rx="2" fill="{exec_fill}" stroke="{exec_stroke}" stroke-width="{card_sw}"/>
    <text x="122" y="16" font-size="11.5" font-weight="bold" fill="{text_color}" text-anchor="middle">Compiler Build (GCC_INST)</text>
    <text x="122" y="30" font-size="10" font-weight="bold" fill="#1E293B" text-anchor="middle">Programmatic Oracle Adjudication</text>
  </g>

  <!-- Bottom Card: Adaptive Feedback Agent -->
  <g transform="translate(638, 162)">
    <rect x="0" y="0" width="244" height="36" rx="2" fill="{card_fill}" stroke="{card_stroke}" stroke-width="{card_sw}"/>
    <text x="122" y="15" font-size="11.5" font-weight="bold" fill="{text_color}" text-anchor="middle">Adaptive Feedback Agent</text>
    <text x="122" y="28" font-size="10" fill="{subtext_color}" text-anchor="middle">Diagnostics &amp; Telemetry Analysis</text>
  </g>
''')

    # Arrows entering Step 4:
    # 52px gap between x=574 and x=626. Labels centered at x=600 (NO OVERLAP!)
    svg.append('''
  <!-- From Invariants to Generator Agent -->
  <line x1="574" y1="48" x2="636" y2="48" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="600" y="41" font-size="10" font-style="italic" fill="#1E293B" text-anchor="middle">Invariants</text>

  <!-- From Oracles directly into Compiler Build & Adjudication -->
  <line x1="574" y1="106" x2="636" y2="106" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="600" y="99" font-size="10" font-style="italic" fill="#1E293B" text-anchor="middle">Oracles</text>
''')

    # Internal Fuzzing Flow:
    # 1. Generator Agent -> Compiler Build (Seeds)
    svg.append('''
  <line x1="760" y1="68" x2="760" y2="92" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="766" y="83" font-size="10.5" font-style="italic" fill="#1E293B">Seeds</text>
''')

    # 2. Compiler Build -> Feedback Agent (Telemetry)
    # Arrow at x=722, text with text-anchor="end" at x=715 (NO OVERLAP!)
    svg.append('''
  <!-- Downward arrow: Telemetry -->
  <line x1="722" y1="134" x2="722" y2="160" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="715" y="150" font-size="9.5" font-style="italic" fill="#1E293B" text-anchor="end">Telemetry</text>

  <!-- Upward arrow: Mutation Hints -->
  <line x1="796" y1="162" x2="796" y2="136" stroke="#B45309" stroke-width="1.2" marker-end="url(#arr-amber)"/>
  <text x="802" y="150" font-size="10" font-style="italic" font-weight="bold" fill="#B45309">Mutation Hints</text>
''')

    # =========================================================================
    # 6. BYPASS LINE: Compiler Source Code along bottom into GCC_INST
    # =========================================================================
    svg.append('''
  <!-- Bypass line from Compiler Source Code to GCC_INST build -->
  <path d="M 45 178 L 45 264 L 610 264 L 610 122 L 636 122" fill="none" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="320" y="259" font-size="10.5" font-style="italic" fill="#1E293B" text-anchor="middle">Compiler Source Code (Instrumentation &amp; Build)</text>
''')

    # =========================================================================
    # 7. OUTPUT (Far Right): Silent Defense Bugs / Report & PoC
    # =========================================================================
    svg.append(f'''
  <!-- Far Right Output: Silent Defense Bugs -->
  <line x1="882" y1="114" x2="946" y2="114" stroke="#1E293B" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="914" y="106" font-size="10" font-style="italic" fill="#DC2626" text-anchor="middle">Verdict: FAIL</text>

  <g transform="translate(948, 88)">
    <!-- Document Icon with folded corner -->
    <path d="M 12 0 L 26 0 L 34 8 L 34 38 L 12 38 Z" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.3" stroke-linejoin="round"/>
    <path d="M 26 0 L 26 8 L 34 8 Z" fill="#E2E8F0" stroke="#1E293B" stroke-width="1.2" stroke-linejoin="round"/>
    <!-- Bug silhouette inside doc -->
    <ellipse cx="23" cy="22" rx="4.5" ry="5.5" fill="#DC2626"/>
    <circle cx="23" cy="15" r="2.5" fill="#DC2626"/>
    <line x1="16" y1="19" x2="30" y2="19" stroke="#DC2626" stroke-width="1.1"/>
    <line x1="15" y1="23" x2="31" y2="23" stroke="#DC2626" stroke-width="1.1"/>
    <line x1="16" y1="27" x2="30" y2="27" stroke="#DC2626" stroke-width="1.1"/>
    <line x1="21" y1="13" x2="19" y2="10" stroke="#DC2626" stroke-width="1.1"/>
    <line x1="25" y1="13" x2="27" y2="10" stroke="#DC2626" stroke-width="1.1"/>

    <!-- Labels below -->
    <text x="23" y="52" font-size="12" font-weight="bold" fill="{text_color}" text-anchor="middle">Silent Defense Bugs</text>
    <text x="23" y="65" font-size="10" fill="{subtext_color}" text-anchor="middle">Verified PoCs &amp; Patches</text>
  </g>
''')

    svg.append('</svg>')
    return "".join(svg)

def main():
    svg_content = generate_svg()
    svg_path = "figures/method-overview.svg"
    pdf_path = "figures/method-overview.pdf"
    png_path = "figures/method-overview.png"

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {svg_path}")

    # Convert SVG to PDF and PNG using rsvg-convert
    try:
        subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, svg_path], check=True)
        print(f"Generated {pdf_path}")
        subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-d", "300", "-p", "300", "-o", png_path, svg_path], check=True)
        print(f"Generated {png_path}")
    except Exception as e:
        print(f"Conversion error: {e}")

if __name__ == "__main__":
    main()
