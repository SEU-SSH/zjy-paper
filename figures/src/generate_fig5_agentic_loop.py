#!/usr/bin/env python3
"""
Generate a clean, streamlined, publication-grade vector diagram for Figure 5:
Online Closed-Loop Agentic Fuzzing and Adaptive Feedback Loop (Stage 4).
Produces SVG, PDF, PNG, and JPG.
"""

import os
import subprocess

def create_fig5_svg(output_base="figures/method-agentic-loop"):
    width = 1060
    height = 560

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    svg.append('''
  <defs>
    <marker id="arr5-gray" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#475569"/>
    </marker>
    <marker id="arr5-purple" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#7C3AED"/>
    </marker>
    <marker id="arr5-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>
    <marker id="arr5-cyan" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#0284C7"/>
    </marker>
  </defs>
''')

    # Title at very top
    svg.append(f'''
  <text x="{width/2}" y="28" fill="#0F172A" font-size="17" font-weight="700" text-anchor="middle">Stage 4: Online Closed-Loop Agentic Fuzzing and Adaptive Feedback Loop</text>
''')

    # Cards start at top_y = 80
    top_y = 82
    box_h = 370

    # 1. Left Container: Orchestration & Generator Agent (Width: 250)
    c1_x = 30
    c1_w = 250
    svg.append(f'''
  <!-- Block 1: Orchestrator & Generator -->
  <rect x="{c1_x}" y="{top_y}" width="{c1_w}" height="{box_h}" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.5"/>
  <text x="{c1_x + c1_w/2}" y="{top_y + 26}" fill="#5B21B6" font-size="13" font-weight="700" text-anchor="middle">1. Orchestration &amp; Generation</text>

  <!-- Orchestrator Box -->
  <g transform="translate({c1_x + 14}, {top_y + 42})">
    <rect x="0" y="0" width="{c1_w - 28}" height="100" rx="6" fill="#FFFFFF" stroke="#C4B5FD" stroke-width="1.2"/>
    <text x="12" y="22" fill="#6D28D9" font-size="11.5" font-weight="700">Deterministic Orchestrator</text>
    <rect x="10" y="32" width="{c1_w - 48}" height="24" rx="3" fill="#EDE9FE"/>
    <text x="16" y="48" fill="#4C1D95" font-size="10" font-weight="600">Target Invariant: &#966;i</text>
    <rect x="10" y="62" width="{c1_w - 48}" height="24" rx="3" fill="#EDE9FE"/>
    <text x="16" y="78" fill="#4C1D95" font-size="10" font-weight="600">Time Budget: Fixed T</text>
  </g>

  <!-- Generator Agent Box -->
  <g transform="translate({c1_x + 14}, {top_y + 160})">
    <rect x="0" y="0" width="{c1_w - 28}" height="190" rx="6" fill="#FFFFFF" stroke="#C4B5FD" stroke-width="1.2"/>
    <text x="12" y="24" fill="#6D28D9" font-size="12" font-weight="700">LLM Generator Agent</text>
    
    <rect x="10" y="36" width="{c1_w - 48}" height="50" rx="4" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="16" y="54" fill="#5B21B6" font-size="10.5" font-weight="700">Anti-DCE C/C++ Seeds</text>
    <text x="16" y="72" fill="#6B21A8" font-size="9.5">VLAs, dynamic bounds, asm barriers</text>

    <text x="12" y="108" fill="#475569" font-size="9.5">&#x2022; Checker-aware prompt context</text>
    <text x="12" y="126" fill="#475569" font-size="9.5">&#x2022; Forces compiler backend</text>
    <text x="12" y="140" fill="#475569" font-size="9.5">  to preserve full stack frames</text>
    <text x="12" y="164" fill="#059669" font-size="10" font-weight="700">&#8658; Emits seed_sp_probe.c</text>
  </g>
''')

    # Arrow 1 -> 2
    arr1_x = c1_x + c1_w + 4
    svg.append(f'''
  <line x1="{arr1_x}" y1="{top_y + 245}" x2="{arr1_x + 32}" y2="{top_y + 245}" 
        stroke="#475569" stroke-width="2.5" marker-end="url(#arr5-gray)"/>
  <text x="{arr1_x + 16}" y="{top_y + 237}" fill="#475569" font-size="9" font-weight="600" text-anchor="middle">Seed .c</text>
''')

    # 2. Middle Container: Build & Dual Oracle (Width: 260)
    c2_x = c1_x + c1_w + 40
    c2_w = 260
    svg.append(f'''
  <!-- Block 2: Build & Dual Oracle -->
  <rect x="{c2_x}" y="{top_y}" width="{c2_w}" height="{box_h}" rx="8" fill="#ECFEFF" stroke="#BAE6FD" stroke-width="1.5"/>
  <text x="{c2_x + c2_w/2}" y="{top_y + 26}" fill="#0369A1" font-size="13" font-weight="700" text-anchor="middle">2. Build &amp; Dual Oracle Adjudication</text>

  <!-- Rebuilt Compiler -->
  <g transform="translate({c2_x + 14}, {top_y + 42})">
    <rect x="0" y="0" width="{c2_w - 28}" height="110" rx="6" fill="#FFFFFF" stroke="#7DD3FC" stroke-width="1.2"/>
    <text x="12" y="22" fill="#0284C7" font-size="11.5" font-weight="700">Instrumented Compiler IC</text>
    <rect x="10" y="32" width="{c2_w - 48}" height="32" rx="4" fill="#E0F2FE" stroke="#38BDF8" stroke-width="1.2"/>
    <text x="{c2_w/2 - 14}" y="52" fill="#0369A1" font-size="11" font-weight="800" text-anchor="middle">GCC_INST / CLANG_INST</text>
    
    <text x="12" y="82" fill="#475569" font-size="9.5">&#x2022; Compiles seeds with defense flags</text>
    <text x="12" y="96" fill="#0284C7" font-size="9.5" font-weight="600">&#8669; Emits UID Trace Stream</text>
  </g>

  <!-- Down Arrow inside Block 2 -->
  <line x1="{c2_x + c2_w/2}" y1="{top_y + 158}" x2="{c2_x + c2_w/2}" y2="{top_y + 178}" 
        stroke="#0284C7" stroke-width="2" marker-end="url(#arr5-cyan)"/>
  <text x="{c2_x + c2_w/2 + 32}" y="{top_y + 171}" fill="#0284C7" font-size="8.5" font-weight="600">Binary + Trace</text>

  <!-- Dual Oracle Box -->
  <g transform="translate({c2_x + 14}, {top_y + 182})">
    <rect x="0" y="0" width="{c2_w - 28}" height="168" rx="6" fill="#FFFFFF" stroke="#7DD3FC" stroke-width="1.2"/>
    <text x="12" y="22" fill="#0284C7" font-size="11.5" font-weight="700">Dual Deterministic Oracle</text>

    <rect x="10" y="32" width="{c2_w - 48}" height="42" rx="4" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1"/>
    <text x="16" y="48" fill="#0F766E" font-size="10" font-weight="700">Static Inspection</text>
    <text x="16" y="64" fill="#475569" font-size="9">Disassembly &amp; DWARF offset check</text>

    <rect x="10" y="82" width="{c2_w - 48}" height="42" rx="4" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1"/>
    <text x="16" y="98" fill="#0F766E" font-size="10" font-weight="700">Dynamic Probe</text>
    <text x="16" y="114" fill="#475569" font-size="9">Runtime execution &amp; trap observation</text>

    <text x="12" y="148" fill="#0F766E" font-size="9.5" font-style="italic">Evaluates against Invariant &#966;i</text>
  </g>
''')

    # Arrow 2 -> 3
    arr2_x = c2_x + c2_w + 4
    svg.append(f'''
  <line x1="{arr2_x}" y1="{top_y + 245}" x2="{arr2_x + 36}" y2="{top_y + 245}" 
        stroke="#475569" stroke-width="2.5" marker-end="url(#arr5-gray)"/>
  <text x="{arr2_x + 18}" y="{top_y + 237}" fill="#475569" font-size="9" font-weight="600" text-anchor="middle">Verdict</text>
''')

    # 3. Right Container: Verdict Dispatch & Closed Loops (Width: 430)
    c3_x = c2_x + c2_w + 44
    c3_w = 430

    svg.append(f'''
  <!-- Block 3: Verdict Dispatch & Loops -->
  <rect x="{c3_x}" y="{top_y}" width="{c3_w}" height="{box_h}" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  <text x="{c3_x + c3_w/2}" y="{top_y + 26}" fill="#1E293B" font-size="13" font-weight="700" text-anchor="middle">3. Verdict Dispatch &amp; Closed Loops</text>

  <!-- Decision Diamond -->
  <g transform="translate({c3_x + 40}, {top_y + 245})">
    <polygon points="0,-24 45,0 0,24 -45,0" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
    <text x="0" y="-3" fill="#0F172A" font-size="9.5" font-weight="700" text-anchor="middle">Invariant</text>
    <text x="0" y="9" fill="#0F172A" font-size="9.5" font-weight="700" text-anchor="middle">Violated?</text>
  </g>
''')

    # Path [NO] (PASS / N/A / ERROR) -> Up to Feedback Agent
    dia_x = c3_x + 40
    dia_y = top_y + 245
    fb_x = c3_x + 125
    fb_y = top_y + 45
    fb_w = 285

    svg.append(f'''
  <!-- Path [NO] -->
  <path d="M {dia_x} {dia_y - 24} L {dia_x} {fb_y + 45} L {fb_x - 8} {fb_y + 45}" 
        fill="none" stroke="#64748B" stroke-width="2" marker-end="url(#arr5-gray)"/>
  <text x="{dia_x + 6}" y="{dia_y - 35}" fill="#64748B" font-size="9.5" font-weight="700">NO (PASS/NA)</text>

  <!-- Feedback Agent Box -->
  <g transform="translate({fb_x}, {fb_y})">
    <rect x="0" y="0" width="{fb_w}" height="105" rx="6" fill="#FFFFFF" stroke="#8B5CF6" stroke-width="1.5"/>
    <rect x="10" y="8" width="120" height="20" rx="3" fill="#EDE9FE"/>
    <text x="16" y="22" fill="#5B21B6" font-size="10.5" font-weight="700">Feedback Agent</text>
    
    <text x="12" y="44" fill="#334155" font-size="9.5">&#x2022; Ingests compiler warnings &amp; diagnostics</text>
    <text x="12" y="58" fill="#334155" font-size="9.5">&#x2022; Analyzes UID hit traces: hit_count(UID)</text>
    
    <rect x="10" y="70" width="{fb_w - 20}" height="26" rx="3" fill="#F5F3FF"/>
    <text x="16" y="87" fill="#6D28D9" font-size="9.5" font-weight="600">Drives Seed Mutation Hints &amp; Oracle Evolution</text>
  </g>
''')

    # Path [YES] (FAIL) -> Down to Confirmed Bug & C-Reduce
    bug_x = c3_x + 125
    bug_y = top_y + 190
    bug_w = 285

    svg.append(f'''
  <!-- Path [YES] -->
  <path d="M {dia_x} {dia_y + 24} L {dia_x} {bug_y + 45} L {bug_x - 8} {bug_y + 45}" 
        fill="none" stroke="#DC2626" stroke-width="2.5" marker-end="url(#arr5-red)"/>
  <text x="{dia_x + 6}" y="{dia_y + 42}" fill="#DC2626" font-size="10" font-weight="700">YES: FAIL</text>

  <!-- Confirmed Bug Box -->
  <g transform="translate({bug_x}, {bug_y})">
    <rect x="0" y="0" width="{bug_w}" height="160" rx="6" fill="#FFFFFF" stroke="#EF4444" stroke-width="1.5"/>
    
    <!-- Red Alert Header -->
    <rect x="10" y="8" width="{bug_w - 20}" height="26" rx="4" fill="#FEE2E2" stroke="#DC2626" stroke-width="1"/>
    <text x="{bug_w/2}" y="25" fill="#991B1B" font-size="11" font-weight="800" text-anchor="middle">&#9888; CONFIRMED SILENT DEFENSE BUG</text>

    <text x="14" y="50" fill="#334155" font-size="9.5">&#x2022; Deterministic binary / runtime proof established</text>

    <!-- C-Reduce -->
    <rect x="10" y="60" width="{bug_w - 20}" height="38" rx="4" fill="#FEF2F2" stroke="#F87171" stroke-width="1"/>
    <text x="16" y="76" fill="#B91C1C" font-size="10" font-weight="700">Automated C-Reduce Minimizer</text>
    <text x="16" y="90" fill="#7F1D1D" font-size="8.5">Delta-debugging produces minimal Zero-Day PoC</text>

    <!-- Feedback to Corpus -->
    <rect x="10" y="108" width="{bug_w - 20}" height="42" rx="4" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
    <text x="16" y="125" fill="#334155" font-size="9.5" font-weight="700">&#8635; Lateral Exploration Loop</text>
    <text x="16" y="140" fill="#64748B" font-size="8.5">Mutate boundary types, structs &amp; alignments for &#966;i</text>
  </g>
''')

    # Feedback Loop Arrows
    # 1. Purple: Guidance Loop (from Feedback Agent back to Generator Agent)
    svg.append(f'''
  <!-- Guidance Loop (Top) -->
  <path d="M {fb_x + fb_w/2} {top_y} 
           C {fb_x + fb_w/2} {top_y - 30}, {c1_x + c1_w/2} {top_y - 30}, {c1_x + c1_w/2} {top_y}"
        fill="none" stroke="#7C3AED" stroke-width="2" stroke-dasharray="6,4" marker-end="url(#arr5-purple)"/>
  <rect x="{width/2 - 130}" y="{top_y - 42}" width="260" height="24" rx="4" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1"/>
  <text x="{width/2}" y="{top_y - 26}" fill="#6D28D9" font-size="10" font-weight="700" text-anchor="middle">Guidance Loop: Mutation Hints &#8594; Generator</text>
''')

    # 2. Red: Checker Rewrite Loop (from Feedback Agent to Dual Oracle)
    svg.append(f'''
  <!-- Checker Rewrite Loop (Middle) -->
  <path d="M {fb_x + 30} {fb_y + 105} 
           C {fb_x + 30} {fb_y + 130}, {c2_x + c2_w - 20} {fb_y + 130}, {c2_x + c2_w - 20} {top_y + 182}"
        fill="none" stroke="#DC2626" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arr5-red)"/>
  <rect x="{c2_x + c2_w - 110}" y="{fb_y + 118}" width="180" height="22" rx="3" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
  <text x="{c2_x + c2_w - 20}" y="{fb_y + 133}" fill="#991B1B" font-size="9" font-weight="700" text-anchor="middle">Checker Rewrite (Votes &#8805; &#964;)</text>
''')

    # 3. Cyan: Lateral Exploration Loop (from Bug Box back to Generator Agent)
    svg.append(f'''
  <!-- Lateral Exploration Loop (Bottom) -->
  <path d="M {bug_x + bug_w/2} {top_y + box_h} 
           C {bug_x + bug_w/2} {top_y + box_h + 46}, {c1_x + c1_w/2} {top_y + box_h + 46}, {c1_x + c1_w/2} {top_y + box_h}"
        fill="none" stroke="#0284C7" stroke-width="2.2" stroke-dasharray="6,4" marker-end="url(#arr5-cyan)"/>
  <rect x="{width/2 - 160}" y="{top_y + box_h + 32}" width="320" height="26" rx="4" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1"/>
  <text x="{width/2}" y="{top_y + box_h + 49}" fill="#0369A1" font-size="10.5" font-weight="700" text-anchor="middle">&#8635; Lateral Exploration Loop (Bug Amplification Mechanism)</text>
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
    create_fig5_svg()
