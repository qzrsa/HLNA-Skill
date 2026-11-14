# 方舟 BOSS 信息表 · 帖子导入交接包

生成时间：2026-11-14
用途：在目标网站上新建一篇帖子并导入「方舟 BOSS 信息详情表（ASE / ASA 双版本独立完整表）」。

**本包完全自包含**：不依赖任何外部站点、不依赖抓取脚本、不依赖本机临时目录，也不含任何图片附件。下游分支解压即可操作。

数据参考站点（页脚「数据来源与参考」一行、以及「版本分区与数据来源」面板内都要保留，**不要删**）：
- https://wikily.gg/ark-survival-ascended （ASA）
- https://wikily.gg/ark-survival-evolved （ASE）
- https://ark.wiki.gg/ （ARK Official Community Wiki）

页脚在保留上面三个链接的基础上：
- 在同一行「数据来源与参考」末尾追加第四个来源，显示名字 `Teandy`、指向 `http://www.teandy.com/boss.html`，紧接在 ARK Official Community Wiki 后面，用 ｜ 分隔
- 另起一行「数据来源由曲終人散的智能体HLN-A生成 仅供参考」
- 顶部徽章与「版本分区与数据来源」面板的「参考站点」行，在三个 Wiki 之后加「听宇网」（同样指向 `http://www.teandy.com/boss.html`）
- 不再单独占一行重复写这个网址

**注意**：这三个 Wiki 链接是原来的数据来源，属于「保留」而非「替换」；同时不要加回署名、旧版本标记、版权或转载声明。

---

## 一、直接复制给另一个分支的指令

把下面整段原样发给负责发帖的分支，不需要额外补充上下文：

```
你要在目标网站上新建一篇帖子并导入一篇「方舟 BOSS 信息详情表（ASE / ASA 双版本独立完整表）」。

素材已全部放在当前工作目录的 ark-boss-post/ 中（若收到的是 zip，先解压）。请先完整阅读 HANDOFF.md，然后按其中「导入路径决策」选择对应文件，不要重新抓取网页、不要改写任何数值、不要添加或删除数据条目。

执行要求：
1. 先确认目标站点类型（WordPress / Typecho / Hexo-Hugo-Ghost 等静态博客 / 自托管 HTML / 论坛）。无法确认时，默认使用 post-static.html（兼容性最强），或直接询问站点类型。
2. WordPress 或 Typecho：用后台「工具 → 导入 → WordPress」导入 wordpress.xml，它会自动生成一篇状态为 draft 的草稿帖。导入后预览检查，再发布。
3. 自托管站点或自定义 CMS：优先粘贴 post.html（交互版，含 ASE/ASA 版本切换、搜索、地图标签、难度筛选），整段复制进文章正文的 HTML／源码模式。若编辑器会过滤 <script>，改用 post-static.html（零脚本，两版本完整表并列）。
4. 静态博客：使用 post.md，正文已按 ASE / ASA 分成两章。
5. 程序化导入：读取 boss-data.json（含 bosses 与 asa_bosses 两组独立数据）或三份 CSV 自行构造文章。
6. 发布前按 HANDOFF.md 的「校验清单」逐项检查；保留页脚原来的三个 Wiki 数据来源链接，并在同一行末尾追加名字为 Teandy 的第四个来源链接（指向 http://www.teandy.com/boss.html），另加「数据来源由曲終人散的智能体HLN-A生成 仅供参考」；「参考站点」行追加「听宇网」。
7. 完成后报告：帖子标题、URL 或 ID、使用的文件、发布状态。

约束：
- ASE（方舟：生存进化）与 ASA（方舟：生存飞升）是两张互不引用的独立数据表，各有完整表与各自的地图范围，禁止混用、禁止把 ASE 数值标成 ASA、禁止把 ASE 独有地图放进 ASA 表。
- ASA 独占 BOSS 的血量／贡品／元素／印痕均已按各自 Wiki 页面补齐，**不要再用 ASE 数值覆盖**；其中 Wiki 确实没写的字段（如 Nunatak 的元素与掉落物）写「Wiki 未列出」，保留原样，不要自行补数。
- 不要改变血量、等级、能量元素、贡品数量等任何数值；不要把已展开的解锁内容改回省略写法。
- 神器贡品与战利品贡品是表格常驻列，不要改成折叠或点击展开。
- 贡品数量列已把原表未写出具体数量的行全部补齐为按战利品贡品列顺序对应的实际数字（用 / 分隔），不要改回笼统标注。
- 「关于角色最高等级」有 ASE / ASA 切换，两版机制与上限都不同，不要合并或互换。
- Astraeos 地图显示为「阿斯特赖俄斯/星曜/繁星」，三者是同一张地图的不同中文译名，不要拆成三张地图。
- 保留页脚原来的三个 Wiki 数据来源链接（不要删），并在同一行末尾追加第四个来源链接，显示名字 Teandy、指向 http://www.teandy.com/boss.html；另加「数据来源由曲終人散的智能体HLN-A生成 仅供参考」；「参考站点」行加「听宇网」。不要加回旧版本标记、版权或转载声明。
```

