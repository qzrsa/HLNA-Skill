# HLNA-Skill · 方舟生存专家（WorkBuddy 专家包）

> **English summary:** A WorkBuddy **expert package** for ARK: Survival Ascended (ASA) and ARK: Survival Evolved (ASE). It is **not** a generic Claude/Codex Skill — it uses WorkBuddy's proprietary `.codebuddy-plugin/plugin.json` format and must be installed into a WorkBuddy desktop client. See [安装](#安装).

**HLN-A** 是覆盖《方舟：生存飞升》与《方舟：生存进化》全领域的 AI 专家：生物驯服与繁育、建筑与部落经营、地图探索、装备科技、版本更新查证、官方服务器倍率、服务器状态查询，以及 ASE / ASA 双版本 BOSS 完整数值表。遇到不确定内容时按优先级查证权威资料（wikily.gg 中文站 → ark.wiki.gg → survivetheark 官方论坛）。

---

## ⚠️ 先读：这是什么、不是什么

| | 说明 |
|---|---|
| **是** | WorkBuddy 桌面端可用的 **Agent 型专家包**（`expertType: agent`） |
| **不是** | 通用 Skill（Claude Skill / Codex / MCP server / ChatGPT GPTs 均不兼容） |
| **能用的人** | 安装了 **WorkBuddy 桌面端**的用户；GitHub 只负责分发，**不会自动生效** |
| **别人要做的** | 下载本仓库 → 把 `hln-a/` 放进自己的专家目录 → 运行注册脚本 → 在「专家中心 → 我的专家」开启对话 |

也就是说：**传到 GitHub ≠ 开箱即用**。仓库只是让所有人都能取到文件，安装仍需 3 步手动操作。仓库名沿用 `HLNA-Skill`，请不要因名称误判为通用 Skill。

---

## 前置条件

- WorkBuddy 桌面端（Windows / macOS）
- Python 3（用于运行注册脚本；脚本随 WorkBuddy 安装，完整路径见下方「方式 C」）

---

## 安装

`~` 代表你的用户主目录（Windows 为 `C:\Users\<你的用户名>`）。

### 方式 A：从仓库克隆（推荐）

```bash
git clone https://github.com/qzrsa/HLNA-Skill.git
```

然后把专家包目录**整体复制**到 WorkBuddy 专家目录：

```bash
# Windows 示例（PowerShell）
Copy-Item -Recurse .\HLNA-Skill\hln-a "$env:USERPROFILE\.workbuddy\plugins\marketplaces\my-experts\plugins\hln-a"

# macOS / Linux 示例
cp -r ./HLNA-Skill/hln-a ~/.workbuddy/plugins/marketplaces/my-experts/plugins/hln-a
```

### 方式 B：直接下载 zip

下载仓库中的 **`hln-a.zip`**（分享包，与 `hln-a/` 内容一致），解压到同一专家目录。

### 方式 C：从专家包源码自行校验注册

脚本位于 WorkBuddy 内置的 `expert-manager` 技能目录中。**优先使用 `marketplaces` 下的稳定路径**，不要使用带版本哈希的旧 `cache` 路径（升级后经常失效）：

```bash
# macOS / Linux
EXPERT=~/.workbuddy/plugins/marketplaces/my-experts/plugins/hln-a
SCRIPTS=~/.workbuddy/plugins/marketplaces/workbuddy-builtin/skills/expert-manager/scripts
python3 "$SCRIPTS/validate_expert.py" "$EXPERT"
python3 "$SCRIPTS/register_expert.py" "$EXPERT"
```

```powershell
# Windows（PowerShell；Windows 通常用 python 而非 python3）
$EXPERT  = "$env:USERPROFILE\.workbuddy\plugins\marketplaces\my-experts\plugins\hln-a"
$SCRIPTS = "$env:USERPROFILE\.workbuddy\plugins\marketplaces\workbuddy-builtin\skills\expert-manager\scripts"
python "$SCRIPTS\validate_expert.py" "$EXPERT"
python "$SCRIPTS\register_expert.py" "$EXPERT"
```

> 若 `marketplaces/workbuddy-builtin` 下找不到脚本，可到 `~/.workbuddy/plugins/cache/workbuddy-builtin/skill-expert-manager/<最新版本目录>/scripts/` 中查找，选择版本号最新的那个目录。

`validate_expert.py` 会检查结构是否合规，`register_expert.py` 会把专家写入 `my-experts/.codebuddy-plugin/marketplace.json`。注册成功后重启或刷新 WorkBuddy，在「专家中心 → 我的专家」即可看到 **HLN-A（方舟生存专家）**。

> 目录必须是 `.../marketplaces/my-experts/plugins/hln-a/`，放到别处不会被检测到。若目录里已有同名专家，直接覆盖即可，然后**务必重新注册一次**。

---

