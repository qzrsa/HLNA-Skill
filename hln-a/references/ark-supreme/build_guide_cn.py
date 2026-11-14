import re, json, os, sys

# 一次性数据生成脚本：输入为 ARK-Supreme 资料页的本地 HTML 缓存，输出为中文版攻略 MD。
# 路径已参数化，不含任何本机绝对路径。用法: python build_guide_cn.py [输入HTML] [输出MD]
BASE = os.path.dirname(os.path.abspath(__file__))
HTML = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "as.html")
OUT  = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE, "ARK-Supreme-完整攻略与生成代码-中文版.md")

html = open(HTML, encoding="utf-8").read()

def grab(start_marker, end_marker):
    i = html.index(start_marker) + len(start_marker)
    j = html.index(end_marker, i)
    s = html[i:j].strip()
    return s.rstrip(";").strip()

CRE = json.loads(grab("const CREATURE_DATA=", "\nconst TIER_MAP="))
ITM = json.loads(grab("const ITEM_DATA = ", "\nconst ITEM_SUBCATEGORY_ORDER"))
ORDER = json.loads(grab("const ITEM_SUBCATEGORY_ORDER = ", "\nconst NAME_MAP"))

cre_by_tier = {}
for name, d in CRE.items():
    tier = name.split(" ", 1)[0]
    cre_by_tier.setdefault(tier, []).append((name, d))
for t in cre_by_tier:
    cre_by_tier[t].sort(key=lambda x: x[0])

itm_by_sub = {}
for name, d in ITM.items():
    sub = d.get("subcategory") or d.get("category") or "未分类"
    itm_by_sub.setdefault(sub, []).append((name, d))
ordered_subs = [s for s in ORDER if s in itm_by_sub]
for s in itm_by_sub:
    if s not in ordered_subs:
        ordered_subs.append(s)