---

## 二、版本分区说明（重点）

页面顶部有 **ASE / ASA 两个版本按钮**，对应两张互不引用的独立完整表：

| 分区 | 地图范围 | 规模 | 数据性质 |
| --- | --- | --- | --- |
| **ASE · 方舟：生存进化** | 12 张地图 | 25 个 BOSS / 63 行 | 完整数值表，省略提示已全部展开为实际内容 |
| **ASA · 方舟：生存飞升** | 10 张已发布官方地图及官方收录 DLC 地图 | 22 个 BOSS / 60 行 | 独立完整表，含 ASA 独占 BOSS |

切到 ASA 时，ASE 整块（含标题、搜索框、地图标签、25 张卡片）完全隐藏；反之亦然。两区在页面、Markdown、CSV、JSON 中都是分开的数据结构。

### 关于角色最高等级（两套机制，页面可切换）

「关于角色最高等级」一节有独立的 **ASE / ASA 切换按钮**，并与顶部版本切换联动。无脚本环境下两套说明并列显示，不丢数据。依据 `ark.wiki.gg/wiki/Leveling` 的 Max Levels 段：

| 版本 | 上限 | 关键来源 |
| --- | --- | --- |
| **ASE** | 205 级（preaquatica 分支）；含 Aquatica 的当前分支 Steam 版 220 级 | 105 基础 + 5 场 α 困难飞升各 +15 + 探险笔记 +10 + 维京 200 符文 +10 + chibi 6 级 +5；Steam 版再 +15（α Pygocentrus） |
| **ASA** | 245 级（官方 Wiki 截至 2026-08-28） | 105 基础 + 7 项 α 困难飞升各 +105 + Bob's Tall Tales 笔记 ×3 共 +15 + Tides of Fortune 笔记 +5 + 常规笔记 +10 + chibi +5 |

ASA 多出的部分来自君王泰坦、失落之王、Astraeos 双 Kraken 与 DLC 笔记；ASA 没有维京符文、创世纪 II 终极罗克韦尔与 Pygocentrus。**不要把 ASE 的 205 级当成 ASA 上限**。

### ASA 地图范围（截至 2026-11-14 已发布）

| 地图 | 英文 | 发布 | 类型 |
| --- | --- | --- | --- |
| 孤岛 | The Island | 2023-10-25 | 本体 |
| 焦土 | Scorched Earth | 2024-04-01 | 免费 |
| 中心岛 | The Center | 2024-06-04 | 免费 |
| 畸变 | Aberration | 2024-09-05 | 免费 |
| 灭绝 | Extinction | 2024-12-20 | 免费 |
| 阿斯特赖俄斯/星曜/繁星 | Astraeos | 2025-02-14 | 付费 DLC |
| 仙境 | Ragnarok (Ascended) | 2025-06-20 | 免费 |
| 瓦尔盖罗 | Valguero (Ascended) | 2025-10-07 | 免费 |
| 失落殖民地 | Lost Colony | 2025-12-19 | 付费 DLC |
| 创世纪 I | Genesis: Part 1 | 2026-07-03 | 免费 |

