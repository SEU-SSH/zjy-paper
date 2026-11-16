#!/usr/bin/env python3
"""
Generate publication-grade vector SVG & PDF figures for Section V (Evaluation):
1. figures/eval-bug-char.{svg,pdf}: Two-panel characterization of the 111 silent defense bugs
   (a) Root-cause compilation stage (GCC vs. LLVM)
   (b) Target ISA scope split by compiler
2. figures/eval-rq2-comparison.{svg,pdf}: Baseline comparison across 6 compiler fuzzers
   (a) Silent defense bugs by family (F1-F6) under the shared DeFenzz checker suite
   (b) Defense branch coverage (%) across all four 64-bit target ISAs (/ 9,061 probes)
3. figures/eval-ablation.{svg,pdf}: Two-scope controlled ablation study
   (a) Full campaign (921 invariants, 4 ISAs): Check IR & RAG transfer
   (b) Controlled audit lane (41 invariants, GCC-16 AArch64): Source mapping, LLM judge, & Bare agent
4. figures/eval-tool-calls.{svg,pdf}: Agent tool-invocation share & volume across pipeline stages

Palette matches figures/method-overview.pdf and figures/defense-matrix.pdf:
deep emerald (#228833), warm amber (#D97706), bronze (#92400E), honey gold (#FDE68A),
crimson (#B91C1C / #DC2626), muted cerulean (#0284C7), slate stone (#CBD5E1 / #94A3B8).
"""

import os
import subprocess

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RSVG = "/opt/homebrew/bin/rsvg-convert"
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"


def save_and_compile(svg_lines, stem):
    svg_path = os.path.join(ROOT_DIR, f"{stem}.svg")
    pdf_path = os.path.join(ROOT_DIR, f"{stem}.pdf")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
    subprocess.run([RSVG, "--format=pdf1.5", "-o", pdf_path, svg_path], check=True)
    print(f"Generated {svg_path} -> {pdf_path}")


