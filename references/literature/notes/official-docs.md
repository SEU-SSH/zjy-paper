# 官方规范与实现文档收集

核验日期：2026-11-12。收集身份可确认的官方资料，并阅读与用途相关的小节；不将文档描述等同于已验证的实现能力。GCC 使用 15.2 版本化链接，Arm 使用 2025Q1；LLVM、glibc 等滚动链接记录访问日期，正式写作前需对齐实验版本。

特别注意：RISC-V psABI 当前页面为 **2.0-rc0 / 2026-11-04 / Pre-release**；LoongArch ABI 为 2.01，ISA Volume 1 为 1.10。

## 已核验的关键边界

- GCC 的 `strub` 主要定义在 Common Type Attributes；`zero_call_used_regs` 在函数属性与优化选项中；不能把这些位置或语义混用。
- GCC/LLVM 属性手册区分启用前提、目标支持及预期行为，手册存在一个选项不证明它在四 ISA 均可用。
- UBSan 的 recover/trap/report 行为可配置，不能把所有 sanitizer 成功诊断都说成必然崩溃。
- glibc 明确区别普通内存擦除与 explicit_bzero/memset_explicit 的不被优化删除承诺；擦除内存也不自动清除其他副本。
- RISC-V CFI 官方网页旧路径已失效，改读取官方 ISA 仓库 `src/unpriv/cfi.adoc`；正式引用应再固定 release/commit。
- Intel SDM/CET 官方链接本轮返回 403，Clang MemTagSanitizer 旧路径返回 404；未冒称读取，也未纳入已核验候选。MTE 的精确架构规范仍是补读项。

## 逐项用途