# ---------- Chinese translation of the narrative guide ----------
GUIDE_CN = r"""# 第一部分：详细图文攻略（中文翻译）

> 以下为社区站 rokiarknet.github.io 攻略正文的中文翻译（原文为英文）。数值基于 150 级无增益、无服务器倍率。模组持续更新，最新机制以官方 Discord 为准。

## 基础设定 (baseline)
所有数值基于 **150 级、无增益** 的野生生物——不使用服务器倍率或自定义印记。默认你已掌握 ARK 基础机制。

## 等级列表 (tier-list)
完整进阶顺序（由低到高）：
**Elite（精英）｜ Savage（野蛮）｜ Toxic（剧毒）｜ Berserk（狂暴）｜ Necrotic（坏死）｜ Grenadier（榴弹）｜ Prime（至尊）｜ Nuclear（核）｜ Vampiric（吸血）｜ Wardens（守望者）｜ Hellfire（地狱火）｜ DarkGod（暗神）｜ Corrupted Darkgods（腐化暗神）｜ Spectral Wardens（光谱守望者）｜ Primordial（原初）**

## 开局 (getting-started)
出生自带 **40 秒护盾**——利用它观察地形、找掩护。
撑到能建立一个安全点为止——无论是木筏基地，还是藏在危险之外的偏僻陆地前哨。

### 核心制造建筑
- **Supreme Forge（至尊熔炉）**——熔炼金属与合金。
- **Supreme Bench（至尊工作台）**——制造 mod 装备、饲料(kibble)、Boss 物品、药水与消耗品的主工作站。
- **Supreme Bed（至尊床）**——复活点。

### 进阶循环 (The Progression Loop)
前三个阶层（Savage、Toxic、Berserk）遵循同一套循环：
1. **狩猎与采集**——击杀目标阶层的野生生物并采集它们的血
2. **制造麻醉剂**——用血制造对应阶层的镇静剂(tranqs)
3. **驯服**——击晕并驯服该阶层的生物
4. **建立卵场**——繁殖你的驯服龙以产出下一阶层饲料所需的蛋
5. **重复**——进入下一阶层，再来一遍

## 核心与精华 (cores-essence)
每只野生生物被击杀时掉落对应阶层的 **Dino Core（恐龙核心）**。**1 个恐龙核心 = 10 点 Essence（精华）**。
- **核心**用于制造 Boss 召唤物。
- **精华**是所有饲料配方中额外的必需材料（在循环已覆盖的蛋之外还需要它）。

## 精英阶 (elite)
你真正的起点。精英生物相比原版有小幅属性提升，在你准备挑战 Savage 阶时，是很好的早期过渡驯服对象。

## 野蛮阶 (savage)
你的第一个分层进度。狩猎 Savage 生物获取 Savage Blood（野蛮之血），制造 Savage Tranqs（野蛮麻醉剂），驯服你的第一批 Savage 恐龙。建立繁殖对来生产 Savage Eggs（野蛮蛋），用于制作 Toxic Kibble（剧毒饲料）。

## 野蛮 Boss (savage-boss)
Savage Boss 是你的第一个 Boss 门槛。击败后，它会刷出一个可用饲料驯服的版本。

### 野蛮蜗牛 (Savage Snail)
这只可驯服的 Savage Boss 会生产 **Savage Slime Balls（野蛮史莱姆球）**——从 Toxic 阶开始，所有饲料的制作都需要它。驯服这个 Boss 对进度推进至关重要。
- 喂浆果来生产史莱姆球
- 可进化成更小的版本，便于在基地存放
- 如果史莱姆停产，把它收进 pod 再重新放出即可恢复

## 剧毒阶 (toxic)
备好 Toxic Kibble 后，重复上述循环。采集 Toxic Blood（剧毒之血），制造 Toxic Tranqs（剧毒麻醉剂），驯服 Toxic 生物，并繁殖它们以生产 Berserk Kibble（狂暴饲料）。
Toxic 生物拥有造成眩晕的 AOE 能力——是击晕目标时替代麻醉剂的强力手段。
> 在推进此阶段时，开始种植作物——Berserk Kibble 会需要它们。

## 狂暴阶 (berserk)
同样的模式，但风险更高。Berserk 生物打得更狠、也更难打倒，但相应回报也更高。

### 狂暴三王 (Berserk Kings)
三个 Berserk King（狂暴王）把守通往 Necrotic 阶的入口：
- **King of the Swamps（沼泽之王）**——沼泽生物群系（sarco 变体）
- **King of the Grasslands（草原之王）**——草原/平原区域（giga 变体）
- **King of the Desert（沙漠之王）**——沙漠区域（deathworm 变体）

你必须从 **全部三只王** 各取得一个灵魂(soul)，才能把你的 Savage Snail 进化成 **Berserk Snail（狂暴蜗牛）**，它生产 Berserk Slime Balls（狂暴史莱姆球），用于 Necrotic 阶及之后所有饲料。
> 进化前先再驯一只 Savage Snail。从 Necrotic 阶起的饲料 **同时需要** Savage 和 Berserk 两种史莱姆球，所以你需要两只蜗牛并行运行。把唯一的蜗牛进化掉，你就无法再生产 Savage 史莱姆了。

**服务器 INI 设置**（`[ArkSupreme]` 段）——限制每只王同时存活在世界中的数量：
```
MaxKingOfTheDesert=3
MaxKingOfTheGrass=3
MaxKingOfTheSwamp=3
```

## 坏死阶 (necrotic)
到了 Necrotic，情况开始改变。这里解锁两套新系统：**Paragon Levels（至尊等级）**（用于培养已驯服的恐龙，见下文 FAQ）以及用于高阶制造的 **Queen Bee（蜂后）** 蜂蜜生产。

### 蜂蜜生产 (Honey Production)
野生蜂具有敌意，看到你就攻击。建立蜂蜜生产的步骤：
1. **击杀野生蜂**以收集少量蜂蜜
2. 在 Supreme Bench（至尊工作台）用这些蜂蜜 **制作 Necrotic Kibble（坏死饲料）**
3. **驯服一只 Queen Bee（蜂后）**，获得持续的蜂蜜产出

驯服后，把该阶层的稀有花（在 Supreme Bench 制作）放进蜂的背包——蜂会自动产蜜。
Queen Bee 在 Necrotic、Prime、Nuclear、Vampiric、Hellfire 和 DarkGod 各阶都有——每阶的蜂使用对应阶层的稀有花。

## 坏死 Boss (necrotic-boss)
Necrotic Boss 是一个 **Golem BOSS（石巨人 Boss）**，是通往 Grenadier 阶的门槛。
- **可驯服**：是——用饲料驯服
- **奖励**：击败该 Boss 解锁 Grenadier 饲料的印痕

## 榴弹阶 (grenadier)
Grenadier 阶引入了爆炸战斗机制。

### 榴弹令牌与工厂 (Grenadier Tokens & Factory)
野生 **Grenadier Bosses** 掉落 **Grenadier Token（榴弹令牌）** 和 **Grenadier Factory（榴弹工厂）**。要生产 **Grenadier Herb（榴弹草）**（Prime Kibble 的关键材料），工厂需要同时具备 Grenadier Token *和* 由 Grenadier Boss Tribesman（榴弹部落酋长）掉落的 **Chief Grenadier Token（首席榴弹令牌）**。

### 榴弹部落酋长 (Grenadier Boss Tribesman)
一个 **只能用 Grenadier 阶或更高阶已驯服龙** 才能对抗的敌对部落。其酋长掉落生产 Grenadier Herb 所需的 Chief Grenadier Token。

## 至尊阶 (prime)
Prime 阶设有作为通往 Nuclear 和 Vampiric 阶门槛的守护者(Guardian) Boss。

### 驯服 Prime 生物 (Taming Prime Creatures)
驯服 Prime 阶生物需要由 Grenadier Herb 制作的 Prime Kibble：
1. **收集 Grenadier Herb**——由 Grenadier Factory 生产（见上）
2. **制作饲料**——在 Supreme Bench 用 Grenadier Herb 制作 **Prime Kibble**
3. **驯服**——用对应的麻醉剂击晕 Prime 生物，喂 Prime Kibble

### Prime 守护者 (Prime Guardians)
存在三个守护者 Boss：Broodmother（育母蜘蛛）、Ferox、Spino（棘背龙）。
> Prime 阶 Boss 对 **非 tek 类型** 恐龙造成的伤害有减免——带 Prime（或更高 tek 阶）去打 Prime。

击败全部三个 Prime 守护者，解锁 Nuclear 和 Vampiric 饲料印痕。
现在击杀每个 Prime 守护者会在当场刷出一个 **可驯服变体**——可驯服的 Prime Broodmother、Ferox 和 Spino。每只可驯服的 Prime 守护者，在你到达 Primordial 阶后，都可 **进化成对应的 Primordial（原初）形态**。

## 核与吸血阶 (nuclear-vampiric)
Nuclear 和 Vampiric 生物 **无法用飞镖或箭麻醉**——它们需要对应阶层的火箭筒发射麻醉火箭(tranq rockets)才能击晕。

### 驯服流程 (Taming Flow)
1. **获取蓝图**——Nuclear 和 Vampiric 的 Tribesmen（部落人）掉落对应阶层火箭筒和麻醉火箭弹药的蓝图
2. **击晕**——用对应阶层的火箭筒装填麻醉火箭，把目标击晕
3. **喂饲料**——Nuclear 生物喂 Nuclear Kibble，Vampiric 生物喂 Vampiric Kibble

### 阶层锁定的麻醉 (Tier-Locked Tranqing)
火箭是 **1:1 阶层锁定** 的——Nuclear 火箭只麻醉 Nuclear 生物，Vampiric 火箭只麻醉 Vampiric 生物。不存在跨阶层麻醉。

| 阶层 | 麻醉武器 | 弹药 | 饲料 |
|------|----------|------|------|
| Nuclear（核） | Nuclear Rocket Launcher（核火箭筒） | Nuclear Rocket（核火箭） | Nuclear Kibble（核饲料） |
| Vampiric（吸血） | Vampiric Rocket Launcher（吸血火箭筒） | Vampiric Rocket（吸血火箭） | Vampiric Kibble（吸血饲料） |

## 守望者阶 (wardens)
Wardens 阶引入了"仅野生 Boss 生成"机制。

### 野生 Boss 生成 (Wild Boss Spawning)
击杀野生 Warden Boss 会在当场刷出一个可驯服版本——把它击晕，用对应饲料驯服。

### 可驯服守望巨兽 (Tameable Warden Kaiju)
击杀 Warden Kaiju（巨兽）Boss 会在当场刷出一只 **Tameable Warden Kaiju（可驯服守望巨兽）**。驯服后，它可 **进化成 Tameable Spectral Warden Kaiju（可驯服光谱守望巨兽）**。

### 光谱进化 (Spectral Evolution)
Wardens 进化为 Spectral Wardens——进化需求见下文 Spectral Wardens 章节。

## 地狱火阶 (hellfire)
Hellfire 生物使用基于传送门的攻击(portal-based attacks)。
击败 Hellfire Boss 解锁 DarkGod 饲料。

## 暗神阶 (darkgod)
DarkGods 通过使用 DarkGod King 掉落的 token 进化生物来获得。

### 暗神阵容 (DarkGod Lineup)
可用的 DarkGod 变体：Rex（霸王龙）、Spider（育母蜘蛛）、Crab（蟹）、Golem（石巨人）、**Griffin（狮鹫）** 和 **Reaper（死神）**。

### 暗神王 (DarkGod King)
**DarkGod King** 掉落 DarkGod token——进化 DarkGod 生物的关键物品。该 token 拾取半径很大，所以你不用精准落在尸体上。

### 暗神掉落 (DarkGod Drops)
击败野生 DarkGods 的奖励：大瓶 XP 药剂、随机生命药剂、随机麻醉剂、随机 DarkGod 阶鞍具。

## 腐化暗神阶 (corrupted-darkgods)
Corrupted DarkGods（腐化暗神）是用来对抗 Spectral Wardens 的最佳生物。

### 获取腐化暗神 (Obtaining Corrupted DarkGods)
Corrupted DarkGod 的 Rex、Broodmother、Golem、**Griffin** 和 **Reaper** **只能通过将对应的 DarkGod 进化获得**——它们不会在野外生成，也无法直接驯服。

### 腐化暗神王 (Corrupted DarkGod King)
击败 **Corrupted DarkGod King** 掉落用于把 Wardens 进化成 Spectral Wardens 的 token。

## 光谱守望者阶 (spectral-wardens)
Spectral Wardens 是 Wardens 的最终进化形态。

### 进化需求 (Evolution Requirement)
把 Warden 进化成 Spectral Warden 需要一个 **Corrupted DarkGod King token**，由 Corrupted DarkGod King 掉落（见上）。

### 光谱守望掉落 (Spectral Warden Drops)
击败野生 Spectral Wardens 的奖励：大瓶 XP 药剂、随机生命药剂、随机麻醉剂、随机光谱守望鞍具。

## 光谱阶梯 Boss (spectral-tiered-boss)
**Spectral Tiered Boss**——一只巨大的 Spectral Kraken（光谱海妖）——是 Spectral Wardens 与 Juggernaut 之间的新门槛。击败它解锁召唤 Juggernaut 所需的物品。
**召唤方式：** 在 Bench 制作的 Spectral Kraken 召唤物。

## 主宰者阶 (juggernaut)
Juggernaut 位于 Spectral Wardens 与新的 Primordial 阶之间。通过击败 Spectral Tiered Boss 解锁。

### Boss 战 (Boss Fight)
Juggernaut 的实力与 Spectral Wardens 相当，是重大挑战。击败它掉落 **Tameable Juggernaut Saddle（可驯服主宰者鞍）** *以及* **Primordial Factory（原初工厂）**——解锁 Primordial 阶的建筑。

### 可驯服主宰者 (Tameable Juggernaut)
Juggernaut Boss 被击败后，会刷出一只 **Tameable Juggernaut（可驯服主宰者）**。用 **Juggernaut Kibble** 驯服它。

## 原初阶 (primordial)
Primordial 是新的终局阶层——由 Juggernaut 掉落的 **Primordial Factory** 解锁。

### 原初生物 (Primordial Creatures)
有八种 Primordial 驯服对象：**DefenseUnit、Ferox、Mammoth、Griffin、Broodmother、Spino、Saber、Wyvern**。每种也作为 **野生 BOSS 变体** 在世界中生成。

### 进化路径 (Evolution Path)
每只 Primordial 生物都是通过 **用 Primordial Cube（原初方块）进化其 Prime 对应体** 获得——Prime DefenseUnit → Primordial DefenseUnit，Prime Ferox → Primordial Ferox，依此类推。在 Prime 守护者阶段驯服的可驯服 Prime 守护者（Broodmother、Ferox、Spino）可直接用于此进化。

### 原初工厂 (Primordial Factory)
**Primordial Factory**（由 Juggernaut 掉落）生产 **Primordial Cube（原初方块）**——把 Prime 驯服龙转化为 Primordial 形态所需的进化催化剂。模式与 Grenadier Factory 生产 Grenadier Herb 相同。

## 原初神明 (primordial-deity)
**Primordial Deity（原初神明）** 是进阶的新最终 Boss。它 **会飞**——带飞行坐骑去。

### 可驯服原初神明 (Tameable Primordial Deity)
Primordial Deity 被击败后，会刷出一只 **Tameable Primordial Deity（可驯服原初神明）**。它在普通招式之外 **额外拥有 3 个特殊攻击**——最后一个特殊攻击使用 **X** 键（手柄用 **左摇杆**）。

## 常见问题 (faq)

### Boss 战斗 (Boss Combat)
所有地面 Boss 都会把飞行坐骑击落（10 秒冷却）——打 Boss 时带地面坐骑。飞龙型 Boss（Wyverns 飞龙、Manticores 蝎狮）是例外，不会把你击落。

### 工具采集率 (Tool Harvest Rates)

| 阶层 | 采集倍率 |
|------|----------|
| Savage（野蛮） | 1.5x |
| Toxic（剧毒） | 2x |
| Berserk（狂暴） | 2.5x |
| Necrotic（坏死） | 3x |
| Prime（至尊） | 3.5x |
| Hellfire（地狱火） | 4x |

*Hellfire 工具使用自定义材料。*

### 护甲评级 (Armor Ratings)

| 阶层 | 评级 |
|------|------|
| Savage（野蛮） | 60 |
| Toxic（剧毒） | 100 |
| Berserk（狂暴） | 200 |
| Necrotic（坏死） | 300 |
| Prime（至尊） | 400 |
| Hellfire（地狱火） | 600 |

*每件。所有分层护甲均为无限耐久。*

### 部落人与掠夺 Boss (Tribesman & Lootbosses)
在野外生成、击杀后掉落珍贵战利品的敌对 NPC。每个部落人阶层掉落的物品都按自身阶层缩放。

**部落人阶层**（适用时有随从 Minion 和酋长 Chief 变体）：Savage、Toxic、Berserk、Necrotic、Grenadier、Prime

**Boss 部落人**：**Grenadier Boss Tribesman（榴弹 Boss 部落人）**——掉落 Grenadier Factory 生产 Grenadier Herb 所需的 **Chief Grenadier Token（首席榴弹令牌）**。只能用 Grenadier 阶或更高阶已驯服龙对抗。

**骑乘变体**——在更高阶层，部分部落人骑着坐骑恐龙投入战斗。

**通用掉落**——每个部落人掉落与其阶层匹配的混合物品：XP 药剂（尺寸随阶层缩放：Tiny → Medium → High → Extra Large）、生命药剂、本阶及以下的麻醉剂、本阶的鞍具/护甲/工具、从 Berserk 阶起的高品质武器（制式狙击枪、长管步枪等）、弹药与弹药材料（Grenadier Boss Tribesman）、Taming Cakes（驯服蛋糕 x50 / x100 / x250，驯服时瞬间清除饱食度）。

**值得注意的额外掉落**：Necrotic 部落人还会掉落可驯服的 Necrotic Boss 鞍具；Prime 部落人极度危险；Prime 之后，Boss 阶生物（Wardens、Spectral Wardens）会掉落你尚未解锁的更高阶鞍具——但 Nuclear、Vampiric、Hellfire 的鞍具不在掉落池内。

### 部落人侵略性 (Tribesman Aggression)
现在所有部落人一见你就立刻敌对——无需挑衅。当你攻击某个部族时，邻近部族的部落人会加入互相防御。规划战斗时要考虑侧翼包抄。

### 至尊等级 (Paragon Levels)
从 Necrotic 阶起，你的驯服龙可以 **通过 10 个 Paragon Levels（至尊等级）进行培养**——这是叠加在正常驯服之上的一套独立进度。更高等级提升属性并解锁新能力。

**等级进度**——通过用你的龙击杀野生生物来升级。专用 UI 显示当前 Paragon 等级及下一级进度。截至 2026-08-29 补丁，每个等级所需击杀数在各阶层（Necrotic → Spectral）都已下调。

| 等级 | 奖励 |
|------|------|
| 1–4 | 每级属性提升 |
| 5 | 属性提升 + 解锁 **Powerup Ability（强化能力）**（需用该龙击败一个 Paragon Boss） |
| 6–9 | 每级属性提升 |
| 10 | 解锁该龙的 **Supreme 版本**——大幅属性升级 |

**Powerup Ability（强化能力）**——Necrotic 阶及以上的龙在驯服时处于 **弱化(powered down)** 状态。完成 Paragon 5 级 *并且* 用该龙击败一个 Paragon Boss 后，一个按键组合会解锁，可在强化与弱化状态间切换。强化状态下有视觉变化、**+30% 抗性** 和速度提升。

**Paragon Bosses**——在更高阶层可召唤 80 个 Paragon Bosses。每次召唤刷出一只随机更高阶生物且其强化能力激活——这些就是你在 5 级解锁龙强化能力所需的门槛。强化能力在 Necrotic 及以上的每个阶层都可用：Necrotic、Grenadier、Prime、Nuclear、Vampiric、Wardens、Hellfire、DarkGod、Corrupted DarkGod 和 Spectral Wardens。

### 敌对系统 (Hostile System)
击杀部落人会触发一个 **敌对计数器**（图标出现在右下角）。随着敌意增加（x2、x4 等），更多部落人会主动追杀你，武器也会从长矛逐步升级到长管步枪。这个增益 **按设计是永久的**——不会衰减或清除——这个系统存在的目的，就是让部落人持续对触发它的玩家保持侵略性。
"""

