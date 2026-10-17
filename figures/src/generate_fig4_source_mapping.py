#!/usr/bin/env python3
"""
Generate a clean, streamlined, publication-grade vector diagram for Figure 4:
Hierarchical Source Mapping and Log Instrumentation Pipeline (Stage 3).
Produces SVG, PDF, and high-res PNG.
"""

import os
import subprocess

def create_fig4_svg(output_base="figures/method-source-mapping"):
    width = 1000
    height = 470

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    svg.append('''
  <defs>
    <marker id="arr4-gray" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#475569"/>
    </marker>
    <marker id="arr4-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#D97706"/>
    </marker>
  </defs>
''')

    # Title
    svg.append(f'''
  <text x="{width/2}" y="36" fill="#0F172A" font-size="18" font-weight="700" text-anchor="middle">Stage 3: Hierarchical Source Mapping and Log Instrumentation Pipeline</text>
''')

    top_y = 60
    card_h = 345

    # 1. Left Card: Autonomous MCP Navigation (Width: 280)
    c1_x = 35
    c1_w = 280
    svg.append(f'''
  <!-- Card 1: Autonomous Agent Navigation -->
  <rect x="{c1_x}" y="{top_y}" width="{c1_w}" height="{card_h}" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1.5"/>
  <text x="{c1_x + c1_w/2}" y="{top_y + 28}" fill="#3730A3" font-size="13.5" font-weight="700" text-anchor="middle">1. Autonomous MCP Agent Navigation</text>

  <!-- Agent Box -->
  <g transform="translate({c1_x + 14}, {top_y + 45})">
    <rect x="0" y="0" width="{c1_w - 28}" height="100" rx="6" fill="#FFFFFF" stroke="#A5B4FC" stroke-width="1.2"/>
    <text x="12" y="24" fill="#312E81" font-size="12" font-weight="700">Autonomous Coding Agent</text>
    <text x="12" y="44" fill="#475569" font-size="10">&#x2022; Navigates millions of lines of compiler C++</text>
    <text x="12" y="62" fill="#475569" font-size="10">&#x2022; Discovers defense pass implementations</text>
    <text x="12" y="80" fill="#4F46E5" font-size="9.5" font-style="italic">Driven by invariant precondition semantics</text>
  </g>

  <!-- MCP Tools Box -->
  <g transform="translate({c1_x + 14}, {top_y + 160})">
    <rect x="0" y="0" width="{c1_w - 28}" height="160" rx="6" fill="#FFFFFF" stroke="#A5B4FC" stroke-width="1.2"/>
    <text x="12" y="22" fill="#312E81" font-size="11.5" font-weight="700">Model Context Protocol (MCP) Tools</text>

    <rect x="12" y="32" width="{c1_w - 52}" height="28" rx="4" fill="#E0E7FF"/>
    <text x="20" y="50" fill="#1E1B4B" font-size="10"><tspan font-weight="700">CallGraph MCP:</tspan> Inter-procedural trace</text>

    <rect x="12" y="66" width="{c1_w - 52}" height="28" rx="4" fill="#E0E7FF"/>
    <text x="20" y="84" fill="#1E1B4B" font-size="10"><tspan font-weight="700">AST Parser:</tspan> Struct &amp; condition inspection</text>

    <rect x="12" y="100" width="{c1_w - 52}" height="28" rx="4" fill="#E0E7FF"/>
    <text x="20" y="118" fill="#1E1B4B" font-size="10"><tspan font-weight="700">Code Search:</tspan> Cross-file macro resolution</text>

    <text x="12" y="146" fill="#64748B" font-size="9">Autonomous multi-step exploration</text>
  </g>
''')

    # Arrow 1 -> 2
    arr1_x = c1_x + c1_w + 5
    svg.append(f'''
  <line x1="{arr1_x}" y1="{top_y + card_h/2}" x2="{arr1_x + 30}" y2="{top_y + card_h/2}" 
        stroke="#475569" stroke-width="2.5" marker-end="url(#arr4-gray)"/>
''')

    # 2. Middle Card: 3-Level Hierarchical Mapping (Width: 320)
    c2_x = c1_x + c1_w + 40
    c2_w = 320
    svg.append(f'''
  <!-- Card 2: 3-Level Hierarchical Mapping -->
  <rect x="{c2_x}" y="{top_y}" width="{c2_w}" height="{card_h}" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
  <text x="{c2_x + c2_w/2}" y="{top_y + 28}" fill="#92400E" font-size="13.5" font-weight="700" text-anchor="middle">2. 3-Level Hierarchical Mapping</text>

  <!-- Level 1: Pass -->
  <g transform="translate({c2_x + 16}, {top_y + 45})">
    <rect x="0" y="0" width="{c2_w - 32}" height="68" rx="6" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1.2"/>
    <rect x="10" y="10" width="130" height="20" rx="3" fill="#FEF3C7"/>
    <text x="16" y="24" fill="#92400E" font-size="10.5" font-weight="700">Level 1: Compiler Pass</text>
    <text x="12" y="48" fill="#1E293B" font-size="11" font-weight="600" font-family="monospace">pass_stack_protect / StackProtectorPass</text>
  </g>

  <!-- Down Arrow 1 -> 2 -->
  <line x1="{c2_x + c2_w/2}" y1="{top_y + 115}" x2="{c2_x + c2_w/2}" y2="{top_y + 133}" 
        stroke="#D97706" stroke-width="2" marker-end="url(#arr4-down)"/>

  <!-- Level 2: Functions -->
  <g transform="translate({c2_x + 16}, {top_y + 138})">
    <rect x="0" y="0" width="{c2_w - 32}" height="68" rx="6" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1.2"/>
    <rect x="10" y="10" width="145" height="20" rx="3" fill="#FEF3C7"/>
    <text x="16" y="24" fill="#92400E" font-size="10.5" font-weight="700">Level 2: Target Functions</text>
    <text x="12" y="48" fill="#1E293B" font-size="11" font-weight="600" font-family="monospace">expand_used_vars() / LayoutStackNodes()</text>
  </g>

  <!-- Down Arrow 2 -> 3 -->
  <line x1="{c2_x + c2_w/2}" y1="{top_y + 208}" x2="{c2_x + c2_w/2}" y2="{top_y + 226}" 
        stroke="#D97706" stroke-width="2" marker-end="url(#arr4-down)"/>

  <!-- Level 3: Conditions -->
  <g transform="translate({c2_x + 16}, {top_y + 231})">
    <rect x="0" y="0" width="{c2_w - 32}" height="88" rx="6" fill="#FFFFFF" stroke="#F59E0B" stroke-width="1.2"/>
    <rect x="10" y="10" width="165" height="20" rx="3" fill="#FEF3C7"/>
    <text x="16" y="24" fill="#92400E" font-size="10.5" font-weight="700">Level 3: Critical Conditions</text>
    <text x="12" y="48" fill="#B45309" font-size="10.5" font-weight="600" font-family="monospace">has_vla, stack_protect_decl, canary_loc</text>
    <text x="12" y="70" fill="#64748B" font-size="9.5">Pinpoints decision branches &amp; stack offset calculations</text>
  </g>
''')

    # Arrow 2 -> 3
    arr2_x = c2_x + c2_w + 5
    svg.append(f'''
  <line x1="{arr2_x}" y1="{top_y + card_h/2}" x2="{arr2_x + 30}" y2="{top_y + card_h/2}" 
        stroke="#475569" stroke-width="2.5" marker-end="url(#arr4-gray)"/>
''')

    # 3. Right Card: Log Probing & Driver Rebuild (Width: 280)
    c3_x = c2_x + c2_w + 40
    c3_w = 280
    svg.append(f'''
  <!-- Card 3: Probing & Compiler Rebuild -->
  <rect x="{c3_x}" y="{top_y}" width="{c3_w}" height="{card_h}" rx="8" fill="#FFF7ED" stroke="#FED7AA" stroke-width="1.5"/>
  <text x="{c3_x + c3_w/2}" y="{top_y + 28}" fill="#9A3412" font-size="13.5" font-weight="700" text-anchor="middle">3. Probing &amp; Rebuild (GCC_INST)</text>

  <!-- Probe Injection Box -->
  <g transform="translate({c3_x + 14}, {top_y + 45})">
    <rect x="0" y="0" width="{c3_w - 28}" height="100" rx="6" fill="#FFFFFF" stroke="#FB923C" stroke-width="1.2"/>
    <text x="12" y="22" fill="#C2410C" font-size="11.5" font-weight="700">Lightweight UID Log Probes</text>
    
    <rect x="12" y="32" width="{c3_w - 52}" height="32" rx="4" fill="#FFEDD5" stroke="#FDBA74" stroke-width="1"/>
    <text x="20" y="52" fill="#9A3412" font-size="10.5" font-weight="700" font-family="monospace">DEFUZZ_LOG("SP#a3f2:hit", slot)</text>

    <text x="12" y="80" fill="#475569" font-size="9.5">&#x2022; Zero runtime overhead in target binary</text>
    <text x="12" y="94" fill="#475569" font-size="9.5">&#x2022; Uniquely tracks internal defense paths</text>
  </g>

  <!-- Rebuilt Compiler Driver Box -->
  <g transform="translate({c3_x + 14}, {top_y + 160})">
    <rect x="0" y="0" width="{c3_w - 28}" height="160" rx="6" fill="#FFFFFF" stroke="#FB923C" stroke-width="1.2"/>
    <text x="12" y="22" fill="#C2410C" font-size="11.5" font-weight="700">Rebuilt Compiler Driver</text>

    <rect x="12" y="34" width="{c3_w - 52}" height="42" rx="4" fill="#FFEDD5" stroke="#F97316" stroke-width="1.5"/>
    <text x="{c3_w/2 - 14}" y="52" fill="#7C2D12" font-size="12" font-weight="800" text-anchor="middle">GCC_INST / CLANG_INST</text>
    <text x="{c3_w/2 - 14}" y="67" fill="#9A3412" font-size="9" text-anchor="middle">Standalone, independently executable binary</text>

    <g transform="translate(12, 86)">
      <rect x="0" y="0" width="{c3_w - 52}" height="32" rx="4" fill="#FFF7ED"/>
      <text x="8" y="20" fill="#C2410C" font-size="10" font-weight="700">&#8669; UID Trace Stream</text>
    </g>

    <text x="12" y="136" fill="#475569" font-size="9.5">&#x2022; Emits deterministic execution logs</text>
    <text x="12" y="150" fill="#475569" font-size="9.5">&#x2022; Feeds condition hit counts to Feedback Agent</text>
  </g>
''')

    # Bottom summary
    svg.append(f'''
  <text x="{width/2}" y="{top_y + card_h + 26}" fill="#64748B" font-size="11" font-weight="500" text-anchor="middle">
    Autonomous MCP tools locate critical defense conditions, insert UID probes, and produce the independently executable driver GCC_INST.
  </text>
''')

    svg.append('</svg>')

    os.makedirs(os.path.dirname(output_base), exist_ok=True)
    svg_path = f"{output_base}.svg"
    pdf_path = f"{output_base}.pdf"
    png_path = f"{output_base}.png"

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {svg_path}")

    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, svg_path], check=True)
    print(f"Compiled to {pdf_path}")

    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-d", "300", "-p", "300", "-o", png_path, svg_path], check=True)
    print(f"Compiled to {png_path}")

if __name__ == "__main__":
    create_fig4_svg()