- **GCC 15.2: Instrumentation Options**（`gcc15instrumentation`）：栈保护、stack-clash、CFI、sanitizer、hardened 选项及平台限制。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Instrumentation-Options.html)。边界：选项文档描述预期行为，不能证明具体编译器构建的实现正确。
- **GCC 15.2: Common Function Attributes**（`gcc15commonfunctionattrs`）：zero_call_used_regs、access 等函数属性的规范与启用条件。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Common-Function-Attributes.html)。边界：strub 的主要规范在 Common Type Attributes，不能把属性存在等同于任意调用点已被正确加固。
- **GCC 15.2: Common Variable Attributes**（`gcc15commonvariableattrs`）：counted_by 和 nonstring 属性及对象边界相关语义。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Common-Variable-Attributes.html)。边界：属性支持和语义依赖语言及编译器版本，不代表自动保证所有动态边界安全。
- **GCC 15.2: Code Generation Options**（`gcc15codegen`）：栈复用、代码生成与 noplt 等编译选项背景。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Code-Gen-Options.html)。边界：ABI、链接器和平台条件需要同时核对；性能选项并非一律是安全防御。
- **GCC 15.2: Static Analyzer Options**（`gcc15staticanalysis`）：-fanalyzer 的用途、检查器选项和诊断边界。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Static-Analyzer-Options.html)。边界：静态诊断与运行时插桩属于不同验证对象，不应混为所有后端均生效的防御。
- **GCC 15.2: Optimize Options**（`gcc15optimize`）：自动变量初始化、寄存器清零以及优化选项的预期语义。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Optimize-Options.html)。边界：需同时考虑优化等级、目标支持和显式选项；此页面不是实验支持矩阵。
- **Clang: Control Flow Integrity**（`clangcfi`）：Clang CFI 方案、启用条件及使用限制。 [官方来源](https://clang.llvm.org/docs/ControlFlowIntegrity.html)。边界：不同 CFI 方案、LTO 和可见性条件不同，不能概括为同一检查契约。
- **Clang: Control Flow Integrity Design Documentation**（`clangcfidesign`）：类型测试与控制流完整性实现设计背景。 [官方来源](https://clang.llvm.org/docs/ControlFlowIntegrityDesign.html)。边界：设计文档不证明当前版本或所有 ISA 上的实现正确。
- **Clang: SafeStack**（`clangsafestack`）：safe/unsafe stack 划分、使用条件和已说明的限制。 [官方来源](https://clang.llvm.org/docs/SafeStack.html)。边界：SafeStack 不等于通用越界检测，也不能等同于硬件 shadow stack。
- **Clang: ShadowCallStack**（`clangshadowcallstack`）：返回地址保护与架构专用寄存器、运行时支持前提。 [官方来源](https://clang.llvm.org/docs/ShadowCallStack.html)。边界：页面是滚动版本；平台支持需对齐实验编译器，不能仅由文档清单推出可用性。
- **Clang: AddressSanitizer**（`clangasan`）：ASan 检测对象、构建和运行要求、局限。 [官方来源](https://clang.llvm.org/docs/AddressSanitizer.html)。边界：检测器本身的正确性与覆盖范围仍需独立验证，不代表不存在漏报。
- **Clang: MemorySanitizer**（`clangmsan`）：未初始化内存使用检测与完整插桩等运行前提。 [官方来源](https://clang.llvm.org/docs/MemorySanitizer.html)。边界：MSan 与 ASan 的问题模型不同，不能交换其缺陷覆盖范围。
- **Clang: UndefinedBehaviorSanitizer**（`clangubsan`）：UBSan 检查集合、recover/trap 等报告行为。 [官方来源](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html)。边界：报告模式可配置；不能把所有 sanitizer 的成功诊断都概括成必然进程崩溃。
- **Clang: Hardware-assisted AddressSanitizer Design**（`clanghwasan`）：指针/内存标记及 AArch64 TBI 支持下的检测设计。 [官方来源](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html)。边界：HWASan 与硬件 MTE 不是同一机制，也不提供一般无遗漏保证。
- **LLVM: Speculative Load Hardening**（`clangslh`）：SLH 的威胁范围、谓词依赖与实现思路。 [官方来源](https://llvm.org/docs/SpeculativeLoadHardening.html)。边界：只适用于文档明确的推测执行问题模型，不是所有微架构侧信道的统一防御。
- **Clang: Attribute Reference**（`clangattrs`）：musttail、counted_by 及其他检查适用条件所需的属性规范。 [官方来源](https://clang.llvm.org/docs/AttributeReference.html)。边界：必须引用具体属性小节；整个属性目录不能作为某一目标后端正确实现的证据。
- **LLVM Language Reference Manual**（`llvmreflang`）：IR 语义、属性、内存操作与正确性约束的规范基础。 [官方来源](https://llvm.org/docs/LangRef.html)。边界：滚动开发版需与实验 LLVM commit 对齐；不能自动覆盖机器码层防御义务。
- **LLVM IR Undefined Behavior Manual**（`llvmub`）：undef、poison、freeze 与 refinement 比较的语义背景。 [官方来源](https://llvm.org/docs/UndefinedBehavior.html)。边界：LLVM IR 的 UB 语义不能直接等同于 C/C++ 源语言规则。
- **The LLVM Target-Independent Code Generator**（`llvmcodegen`）：middle-end/backend lowering、指令选择与机器级变换背景。 [官方来源](https://llvm.org/docs/CodeGenerator.html)。边界：架构说明不证明某个 pass 或保护机制在全部目标上的行为。
- **LLVM Testing Infrastructure Guide**（`llvmtestguide`）：回归测试、lit/FileCheck 等实现验证背景。 [官方来源](https://llvm.org/docs/TestingGuide.html)。边界：通过既有回归测试不等于对全部安全契约的语义证明。
- **The GNU C Library: Source Fortification**（`glibcfortify`）：_FORTIFY_SOURCE、对象大小内建函数及加固调用的库/编译器契约。 [官方来源](https://sourceware.org/glibc/manual/latest/html_node/Source-Fortification.html)。边界：glibc 版本、编译器能力和优化条件共同决定行为，不能由符号存在推出边界计算正确。
- **The GNU C Library: Erasing Sensitive Data**（`glibcerase`）：普通擦除可能被优化删除，与 explicit_bzero/memset_explicit 承诺的区别。 [官方来源](https://sourceware.org/glibc/manual/latest/html_node/Erasing-Sensitive-Data.html)。边界：擦除目标内存的保证不自动覆盖寄存器副本和所有中间数据。
- **Procedure Call Standard for the Arm 64-bit Architecture (AAPCS64), 2025Q1**（`arm_aapcs64`）：AArch64 参数、返回值、callee-saved 与平台寄存器约定。 [官方来源](https://raw.githubusercontent.com/ARM-software/abi-aa/2025Q1/aapcs64/aapcs64.rst)。边界：特别注意 x18 的平台保留规则；ABI 义务与 caller-saved 寄存器清零义务不同。
- **System V ABI for the Arm 64-bit Architecture, 2025Q1**（`arm_sysvabi64`）：BTI、PAC、GCS 相关 ELF 特性与链接/调用约定。 [官方来源](https://raw.githubusercontent.com/ARM-software/abi-aa/2025Q1/sysvabi64/sysvabi64.rst)。边界：规范支持不表示任意硬件、内核或 QEMU 已实现该特性。
- **RISC-V ABIs Specification, version 2.0-rc0**（`riscvpsabi`）：RISC-V 寄存器约定、调用约定和 ELF ABI。 [官方来源](https://riscv-non-isa.github.io/riscv-elf-psabi-doc/)。边界：本次页面标示 2026-11-04 pre-release 2.0-rc0；不能当作已冻结正式版本，实验前必须固定版本。
- **LoongArch ELF ABI Specification, version 2.01**（`loongarchabi`）：LoongArch 寄存器、参数/返回值及 ELF ABI。 [官方来源](https://loongson.github.io/LoongArch-Documentation/LoongArch-ELF-ABI-EN.html)。边界：ABI 文档不能证明某个 compiler defense 已被 LoongArch 后端实现。
- **LoongArch Reference Manual, Volume 1: Basic Architecture, version 1.10**（`loongarchisa`）：LoongArch 指令语义及机器级观察的规范入口。 [官方来源](https://loongson.github.io/LoongArch-Documentation/LoongArch-Vol1-EN.html)。边界：按具体指令小节和版本引用，不从 ISA 规范推断工具链与运行环境支持。
- **RISC-V Unprivileged ISA Manual: Control-Flow Integrity**（`riscvcfi_raw`）：Zicfilp 前向边与 Zicfiss 后向边防御的官方规范源码。 [官方来源](https://raw.githubusercontent.com/riscv/riscv-isa-manual/main/src/unpriv/cfi.adoc)。边界：读取的是 main 分支规范源码；正式引用前应固定 release/commit，并核验硬件及编译器支持。
- **System V Application Binary Interface: AMD64 Architecture Processor Supplement**（`x86psabi`）：x86-64 psABI 维护仓库与规范入口。 [官方来源](https://gitlab.com/x86-psABIs/x86-64-ABI)。边界：本次只核维护仓库和规范入口；具体寄存器或 red-zone 论断需进一步查阅相应版本 PDF。
- **Clang Static Analyzer: Checker Developer Manual**（`clangcsacheckers`）：CSA checker 接口与扩展分析器背景，可配合 KNighter。 [官方来源](https://clang-analyzer.llvm.org/checker_dev_manual.html)。边界：这里只支持开发接口背景，不证明合成 checker 的可靠性。
- **GCC 15.2: Common Type Attributes**（`gcctypeattrs`）：strub 类型属性、模式、调用约束与栈擦除规范。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Common-Type-Attributes.html)。边界：须与 instrumentation options 联合读；不能把未启用或不适用的擦除视为遗漏。
- **GCC 15.2: Object Size Checking**（`gccobjectsize`）：__builtin_object_size、动态对象大小和加固调用的判定基础。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Object-Size-Checking.html)。边界：对象大小语义及未知值处理依赖 type 参数；常量差异本身不能证明错误。
- **GCC 15.2: C Dialect Options**（`gccstrictflex`）：-fstrict-flex-arrays 等 C 方言选项与柔性数组的适用规则。 [官方来源](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/C-Dialect-Options.html)。边界：语言选项的行为不等同于独立运行时 bounds checker。