CN_TIER = {
    "Elite":"精英","Savage":"野蛮","Toxic":"剧毒","Berserk":"狂暴","Necrotic":"坏死",
    "Grenadier":"榴弹","Prime":"至尊","Nuclear":"核","Vampiric":"吸血","Wardens":"守望者",
    "Warden":"守望者","Hellfire":"地狱火","DarkGod":"暗神","Darkgod":"暗神","Corrupted":"腐化暗神",
    "Spectral":"光谱","Primordial":"原初","Lootbosses":"掠夺Boss","Berserk Kings":"狂暴三王",
    "Tier Bosses":"阶层Boss","Bee Progression":"蜂群进度","Special Spawns":"特殊生成",
}
CN_SUB = {
    "Standard Tier Kibbles":"标准阶层饲料","Boss Kibbles":"Boss 饲料","Trait Kibbles":"特性饲料",
    "Sushi Kibbles":"寿司饲料","Health Potions":"生命药剂","XP Potions":"经验药剂",
    "Buffs & Elixirs":"增益与灵药","Narcotics":"麻醉剂","Taming Helpers":"驯服辅助",
    "Survival Aids":"生存辅助","Tier Boss Summons":"阶层 Boss 召唤物","Tameable Boss Summons":"可驯服 Boss 召唤物",
    "Mini-Boss Tameable Scrolls":"迷你 Boss 驯服卷轴","Tier Boss Tokens":"阶层 Boss 令牌",
    "Godly Boss Tokens":"神明 Boss 令牌","Boss Skulls":"Boss 头骨","Boss Essences":"Boss 精华",
    "Dino Cores":"恐龙核心","Elemental Cores":"元素核心","Dino Essences":"恐龙精华",
    "Elemental Essences":"元素精华","Blood":"血液","Hide":"皮革","Loot Quality Keys":"战利品品质钥匙",
    "Elemental Fruits":"元素果实","Rare Flowers":"稀有花","Honey":"蜂蜜","Seeds":"种子","Feather":"羽毛",
    "Raw Prime Meat":"生 Prime 肉","Ores":"矿石","Ingots":"铸锭","Souls":"灵魂","Lore Notes":"背景笔记",
    "Evolutions":"进化物品","Tranq Darts":"麻醉飞镖","Tranq Rockets":"麻醉火箭","Sniper Bullets":"狙击子弹",
    "Compound Bow Arrows":"复合弓箭","Basic Tranq Arrows":"基础麻醉箭","Plasma Netgun Ammo":"等离子网枪弹药",
    "Modded Metal Tools":"改版金属工具","Special Weapons":"特殊武器","Utility Tools":"实用工具",
    "Other Weapons":"其他武器","Lesser Charms":"次级护符","Greater Charms":"高级护符","Other Charms":"其他护符",
    "Workstations":"工作站","Crop Plots":"作物田","Furniture":"家具","Rafts":"木筏","Spike Walls":"尖刺墙",
    "Godly Building Set":"神明建筑套件","Titan Eggs":"泰坦蛋","Other Structures":"其他建筑",
    "Cloth Armor":"布甲","Desert Cloth Armor":"沙漠布甲","Hide Armor":"皮甲","Flak Armor":"板甲",
    "Fur Armor":"毛皮甲","Ghillie Armor":"吉利服","Riot Armor":"防暴甲","Scuba Armor":"潜水甲",
    "Chitin Armor":"甲壳甲","Tek Armor":"Tek 甲","Kevlar Armor":"凯夫拉甲","Plate Armor":"重板甲",
}

