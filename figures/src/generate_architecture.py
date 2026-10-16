#!/usr/bin/env python3
"""
DeFuzz System Architecture Diagram Generator (Version 3 - Perfected Alignment)
Generates an extraordinary, publication-grade vector SVG and PDF matching top security conference standards
(IEEE S&P, USENIX Security, ACM CCS, NDSS).
"""

import os
import xml.etree.ElementTree as ET

def create_defuzz_svg():
    width = 1880
    height = 1010

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    # Definitions
    svg.append('''
  <defs>
    <!-- Drop Shadows -->
    <filter id="shadow-sm" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <filter id="shadow-md" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
    <filter id="shadow-lg" x="-10%" y="-10%" width="120%" height="125%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0F172A" flood-opacity="0.12"/>
    </filter>

    <!-- Stage Background Gradients -->
    <linearGradient id="bg-stage1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>
    <linearGradient id="bg-stage2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F0FDF4"/>
    </linearGradient>
    <linearGradient id="bg-stage3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#EFF6FF"/>
    </linearGradient>

    <!-- Stage Header Gradients -->
    <linearGradient id="hdr-stage1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#312E81"/>
      <stop offset="100%" stop-color="#4338CA"/>
    </linearGradient>
    <linearGradient id="hdr-stage2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#0D9488"/>
    </linearGradient>
    <linearGradient id="hdr-stage3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="100%" stop-color="#2563EB"/>
    </linearGradient>

    <!-- Card Background Gradients -->
    <linearGradient id="card-grad-indigo" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#EEF2FF"/>
    </linearGradient>
    <linearGradient id="card-grad-teal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F0FDFA"/>
    </linearGradient>
    <linearGradient id="card-grad-blue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F0F9FF"/>
    </linearGradient>
    <linearGradient id="card-grad-amber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#FEF3C7"/>
    </linearGradient>
    <linearGradient id="card-grad-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#FAF5FF"/>
    </linearGradient>
    <linearGradient id="card-grad-rose" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#FFE4E6"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrow-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#334155"/>
    </marker>
    <marker id="arrow-indigo" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#4338CA"/>
    </marker>
    <marker id="arrow-teal" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0D9488"/>
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563EB"/>
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#7C3AED"/>
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#D97706"/>
    </marker>
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#E11D48"/>
    </marker>
    <marker id="arrow-emerald" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#059669"/>
    </marker>
  </defs>
''')

    # SVG Icon helper
    icons = {
        'book': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20M4 19.5A2.5 2.5 0 0 0 6.5 22H20V2H6.5A2.5 2.5 0 0 0 4 4.5v15z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'brain': '<path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-2.04zM14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-2.04z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'search': '<circle cx="11" cy="11" r="8" fill="none" stroke="currentColor" stroke-width="2"/><line x1="21" y1="21" x2="16.65" y2="16.65" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
        'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'shield-check': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="m9 12 2 2 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'code': '<polyline points="16 18 22 12 16 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><polyline points="8 6 2 12 8 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'git-network': '<circle cx="18" cy="6" r="3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="6" cy="6" r="3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="6" cy="18" r="3" fill="none" stroke="currentColor" stroke-width="2"/><line x1="6" y1="9" x2="6" y2="15" stroke="currentColor" stroke-width="2"/><path d="M18 9a9 9 0 0 1-9 9" fill="none" stroke="currentColor" stroke-width="2"/>',
        'cpu': '<rect x="4" y="4" width="16" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><rect x="9" y="9" width="6" height="6" fill="none" stroke="currentColor" stroke-width="2"/><line x1="9" y1="1" x2="9" y2="4" stroke="currentColor" stroke-width="2"/><line x1="15" y1="1" x2="15" y2="4" stroke="currentColor" stroke-width="2"/><line x1="9" y1="20" x2="9" y2="23" stroke="currentColor" stroke-width="2"/><line x1="15" y1="20" x2="15" y2="23" stroke="currentColor" stroke-width="2"/><line x1="20" y1="9" x2="23" y2="9" stroke="currentColor" stroke-width="2"/><line x1="20" y1="15" x2="23" y2="15" stroke="currentColor" stroke-width="2"/><line x1="1" y1="9" x2="4" y2="9" stroke="currentColor" stroke-width="2"/><line x1="1" y1="15" x2="4" y2="15" stroke="currentColor" stroke-width="2"/>',
        'tool': '<path d="m14.7 10.7 6 6a1 1 0 0 1-1.4 1.4l-6-6M4 20l6.7-6.7M15 4a6 6 0 0 0-8.5 8.5L13 19l6.5-6.5A6 6 0 0 0 15 4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'terminal': '<polyline points="4 17 10 11 4 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><line x1="12" y1="19" x2="20" y2="19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
        'sparkles': '<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3L12 3z" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'activity': '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'refresh': '<polyline points="23 4 23 10 17 10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><polyline points="1 20 1 14 7 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'bug': '<rect x="6" y="8" width="12" height="12" rx="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 2v6M4 11h4M16 11h4M4 17h4M16 17h4M7 5l3 3M17 5l-3 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
        'database': '<ellipse cx="12" cy="5" rx="9" ry="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" fill="none" stroke="currentColor" stroke-width="2"/>',
        'clock': '<circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="12 6 12 12 16 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'target': '<circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="6" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="2" fill="none" stroke="currentColor" stroke-width="2"/>',
        'layers': '<polygon points="12 2 2 7 12 12 22 7 12 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><polyline points="2 17 12 22 22 17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><polyline points="2 12 12 17 22 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
        'wand': '<path d="m15 4 4 4L8 19l-4-4L15 4zM21 2l-2 2M3 22l2-2M18 11l3-3M6 17l-3 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
    }

    def render_icon(name, x, y, size=18, color="#FFFFFF"):
        if name not in icons:
            return ""
        return f'<g transform="translate({x},{y}) scale({size/24})" color="{color}">{icons[name]}</g>'

    # ==================== MAIN HEADER ====================
    svg.append('''
  <!-- Top System Header Banner -->
  <rect x="25" y="12" width="1830" height="46" rx="8" fill="#0F172A" filter="url(#shadow-md)"/>
  <text x="45" y="41" fill="#F8FAFC" font-size="17" font-weight="700" letter-spacing="0.4">DeFuzz: Invariant-Guided Agentic Testing Framework for Compiler-Instrumented Defenses</text>
  <rect x="1485" y="23" width="345" height="24" rx="12" fill="#1E293B"/>
  <text x="1500" y="39" fill="#38BDF8" font-size="11" font-weight="600">IEEE S&amp;P / USENIX Security Architecture</text>
''')

    # Dimensions
    top_y = 70
    stage_h = 860

    # Layout Coordinates
    s1_x = 25
    s1_w = 485

    s2_x = 535
    s2_w = 555

    s3_x = 1120
    s3_w = 735

    # -------------------------------------------------------------
    # STAGE 1: INVARIANT EXTRACTION & FORMALIZATION (Offline)
    # -------------------------------------------------------------
    svg.append(f'''
  <!-- STAGE 1 CONTAINER -->
  <g id="stage-1">
    <rect x="{s1_x}" y="{top_y}" width="{s1_w}" height="{stage_h}" rx="10" fill="url(#bg-stage1)" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow-md)"/>
    <rect x="{s1_x}" y="{top_y}" width="{s1_w}" height="36" rx="10" fill="url(#hdr-stage1)"/>
    <rect x="{s1_x}" y="{top_y+24}" width="{s1_w}" height="12" fill="#4338CA"/>
    {render_icon('brain', s1_x+14, top_y+8, 20, '#FFFFFF')}
    <text x="{s1_x+42}" y="{top_y+23}" fill="#FFFFFF" font-size="13.5" font-weight="700" letter-spacing="0.3">STAGE 1: Invariant Generation (CoT &amp; RAG)</text>
    <rect x="{s1_x+370}" y="{top_y+7}" width="100" height="22" rx="11" fill="#312E81"/>
    <text x="{s1_x+382}" y="{top_y+22}" fill="#C7D2FE" font-size="10.5" font-weight="600">OFFLINE PREP</text>
''')

    # 1.1 Multi-Source Knowledge Base Card
    c1_y = top_y + 48
    svg.append(f'''
    <!-- 1.1 Knowledge Base -->
    <g transform="translate({s1_x+15}, {c1_y})">
      <rect x="0" y="0" width="455" height="126" rx="8" fill="url(#card-grad-indigo)" stroke="#C7D2FE" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="455" height="26" rx="8" fill="#E0E7FF"/>
      <rect x="0" y="16" width="455" height="10" fill="#E0E7FF"/>
      {render_icon('book', 10, 4, 17, '#4338CA')}
      <text x="34" y="18" fill="#312E81" font-size="11.5" font-weight="700">1.1 Multi-Source Defense Knowledge Base</text>
      
      <!-- Items -->
      <g transform="translate(10, 34)">
        <rect x="0" y="0" width="435" height="25" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
        {render_icon('code', 8, 5, 14, '#6366F1')}
        <text x="28" y="17" fill="#1E293B" font-size="10.5" font-weight="600">Compiler Sources:</text>
        <text x="135" y="17" fill="#475569" font-size="10.5">Pass comments, layout asserts, backend macros</text>
      </g>
      <g transform="translate(10, 64)">
        <rect x="0" y="0" width="435" height="25" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
        {render_icon('layers', 8, 5, 14, '#0D9488')}
        <text x="28" y="17" fill="#1E293B" font-size="10.5" font-weight="600">Arch &amp; ABI Specs:</text>
        <text x="142" y="17" fill="#475569" font-size="10.5">ARM AAPCS, SysV ABI, ShadowStack, CET/PAC</text>
      </g>
      <g transform="translate(10, 94)">
        <rect x="0" y="0" width="435" height="25" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
        {render_icon('bug', 8, 5, 14, '#E11D48')}
        <text x="28" y="17" fill="#1E293B" font-size="10.5" font-weight="600">Bug Corpus &amp; Patches:</text>
        <text x="160" y="17" fill="#475569" font-size="10.5">CVE-2023-4039, GCC PR-96191, LLVM PRs</text>
      </g>
    </g>
''')

    # Arrow 1.1 -> 1.2
    svg.append(f'''
    <path d="M {s1_x+242} {c1_y+126} L {s1_x+242} {c1_y+152}" fill="none" stroke="#6366F1" stroke-width="2" marker-end="url(#arrow-indigo)"/>
    <rect x="{s1_x+182}" y="{c1_y+132}" width="120" height="16" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="{s1_x+192}" y="{c1_y+144}" fill="#4338CA" font-size="9.5" font-weight="600">Raw Corpus Streams</text>
''')

    # 1.2 Dual-Track Reasoning Engine (CoT + RAG)
    c2_y = c1_y + 156
    svg.append(f'''
    <!-- 1.2 Dual-Track Reasoning Engine -->
    <g transform="translate({s1_x+15}, {c2_y})">
      <rect x="0" y="0" width="455" height="225" rx="8" fill="url(#card-grad-indigo)" stroke="#C7D2FE" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="455" height="26" rx="8" fill="#E0E7FF"/>
      <rect x="0" y="16" width="455" height="10" fill="#E0E7FF"/>
      {render_icon('sparkles', 10, 4, 17, '#4338CA')}
      <text x="34" y="18" fill="#312E81" font-size="11.5" font-weight="700">1.2 Dual-Track Invariant Mining Engine</text>

      <!-- Track A: Segmented CoT -->
      <g transform="translate(10, 34)">
        <rect x="0" y="0" width="210" height="180" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
        <rect x="0" y="0" width="210" height="22" rx="6" fill="#EEF2FF"/>
        <text x="8" y="15" fill="#3730A3" font-size="10.5" font-weight="700">Track A: Segmented CoT</text>
        <text x="8" y="36" fill="#1E293B" font-size="9.5" font-weight="600">Pass-by-Pass Decomposition</text>
        <text x="8" y="52" fill="#64748B" font-size="9">• Semantic partitioning</text>
        <text x="8" y="66" fill="#64748B" font-size="9">• Isolate protected assets</text>
        <text x="8" y="80" fill="#64748B" font-size="9">• Extract canary/CFI preconds</text>
        <rect x="6" y="94" width="198" height="76" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="108" fill="#475569" font-size="8.5" font-weight="700">Prompting Focus:</text>
        <text x="10" y="122" fill="#64748B" font-size="8.5">"Derive boundary invariants</text>
        <text x="10" y="134" fill="#64748B" font-size="8.5">for dynamic stack frames</text>
        <text x="10" y="146" fill="#64748B" font-size="8.5">under alloca &amp; VLAs"</text>
      </g>

      <!-- Track B: Historical-Bug RAG -->
      <g transform="translate(235, 34)">
        <rect x="0" y="0" width="210" height="180" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
        <rect x="0" y="0" width="210" height="22" rx="6" fill="#EEF2FF"/>
        <text x="8" y="15" fill="#3730A3" font-size="10.5" font-weight="700">Track B: Historical-Bug RAG</text>
        <text x="8" y="36" fill="#1E293B" font-size="9.5" font-weight="600">Cross-Mechanism Transfer</text>
        <text x="8" y="52" fill="#64748B" font-size="9">• Root-cause distillation</text>
        <text x="8" y="66" fill="#64748B" font-size="9">• Dense + Sparse BM25 RAG</text>
        <text x="8" y="80" fill="#64748B" font-size="9">• Isomorphic defect retrieval</text>
        <rect x="6" y="94" width="198" height="76" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
        <text x="10" y="108" fill="#475569" font-size="8.5" font-weight="700">Hybrid Query Probes:</text>
        <text x="10" y="122" fill="#64748B" font-size="8.5">Dense: Abstract bypass pattern</text>
        <text x="10" y="134" fill="#64748B" font-size="8.5">Sparse: critical_tokens</text>
        <text x="10" y="146" fill="#64748B" font-size="8.5">(e.g., ix86_zero_call_used)</text>
      </g>
    </g>
''')

    # Arrow 1.2 -> 1.3
    svg.append(f'''
    <path d="M {s1_x+242} {c2_y+225} L {s1_x+242} {c2_y+252}" fill="none" stroke="#6366F1" stroke-width="2" marker-end="url(#arrow-indigo)"/>
    <rect x="{s1_x+177}" y="{c2_y+232}" width="130" height="16" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="{s1_x+187}" y="{c2_y+244}" fill="#4338CA" font-size="9.5" font-weight="600">Candidate Invariants</text>
''')

    # 1.3 Grounding & Novelty Gate
    c3_y = c2_y + 256
    svg.append(f'''
    <!-- 1.3 Grounding Gate -->
    <g transform="translate({s1_x+15}, {c3_y})">
      <rect x="0" y="0" width="455" height="90" rx="8" fill="url(#card-grad-indigo)" stroke="#C7D2FE" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="455" height="26" rx="8" fill="#E0E7FF"/>
      <rect x="0" y="16" width="455" height="10" fill="#E0E7FF"/>
      {render_icon('shield-check', 10, 4, 17, '#4338CA')}
      <text x="34" y="18" fill="#312E81" font-size="11.5" font-weight="700">1.3 Grounding &amp; Novelty Verification Gate</text>
      
      <g transform="translate(10, 32)">
        <rect x="0" y="0" width="210" height="48" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
        <text x="8" y="17" fill="#1E293B" font-size="10" font-weight="600">Evidence Grounding</text>
        <text x="8" y="33" fill="#64748B" font-size="9">Validates source AST anchors &amp; ABI</text>
      </g>
      <g transform="translate(235, 32)">
        <rect x="0" y="0" width="210" height="48" rx="4" fill="#FFFFFF" stroke="#CBD5E1"/>
        <text x="8" y="17" fill="#1E293B" font-size="10" font-weight="600">Deduplication &amp; Novelty</text>
        <text x="8" y="33" fill="#64748B" font-size="9">Embedding similarity threshold &gt; 85%</text>
      </g>
    </g>
''')

    # Arrow 1.3 -> 1.4
    svg.append(f'''
    <path d="M {s1_x+242} {c3_y+90} L {s1_x+242} {c3_y+116}" fill="none" stroke="#6366F1" stroke-width="2" marker-end="url(#arrow-indigo)"/>
    <rect x="{s1_x+167}" y="{c3_y+96}" width="150" height="16" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="{s1_x+175}" y="{c3_y+108}" fill="#4338CA" font-size="9.5" font-weight="600">Grounded Formal Invariants</text>
''')

    # 1.4 Formal Invariant Catalog (Output of Stage 1)
    c4_y = c3_y + 120
    svg.append(f'''
    <!-- 1.4 Formal Invariant Catalog -->
    <g transform="translate({s1_x+15}, {c4_y})">
      <rect x="0" y="0" width="455" height="185" rx="8" fill="#1E1B4B" stroke="#4338CA" stroke-width="1.5" filter="url(#shadow-md)"/>
      <rect x="0" y="0" width="455" height="26" rx="8" fill="#312E81"/>
      <rect x="0" y="16" width="455" height="10" fill="#312E81"/>
      {render_icon('database', 10, 4, 17, '#A5B4FC')}
      <text x="34" y="18" fill="#F8FAFC" font-size="11.5" font-weight="700">Security Invariant Catalog (N Invariants / Defense)</text>
      <rect x="370" y="4" width="75" height="18" rx="9" fill="#4338CA"/>
      <text x="380" y="16" fill="#E0E7FF" font-size="9.5" font-weight="600">SCHEMA v2</text>

      <!-- Code Snippet Display -->
      <g transform="translate(10, 32)">
        <rect x="0" y="0" width="435" height="142" rx="4" fill="#0F172A" stroke="#334155"/>
        <text x="10" y="18" fill="#38BDF8" font-family="monospace" font-size="9.5">invariant_id: <tspan fill="#FDE047">"INV-SP-L02"</tspan> <tspan fill="#64748B"># Stack Protector</tspan></text>
        <text x="10" y="34" fill="#38BDF8" font-family="monospace" font-size="9.5">mechanism:    <tspan fill="#FDE047">"stack-protector-vla-boundary"</tspan></text>
        <text x="10" y="50" fill="#38BDF8" font-family="monospace" font-size="9.5">pipeline_scope: <tspan fill="#FDE047">"BACKEND_FRAME_LOWERING"</tspan></text>
        <text x="10" y="66" fill="#38BDF8" font-family="monospace" font-size="9.5">statement:    <tspan fill="#A5B4FC">"VLA buffer must NOT precede canary in stack frame"</tspan></text>
        <text x="10" y="82" fill="#38BDF8" font-family="monospace" font-size="9.5">semantic_assert: <tspan fill="#4ADE80">"frame.locals_offset &lt; frame.canary_offset"</tspan></text>
        <text x="10" y="98" fill="#38BDF8" font-family="monospace" font-size="9.5">observation:  <tspan fill="#F472B6">"Canary untouched on dynamic VLA overflow"</tspan></text>
        <text x="10" y="114" fill="#38BDF8" font-family="monospace" font-size="9.5">target_isas:   <tspan fill="#94A3B8">["x86_64", "aarch64", "riscv64", "armv7"]</tspan></text>
        <text x="10" y="130" fill="#64748B" font-family="monospace" font-size="8.5">source_anchors: ["gcc/config/aarch64/aarch64.cc:6912-6915"]</text>
      </g>
    </g>
  </g>
''')

    # -------------------------------------------------------------
    # STAGE 2: CODE MAPPING, LOGGING & MULTI-ISA ORACLE SYNTHESIS
    # -------------------------------------------------------------
    svg.append(f'''
  <!-- STAGE 2 CONTAINER -->
  <g id="stage-2">
    <rect x="{s2_x}" y="{top_y}" width="{s2_w}" height="{stage_h}" rx="10" fill="url(#bg-stage2)" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow-md)"/>
    <rect x="{s2_x}" y="{top_y}" width="{s2_w}" height="36" rx="10" fill="url(#hdr-stage2)"/>
    <rect x="{s2_x}" y="{top_y+24}" width="{s2_w}" height="12" fill="#0D9488"/>
    {render_icon('tool', s2_x+14, top_y+8, 20, '#FFFFFF')}
    <text x="{s2_x+42}" y="{top_y+23}" fill="#FFFFFF" font-size="13.5" font-weight="700" letter-spacing="0.3">STAGE 2: Code Mapping, Logging &amp; Oracle Synthesis</text>
    <rect x="{s2_x+435}" y="{top_y+7}" width="105" height="22" rx="11" fill="#134E4A"/>
    <text x="{s2_x+445}" y="{top_y+22}" fill="#99F6E4" font-size="10.5" font-weight="600">BRIDGE &amp; ORACLE</text>
''')

    # 2.1 Autonomous Agent & 3-Level Codebase Mapping
    c21_y = top_y + 48
    svg.append(f'''
    <!-- 2.1 Autonomous Codebase Mapping -->
    <g transform="translate({s2_x+15}, {c21_y})">
      <rect x="0" y="0" width="525" height="275" rx="8" fill="url(#card-grad-teal)" stroke="#99F6E4" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="525" height="26" rx="8" fill="#CCFBF1"/>
      <rect x="0" y="16" width="525" height="10" fill="#CCFBF1"/>
      {render_icon('git-network', 10, 4, 17, '#0F766E')}
      <text x="34" y="18" fill="#134E4A" font-size="11.5" font-weight="700">2.1 Invariant-to-Source Mapping (Free Agent + MCP Tools)</text>
      
      <!-- Autonomous Agent Banner -->
      <g transform="translate(10, 32)">
        <rect x="0" y="0" width="505" height="28" rx="4" fill="#0F766E"/>
        {render_icon('terminal', 8, 5, 16, '#5EEAD4')}
        <text x="30" y="18" fill="#FFFFFF" font-size="10.5" font-weight="700">Autonomous Free Agent (Claude Code / Codebase Navigator)</text>
        <rect x="345" y="4" width="152" height="20" rx="10" fill="#134E4A"/>
        <text x="355" y="17" fill="#99F6E4" font-size="9" font-weight="600">MCP Tools &amp; Call-Graph</text>
      </g>

      <!-- Tool & MCP Row -->
      <g transform="translate(10, 66)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="161" height="34" rx="4" fill="#FFFFFF" stroke="#99F6E4"/>
          <text x="8" y="14" fill="#0F766E" font-size="9.5" font-weight="700">CodeQL Database</text>
          <text x="8" y="27" fill="#64748B" font-size="8.5">Global AST &amp; Virtual Calls</text>
        </g>
        <g transform="translate(171, 0)">
          <rect x="0" y="0" width="161" height="34" rx="4" fill="#FFFFFF" stroke="#99F6E4"/>
          <text x="8" y="14" fill="#0F766E" font-size="9.5" font-weight="700">Compiler IPA Dumps</text>
          <text x="8" y="27" fill="#64748B" font-size="8.5">GCC cgraph / LLVM opt dot</text>
        </g>
        <g transform="translate(342, 0)">
          <rect x="0" y="0" width="163" height="34" rx="4" fill="#FFFFFF" stroke="#99F6E4"/>
          <text x="8" y="14" fill="#0F766E" font-size="9.5" font-weight="700">File &amp; AST Navigators</text>
          <text x="8" y="27" fill="#64748B" font-size="8.5">Precision line_range tools</text>
        </g>
      </g>

      <!-- 3-Level Mapping Hierarchy Box -->
      <g transform="translate(10, 108)">
        <rect x="0" y="0" width="505" height="156" rx="5" fill="#F8FAFC" stroke="#CBD5E1"/>
        
        <!-- Level 1 -->
        <g transform="translate(8, 6)">
          <rect x="0" y="0" width="489" height="42" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
          <rect x="6" y="6" width="68" height="30" rx="3" fill="#E0F2FE"/>
          <text x="14" y="25" fill="#0369A1" font-size="10" font-weight="700">Level 1</text>
          <text x="82" y="18" fill="#1E293B" font-size="10.5" font-weight="600">Pipeline Scope &amp; Target Pass</text>
          <text x="82" y="32" fill="#64748B" font-size="9">pass_thread_prologue_and_epilogue (gcc/config/aarch64/aarch64.cc)</text>
        </g>

        <!-- Level 2 -->
        <g transform="translate(8, 52)">
          <rect x="0" y="0" width="489" height="48" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
          <rect x="6" y="6" width="68" height="36" rx="3" fill="#F0FDFA"/>
          <text x="14" y="28" fill="#0F766E" font-size="10" font-weight="700">Level 2</text>
          <text x="82" y="18" fill="#1E293B" font-size="10.5" font-weight="600">Function Cluster (Deep Call Stack Penetration)</text>
          <text x="82" y="33" fill="#64748B" font-size="9">aarch64_layout_frame (d=0) → assign_stack_local_1 (depth=6) → prologue_emit</text>
        </g>

        <!-- Level 3 -->
        <g transform="translate(8, 104)">
          <rect x="0" y="0" width="489" height="44" rx="4" fill="#FFFFFF" stroke="#E2E8F0"/>
          <rect x="6" y="6" width="68" height="32" rx="3" fill="#FEF3C7"/>
          <text x="14" y="26" fill="#B45309" font-size="10" font-weight="700">Level 3</text>
          <text x="82" y="18" fill="#1E293B" font-size="10.5" font-weight="600">Semantic Anchors &amp; Conditions</text>
          <text x="82" y="32" fill="#64748B" font-size="9">struct aarch64_frame.canary_offset | frame.locals_offset &lt; canary_offset</text>
        </g>
      </g>
    </g>
''')

    # 2.2 Targeted Log Instrumentation & Rebuild
    c22_y = c21_y + 288
    svg.append(f'''
    <!-- 2.2 Targeted Log Instrumentation & Rebuild -->
    <g transform="translate({s2_x+15}, {c22_y})">
      <rect x="0" y="0" width="525" height="152" rx="8" fill="url(#card-grad-teal)" stroke="#99F6E4" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="525" height="26" rx="8" fill="#CCFBF1"/>
      <rect x="0" y="16" width="525" height="10" fill="#CCFBF1"/>
      {render_icon('wand', 10, 4, 17, '#0F766E')}
      <text x="34" y="18" fill="#134E4A" font-size="11.5" font-weight="700">2.2 Targeted Log Instrumentation &amp; Compiler Rebuild</text>
      
      <!-- Content -->
      <g transform="translate(10, 32)">
        <rect x="0" y="0" width="505" height="52" rx="4" fill="#0F172A" stroke="#334155"/>
        <text x="8" y="15" fill="#F8FAFC" font-size="9.5" font-weight="600">Unique-ID Log Injection at Critical Anchors:</text>
        <text x="8" y="30" fill="#38BDF8" font-family="monospace" font-size="8.5">fprintf(stderr, "[INV-LOG-SP02] frame_sz=%ld canary_off=%ld\\n", ...);</text>
        <text x="8" y="44" fill="#4ADE80" font-family="monospace" font-size="8.5">if (cfun-&gt;calls_alloca) fprintf(stderr, "[INV-LOG-SP02-ALLOCA] hit\\n");</text>
      </g>
      <g transform="translate(10, 90)">
        <rect x="0" y="0" width="505" height="50" rx="4" fill="#FFFFFF" stroke="#99F6E4"/>
        <text x="10" y="18" fill="#134E4A" font-size="10.5" font-weight="700">Automated Fast Toolchain Recompilation:</text>
        <text x="10" y="36" fill="#475569" font-size="9.5">Builds Patched Target Compiler → <tspan font-weight="700" fill="#0F766E">Instrumented GCC / LLVM</tspan> (Emits execution traces)</text>
      </g>
    </g>
''')

    # Arrow 2.1 -> 2.2
    svg.append(f'''
    <path d="M {s2_x+277} {c21_y+275} L {s2_x+277} {c22_y}" fill="none" stroke="#0D9488" stroke-width="2" marker-end="url(#arrow-teal)"/>
''')

    # 2.3 Multi-ISA Oracle Synthesis & Tier 1 Grounding Gate
    c23_y = c22_y + 164
    svg.append(f'''
    <!-- 2.3 Multi-ISA Oracle Synthesis -->
    <g transform="translate({s2_x+15}, {c23_y})">
      <rect x="0" y="0" width="525" height="235" rx="8" fill="url(#card-grad-amber)" stroke="#FDE68A" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="525" height="26" rx="8" fill="#FEF3C7"/>
      <rect x="0" y="16" width="525" height="10" fill="#FEF3C7"/>
      {render_icon('shield', 10, 4, 17, '#B45309')}
      <text x="34" y="18" fill="#78350F" font-size="11.5" font-weight="700">2.3 Multi-ISA Oracle Synthesis &amp; Baseline Gate (Tier 1)</text>

      <!-- Multi-ISA Checkers Split -->
      <g transform="translate(10, 32)">
        <!-- Static Checkers Column -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="248" height="126" rx="5" fill="#FFFFFF" stroke="#FDE68A"/>
          <rect x="0" y="0" width="248" height="22" rx="5" fill="#FFFBEB"/>
          <text x="8" y="15" fill="#92400E" font-size="10" font-weight="700">Static Checkers (Binary &amp; ELF)</text>
          <text x="8" y="34" fill="#1E293B" font-size="9" font-weight="600">• ELF .dynsym &amp; Relocation Audit</text>
          <text x="8" y="48" fill="#64748B" font-size="8.5">  Symbol lookup (__stack_chk_fail)</text>
          <text x="8" y="64" fill="#1E293B" font-size="9" font-weight="600">• Disassembly Pattern Matching</text>
          <text x="8" y="78" fill="#64748B" font-size="8.5">  Prologue/epilogue canary setup</text>
          <text x="8" y="94" fill="#1E293B" font-size="9" font-weight="600">• Shadow Stack &amp; IBT Opcode</text>
          <text x="8" y="108" fill="#64748B" font-size="8.5">  endbr64, bti c, paciasp verification</text>
        </g>

        <!-- Dynamic Checkers Column -->
        <g transform="translate(257, 0)">
          <rect x="0" y="0" width="248" height="126" rx="5" fill="#FFFFFF" stroke="#FDE68A"/>
          <rect x="0" y="0" width="248" height="22" rx="5" fill="#FFFBEB"/>
          <text x="8" y="15" fill="#92400E" font-size="10" font-weight="700">Dynamic Checkers (Runtime Oracle)</text>
          <text x="8" y="34" fill="#1E293B" font-size="9" font-weight="600">• Memory Canary Corruption Probe</text>
          <text x="8" y="48" fill="#64748B" font-size="8.5">  VLA overwrite vs. __stack_chk_fail</text>
          <text x="8" y="64" fill="#1E293B" font-size="9" font-weight="600">• Register &amp; Signal State Oracle</text>
          <text x="8" y="78" fill="#64748B" font-size="8.5">  SIGSEGV vs. SIGILL trap checking</text>
          <text x="8" y="94" fill="#1E293B" font-size="9" font-weight="600">• Execution Exit &amp; Clobber Audit</text>
          <text x="8" y="108" fill="#64748B" font-size="8.5">  Verify return address tamper trap</text>
        </g>
      </g>

      <!-- Tier 1 Grounding Gate Banner -->
      <g transform="translate(10, 168)">
        <rect x="0" y="0" width="505" height="54" rx="5" fill="#FEF2F2" stroke="#F87171" stroke-width="1.2"/>
        {render_icon('shield-check', 10, 15, 20, '#DC2626')}
        <text x="36" y="21" fill="#991B1B" font-size="10.5" font-weight="700">Tier 1 Offline Grounding Gate (Regression Gate)</text>
        <text x="36" y="35" fill="#7F1D1D" font-size="9">Pre-validates synthesized checkers on Canonical Positive &amp; Negative Baselines</text>
        <text x="36" y="47" fill="#B91C1C" font-size="8.5" font-weight="600">Zero Goalpost Moving Guarantee • Prevents faulty oracles entering fuzz loop</text>
      </g>
    </g>
  </g>
''')

    # Inter-Stage Connectors (Stage 1 Catalog -> Stage 2) via Vertical Gutter
    # Gutter 1-2 is between s1_x+s1_w (510) and s2_x (535). Gutter center = 522.
    svg.append(f'''
    <!-- Inter-Stage Connections from Invariant Catalog into Stage 2 via Gutter -->
    <!-- Catalog -> 2.1 Mapping -->
    <path d="M {s1_x+470} {c4_y+50} H 522 V {c21_y+48} H {s2_x+15}" fill="none" stroke="#4338CA" stroke-width="2" marker-end="url(#arrow-indigo)"/>
    <rect x="485" y="{c21_y+58}" width="68" height="16" rx="8" fill="#EEF2FF" stroke="#C7D2FE" stroke-width="1"/>
    <text x="491" y="{c21_y+70}" fill="#4338CA" font-size="8.5" font-weight="600">Invariants</text>

    <!-- Catalog -> 2.3 Oracles -->
    <path d="M {s1_x+470} {c4_y+95} H 522 V {c23_y+50} H {s2_x+15}" fill="none" stroke="#4338CA" stroke-width="2" marker-end="url(#arrow-indigo)"/>
''')

    # -------------------------------------------------------------
    # STAGE 3: INVARIANT-GUIDED AGENTIC FUZZING & ADAPTIVE FEEDBACK
    # -------------------------------------------------------------
    svg.append(f'''
  <!-- STAGE 3 CONTAINER -->
  <g id="stage-3">
    <rect x="{s3_x}" y="{top_y}" width="{s3_w}" height="{stage_h}" rx="10" fill="url(#bg-stage3)" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow-md)"/>
    <rect x="{s3_x}" y="{top_y}" width="{s3_w}" height="36" rx="10" fill="url(#hdr-stage3)"/>
    <rect x="{s3_x}" y="{top_y+24}" width="{s3_w}" height="12" fill="#2563EB"/>
    {render_icon('refresh', s3_x+14, top_y+8, 20, '#FFFFFF')}
    <text x="{s3_x+42}" y="{top_y+23}" fill="#FFFFFF" font-size="13.5" font-weight="700" letter-spacing="0.3">STAGE 3: Invariant-Guided Agentic Fuzzing &amp; Adaptive Feedback Loop</text>
    <rect x="{s3_x+615}" y="{top_y+7}" width="105" height="22" rx="11" fill="#1E3A8A"/>
    <text x="{s3_x+625}" y="{top_y+22}" fill="#BFDBFE" font-size="10.5" font-weight="600">ONLINE LOOP</text>
''')

    # 3.1 Fixed-Budget Invariant Scheduler
    c31_y = top_y + 48
    svg.append(f'''
    <!-- 3.1 Fixed-Budget Invariant Scheduler -->
    <g transform="translate({s3_x+15}, {c31_y})">
      <rect x="0" y="0" width="705" height="48" rx="6" fill="#1E293B" stroke="#334155" stroke-width="1.2" filter="url(#shadow-sm)"/>
      {render_icon('clock', 12, 14, 20, '#38BDF8')}
      <text x="40" y="20" fill="#F8FAFC" font-size="11" font-weight="700">Target Invariant Scheduler (Equal Time Budget T_inv per Invariant)</text>
      <text x="40" y="37" fill="#94A3B8" font-size="9.5">Locks 1 Invariant (I_k) + Multi-ISA Checker Suite • Round-robin queue • Ensures equal exploration depth</text>
      <rect x="595" y="12" width="98" height="24" rx="12" fill="#0369A1"/>
      <text x="605" y="28" fill="#E0F2FE" font-size="10" font-weight="700">T_inv = const</text>
    </g>
''')

    # 3.2 PBT-Aware Seed Generator Agent
    c32_y = c31_y + 56
    svg.append(f'''
    <!-- 3.2 PBT-Aware Seed Generator Agent -->
    <g transform="translate({s3_x+15}, {c32_y})">
      <rect x="0" y="0" width="705" height="154" rx="8" fill="url(#card-grad-blue)" stroke="#93C5FD" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="705" height="26" rx="8" fill="#DBEAFE"/>
      <rect x="0" y="16" width="705" height="10" fill="#DBEAFE"/>
      {render_icon('brain', 10, 4, 17, '#1D4ED8')}
      <text x="34" y="18" fill="#1E3A8A" font-size="11.5" font-weight="700">3.2 Generator Agent (Defense &amp; Checker-Aware C/C++ Synthesis)</text>
      <rect x="565" y="4" width="130" height="18" rx="9" fill="#1D4ED8"/>
      <text x="575" y="16" fill="#EFF6FF" font-size="9.5" font-weight="600">PBT HARNESS GEN</text>

      <!-- 3 Columns of PBT Generator Features -->
      <g transform="translate(10, 32)">
        <!-- PBT Feature 1 -->
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="222" height="112" rx="5" fill="#FFFFFF" stroke="#BFDBFE"/>
          <text x="8" y="16" fill="#1E3A8A" font-size="9.5" font-weight="700">1. Macro Switch Matrix (-D)</text>
          <text x="8" y="32" fill="#64748B" font-size="8">#ifndef BUF_SZ</text>
          <text x="8" y="44" fill="#64748B" font-size="8">#define BUF_SZ 64</text>
          <text x="8" y="56" fill="#64748B" font-size="8">#endif</text>
          <text x="8" y="72" fill="#1E293B" font-size="8.5">Injects -DBUF_SZ=... for</text>
          <text x="8" y="86" fill="#1E293B" font-size="8.5">dynamic parameter sweep</text>
          <text x="8" y="100" fill="#2563EB" font-size="8" font-weight="600">Checker-aware layout</text>
        </g>

        <!-- PBT Feature 2 -->
        <g transform="translate(232, 0)">
          <rect x="0" y="0" width="222" height="112" rx="5" fill="#FFFFFF" stroke="#BFDBFE"/>
          <text x="8" y="16" fill="#1E3A8A" font-size="9.5" font-weight="700">2. Anti-Optimization Barrier</text>
          <text x="8" y="32" fill="#64748B" font-size="8">asm volatile("" : "+m"(buf)</text>
          <text x="8" y="44" fill="#64748B" font-size="8">             : : "memory");</text>
          <text x="8" y="56" fill="#64748B" font-size="8">volatile sink = buf;</text>
          <text x="8" y="72" fill="#1E293B" font-size="8.5">Prevents middle-end SRA /</text>
          <text x="8" y="86" fill="#1E293B" font-size="8.5">DCE silent elimination</text>
          <text x="8" y="100" fill="#0D9488" font-size="8" font-weight="600">Forces stack frame entry</text>
        </g>

        <!-- PBT Feature 3 -->
        <g transform="translate(464, 0)">
          <rect x="0" y="0" width="221" height="112" rx="5" fill="#FFFFFF" stroke="#BFDBFE"/>
          <text x="8" y="16" fill="#1E3A8A" font-size="9.5" font-weight="700">3. Dynamic Probe Interface</text>
          <text x="8" y="32" fill="#64748B" font-size="8">int main(int argc, char**v) {{</text>
          <text x="8" y="44" fill="#64748B" font-size="8">  sz = atoll(v[1]);</text>
          <text x="8" y="56" fill="#64748B" font-size="8">  probe = atoll(v[2]);</text>
          <text x="8" y="72" fill="#1E293B" font-size="8.5">Enables runtime binary</text>
          <text x="8" y="86" fill="#1E293B" font-size="8.5">binary search &amp; fuzz probes</text>
          <text x="8" y="100" fill="#B45309" font-size="8" font-weight="600">Dynamic Oracle Driven</text>
        </g>
      </g>
    </g>
''')

    # Arrow 3.1 -> 3.2
    svg.append(f'''
    <path d="M {s3_x+367} {c31_y+48} L {s3_x+367} {c32_y}" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow-blue)"/>
''')

    # 3.3 Instrumented Compiler Execution & Diagnostic Extractor
    c33_y = c32_y + 162
    svg.append(f'''
    <!-- 3.3 Instrumented Compiler Execution Engine -->
    <g transform="translate({s3_x+15}, {c33_y})">
      <rect x="0" y="0" width="705" height="142" rx="8" fill="url(#card-grad-blue)" stroke="#93C5FD" stroke-width="1.2" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="705" height="26" rx="8" fill="#DBEAFE"/>
      <rect x="0" y="16" width="705" height="10" fill="#DBEAFE"/>
      {render_icon('cpu', 10, 4, 17, '#1D4ED8')}
      <text x="34" y="18" fill="#1E3A8A" font-size="11.5" font-weight="700">3.3 Instrumented Compiler Execution &amp; Diagnostic Pipeline</text>
      
      <!-- Inside Pipeline Flow -->
      <g transform="translate(10, 32)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="255" height="98" rx="5" fill="#FFFFFF" stroke="#93C5FD"/>
          <text x="8" y="18" fill="#0F172A" font-size="10" font-weight="700">Target Compiler Build</text>
          <text x="8" y="34" fill="#475569" font-size="8.5">• GCC: -fstack-protector-strong</text>
          <text x="8" y="48" fill="#475569" font-size="8.5">• LLVM: -fsanitize=safe-stack, cfi</text>
          <text x="8" y="62" fill="#475569" font-size="8.5">• Multi-ISA cross compile</text>
          <rect x="8" y="74" width="239" height="16" rx="3" fill="#EFF6FF"/>
          <text x="12" y="86" fill="#1D4ED8" font-size="8.5" font-weight="700">Outputs: Executable Binaries + ASM</text>
        </g>

        <g transform="translate(265, 0)">
          <rect x="0" y="0" width="420" height="98" rx="5" fill="#0F172A" stroke="#334155"/>
          <text x="10" y="18" fill="#38BDF8" font-size="10" font-weight="700">Diagnostic Stream &amp; Log Capture (MCP):</text>
          <text x="10" y="35" fill="#94A3B8" font-size="8.5">• Stack usage dump: <tspan fill="#FDE047">-fstack-usage / .stack_sizes</tspan></text>
          <text x="10" y="50" fill="#94A3B8" font-size="8.5">• Optimization reports: <tspan fill="#FDE047">-fopt-info-missed / -Rpass-missed</tspan></text>
          <text x="10" y="65" fill="#94A3B8" font-size="8.5">• Middle-end dump: <tspan fill="#FDE047">GIMPLE/RTL / LLVM IR print-after-all</tspan></text>
          <text x="10" y="80" fill="#4ADE80" font-family="monospace" font-size="8.5">• Hit logs: "[INV-LOG-SP02] layout_frame called, VLA=yes"</text>
        </g>
      </g>
    </g>
''')

    # Arrow 3.2 -> 3.3
    svg.append(f'''
    <path d="M {s3_x+367} {c32_y+154} L {s3_x+367} {c33_y}" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow-blue)"/>
    <rect x="{s3_x+287}" y="{c32_y+154}" width="160" height="16" rx="8" fill="#DBEAFE" stroke="#93C5FD" stroke-width="1"/>
    <text x="{s3_x+297}" y="{c32_y+166}" fill="#1E3A8A" font-size="9" font-weight="600">Parameterized C/C++ Seeds</text>
''')

    # Arrow from Stage 2 Compiler into 3.3 (Horizontal through gutter 2-3)
    svg.append(f'''
    <path d="M {s2_x+540} {c22_y+115} H {s3_x+15}" fill="none" stroke="#0D9488" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrow-teal)"/>
    <rect x="{s2_x+535}" y="{c22_y+106}" width="80" height="16" rx="8" fill="#F0FDFA" stroke="#99F6E4" stroke-width="1"/>
    <text x="{s2_x+540}" y="{c22_y+118}" fill="#0F766E" font-size="8.5" font-weight="600">Patched Binary</text>
''')

    # 3.4 Oracle Evaluation & Branch Decision
    c34_y = c33_y + 152
    svg.append(f'''
    <!-- 3.4 Oracle Evaluation Point -->
    <g transform="translate({s3_x+15}, {c34_y})">
      <rect x="0" y="0" width="705" height="96" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="705" height="26" rx="8" fill="#F1F5F9"/>
      <rect x="0" y="16" width="705" height="10" fill="#F1F5F9"/>
      {render_icon('target', 10, 4, 17, '#334155')}
      <text x="34" y="18" fill="#0F172A" font-size="11.5" font-weight="700">3.4 Multi-ISA Checker Oracle Adjudication (Static &amp; Dynamic Check)</text>

      <!-- Decision Split -->
      <g transform="translate(10, 32)">
        <g transform="translate(0, 0)">
          <rect x="0" y="0" width="335" height="54" rx="4" fill="#FFF1F2" stroke="#FDA4AF"/>
          <text x="8" y="18" fill="#E11D48" font-size="10.5" font-weight="700">FAIL (Invariant Violation Detected!)</text>
          <text x="8" y="34" fill="#9F1239" font-size="9">• Canary bypassed / layout inverted / CFI missing</text>
          <text x="8" y="47" fill="#BE123C" font-size="8.5" font-weight="600">→ Enters Lateral Diversification Engine</text>
        </g>

        <g transform="translate(350, 0)">
          <rect x="0" y="0" width="335" height="54" rx="4" fill="#F5F3FF" stroke="#DDD6FE"/>
          <text x="8" y="18" fill="#7C3AED" font-size="10.5" font-weight="700">PASS / NOT_APPLICABLE / ERROR</text>
          <text x="8" y="34" fill="#5B21B6" font-size="9">• Defense intact OR optimization elimination</text>
          <text x="8" y="47" fill="#6D28D9" font-size="8.5" font-weight="600">→ Enters Feedback Agent &amp; Diagnostics Loop</text>
        </g>
      </g>
    </g>
''')

    # Arrow from Stage 2 Checkers into 3.4
    svg.append(f'''
    <path d="M {s2_x+540} {c23_y+50} H {s3_x+15}" fill="none" stroke="#D97706" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrow-amber)"/>
    <rect x="{s2_x+538}" y="{c23_y+41}" width="75" height="16" rx="8" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1"/>
    <text x="{s2_x+543}" y="{c23_y+53}" fill="#B45309" font-size="8.5" font-weight="600">ISA Oracles</text>
''')

    # Arrow 3.3 -> 3.4
    svg.append(f'''
    <path d="M {s3_x+367} {c33_y+142} L {s3_x+367} {c34_y}" fill="none" stroke="#2563EB" stroke-width="2" marker-end="url(#arrow-blue)"/>
''')

    # 3.5 Lateral Diversification & PoC Minimization (LEFT BRANCH under 3.4)
    # 3.6 Diagnostic Feedback & Checker Refinement (RIGHT BRANCH under 3.4)
    c35_y = c34_y + 108
    svg.append(f'''
    <!-- 3.5 Lateral Diversification (Bug Discovery Path) -->
    <g transform="translate({s3_x+15}, {c35_y})">
      <rect x="0" y="0" width="335" height="260" rx="8" fill="url(#card-grad-rose)" stroke="#FDA4AF" stroke-width="1.5" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="335" height="26" rx="8" fill="#FFE4E6"/>
      <rect x="0" y="16" width="335" height="10" fill="#FFE4E6"/>
      {render_icon('bug', 8, 4, 16, '#BE123C')}
      <text x="30" y="18" fill="#881337" font-size="11" font-weight="700">3.5 Lateral Diversification &amp; PoC</text>

      <g transform="translate(8, 34)">
        <!-- Lateral Thinking Guidance Box -->
        <rect x="0" y="0" width="319" height="72" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
        <text x="8" y="17" fill="#9F1239" font-size="9.5" font-weight="700">Divergent / Lateral Thinking:</text>
        <text x="8" y="33" fill="#475569" font-size="8.5">• Explores diverse violation postures</text>
        <text x="8" y="47" fill="#475569" font-size="8.5">• Varying alloca depths, struct nests</text>
        <text x="8" y="61" fill="#475569" font-size="8.5">• Flag variations (-O0..-O3, -fno-inline)</text>
      </g>

      <g transform="translate(8, 114)">
        <!-- PoC Minimization & Deliverable -->
        <rect x="0" y="0" width="319" height="72" rx="4" fill="#FFFFFF" stroke="#FECDD3"/>
        <text x="8" y="17" fill="#9F1239" font-size="9.5" font-weight="700">C-Reduce Delta Minimization:</text>
        <text x="8" y="33" fill="#475569" font-size="8.5">• Automated token &amp; AST reduction</text>
        <text x="8" y="47" fill="#475569" font-size="8.5">• Strict oracle-preserving delta test</text>
        <text x="8" y="61" fill="#BE123C" font-size="8.5" font-weight="600">→ Minimal Reproducible PoC</text>
      </g>

      <g transform="translate(8, 194)">
        <!-- Zero-Day Bug Report Output -->
        <rect x="0" y="0" width="319" height="56" rx="4" fill="#881337"/>
        <text x="8" y="18" fill="#FECDD3" font-size="10.5" font-weight="700">Verified Silent Failure Bug Report</text>
        <text x="8" y="34" fill="#FFFFFF" font-size="8.5">• Zero-Day Report with Invariant Trace</text>
        <text x="8" y="47" fill="#FDA4AF" font-size="8">Confirmed Root Cause → Feedback to RAG</text>
      </g>
    </g>

    <!-- 3.6 Diagnostic Feedback Agent & Checker Refinement (Refinement Path) -->
    <g transform="translate({s3_x+365}, {c35_y})">
      <rect x="0" y="0" width="355" height="260" rx="8" fill="url(#card-grad-purple)" stroke="#DDD6FE" stroke-width="1.5" filter="url(#shadow-sm)"/>
      <rect x="0" y="0" width="355" height="26" rx="8" fill="#EDE9FE"/>
      <rect x="0" y="16" width="355" height="10" fill="#EDE9FE"/>
      {render_icon('activity', 8, 4, 16, '#6D28D9')}
      <text x="30" y="18" fill="#4C1D95" font-size="11" font-weight="700">3.6 Feedback Agent &amp; Adaptive Evolution</text>

      <!-- Feedback Agent Logic -->
      <g transform="translate(8, 34)">
        <rect x="0" y="0" width="339" height="96" rx="4" fill="#FFFFFF" stroke="#DDD6FE"/>
        <text x="8" y="17" fill="#5B21B6" font-size="9.5" font-weight="700">Feedback Agent (via MCP):</text>
        <text x="8" y="33" fill="#475569" font-size="8.5">• Reads diagnostic JSON from compiler</text>
        <text x="8" y="47" fill="#475569" font-size="8.5">• Detects SRA/DCE optimization elimination</text>
        <text x="8" y="61" fill="#475569" font-size="8.5">• Evaluates log hit traces &amp; condition triggers</text>
        <text x="8" y="78" fill="#6D28D9" font-size="8.5" font-weight="600">→ Guides Generator with Anti-Opt hints</text>
      </g>

      <!-- Checker Refinement Trigger -->
      <g transform="translate(8, 138)">
        <rect x="0" y="0" width="339" height="112" rx="4" fill="#FAF5FF" stroke="#A78BFA"/>
        <text x="8" y="17" fill="#6D28D9" font-size="9.5" font-weight="700">Checker Refinement Loop (Tier 2):</text>
        <text x="8" y="33" fill="#475569" font-size="8.5">• Trigger: Consecutive N/A / Error count &gt; K</text>
        <text x="8" y="47" fill="#475569" font-size="8.5">• Checker Refinement Agent rewrites oracle</text>
        <text x="8" y="61" fill="#475569" font-size="8.5">• Re-validates against Tier 1 Grounding Gate</text>
        <text x="8" y="76" fill="#059669" font-size="8.5" font-weight="600">✓ Hot-replaces Checker in fuzzing loop</text>
        <text x="8" y="96" fill="#B45309" font-size="8" font-style="italic">Preserves Grounding Gate • No Goalpost Shift</text>
      </g>
    </g>
  </g>
''')

    # Arrows for Decision Paths
    # FAIL -> 3.5
    svg.append(f'''
    <path d="M {s3_x+182} {c34_y+96} L {s3_x+182} {c35_y}" fill="none" stroke="#E11D48" stroke-width="2" marker-end="url(#arrow-rose)"/>
    <rect x="{s3_x+137}" y="{c34_y+97}" width="90" height="16" rx="8" fill="#FFE4E6" stroke="#FDA4AF" stroke-width="1"/>
    <text x="{s3_x+145}" y="{c34_y+109}" fill="#BE123C" font-size="8.5" font-weight="700">Violation Found</text>
''')

    # PASS/ERR -> 3.6
    svg.append(f'''
    <path d="M {s3_x+542} {c34_y+96} L {s3_x+542} {c35_y}" fill="none" stroke="#7C3AED" stroke-width="2" marker-end="url(#arrow-purple)"/>
    <rect x="{s3_x+497}" y="{c34_y+97}" width="90" height="16" rx="8" fill="#EDE9FE" stroke="#DDD6FE" stroke-width="1"/>
    <text x="{s3_x+505}" y="{c34_y+109}" fill="#6D28D9" font-size="8.5" font-weight="700">No Violation</text>
''')

    # Feedback Loops:
    # 1. Lateral Exploration Loop: 3.5 -> 3.2 (Generator) inside gutter 2-3
    svg.append(f'''
    <!-- Lateral Exploration Feedback Loop via Gutter 2-3 -->
    <path d="M {s3_x+15} {c35_y+50} H {s3_x-18} V {c32_y+75} H {s3_x+15}" fill="none" stroke="#E11D48" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrow-rose)"/>
    <rect x="{s3_x-42}" y="{c32_y+110}" width="54" height="28" rx="4" fill="#FFF1F2" stroke="#FDA4AF" stroke-width="1"/>
    <text x="{s3_x-38}" y="{c32_y+122}" fill="#9F1239" font-size="7.5" font-weight="700">Lateral</text>
    <text x="{s3_x-38}" y="{c32_y+132}" fill="#9F1239" font-size="7">Explore</text>
''')

    # 2. Diagnostic Feedback Guidance Loop: 3.6 -> 3.2 (Generator) on right side
    svg.append(f'''
    <!-- Diagnostic Feedback Guidance Loop on right edge -->
    <path d="M {s3_x+720} {c35_y+55} H {s3_x+738} V {c32_y+55} H {s3_x+720}" fill="none" stroke="#7C3AED" stroke-width="2" stroke-dasharray="5 3" marker-end="url(#arrow-purple)"/>
    <rect x="{s3_x+712}" y="{c32_y+100}" width="50" height="28" rx="4" fill="#FAF5FF" stroke="#DDD6FE" stroke-width="1"/>
    <text x="{s3_x+716}" y="{c32_y+112}" fill="#5B21B6" font-size="7.5" font-weight="700">Feedback</text>
    <text x="{s3_x+716}" y="{c32_y+122}" fill="#5B21B6" font-size="7">Anti-Opt</text>
''')

    # 3. Checker Refinement Hot-Replacement Loop: 3.6 -> Stage 2.3 Oracle Synthesis (via bottom routing channel)
    svg.append(f'''
    <!-- Checker Refinement Loop back to Stage 2 -->
    <path d="M {s3_x+542} {c35_y+260} V 905 H {s2_x+277} V {c23_y+235}" fill="none" stroke="#D97706" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arrow-amber)"/>
    <rect x="{s2_x+420}" y="896" width="180" height="18" rx="9" fill="#FEF3C7" stroke="#FDE68A" stroke-width="1"/>
    <text x="{s2_x+430}" y="909" fill="#B45309" font-size="9" font-weight="700">Checker Refinement &amp; Tier 1 Gate</text>
''')

    # 4. Confirmed Root-Cause feedback loop: 3.5 -> Stage 1 Historical Bug RAG Knowledge Pool (via bottom channel)
    svg.append(f'''
    <!-- Confirmed Finding Loop to Stage 1 RAG -->
    <path d="M {s3_x+182} {c35_y+260} V 928 H {s1_x+242} V {c1_y+126}" fill="none" stroke="#312E81" stroke-width="1.8" stroke-dasharray="6 4" marker-end="url(#arrow-indigo)"/>
    <rect x="{s1_x+345}" y="919" width="245" height="18" rx="9" fill="#312E81" stroke="#818CF8" stroke-width="1"/>
    <text x="{s1_x+355}" y="932" fill="#EEF2FF" font-size="9" font-weight="700">Confirmed Zero-Day / Bug Finding → New RAG Probes</text>
''')

    # ==================== LEGEND & NOTATION BAR ====================
    leg_y = 955
    svg.append(f'''
  <!-- Bottom Legend Bar -->
  <g transform="translate(30, {leg_y})">
    <rect x="0" y="0" width="1820" height="30" rx="6" fill="#0F172A" filter="url(#shadow-sm)"/>
    <text x="15" y="19" fill="#94A3B8" font-size="10.5" font-weight="700">LEGEND &amp; CONTROL FLOW:</text>
    
    <!-- Primary Flow -->
    <line x1="185" y1="15" x2="215" y2="15" stroke="#FFFFFF" stroke-width="2.5"/>
    <circle cx="215" cy="15" r="3" fill="#FFFFFF"/>
    <text x="225" y="19" fill="#E2E8F0" font-size="10">Primary Pipeline Data Flow</text>

    <!-- MCP / Tool Call -->
    <line x1="420" y1="15" x2="450" y2="15" stroke="#2DD4BF" stroke-width="2" stroke-dasharray="4 2"/>
    <circle cx="450" cy="15" r="3" fill="#2DD4BF"/>
    <text x="460" y="19" fill="#2DD4BF" font-size="10">MCP &amp; Toolchain Invocation</text>

    <!-- Diagnostic Feedback -->
    <line x1="680" y1="15" x2="710" y2="15" stroke="#C084FC" stroke-width="2" stroke-dasharray="5 3"/>
    <circle cx="710" cy="15" r="3" fill="#C084FC"/>
    <text x="720" y="19" fill="#C084FC" font-size="10">Compiler Diagnostic Feedback</text>

    <!-- Refinement Loop -->
    <line x1="945" y1="15" x2="975" y2="15" stroke="#FBBF24" stroke-width="2" stroke-dasharray="4 3"/>
    <circle cx="975" cy="15" r="3" fill="#FBBF24"/>
    <text x="985" y="19" fill="#FBBF24" font-size="10">Checker Refinement &amp; Tier 1 Gate</text>

    <!-- Lateral Generalization -->
    <line x1="1230" y1="15" x2="1260" y2="15" stroke="#FB7185" stroke-width="2" stroke-dasharray="5 3"/>
    <circle cx="1260" cy="15" r="3" fill="#FB7185"/>
    <text x="1270" y="19" fill="#FB7185" font-size="10">Lateral Thinking (Bug Generalization)</text>

    <!-- RAG Feeder -->
    <line x1="1520" y1="15" x2="1550" y2="15" stroke="#818CF8" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="1550" cy="15" r="3" fill="#818CF8"/>
    <text x="1560" y="19" fill="#818CF8" font-size="10">Confirmed Bug Knowledge Feedback</text>
  </g>
''')

    svg.append('</svg>')
    res = '\n'.join(svg)
    
    # Validate with ElementTree
    try:
        ET.fromstring(res)
        print("✓ SVG valid XML!")
    except Exception as e:
        print("✗ XML Error:", e)
        raise e

    return res

if __name__ == '__main__':
    svg_content = create_defuzz_svg()
    out_svg = '/mnt/propagation/sources/research-defuzz-paper-0a9b3a25380dae02/figures/architecture.svg'
    with open(out_svg, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated {out_svg} ({len(svg_content)} bytes)")