**仅 ASE 有、ASA 未发布的地图不列入 ASA 表**：水晶岛 Crystal Isles、失落岛 Lost Island、维京 / 菲尤尔 Fjordur、创世纪 II Genesis: Part 2。页面 ASA 说明区也列出了这四张，避免读者误以为漏了。

### ASA 数据口径（务必如实理解）

1. 官方 Wiki 的 Drops / Inventory 表按 **「ARK: Survival Ascended」与「ARK: Survival Evolved」两个 tab 分列**，两套能量元素数值**并不相同**（例：育母蜘蛛 ASE 20/56/148、ASA 24/68/178）。本表 ASE 取 evolved 栏、ASA 取 ascended 栏，**不互相套用**。
2. 该页同时明确了 ASA 的 **BOSS 阵容替换**：仙境竞技场改为 **Nunatak**（不再是喷火龙＋狮身蝎尾兽），瓦尔盖罗改为 **Grendel**（不再是三合一）；中心岛 BOSS 相同但竞技场更小更简单。ASA 表按此替换，未沿用 ASE 阵容。
3. **ASA 独占 BOSS 的数值已全部补齐**：Nunatak、Grendel、Lost King + Lost Queen，以及 Astraeos 的 Natrix / Thodes / Hydraskos / Manticore / Abyssalus / Shallocis，共 9 个条目。血量、准入等级、贡品、贡品数量、能量元素、泰克印痕解锁均取自各自 Wiki 页面，**全包已无「暂无数据」**。
4. **ASA 与 ASE 的元素差异（表内已按 ASA 栏替换）**：

| 地图 | BOSS | γ 简单 | β 中等 | α 困难 | ASE 对照 |
| --- | --- | --- | --- | --- | --- |
| 孤岛 | 育母蜘蛛 | 24 | 68 | 178 | 20 / 56 / 148 |
| 孤岛 | 大金刚 | 48 | 132 | 264 | 40 / 110 / 220 |
| 孤岛 | 喷火龙 | 96 | 264 | 528 | 80 / 220 / 440 |
| 焦土 | 狮身蝎尾兽 | 68 | 244 | 514 | 38 / 135 / 285 |
| 畸变 | 罗克韦尔 | 48 | 132 | 264 | 不掉落 |

5. **能量元素显示「-」的含义**：监察者、莫德尔、腐化主宰、终极罗克韦尔经官方 Wiki 明确注明不掉落元素；四只泰坦的元素只在随机战利品箱里出现（40%~60% 概率、每次 1~3 个），没有固定产出。
6. ASA 表的数据状态分四类：`standard`（与 ASE 数值一致）、`confirmed_diff`（元素已按 ASA 栏替换）、`wiki`（ASA 独占 BOSS，取自 Wiki 专属页面）、`noelement`（官方注明不掉元素）。JSON 与 `asa-boss-table.csv` 都有 `data_status` 字段。
7. **非竞技场战斗单位**：另有 14 个没有 Gamma/Beta/Alpha 三档的单位（ASE 侧 7 个：仙境地下城的冰虫女王 / 熔岩元素 / 幽灵恐熊与幽灵恐狼、创世纪 II 的 4 个任务 BOSS；ASA 侧 7 个：Astraeos 的世界 BOSS 塔纳托斯与 4 个小 BOSS、失落殖民地的奴仆与巨链兽），单独排在每张表末尾的独立分区，**不计入主表行数统计**。

**无脚本降级**：若目标 CMS 过滤 `<script>`，`post.html` 不会丢失任何数据——两张完整表会并列显示（ASE 全表 + ASA 全表），顶部出现一条提示，只是无法点击切换与筛选。需要切换能力请使用支持脚本的环境；纯静态场景建议直接用 `post-static.html`。

---

## 三、文件清单