def esc(s): return (s or "").replace("|","\\|")

L = []
L.append("# ARK Supreme（方舟生存飞升）完整攻略【中文版】+ 全量生成代码\n")
L.append("> 资料来源：社区站 https://rokiarknet.github.io/ark-supreme.html （第三方粉丝站，非官方；官方以 CurseForge + Discord 为准）\n")
L.append("> 数据基于模组实际资产提取；数值按 **150 级无增益、无服务器倍率** 标注。模组持续更新，最新机制请以官方 Discord 为准。\n")
L.append(f"> 本文件含 **{len(CRE)}** 条生物生成代码、**{len(ITM)}** 条物品生成代码。攻略正文已译为中文；生物/物品名为英文原名（控制台指令须原样复制）。\n")

L.append("\n---\n")
L.append(GUIDE_CN)

# ===== Part 2: creature codes =====
L.append("\n\n---\n")
L.append("# 第二部分：生物生成代码（全量）\n")
L.append("使用说明：\n")
L.append("- `召唤(野生)` = `cheat summon <类名>`：在身边生成一只野生。\n")
L.append("- `召唤(驯服)` = `admincheat GMSummon \"<类名>\" 150`：直接生成一只 150 级已驯服。\n")
L.append("- `SpawnDino` = `cheat spawndino \"<蓝图路径>\" X Y Z 等级`：在指定坐标生成（示例坐标 500 0 0）。\n")
L.append("- `Game.ini 屏蔽`：写入 Game.ini 可让该生物不再自然刷新。\n\n")