def generate_bug_char():
    W, H = 880, 212
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'style="background-color: #FFFFFF; font-family: {FONT};">'
    ]

    C_GCC = "#228833"
    C_LLVM = "#D97706"
    C_HIGH = "#B91C1C"
    C_MED = "#D97706"
    C_LOW = "#CBD5E1"
    C_INK = "#1C1917"
    C_SUB = "#57534E"
    C_GRID = "#E7E5E4"
    C_AXIS = "#78716C"

    # ---------------- PANEL (a): Root-Cause Compilation Stage ----------------
    ax_x = 162
    ax_w = 232
    row_h = 22
    max_a = 60.0

    svg.append(
        f'<text x="{ax_x + ax_w/2 - 15}" y="16" fill="{C_INK}" font-size="11.5" '
        f'font-weight="700" text-anchor="middle">(a) Root-Cause Compilation Stage (n = 111)</text>'
    )

    leg_a_x = ax_x + 4
    svg.append(f'<rect x="{leg_a_x}" y="23" width="9" height="9" rx="1.5" fill="{C_GCC}"/>')
    svg.append(f'<text x="{leg_a_x + 13}" y="31" fill="{C_SUB}" font-size="9.5" font-weight="600">GCC (58)</text>')
    svg.append(f'<rect x="{leg_a_x + 70}" y="23" width="9" height="9" rx="1.5" fill="{C_LLVM}"/>')
    svg.append(f'<text x="{leg_a_x + 83}" y="31" fill="{C_SUB}" font-size="9.5" font-weight="600">LLVM (53)</text>')

    stages = [
        ("Backend Lowering", 27, 27),
        ("Middle-End Passes", 12, 13),
        ("Frontend", 9, 3),
        ("Option Lowering", 5, 5),
        ("IPA and LTO", 5, 2),
        ("Runtime Library", 0, 3),
    ]

    plot_top = 40
    plot_bot = plot_top + len(stages) * row_h

    for tick in [0, 15, 30, 45, 60]:
        tx = ax_x + (tick / max_a) * ax_w
        svg.append(f'<line x1="{tx:.1f}" y1="{plot_top}" x2="{tx:.1f}" y2="{plot_bot}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{tx:.1f}" y="{plot_bot + 13}" fill="{C_SUB}" font-size="9" text-anchor="middle">{tick}</text>')

    svg.append(
        f'<text x="{ax_x + ax_w/2}" y="{plot_bot + 27}" fill="{C_INK}" font-size="9.5" '
        f'font-weight="600" text-anchor="middle">Silent Defense Bugs</text>'
    )

    for idx, (label, g_val, l_val) in enumerate(stages):
        cy = plot_top + idx * row_h + 4
        bh = 14
        tot = g_val + l_val
        pct = tot / 111.0 * 100.0
        gw = (g_val / max_a) * ax_w
        lw = (l_val / max_a) * ax_w

        svg.append(f'<text x="{ax_x - 7}" y="{cy + 10.5}" fill="{C_INK}" font-size="9.8" font-weight="500" text-anchor="end">{label}</text>')
        if gw > 0:
            svg.append(f'<rect x="{ax_x:.1f}" y="{cy}" width="{gw:.1f}" height="{bh}" fill="{C_GCC}"/>')
            if gw >= 18:
                svg.append(f'<text x="{ax_x + gw/2:.1f}" y="{cy + 10.3}" fill="#FFFFFF" font-size="8.5" font-weight="700" text-anchor="middle">{g_val}</text>')
        if lw > 0:
            svg.append(f'<rect x="{ax_x + gw:.1f}" y="{cy}" width="{lw:.1f}" height="{bh}" fill="{C_LLVM}"/>')
            if lw >= 18:
                svg.append(f'<text x="{ax_x + gw + lw/2:.1f}" y="{cy + 10.3}" fill="#FFFFFF" font-size="8.5" font-weight="700" text-anchor="middle">{l_val}</text>')

        svg.append(f'<text x="{ax_x + gw + lw + 5:.1f}" y="{cy + 10.3}" fill="{C_INK}" font-size="9" font-weight="600">{tot} ({pct:.1f}%)</text>')

    svg.append(f'<line x1="{ax_x}" y1="{plot_top}" x2="{ax_x}" y2="{plot_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{ax_x}" y1="{plot_bot}" x2="{ax_x + ax_w}" y2="{plot_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    svg.append(f'<line x1="448" y1="12" x2="448" y2="{H - 12}" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3,3"/>')

    # ---------------- PANEL (b): Target ISA Scope (GCC vs. LLVM) ----------------
    bx_x = 608
    bx_w = 212
    max_b = 75.0
    row_hb = 33

    svg.append(
        f'<text x="{bx_x + bx_w/2 - 18}" y="16" fill="{C_INK}" font-size="11.5" '
        f'font-weight="700" text-anchor="middle">(b) Target ISA Scope (n = 111)</text>'
    )

    leg_b_x = bx_x + 4
    svg.append(f'<rect x="{leg_b_x}" y="23" width="9" height="9" rx="1.5" fill="{C_GCC}"/>')
    svg.append(f'<text x="{leg_b_x + 13}" y="31" fill="{C_SUB}" font-size="9.5" font-weight="600">GCC (58)</text>')
    svg.append(f'<rect x="{leg_b_x + 70}" y="23" width="9" height="9" rx="1.5" fill="{C_LLVM}"/>')
    svg.append(f'<text x="{leg_b_x + 83}" y="31" fill="{C_SUB}" font-size="9.5" font-weight="600">LLVM (53)</text>')

    scopes = [
        ("Cross-ISA (&#8805;3 / Generic)", 28, 19, 0),
        ("Non-x86 Only (ARM/RV/LA)", 17, 18, 0),
        ("x86-64 / x86 Only", 12, 10, 0),
        ("Dual-ISA (x86 + Non-x86)", 1, 6, 0),
    ]

    plot_bot_b = plot_top + len(scopes) * row_hb

    for tick in [0, 25, 50, 75]:
        tx = bx_x + (tick / max_b) * bx_w
        svg.append(f'<line x1="{tx:.1f}" y1="{plot_top}" x2="{tx:.1f}" y2="{plot_bot_b}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{tx:.1f}" y="{plot_bot_b + 13}" fill="{C_SUB}" font-size="9" text-anchor="middle">{tick}</text>')

    svg.append(
        f'<text x="{bx_x + bx_w/2}" y="{plot_bot_b + 27}" fill="{C_INK}" font-size="9.5" '
        f'font-weight="600" text-anchor="middle">Silent Defense Bugs</text>'
    )

    for idx, (label, h_val, m_val, l_val) in enumerate(scopes):
        cy = plot_top + idx * row_hb + 7
        bh = 18
        tot = h_val + m_val + l_val
        pct = tot / 111.0 * 100.0
        hw = (h_val / max_b) * bx_w
        mw = (m_val / max_b) * bx_w
        lw = (l_val / max_b) * bx_w

        svg.append(f'<text x="{bx_x - 7}" y="{cy + 12.5}" fill="{C_INK}" font-size="9.8" font-weight="500" text-anchor="end">{label}</text>')
        if hw > 0:
            svg.append(f'<rect x="{bx_x:.1f}" y="{cy}" width="{hw:.1f}" height="{bh}" fill="{C_GCC}"/>')
            if hw >= 16:
                svg.append(f'<text x="{bx_x + hw/2:.1f}" y="{cy + 12.5}" fill="#FFFFFF" font-size="8.5" font-weight="700" text-anchor="middle">{h_val}</text>')
        if mw > 0:
            svg.append(f'<rect x="{bx_x + hw:.1f}" y="{cy}" width="{mw:.1f}" height="{bh}" fill="{C_LLVM}"/>')
            if mw >= 16:
                svg.append(f'<text x="{bx_x + hw + mw/2:.1f}" y="{cy + 12.5}" fill="#FFFFFF" font-size="8.5" font-weight="700" text-anchor="middle">{m_val}</text>')
        if lw > 0:
            svg.append(f'<rect x="{bx_x + hw + mw:.1f}" y="{cy}" width="{lw:.1f}" height="{bh}" fill="{C_LOW}" stroke="#94A3B8" stroke-width="0.6"/>')
            if lw >= 15:
                svg.append(f'<text x="{bx_x + hw + mw + lw/2:.1f}" y="{cy + 12.5}" fill="#1E293B" font-size="8.5" font-weight="700" text-anchor="middle">{l_val}</text>')

        svg.append(f'<text x="{bx_x + hw + mw + lw + 5:.1f}" y="{cy + 12.5}" fill="{C_INK}" font-size="9" font-weight="600">{tot} ({pct:.1f}%)</text>')

    svg.append(f'<line x1="{bx_x}" y1="{plot_top}" x2="{bx_x}" y2="{plot_bot_b}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{bx_x}" y1="{plot_bot_b}" x2="{bx_x + bx_w}" y2="{plot_bot_b}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    svg.append("</svg>")
    save_and_compile(svg, "eval-bug-char")


def generate_rq2_comparison():
    W, H = 880, 232
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'style="background-color: #FFFFFF; font-family: {FONT};">'
    ]

    C_INK = "#1C1917"
    C_SUB = "#57534E"
    C_GRID = "#E7E5E4"
    C_AXIS = "#78716C"

    # Family palette for Panel (a)
    FAM_COLS = [
        ("F1 CFI",       "#1B7837", "#FFFFFF", None,      14),
        ("F2 Stack",     "#D97706", "#FFFFFF", None,      66),
        ("F3 Sanitizer", "#92400E", "#FFFFFF", None,      126),
        ("F4 Scrub",     "#0284C7", "#FFFFFF", None,      202),
        ("F5 Spec",      "#FDE68A", "#78350F", "#B45309", 264),
        ("F6 Fortify",   "#B91C1C", "#FFFFFF", None,      322),
    ]

    # ---------------- PANEL (a): Per-Family Silent Bugs (+Our Oracle) ----------------
    ax_x = 80
    ax_w = 248
    plot_top = 43
    row_h = 22.5
    ours_extra_gap = 9.0
    max_a = 120.0

    svg.append(
        f'<text x="214" y="15.5" fill="{C_INK}" font-size="11.3" '
        f'font-weight="700" text-anchor="middle">(a) Silent Bugs by Defense Family</text>'
    )

    # Uniformly spaced single-row legend for F1..F6
    for lbl, fill, _, stroke, lx in FAM_COLS:
        st_attr = f' stroke="{stroke}" stroke-width="0.6"' if stroke else ""
        svg.append(f'<rect x="{lx}" y="23" width="8.5" height="8.5" rx="1.5" fill="{fill}"{st_attr}/>')
        svg.append(f'<text x="{lx + 11}" y="30.5" fill="{C_SUB}" font-size="8.6" font-weight="600">{lbl}</text>')

    fuzzers_a = [
        ("YARPGen",     [1, 0, 0, 0, 0, 0],     "1",     False),
        ("UBfuzz",      [1, 0, 2, 0, 0, 0],     "3",    False),
        ("MetaMut",     [1, 1, 6, 0, 0, 0],     "8",     False),
        ("FeatureFuzz", [2, 1, 7, 0, 1, 3],     "14",    False),
        ("Fuzz4All",    [3, 1, 9, 1, 1, 3],     "18",   False),
        ("DeFenzz",     [36, 21, 21, 10, 9, 14], "111", True),
    ]

    plot_bot_a = plot_top + len(fuzzers_a) * row_h + ours_extra_gap

    for tick in [0, 30, 60, 90, 120]:
        tx = ax_x + (tick / max_a) * ax_w
        svg.append(f'<line x1="{tx:.1f}" y1="{plot_top}" x2="{tx:.1f}" y2="{plot_bot_a:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{tx:.1f}" y="{plot_bot_a + 12.5:.1f}" fill="{C_SUB}" font-size="8.8" text-anchor="middle">{tick}</text>')

    svg.append(
        f'<text x="{ax_x + ax_w/2:.1f}" y="{plot_bot_a + 26.5:.1f}" fill="{C_INK}" font-size="9.4" '
        f'font-weight="600" text-anchor="middle">Deduplicated Silent Defense Bugs (F1&#8211;F6)</text>'
    )

    # Vertical dashed guide from Fuzz4All end (18) down into the bracket channel
    x_18 = ax_x + (18.0 / max_a) * ax_w
    x_111 = ax_x + (111.0 / max_a) * ax_w
    br_y = plot_top + 5 * row_h + 6.5
    svg.append(
        f'<line x1="{x_18:.1f}" y1="{plot_top + 4 * row_h + 18:.1f}" x2="{x_18:.1f}" '
        f'y2="{br_y + 3:.1f}" stroke="#B45309" stroke-width="1" stroke-dasharray="2.5,2"/>'
    )

    # Bracket spanning [18, 111] directly above DeFenzz bar
    svg.append(f'<line x1="{x_18:.1f}" y1="{br_y:.1f}" x2="{x_111:.1f}" y2="{br_y:.1f}" stroke="#B45309" stroke-width="1.15"/>')
    svg.append(f'<line x1="{x_18:.1f}" y1="{br_y - 2.6:.1f}" x2="{x_18:.1f}" y2="{br_y + 2.6:.1f}" stroke="#B45309" stroke-width="1.15"/>')
    svg.append(f'<line x1="{x_111:.1f}" y1="{br_y - 2.6:.1f}" x2="{x_111:.1f}" y2="{br_y + 2.6:.1f}" stroke="#B45309" stroke-width="1.15"/>')

    # Exclusive callout badge placed in clean upper-right whitespace (rows 0-2, x=196..396)
    badge_x, badge_y, badge_w, badge_h = 196.0, plot_top + 10.0, 198.0, 31.0
    lead_x = 236.0
    svg.append(
        f'<line x1="{lead_x:.1f}" y1="{badge_y + badge_h:.1f}" x2="{lead_x:.1f}" y2="{br_y:.1f}" '
        f'stroke="#D97706" stroke-width="0.9" stroke-dasharray="2.5,2"/>'
    )
    svg.append(f'<circle cx="{lead_x:.1f}" cy="{br_y:.1f}" r="2.0" fill="#B45309"/>')
    svg.append(f'<rect x="{badge_x:.1f}" y="{badge_y:.1f}" width="{badge_w:.1f}" height="{badge_h:.1f}" rx="3.5" fill="#FEFCE8" stroke="#D97706" stroke-width="0.9"/>')
    svg.append(
        f'<text x="{badge_x + badge_w/2:.1f}" y="{badge_y + 12.5:.1f}" fill="#92400E" font-size="8.4" '
        f'font-weight="700" text-anchor="middle">+93 Exclusive to DeFenzz (83.8%)</text>'
    )
    svg.append(
        f'<text x="{badge_x + badge_w/2:.1f}" y="{badge_y + 24.5:.1f}" fill="#78350F" font-size="7.9" '
        f'font-weight="600" text-anchor="middle">Covers Every Baseline Bug (0 Missed)</text>'
    )

    for idx, (name, counts, right_lbl, is_ours) in enumerate(fuzzers_a):
        cy = plot_top + idx * row_h + (ours_extra_gap if is_ours else 0.0) + 4.0
        bh = 14.2
        fw = "700" if is_ours else "500"
        svg.append(f'<text x="{ax_x - 6}" y="{cy + 10.4:.1f}" fill="{C_INK}" font-size="9.4" font-weight="{fw}" text-anchor="end">{name}</text>')

        cur_x = float(ax_x)
        for val, (_, fill, txt_col, stroke, _) in zip(counts, FAM_COLS):
            if val <= 0:
                continue
            sw = (val / max_a) * ax_w
            st_attr = f' stroke="{stroke}" stroke-width="0.5"' if stroke else ""
            svg.append(f'<rect x="{cur_x:.2f}" y="{cy:.1f}" width="{sw:.2f}" height="{bh}" fill="{fill}"{st_attr}/>')
            if sw >= 15.0:
                svg.append(f'<text x="{cur_x + sw/2:.1f}" y="{cy + 10.3:.1f}" fill="{txt_col}" font-size="8.0" font-weight="700" text-anchor="middle">{val}</text>')
            cur_x += sw

        lbl_col = "#166534" if is_ours else C_SUB
        lbl_w = "700" if is_ours else "600"
        svg.append(f'<text x="{cur_x + 5:.1f}" y="{cy + 10.4:.1f}" fill="{lbl_col}" font-size="8.6" font-weight="{lbl_w}">{right_lbl}</text>')

    svg.append(f'<line x1="{ax_x}" y1="{plot_top}" x2="{ax_x}" y2="{plot_bot_a:.1f}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{ax_x}" y1="{plot_bot_a:.1f}" x2="{ax_x + ax_w}" y2="{plot_bot_a:.1f}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    # Divider
    svg.append(f'<line x1="428" y1="12" x2="428" y2="{H - 12}" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3,3"/>')

    # ---------------- PANEL (b): Per-ISA Defense Branch Coverage (%) ----------------
    bx_x = 478
    bx_w = 386
    by_top = 45
    by_bot = 188
    bh_plot = by_bot - by_top

    svg.append(
        f'<text x="{bx_x + bx_w/2 - 6:.1f}" y="15.5" fill="{C_INK}" font-size="11.3" '
        f'font-weight="700" text-anchor="middle">(b) Defense Branch Coverage Across 4 ISAs (/ 9,061 Probes)</text>'
    )

    TOOL_COLS = [
        ("YARPGen",     "#E2E8F0", "#64748B", 444),
        ("UBfuzz",      "#94A3B8", None,      510),
        ("MetaMut",     "#FDE68A", "#B45309", 566),
        ("FeatureFuzz", "#F59E0B", None,      629),
        ("Fuzz4All",    "#B45309", None,      709),
        ("DeFenzz",     "#228833", None,      772),
    ]

    for tname, fill, stroke, lx in TOOL_COLS:
        st_attr = f' stroke="{stroke}" stroke-width="0.6"' if stroke else ""
        svg.append(f'<rect x="{lx}" y="23" width="8.5" height="8.5" rx="1.5" fill="{fill}"{st_attr}/>')
        fw = "700" if tname == "DeFenzz" else "600"
        fc = "#166534" if tname == "DeFenzz" else C_SUB
        svg.append(f'<text x="{lx + 11}" y="30.5" fill="{fc}" font-size="8.5" font-weight="{fw}">{tname}</text>')

    for tick in [0, 25, 50, 75, 100]:
        ty = by_bot - (tick / 100.0) * bh_plot
        svg.append(f'<line x1="{bx_x}" y1="{ty:.1f}" x2="{bx_x + bx_w}" y2="{ty:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{bx_x - 5}" y="{ty + 3.2:.1f}" fill="{C_SUB}" font-size="8.6" text-anchor="end">{tick}%</text>')

    isa_groups = [
        ("x86-64",      "(2,295)", [53.3, 64.5, 72.7, 71.0, 74.0, 80.1]),
        ("AArch64",     "(2,568)", [50.3, 61.0, 69.1, 66.9, 69.9, 79.9]),
        ("RISC-V64",    "(2,095)", [50.1, 62.1, 70.4, 68.6, 72.0, 78.5]),
        ("LoongArch64", "(2,103)", [51.5, 62.9, 71.9, 70.0, 73.3, 79.7]),
    ]

    slot_w = bx_w / len(isa_groups)
    bw = 11.2
    gap = 1.8

    for g_idx, (isa_lbl, sub_lbl, pcts) in enumerate(isa_groups):
        cx = bx_x + (g_idx + 0.5) * slot_w
        svg.append(f'<text x="{cx:.1f}" y="{by_bot + 13.5}" fill="{C_INK}" font-size="9.2" font-weight="600" text-anchor="middle">{isa_lbl}</text>')
        svg.append(f'<text x="{cx:.1f}" y="{by_bot + 24.5}" fill="{C_SUB}" font-size="8.2" font-weight="500" text-anchor="middle">{sub_lbl}</text>')

        grp_w = len(pcts) * bw + (len(pcts) - 1) * gap
        gx = cx - grp_w / 2.0
        for b_idx, (pct, (tname, fill, stroke, _)) in enumerate(zip(pcts, TOOL_COLS)):
            x_bar = gx + b_idx * (bw + gap)
            h_bar = (pct / 100.0) * bh_plot
            y_bar = by_bot - h_bar
            st_attr = f' stroke="{stroke}" stroke-width="0.6"' if stroke else ""
            svg.append(f'<rect x="{x_bar:.1f}" y="{y_bar:.1f}" width="{bw:.1f}" height="{h_bar:.1f}" rx="1.2" fill="{fill}"{st_attr}/>')
            if tname == "DeFenzz":
                svg.append(
                    f'<text x="{x_bar + bw/2:.1f}" y="{y_bar - 3.8:.1f}" fill="#166534" '
                    f'font-size="8.2" font-weight="700" text-anchor="middle">{pct:.1f}%</text>'
                )
            elif tname == "YARPGen":
                svg.append(
                    f'<text x="{x_bar + bw/2:.1f}" y="{y_bar - 3.5:.1f}" fill="#64748B" '
                    f'font-size="7.6" font-weight="600" text-anchor="middle">{pct:.0f}%</text>'
                )

    svg.append(f'<line x1="{bx_x}" y1="{by_top}" x2="{bx_x}" y2="{by_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{bx_x}" y1="{by_bot}" x2="{bx_x + bx_w}" y2="{by_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    svg.append("</svg>")
    save_and_compile(svg, "eval-rq2-comparison")


def generate_ablation():
    W, H = 540, 256
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'style="background-color: #FFFFFF; font-family: {FONT};">'
    ]

    C_TP = "#228833"      # Silent Bugs
    C_NONX = "#D97706"    # RV64 + LA64 Detections
    C_FP = "#DC2626"      # False / Spurious Claims
    C_LAT = "#92400E"     # LLM Latency (h) in Scope B
    C_INK = "#1C1917"
    C_SUB = "#57534E"
    C_GRID = "#E7E5E4"
    C_AXIS = "#78716C"

    y_top = 56
    y_bot = 212
    ph = y_bot - y_top

    # ---------------- PANEL (a): Scope A Full Campaign (921 Inv., 4 ISAs) ----------------
    ax0, ax1 = 34, 258
    aw = ax1 - ax0
    max_a = 160.0

    svg.append(
        f'<text x="{(ax0 + ax1)/2:.1f}" y="15" fill="{C_INK}" font-size="10.2" '
        f'font-weight="700" text-anchor="middle">(a) Full Campaign (921 Inv., 4 ISAs)</text>'
    )

    # Legend (a)
    svg.append(f'<rect x="24" y="23" width="8.5" height="8.5" rx="1.5" fill="{C_TP}"/>')
    svg.append(f'<text x="35" y="30.5" fill="{C_SUB}" font-size="8.2" font-weight="600">Silent Bugs</text>')
    svg.append(f'<rect x="92" y="23" width="8.5" height="8.5" rx="1.5" fill="{C_NONX}"/>')
    svg.append(f'<text x="103" y="30.5" fill="{C_SUB}" font-size="8.2" font-weight="600">RV64+LA64</text>')
    svg.append(f'<rect x="166" y="23" width="8.5" height="8.5" rx="1.5" fill="{C_FP}"/>')
    svg.append(f'<text x="177" y="30.5" fill="{C_SUB}" font-size="8.2" font-weight="600">False Alerts</text>')

    # Callout badge (a)
    svg.append(f'<rect x="40" y="36" width="212" height="15.5" rx="2.5" fill="#FEFCE8" stroke="#D97706" stroke-width="0.8"/>')
    svg.append(
        f'<text x="146" y="46.8" fill="#92400E" font-size="8.0" font-weight="700" '
        f'text-anchor="middle">Check IR: +29 Bugs | 2.1x Non-x86 | -51 FPs</text>'
    )

    for tick in [0, 40, 80, 120, 160]:
        ty = y_bot - (tick / max_a) * ph
        svg.append(f'<line x1="{ax0}" y1="{ty:.1f}" x2="{ax1}" y2="{ty:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{ax0 - 5}" y="{ty + 3:.1f}" fill="{C_SUB}" font-size="8.4" text-anchor="end">{tick}</text>')

    vars_a = [
        ("Full", "DeFenzz", (111, 136, 0)),
        ("w/o", "Check IR", (82, 64, 51)),
        ("w/o", "RAG", (109, 135, 0)),
    ]
    slot_a = aw / len(vars_a)
    bw_a = 16.0
    gap_a = 2.8

    for idx, (l1, l2, vals) in enumerate(vars_a):
        cx = ax0 + (idx + 0.5) * slot_a
        fw = "700" if idx == 0 else "600"
        svg.append(f'<text x="{cx:.1f}" y="{y_bot + 13.5}" fill="{C_INK}" font-size="8.8" font-weight="{fw}" text-anchor="middle">{l1}</text>')
        svg.append(f'<text x="{cx:.1f}" y="{y_bot + 24}" fill="{C_INK}" font-size="8.8" font-weight="{fw}" text-anchor="middle">{l2}</text>')

        grp_w = 3 * bw_a + 2 * gap_a
        gx = cx - grp_w / 2.0
        for j, (val, col) in enumerate(zip(vals, [C_TP, C_NONX, C_FP])):
            bx = gx + j * (bw_a + gap_a)
            if val == 0:
                svg.append(f'<rect x="{bx:.1f}" y="{y_bot - 2.2:.1f}" width="{bw_a:.1f}" height="2.2" fill="{col}"/>')
                svg.append(f'<text x="{bx + bw_a/2:.1f}" y="{y_bot - 5.5:.1f}" fill="{col}" font-size="8.0" font-weight="700" text-anchor="middle">0</text>')
            else:
                bh = (val / max_a) * ph
                by = y_bot - bh
                svg.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw_a:.1f}" height="{bh:.1f}" rx="1.4" fill="{col}"/>')
                svg.append(f'<text x="{bx + bw_a/2:.1f}" y="{by - 3.5:.1f}" fill="{C_INK}" font-size="8.0" font-weight="700" text-anchor="middle">{val}</text>')

    svg.append(f'<line x1="{ax0}" y1="{y_top}" x2="{ax0}" y2="{y_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{ax0}" y1="{y_bot}" x2="{ax1}" y2="{y_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    # Vertical divider
    svg.append(f'<line x1="272" y1="10" x2="272" y2="{H - 10}" stroke="#CBD5E1" stroke-width="1.1" stroke-dasharray="3,3"/>')

    # ---------------- PANEL (b): Scope B Controlled Lane (41 Inv., AArch64) ----------------
    bx0, bx1 = 304, 530
    bw_tot = bx1 - bx0
    max_b = 18.0

    svg.append(
        f'<text x="{(bx0 + bx1)/2:.1f}" y="15" fill="{C_INK}" font-size="10.2" '
        f'font-weight="700" text-anchor="middle">(b) Controlled Lane (41 Inv., AArch64)</text>'
    )

    # Legend (b)
    svg.append(f'<rect x="294" y="23" width="8.5" height="8.5" rx="1.5" fill="{C_LAT}"/>')
    svg.append(f'<text x="305" y="30.5" fill="{C_SUB}" font-size="8.2" font-weight="600">LLM Latency (h)</text>')
    svg.append(f'<rect x="392" y="23" width="8.5" height="8.5" rx="1.5" fill="{C_FP}"/>')
    svg.append(f'<text x="403" y="30.5" fill="{C_SUB}" font-size="8.2" font-weight="600">False Claims (! = Leaked)</text>')

    # Callout badge (b)
    svg.append(f'<rect x="308" y="36" width="218" height="15.5" rx="2.5" fill="#FEF2F2" stroke="#DC2626" stroke-width="0.8"/>')
    svg.append(
        f'<text x="417" y="46.8" fill="#991B1B" font-size="8.0" font-weight="700" '
        f'text-anchor="middle">LLM Judge: 6.9x Latency | Leaks Hallucination</text>'
    )

    for tick in [0, 6, 12, 18]:
        ty = y_bot - (tick / max_b) * ph
        svg.append(f'<line x1="{bx0}" y1="{ty:.1f}" x2="{bx1}" y2="{ty:.1f}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{bx0 - 5}" y="{ty + 3:.1f}" fill="{C_SUB}" font-size="8.4" text-anchor="end">{tick}</text>')

    # (line1, line2, latency_h, false_claims, leaked_flag)
    vars_b = [
        ("Full", "DeFenzz", 2.26, 4, False),
        ("w/o", "Mapping", 2.67, 9, True),
        ("w/o", "Oracle", 15.50, 6, True),
        ("Bare", "Agent", 0.14, 1, False),
    ]
    slot_b = bw_tot / len(vars_b)
    bw_b = 17.5
    gap_b = 3.2

    for idx, (l1, l2, lat_h, fc_cnt, leaked) in enumerate(vars_b):
        cx = bx0 + (idx + 0.5) * slot_b
        fw = "700" if idx == 0 else "600"
        svg.append(f'<text x="{cx:.1f}" y="{y_bot + 13.5}" fill="{C_INK}" font-size="8.8" font-weight="{fw}" text-anchor="middle">{l1}</text>')
        svg.append(f'<text x="{cx:.1f}" y="{y_bot + 24}" fill="{C_INK}" font-size="8.8" font-weight="{fw}" text-anchor="middle">{l2}</text>')

        grp_w = 2 * bw_b + gap_b
        gx = cx - grp_w / 2.0

        # Bar 1: Latency (h)
        h_lat = max((lat_h / max_b) * ph, 2.5)
        y_lat = y_bot - h_lat
        svg.append(f'<rect x="{gx:.1f}" y="{y_lat:.1f}" width="{bw_b:.1f}" height="{h_lat:.1f}" rx="1.4" fill="{C_LAT}"/>')
        lat_lbl = f"{lat_h:.1f}h"
        svg.append(f'<text x="{gx + bw_b/2:.1f}" y="{y_lat - 3.5:.1f}" fill="{C_INK}" font-size="7.8" font-weight="700" text-anchor="middle">{lat_lbl}</text>')

        # Bar 2: False candidate claims
        bx_f = gx + bw_b + gap_b
        h_fc = max((fc_cnt / max_b) * ph, 2.5)
        y_fc = y_bot - h_fc
        svg.append(f'<rect x="{bx_f:.1f}" y="{y_fc:.1f}" width="{bw_b:.1f}" height="{h_fc:.1f}" rx="1.4" fill="{C_FP}"/>')
        fc_lbl = f"{fc_cnt}!" if leaked else f"{fc_cnt}"
        fc_col = "#B91C1C" if leaked else C_INK
        svg.append(f'<text x="{bx_f + bw_b/2:.1f}" y="{y_fc - 3.5:.1f}" fill="{fc_col}" font-size="8.0" font-weight="700" text-anchor="middle">{fc_lbl}</text>')

    svg.append(f'<line x1="{bx0}" y1="{y_top}" x2="{bx0}" y2="{y_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{bx0}" y1="{y_bot}" x2="{bx1}" y2="{y_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    svg.append("</svg>")
    save_and_compile(svg, "eval-ablation")


def generate_tool_calls():
    W, H = 520, 246
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'style="background-color: #FFFFFF; font-family: {FONT};">'
    ]

    C_CG = "#92400E"      # Call-Graph Query (deep bronze)
    C_GREP = "#D97706"    # Lexical Search (warm amber)
    C_READ = "#FDE68A"    # Slice Read (honey gold)
    C_WRITE = "#228833"   # Write / Edit (emerald)
    C_WS = "#CBD5E1"      # Workspace / Exec (slate stone)

    C_INK = "#1C1917"
    C_SUB = "#57534E"
    C_GRID = "#E7E5E4"
    C_AXIS = "#78716C"

    leg_items = [
        ("Call-Graph", C_CG, None),
        ("Lexical Search", C_GREP, None),
        ("Slice Read", C_READ, "#B45309"),
        ("Write / Edit", C_WRITE, None),
        ("Workspace / Exec", C_WS, "#94A3B8"),
    ]
    lx = 16
    for label, fill, stroke in leg_items:
        st_attr = f' stroke="{stroke}" stroke-width="0.7"' if stroke else ""
        svg.append(f'<rect x="{lx}" y="9" width="9.5" height="9.5" rx="1.5" fill="{fill}"{st_attr}/>')
        svg.append(f'<text x="{lx + 12.5}" y="17.2" fill="{C_INK}" font-size="8.6" font-weight="600">{label}</text>')
        lx += len(label) * 5.0 + 22

    rows = [
        ("Source Map (GCC)",   9529, 17322, 12292,    0, 13810, 3677, False),
        ("Source Map (LLVM)",     9,  3421,  2606,    0,   208,  568, False),
        ("Check IR (GCC)",        0,   101,    90,  607,    10,  558, False),
        ("Check IR (LLVM)",       0,   155,    91,  609,    17,  562, False),
        ("Fuzz Loop (GCC)",    1498, 10757, 10261,    0,  1408,  860, False),
        ("Fuzz Loop (LLVM)",   1077,  7317,  5272,    0,   769,  573, False),
        ("w/o Check IR (All)",    0,  4606,  7961, 4447,  1481, 1229, True),
    ]

    x0 = 114
    bw_tot = 292
    y_top = 35
    row_h = 24.5
    plot_bot = y_top + len(rows) * row_h + 5

    svg.append(f'<text x="{x0 + bw_tot + 8}" y="30" fill="{C_SUB}" font-size="8.5" font-weight="700">Calls (Avg/Sess)</text>')

    for tick in [0, 25, 50, 75, 100]:
        tx = x0 + (tick / 100.0) * bw_tot
        svg.append(f'<line x1="{tx:.1f}" y1="{y_top}" x2="{tx:.1f}" y2="{plot_bot}" stroke="{C_GRID}" stroke-width="1"/>')
        svg.append(f'<text x="{tx:.1f}" y="{plot_bot + 12}" fill="{C_SUB}" font-size="8.8" text-anchor="middle">{tick}%</text>')

    svg.append(
        f'<text x="{x0 + bw_tot/2}" y="{plot_bot + 25}" fill="{C_INK}" font-size="9.3" '
        f'font-weight="600" text-anchor="middle">Tool Invocation Share (%)</text>'
    )

    for idx, (label, cg, gr, rd, wr, ws, sess, is_base) in enumerate(rows):
        extra_y = 5.0 if is_base else 0.0
        if is_base:
            sep_y = y_top + idx * row_h + 2.0
            svg.append(f'<line x1="12" y1="{sep_y:.1f}" x2="{W - 10}" y2="{sep_y:.1f}" stroke="#CBD5E1" stroke-width="1" stroke-dasharray="3,2.5"/>')

        cy = y_top + idx * row_h + 4.5 + extra_y
        bh = 15.0
        tot = cg + gr + rd + wr + ws
        avg_s = tot / max(sess, 1)

        lbl_weight = "700" if is_base else "600"
        lbl_col = "#78716C" if is_base else C_INK
        svg.append(f'<text x="{x0 - 6}" y="{cy + 11}" fill="{lbl_col}" font-size="9.2" font-weight="{lbl_weight}" text-anchor="end">{label}</text>')

        cur_x = float(x0)
        segs = [
            (cg, C_CG, "#FFFFFF", None),
            (gr, C_GREP, "#FFFFFF", None),
            (rd, C_READ, "#78350F", "#D97706"),
            (wr, C_WRITE, "#FFFFFF", None),
            (ws, C_WS, "#334155", "#94A3B8"),
        ]
        for val, fill, txt_col, stroke in segs:
            if val <= 0:
                continue
            pct = (val / tot) * 100.0
            sw = (pct / 100.0) * bw_tot
            st_attr = f' stroke="{stroke}" stroke-width="0.5"' if stroke else ""
            svg.append(f'<rect x="{cur_x:.2f}" y="{cy:.1f}" width="{sw:.2f}" height="{bh}" fill="{fill}"{st_attr}/>')
            if pct >= 11.5:
                svg.append(f'<text x="{cur_x + sw/2:.1f}" y="{cy + 10.7:.1f}" fill="{txt_col}" font-size="8.0" font-weight="700" text-anchor="middle">{pct:.0f}%</text>')
            cur_x += sw

        tot_str = f"{tot/1000:.1f}k" if tot >= 1000 else f"{tot}"
        svg.append(f'<text x="{x0 + bw_tot + 8}" y="{cy + 11:.1f}" fill="{lbl_col}" font-size="8.8" font-weight="600">{tot_str} ({avg_s:.1f}/s)</text>')

    svg.append(f'<line x1="{x0}" y1="{y_top}" x2="{x0}" y2="{plot_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')
    svg.append(f'<line x1="{x0}" y1="{plot_bot}" x2="{x0 + bw_tot}" y2="{plot_bot}" stroke="{C_AXIS}" stroke-width="1.2"/>')

    svg.append("</svg>")
    save_and_compile(svg, "eval-tool-calls")


if __name__ == "__main__":
    generate_bug_char()
    generate_rq2_comparison()
    generate_ablation()
    generate_tool_calls()
