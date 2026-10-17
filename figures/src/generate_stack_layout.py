#!/usr/bin/env python3
"""
Generate a clean, elegant, top-tier academic memory layout diagram for Figure 1:
CVE-2023-4039 Buggy AArch64 Stack Frame Layout.
Produces SVG and converts to vector PDF via rsvg-convert.
"""

import os
import subprocess

def create_stack_layout_svg(output_path="figures/stack-layout.svg"):
    width = 620
    height = 430

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    svg.append('''
  <defs>
    <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#64748B"/>
    </marker>
    <marker id="arrow-red-up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>
  </defs>
''')

    # Memory Address Axis (Left)
    axis_x = 42
    svg.append(f'''
  <!-- Memory Address Axis -->
  <line x1="{axis_x}" y1="52" x2="{axis_x}" y2="378" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="{axis_x}" y1="370" x2="{axis_x}" y2="384" stroke="#64748B" stroke-width="2" marker-end="url(#arrow-down)"/>
  <text x="{axis_x}" y="36" fill="#64748B" font-size="11" font-weight="600" text-anchor="middle">High Address</text>
  <text x="{axis_x}" y="408" fill="#64748B" font-size="11" font-weight="600" text-anchor="middle">Low Address</text>
  <text x="{axis_x - 12}" y="215" fill="#64748B" font-size="10" font-weight="500" text-anchor="middle" transform="rotate(-90 {axis_x - 12} 215)">Stack Grows Down</text>
''')

    # Stack Slots (Center Column)
    box_x = 88
    box_w = 232
    h_slot = 44
    gap = 6
    start_y = 52

    slots = [
        {"name": "Incoming Stack Arguments", "sub": "Caller frame arguments", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155"},
        {"name": "Stack Canary", "sub": "Checked at function epilogue", "bg": "#FEF3C7", "border": "#F59E0B", "txt": "#92400E"},
        {"name": "Local Variables &amp; Spills", "sub": "Static arrays &amp; scalars", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155"},
        {"name": "Saved Return Address (LR')", "sub": "Target of control-flow hijack", "bg": "#FEE2E2", "border": "#EF4444", "txt": "#991B1B"},
        {"name": "Callee-Saved Regs (FP', SVE)", "sub": "Frame pointer &amp; vector regs", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155"},
        {"name": "VLA / Dynamic Buffer", "sub": "Allocated below saved registers", "bg": "#FFEDD5", "border": "#F97316", "txt": "#9A3412"},
        {"name": "Outgoing Stack Arguments", "sub": "Space reserved for callees", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155"}
    ]

    for i, s in enumerate(slots):
        y = start_y + i * (h_slot + gap)
        svg.append(f'''
  <g id="slot-{i}">
    <rect x="{box_x}" y="{y}" width="{box_w}" height="{h_slot}" rx="4" fill="{s['bg']}" stroke="{s['border']}" stroke-width="1.5"/>
    <text x="{box_x + 14}" y="{y + 20}" fill="{s['txt']}" font-size="12" font-weight="600">{s['name']}</text>
    <text x="{box_x + 14}" y="{y + 35}" fill="#64748B" font-size="10">{s['sub']}</text>
  </g>''')

    # Annotations on the Right
    vla_y = start_y + 5 * (h_slot + gap) + 22
    lr_y = start_y + 3 * (h_slot + gap) + 22
    canary_y = start_y + 1 * (h_slot + gap) + 22

    arrow_x1 = box_x + box_w + 12
    arc_x = arrow_x1 + 32

    # 1. Overflow Trajectory
    svg.append(f'''
  <!-- Overflow trajectory from VLA up to Saved LR' -->
  <path d="M {arrow_x1} {vla_y} C {arc_x} {vla_y}, {arc_x} {lr_y}, {arrow_x1 + 6} {lr_y}" 
        fill="none" stroke="#DC2626" stroke-width="2.5" stroke-dasharray="5,3" marker-end="url(#arrow-red-up)"/>
  
  <text x="{arc_x + 16}" y="{vla_y - 18}" fill="#DC2626" font-size="11.5" font-weight="700">1. Buffer Overflow</text>
  <text x="{arc_x + 16}" y="{vla_y - 4}" fill="#991B1B" font-size="10">Grows toward higher addresses</text>
  <text x="{arc_x + 16}" y="{lr_y + 4}" fill="#DC2626" font-size="11.5" font-weight="700">Corrupts LR' directly!</text>
''')

    # 2. Canary bypassed indicator
    svg.append(f'''
  <!-- Canary untouched indicator -->
  <line x1="{box_x + box_w + 12}" y1="{canary_y}" x2="{arc_x + 14}" y2="{canary_y}" stroke="#D97706" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="{arc_x + 16}" y="{canary_y - 15}" width="200" height="30" rx="4" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1"/>
  <text x="{arc_x + 28}" y="{canary_y + 4}" fill="#92400E" font-size="10.5" font-weight="600">2. Canary Sits Above (Intact)</text>
''')

    # 3. Silent Failure Verdict Banner at Bottom Right
    svg.append(f'''
  <!-- Silent Failure Verdict Box -->
  <g transform="translate({arc_x + 16}, 336)">
    <rect x="0" y="0" width="200" height="56" rx="5" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
    <text x="12" y="20" fill="#991B1B" font-size="11.5" font-weight="700">&#9888; Silent Defense Failure</text>
    <text x="12" y="36" fill="#64748B" font-size="9.5">&#x2022; LR' hijacked without crash</text>
    <text x="12" y="48" fill="#64748B" font-size="9.5">&#x2022; Epilogue canary check PASSES</text>
  </g>
''')

    svg.append('</svg>')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

    # Compile to PDF
    pdf_path = output_path.replace(".svg", ".pdf")
    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, output_path], check=True)
    print(f"Compiled to {pdf_path}")

if __name__ == "__main__":
    create_stack_layout_svg()
