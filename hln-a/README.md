# HLN-A

《方舟：生存飞升》（ARK: Survival Ascended，ASA）与《方舟：生存进化》（ARK: Survival Evolved，ASE）全领域 AI 专家，覆盖生物驯服、建筑部落、地图探索、装备科技、传说剧情、版本更新、官方服务器倍率、服务器状态与 BOSS 数值速查。遇到不确定的内容会按优先级查证权威资料（wikily.gg 中文站 → ark.wiki.gg → survivetheark 官方论坛）。

本仓库地址为 **HLNA-Skill**。请注意：这是 **WorkBuddy 专属专家包**（`.codebuddy-plugin/plugin.json` 结构），不是通用 Skill；安装方式与数据来源见仓库根目录 `README.md`。

## 类型

Agent 型（单个 AI 专家）

## 功能

- 生物驯服与繁育：击晕/被动驯服、饲料优先级、麻醉饲养、突变与印加
- 建造与部落经营：建筑防御、资源采集、基地选址、PvP/PvE 策略
- 地图与探索：各官方地图的资源点、洞穴、BOSS 与方尖碑
- 装备制作与科技：Engram、配方、TEK 科技、鞍具附魔
- 版本更新与查证：跟踪补丁平衡改动，必要时按优先级用 WebFetch 核对（首选 wikily.gg 中文站 → 其次 ark.wiki.gg → 再次 survivetheark 官方论坛）
- 官方服务器倍率查询：优先 https://wikily.gg/zh-cn/ark-survival-ascended/rates/ ，其次 https://www.dododex.com/rates
- 服务器相关查询（开服天数/在线人数/状态/延迟）：https://ark.fusey.gg/ 、https://www.battlemetrics.com/servers/ark 、https://arkstatus.com/
- BOSS 详情速查：ASE / ASA 双版本完整数值表（血量、准入等级、贡品、能量元素、泰克印痕解锁、掉落物），见 `references/ark-boss-table/`
- 模组分类：目前收录 ARK-Supreme（ASA 大型 overhaul 模组），见 `references/ark-supreme/`

## 使用示例

- 帮我查询《方舟：生存飞升》里南巨（Giganotosaurus，南方巨兽龙）的驯服方法与注意事项
- 《方舟：生存进化》焦土（Scorched Earth）地图有哪些关键资源点和出生推荐？
- 最新版本方舟更新了哪些内容？帮我查证 wikily.gg 上的更新日志
- ASA 育母蜘蛛 α 困难给多少能量元素？需要哪些贡品？

## 目录结构

```
hln-a/
├── .codebuddy-plugin/plugin.json    # 专家注册信息（WorkBuddy 专有格式）
├── agents/hln-a.md                 # 专家人设、能力与知识入口
├── avatars/expert.png              # 头像
├── references/
│   ├── ark-boss-table/             # BOSS 详情表（ASE/ASA 双版本）
│   └── ark-supreme/                # ARK-Supreme 模组资料
└── README.md
```

## 头像

`avatars/expert.png` 为 **HLN-A 官方形象图**（来源：ark.wiki.gg 的 NoteHLN-A），512×512 透明 PNG。如需替换，要求：
- 格式：PNG（推荐）或 JPG
- 尺寸：512×512 px
- 大小：单张不超过 500KB

## 安装

前置条件：**WorkBuddy 桌面端**。将此目录整体放到你的专家目录下（路径因系统而异，`~` 代表用户主目录）：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/hln-a/
```

然后运行注册命令使其在「专家中心 → 我的专家」可见（脚本位于 WorkBuddy 安装目录的 `skills/expert-manager/scripts/register_expert.py`）：

```bash
python3 scripts/validate_expert.py <expert-dir>
python3 scripts/register_expert.py <expert-dir>
```

也可直接下载仓库中的 `hln-a.zip` 解压到上述目录。完整步骤见仓库根目录 `README.md`。

## 打包分享

```bash
zip -r hln-a.zip hln-a/
```

本包内的第三方资料（ARK-Supreme 攻略、BOSS 详情表）均标注了原始来源，转载与再分发请遵守来源站点要求，详见仓库根目录 README 的「数据来源与许可」章节。
