#!/usr/bin/env python3
"""
Generate a clean, streamlined, publication-grade vector diagram for Figure 2:
Multi-Source Security Invariant Extraction and Transfer Pipeline (Stage 1).
Produces SVG, PDF, PNG, and JPG.
"""

import os
import subprocess

def create_fig2_svg(output_base="figures/method-invariant-gen"):
    width = 1000
    height = 490

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    # Definitions
    svg.append('''
  <defs>
    <marker id="arr-gray" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#475569"/>
    </marker>
    <marker id="arr-dash" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#64748B"/>
    </marker>
  </defs>
''')

    # Title
    svg.append(f'''
  <text x="{width/2}" y="36" fill="#0F172A" font-size="18" font-weight="700" text-anchor="middle">Stage 1: Multi-Source Security Invariant Extraction and Transfer Pipeline</text>
''')

    # Dimensions for 3 main cards
    top_y = 58
    card_w = 285
    card_h = 330
    gap = 42
    c1_x = 35
    c2_x = c1_x + card_w + gap
    c3_x = c2_x + card_w + gap

    # CARD 1: Knowledge Corpora & Extraction
    svg.append(f'''
  <!-- Card 1: Knowledge Corpora & Extraction -->
  <rect x="{c1_x}" y="{top_y}" width="{card_w}" height="{card_h}" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.5"/>
  <text x="{c1_x + card_w/2}" y="{top_y + 28}" fill="#166534" font-size="14" font-weight="700" text-anchor="middle">1. Knowledge Corpora &amp; Extraction</text>

  <!-- Box 1A: Multi-Source Corpora -->
  <g transform="translate({c1_x + 15}, {top_y + 45})">
    <rect x="0" y="0" width="{card_w - 30}" height="110" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.2"/>
    <text x="12" y="22" fill="#15803D" font-size="11.5" font-weight="700">Multi-Source Corpora</text>
    
    <rect x="12" y="32" width="230" height="20" rx="3" fill="#F0FDF4"/>
    <text x="18" y="46" fill="#334155" font-size="10">&#x2022; Compiler Source &amp; Assertions (GCC/LLVM)</text>

    <rect x="12" y="56" width="230" height="20" rx="3" fill="#F0FDF4"/>
    <text x="18" y="70" fill="#334155" font-size="10">&#x2022; ISA &amp; ABI Specifications (x86, ARM, RV)</text>

    <rect x="12" y="80" width="230" height="20" rx="3" fill="#F0FDF4"/>
    <text x="18" y="94" fill="#334155" font-size="10">&#x2022; Historical Bug Patches (e.g. CVE-2023-4039)</text>
  </g>

  <!-- Box 1B: Dual Extraction Paths -->
  <g transform="translate({c1_x + 15}, {top_y + 170})">
    <rect x="0" y="0" width="{card_w - 30}" height="135" rx="6" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.2"/>
    <text x="12" y="22" fill="#15803D" font-size="11.5" font-weight="700">Dual Extraction Paths</text>

    <!-- Path A -->
    <rect x="12" y="32" width="230" height="42" rx="4" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
    <text x="20" y="48" fill="#14532D" font-size="10.5" font-weight="700">Segmented CoT Review</text>
    <text x="20" y="64" fill="#475569" font-size="9.5">Partitioned pass &amp; function boundary slicing</text>

    <!-- Path B -->
    <rect x="12" y="80" width="230" height="42" rx="4" fill="#DCFCE7" stroke="#86EFAC" stroke-width="1"/>
    <text x="20" y="96" fill="#14532D" font-size="10.5" font-weight="700">Historical Bug Probe Pool</text>
    <text x="20" y="112" fill="#475569" font-size="9.5">Distilled root causes across compiler backends</text>
  </g>
''')

    # Arrow 1 -> 2
    arr1_x = c1_x + card_w + 5
    svg.append(f'''
  <line x1="{arr1_x}" y1="{top_y + card_h/2}" x2="{arr1_x + gap - 10}" y2="{top_y + card_h/2}" 
        stroke="#475569" stroke-width="2.5" marker-end="url(#arr-gray)"/>
''')

    # CARD 2: Hybrid RAG & Generalization
    svg.append(f'''
  <!-- Card 2: Hybrid RAG & Generalization -->
  <rect x="{c2_x}" y="{top_y}" width="{card_w}" height="{card_h}" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
  <text x="{c2_x + card_w/2}" y="{top_y + 28}" fill="#92400E" font-size="14" font-weight="700" text-anchor="middle">2. Hybrid RAG &amp; Generalization</text>

  <!-- Box 2A: Dual-Aspect Query -->
  <g transform="translate({c2_x + 15}, {top_y + 45})">
    <rect x="0" y="0" width="{card_w - 30}" height="110" rx="6" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.2"/>
    <text x="12" y="22" fill="#B45309" font-size="11.5" font-weight="700">Dual-Aspect Query Formulation</text>

    <rect x="12" y="34" width="230" height="30" rx="4" fill="#FEF3C7"/>
    <text x="18" y="52" fill="#78350F" font-size="10"><tspan font-weight="700">Sparse BM25:</tspan> Critical code tokens &amp; ASTs</text>

    <rect x="12" y="70" width="230" height="30" rx="4" fill="#FEF3C7"/>
    <text x="18" y="88" fill="#78350F" font-size="10"><tspan font-weight="700">Dense Vector:</tspan> Semantic root cause embeddings</text>
  </g>

  <!-- Box 2B: Cross-Mechanism Transfer -->
  <g transform="translate({c2_x + 15}, {top_y + 170})">
    <rect x="0" y="0" width="{card_w - 30}" height="135" rx="6" fill="#FFFFFF" stroke="#FCD34D" stroke-width="1.2"/>
    <text x="12" y="22" fill="#B45309" font-size="11.5" font-weight="700">Cross-Mechanism Transfer Pipeline</text>

    <g transform="translate(14, 38)">
      <rect x="0" y="0" width="66" height="38" rx="4" fill="#FDE68A" stroke="#F59E0B" stroke-width="1"/>
      <text x="33" y="18" fill="#92400E" font-size="9.5" font-weight="700" text-anchor="middle">Distill</text>
      <text x="33" y="30" fill="#78350F" font-size="8" text-anchor="middle">Root Cause</text>

      <line x1="68" y1="19" x2="78" y2="19" stroke="#78350F" stroke-width="1.5" marker-end="url(#arr-gray)"/>

      <rect x="82" y="0" width="66" height="38" rx="4" fill="#FDE68A" stroke="#F59E0B" stroke-width="1"/>
      <text x="115" y="18" fill="#92400E" font-size="9.5" font-weight="700" text-anchor="middle">Filter</text>
      <text x="115" y="30" fill="#78350F" font-size="8" text-anchor="middle">Structural</text>

      <line x1="150" y1="19" x2="160" y2="19" stroke="#78350F" stroke-width="1.5" marker-end="url(#arr-gray)"/>

      <rect x="164" y="0" width="66" height="38" rx="4" fill="#FDE68A" stroke="#F59E0B" stroke-width="1"/>
      <text x="197" y="18" fill="#92400E" font-size="9.5" font-weight="700" text-anchor="middle">Specialize</text>
      <text x="197" y="30" fill="#78350F" font-size="8" text-anchor="middle">Frame Map</text>
    </g>

    <text x="14" y="102" fill="#64748B" font-size="9.5">&#x2022; Transfers across mechanisms (e.g. Canary &#8594; PAC)</text>
    <text x="14" y="118" fill="#64748B" font-size="9.5">&#x2022; Yields candidate invariants for diverse backends</text>
  </g>
''')

    # Arrow 2 -> 3
    arr2_x = c2_x + card_w + 5
    svg.append(f'''
  <line x1="{arr2_x}" y1="{top_y + card_h/2}" x2="{arr2_x + gap - 10}" y2="{top_y + card_h/2}" 
        stroke="#475569" stroke-width="2.5" marker-end="url(#arr-gray)"/>
''')

    # CARD 3: Acceptance Gates & Catalog
    svg.append(f'''
  <!-- Card 3: Acceptance Gates & Catalog -->
  <rect x="{c3_x}" y="{top_y}" width="{card_w}" height="{card_h}" rx="8" fill="#FAF5FF" stroke="#D8B4FE" stroke-width="1.5"/>
  <text x="{c3_x + card_w/2}" y="{top_y + 28}" fill="#6B21A8" font-size="14" font-weight="700" text-anchor="middle">3. Acceptance Gates &amp; Catalog</text>

  <!-- Box 3A: Acceptance Gates -->
  <g transform="translate({c3_x + 15}, {top_y + 45})">
    <rect x="0" y="0" width="{card_w - 30}" height="110" rx="6" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1.2"/>
    <text x="12" y="22" fill="#7E22CE" font-size="11.5" font-weight="700">Triple Acceptance Screening</text>

    <rect x="12" y="32" width="230" height="20" rx="3" fill="#FAF5FF"/>
    <text x="18" y="46" fill="#334155" font-size="10"><tspan font-weight="700">1. Grounding Gate:</tspan> Source evidence &amp; assertions</text>

    <rect x="12" y="56" width="230" height="20" rx="3" fill="#FAF5FF"/>
    <text x="18" y="70" fill="#334155" font-size="10"><tspan font-weight="700">2. Observability Gate:</tspan> Binary or runtime check</text>

    <rect x="12" y="80" width="230" height="20" rx="3" fill="#FAF5FF"/>
    <text x="18" y="94" fill="#334155" font-size="10"><tspan font-weight="700">3. Novelty Gate:</tspan> Deduplication threshold &#8805; 85%</text>
  </g>

  <!-- Box 3B: Invariant Catalog Φ -->
  <g transform="translate({c3_x + 15}, {top_y + 170})">
    <rect x="0" y="0" width="{card_w - 30}" height="135" rx="6" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1.2"/>
    <text x="12" y="22" fill="#7E22CE" font-size="11.5" font-weight="700">Security Invariant Catalog &#934;</text>

    <g transform="translate(14, 35)">
      <rect x="0" y="0" width="228" height="42" rx="4" fill="#F3E8FF" stroke="#C084FC" stroke-width="1.2"/>
      <text x="114" y="20" fill="#581C87" font-size="11" font-weight="700" text-anchor="middle">&#934; = {{ &#966;1, &#966;2, ..., &#966;n }}</text>
      <text x="114" y="34" fill="#6B21A8" font-size="9" text-anchor="middle">Formal Security Invariant Contracts</text>
    </g>

    <text x="14" y="98" fill="#475569" font-size="9.5">&#x2022; Formalized preconditions &amp; assertions</text>
    <text x="14" y="116" fill="#475569" font-size="9.5">&#x2022; Readied for downstream machine oracles</text>
  </g>
''')

    # Bottom Feedback Arrow: from Catalog (Card 3) back to Bug Probe Pool (Card 1)
    svg.append(f'''
  <!-- Feedback Arrow Loop -->
  <path d="M {c3_x + card_w/2} {top_y + card_h} 
           C {c3_x + card_w/2} {top_y + card_h + 46}, {c1_x + card_w/2} {top_y + card_h + 46}, {c1_x + card_w/2} {top_y + card_h} "
        fill="none" stroke="#64748B" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arr-dash)"/>
  
  <rect x="{width/2 - 165}" y="{top_y + card_h + 30}" width="330" height="26" rx="4" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
  <text x="{width/2}" y="{top_y + card_h + 47}" fill="#334155" font-size="10.5" font-weight="600" text-anchor="middle">&#8635; Confirmed Bug Feedback (Iterative Corpus Enrichment)</text>
''')

    svg.append('</svg>')

    os.makedirs(os.path.dirname(output_base), exist_ok=True)
    svg_path = f"{output_base}.svg"
    pdf_path = f"{output_base}.pdf"
    png_path = f"{output_base}.png"
    jpg_path = f"{output_base}.jpg"

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {svg_path}")

    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, svg_path], check=True)
    print(f"Compiled to {pdf_path}")

    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-d", "300", "-p", "300", "-o", png_path, svg_path], check=True)
    print(f"Compiled to {png_path}")

    subprocess.run(["/usr/bin/sips", "-s", "format", "jpeg", png_path, "--out", jpg_path], check=True)
    print(f"Compiled to {jpg_path}")

if __name__ == "__main__":
    create_fig2_svg()