| 文件 | 用途 | 是否自包含 |
| --- | --- | --- |
| `HANDOFF.md` | 本说明，下游必读 | — |
| `wordpress.xml` | WXR 导入文件，直接生成草稿帖 | 是（正文为内联 HTML） |
| `post.html` | **推荐**，交互式文章片段：版本切换 / 搜索 / 地图标签 / 难度筛选 | 是，HTML+CSS+JS+全表全内联，零外部请求 |
| `post-static.html` | 兜底版：零脚本，ASE 与 ASA 两张完整表并列 | 是 |
| `index.html` | 完整独立页面，内容与 `post.html` 一致，用于本地预览或直接发布 | 是 |
| `post.md` | Markdown 版，供 Hexo / Hugo / Ghost / 语雀等使用 | 是 |
| `boss-data.json` | 结构化数据，含 `bosses`（ASE）与 `asa_bosses`（ASA）两组独立数组，以及 `special_bosses`（14 个非竞技场单位） | 是 |
| `boss-table.csv` | ASE 63 行平表，UTF-8 BOM | 是 |
| `asa-boss-table.csv` | ASA 60 行平表，含「数据状态」列 | 是 |
| `asa-differences.csv` | ASA 5 条元素差异与 ASE 对照 | 是 |
| `tools/data.py` | 数据定义（含占位展开与 ASA 数据集构建） | — |
| `tools/wiki_data.py` | 官方 Wiki 抓取结果：ASE/ASA 两套能量元素、9 个 ASA 独占 BOSS 全量数据、14 个特殊 BOSS、ASE 掉落物。**自动生成，勿手改** | — |
| `tools/sync_wiki.py` | 把 `tools/_*.json` 抓取结果合成 `wiki_data.py`，`python tools/sync_wiki.py` | — |
| `tools/build.py` | 构建脚本，`python tools/build.py` 重生成全部文件 | — |

**所有版本都不引用图片或外部资源**，粘贴后即可完整使用。

优先级：`wordpress.xml`（一键建帖） > `post.html`（交互体验最好） > `post-static.html`（兼容性最好）。

---

## 四、导入路径决策

| 目标环境 | 使用文件 | 操作 |
| --- | --- | --- |
| WordPress | `wordpress.xml` | 后台 → 工具 → 导入 → WordPress → 选择文件 → 上传。生成 draft 草稿，标签 BOSS / ASE / ASA / 数据表 |
| Typecho / 其他支持 WXR 的博客 | `wordpress.xml` | 同上 |
| 自托管 CMS / 企业站后台 | `post.html` | 切到「HTML 源码」模式，整段粘贴，先预览 |
| 会过滤 `<script>` 的编辑器 / 论坛 | `post-static.html` | 整段粘贴；若 `<style>` 也被过滤，原生 `<table>` 结构仍可读 |
| Hexo / Hugo / Ghost / 语雀 | `post.md` | 放入 content/posts，自行添加 front-matter |
| 需要入库 / API 发帖 | `boss-data.json` 或三份 CSV | 按字段字典映射 |

---

## 五、数据字段字典

`boss-data.json` 顶层：

- `meta`：标题、副标题、生成时间、ASE 规模（25 / 63 / 12）、ASA 规模（22 / 60 / 10）、差异条数、校对状态
- `game_versions`：两个版本对象，字段 `id / short / name / en / source / desc`
- `data_credit` / `original_page` / `original_page_name`：页脚的署名说明「数据来源由曲終人散的智能体HLN-A生成 仅供参考」、原表网址与其链接名 `Teandy`（原有三个 Wiki 链接见 `sources`，保持不变）
- `qty_note`：贡品数量列的读法说明
- `level_notes`：对象，含 `ase` / `asa` 两个数组（两版等级上限机制）
- `asa_extra_notes`：对照官方 Wiki 补齐的 6 条核对说明
- `sources`：三个原有的数据来源站点，`name / url / version`（页脚「数据来源与参考」一行仍全部保留）
- `maps`、`bosses`：**ASE** 的 12 张地图与 25 个 BOSS
- `asa_maps`、`asa_bosses`：**ASA** 的 10 张地图与 22 个 BOSS（独立数组，不引用 `bosses`）
- `asa_not_available`：仅 ASE 有、ASA 未发布的 4 张地图
- `asa_status_text`：`standard / confirmed_diff / wiki / noelement` 四种状态说明
- `asa_variants`：5 条 ASA / ASE 元素差异
- `special_bosses`：14 个非竞技场战斗单位
- `arena_rules`、`source_notes`：规则与版本说明文字
- `difficulties`：`gamma` γ简单、`beta` β中等、`alpha` α困难、`single` 单一难度

