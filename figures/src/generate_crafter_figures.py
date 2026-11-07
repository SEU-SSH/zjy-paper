#!/usr/bin/env python3
"""
Generate publication-grade academic vector figures using Crafter principles:
1. figures/defense-matrix.svg & figures/defense-matrix.pdf
2. figures/stack-layout.svg & figures/stack-layout.pdf
"""

import os
import subprocess

def create_defense_matrix_svg(output_path="figures/defense-matrix.svg"):
    # Target single column: compact 5 ISAs (rows) x 9 single Defense Mechanisms (columns)
    w = 520
    h = 232
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')
    
    # Fill colors (DeFuzz status: Confirmed / Reported / None)
    C_REP  = "#E3F1E7"   # Reported (light green fill)
    C_CONF = "#228833"   # Confirmed (dark green fill)
    C_NONE = "#FFFFFF"   # Empty (white fill)
    
    # Border color for Historical bugs (orthogonal soft coral-red frame, keeps interior fill intact)
    B_HIST = "#E57373"   # Soft muted red border for cells with prior historical bugs
    
    # Horizontal: 9 Single Defense Mechanisms (each column is strictly one mechanism)
    cols = [
        ("Stack", "Canary"),
        ("FORTIFY", "SOURCE"),
        ("Stack", "Clash"),
        ("IBT", ""),
        ("Shadow", "Stack"),
        ("PAC", ""),
        ("Zero-", "Regs"),
        ("ASan", ""),
        ("Safe-", "Stack"),
    ]
    
    # Vertical: ISAs (5 rows) -> each cell is (fill_color, has_historical_red_border)
    # Updated to match the 2026-11-06 bug ledger (126 discovered, 34 confirmed / 11 fixed)
    rows = [
        ("x86-64", [
            (C_CONF, False), # Stack Canary: DF-L-007, DF-L-036 (confirmed)
            (C_CONF, True),  # FORTIFY_SOURCE: DF-G-002 (fixed), DF-G-013 (confirmed) + Hist (PR 101836)
            (C_REP,  True),  # Stack Clash: DF-G-014 (reported) + Hist (CVE-2017-1000364)
            (C_CONF, True),  # IBT: DF-G-004 (confirmed), DF-G-043 (fixed), DF-L-001 (fixed) + Hist (#44527)
            (C_CONF, True),  # Shadow Stack: DF-G-025 (fixed), DF-G-050 (fixed), DF-L-029 (confirmed) + Hist
            (C_NONE, False), # PAC: N/A on x86-64
            (C_CONF, True),  # Zero-Regs: DF-G-041, DF-L-009, DF-L-010 (confirmed) + Hist (PR 104666)
            (C_REP,  False), # ASan: DF-L-011, DF-L-016, DF-L-017, DF-L-027, DF-L-028, DF-L-030 (reported)
            (C_REP,  False), # SafeStack: DF-L-012, DF-L-033 (reported)
        ]),
        ("AArch64", [
            (C_CONF, True),  # Stack Canary: DF-L-007, DF-L-036 (confirmed) + Hist (CVE-2023-4039, PR 96191)
            (C_CONF, False), # FORTIFY_SOURCE: DF-G-002 (fixed), DF-G-013 (confirmed)
            (C_REP,  True),  # Stack Clash: DF-L-031 (reported) + Hist (PR 91458)
            (C_NONE, False), # IBT: x86/RISC-V specific
            (C_REP,  False), # Shadow Stack: DF-G-027, DF-G-031 (reported)
            (C_CONF, True),  # PAC: DF-G-028, DF-L-034, DF-L-035 (confirmed) + Hist (PR 93423 / PR 111703)
            (C_CONF, False), # Zero-Regs: DF-G-041, DF-L-009, DF-L-010 (confirmed)
            (C_REP,  False), # ASan: DF-G-022, DF-L-011, DF-L-016, DF-L-017, DF-L-027, DF-L-030 (reported)
            (C_CONF, False), # SafeStack: DF-L-026 (confirmed), DF-L-012, DF-L-033 (reported)
        ]),
        ("RISC-V", [
            (C_CONF, False), # Stack Canary: DF-L-036 (confirmed), DF-G-030, DF-L-018 (reported)
            (C_CONF, False), # FORTIFY_SOURCE: DF-G-002 (fixed), DF-G-013 (confirmed)
            (C_CONF, False), # Stack Clash: DF-G-010 (fixed), DF-G-016 (reported)
            (C_REP,  False), # IBT: DF-G-019 (reported)
            (C_CONF, False), # Shadow Stack: DF-G-020, DF-G-029 (confirmed), DF-G-018 (reported)
            (C_NONE, False), # PAC: N/A on RISC-V
            (C_REP,  False), # Zero-Regs: DF-G-063 (ready)
            (C_REP,  False), # ASan: DF-G-022, DF-L-016 (reported)
            (C_NONE, False), # SafeStack: N/A on RISC-V
        ]),
        ("LoongArch", [
            (C_CONF, False), # Stack Canary: DF-G-001 / PR 125049 (fixed)
            (C_CONF, False), # FORTIFY_SOURCE: DF-G-002 (fixed), DF-G-013 (confirmed)
            (C_CONF, False), # Stack Clash: DF-G-015 / PR 128036 (confirmed)
            (C_NONE, False), # IBT
            (C_NONE, False), # Shadow Stack
            (C_NONE, False), # PAC
            (C_REP,  False), # Zero-Regs: generic LTO / middle-end
            (C_REP,  False), # ASan: DF-G-022 (reported)
            (C_NONE, False), # SafeStack
        ]),
        ("MIPS", [
            (C_REP,  False), # Stack Canary: DF-G-001 / PR 125077 (reported)
            (C_CONF, False), # FORTIFY_SOURCE: DF-G-002 (fixed), DF-G-013 (confirmed)
            (C_NONE, False), # Stack Clash
            (C_NONE, False), # IBT
            (C_NONE, False), # Shadow Stack
            (C_NONE, False), # PAC
            (C_REP,  False), # Zero-Regs: generic LTO / middle-end
            (C_REP,  False), # ASan: generic middle-end
            (C_NONE, False), # SafeStack
        ]),
    ]
    
    start_x = 74
    col_w = 44
    gap_x = 5
    
    start_y = 14
    row_h = 26
    gap_y = 5
    
    # Draw Column Headers (1 or 2 lines centered cleanly)
    for j, (line1, line2) in enumerate(cols):
        cx = start_x + j * (col_w + gap_x) + col_w / 2
        if line2:
            svg.append(f'<text x="{cx}" y="{start_y + 8}" fill="#374151" font-size="8.8" font-weight="600" text-anchor="middle">{line1}</text>')
            svg.append(f'<text x="{cx}" y="{start_y + 19}" fill="#374151" font-size="8.8" font-weight="600" text-anchor="middle">{line2}</text>')
        else:
            svg.append(f'<text x="{cx}" y="{start_y + 14}" fill="#374151" font-size="9.0" font-weight="600" text-anchor="middle">{line1}</text>')
            
    # Draw Matrix Rows (ISAs)
    y = start_y + 27
    for row_name, cells in rows:
        # Row Label (ISA)
        svg.append(f'<text x="{start_x - 8}" y="{y + row_h/2 + 4}" fill="#1F2937" font-size="10.0" font-weight="600" text-anchor="end">{row_name}</text>')
        
        # Cells
        for j, (fill_color, is_hist) in enumerate(cells):
            cx = start_x + j * (col_w + gap_x)
            if is_hist:
                border_color, stroke_w = B_HIST, "1.35"
            elif fill_color == C_CONF:
                border_color, stroke_w = "#15803D", "1.0"
            elif fill_color == C_REP:
                border_color, stroke_w = "#86EFAC", "1.0"
            else:
                border_color, stroke_w = "#E5E7EB", "1.0"
            svg.append(f'<rect x="{cx}" y="{y}" width="{col_w}" height="{row_h}" rx="4" fill="{fill_color}" stroke="{border_color}" stroke-width="{stroke_w}"/>')
            
        y += row_h + gap_y

    # Legend at Bottom: Historical is shown with hollow interior + soft red border
    legend_y = y + 10
    legend_items = [
        ("Historical", "#FFFFFF", B_HIST,    "1.35", "#C53030"),
        ("Reported",   C_REP,     "#86EFAC", "1.0",  "#166534"),
        ("Confirmed",  C_CONF,    "#15803D", "1.0",  "#FFFFFF"),
    ]
    
    badge_w = 106
    badge_h = 22
    badge_gap = 18
    total_leg_w = len(legend_items) * badge_w + (len(legend_items) - 1) * badge_gap
    leg_start_x = start_x + (len(cols) * (col_w + gap_x) - gap_x - total_leg_w) / 2
    
    for k, (label, bg, border, sw, txt) in enumerate(legend_items):
        bx = leg_start_x + k * (badge_w + badge_gap)
        svg.append(f'<rect x="{bx}" y="{legend_y}" width="{badge_w}" height="{badge_h}" rx="4" fill="{bg}" stroke="{border}" stroke-width="{sw}"/>')
        svg.append(f'<text x="{bx + badge_w/2}" y="{legend_y + 15}" fill="{txt}" font-size="10" font-weight="600" text-anchor="middle">{label}</text>')
        
    svg.append('</svg>')
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")
    
    pdf_path = output_path.replace(".svg", ".pdf")
    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, output_path], check=True)
    print(f"Compiled to {pdf_path}")

