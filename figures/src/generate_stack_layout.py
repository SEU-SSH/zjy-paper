#!/usr/bin/env python3
"""
Generate a publication-grade, colorful vector diagram for Figure 1:
CVE-2023-4039 Buggy AArch64 Stack Frame Layout.
Produces SVG and converts to PDF via rsvg-convert.
"""

import os
import subprocess

def create_stack_layout_svg(output_path="figures/stack-layout.svg"):
    # Dimensions suited for standard IEEE single-column width (approx 3.5 in)
    width = 720
    height = 540
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')
    
    # SVG Definitions (Gradients, Shadows, Markers, Symbols)
    svg.append('''
  <defs>
    <!-- Drop Shadows -->
    <filter id="shadow-card" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <filter id="shadow-alert" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#dc2626" flood-opacity="0.2"/>
    </filter>

    <!-- Gradients -->
    <linearGradient id="grad-canary" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FEF3C7"/>
      <stop offset="100%" stop-color="#FDE68A"/>
    </linearGradient>
    <linearGradient id="grad-lr" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FEE2E2"/>
      <stop offset="100%" stop-color="#FECACA"/>
    </linearGradient>
    <linearGradient id="grad-vla" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFEDD5"/>
      <stop offset="100%" stop-color="#FED7AA"/>
    </linearGradient>
    <linearGradient id="grad-neutral" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <linearGradient id="grad-overflow" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#EA580C"/>
      <stop offset="60%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#991B1B"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrow-axis-up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 10 L 5 0 L 10 10 z" fill="#64748B"/>
    </marker>
    <marker id="arrow-axis-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 0 L 5 10 z" fill="#64748B"/>
    </marker>
    <marker id="arrow-overflow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>

    <!-- Vector Icon: Shield -->
    <g id="icon-shield">
      <path d="M 8 1 L 1 4 C 1 9 4.5 13.5 8 15 C 11.5 13.5 15 9 15 4 Z" fill="#D97706" stroke="#92400E" stroke-width="1.2"/>
      <path d="M 5 7.5 L 7 9.5 L 11 5" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- Vector Icon: Alert Triangle -->
    <g id="icon-alert">
      <path d="M 8 1 L 15 14 L 1 14 Z" fill="#DC2626" stroke="#991B1B" stroke-width="1.2" stroke-linejoin="round"/>
      <line x1="8" y1="5.5" x2="8" y2="9.5" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="8" cy="11.8" r="0.9" fill="#FFFFFF"/>
    </g>

    <!-- Vector Icon: Origin Crosshair -->
    <g id="icon-origin">
      <circle cx="8" cy="8" r="6.5" fill="#EA580C" stroke="#C2410C" stroke-width="1.2"/>
      <circle cx="8" cy="8" r="2.5" fill="#FFFFFF"/>
    </g>

    <!-- Vector Icon: Checkmark -->
    <g id="icon-check">
      <circle cx="7" cy="7" r="6" fill="#16A34A"/>
      <path d="M 4 7 L 6 9 L 10 4.5" fill="none" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </defs>
''')
    
    # Left Axis: Memory Address & Stack Growth
    svg.append('''
  <!-- Memory Address Axis (Leftmost) -->
  <line x1="45" y1="490" x2="45" y2="45" stroke="#64748B" stroke-width="2" marker-end="url(#arrow-axis-up)"/>
  <text x="45" y="30" font-size="11.5" font-weight="700" fill="#334155" text-anchor="middle">High Address</text>
  <text x="32" y="265" font-size="11" font-weight="600" fill="#64748B" text-anchor="middle" transform="rotate(-90 32 265)">Memory Address Grows</text>
  <text x="45" y="515" font-size="11.5" font-weight="700" fill="#334155" text-anchor="middle">Low Address</text>

  <!-- Stack Growth Axis -->
  <line x1="80" y1="55" x2="80" y2="480" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#arrow-axis-down)"/>
  <text x="92" y="265" font-size="11" font-weight="600" fill="#64748B" text-anchor="middle" transform="rotate(90 92 265)">Stack Grows Down</text>
''')

    # Stack Blocks Configuration
    stack_x = 125
    stack_w = 335
    
    blocks = [
        {
            "id": "incoming",
            "y": 45, "h": 50,
            "fill": "url(#grad-neutral)", "stroke": "#94A3B8", "sw": 1.5,
            "icon": None,
            "title": "Incoming Stack Arguments",
            "badge": "Caller Frame", "badge_bg": "#E2E8F0", "badge_fg": "#475569",
            "note": "Caller arguments passed on stack"
        },
        {
            "id": "canary",
            "y": 105, "h": 56,
            "fill": "url(#grad-canary)", "stroke": "#D97706", "sw": 2.2,
            "icon": "icon-shield",
            "title": "Stack Canary (Guard Slot)",
            "badge": "Epilogue Checked", "badge_bg": "#FEF3C7", "badge_fg": "#B45309",
            "note": "Intended to guard saved frame records"
        },
        {
            "id": "locals",
            "y": 171, "h": 50,
            "fill": "url(#grad-neutral)", "stroke": "#94A3B8", "sw": 1.5,
            "icon": None,
            "title": "Local Variables &amp; Spills",
            "badge": "frame_pointer_rtx", "badge_bg": "#E2E8F0", "badge_fg": "#475569",
            "note": "Static scalar &amp; array local allocations"
        },
        {
            "id": "retaddr",
            "y": 231, "h": 56,
            "fill": "url(#grad-lr)", "stroke": "#DC2626", "sw": 2.2,
            "icon": "icon-alert",
            "title": "Saved Return Address (LR\')",
            "badge": "ATTACK TARGET", "badge_bg": "#FEE2E2", "badge_fg": "#B91C1C",
            "note": "Corrupted before canary is reached!"
        },
        {
            "id": "fpsve",
            "y": 297, "h": 50,
            "fill": "url(#grad-neutral)", "stroke": "#94A3B8", "sw": 1.5,
            "icon": None,
            "title": "Saved FP\' / SVE Registers",
            "badge": "Callee-Saved", "badge_bg": "#E2E8F0", "badge_fg": "#475569",
            "note": "Frame pointer and vector registers"
        },
        {
            "id": "vla",
            "y": 357, "h": 60,
            "fill": "url(#grad-vla)", "stroke": "#EA580C", "sw": 2.2,
            "icon": "icon-origin",
            "title": "VLA Buffer (alloca / Dynamic)",
            "badge": "OVERFLOW ORIGIN", "badge_bg": "#FFEDD5", "badge_fg": "#C2410C",
            "note": "Dynamic array allocated below saved LR\'"
        },
        {
            "id": "outgoing",
            "y": 427, "h": 50,
            "fill": "url(#grad-neutral)", "stroke": "#CBD5E1", "sw": 1.5,
            "icon": None,
            "title": "Outgoing Stack Arguments",
            "badge": "Callee Args", "badge_bg": "#E2E8F0", "badge_fg": "#475569",
            "note": "Space reserved for outgoing calls"
        }
    ]

    for b in blocks:
        text_x = stack_x + 16
        icon_svg = ""
        if b["icon"]:
            icon_svg = f'<use href="#{b["icon"]}" x="{stack_x + 14}" y="{b["y"] + 12}"/>'
            text_x = stack_x + 36

        svg.append(f'''
  <!-- Block: {b['id']} -->
  <g filter="url(#shadow-card)">
    <rect x="{stack_x}" y="{b['y']}" width="{stack_w}" height="{b['h']}" rx="6" fill="{b['fill']}" stroke="{b['stroke']}" stroke-width="{b['sw']}"/>
    {icon_svg}
    <text x="{text_x}" y="{b['y'] + 24}" font-size="13" font-weight="700" fill="#1E293B">{b['title']}</text>
    <text x="{stack_x + 16}" y="{b['y'] + 42}" font-size="11" font-weight="500" fill="#64748B">{b['note']}</text>
    
    <!-- Badge -->
    <rect x="{stack_x + stack_w - 118}" y="{b['y'] + 12}" width="106" height="20" rx="4" fill="{b['badge_bg']}" stroke="{b['stroke']}" stroke-width="1"/>
    <text x="{stack_x + stack_w - 65}" y="{b['y'] + 26}" font-size="9.5" font-weight="700" fill="{b['badge_fg']}" text-anchor="middle">{b['badge']}</text>
  </g>
''')

    # Overflow Trajectory Arrow (Right side)
    svg.append('''
  <!-- Overflow Trajectory (Red curved dashed line) -->
  <g filter="url(#shadow-alert)">
    <path d="M 460 387 C 520 387, 525 330, 525 259 L 467 259" 
          fill="none" stroke="url(#grad-overflow)" stroke-width="3.5" stroke-dasharray="6 3"
          marker-end="url(#arrow-overflow)"/>
    
    <!-- Pulse dot at overflow origin -->
    <circle cx="460" cy="387" r="5" fill="#EA580C" stroke="#FFFFFF" stroke-width="2"/>
  </g>

  <!-- Explanatory Callout Card for Vulnerability -->
  <g filter="url(#shadow-alert)">
    <rect x="510" y="190" width="195" height="138" rx="8" fill="#FFF1F2" stroke="#F43F5E" stroke-width="1.8"/>
    
    <!-- Callout Header -->
    <rect x="510" y="190" width="195" height="28" rx="8" fill="#FFE4E6"/>
    <use href="#icon-alert" x="522" y="196"/>
    <text x="618" y="209" font-size="11.5" font-weight="800" fill="#BE123C" text-anchor="middle">SILENT DEFENSE FAILURE</text>
    
    <text x="522" y="238" font-size="10.5" font-weight="700" fill="#881337">• Overflow grows UP</text>
    <text x="522" y="254" font-size="10" font-weight="600" fill="#9F1239">  from VLA into saved LR\'</text>
    
    <text x="522" y="278" font-size="10.5" font-weight="700" fill="#881337">• LR\' corrupted &amp; hijacked!</text>
    
    <text x="522" y="300" font-size="10" font-weight="600" fill="#4C1D95">• Canary sits HIGHER above</text>
    <use href="#icon-check" x="522" y="307"/>
    <text x="540" y="318" font-size="10" font-weight="700" fill="#15803D">Canary check PASSES!</text>
  </g>
''')

    svg.append('</svg>')
    
    content = "\n".join(svg)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated SVG: {output_path}")

    # Convert to PDF via rsvg-convert
    pdf_path = output_path.replace(".svg", ".pdf")
    cmd = ["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, output_path]
    subprocess.run(cmd, check=True)
    print(f"Generated PDF: {pdf_path}")

if __name__ == "__main__":
    create_stack_layout_svg()