`bosses[]` 与 `asa_bosses[]` 的条目结构相同：

| 字段 | 含义 |
| --- | --- |
| `game_version` | `ase` 或 `asa` |
| `data_status` | 仅 ASA 有：`standard` / `confirmed_diff` / `wiki` / `noelement` |
| `map` | 对应各自地图数组的 `id` |
| `name` / `en` | 中文名 / 英文名 |
| `artifacts` | 神器贡品（表格常驻列） |
| `trophies` | 战利品贡品（表格常驻列）；部分条目以 γ/β/α 前缀区分难度 |
| `trophies_detail` | 可选，按难度给出的逐项贡品数量说明 |
| `artifacts_by_diff` | 可选，神器分档不同时的逐档覆盖（格伦德尔、纳特里克斯） |
| `trophies_by_diff` | 可选，战利品分档不同时的逐档覆盖（格伦德尔、努纳塔克、失落之王 + 失落女王）。有值时该档只显示本档需要的项目，数量与本档项目一一对应 |
| `drops` | 掉落物（Drops 段固定掉落，不含随机战利品箱） |
| `arena` | 竞技场名称 |
| `note` | 可选备注，直接显示在卡片底部 |
| `rows[]` | 难度行 |

`rows[]`：

| 字段 | 含义 | 取值说明 |
| --- | --- | --- |
| `diff` | 难度键 | `gamma` / `beta` / `alpha` / `single` |
| `hp` | BOSS 血量 | 含「本体 / 触手」「A / B」双值时以字符串保留；组合 BOSS 已按组成 BOSS 展开为 `432000 / 100000` 形式 |
| `level` | 允许玩家进入等级 | 未填为 `-` |
| `qty` | 贡品数量 | 单个数字＝每种贡品各需该数量；用 `/` 分隔的一组数字＝按 `trophies` 列的项目顺序逐项对应。原表未写出具体数量的行已全部补齐为实际数字，全包不再出现笼统标注 |
| `element` | 战胜后获得的能量元素 | 未给为 `-` |
| `unlock` | 解锁泰克印痕 / 飞升植入体 / 奖励 | 已全部展开为实际项目，无省略提示 |
| ASA 独占条目 | 上述 4 个数值字段 | 全部为官方 Wiki 实际数值；Wiki 未列出的字段写 `Wiki 未列出`，不填推测值 |

`special_bosses[]`：`key / map / name / en / category / hp / level / artifacts / trophies / element / drops / note`。`category` 为「地下城 BOSS」「任务 BOSS」「世界 BOSS」「小 BOSS」「竞技场随从」之一。

CSV：`boss-table.csv` 一行 = 一个 ASE BOSS 的一个难度（63 行 + 表头，含「掉落物」列）；`asa-boss-table.csv` 同理（60 行 + 表头，多一列「数据状态」）；`asa-differences.csv` 为 5 行差异。

### 分档贡品与解锁的两条写法约定（易错，务必保留）

**一、官方表的「0」不能直接照抄。**
官方 Wiki 的 Tribute Requirements 是一张三列表（Gamma / Beta / Alpha），用 `0` 表示该档不需要该物品。照抄会让读者以为「α 档既要顶级符印又要次级符印」，也让数量列出现一串 0。
处理方式：按档拆开，每档只列本档真正需要的项目，数量与项目重新一一对应。

- `tools/sync_wiki.py` 的 `PER_DIFF`：格伦德尔（神器 3/3/4 + 战利品分档）、努纳塔克（γ 无战利品）。
- `tools/sync_wiki.py` 的 `ZERO_SPLIT` + `split_zero_rows()`：失落之王 + 失落女王（同名 9 项、靠 0 区分档位，自动剔除 0 项）。
- 构建端 `build.py` 的 `card_html()` 与 `csv_rows()` 已支持 `trophies_by_diff`；`check.py` 断言「每档战利品项目数 == 数量项数」且全包不含 0 数量。