def create_stack_layout_svg(output_path="figures/stack-layout.svg"):
    # Target single column: width 500, height 360
    w = 500
    h = 360
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')
    
    svg.append('''
  <defs>
    <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#64748B"/>
    </marker>
    <marker id="arrow-red-up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#CC3311"/>
    </marker>
    <filter id="subtle-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.06"/>
    </filter>
  </defs>
''')
    
    # Left Axis: Memory Direction
    axis_x = 32
    top_y = 28
    bot_y = 330
    svg.append(f'''
  <!-- Memory Address Axis -->
  <line x1="{axis_x}" y1="{top_y + 18}" x2="{axis_x}" y2="{bot_y - 18}" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="{axis_x}" y1="{bot_y - 24}" x2="{axis_x}" y2="{bot_y - 10}" stroke="#64748B" stroke-width="2" marker-end="url(#arrow-down)"/>
  <text x="{axis_x}" y="{top_y + 8}" fill="#64748B" font-size="10" font-weight="600" text-anchor="middle">High Addr</text>
  <text x="{axis_x}" y="{bot_y + 12}" fill="#64748B" font-size="10" font-weight="600" text-anchor="middle">Low Addr</text>
  <text x="{axis_x - 10}" y="180" fill="#64748B" font-size="9.5" font-weight="500" text-anchor="middle" transform="rotate(-90 {axis_x - 10} 180)">Stack Grows Down</text>
''')

    # Middle Slots
    box_x = 76
    box_w = 210
    h_slot = 38
    gap = 6
    start_y = 34
    
    slots = [
        {"name": "Incoming Arguments", "sub": "Caller frame arguments", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155", "sub_txt": "#64748B", "w": 1.2},
        {"name": "Stack Canary", "sub": "Verified at function epilogue", "bg": "#FFF8E1", "border": "#F59E0B", "txt": "#7D4E00", "sub_txt": "#92400E", "w": 2.2},
        {"name": "Local Variables &amp; Spills", "sub": "Frame-relative scalar / arrays", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155", "sub_txt": "#64748B", "w": 1.2},
        {"name": "Saved Return Address (LR')", "sub": "Target of control-flow hijack", "bg": "#F4DFD8", "border": "#CC3311", "txt": "#7F2615", "sub_txt": "#991B1B", "w": 2.4},
        {"name": "Callee-Saved Regs (FP', SVE)", "sub": "Frame pointer &amp; vector context", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155", "sub_txt": "#64748B", "w": 1.2},
        {"name": "VLA / Dynamic Buffer", "sub": "Allocated below saved registers", "bg": "#E3F1E7", "border": "#228833", "txt": "#195C24", "sub_txt": "#166534", "w": 2.2},
        {"name": "Outgoing Arguments", "sub": "Reserved space for callees", "bg": "#F8FAFC", "border": "#CBD5E1", "txt": "#334155", "sub_txt": "#64748B", "w": 1.2}
    ]
    
    for i, s in enumerate(slots):
        sy = start_y + i * (h_slot + gap)
        svg.append(f'''
  <g id="slot-{i}" filter="url(#subtle-shadow)">
    <rect x="{box_x}" y="{sy}" width="{box_w}" height="{h_slot}" rx="4" fill="{s['bg']}" stroke="{s['border']}" stroke-width="{s['w']}"/>
    <text x="{box_x + 12}" y="{sy + 16}" fill="{s['txt']}" font-size="11" font-weight="700">{s['name']}</text>
    <text x="{box_x + 12}" y="{sy + 30}" fill="{s['sub_txt']}" font-size="9">{s['sub']}</text>
  </g>''')

    # Right Side: Attack & Bypass Dynamics
    vla_y = start_y + 5 * (h_slot + gap) + h_slot / 2
    lr_y = start_y + 3 * (h_slot + gap) + h_slot / 2
    canary_y = start_y + 1 * (h_slot + gap) + h_slot / 2
    
    arrow_origin_x = box_x + box_w + 10
    curve_x = arrow_origin_x + 24
    
    # Red Upward Overflow Vector
    svg.append(f'''
  <!-- Upward Overflow Path -->
  <path d="M {arrow_origin_x} {vla_y} C {curve_x + 10} {vla_y}, {curve_x + 10} {lr_y}, {arrow_origin_x + 4} {lr_y}" 
        fill="none" stroke="#CC3311" stroke-width="2.2" stroke-dasharray="5,3" marker-end="url(#arrow-red-up)"/>
        
  <!-- Overflow Annotation -->
  <g transform="translate({curve_x + 20}, {vla_y - 20})">
    <text x="0" y="0" fill="#CC3311" font-size="11" font-weight="700">1. Buffer Overflow</text>
    <text x="0" y="14" fill="#7F2615" font-size="9.5">Grows upward toward higher addr</text>
  </g>

  <!-- Hijack Annotation -->
  <g transform="translate({curve_x + 20}, {lr_y + 4})">
    <text x="0" y="0" fill="#CC3311" font-size="11" font-weight="700">Clobbers LR' Directly!</text>
    <text x="0" y="14" fill="#64748B" font-size="9">Control flow hijacked on return</text>
  </g>
''')

    # Canary Intact Indicator
    svg.append(f'''
  <!-- Canary Status Indicator -->
  <line x1="{box_x + box_w + 10}" y1="{canary_y}" x2="{curve_x + 14}" y2="{canary_y}" stroke="#F5A623" stroke-width="1.5" stroke-dasharray="3,3"/>
  <rect x="{curve_x + 18}" y="{canary_y - 14}" width="160" height="28" rx="4" fill="#FFF8E1" stroke="#F5A623" stroke-width="1.2"/>
  <text x="{curve_x + 28}" y="{canary_y + 4}" fill="#7D4E00" font-size="10" font-weight="700">2. Canary Intact (Bypassed!)</text>
''')

    # Silent Failure Verdict Badge at Bottom
    verdict_y = start_y + 6 * (h_slot + gap) + 4
    svg.append(f'''
  <!-- Verdict Box -->
  <g transform="translate({curve_x + 18}, {verdict_y})">
    <rect x="0" y="0" width="160" height="34" rx="4" fill="#FEF2F2" stroke="#DC2626" stroke-width="1.2"/>
    <text x="10" y="15" fill="#991B1B" font-size="10" font-weight="700">&#x26A0; Silent Defense Failure</text>
    <text x="10" y="27" fill="#64748B" font-size="8.5">Epilogue check PASSES silently</text>
  </g>
''')

    svg.append('</svg>')
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")
    
    pdf_path = output_path.replace(".svg", ".pdf")
    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, output_path], check=True)
    print(f"Compiled to {pdf_path}")

if __name__ == "__main__":
    create_defense_matrix_svg()
    create_stack_layout_svg()
