#!/usr/bin/env python3
"""
Generate a publication-grade, vector-based, logo-rich diagram for Figure 5:
Stage 4: Online Closed-Loop Agentic Fuzzing and Adaptive Feedback Loop.
Outputs SVG, compiles to PDF via rsvg-convert, and renders PNG via pdftoppm.
"""

import os
import subprocess

def create_stage4_svg(output_path="figures/method-agentic-loop.svg"):
    width = 1720
    height = 960

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, Helvetica, Arial, sans-serif;">')

    # Definitions
    svg.append('''
  <defs>
    <!-- Drop Shadows -->
    <filter id="shadow-card" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
    <filter id="shadow-alert" x="-10%" y="-10%" width="120%" height="125%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#DC2626" flood-opacity="0.25"/>
    </filter>

    <!-- Gradients -->
    <linearGradient id="bg-card-violet" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FAF5FF"/>
      <stop offset="100%" stop-color="#F3E8FF"/>
    </linearGradient>
    <linearGradient id="bg-card-cyan" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F0FDFA"/>
      <stop offset="100%" stop-color="#CCFBF1"/>
    </linearGradient>
    <linearGradient id="bg-card-slate" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC"/>
      <stop offset="100%" stop-color="#F1F5F9"/>
    </linearGradient>

    <!-- Headers -->
    <linearGradient id="hdr-violet" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6B21A8"/>
      <stop offset="100%" stop-color="#9333EA"/>
    </linearGradient>
    <linearGradient id="hdr-teal" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F766E"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <linearGradient id="hdr-slate" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arr-purple" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#9333EA"/>
    </marker>
    <marker id="arr-red" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>
    <marker id="arr-cyan" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284C7"/>
    </marker>
    <marker id="arr-slate" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#475569"/>
    </marker>
    <marker id="arr-teal" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0D9488"/>
    </marker>
  </defs>
''')

    # Title Banner
    svg.append('''
  <!-- Main Title -->
  <text x="860" y="38" font-size="26" font-weight="800" fill="#0F172A" text-anchor="middle" letter-spacing="-0.5">Online Closed-Loop Agentic Fuzzing and Adaptive Feedback Loop</text>
''')

    # Card Coordinates
    c_y = 100
    c_h = 750

    # ================= CARD 1: Orchestrator & Generator Agent =================
    c1_x = 30
    c1_w = 460
    svg.append(f'''
  <!-- Card 1 -->
  <g filter="url(#shadow-card)">
    <rect x="{c1_x}" y="{c_y}" width="{c1_w}" height="{c_h}" rx="14" fill="url(#bg-card-violet)" stroke="#D8B4FE" stroke-width="2"/>
    <rect x="{c1_x}" y="{c_y}" width="{c1_w}" height="44" rx="14" fill="url(#hdr-violet)"/>
    <rect x="{c1_x}" y="{c_y+28}" width="{c1_w}" height="16" fill="#9333EA"/>
    <text x="{c1_x + c1_w/2}" y="{c_y+28}" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">Orchestration &amp; Seed Synthesis</text>
  </g>

  <!-- 1.1 Deterministic Orchestrator -->
  <g filter="url(#shadow-card)" transform="translate({c1_x + 20}, {c_y + 58})">
    <rect x="0" y="0" width="{c1_w - 40}" height="135" rx="10" fill="#FFFFFF" stroke="#C084FC" stroke-width="1.8"/>
    <rect x="0" y="0" width="{c1_w - 40}" height="32" rx="10" fill="#F3E8FF"/>
    
    <!-- Clock / Scheduler Icon -->
    <circle cx="20" cy="16" r="10" fill="#9333EA"/>
    <polyline points="20,11 20,16 24,18" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
    <text x="38" y="21" font-size="13" font-weight="800" fill="#581C87">Deterministic Orchestrator</text>

    <!-- Badge: Time Budget -->
    <rect x="{c1_w - 170}" y="5" width="120" height="22" rx="11" fill="#7E22CE"/>
    <text x="{c1_w - 110}" y="19" font-size="10.5" font-weight="700" fill="#FAF5FF" text-anchor="middle">Fixed Budget T</text>

    <text x="16" y="54" font-size="12" font-weight="700" fill="#1E293B">• Locks Target Invariant φ<tspan font-size="9" dy="2">i</tspan><tspan dy="-2"> + Dedicated ISA Checker</tspan></text>
    <text x="16" y="74" font-size="11" font-weight="500" fill="#475569">• Allocates uniform execution budget T per target</text>
    <text x="16" y="92" font-size="11" font-weight="500" fill="#475569">• Ensures equal opportunity across all invariants</text>
    
    <rect x="14" y="102" width="{c1_w - 68}" height="22" rx="4" fill="#FAF5FF" stroke="#E9D5FF"/>
    <text x="24" y="117" font-size="10" font-weight="700" fill="#7E22CE">Target Queue: Invariant Catalog Φ (topological dispatch)</text>
  </g>

  <!-- Downward Arrow to Generator Agent -->
  <path d="M {c1_x + c1_w/2} {c_y + 195} L {c1_x + c1_w/2} {c_y + 225}" fill="none" stroke="#9333EA" stroke-width="2.5" marker-end="url(#arr-purple)"/>

  <!-- 1.2 LLM Generator Agent -->
  <g filter="url(#shadow-card)" transform="translate({c1_x + 20}, {c_y + 230})">
    <rect x="0" y="0" width="{c1_w - 40}" height="495" rx="10" fill="#FFFFFF" stroke="#C084FC" stroke-width="1.8"/>
    <rect x="0" y="0" width="{c1_w - 40}" height="34" rx="10" fill="#F3E8FF"/>

    <!-- AI Robot / Brain Icon -->
    <rect x="10" y="7" width="20" height="20" rx="4" fill="#9333EA"/>
    <circle cx="16" cy="15" r="2" fill="#FFFFFF"/>
    <circle cx="24" cy="15" r="2" fill="#FFFFFF"/>
    <line x1="16" y1="21" x2="24" y2="21" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
    <text x="38" y="22" font-size="13" font-weight="800" fill="#581C87">LLM Generator Agent</text>
    
    <rect x="{c1_w - 180}" y="6" width="130" height="22" rx="11" fill="#9333EA"/>
    <text x="{c1_w - 115}" y="20" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Checker-Aware</text>

    <text x="16" y="58" font-size="12" font-weight="700" fill="#1E293B">Synthesizes C/C++ Seeds ('seed_sp_probe.c')</text>
    <text x="16" y="76" font-size="11" font-weight="500" fill="#64748B">Conditioned on formal φ<tspan font-size="9" dy="2">i</tspan><tspan dy="-2"> + Level-3 predicates from Stage 3</tspan></text>

    <!-- Subcard: Anti-DCE Evasion Patterns -->
    <g transform="translate(12, 88)">
      <rect x="0" y="0" width="{c1_w - 64}" height="390" rx="8" fill="#FDF4FF" stroke="#F0ABFC" stroke-width="1.2"/>
      
      <!-- Anti-DCE Header -->
      <rect x="0" y="0" width="{c1_w - 64}" height="28" rx="8" fill="#FAE8FF"/>
      <!-- Shield Icon -->
      <path d="M 16 6 L 10 9 C 10 14 13.5 19 16 21 C 18.5 19 22 14 22 9 Z" fill="#C026D3"/>
      <text x="30" y="19" font-size="11" font-weight="800" fill="#86198F">Anti-Dead Code Elimination (Anti-DCE) Design</text>

      <!-- Pattern 1: Dynamic VLAs with argc -->
      <g transform="translate(10, 36)">
        <rect x="0" y="0" width="{c1_w - 84}" height="90" rx="6" fill="#FFFFFF" stroke="#E879F9"/>
        <text x="10" y="18" font-size="10.5" font-weight="700" fill="#701A75">1. Dynamic VLAs (argc bounds):</text>
        <rect x="8" y="24" width="{c1_w - 100}" height="56" rx="4" fill="#18181B"/>
        <text x="14" y="42" font-family="monospace" font-size="9.5" fill="#F472B6">int n = argc &gt; 1 ? atoi(argv[1]) : 64;</text>
        <text x="14" y="58" font-family="monospace" font-size="9.5" fill="#38BDF8">char buf[n];</text>
        <text x="14" y="72" font-family="monospace" font-size="8.5" fill="#94A3B8">// runtime dimensions force dynamic stack frame</text>
      </g>

      <!-- Pattern 2: asm volatile barriers -->
      <g transform="translate(10, 138)">
        <rect x="0" y="0" width="{c1_w - 84}" height="106" rx="6" fill="#FFFFFF" stroke="#E879F9"/>
        <text x="10" y="18" font-size="10.5" font-weight="700" fill="#701A75">2. Escaping Volatile Barriers:</text>
        <rect x="8" y="24" width="{c1_w - 100}" height="72" rx="4" fill="#18181B"/>
        <text x="14" y="42" font-family="monospace" font-size="9.5" fill="#4ADE80">asm volatile("" : "+m"(buf) : : "memory");</text>
        <text x="14" y="58" font-family="monospace" font-size="9.5" fill="#FDE047">volatile char sink = buf[0];</text>
        <text x="14" y="74" font-family="monospace" font-size="8.5" fill="#94A3B8">// prevents middle-end SRA / DCE elimination</text>
        <text x="14" y="88" font-family="monospace" font-size="8.5" fill="#38BDF8">// forces compiler backend to emit defense check</text>
      </g>

      <!-- Pattern 3: Non-inlinable calls -->
      <g transform="translate(10, 256)">
        <rect x="0" y="0" width="{c1_w - 84}" height="120" rx="6" fill="#FFFFFF" stroke="#E879F9"/>
        <text x="10" y="18" font-size="10.5" font-weight="700" fill="#701A75">3. External Non-Inlinable Calls:</text>
        <rect x="8" y="24" width="{c1_w - 100}" height="84" rx="4" fill="#18181B"/>
        <text x="14" y="40" font-family="monospace" font-size="9.5" fill="#F472B6">__attribute__((noinline))</text>
        <text x="14" y="56" font-family="monospace" font-size="9.5" fill="#38BDF8">void trigger_guard(char *p);</text>
        <text x="14" y="74" font-family="monospace" font-size="8.5" fill="#94A3B8">// prevents inlining; preserves complete prologue,</text>
        <text x="14" y="88" font-family="monospace" font-size="8.5" fill="#94A3B8">// return address LR\', and epilogue stack check</text>
      </g>
    </g>
  </g>
''')

    # Horizontal Arrow Card 1 -> Card 2
    seed_arrow_y = c_y + 450
    svg.append(f'''
  <!-- Arrow Card 1 -> Card 2 -->
  <path d="M {c1_x + c1_w} {seed_arrow_y} L {c1_x + c1_w + 50} {seed_arrow_y}" fill="none" stroke="#9333EA" stroke-width="3" marker-end="url(#arr-purple)"/>
  <rect x="{c1_x + c1_w + 2}" y="{seed_arrow_y - 28}" width="50" height="20" rx="4" fill="#F3E8FF" stroke="#C084FC"/>
  <text x="{c1_x + c1_w + 27}" y="{seed_arrow_y - 14}" font-size="9.5" font-weight="800" fill="#7E22CE" text-anchor="middle">Seed .c</text>
''')

    # ================= CARD 2: Instrumented Build & Dual Oracle =================
    c2_x = 550
    c2_w = 480
    svg.append(f'''
  <!-- Card 2 -->
  <g filter="url(#shadow-card)">
    <rect x="{c2_x}" y="{c_y}" width="{c2_w}" height="{c_h}" rx="14" fill="url(#bg-card-cyan)" stroke="#5EEAD4" stroke-width="2"/>
    <rect x="{c2_x}" y="{c_y}" width="{c2_w}" height="44" rx="14" fill="url(#hdr-teal)"/>
    <rect x="{c2_x}" y="{c_y+28}" width="{c2_w}" height="16" fill="#14B8A6"/>
    <text x="{c2_x + c2_w/2}" y="{c_y+28}" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">Instrumented Build &amp; Dual Oracle</text>
  </g>

  <!-- 2.1 Rebuilt Instrumented Compiler Driver -->
  <g filter="url(#shadow-card)" transform="translate({c2_x + 20}, {c_y + 58})">
    <rect x="0" y="0" width="{c2_w - 40}" height="320" rx="10" fill="#FFFFFF" stroke="#2DD4BF" stroke-width="1.8"/>
    <rect x="0" y="0" width="{c2_w - 40}" height="34" rx="10" fill="#CCFBF1"/>

    <!-- Compiler Logo / Chip Icon -->
    <rect x="10" y="7" width="20" height="20" rx="4" fill="#0F766E"/>
    <path d="M 13 17 L 17 21 L 27 11" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
    <text x="38" y="22" font-size="13" font-weight="800" fill="#042F2E">Rebuilt Compiler Driver (GCC_INST)</text>
    
    <rect x="{c2_w - 180}" y="6" width="130" height="22" rx="11" fill="#0D9488"/>
    <text x="{c2_w - 115}" y="20" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Standalone Binary</text>

    <!-- Technical Spec Badges (GCC, Clang) -->
    <g transform="translate(14, 46)">
      <!-- GCC Badge -->
      <rect x="0" y="0" width="130" height="26" rx="5" fill="#FEF3C7" stroke="#F59E0B"/>
      <text x="10" y="17" font-size="11" font-weight="800" fill="#92400E">GNU GCC 16.1</text>
      
      <!-- LLVM Badge -->
      <rect x="140" y="0" width="130" height="26" rx="5" fill="#E0E7FF" stroke="#6366F1"/>
      <text x="150" y="17" font-size="11" font-weight="800" fill="#3730A3">Clang / LLVM 21</text>
      
      <!-- Multi-ISA Badge -->
      <rect x="280" y="0" width="145" height="26" rx="5" fill="#F1F5F9" stroke="#94A3B8"/>
      <text x="290" y="17" font-size="10.5" font-weight="700" fill="#334155">x86_64, AArch64, RV64</text>
    </g>

    <!-- Compiler Flags Box -->
    <g transform="translate(14, 82)">
      <rect x="0" y="0" width="{c2_w - 68}" height="64" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="10" y="18" font-size="10.5" font-weight="700" fill="#0F172A">Compilation Flags &amp; Defense Profiles:</text>
      <text x="10" y="36" font-family="monospace" font-size="9" fill="#2563EB">-fstack-protector-strong -fstack-clash-protection</text>
      <text x="10" y="52" font-family="monospace" font-size="9" fill="#059669">-fsanitize=safe-stack -mbranch-protection=standard</text>
    </g>

    <!-- Real-time UID Trace Output Window -->
    <g transform="translate(14, 156)">
      <rect x="0" y="0" width="{c2_w - 68}" height="150" rx="6" fill="#0F172A" stroke="#334155"/>
      <rect x="0" y="0" width="{c2_w - 68}" height="24" rx="6" fill="#1E293B"/>
      <circle cx="12" cy="12" r="3.5" fill="#EF4444"/>
      <circle cx="24" cy="12" r="3.5" fill="#F59E0B"/>
      <circle cx="36" cy="12" r="3.5" fill="#10B981"/>
      <text x="50" y="16" font-family="monospace" font-size="9.5" fill="#94A3B8">GCC_INST Execution Stream (UID Trace)</text>

      <text x="12" y="42" font-family="monospace" font-size="9" fill="#4ADE80">[DEFUZZ_LOG:SP#a3f2:hit] expand_stack_protection()</text>
      <text x="12" y="58" font-family="monospace" font-size="9" fill="#38BDF8">  has_vla=1, stack_protect_decl=1, canary_slot=0x30</text>
      <text x="12" y="74" font-family="monospace" font-size="9" fill="#FDE047">[DEFUZZ_LOG:SP#b109:hit] aarch64_layout_frame()</text>
      <text x="12" y="90" font-family="monospace" font-size="9" fill="#F472B6">  LR_offset=0x20, canary_offset=0x38 (ALERT: LR &lt; canary!)</text>
      <text x="12" y="108" font-family="monospace" font-size="9" fill="#A78BFA">[DEFUZZ_BIN] Compiled Target Binary: ./a.out (deterministic)</text>
      <text x="12" y="126" font-family="monospace" font-size="8.5" fill="#94A3B8">&gt;&gt; Streamed directly to Dual Deterministic Oracle</text>
    </g>
  </g>

  <!-- Downward Arrow to Dual Deterministic Oracle -->
  <path d="M {c2_x + c2_w/2} {c_y + 390} L {c2_x + c2_w/2} {c_y + 418}" fill="none" stroke="#0D9488" stroke-width="2.5" marker-end="url(#arr-teal)"/>

  <!-- 2.2 Dual Deterministic Oracle Suite -->
  <g filter="url(#shadow-card)" transform="translate({c2_x + 20}, {c_y + 422})">
    <rect x="0" y="0" width="{c2_w - 40}" height="305" rx="10" fill="#FFFFFF" stroke="#2DD4BF" stroke-width="1.8"/>
    <rect x="0" y="0" width="{c2_w - 40}" height="34" rx="10" fill="#CCFBF1"/>

    <!-- Scales / Checkmark Icon -->
    <rect x="10" y="7" width="20" height="20" rx="4" fill="#0D9488"/>
    <path d="M 14 17 L 18 21 L 26 13" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
    <text x="38" y="22" font-size="13" font-weight="800" fill="#042F2E">Dual Deterministic Machine Oracle O(P, I, S)</text>

    <!-- Oracle Formal Contract Pill -->
    <rect x="14" y="44" width="{c2_w - 68}" height="26" rx="4" fill="#F0FDFA" stroke="#99F6E4"/>
    <text x="24" y="61" font-size="10.5" font-weight="700" fill="#0F766E">Deterministic Function: O : P × I × S → {{PASS, FAIL, NA, ERROR}}</text>

    <!-- Two Checker Columns: Static & Dynamic -->
    <!-- Column 1: Static Checker -->
    <g transform="translate(14, 80)">
      <rect x="0" y="0" width="200" height="210" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
      <rect x="0" y="0" width="200" height="24" rx="6" fill="#E2E8F0"/>
      <!-- Microscope icon -->
      <text x="8" y="16" font-size="10.5" font-weight="800" fill="#334155">🔬 Static Audit Checker</text>
      <text x="8" y="42" font-size="9.5" font-weight="700" fill="#0F172A">• GIMPLE / LLVM IR Audit</text>
      <text x="8" y="58" font-size="9" fill="#475569">  Verifies __stack_chk_fail call</text>
      <text x="8" y="78" font-size="9.5" font-weight="700" fill="#0F172A">• DWARF Frame Inspector</text>
      <text x="8" y="94" font-size="9" fill="#475569">  Extracts stack layout offsets</text>
      <text x="8" y="114" font-size="9.5" font-weight="700" fill="#0F172A">• Assembly Disassembler</text>
      <text x="8" y="130" font-size="9" fill="#475569">  AArch64 / x86 prologue check</text>
      <rect x="8" y="160" width="184" height="36" rx="4" fill="#EFF6FF" stroke="#BFDBFE"/>
      <text x="14" y="176" font-size="9" font-weight="700" fill="#1D4ED8">Evaluates unexecuted binaries</text>
      <text x="14" y="190" font-size="8" fill="#475569">Zero-execution static audit</text>
    </g>

    <!-- Column 2: Dynamic Checker -->
    <g transform="translate(226, 80)">
      <rect x="0" y="0" width="200" height="210" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
      <rect x="0" y="0" width="200" height="24" rx="6" fill="#E2E8F0"/>
      <!-- Gear/Sandbox icon -->
      <text x="8" y="16" font-size="10.5" font-weight="800" fill="#334155">⚙️ Dynamic Sandbox Probe</text>
      <text x="8" y="42" font-size="9.5" font-weight="700" fill="#0F172A">• Isolated Execution Box</text>
      <text x="8" y="58" font-size="9" fill="#475569">  QEMU / Bare-metal execution</text>
      <text x="8" y="78" font-size="9.5" font-weight="700" fill="#0F172A">• Runtime Overflow Trigger</text>
      <text x="8" y="94" font-size="9" fill="#475569">  Executes off-by-one / VLA probe</text>
      <text x="8" y="114" font-size="9.5" font-weight="700" fill="#0F172A">• Trap &amp; Signal Handler</text>
      <text x="8" y="130" font-size="9" fill="#475569">  SIGSEGV vs Canary exit(0)</text>
      <rect x="8" y="160" width="184" height="36" rx="4" fill="#FEF3C7" stroke="#FDE68A"/>
      <text x="14" y="176" font-size="9" font-weight="700" fill="#B45309">Observes live hardware traps</text>
      <text x="14" y="190" font-size="8" fill="#475569">Runtime verification proof</text>
    </g>
  </g>
''')

    # Horizontal Arrow Card 2 -> Card 3
    verdict_arrow_y = c_y + 530
    svg.append(f'''
  <!-- Arrow Card 2 -> Card 3 -->
  <path d="M {c2_x + c2_w} {verdict_arrow_y} L {c2_x + c2_w + 45} {verdict_arrow_y}" fill="none" stroke="#0D9488" stroke-width="3" marker-end="url(#arr-teal)"/>
  <rect x="{c2_x + c2_w + 2}" y="{verdict_arrow_y - 28}" width="48" height="20" rx="4" fill="#CCFBF1" stroke="#2DD4BF"/>
  <text x="{c2_x + c2_w + 26}" y="{verdict_arrow_y - 14}" font-size="9.5" font-weight="800" fill="#0F766E" text-anchor="middle">Verdict</text>
''')

    # ================= CARD 3: Verdict Dispatch & Closed Loops =================
    c3_x = 1085
    c3_w = 605
    svg.append(f'''
  <!-- Card 3 -->
  <g filter="url(#shadow-card)">
    <rect x="{c3_x}" y="{c_y}" width="{c3_w}" height="{c_h}" rx="14" fill="url(#bg-card-slate)" stroke="#94A3B8" stroke-width="2"/>
    <rect x="{c3_x}" y="{c_y}" width="{c3_w}" height="44" rx="14" fill="url(#hdr-slate)"/>
    <rect x="{c3_x}" y="{c_y+28}" width="{c3_w}" height="16" fill="#334155"/>
    <text x="{c3_x + c3_w/2}" y="{c_y+28}" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">Verdict Dispatch &amp; Closed Loops</text>
  </g>

  <!-- Central Decision Diamond: Invariant Violated? -->
  <g filter="url(#shadow-card)" transform="translate({c3_x + 90}, {c_y + 480})">
    <!-- Diamond Shape -->
    <polygon points="65,0 130,50 65,100 0,50" fill="#FFFFFF" stroke="#0284C7" stroke-width="2.5"/>
    <text x="65" y="44" font-size="12" font-weight="800" fill="#0F172A" text-anchor="middle">Invariant</text>
    <text x="65" y="62" font-size="12" font-weight="800" fill="#0284C7" text-anchor="middle">Violated?</text>
  </g>

  <!-- Branch NO: Points UPWARD to Feedback Agent -->
  <path d="M {c3_x + 155} {c_y + 480} L {c3_x + 155} {c_y + 355}" fill="none" stroke="#475569" stroke-width="2.5" marker-end="url(#arr-slate)"/>
  <rect x="{c3_x + 165}" y="{c_y + 400}" width="155" height="22" rx="4" fill="#F1F5F9" stroke="#CBD5E1"/>
  <text x="{c3_x + 242}" y="{c_y + 415}" font-size="10" font-weight="800" fill="#475569" text-anchor="middle">NO: PASS / NA / ERROR</text>

  <!-- Branch YES: Points RIGHT to Confirmed Bug -->
  <path d="M {c3_x + 220} {c_y + 530} L {c3_x + 320} {c_y + 530}" fill="none" stroke="#DC2626" stroke-width="3" marker-end="url(#arr-red)"/>
  <rect x="{c3_x + 235}" y="{c_y + 500}" width="75" height="20" rx="4" fill="#FEE2E2" stroke="#F87171"/>
  <text x="{c3_x + 272}" y="{c_y + 514}" font-size="10.5" font-weight="800" fill="#DC2626" text-anchor="middle">YES: FAIL</text>

  <!-- Branch Lateral: Points DOWN to Lateral Exploration -->
  <path d="M {c3_x + 155} {c_y + 580} L {c3_x + 155} {c_y + 645}" fill="none" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arr-cyan)"/>

  <!-- ================= SUB-BLOCK: Feedback Agent (Top of Card 3) ================= -->
  <g filter="url(#shadow-card)" transform="translate({c3_x + 20}, {c_y + 58})">
    <rect x="0" y="0" width="{c3_w - 40}" height="280" rx="10" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.8"/>
    <rect x="0" y="0" width="{c3_w - 40}" height="34" rx="10" fill="#F3E8FF"/>

    <!-- Terminal / Feedback Agent Icon -->
    <rect x="10" y="7" width="20" height="20" rx="4" fill="#9333EA"/>
    <polyline points="14,14 18,17 14,20" fill="none" stroke="#FFFFFF" stroke-width="1.5"/>
    <line x1="20" y1="21" x2="25" y2="21" stroke="#FFFFFF" stroke-width="1.5"/>
    <text x="38" y="22" font-size="13" font-weight="800" fill="#581C87">Feedback Agent (Advanced Multimodal Analysis)</text>

    <!-- Feedback Extraction Details -->
    <g transform="translate(14, 46)">
      <rect x="0" y="0" width="{c3_w - 68}" height="72" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
      <text x="10" y="18" font-size="10.5" font-weight="700" fill="#0F172A">Multi-Dimensional Feedback Ingestion via Bash &amp; MCP:</text>
      <text x="10" y="34" font-size="9.5" fill="#475569">• Compiler diagnostics, warnings, and optimization records (-fopt-info)</text>
      <text x="10" y="50" font-size="9.5" fill="#475569">• UID probe hits: <tspan font-family="monospace" fill="#7E22CE">hit_count(UID)</tspan> tracking unreached critical conditions</text>
      <text x="10" y="66" font-size="9.5" fill="#475569">• Detailed Oracle execution traces and DWARF register offsets</text>
    </g>

    <!-- Action 1: Guidance Loop Banner -->
    <g transform="translate(14, 128)">
      <rect x="0" y="0" width="{c3_w - 68}" height="60" rx="6" fill="#FAF5FF" stroke="#D8B4FE"/>
      <circle cx="16" cy="18" r="8" fill="#9333EA"/>
      <text x="16" y="22" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
      <text x="32" y="21" font-size="11" font-weight="800" fill="#6B21A8">Guidance Loop (Mutation Hints)</text>
      <text x="32" y="38" font-size="9.5" fill="#475569">If condition unreached (e.g., has_vla == false), generates precise</text>
      <text x="32" y="52" font-size="9.5" fill="#475569">syntactic mutation instructions to steer Generator Agent.</text>
    </g>

    <!-- Action 2: Checker Evolution Loop Banner -->
    <g transform="translate(14, 198)">
      <rect x="0" y="0" width="{c3_w - 68}" height="70" rx="6" fill="#FEF2F2" stroke="#FCA5A5"/>
      <circle cx="16" cy="18" r="8" fill="#DC2626"/>
      <text x="16" y="22" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">2</text>
      <text x="32" y="21" font-size="11" font-weight="800" fill="#991B1B">Checker Adaptive Rewrite (Evolution &amp; Pool Replay)</text>
      <text x="32" y="38" font-size="9.5" fill="#475569">When rule ambiguity votes ≥ τ: triggers automated checker rewrite,</text>
      <text x="32" y="52" font-size="9.5" font-weight="700" fill="#DC2626">AND immediately replays the entire historical seed pool H</text>
      <text x="32" y="65" font-size="9" fill="#475569">against new checker to catch previously masked violations.</text>
    </g>
  </g>

  <!-- ================= SUB-BLOCK: Confirmed Bug & C-Reduce (Right of Card 3) ================= -->
  <g filter="url(#shadow-alert)" transform="translate({c3_x + 330}, {c_y + 440})">
    <rect x="0" y="0" width="{c3_w - 350}" height="175" rx="10" fill="#FFF1F2" stroke="#F43F5E" stroke-width="2"/>
    <rect x="0" y="0" width="{c3_w - 350}" height="32" rx="10" fill="#FFE4E6"/>
    
    <!-- Bug Explosion Icon -->
    <circle cx="18" cy="16" r="9" fill="#E11D48"/>
    <text x="18" y="20" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">✕</text>
    <text x="34" y="21" font-size="12" font-weight="800" fill="#9F1239">CONFIRMED BUG</text>

    <text x="12" y="52" font-size="11" font-weight="800" fill="#881337">Deterministic Violation Proven!</text>
    <text x="12" y="68" font-size="9.5" fill="#475569">Zero-false-positive binary trace</text>

    <!-- C-Reduce Minimizer Box -->
    <g transform="translate(8, 80)">
      <rect x="0" y="0" width="{c3_w - 366}" height="82" rx="6" fill="#FFFFFF" stroke="#FDA4AF"/>
      <!-- Scissor Icon -->
      <text x="8" y="16" font-size="10.5" font-weight="800" fill="#BE123C">✂️ Automated C-Reduce</text>
      <text x="8" y="32" font-size="9" fill="#475569">Delta-debugging + semantic test</text>
      <rect x="6" y="46" width="{c3_w - 378}" height="26" rx="4" fill="#FEE2E2" stroke="#F87171"/>
      <text x="12" y="62" font-size="9.5" font-weight="800" fill="#991B1B">Output: Minimal Zero-Day PoC</text>
    </g>
  </g>

  <!-- Arrow from Confirmed Bug down to Lateral Exploration -->
  <path d="M {c3_x + 455} {c_y + 615} L {c3_x + 455} {c_y + 645}" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arr-cyan)"/>

  <!-- ================= SUB-BLOCK: Lateral Exploration (Bug Amplification) ================= -->
  <g filter="url(#shadow-card)" transform="translate({c3_x + 20}, {c_y + 655})">
    <rect x="0" y="0" width="{c3_w - 40}" height="175" rx="10" fill="#F0F9FF" stroke="#38BDF8" stroke-width="1.8"/>
    <rect x="0" y="0" width="{c3_w - 40}" height="32" rx="10" fill="#E0F2FE"/>
    
    <!-- Amplification Icon -->
    <circle cx="16" cy="16" r="8" fill="#0284C7"/>
    <polygon points="13,12 21,16 13,20" fill="#FFFFFF"/>
    <text x="32" y="21" font-size="12" font-weight="800" fill="#0369A1">3. Lateral Exploration Loop (Bug Amplification Mechanism)</text>

    <text x="14" y="52" font-size="10.5" font-weight="800" fill="#0F172A">Does NOT terminate on first bug! Drives Generator to amplify finding:</text>
    
    <g transform="translate(14, 62)">
      <rect x="0" y="0" width="{c3_w - 68}" height="106" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
      <text x="10" y="18" font-size="10" font-weight="700" fill="#0369A1">• Mutate Boundary Types:</text>
      <text x="160" y="18" font-size="9.5" fill="#475569">signed/unsigned wraps, multi-dimension VLAs</text>
      
      <text x="10" y="38" font-size="10" font-weight="700" fill="#0369A1">• Composite Structures:</text>
      <text x="160" y="38" font-size="9.5" fill="#475569">nested structs, flexible array members, alloca() chains</text>
      
      <text x="10" y="58" font-size="10" font-weight="700" fill="#0369A1">• Atypical Stack Alignment:</text>
      <text x="160" y="58" font-size="9.5" fill="#475569">forced 32/64-byte vector alignment, SVE registers</text>
      
      <rect x="8" y="76" width="{c3_w - 84}" height="22" rx="3" fill="#E0F2FE"/>
      <text x="14" y="91" font-size="9" font-weight="800" fill="#0284C7">Maximal Vulnerability Discovery across Alternate Backend Lowering Paths</text>
    </g>
  </g>

  <!-- ================= RETURNING FEEDBACK CLOSED LOOPS (Non-overlapping arcs) ================= -->
  <!-- Loop 1: Guidance Loop (Purple dashed, clear arc above card headers, entering Generator Agent) -->
  <path d="M {c3_x + 180} {c_y} C {c3_x + 180} 58, {c1_x - 15} 58, {c1_x - 15} {c_y + 350} L {c1_x + 20} {c_y + 350}" 
        fill="none" stroke="#9333EA" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arr-purple)"/>
  
  <rect x="710" y="46" width="310" height="24" rx="12" fill="#FAF5FF" stroke="#C084FC" stroke-width="1.5"/>
  <text x="865" y="62" font-size="11" font-weight="800" fill="#7E22CE" text-anchor="middle">Guidance Loop: Mutation Hints → Generator</text>

  <!-- Loop 2: Checker Rewrite Loop (Red dashed, direct arc through middle gutter to Oracle) -->
  <path d="M {c3_x} {c_y + 260} C {c3_x - 30} {c_y + 260}, {c2_x + c2_w + 30} {c_y + 440}, {c2_x + c2_w} {c_y + 440}" 
        fill="none" stroke="#DC2626" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arr-red)"/>
  
  <rect x="1005" y="{c_y + 340}" width="180" height="22" rx="11" fill="#FEF2F2" stroke="#F87171" stroke-width="1.5"/>
  <text x="1095" y="{c_y + 355}" font-size="9" font-weight="800" fill="#DC2626" text-anchor="middle">Rewrite &amp; Replay Pool H</text>

  <!-- Loop 3: Lateral Exploration Loop (Cyan dashed, bottom margin channel back to Generator) -->
  <path d="M {c3_x + 180} {c_y + c_h} C {c3_x + 180} 925, {c1_x + c1_w/2} 925, {c1_x + c1_w/2} {c_y + c_h}" 
        fill="none" stroke="#0284C7" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arr-cyan)"/>
  
  <rect x="670" y="910" width="380" height="26" rx="13" fill="#F0F9FF" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="860" y="927" font-size="11" font-weight="800" fill="#0369A1" text-anchor="middle">Lateral Exploration Loop: Bug Amplification (Variants)</text>

  </svg>''')

    content = "\n".join(svg)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated SVG: {output_path}")

    # Compile to PDF
    pdf_path = output_path.replace(".svg", ".pdf")
    cmd_pdf = ["/opt/homebrew/bin/rsvg-convert", "-f", "pdf", "-o", pdf_path, output_path]
    subprocess.run(cmd_pdf, check=True)
    print(f"Generated PDF: {pdf_path}")

    # Render PNG
    png_path = output_path.replace(".svg", ".png")
    cmd_png = ["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-w", "2400", "-o", png_path, output_path]
    subprocess.run(cmd_png, check=True)
    print(f"Generated PNG: {png_path}")

    # Also update jpg if needed
    jpg_path = output_path.replace(".svg", ".jpg")
    cmd_jpg = ["/opt/homebrew/bin/rsvg-convert", "-f", "png", "-w", "2400", "-o", jpg_path, output_path]
    subprocess.run(cmd_jpg, check=True)
    print(f"Generated JPG: {jpg_path}")

if __name__ == "__main__":
    create_stage4_svg()