**二、官方 TekgramUnlocks 是累计清单。**
Beta 包含 Gamma 全部内容，Alpha 包含 Beta 全部内容。抓取时部分新 BOSS 的 β / α 行只记了相对上一档新增的部分，且没写继承关系，读起来会像「α 解锁比 γ 还少」。
处理方式：`tools/sync_wiki.py` 的 `label_unlock_deltas()` 给缺继承说明的 β / α 行补上「包含简单解锁的所有内容↑，及：」/「包含中等解锁的所有内容↑，及：」，与 ASE 表既有写法一致。
不适用的情况：监察者、君王泰坦（写的是飞升植入体 / 战利品，不是泰克印痕）、芬里尔巨狼（单档独立内容）。

### 神器中文名对照（正式译名）
`tools/data.py` 末尾的 `_ART_NAME_FIX` 会在导入时对 `BOSSES` / `ASA_BOSSES` / `SPECIAL_BOSSES` 的 `artifacts`、`trophies`、`note`、`artifacts_by_diff` 统一替换，改译名只改这一处即可，不要逐条去改数据。

| 英文 | 正式中文 | 曾用（已全部替换） |
| --- | --- | --- |
| Skylord | 天主 | 天空之主 |
| Hunter | 猎手 | 猎人 |
| Massive | 稳重 | 庞然 |
| Clever | 智慧 | 机敏 |
| Devourer | 吞噬 | 吞噬者 |
| Immune | 免疫 | — |
| Brute | 残暴 | 野蛮 |
| Pack | 团结 | 群兽 |
| Cunning | 狡诈 | — |
| Destroyer | 灭世 | 毁灭者 |
| Crag | 岩壁 | 峭壁 |
| Gatekeeper | 卫士 | 守门者 |
| Strong | 强壮 | — |

另有 4 个不在上述 13 个正式名清单内、但数据里在用的神器，沿用通行译名，未作改动：

| 英文 | 中文 | 出现位置 |
| --- | --- | --- |
| Devious | 邪僻 | ASA 仙境·努纳塔克（主表）；ASA 仙境·幽灵恐熊与幽灵恐狼（特殊单位） |
| Depths | 深渊 | ASE 畸变、创世纪等地牢 BOSS |
| Shadows | 暗影 | 同上 |
| Chaos | 混沌 | ASE 创世纪 II |

**待确认**：ASE 表中原表沿用了带颜色后缀的写法 `狡诈(紫)`、`狡诈(绿)`、`狡诈(猾)`（仙境、瓦尔盖罗、维京、水晶岛等组合 BOSS 行）。这三者到底是同一神器的不同外观，还是三个不同神器，原表未说明，代码保持了原样未合并。若确认与 `狡诈` 为同一物，再在 `_ART_NAME_FIX` 里加三条去掉后缀即可。

---

## 六、校验清单（发布前逐项确认）