for tier in sorted(cre_by_tier.keys()):
    cn = CN_TIER.get(tier, tier)
    L.append(f"\n## {tier} 阶 / {cn}（{len(cre_by_tier[tier])} 种）\n")
    L.append("| 生物(英文名) | 蓝图类名 | 召唤(野生) | 召唤(驯服) | SpawnDino | Game.ini 屏蔽 |\n")
    L.append("|---|---|---|---|---|---|\n")
    for name, d in cre_by_tier[tier]:
        L.append(f"| {esc(name)} | `{esc(d.get('blueprint',''))}` | `{esc(d.get('summonWild',''))}` | `{esc(d.get('summonTamed',''))}` | `{esc(d.get('spawnDino',''))}` | `{esc(d.get('disable',''))}` |\n")

# ===== Part 3: item codes =====
L.append("\n\n---\n")
L.append("# 第三部分：物品生成代码（全量）\n")
L.append("使用说明：\n")
L.append("- `生成(gfi)` = `cheat gfi <物品ID> 1 0 0`：直接获得 1 个物品。\n")
L.append("- `类名`：可用于蓝图/高级指令。`蓝图路径`：完整资产路径。\n")
L.append("- `Game.ini 屏蔽`：用 `OverrideNamedEngramEntries` 可隐藏/移除该印痕。\n\n")

for sub in ordered_subs:
    items = itm_by_sub[sub]
    cn = CN_SUB.get(sub, "")
    label = f"{sub}（{cn}）" if cn else sub
    L.append(f"\n## {label}（{len(items)} 项）\n")
    L.append("| 物品(英文名) | 生成(gfi) | 类名 | 蓝图路径 | Game.ini 屏蔽 |\n")
    L.append("|---|---|---|---|---|\n")
    for name, d in sorted(items, key=lambda x: x[0]):
        eng = d.get("engramName") or name
        L.append(f"| {esc(eng)} | `{esc(d.get('spawn',''))}` | `{esc(d.get('class',''))}` | `{esc(d.get('blueprintPath',''))}` | `{esc(d.get('disable',''))}` |\n")

out = "".join(L)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(out)
print("WROTE", OUT, "bytes=", len(out.encode("utf-8")))
print("creatures=", len(CRE), "items=", len(ITM), "subs=", len(ordered_subs))