## 目录结构

```
HLNA-Skill/
├── README.md                  ← 本文件
├── LICENSE                    ← 原创部分许可与第三方资料边界
├── .gitignore
├── hln-a/                     ← 专家包本体（安装时用这个目录）
│   ├── .codebuddy-plugin/plugin.json
│   ├── agents/hln-a.md        ← 专家人设、能力、知识入口
│   ├── avatars/expert.png     ← HLN-A 官方形象图
│   ├── README.md
│   └── references/
│       ├── ark-boss-table/    ← BOSS 详情表（ASE 63 行 + ASA 60 行 + 数据 + 口径）
│       └── ark-supreme/       ← ARK-Supreme 模组攻略与生成代码
└── hln-a.zip                  ← 与 hln-a/ 等价的分享包
```

---

## 专家能力概览

- **生物对照**：原版生物（按官方地图归类）+ 官方付费 DLC 生物（Fantastic Tames / ARK: Dragontopia）+ 模组生物（ARK-Supreme），三类分开，避免混淆。
- **版本更新**：内置 v97（ASA 97.0，2026-11-06）记录，含南巨「巅峰挑战 Apex Challenge」驯服重做（**仅 ASA 生效，ASE 仍为传统击晕驯服**）、Enigmasaur 上线、UE 5.8 升级等；防止沿用旧版攻略，并对官方 Wiki 信息卡滞后于补丁的情况做出标注。
- **BOSS 详情速查**：ASE 12 图 / 25 BOSS / 63 行，ASA 10 图 / 22 BOSS / 60 行，双版本独立、禁止跨版本套用；含血量、准入等级、神器/战利品贡品、贡品数量、γ/β/α 能量元素、泰克印痕解锁、掉落物。
- **查证链**：wikily.gg 中文站 → ark.wiki.gg → survivetheark 官方论坛；官方服倍率另查 wikily.gg/rates 与 dododex；服务器状态查 ark.fusey.gg / BattleMetrics / arkstatus。

试试这样问：

- 帮我查询《方舟：生存飞升》里南巨（Giganotosaurus）的驯服方法与注意事项
- ASA 育母蜘蛛 α 困难给多少能量元素？需要哪些贡品？
- 最新版本方舟更新了哪些内容？帮我查证 wikily.gg 上的更新日志

---

## 数据来源与许可（重要）

本仓库**混合了原创内容与第三方资料**，请区别对待：

| 内容 | 来源 | 说明 |
|---|---|---|
| 专家配置、`agents/hln-a.md`、README、`.gitignore` | 本仓库原创 | 原创部分按 `LICENSE`（MIT）授权 |
| BOSS 详情表（`references/ark-boss-table/`） | [Wikily ASA](https://wikily.gg/ark-survival-ascended)、[Wikily ASE](https://wikily.gg/ark-survival-evolved)、[ARK Official Community Wiki](https://ark.wiki.gg/)、[Teandy / 听宇网](http://www.teandy.com/boss.html) | 结构化整理与转录；数据文件内保留「数据来源由曲終人散的智能体HLN-A生成 仅供参考」及四个来源署名，**转载时请勿删除** |
| ARK-Supreme 资料（`references/ark-supreme/`） | 社区粉丝站 [rokiarknet](https://rokiarknet.github.io/ark-supreme.html)（非官方）；官方以 CurseForge + Discord 为准 | 攻略正文为中文翻译，含 544 条生物生成码、761 条物品生成码；第三方内容，权利归原作者 |
| 头像 `avatars/expert.png` | [ark.wiki.gg](https://ark.wiki.gg/) 的 HLN-A 官方形象图 | 游戏官方素材，仅作专家标识用 |

**转载边界**：`LICENSE` 仅覆盖本仓库原创部分，不覆盖上述第三方 Wiki 数据、粉丝站翻译、Teandy 数据与游戏官方素材。再分发时请保留各来源署名，并遵守来源站点的使用条款。若你是权利方且不希望相关内容出现在本仓库，请通过 GitHub Issue 联系，我会及时处理。

**准确性说明**：BOSS 表的血量、准入等级、能量元素、贡品数量已核对；神器贡品、战利品贡品、泰克印痕等长文本为转录，用于严肃攻略前建议对照 wikily.gg 或 ark.wiki.gg 复核。ARK-Supreme 数值基于 150 级、无增益、无服务器倍率，模组持续更新，最新机制以官方 Discord 为准。本资料**仅供参考，不构成官方攻略**。

---

## 免责声明

本仓库与 Studio Wildcard / ARK 官方、Wikily、ark.wiki.gg、Teandy、rokiarknet 均无隶属或授权关系。所有商标、游戏名称与素材归各自权利人所有。专家给出的数值与建议由 AI 生成，可能存在过时或误差，请以游戏内实际情况与官方资料为准。