- [ ] 标题正确：方舟 BOSS 信息详情表
- [ ] 顶部有 **ASE / ASA 版本切换**，默认停在 ASE
- [ ] 切到 ASA 后，ASE 整块（标题、搜索框、难度筛选、地图标签、25 张卡片）全部消失；显示的是「BOSS 数据速查 · ASA 完整表」，含 10 张地图与 22 张 BOSS 卡片
- [ ] 元信息显示 ASE 12 图 / 25 BOSS / 63 行，ASA 10 图 / 22 BOSS / 60 行
- [ ] **ASE 表中没有任何省略提示**，组合 BOSS 的血量与解锁项目都已写成实际内容
- [ ] **神器贡品、战利品贡品是表格里的常驻列**，每个难度行都能直接看到，不需要点击展开
- [ ] ASA 表中 Nunatak、Grendel、Astraeos 系列、Lost King / Queen 都有实际血量与贡品，**全表没有「暂无数据」**
- [ ] ASA 同名 BOSS 的能量元素取的是 ASA 栏（育母蜘蛛 24/68/178、狮身蝎尾兽 68/244/514），不是 ASE 栏
- [ ] 每张表末尾都有「非竞技场战斗单位」分区：ASE 7 个、ASA 7 个，共 14 张卡片
- [ ] 表格是 **9 列**，最后一列是「掉落物」
- [ ] ASA 表不含水晶岛、失落岛、维京、创世纪 II
- [ ] 竞技场规则、贡品数量读法、「关于角色最高等级」的 ASE / ASA 切换、版本分区说明都在；等级说明写的是 ASE 205 / 220 级与 ASA 245 级，不是只有 ASE
- [ ] **贡品数量列没有任何笼统标注**，逐项数量以 `/` 分隔并按战利品贡品列顺序对应
- [ ] Astraeos 地图显示为「阿斯特赖俄斯/星曜/繁星」，没有被拆成三张地图
- [ ] 交互式版本：搜索框可用、地图标签可切换、γ/β/α 筛选生效（筛选后行数正确）
- [ ] 难度徽章配色 γ绿 / β蓝 / α红
- [ ] 页脚「数据来源与参考：Wikily ASA ｜ Wikily ASE ｜ ARK Official Community Wiki ｜ Teandy」四个链接都在，Teandy 排在最后
- [ ] 页脚下一行是「数据来源由曲終人散的智能体HLN-A生成 仅供参考」，网址没有单独占一行
- [ ] 顶部徽章与数据来源面板的「参考站点」行都带「听宇网」
- [ ] 「版本分区与数据来源」面板仍保留 3 个参考站点链接
- [ ] 全文没有署名、旧版本标记、版权与转载声明（页脚参考网址是明确要求保留的，不算旧署名）
- [ ] 手机端预览：难度行转为堆叠卡片，不出现横向滚动；窄桌面窗口（内容区 < 1180px）表格在卡片内可左右滑动，9 列齐全且不拆断数字
- [ ] 若站点过滤脚本，已改用 `post-static.html`，两张完整表仍并列完整
- [ ] 若用 WXR 导入，确认生成的是 draft 草稿，检查后再发布

---

## 七、数据质量与已知限制（务必如实告知）

1. **ASE 数值字段**：血量、准入等级、能量元素、贡品数量已核对，可信度较高。组合 BOSS 的空血量按组成 BOSS 标准血量展开，省略的解锁项目按同名 BOSS 展开，属于对已有数据的展开，不是新增推测值。
2. **长文本字段**：神器贡品、战利品贡品、泰克印痕列表为转录。原表存在跨行合并、按难度分行书写、单元格内逐项标数量等不规则排版；原表在贡品数量列未写出具体数量的 22 行（ASE）/ 10 行（ASA），现已依据同一条目贡品文本里的逐项数字展开为 `/` 分隔的实际数量串，**没有新增推测值**。若用于严肃攻略，建议对照 Wikily 或 ark.wiki.gg 复核。
3. **创世纪 II 罗克韦尔（终极）** 的 BOSS 血量在来源中即为空，保留 `-`，未编造。
4. **ASA 地图清单**来自公开资料，截至 2026-11-14；游戏发布进度会变化，新地图上线后需更新 `ASA_MAPS`。社区 mod 地图与尚未发布的官方地图（如 Dragontopia）未列入。
5. **ASA 数值**：官方 Wiki 的 Drops 表分 ascended / evolved 两栏，本表按栏取用。ASA 独占 9 个条目的血量、等级、贡品、元素、印痕均逐个取自 Wiki 专属页面（2026-11-14 抓取）。`Nunatak` 页面确实没有 Drops 段，其元素与掉落物如实写「Wiki 未列出」；Astraeos 的 Manticore 没有专属数值表，沿用焦土共用的一套，已在卡片备注注明。
6. **等级上限**：ASE 205 / 220 级、ASA 245 级均依据 `ark.wiki.gg/wiki/Leveling` 的 Max Levels 段（ASA 数据截至 2026-08-28），页面已按版本分列并可切换。两版不可互套。
7. **非竞技场单位已单列**：Astraeos 的世界 BOSS 塔纳托斯与 4 个小 BOSS、Lost Colony 的奴仆与巨链兽、仙境地下的 3 组、创世纪 II 的 4 个任务 BOSS，共 14 个，作为独立分区展示。其中创世纪 II 的 4 个任务 BOSS 官方 Wiki 未给血量与等级，如实写「Wiki 未列出」；幽灵恐熊与幽灵恐狼、安德洛克等同样有缺项，卡片内均注明。
8. **已清理的残留**：`MAPS` 里早期指向已删除图片切片的 `slice` / `y` 字段已移除；`ase_vernote` 的地图数与 BOSS 数改为按数据自动计算，不再硬编码。
9. **版本隔离**：ASE 数值不会被当作 ASA 数值使用；ASA 表也不引用 ASE 的地图数组或 BOSS 数组。两区在页面、Markdown、CSV、JSON 中完全分开。
10. **链接状态**：三个 Wiki 与 www.teandy.com 在生成时均可访问；Teandy 作为第四个来源名排在页脚第一行末尾，「参考站点」行另以「听宇网」列出同一站点。
11. 本包为结构化数据整理，转载时保留页脚四个来源链接与「数据来源由曲終人散的智能体HLN-A生成 仅供参考」这一行即可，不要额外添加版权或转载声明。

