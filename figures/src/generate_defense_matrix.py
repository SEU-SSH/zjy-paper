#!/usr/bin/env python3
"""
Generate a publication-grade, crisp vector diagram for Figure:
The Defense Mechanism x ISA Research & Testing Space Matrix.
Produces SVG and converts to vector PDF via rsvg-convert.
"""

import os
import subprocess

def create_defense_matrix_svg(output_path="figures/defense-matrix.svg"):
    width = 680
    height = 290

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    # Grid specifications
    x_start = 180
    y_start = 45
    cell_w = 78
    cell_h = 36
    gap = 5

    isas = ["x86-64", "AArch64", "RISC-V", "LoongArch", "MIPS", "..."]
    defenses = [
        "Stack Canary",
        "_FORTIFY_SOURCE",
        "PAC / CFI",
        "Shadow Stack",
        "SafeStack"
    ]

    matrix_data = [
        # Stack Canary
        [0, 1, 0, 3, 3, -1],
        # _FORTIFY_SOURCE
        [3, 3, 3, 3, 3, -1],
        # PAC / CFI
        [2, 0, 0, 0, 0, -1],
        # Shadow Stack
        [0, 2, 0, 0, 0, -1],
        # SafeStack
        [0, 0, 2, 0, 0, -1]
    ]

    # Draw Column Headers (ISAs)
    for j, isa in enumerate(isas):
        cx = x_start + j * (cell_w + gap) + cell_w / 2
        svg.append(f'<text x="{cx}" y="{y_start - 12}" fill="#334155" font-size="12" font-weight="700" text-anchor="middle">{isa}</text>')

    # Draw Rows
    for i, defense in enumerate(defenses):
        cy = y_start + i * (cell_h + gap)
        # Row label
        svg.append(f'<text x="{x_start - 14}" y="{cy + cell_h/2 + 4}" fill="#1E293B" font-size="12" font-weight="600" text-anchor="end">{defense}</text>')

        # Cells
        for j in range(len(isas)):
            cx = x_start + j * (cell_w + gap)
            status = matrix_data[i][j]

            if j == len(isas) - 1: # The "..." column
                svg.append(f'<text x="{cx + cell_w/2}" y="{cy + cell_h/2 + 4}" fill="#94A3B8" font-size="14" font-weight="600" text-anchor="middle">...</text>')
                continue

            if status == 0:
                # Unexplored
                svg.append(f'<rect x="{cx}" y="{cy}" width="{cell_w}" height="{cell_h}" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/>')
                svg.append(f'<text x="{cx + cell_w/2}" y="{cy + cell_h/2 + 4}" fill="#CBD5E1" font-size="13" text-anchor="middle">&#x2014;</text>')
            elif status == 1:
                # Historical CVE
                svg.append(f'<rect x="{cx}" y="{cy}" width="{cell_w}" height="{cell_h}" rx="4" fill="#FEE2E2" stroke="#F87171" stroke-width="1.5"/>')
                svg.append(f'<circle cx="{cx + 18}" cy="{cy + cell_h/2}" r="4" fill="#DC2626"/>')
                svg.append(f'<text x="{cx + 28}" y="{cy + cell_h/2 + 3.5}" fill="#991B1B" font-size="9.5" font-weight="700">CVE</text>')
            elif status == 2:
                # Reported / Audit
                svg.append(f'<rect x="{cx}" y="{cy}" width="{cell_w}" height="{cell_h}" rx="4" fill="#FEF3C7" stroke="#FBBF24" stroke-width="1.5"/>')
                svg.append(f'<circle cx="{cx + 16}" cy="{cy + cell_h/2}" r="4" fill="#D97706"/>')
                svg.append(f'<text x="{cx + 26}" y="{cy + cell_h/2 + 3.5}" fill="#92400E" font-size="9.5" font-weight="700">Audit</text>')
            elif status == 3:
                # Confirmed & Merged (DeFuzz)
                svg.append(f'<rect x="{cx}" y="{cy}" width="{cell_w}" height="{cell_h}" rx="4" fill="#D1FAE5" stroke="#34D399" stroke-width="1.5"/>')
                svg.append(f'<text x="{cx + 15}" y="{cy + cell_h/2 + 4}" fill="#059669" font-size="11" font-weight="800">&#x2713;</text>')
                svg.append(f'<text x="{cx + 26}" y="{cy + cell_h/2 + 3.5}" fill="#065F46" font-size="9.5" font-weight="700">Verified</text>')

    # Legend at Bottom
    leg_y = y_start + len(defenses) * (cell_h + gap) + 18
    svg.append(f'''
  <!-- Legend Container -->
  <g id="legend" transform="translate(30, {leg_y})">
    <!-- Unexplored -->
    <rect x="0" y="0" width="16" height="16" rx="3" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="22" y="12.5" fill="#64748B" font-size="10.5">Unexplored Space</text>

    <!-- Historical CVE -->
    <rect x="135" y="0" width="16" height="16" rx="3" fill="#FEE2E2" stroke="#F87171" stroke-width="1.5"/>
    <circle cx="143" cy="8" r="3" fill="#DC2626"/>
    <text x="157" y="12.5" fill="#64748B" font-size="10.5">Historical CVE</text>

    <!-- Reported / Audit -->
    <rect x="255" y="0" width="16" height="16" rx="3" fill="#FEF3C7" stroke="#FBBF24" stroke-width="1.5"/>
    <circle cx="263" cy="8" r="3" fill="#D97706"/>
    <text x="277" y="12.5" fill="#64748B" font-size="10.5">Reported / Under Audit</text>

    <!-- Confirmed & Merged -->
    <rect x="425" y="0" width="16" height="16" rx="3" fill="#D1FAE5" stroke="#34D399" stroke-width="1.5"/>
    <text x="428" y="12.5" fill="#059669" font-size="10" font-weight="800">&#x2713;</text>
    <text x="447" y="12.5" fill="#64748B" font-size="10.5">Confirmed &amp; Merged (DeFuzz)</text>
  </g>
''')

    svg.append('</svg>')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print(f"Generated {output_path}")

    pdf_path = output_path.replace(".svg", ".pdf")
    subprocess.run(["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, output_path], check=True)
    print(f"Compiled to {pdf_path}")

if __name__ == "__main__":
    create_defense_matrix_svg()