---

## 八、故障排查

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| 贴进去后只有说明文字、没有表格 | 编辑器过滤了 `<script>` **且** 用的是精简模板 | 用 `post-static.html`；`post.html` 的表格本身是静态 HTML，正常不会被过滤 |
| 版本切换按钮点了没反应 | `<script>` 被过滤 | `post.html` 自动降级为两区并列，数据不丢失；需要切换能力请用支持脚本的环境 |
| 「关于角色最高等级」的 ASE / ASA 按钮点了没反应 | `<script>` 被过滤 | 两套等级说明会并列显示，内容不丢失；两套等级上限不同，请勿合并 |
| 贡品数量显示一串用 `/` 分隔的数字 | 设计如此，原表笼统标注已补齐 | 按左侧「战利品贡品」列的项目顺序逐项对应，不要改回笼统标注 |
| 两张表同时出现 | 无脚本降级（预期行为） | 正常；需要切换能力请启用脚本或换用支持脚本的编辑器 |
| 表格样式丢失但内容还在 | `<style>` 被过滤 | 正常，原生 `<table>` 结构仍可读；或把 CSS 加进主题样式表 |
| 窄窗口只看到前几列、卡片下方有滚动条 | 表格是 9 列宽表，桌面最小宽度 1180px | 这是预期行为：在表格内左右滑动即可看到「能量元素」「解锁」「掉落物」等右侧列；内容区 ≥ 1180px 时不会出现滚动条。页面有滑动提示，请勿删掉列 |
| 表头文字挤在一起 / 数字被拆成两行 | CSS 被主题覆盖（如主题的 `table{white-space:nowrap}`） | 保持 `post.html` 内联 `<style>`，或把 `.abp-table th{white-space:normal}` 写进主题样式表 |
| WXR 导入报错 | 导入器不匹配 | 确认选择 WordPress 导入器；文件约 170 KB，无需分片 |
| 导入后是草稿找不到 | `wp:post_status` 为 `draft` | 后台「文章 → 草稿」 |
| 中文乱码 | 文件编码 | 全部 UTF-8；CSV 带 BOM；HTML 已声明 `<meta charset="utf-8">` |

---

## 九、重新生成

修改 `tools/data.py`（例如往 `ASA_MAPS` 或 `tools/wiki_data.py` 增加条目）后运行：

```
python tools/build.py
```

会重新生成 `boss-data.json`、`boss-table.csv`、`asa-boss-table.csv`、`asa-differences.csv`、`post.html`、`post-static.html`、`index.html`、`post.md`、`wordpress.xml`。`HANDOFF.md` 不受影响。
