# 2026-11-02 操作理由日志（盘前事前记录）

## 记录身份与边界

- 记录ID：OP-20261102-01。
- 对应市场交易日：2026-11-02，America/New_York。
- 编写时间：2026-11-02约21:31，Asia/Shanghai（纽约约08:31 EST）；尚未开市。
- 本篇为对本轮已给建议的归档及纠错，不是一次新的即时行情研究，也不是日终复盘。
- 研究证据截止沿用[当日盘前复核](../reviews/2026-11-02_PREOPEN_FIXED_STANDARD_REVIEW.md)的北京时间约21:12。后续公告、行情、收盘结果及执行状态尚未写入。
- 标准采用[现行流水线](../STOCK_SELECTION_PIPELINE.md)2026-11-02版本（规则提交 `3f445afe3ca971d5b57bf38717a039f3499b2567`），依[投资日志模板](../INVESTMENT_JOURNAL_TEMPLATE.md)记录。
- 公开版只记脱敏研究建议与依据；不披露个人持有标识、账户、数量、成本、余额、订单、实际成交或个人收益。

## 当时的唯一操作结论

**本轮不提出新增换股或加仓限价单；暂停原HII→AMP、DOX→ADBE配对的执行资格。**

这是对已完成研究范围的执行约束，不是证明全部现股最佳、安全，或已经完成全100只的比较。其他股票的独立现金归一化及替代估值缺项保留为待复核，不能自动改称正式持有结论。

| 研究方案 | 旧研究条件（USD，非实际订单） | 本轮状态与理由 | 最强反方／缺项 | 重算条件 |
| --- | --- | --- | --- | --- |
| HII→AMP | 325／480 | 暂停；AMP有盈利与资本支持，但独立上游资本资料尚不足验证旧可分配现金假设；新旧估值尺度不够一致 | AMP可能仍有配置价值；HII的EAC、养老金、季节性与现金转换也需公平处理，不能只严格审查候选 | 两端正常化及独立现金／资本桥完成，再按实际价格同额比较 |
| DOX→ADBE | 65／250 | 暂停；旧方案的较大空间依赖估值重估或净股数下降假设；无倍数扩张检验未支持原来的肯定语气 | DOX持续重组及业务出售净影响未知，不能将有利分支当事实；ADBE实际现金仍是正面证据 | 新年度指引、持续费用与处置影响明朗，两端现金及估值重新核对 |
| HUBB、ROP、ORLY | 详见盘前复核 | 观察暂不买入；未形成已验证的明确替换优势 | 部分现金预测、收购债务及价格余量仍需验证 | 现金证据或价格实质改变后重算；原研究区间不是自动买点 |

不默认预扣固定2.5%磨损。已确认费用与未知税务分别处理；本轮暂停不以重新引入固定成本为理由。限价只能约束价格，不保证两端成交。

## 相对本轮早先建议，为什么改变

本轮主要属于**模型与研究流程纠错**，不能包装成企业前景一晚突变。不是因后来股价涨跌而改写原理由。

| 分类 | 本轮核对结果 |
| --- | --- |
| 新事实 | 补读原始现金与资本资料；资料是本轮新核对，不代表全是当日新发布。具体原始来源与日期见盘前复核 |
| 价格变化 | 本次撤回不单由价格变化触发；没有增加新的即时可执行报价 |
| 模型纠错 | 候选与旧股采用不够对称的盈利／倍数假设；EPS乘现金转换率被赋予过高的独立验证作用 |
| 研究完成度纠错 | 在关键比较完成前给出了可执行限价，语气超出了证据支持程度；应先列待复核 |
| 用户约束 | 不新增交易授权；不以用户能承受亏损推定其接受研究遗漏 |

长期研究方向仍是实际业务、可持续盈利、普通股现金、合理价格及分散。合理预测可以使用，但要标为假设并检查敏感性；不要求所有不确定性消失才投资。无倍数扩张检验用于检查回报来源，可能的重估应单列，不当作确定回报。

## 来源、执行与结果

- 决策依据：[2026-11-02盘前复核](../reviews/2026-11-02_PREOPEN_FIXED_STANDARD_REVIEW.md)，归档提交 `740bff950fcc6f40cf243cef4e6a88ddaa8b102b`。其内附公司公告、SEC财报、现金口径、事件日期与报价限制。
- 过程复盘：[早期经验与后期标准漂移](2026-11-02_EARLY_SELECTION_LESSONS.md)。
- 本篇不声称取消、提交或成交任何订单。执行确认属于私人记录，建议与执行不相互替代。
- 当日尚未收盘；收益、相对基准、回撤、成交及日终结果：尚未记录，不填零。
- 本篇没有识别因果效应；尚未用未来涨跌证明今日决定正确或错误。
- 过程评价：先给限价后补齐比较是研究流程问题，予以保留；暂停原建议是纠错，不证明原持仓最优。

## 后续追加方法

按对应美国交易日维护 `docs/journal/YYYY-MM-DD_OPERATION_REASON_LOG.md`。后续补充须标时间和新增证据，保留以上事前结论；不要用收盘后的解释覆盖原文。休市日按美国当地日期简记休市及是否出现需处理事件，不制造交易理由。没有改变就记录没有改变；连接或数据缺失要写明，不编造已经核查。

后续结论变更必须分别写明：新事实、价格变化、模型纠错或用户约束；列旧结论、新结论、来源、影响和重算条件。每日记录本身不授权自动交易。

## 盘中追加复核 OP-20261102-02（北京23:17）

本段实际编写于北京2026-11-02 23:17（美国10:17 EST），不回填成晨报当时已知。与21:31事前记录及[晨报回溯补录](2026-11-02_MORNING_RESEARCH_BACKFILL.md)分开。私人账户与可见成交另核，公开版不含持有标识、账户、数量、成本、余额或执行记录。

**当前研究执行约束不变：不提出新的换股或加仓限价方案；HII→AMP、DOX→ADBE继续暂停。** 本轮为开市后的增量事件和价格核查，不是新完成100只或全部现股的独立估值；待复核事项不能写成全部已通过持有标准。

### 新增检查结果与正面依据

| 研究对象 | 当前证据与新增资金判断 | 需要重算的条件 |
| --- | --- | --- |
| BRK.B | 已公布Q2经营利润提供真实经营基础；现金须扣保险及营运需要，未完成最新安全边际模型，暂不新增。Q3日期未取得公司正式确认，不采用第三方日期当事实。 | 承保、正常化经营利润、资本配置或估值出现实质变化 |
| AMZN | Q3营业利润28.1bn、AWS收入增长39.3%支持继续研究；同季度CFO42.422bn减净现金capex75.878bn约负33.456bn，TTM公司FCF负42.357bn。资本投入回报是重点，暂不新增；不能仅凭负FCF机械推出出售。 | AWS增长/利润减速而投入继续扩大，现金改善路径变差或融资风险实质上升 |
| MSFT | FY27Q1营业利润增长21%、Azure增长48%；同季度CFO58bn减现金capex39.367bn仍正18.633bn，不能混写为负。还需扣SBC及融资租赁本金；10/29已公告25bn债券、预计11/4交割，暂不新增。 | 云增长、资本开支/租赁义务和普通股现金的关系恶化 |
| CVS | Q2有实际经营修复；原全年调整EPS7.90–8.10仅作估值参考，须保留准备金、SBC及现金质量核查。11/4 08:00 EST（北京21:00）电话会，财报前不新增。 | 医疗成本、会员定价、准备金质量、现金或新指引恶化 |

BRK.B与MSFT有经营盈利支持；AMZN需要优先完成现金投入回报复核，CVS需取得新业绩验证。上述判断不等于授予在任何价格新增资金的资格。

### 其他事件与候选的增量检查

- 本轮针对REGN、INTU、SCHW、HII、BKNG、G、STRL、DOX、AXS、PRDO的快速检查未核到11/2新增、要求立即退出的公司级重大公告；这不是穷尽性无风险证明。STRL/JV及NCI、HII回款、G回收、AXS底层承保质量仍有独立待核项，不能靠股价上涨解除。
- DOV完成原计划8亿欧元债券发行；MRK新增HIV研发/申请进展；ROP子公司发布产品回顾。尚未量化出足以改变换股判断的新增普通股盈利或现金。
- HUBB、ROP、DOV、MRK、ORLY及AMP、ADBE的可得盘中快照多为纽约09:57–09:58，比本段时间滞后约19分钟；原价格条件未被证明提供更稳健升级。不据延迟行情发布精准成交指令。
- 下一已核重要事件继续为：DOX/BKNG 11/3美国盘后，CVS 11/4早间电话会，G/PRDO 11/5盘后。事件日并不自动触发买卖，需按实际新资料重算。

### 与早先结论的变化及来源

本轮没有新增换股结论。价格上涨/下跌及新增产品或融资消息没有代替现金、估值及同额比较。没有重新引入固定2.5%磨损，也没有为了维持不交易而认定所有现股最优。

- [AMZN Q3官方SEC业绩](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm)
- [MSFT FY27Q1官方业绩](https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast)、[10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm)、[10/29债券公告](https://news.microsoft.com/source/2026/10/29/microsoft-announces-debt-offerings-7)
- [BRK官方Q2](https://www.berkshirehathaway.com/news/aug0826.pdf)、[官方新闻目录](https://berkshirehathaway.com/news/2026news.html)
- [CVS Q2官方业绩](https://investors.cvshealth.com/news/news-details/2026/CVS-HEALTH-CORPORATION-REPORTS-STRONG-SECOND-QUARTER-2026-RESULTS-AND-RAISES-FULL-YEAR-2026-GUIDANCE/)、[11/4官方电话会日程](https://www.cvshealth.com/news/company-news/cvs-health-to-hold-third-quarter-2026-earnings-conference-call.html)
- [DOV 11/2 8-K](https://www.sec.gov/Archives/edgar/data/29905/000119312526442782/d253912d8k.htm)、[MRK公司HIV会议通讯转载](https://finviz.com/news/412985/merck-to-present-new-data-from-its-broad-oral-hiv-portfolio-and-pipeline-at-hiv-glasgow-2026)、[ROP子公司发布稿](https://rss.globenewswire.com/news-release/2026/11/02/3393061/0/en/ai-innovation-takes-center-stage-at-powerplan-elevate-2026.html)

本段没有提交、取消或修改任何订单；未声称掌握所有实时挂单或可支配资金。

## 基金研究追加 OP-20261102-03（2026-11-02盘中）

本段补充VITAX的基金层研究，不披露任何个人持有、账户、数量、余额或收益。研究基金不能只套用个股候选排名，应核成分、行业与全账户共同因子、估值时点和可执行产品范围。

- 官方截至2026-09-30事实页显示，前十大持仓占63.7%；半导体38.1%加半导体设备5.5%，合计43.6%。这说明持有很多公司仍可能集中在同一行业及资本开支周期，不代表基金在11/2的实时权重完全相同。
- 基金跟踪信息科技行业指数；费率0.09%，没有把基金本身视为新增流动性或运营危机。科技公司的实际盈利亦有支持，但不能由少数强公司推出整只行业基金在任何价格都适合作唯一配置。
- 本轮不新增VITAX、不发布临时全额清仓或具体转换指令。中线配置方向为减少单一科技行业集中，以计划内可用的分散化基金承担核心配置；不是单因一天跌幅进行轮换。
- 尚未取得雇主401(k)可选投资清单、适用份额、费用及计划层交易规则，故不假定VFIAX、VTSAX或VTIAX均可买，也不编造转换比例/份数。本轮未完成可执行替代基金比较。
- VITAX为共同基金，不是ETF；按下一适用交易日收盘NAV成交，不能像股票下盘中限价单。Vanguard一般收盘截止规则不能代替具体雇主计划更早的截止或频繁交易限制；摘要招募书无基金赎回费不代表没有任何计划限制。
- 来源：[Vanguard 2026-09-30事实页](https://workplace.vanguard.com/iippdf/pdfs/FS5487.pdf)、[基金摘要招募书](https://www.sec.gov/Archives/edgar/data/52848/000119312525325211/f43604d1.htm)、[Vanguard共同基金定价说明](https://investor.vanguard.com/investor-resources-education/online-trading/buying-selling-mutual-funds)。

当次完整私人摘要须分别覆盖普通投资账户、Roth IRA及雇主401(k)；基金数据与账户余额日期不同、产品菜单未知时要单列，不能因已回答个股就漏掉基金执行结论。


## 收盘后补做复盘 OP-20261102-04

- 对应美国市场日：2026-11-02，常规16:00 EST收盘＝北京11月3日05:00。
- 实际补做与汇总：2026-11-03T09:17:29+08:00；新闻采用截止2026-11-02 20:00 EST／北京2026-11-03 09:00之前的已核资料。原始页面实际读取晚于截止，未独立验证历史页面版本；本篇不是06:00准时完成的报告。
- 沿用11/2现行标准；本轮不改变盈利、业务、现金、估值、分散和新旧同尺度要求。原事前/盘中三段原文保留。
- 股票及ETF取历史表Close，同一历史序列的拆股口径；不加入股息，非含息总回报。四基日为11/2、10/30、10/26、10/5；1/5/20日均由这些Close重新计算。盘后消息及报价不改写常规收盘。
- 私人账户与交易只在对话呈现；本公开段混合全部100只通用研究，不标识个人持有，也不包含账户收益、股数、成本、余额或实际成交。

### 当前动作及研究判定

本轮不提出新增买卖或加仓挂单。STRL的新增资金资格继续冻结于现金归属/项目执行复核，不能因为下跌或高目标价机械补仓；未取得足以直接认定流动性危机的新事实。BKNG监管事项与DOX剥离/持续费用分别评估，财报将近不自行证明应持有；本轮未形成基于新事实的临时卖出方案。

HII→AMP与DOX→ADBE继续暂停：各自仍缺影响决定的可比资本/现金及正常化利润桥，而非因为要求全100只完成估值才允许投资。旧价格条件已不适用。HII/AMP由研究325/480到收盘313.70/504.31，同额换入比约减少8.13%；DOX/ADBE由65/250到63.54/251.47，约减少2.82%。这只是价格事实，不替代未来价值比较，也不倒填为已发生交易。

暂不操作是本轮信息下的执行结论。部分现价持有资格及最强替代比较仍待复核，未完成的项目不自动升为正式持有或全市场最优。下一工作优先收敛于STRL现金归属、DOX新年度持续费用、BKNG监管/营销现金、G回款与AMZN资本投入回报，不把“待复核”永久化。

### 实际覆盖与缺项

| 项目 | 本轮完成 | 含义及未完成 |
|---|---:|---|
| 个股四日期价格及1/5/20日回报 | 100/100 | 400个价格基点、300个计算回报；非100只完整估值 |
| 定向新闻/持续事件基础筛查 | 100/100 | 非穷尽全部公告、法院案卷或媒体；GILD新公告只核官方索引摘要，正文未取得 |
| 公开评级材料 | 99/100 | 100只均尝试检索；PRDO没有取得可靠最新评级，未知不填Hold |
| 重点原始经营/现金核对 | 14/100 | IBKR、VRTX、REGN、DOV、ROP、HUBB、STRL、HII、AMZN、MSFT、DOX、G、ORLY、FANG；不等同完成14只全套现金估值 |
| 完整独立估值及指定同额换股比较 | 0/100 | 没有新增通过方案；不是认为全部公司不值得投资 |
| 基准/基金观察 | 10个工具 | 40个基点、30个回报；VITAX当前第三方NAV未获官方日NAV交叉确认 |

100股当日61涨、39跌；这只描述预先固定的本研究池，不能冒充全市场涨跌家数。全部110工具共440个基点、330个回报。

### 市场与基金对照

| 工具 | 11/2收盘或第三方NAV | 1日 | 5日 | 20日 |
|---|---:|---:|---:|---:|
| [SPY](https://stockanalysis.com/etf/spy/history/) | 752.10 | -0.48% | -1.73% | -2.93% |
| [QQQ](https://stockanalysis.com/etf/qqq/history/) | 681.09 | -1.36% | -4.37% | -9.93% |
| [RSP](https://stockanalysis.com/etf/rsp/history/) | 219.98 | +0.76% | +1.24% | +4.20% |
| [VITAX](https://stockanalysis.com/quote/mutf/VITAX/history/) | 466.13 | -2.70% | -5.90% | -11.90% |
| [XLK](https://stockanalysis.com/etf/xlk/history/) | 174.22 | -2.95% | -6.49% | -13.29% |
| [XLF](https://stockanalysis.com/etf/xlf/history/) | 57.56 | +1.86% | +2.75% | +6.83% |
| [XLV](https://stockanalysis.com/etf/xlv/history/) | 184.60 | -0.15% | +2.97% | +10.29% |
| [XLI](https://stockanalysis.com/etf/xli/history/) | 169.71 | +1.38% | +1.65% | -0.23% |
| [XLY](https://stockanalysis.com/etf/xly/history/) | 118.16 | +2.41% | +3.41% | +7.01% |
| [XLE](https://stockanalysis.com/etf/xle/history/) | 67.25 | -3.96% | -3.43% | +5.99% |

RSP领先SPY约1.24个百分点，科技/能源与金融/工业/消费表现分化。共同风险因子比“大市都涨/都跌”的概括更有解释力；没有因子模型及反事实，不宣称已识别价格因果。

VITAX官方9/30事实页的前十大63.7%、半导体及设备43.6%、费率0.09%未核到新版。当前466.13取第三方历史NAV，未独立取得可读官方日NAV复核。基金按适用收盘NAV交易，不能套股票盘中限价；具体计划产品菜单与截止/频繁交易规则未核实，不编造具体替代基金或转换数量。结构性科技集中仍需处理，不能因单日跌幅临时满仓切换或补仓。

### 重点证据与纠错

| 对象 | 已核变化与正面依据 | 反方及决策后果 |
|---|---|---|
| REGN | Q3业务及Sanofi分成有真实增长；10月十亿美元一次付款已收到、Q4确认收入 | 9M公司FCF29.043亿美元同比约−8.05%、应收增加；付款非经常收入，普通股现金仍须核SBC及回款 |
| STRL | Q3增长/已签积压支持业务，9/30循环贷款尚可用约14亿美元且守契约 | 一般可用现金与JV分开，NCI利润与现金分配不同；Cantor11/2目标742→565仍Overweight，容量/执行反方应保留，不自动买入或推定违约 |
| HII | 造船订单和盈利基础仍在 | EAC及现金季节性不能忽略，Q4兑现所需现金规模待核；11/2维持Hold340不是回款证据 |
| AXS | Wells Fargo112→122、Mizuho116→123，资本/投资收益有支持 | 底层承保比率变差未解除；Mizuho预计增长更多来自投资收益与回购，不能把升目标解读为承保改善 |
| MSFT | CFO58−cash capex39.367−SBC3.134−融资租赁本金1＝正14.499bn | 指定扣项代理不是完整owner cash；Other investing流出12.949bn、未来租赁/供应商占款仍须复核，不能与AMZN都写成负现金 |
| AMZN | AWS业务增长有实际利润支持 | 本季扣SBC/融资租赁及融资义务本金后现金代理约负39.402bn；真实回报路径仍待核，不因股价反弹解除 |
| DOX | 9M扣必要扣项简化现金353.409m有实际基础 | 另有37.260m并购递延/或有支付是资本配置现金，不能自动当经常费用；剥离/重组及FY27指引等待新财报 |
| G | ATS增长有业务基础 | H1补扣融资租赁本金后经营现金代理−57.498m，处置款单列；需以11/5回款和持续业务验证，旧表新补核不伪装新利空 |
| VRTX | 11/2盘后新财报收入+12%，新产品开始贡献、全年收入小幅上修 | 调整净利基本持平、费用上修、并购借款45亿美元；收盘涨跌发生于财报前，不倒置归因 |
| FANG | 11/2盘后Q3已发布，产量指引上调 | CFO25.99亿−capex10.26亿＝15.73亿美元；公司21.48亿FCF剔营运资金，仍须核Viper非控股、SBC/并购，更新旧待财报资料 |
| ORLY | 同店+7.2%、专业业务增长，9M现金仍有基础 | Q3 CFO−capex同比降约17.7%；回购与新发债需并看，90.70对公司全年EPS约27.1–27.9倍，暂不足证明替换优势 |
| ORCL | 正式提交100亿美元普通股及100亿美元债券融资文件 | 尚非已到账；稀释及未来现金投入需重算，升级评级不消除现金风险 |

上述现金代理逐个期间标明，不能跨公司不加桥接地直接排名。MSFT旧“尚未扣融资租赁本金”已补齐；REGN一次付款和经常应收分别处理。SCHW分析师名字Rubin/Rossi、V/MA动作10/30或11/2、GOOGL同日修订次序及G评级日期等来源冲突保留，不擅自选有利版本。

### 候选研究优先序列

维持HUBB、ROP、DOV、MRK、ORLY五个研究方向。本轮排序为研究任务优先，尚未形成可执行买入排名；每天不必换Top5，也不由涨跌直接改变标准。

| 次序 | 代码 | 当前价格 | 经营支持 | 尚需解决的核心问题 |
|---|---|---:|---|---|
| 1 | HUBB | 433.74 | Q3有机增长11%，全年调整EPS20.40–20.60 | 收购债务、NCI及扣退款普通股现金；不是高收入增长直接当可分配现金 |
| 2 | ROP | 479.54 | 经常收入、有机增长7% | 调整利润+5%与每股+15%的区别、Indicor处置/回购归因和收购/SBC后现金 |
| 3 | DOV | 215.91 | 有机增长7%、订单及交付基础 | 新发债是融资，需核经常现金与积压交付；不能直接恢复旧价格条件 |
| 4 | MRK | 148.36 | 新品已有销售，11/2补研发会议进展 | 并购支付与调整EPS同尺度、Keytruda集中，目标价上调不是新盈利 |
| 5 | ORLY | 90.70 | 同店与售后需求 | 季度现金转换、退款和回购融资；当前收益率/倍数未证明更好替代 |

全池成员本轮保持100，不因单日强势买入BSX/XYL/SYK或因下跌抹去ORCL/FANG等。池外AAPL/PLTR的11/2盘后原始业绩已检查，须进一步正常化退款/现金和估值后才讨论替换成员；APH与留档PH继续跟踪。池外未完成全市场比较，不能称名册已最优。

### 下一重要节点（按公司确认，电话会和发布分开）

| 对象 | 美国时间 | 北京时间 | 验证内容 |
|---|---|---|---|
| BKNG | 11/3约16:00发布、16:30电话会 | 11/4约05:00／05:30 | 间夜、营销效率、监管及合规成本、指引 |
| DOX | 11/3盘后；17:00电话会 | 11/4早间；06:00电话会 | FY27剥离后收入、持续费用、GAAP及现金 |
| CVS | 11/4 08:00电话会，具体发布分钟未核 | 11/4 21:00电话会 | 医疗成本/准备金、2027定价及现金 |
| G／PRDO | 11/5盘后、17:00电话会 | 11/6早间、06:00电话会 | 回款/业务及学生融资/招生、并购付款 |

### 与前段判断的关系及验收

- 新事实：VRTX/FANG新季报，IBKR月报、融资/收购阶段、具名分析师动作。
- 价格变化：11/2真实收盘及同口径窗口已更新；未把盘中快照当收盘，也未把当前股数回溯当实际账户收益。
- 模型纠错：补MSFT融资租赁、G租赁、DOX并购现金分类；REGN已收一次付款与应收分开，SCHW/V/MA/GOOGL等冲突保留。
- 用户约束：不默认扣2.5%磨损；以实际限价和已知费用比较，未知税费不填零；本篇无新的买卖配对。
- 原文、旧条件及本段按时间追加；不以结果上涨证明流程无误，不因结果下跌机械否定业务。
- 本轮未核得立即退出的新增经营崩坏事实；事件检索范围有限，不能写成没有风险。普通股现金和当前估值的未完成项目明确列出。

### 100股逐项走势、事件及分析师

以下每股均为公开通用研究。走势表格只用11/2常规收盘；盘后新财报另标。原始日价及评级抓取行未整体发布，正文为研究摘要、计算回报和来源链接。

#### 金融（18股）

| 代码／历史来源 | 11/2 Close | 1日 | 5日 | 20日 |
|---|---:|---:|---:|---:|
| [JPM](https://stockanalysis.com/stocks/jpm/history/) | 340.58 | +1.05% | +1.96% | +2.47% |
| [BAC](https://stockanalysis.com/stocks/bac/history/) | 49.57 | -0.88% | -1.88% | -8.20% |
| [GS](https://stockanalysis.com/stocks/gs/history/) | 898.72 | +0.47% | +0.61% | +0.59% |
| [MS](https://stockanalysis.com/stocks/ms/history/) | 185.73 | +0.78% | +1.22% | -2.35% |
| [IBKR](https://stockanalysis.com/stocks/ibkr/history/) | 74.83 | -2.69% | -7.15% | -15.97% |
| [AMP](https://stockanalysis.com/stocks/amp/history/) | 504.31 | +2.75% | +2.17% | +1.89% |
| [BNY](https://stockanalysis.com/stocks/bny/history/) | 147.78 | +0.46% | +0.41% | +2.80% |
| [TROW](https://stockanalysis.com/stocks/trow/history/) | 105.85 | +1.88% | +2.28% | +1.85% |
| [CB](https://stockanalysis.com/stocks/cb/history/) | 368.98 | +1.33% | +3.43% | +11.65% |
| [CME](https://stockanalysis.com/stocks/cme/history/) | 306.24 | +1.02% | -0.59% | +13.41% |
| [ICE](https://stockanalysis.com/stocks/ice/history/) | 172.28 | +2.03% | +7.64% | +13.23% |
| [V](https://stockanalysis.com/stocks/v/history/) | 425.51 | +2.88% | +5.28% | +15.09% |
| [MA](https://stockanalysis.com/stocks/ma/history/) | 658.10 | +3.15% | +7.27% | +16.56% |
| [MCO](https://stockanalysis.com/stocks/mco/history/) | 506.02 | +2.45% | +4.45% | +12.91% |
| [DFIN](https://stockanalysis.com/stocks/dfin/history/) | 67.75 | +1.29% | +24.98% | +40.33% |
| [AXS](https://stockanalysis.com/stocks/axs/history/) | 106.60 | +1.65% | +4.04% | +11.48% |
| [SCHW](https://stockanalysis.com/stocks/schw/history/) | 88.71 | +0.75% | -1.14% | -9.44% |
| [BRK.B](https://stockanalysis.com/stocks/brk.b/history/) | 556.11 | +2.51% | +1.38% | +10.28% |

##### JPM｜JPMorgan Chase

- **事件核查**：11/2定向新闻检索未核到改变核心盈利指引的新公司公告；新增为券商目标价动作，不能把市场评论当公司盈利上修。
- **具名评级与缺项**：11/2 UBS Erika Najarian维持Buy，目标395→400；公开转述已交叉核，未取得完整原研报。
- **经营支持／持续风险**：Q3净利息收入同比增长13%，贷款、支付和资本市场业务可共同提供盈利来源；观察存款与信贷质量能否支持持续回报。 风险：信贷与资本市场周期；Q3报告EPS与剔除显著项目后EPS不同，不能把一次性项目正常化错配。
- **下一验证**：11/5行业会议及2027-01-14 Q4官方结果；核NII、费用、坏账、资本缓冲，按ROTCE/TBV同尺度估值。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://jpmorganchaseco.gcs-web.com/static-files/71d42762-a4d9-435b-9486-b7327e378dca) · [来源2](https://www.tipranks.com/stocks/jpm/forecast) · [来源3](https://stockanalysis.com/stocks/jpm/) · [来源4](https://stockanalysis.com/stocks/jpm/history/)

##### BAC｜Bank of America

- **事件核查**：11/2未核到监管整改完成或经营指引新上调；10/30员工仲裁诉讼仍为最近新增风险，不能和10/13反洗钱处罚混为同一事件。
- **具名评级与缺项**：11/2 UBS维持Buy，目标67→62，未核到该新条目具名分析师；10/30 JPMorgan Vivek Juneja目标62→59.50。原库和部分聚合表将59.50四舍五入为60。
- **经营支持／持续风险**：固定利率资产重定价与净利息收入恢复提供经营改善线索，但必须先评估新监管处罚和整改。 风险：10/13 FinCEN12亿美元处罚已抵扣OCC7.5亿，另OFAC1160万；2024停止令及回溯/独立审查仍在，持续整改成本和影响未量化。
- **下一验证**：11/5行业会议、2027-01-15 Q4；先核监管整改、持续开支与正常化可分配资本。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.bankofamerica.com/regulatory-and-other-filings/select-sec-filings/content/0000070858-26-000481/bac09302026ex991.htm) · [来源2](https://stockanalysis.com/stocks/bac/) · [来源3](https://www.investing.com/equities/bank-of-america) · [来源4](https://stockanalysis.com/stocks/bac/history/)

##### GS｜Goldman Sachs

- **事件核查**：11/2定向公司/评级检索未核到新的盈利指引或资本返还公告；强投行季度不能推出积压订单持续加速。
- **具名评级与缺项**：11/2 UBS Erika Najarian维持Neutral，目标1010→1000。
- **经营支持／持续风险**：Q3投行费用同比增长21%，并购与股权融资恢复可提供经营杠杆，资产管理提高经常性收入占比。 风险：投行与交易周期波动；公司Q3投行费用积压订单较Q2下降，盈利强不代表后续订单继续加速。
- **下一验证**：核投行积压订单和费用可持续性；2027-01-19官方Q4结果，避免年化高交易季度。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/886982/000088698226000529/a3q26gsearningsresults.htm) · [来源2](https://fr.benzinga.com/quote/GS/price-targets) · [来源3](https://stockanalysis.com/stocks/gs/history/)

##### MS｜Morgan Stanley

- **事件核查**：11/2新增可核为UBS评级条目；Morgan Stanley策略师对大盘的评论不属于MS本身新盈利指引。
- **具名评级与缺项**：11/2 UBS Erika Najarian维持Buy，目标236→240；Investing条目与Benzinga sentiment记录相符，部分评级页仍停在10/5旧目标236。
- **经营支持／持续风险**：Q3财富管理与机构业务共同带动收入增长，观察客户资产转为收费资产及持续利润率的能力。 风险：权益市场下跌会影响资产管理收费和交易活动；高股价不能仅靠单季ROTCE外推。
- **下一验证**：会议实录及2027-01-14官方Q4；核净新增资产、收费资产转化、财富利润率和资本回报。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/895421/000089542126000288/a3q26msearningsrelease.htm) · [来源2](https://www.investing.com/equities/morgan-stanley) · [来源3](https://fr.benzinga.com/quote/MS/sentiment) · [来源4](https://stockanalysis.com/stocks/ms/history/)

##### IBKR｜Interactive Brokers Group

- **事件核查**：11/2 12:01 ET公布10月月报：DARTs430.6万，同比−4%/环比+5%；客户账户567.8万，同比+34%；客户权益9286亿美元，同比+19%但环比−4%；保证金贷款1068亿美元，同比+31%。账户增长与交易活跃度出现分化，不把规模增长直接当利润增长。
- **具名评级与缺项**：定向检索未核到11/2具名新动作；最近可核10/20 UBS Michael Brown Hold，101→97。
- **经营支持／持续风险**：Q3客户账户同比增长35%、佣金收入增长12%，全球低成本平台的新增客户有待转为长期利润。 风险：利息收入占比高、保证金贷款增长快；交易量和监管费用转嫁影响收入质量，需检查系统与合规风险。
- **下一验证**：等下一份官方月度经纪数据，核账户/DARTs/保证金贷款及利息收入；Q4正式财报日未核到。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://ndcdyn.interactivebrokers.com/mkt/getFileNew.php?file=2026Q3_Earnings_Release.pdf) · [来源2](https://www.stockwatch.com/News/Item/U-b20261102149155-U%21IBKR-20261102/U/IBKR) · [来源3](https://stockanalysis.com/stocks/ibkr/forecast/) · [来源4](https://stockanalysis.com/stocks/ibkr/history/)

##### AMP｜Ameriprise Financial

- **事件核查**：定向检索及当前新闻页未核到11/2新的公司经营指引；承接10/29 Q3及顾问留存、财富管理有机流量问题。合并CFO或EPS转换率不能替代独立上游可分配资本。
- **具名评级与缺项**：未核到11/2新具名动作；10/29 Evercore ISI Thomas Gallagher维持In Line/Hold、632→568；10/19 BofA Craig Siegenthaler Buy→Underperform、570→445，理由包括有机增长与费用。
- **经营支持／持续风险**：Q3扣除unlocking后EPS12.07，利润同比+14%；财富流量剔除Comerica后净流入53亿美元。 风险：财富报告流出受Comerica影响；资产管理仍净流出93.17亿美元；9M净上游资本25亿美元，不可用EPS×90%替代独立可分配资本验证。
- **下一验证**：核迁移后财富净流量、资产管理留存、母公司资本桥及RBC压力；下一正式财报日未核到。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/820027/000082002726000054/amp-20260930.htm) · [来源2](https://stockanalysis.com/stocks/amp/forecast/) · [来源3](https://ca.investing.com/news/stock-market-news/bofa-downgrades-ameriprise-financial-stock-rating-on-growth-concerns-93CH-4887888) · [来源4](https://stockanalysis.com/stocks/amp/) · [来源5](https://stockanalysis.com/stocks/amp/history/)

##### BNY｜The Bank of New York Mellon

- **事件核查**：11/2检索及新闻页未核到新的核心经营公告；10/27宣布参加11/5 BMO Financials Conference仍为下一验证，不把旗下封闭式基金分红当上市母公司盈利上调。
- **具名评级与缺项**：未核到11/2新动作；10/30 JPMorgan Vivek Juneja维持Overweight，161→166.50（部分表四舍五入167）。
- **经营支持／持续风险**：Q3收费收入同比增长12%，托管规模与平台效率改善可支持经常性盈利增长。 风险：市场水平、利率和客户资产变动影响收费；Q3杠杆及CET1资本比率同比下降，需要检查资本缓冲。
- **下一验证**：核有机托管收费、NII、资本缓冲及新客户；未来正式财报日未核到。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.bny.com/content/dam/bnymellon/documents/pdf/investor-relations/earnings/earnings-press-release-3q-2026.pdf) · [来源2](https://stockanalysis.com/stocks/bny/) · [来源3](https://www.benzinga.com/quote/BNY/price-targets) · [来源4](https://stockanalysis.com/stocks/bny/history/)

##### TROW｜T. Rowe Price

- **事件核查**：11/2定向检索未核到新的公司经营指引；Q3资产管理规模增长和主动权益产品净流出并存，不能用资产价格上涨掩盖客户流失。
- **具名评级与缺项**：未核到11/2新具名动作；10/30 JPMorgan Kenneth Worthington Underweight、106→107；TD Cowen William Katz Hold、109→96；Evercore Glenn Schorr In Line/Hold109，反映持续净流出分歧。
- **经营支持／持续风险**：Q3调整EPS2.86、收入同比+5.9%；ETF/SMA/模型组合扩展有潜力，未见持续净流出拐点。 风险：Q3净流出283亿美元；调整费用同比+5.8%，不能把市场抬升AUM当作资金流入。
- **下一验证**：下一月AUM与净流量、目标日期基金/ETF及费用；下一正式季度日期未核到。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1113169/000111316926000003/earningsreleaseq32026.htm) · [来源2](https://stockanalysis.com/stocks/trow/) · [来源3](https://stockanalysis.com/stocks/trow/forecast/) · [来源4](https://stockanalysis.com/stocks/trow/history/)

##### CB｜Chubb

- **事件核查**：11/2 10:00 ET公司发布J.D. Power小商业保险客户满意度消息：整体第2、数字渠道第1。它支持渠道/服务质量描述，但不提供保费、承保利润或股东现金的量化上修。
- **具名评级与缺项**：未核到11/2新具名动作；10/28 TD Cowen Andrew Kligerman Hold、360→379；10/27 Morgan Stanley Bob Huang Equal Weight、350→360。
- **经营支持／持续风险**：承保纪律、投资收入及地域分散支持防守型中线观察，重点是有形账面价值长期复利。 风险：Q3承保利润下降、灾损增加；Q3起核心盈利定义排除部分购入无形资产摊销，前期已重述，不能错配同比。
- **下一验证**：看剔灾当年承保、准备金、费率和法定资本；下一正式财报日未核到。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://news.chubb.com/2026-10-20-Chubb-Reports-Third-Quarter-Per-Share-Net-Income-and-Record-Core-Operating-Income-of-7-30-and-7-66,-Respectively,-Up-4-4-and-0-8-Consolidated-Net-Premiums-Written-of-15-1-Billion,-Up-1-9-,-with-P-C-and-Life-Insurance-Up-1-9-and-1-4-P-C-Combined) · [来源2](https://www.prnewswire.com/news-releases/chubb-small-business-recognized-for-outstanding-customer-satisfaction-in-2026-jd-power-study-302926508.html) · [来源3](https://www.benzinga.com/quote/CB/price-targets) · [来源4](https://stockanalysis.com/stocks/cb/history/)

##### CME｜CME Group

- **事件核查**：11/2定向检索和新闻页未核到10月正式月度ADV报告；9月31.8m/三季度29.4m是10/2旧公告，不能改名为11月最新。10/27巴西雷亚尔合约成交纪录也是旧事件。
- **具名评级与缺项**：未核到11/2新动作；最近可核10/23 Goldman Sachs Alexander Blostein Sell、254→271；10/22 JPMorgan Ken Worthington Underweight→Overweight、目标367，与部分券商谨慎意见并存。
- **经营支持／持续风险**：利率、外汇、商品避险需求转为交易与清算收费，Q3收入与净利双位数增长。 风险：成交量可能由异常波动拉动而非永久增长；新永续合约竞争与诉讼边界未完整核清，CME是原告而非被调查方。
- **下一验证**：下一月ADV/RPC及数据收入；核永续合约竞争与法院新裁定，未来正式财报日未核到。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.cmegroup.com/media-room/press-releases/2026/10/21/cme_group_inc_reportshighestq3revenueonrecordforq32026.html) · [来源2](https://stockanalysis.com/stocks/cme/) · [来源3](https://www.tipranks.com/stocks/gb%3A0hr2/forecast) · [来源4](https://www.benzinga.com/quote/CME/sentiment) · [来源5](https://cmegroupinc.gcs-web.com/news-releases/news-release-details/cme-group-reports-record-average-daily-volume-september-and-q3) · [来源6](https://stockanalysis.com/stocks/cme/history/)

##### ICE｜Intercontinental Exchange

- **事件核查**：11/2定向检索未核到公司级新盈利指引或MarketAxess交易完成；继续按10/29 Q3及HSR等待期已提前终止、其他审批尚待核的阶段研究。
- **具名评级与缺项**：未核到11/2新动作；10/30 TD Cowen William Katz Hold、167→182；KBW Chris Allen Outperform、180→190；Barclays Overweight、189→194。
- **经营支持／持续风险**：Q3净收入同比+15%、调整EPS+18%；9M CFO45亿美元，交易与数据业务支持增长。 风险：HSR已于10/21提前终止，但其他审批仍需取得；9月底债务233亿美元，MarketAxess收购融资及协同需重算。
- **下一验证**：核其他审批、2027Q1交割及新增融资；统一调整FCF与股东现金口径。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Reports-Third-Quarter-2026/default.aspx) · [来源2](https://stockanalysis.com/stocks/ice/) · [来源3](https://stockanalysis.com/stocks/ice/history/)

##### V｜Visa

- **事件核查**：11/2行业展望/评级转载为主要新检索线索，未核到改变法律责任或公司指引的正式新公告；FY26法律计提与DOJ借记卡诉讼仍须单独审查。
- **具名评级与缺项**：Cantor Ramsey El-Assal维持Overweight，445→500；首次动作日期有冲突：Benzinga列10/30，TipRanks列11/2。列为新核到的资料线索，不能确定当日新催化。
- **经营支持／持续风险**：FYQ4净收入同比+13%、调整EPS+17%；支付量+9%、跨境剔除欧洲内+14%。 风险：FY26法律计提17亿美元；DOJ借记卡反垄断风险未核到解除，激励、费率和诉讼现金需继续审。
- **下一验证**：审FY26 10-K和法院进展，核客户激励现金、FY27增长及估值；下一正式财报日期未核到。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000126/q42026earningsrelease.htm) · [来源2](https://www.benzinga.com/quote/V/price-targets) · [来源3](https://www.tipranks.com/stocks/v/forecast) · [来源4](https://stockanalysis.com/stocks/v/history/)

##### MA｜Mastercard

- **事件核查**：11/2主要为Q3后分析师/行业评论，未核到新的公司财报或解除商户诉讼的正式公告；9M现金及激励预付款问题继续承接。
- **具名评级与缺项**：Cantor Ramsey El-Assal维持Overweight，695→765；日期冲突：TipRanks/StreetInsider列11/2，而Benzinga动作表列10/30，11/2 MarketBeat转载正文也说Friday，故不当作已确认11/2新动作。
- **经营支持／持续风险**：Q3收入同比+14%、调整EPS+21%，跨境量+11%；支付网络及服务增长持续。 风险：9M CFO118.59亿美元低于去年126.46亿，激励预付款与法律支付增加；商户诉讼及收购债务未清关。
- **下一验证**：审Q3法律附注、激励现金、BVNK/债务及SBC后现金；下一正式财报日未核到。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1141391/000114139126000122/ma09302026-exx991xearnings.htm) · [来源2](https://www.tipranks.com/stocks/ma/forecast) · [来源3](https://www.benzinga.com/quote/MA/price-targets) · [来源4](https://www.marketbeat.com/instant-alerts/analyst-mastercard-nyse-ma-price-target-raised-to-76500-2026-11-02/) · [来源5](https://stockanalysis.com/stocks/ma/history/)

##### MCO｜Moody's

- **事件核查**：11/2定向检索及新闻索引未核到新的经营指引；最近核心事件仍10/21 Q3，评级发行周期走弱与Analytics经常收入增长并存。
- **具名评级与缺项**：未核到11/2新动作；10/22 BMO Jeffrey Silber Market Perform、490→511；BofA Heather Balsky Buy、580→575；Stifel Shlomo Rosenbaum Buy、550→537。
- **经营支持／持续风险**：Q3 Analytics有机恒汇率收入增长8%、ARR增长8%，订阅分析业务可部分平滑债券评级周期。 风险：Q3总收入仅增1%、评级交易收入降5%，调整EPS增长仅6%；不能沿用Q2高增长叙事。
- **下一验证**：看Ratings发行与Analytics续约，核SBC后现金和回购融资；下一正式财报日未核到。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1059556/000162828026066594/a3q26earningsrelease.htm) · [来源2](https://stockanalysis.com/stocks/mco/) · [来源3](https://www.benzinga.com/quote/MCO) · [来源4](https://www.morningstar.com/stocks/xnys/mco/news) · [来源5](https://stockanalysis.com/stocks/mco/history/)

##### DFIN｜Donnelley Financial Solutions

- **事件核查**：11/2‘目标72/共识提高’等转载主要回顾10/29财报和10/30 Needham动作，不是11/2新财报。ActiveDisclosure高增长与整体软件仅约5%增长必须同时保留。
- **具名评级与缺项**：未核到可独立确认11/2首次发布的新具名动作；承接10/30 Needham Kyle Peterson Buy、60→72；11/2自动转载不重复计一次评级变化。
- **经营支持／持续风险**：Q3总收入同比+5.5%，软件+5%、占比51.5%，ActiveDisclosure约+24%；9M现金转换改善。 风险：交易收入仍依赖资本市场周期，整体软件增速仅5%；调整EPS排除SBC，需看扣SBC后现金；Q3印刷已转为同比+9.4%，勿延用Q2下降结论。
- **下一验证**：下一季软件续约、有机增长、交易收入与SBC后现金；下次正式财报日期未核到。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1669811/000119312526436951/dfin-ex99_1.htm) · [来源2](https://www.marketbeat.com/stocks/NYSE/DFIN/news/) · [来源3](https://www.benzinga.com/quote/DFIN/price-targets) · [来源4](https://stockanalysis.com/stocks/dfin/history/)

##### AXS｜AXIS Capital Holdings

- **事件核查**：11/2新增主要为Q3后券商评估。Q3经营净利同比−10%、剔灾/天气当年综合成本率90.3%对比87.7%的底层承保压力仍在；网上关于爱尔兰顾问Axis Capital考虑PTSB收购属于同名异实体，排除于NYSE:AXS事件。
- **具名评级与缺项**：11/2 Wells Fargo Elyse Greenspan Overweight、112→122；Mizuho Yaron Kinar Outperform、116→123。Mizuho公开转述预计2027/28盈利推动由承保转向投资收益与资本返还，并预计保险净保费增速由中双位数放缓至中单位数；2026/27/28 EPS预测12.40/13.80/15.15是券商预测，非公司指引。完整研报未取得，不因目标上调解除底层承保风险。
- **经营支持／持续风险**：Q3剔AOCI每股账面84.33、同比+14.4%，但不能据此忽略承保盈利下降。 风险：Q3经营净利同比−10%，综合成本率94%；剔灾/天气当年综合成本率90.3% vs87.7%，费率软化与竞争并非纯灾损一次性。
- **下一验证**：核承保基础、准备金三角、费率及法定可分配资本；下一正式财报日未核到。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.globenewswire.com/news-release/2026/10/28/3390766/0/en/axis-capital-reports-third-quarter-net-income-available-to-common-shareholders-of-202-million-or-2-75-per-diluted-common-share-and-operating-income-of-229-million-or-3-12-per-dilut.html) · [来源2](https://www.gurufocus.com/news/9162300/axs-maintains-overweight-rating-by-wells-fargo-price-target-raised-to-122) · [来源3](https://www.investing.com/news/analyst-ratings/mizuho-raises-axis-capital-stock-price-target-to-123-on-nii-growth-93CH-4991024) · [来源4](https://stockanalysis.com/stocks/axs/) · [来源5](https://stockanalysis.com/stocks/axs/history/)

##### SCHW｜The Charles Schwab Corporation

- **事件核查**：11/2定向新闻检索未核到新的公司盈利预警；较新的风险解释仍来自10/28券商对资金成本、可生息资产扩张及NIM的重新估计，不能把一切归因于大盘。Q3净流入等经营正面仍在。
- **具名评级与缺项**：未核到11/2新动作。10/28 Evercore In Line/Hold目标104→98；StreetInsider转述2027/28 EPS预测再下调3%/6%至7.75/8.95。分析师名字冲突：StockAnalysis/TipRanks为Benjamin Rubin，StreetInsider/Benzinga为Benjamin Rossi，未取得原研报，保留冲突而不擅定。
- **经营支持／持续风险**：客戶資產、淨流入及財富管理規模增長；Q3核心淨新增資產1904億美元，調整EPS1.69美元。 风险：利率、存款遷移、淨息差、融資與市場活躍度；好財報不自動代表現價比IBKR、AMP等更值得持有。
- **下一验证**：月度流量、存款/现金迁移、NIM与AI成本收益；下一正式季度财报日未核到。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Delivers-Record-Net-New-Assets--Earnings/default.aspx) · [来源2](https://www.streetinsider.com/Analyst%2BComments/Charles%2BSchwab%2BCorp.%2B%28SCHW%29%2BPT%2BLowered%2Bto%2B%2498%2Bat%2BEvercore%2BISI/27243555.html) · [来源3](https://stockanalysis.com/stocks/schw/ratings/) · [来源4](https://www.benzinga.com/quote/SCHW/price-targets) · [来源5](https://stockanalysis.com/stocks/schw/history/)

##### BRK.B｜Berkshire Hathaway Class B

- **事件核查**：11/2官方新闻目录未出现Q3正式发布时间；不能以第三方11/7或11/13当公司确认。另本轮补核10/29 Bending Spoons原始公告/SEC：新增3.3亿美元投资已交割，总持股4%，此前6亿美元IPO投资；这是10/14宣布事项的完成，不是11/2新投资。
- **具名评级与缺项**：定向检索未核到11/2新的具名评级；此前UBS Brian Meredith等旧记录不改写为当日新评级。Q3官方日程仍待确认。
- **经营支持／持续风险**：保險浮存金與多元經營現金流、資本配置；Q2營運收益129.83億美元，並回購約45億美元股票。 风险：Q2保險承保和投資收益同比下降；GEICO理賠頻率與嚴重程度上升。須分離未實現投資收益、匯率及其他項目，不能按表面EPS倍增推論核心盈利倍增。
- **下一验证**：等待官方Q3日程/公告；核正常化经营收益、GEICO、资本部署及回购。聚合日期冲突，不采用为确认日。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.berkshirehathaway.com/qtrly/2ndqtr26.pdf) · [来源2](https://www.berkshirehathaway.com/news/2026news.html) · [来源3](https://investors.bendingspoons.com/newsroom/berkshire-completes-bending-spoons-investment) · [来源4](https://www.sec.gov/Archives/edgar/data/2004711/000200471126000024/bsp_ex99-1.htm) · [来源5](https://stockanalysis.com/stocks/brk.b/history/)

#### 醫療（19股）

| 代码／历史来源 | 11/2 Close | 1日 | 5日 | 20日 |
|---|---:|---:|---:|---:|
| [JNJ](https://stockanalysis.com/stocks/jnj/history/) | 270.56 | -0.97% | +1.60% | +6.97% |
| [MRK](https://stockanalysis.com/stocks/mrk/history/) | 148.36 | -0.78% | +5.51% | +6.32% |
| [ABBV](https://stockanalysis.com/stocks/abbv/history/) | 288.84 | -2.05% | +0.73% | +8.68% |
| [GILD](https://stockanalysis.com/stocks/gild/history/) | 170.33 | -0.21% | +7.34% | +17.77% |
| [REGN](https://stockanalysis.com/stocks/regn/history/) | 961.26 | +3.60% | +19.02% | +32.32% |
| [VRTX](https://stockanalysis.com/stocks/vrtx/history/) | 553.15 | -1.03% | +6.89% | +9.86% |
| [LLY](https://stockanalysis.com/stocks/lly/history/) | 1410.99 | -0.46% | +10.31% | +23.43% |
| [NVO](https://stockanalysis.com/stocks/nvo/history/) | 40.45 | +1.13% | +3.37% | +7.75% |
| [MDT](https://stockanalysis.com/stocks/mdt/history/) | 99.29 | +2.85% | +4.75% | +12.87% |
| [SYK](https://stockanalysis.com/stocks/syk/history/) | 306.81 | +5.12% | +0.22% | +7.57% |
| [BSX](https://stockanalysis.com/stocks/bsx/history/) | 44.32 | +5.57% | -2.76% | +4.53% |
| [ISRG](https://stockanalysis.com/stocks/isrg/history/) | 436.87 | +1.12% | -3.27% | +7.48% |
| [DHR](https://stockanalysis.com/stocks/dhr/history/) | 227.97 | -1.83% | -2.15% | +3.06% |
| [TMO](https://stockanalysis.com/stocks/tmo/history/) | 682.65 | -2.06% | -0.33% | +0.87% |
| [ABT](https://stockanalysis.com/stocks/abt/history/) | 110.16 | +3.73% | +5.03% | +10.05% |
| [ZTS](https://stockanalysis.com/stocks/zts/history/) | 83.18 | +4.34% | +2.73% | +16.48% |
| [MEDP](https://stockanalysis.com/stocks/medp/history/) | 648.14 | -0.59% | -4.23% | +4.45% |
| [IQV](https://stockanalysis.com/stocks/iqv/history/) | 258.44 | -3.33% | -5.54% | -2.87% |
| [CVS](https://stockanalysis.com/stocks/cvs/history/) | 88.51 | -1.93% | -4.34% | +1.72% |

##### JNJ｜Johnson & Johnson

- **事件核查**：11/2定向检索未核到新的集团业绩修订；补核11/1 Shockwave Javelin冠脉IVL的30日研究结果。属美国研究性器械与单臂试验，不等于新增商业销售或利润。
- **具名评级与缺项**：本轮未核到11/2新动作；聚合页最新为10/28 RBC Trung Huynh维持Buy、目标280，Leerink David Risinger重申Buy、272。
- **经营支持／持续风险**：Tremfya等新药增长及骨科业务重组有望改善业务组合，适合观察新产品能否覆盖专利到期压力。 风险：10月13日Q3含滑石粉拟解决方案特别费用；拟和解未等于全部诉讼责任消失，海外MedTech增长偏弱。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：司法批准/参与条件及支付日程、MedTech地区增长和创新药替代；下一正式财报日未核到。 本轮下一验证：核器械批准与真实销售转化；滑石粉拟和解的法院程序仍须继续跟踪。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q3-2026-results-raises-2026-guidance/default.aspx) · [来源2](https://www.jnj.com/media-center/press-releases/johnson-johnsons-novel-shockwave-javelin-coronary-ivl-catheter-delivers-positive-results-in-pivotal-forward-cad-ide-study) · [来源3](https://stockanalysis.com/stocks/jnj/history/)

##### MRK｜Merck & Co.

- **事件核查**：11/2 06:45 EST公司公告将于11/8–11/11 HIV Glasgow发表口服HIV治疗/预防资料，包括ISL/LEN三期亚组及患者报告结果；这是研发推进，未量化为新收入。
- **具名评级与缺项**：11/2聚合页：Leerink Daina Graybosch维持Buy，161→162；Freedom Ilya Zubkov维持Hold，125→140；Cantor Carter Gould维持Hold，145→155。目标上调并非评级上调。
- **经营支持／持续风险**：Q3销售同比+5%；QLEX销售8.30亿美元、Winrevair6.94亿美元且同比+93%，新品采用获得实际收入支持。 风险：Keytruda专利集中度仍在；FY26调整EPS2.77–2.82含大额收购/许可一次费用，估值需统一剔除费用与收购现金/债务，不能只修EPS。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核QLEX/Winrevair现金、管线节点与收购现金/债务；未来正式财报日期未核到。 本轮下一验证：11/8–11/11会议资料及IDVYNSO补充申请2027/4/22目标日期；仍先核Keytruda集中度和并购后股东现金。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.merck.com/news/merck-co-inc-rahway-n-j-usa-announces-third-quarter-2026-financial-results-highlights-multiple-milestones-advancing-broad-diverse-pipeline/) · [来源2](https://www.merck.com/news/merck-to-present-new-data-from-its-broad-oral-hiv-portfolio-and-pipeline-at-hiv-glasgow-2026/) · [来源3](https://stockanalysis.com/stocks/mrk/history/)

##### ABBV｜AbbVie

- **事件核查**：11/2 09:00 EST Brise更新2024年已签的两项临床前偏头痛授权，潜在总额7.57亿美元加版税；不是11/2新增7.57亿美元收入。另11/2 16:05 SEC接收8-K：董事Jennifer L. Davis因任Align CEO离任，公司称无分歧。
- **具名评级与缺项**：11/2：Leerink David Risinger重申Buy、279→325；Cantor Carter Gould维持Buy、290→325；Citi Geoff Meacham维持Hold、260→295。
- **经营支持／持续风险**：Q3收入174.04亿美元+10.3%；Skyrizi+22.7%、Rinvoq+23.9%、神经科学+19.4%，真实商业收入继续接替Humira；全年调整EPS指引上调至13.95–13.99。 风险：Humira收入仍−31.2%；Apogee已完成并购，资金占用与临床兑现仍须核。GAAP EPS2.37与调整3.82差异大，IPR&D和或有对价不能一概抹去；税率比较也影响盈利增幅。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：重建并购后普通股现金、债务和持续EPS；下一财报日期尚未获公司确认，不填估计日期。 本轮下一验证：区分临床前里程碑支出与现有Skyrizi/Rinvoq现金，重建收购后的债务及可持续普通股现金。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm) · [来源2](https://www.stocktitan.net/news/ABBV/brise-pharmaceuticals-announces-global-license-agreement-with-abb-dqjtbgq5f8fy.html) · [来源3](https://www.stocktitan.net/sec-filings/ABBV/8-k-abb-vie-inc-reports-material-event-eba2814cf055.html) · [来源4](https://www.prnewswire.com/news-releases/brise-pharmaceuticals-announces-global-license-agreement-with-abbvie-to-advance-the-next-generation-of-migraine-therapies-302925660.html) · [来源5](https://stockanalysis.com/stocks/abbv/history/)

##### GILD｜Gilead Sciences

- **事件核查**：11/2官方索引确认HIV Glasgow数据展示公告，会议为11/8–11/11；未将新摘要当作已实现收入。官方页面正文打开失败，本轮仅核官方检索摘要及公司原稿转述线索。
- **具名评级与缺项**：11/2：Leerink Daina Graybosch维持Hold、129→145；BMO Evan Seigerman维持Buy、184。评级分歧仍明显，不能只引用多头。
- **经营支持／持续风险**：Q3产品销售83亿美元+13%，剔除Veklury+16%，HIV+18%；Q3经营现金50亿美元，已有业务仍有盈利和现金基础。 风险：细胞治疗销售−18%；HIV增长含净价和库存因素。全年GAAP及nonGAAP指引均为亏损，含并购IPR&D约每股9.88；不能直接使用单季2.55调整EPS年化。9个月收购现金113亿、现金证券降至64亿，须重建债务及股东现金。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核新增HIV预防产品真实收入/支付、并购回报及细胞治疗；下一季官方日期未确认。 本轮下一验证：11/8–11/11核新数据，继续核HIV净价/库存、Biktarvy医保定价与并购现金义务。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/882095/000088209526000037/exhibit991earningspressrel.htm) · [来源2](https://investors.gilead.com/news/news-details/2026/Gilead-to-Present-Late-Breaking-Clinical-Data-and-Real-World-Evidence-at-HIV-Glasgow/default.aspx) · [来源3](https://stockanalysis.com/stocks/gild/history/)

##### REGN｜Regeneron Pharmaceuticals

- **事件核查**：11/2未核到新一轮公司业绩修订；重读10/30原稿：Dupixent增长及开发余额还清支持利润分成提升。9M CFO36.753亿减capex7.710亿＝公司FCF29.043亿（同比约−8.05%，尚未扣SBC）；总应收75.786亿较年末57.411亿上升。10月Sanofi十亿美元upfront已收到，Q4确认收入，非经常。
- **具名评级与缺项**：11/2：BofA Tazeen Ahmad维持Buy、908→1030；Leerink David Risinger维持Hold、835→997；Bernstein William Pickering维持Hold、756→812。多家上调目标，仍有偏谨慎评级。
- **经营支持／持续风险**：Q3收入51.2亿美元+36%、nonGAAP EPS20.07+70%；Dupixent全球销售+35%、Libtayo+51%，偿还Sanofi开发余额后首个完整季度分成改善有真实经营依据。 风险：EYLEA与HD全球合计销售−11%（美国合计−1%，不能混口径）；Sanofi应收款回收和普通股现金需继续核。Q4十亿美元Sanofi upfront不属经常盈利；原审批/竞争事项未以一季增长自动解除。 本轮补核：9M公司FCF低于去年且应收增加，需核Sanofi应收的收款周期、SBC与持续研发开支；不能把October已收的一次upfront与应收回收混为一谈。
- **本轮现金核查**：cash_primary_refresh
- **下一验证**：核Sanofi应收款回款、EYLEA合计下滑及后续研发费用；下一季官方财报日未确认。 本轮下一验证：用最新估值与独立股东现金重算；EYLEA+HD全球合计−11%仍需跟踪，不将连续上涨作为加仓依据。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.regeneron.com/news-releases/news-release-details/regeneron-reports-third-quarter-2026-financial-and-operating) · [来源2](https://new.streetinsider.com/Analyst%2BComments/Regeneron%2BPharma%2B%28REGN%29%2BPT%2BRaised%2Bto%2B%241%2C030%2Bat%2BBofA%2BSecurities/27268380.html) · [来源3](https://stockanalysis.com/stocks/regn/history/)

##### VRTX｜Vertex Pharmaceuticals

- **事件核查**：11/2盘后Q3收入34.408亿美元、同比+12%；GAAP净利6.536亿（去年10.829亿），nonGAAP净利约12亿基本持平。全年收入指引升至131.5–132.5亿，同时nonGAAP综合费用升至约60亿（原56.5–57.5亿）；不能只称盈利增长。
- **具名评级与缺项**：截至本轮未核到对11/2盘后财报的新具名动作；聚合页最新10/28 Leerink David Risinger重申Buy、无新目标，10/27 Citi Geoff Meacham维持Buy、585。旧目标不能冒充财报后更新。
- **经营支持／持续风险**：Q3收入34.408亿美元+12%，新产品开始贡献；全年收入升至131.5–132.5亿美元。Crinetics已完成收购，PALSONIFY纳入报表；但nonGAAP净利约12亿美元基本持平，费用增长抵消收入改善。 风险：CF收入集中、新产品付费/渠道兑现和Crinetics约88亿美元扣现金后交易额需核；公司预计并购至2029才增厚nonGAAP经营利润，潜在峰值销售不是当前盈利。 本轮补核：Q3 GAAP净利下降，费用及并购资金占用上升；9/30现金证券98亿美元、公司新借款45亿美元。需读现金流全表、SBC/租赁/整合现金义务，未完成股东现金和现价估值。
- **本轮现金核查**：new_earnings_primary
- **下一验证**：11/2盘后核Q3非CF实际收入、Crinetics会计/现金支出、可持续利润；11/30 povetacicept审批节点仍需届时官方复核。 本轮下一验证：11/30 povetacicept FDA目标日期；核CF以外收入兑现与费用/债务，财报后评级待更新。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.vrtx.com/news-releases/news-release-details/vertex-announce-third-quarter-2026-financial-results-november) · [来源2](https://investors.vrtx.com/node/35101/pdf) · [来源3](https://stockanalysis.com/stocks/vrtx/history/)

##### LLY｜Eli Lilly

- **事件核查**：11/2定向检索未核到新一轮公司业绩修订，沿用10/29Q3及已记录的收入、IPR&D和费用口径；本轮新增为财报后的具名目标调整。
- **具名评级与缺项**：11/2：Leerink David Risinger维持Buy、1316→1508；Cantor Carter Gould维持Buy、1440→1600；BMO Evan Seigerman维持Buy、1400→1650。
- **经营支持／持续风险**：Q3收入243.97亿美元+39%，GAAP EPS7.22+16%、nonGAAP7.48+7%；全年收入指引850–870亿上调至910–920亿美元，已有销量支撑。 风险：销量扩张同时净价压力；Q3含每股4.57的并购IPR&D。全年nonGAAP EPS实际由35.50–36.50降至35–36，经营改善与并购费用须分开；资本开支、药价政策和估值不能忽略。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核销量、净价、产能投入后股东现金，以及并购后持续EPS；未来官方财报日期未确认。 本轮下一验证：维持销量、净价、产能投入及并购后股东现金复核，不能由目标价上调代替安全边际。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/59478/000005947826000104/q326lillysalesandearningsp.htm) · [来源2](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-third-quarter-2026-financial-results-raises-full) · [来源3](https://stockanalysis.com/stocks/lly/history/)

##### NVO｜Novo Nordisk

- **事件核查**：11/2定向检索未核到新的集团业绩修订；10/28、10/29会议数据预告及11/4业绩节点继续跟踪，不写成11/2已经公布Q3。
- **具名评级与缺项**：未核到11/2新动作；最新10/14 Berenberg Kerry Holford维持Hold、47；10/12 BMO Evan Seigerman维持Hold、47→40。
- **经营支持／持续风险**：10/23公司公告Awiqli获FDA批准用于10岁以上2型糖尿病儿童；11/4九个月业绩日期由公司确认，电话会07:00–08:00EST。 风险：新适应证批准不等于已兑现销售。原有肥胖药竞争、净价压力、340B基数及减值影响未解除；不能以新产品利好或低表面PE跳过利润修复。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：11/4核美国处方/净价、剔除340B与减值后的可比增长、指引与自由现金；批准适应证的商业贡献另跟踪。 本轮下一验证：11/4核九个月结果与指引，剔一次性340B/减值影响，检验美国处方、净价及现金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.novonordisk-us.com/media/press-releases/awiqli-fda-approval-pediatric-type-2-diabetes.html) · [来源2](https://www.novonordisk.com/news-and-media/news-and-ir-materials.html) · [来源3](https://stockanalysis.com/stocks/nvo/history/)

##### MDT｜Medtronic

- **事件核查**：11/2定向检索未核到新增集团盈利指引；产品/获奖及激励安排线索未获得足够时间与影响验证，不当作新盈利催化。MiniMed分拆后的持续业务口径仍待核。
- **具名评级与缺项**：未核到11/2新动作；10/30 BofA Travis Steed维持Buy、110；10/22 Piper Matthew O'Brien重申Hold、85。
- **经营支持／持续风险**：10/22公布Sphere-9与PulseSelect真实世界登记结果，支持心脏消融产品商业路径；10/15 MiniMed分拆完成是原台账遗漏的资本结构事项，需按新口径研究。 风险：登记研究不是新增订单/利润；Sphere-9的VT用途美国尚属研究用途。FY27Q1有额外一周，13.7%有机增长不能直接当等长季度增速；召回、机器人投入和分拆后现金责任仍待核。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：先核MiniMed分拆后持续业务盈利/债务和PFA收入利润；第三方给11/17 FY27Q2，但本轮未取得公司确认，日期列待核。 本轮下一验证：先核分拆后的债务、可比季度与股东现金；下次季度业绩日期仍待公司原文确认。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://news.medtronic.com/2026-10-22-Medtronic-announces-positive-results-from-real-world-registries-for-the-Sphere-9-TM-catheter-and-PulseSelect-TM-PFA-System-at-APHRS-2026) · [来源2](https://news.medtronic.com/press-releases) · [来源3](https://stockanalysis.com/stocks/mdt/history/)

##### SYK｜Stryker

- **事件核查**：11/2未核到新的公司盈利修订；10/29低于公司预期的新指引仍是经营基准，不能因单日反弹当作业绩修复。律师招揽不是监管认定。
- **具名评级与缺项**：11/2：Canaccord Caitlin Roberts降至Hold、385→300；UBS Patrick Wood维持Buy、382→364；Leerink Mike Kratky维持Buy、353→340。评级和目标价转弱未因当日上涨解除。
- **经营支持／持续风险**：Q3收入65亿美元+7.7%、有机+7.7%；调整EPS3.52+10.3%、调整经营利润率26.2%，但公司承认低于自身预期。全年有机增长新范围6.5–7%、调整EPS14.80–14.90。 风险：GAAP净利7.53亿美元−12.3%、EPS1.96−11.7%；收购整合、重组、召回/法律等调整仍须审。原3月网络事件仍在财报风险中，未见结案及全部成本证明。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核增长低于预期的产品/地区、网络恢复成本、GAAP到现金差异和回购资金；下一官方季度日期未核。 本轮下一验证：核产品/地区增长不足、网络事件恢复成本与现金，重算14.80–14.90全年调整EPS对应估值。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/310764/000031076426000059/sykex991earningsq32026.htm) · [来源2](https://www.globenewswire.com/news-release/2026/10/29/3391829/0/en/stryker-reports-third-quarter-2026-operating-results.html) · [来源3](https://stockanalysis.com/stocks/syk/history/)

##### BSX｜Boston Scientific

- **事件核查**：11/2未核到新的盈利指引；10/28网络事件、心脏器械需求与2027压力继续有效。新律所调查招揽不等于已经正式立案或认定违规。
- **具名评级与缺项**：11/2 Citi Joanne Wuensch维持Hold、48→44；10/30 TD Cowen Josh Jennings降至Hold、56→46。目标下调与价格反弹应分开。
- **经营支持／持续风险**：Q3销售51.38亿美元仅+1.5%，GAAP EPS0.40低于去年0.51，调整EPS0.73低于0.75；全年调整EPS新指引3.16–3.18，Q4销售预计−3%至−1%。 风险：8月网络事件造成运营压力；Watchman/电生理竞争、增长重置与调整项仍需核。不能以目标价高于股价或股价下跌恢复新增资金资格。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核网络恢复与实际损失、Watchman/FARAPULSE份额、2027收入/盈利低基数及并购资金；下一官方财报日未核。 本轮下一验证：核网络恢复、实际损失、2027增长及现金；11/11会议若有新增经营披露再评估。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://news.bostonscientific.com/2026-10-28-Boston-Scientific-announces-results-for-third-quarter-2026) · [来源2](https://stockanalysis.com/stocks/bsx/history/)

##### ISRG｜Intuitive Surgical

- **事件核查**：11/2定向检索未核到法院初步/最终批准的新证据。10/21 10-Q仍写反垄断拟和解需批准，4.5亿美元和禁令救济风险继续有效；不能写已结案。
- **具名评级与缺项**：未核到11/2新动作；10/21 BofA Travis Steed重申Buy、470，Leerink Mike Kratky重申Buy、473→503。
- **经营支持／持续风险**：沿用10/20 Q3原始业绩：手术机器人、耗材/服务业务增长；10/21 10Q再次明确4.5亿美元反垄断拟和解需法院初步及最终批准。 风险：4.5亿美元现金和禁令救济对售后经济性的影响未解除；原Q3还含关税退款，不把全部EPS当正常利润。未查到法院批准的新证据，不能宣称已结案。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核法院批准及禁令细则、手术量和装机/租赁现金回报；下次官方财报日期未确认。 本轮下一验证：法院批准/禁令细则，手术量及装机/租赁真实现金回报；未完成新估值不新增。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://isrg.intuitive.com/news-releases/news-release-details/intuitive-announces-third-quarter-earnings-6) · [来源2](https://www.sec.gov/Archives/edgar/data/1035267/000103526726000071/isrg-20260930.htm) · [来源3](https://stockanalysis.com/stocks/isrg/history/)

##### DHR｜Danaher

- **事件核查**：11/2定向检索未核到Abcam验证争议独立解除的新证据；检索到的持仓申报/旧业绩不当新经营催化。争议是公开指控，未当监管造假认定。
- **具名评级与缺项**：未核到11/2新动作；10/22 UBS Doug Schenkel重申Buy、260；TD Cowen Daniel Brennan重申Buy、255→270。
- **经营支持／持续风险**：10/21 Q3收入66亿美元+8.5%，剔除呼吸道核心增长5.5%、整体核心3%；公司FCF16亿美元。全年调整EPS指引8.57–8.62，业务恢复有经营依据。 风险：Abcam抗体验证图片仍有具体公开质疑，未取得独立核验/整改解除证明；这是指控及验证门槛，不等于监管已认定造假。Q4整体核心增长约3%，现金仍需扣正常SBC并核并购回报。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：先核Abcam原始验证资料、独立检查/客户损失，再验证非呼吸道需求和普通股现金；未来财报日期未官方确认。 本轮下一验证：先取得原始验证图及独立核验/客户影响；再审非呼吸道需求及SBC后现金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.danaher.com/2026-10-21-Danaher-Reports-Third-Quarter-2026-Results?asPDF=) · [来源2](https://investors.danaher.com/press-releases?l=100) · [来源3](https://stockanalysis.com/stocks/dhr/history/)

##### TMO｜Thermo Fisher Scientific

- **事件核查**：11/2定向检索未核到抗体图片争议独立解除的新证据；10/30 10-Q及高增长旧财报不能证明争议已解决。
- **具名评级与缺项**：11/2 Barclays Luke Sergott维持Buy、775；10/30 Argus David Toung重申Buy、560→780。评级偏多不能代替独立核验。
- **经营支持／持续风险**：10/21 Q3收入121.4亿美元+9%、有机+6%，GAAP EPS4.64+9%、调整6.68+15%。10/30提交8K说明10/27宣布EVP Michael Shafer于12/31退休，未见改变盈利指引。 风险：公司FAQ否认伪造并称正在审查/标注Western blot图片、可提供部分raw图；未取得足够可复核的独立验证解除。强业绩、评级及价格都不替代该门槛。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：先核原始图、独立审查/客户影响，再核股东现金；后续季度公司日期未确认。 本轮下一验证：核原始图、审查结论及客户影响，再统一股东现金与估值；事件观察不解除。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/97745/000009774526000173/q32026earnings8kex99_1.htm) · [来源2](https://www.thermofisher.com/us/en/home/life-science/antibodies/invitrogen-antibody-validation/image-transparency-frequently-asked-questions.html) · [来源3](https://stockanalysis.com/stocks/tmo/history/)

##### ABT｜Abbott Laboratories

- **事件核查**：11/2 09:00 EST公布Amulet 360 VERITAS一年结果，资料实际11/1 TCT展示；TEE评估完全闭合96.3%。美国仍为研究用途，CE已于8月取得；不可称新增FDA批准或直接当利润。
- **具名评级与缺项**：11/2 Piper Adam Maeder维持Buy、118；10/27 Argus David Toung降至Hold、无目标，作为反方保留。
- **经营支持／持续风险**：10/21 Q3报告销售+14.5%，含Exact Sciences并购后的可比销售+7%；全年可比销售增长约6%，调整EPS缩窄至5.50–5.55。营养业务拟分拆，尚非完成。 风险：营养诉讼责任、分拆债务及现金分配仍待核；GAAP EPS0.53与调整1.42差异明显。报告销售增长不可直接当有机增长；评级偏多也不解除分拆责任门槛。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核分拆法律责任/融资、器械需求和新指引后股东现金，再估值；未来官方财报日未确认。 本轮下一验证：核器械美国审批及商业化、营养分拆债务/诉讼与现金责任，不能以研究数据解除旧风险。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1800/000162828026066601/abt-2026q3xexhibitx991.htm) · [来源2](https://www.stocktitan.net/news/ABT/late-breaking-one-year-data-show-abbott-s-next-generation-amulet-lxo3kmedkk8n.html) · [来源3](https://abbott.mediaroom.com/2026-11-02-Late-breaking-one-year-data-show-Abbotts-next-generation-Amulet-360-TM-device-continues-to-demonstrate-high-rates-of-left-atrial-appendage-closure-and-low-incidence-of-stroke) · [来源4](https://stockanalysis.com/stocks/abt/history/)

##### ZTS｜Zoetis

- **事件核查**：11/2定向检索未核到Q3已发布或利润指引新修订；官方11/5电话会仍是下一验证点。单日反弹不等于美国宠物需求及Librela风险已修复。
- **具名评级与缺项**：未核到11/2新动作；10/29 Morgan Stanley Erin Wright维持Buy、85→82；10/20 Jefferies Keith Devas降至Hold、103→83。
- **经营支持／持续风险**：截至截止未公布Q3，沿用8/6下调后的经营基准；公司9/24公告确认11/5 08:30ET电话会。不能把临近财报预期当新盈利。 风险：美国宠物就诊/价格敏感、Librela需求与安全线索、全年收入及利润下修仍未解除；价格跌幅和历史毛利率不能证明修复。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：11/5核美国宠物收入、Librela、净价/销量、全年指引及现金；必要时跟FDA安全原文。 本轮下一验证：11/5 08:30 ET电话会：核美国宠物销量/价格、Librela、全年指引和现金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.zoetis.com/news/news-details/2026/Zoetis-Announces-Second-Quarter-2026-Results/default.aspx) · [来源2](https://investor.zoetis.com/news/) · [来源3](https://stockanalysis.com/stocks/zts/history/)

##### MEDP｜Medpace Holdings

- **事件核查**：11/2定向检索未核到新的公司业绩或已验证重提诉讼材料；沿用最新10-Q自愿without prejudice撤诉的事实，不倒退为已经确认仍在诉，也不升级为披露完全无误。
- **具名评级与缺项**：未核到11/2新动作；10/26 BMO Sean Dodge重申Hold、600→670；10/23 Truist Jailendra Singh维持Hold、609→633。
- **经营支持／持续风险**：Q3收入7.16亿美元+8.5%，净新增业务8.734亿+10.6%，backlog31.672亿+5.6%；GAAP EPS4.84、CFO2.166亿，实际订单和盈利仍增长。 风险：最新10Q明确Durbin证券案10/12、Bushansky与Mary派生案10/20均自愿without prejudice撤诉；可再提、不等于法院认定披露无误。原‘持续诉讼未核清’须修正；取消率、backlog转化及成长放缓仍需核。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核后续重提案卷、取消率和net book-to-bill（本季约1.22）口径、现金是否含预收；未来官方财报日期未核。 本轮下一验证：取消率、net book-to-bill、backlog转收入与预收款；继续核重提案卷，不靠现金单季强劲自动解冻。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1668397/000166839726000034/medp-20261021exx991.htm) · [来源2](https://investor.medpace.com/news-releases) · [来源3](https://stockanalysis.com/stocks/medp/history/)

##### IQV｜IQVIA Holdings

- **事件核查**：11/2定向检索未核到新的集团业绩修订或意大利数据整改获解除原文；近期回购/AI新闻线索不替代数据合法性与backlog验证。
- **具名评级与缺项**：未核到11/2新动作；10/29 TD Cowen Charles Rhyee维持Buy、288→307；Leerink目标310→320但聚合页未具名，不冒填姓名。
- **经营支持／持续风险**：Q3收入44.28亿美元+8%，净新订单32亿+15%、book-to-bill1.2；GAAP EPS2.10，公司FCF6.67亿，并上调全年收入/调整EPS指引。12/1 Investor Day已在官方业绩稿宣布。 风险：因复核不活跃试验，backlog核减约21亿美元，剩326亿；公司称不影响历史业绩、当年指引或未来12月转收入，仍须验证。意大利数据违法处理700万欧元罚款和120日整改未获解除；净债务138.18亿美元、3.45倍杠杆，FCF同比7.72亿降至6.67亿。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：核意大利数据合法化和客户影响、backlog减记/取消率、真实收入转化及债务/普通股现金；12/1 Investor Day。 本轮下一验证：意大利120日整改、backlog核减/取消与债务，12/1 Investor Day。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://ir.iqvia.com/press-releases/press-release-details/2026/IQVIA-Reports-Third-Quarter-2026-Results/default.aspx) · [来源2](https://ir.iqvia.com/press-releases/) · [来源3](https://stockanalysis.com/stocks/iqv/history/)

##### CVS｜CVS Health

- **事件核查**：11/2定向检索未核到Q3已经发布或原指引新修订；公司10/5原文确认11/4 08:00 ET电话会（北京11/4 21:00）。这是电话会时间，不能当精确财报发布时间。
- **具名评级与缺项**：未核到11/2新具名动作；聚合页最新10/13 BofA Allen Lutz维持Buy、110，10/12 Leerink Michael Cherny重申Buy、119→112。
- **经营支持／持续风险**：截至截止Q3尚未公布；公司确认11/4 08:00ET电话会。沿用Q2修复与10/8星级资料，2027四星以上计划会员比例逾69%仍需量化收益影响。 风险：医疗利用率、Medicare重定价、PBM盈利模式及未来星级奖金影响未解除；不能把预期EPS或分析师目标当已实现收益。
- **本轮现金核查**：event_and_analyst_screen_only
- **下一验证**：11/4核医疗福利比率、2027会员/定价、星级奖金净影响、经营现金及修复指引。 本轮下一验证：11/4核医疗福利比率、2027会员/定价、准备金及经营现金；财报前不因低估值预期新增。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.cvshealth.com/news/company-news/aetna-2027-star-ratings-reflect-strong-clinical-quality-and-member-experience.html) · [来源2](https://www.cvshealth.com/news/company-news/cvs-health-to-hold-third-quarter-2026-earnings-conference-call.html) · [来源3](https://stockanalysis.com/stocks/cvs/history/)

#### 工業與服務（20股）

| 代码／历史来源 | 11/2 Close | 1日 | 5日 | 20日 |
|---|---:|---:|---:|---:|
| [DOV](https://stockanalysis.com/stocks/dov/history/) | 215.91 | +3.93% | +6.62% | +12.86% |
| [ROP](https://stockanalysis.com/stocks/rop/history/) | 479.54 | +2.77% | +8.58% | +31.97% |
| [ITW](https://stockanalysis.com/stocks/itw/history/) | 290.05 | +4.13% | +5.01% | +9.79% |
| [EMR](https://stockanalysis.com/stocks/emr/history/) | 165.96 | +0.62% | +2.63% | +2.24% |
| [ETN](https://stockanalysis.com/stocks/etn/history/) | 366.07 | -1.05% | -1.57% | -15.38% |
| [HUBB](https://stockanalysis.com/stocks/hubb/history/) | 433.74 | +2.67% | -5.59% | -9.76% |
| [IR](https://stockanalysis.com/stocks/ir/history/) | 82.73 | +3.35% | +11.02% | +5.32% |
| [XYL](https://stockanalysis.com/stocks/xyl/history/) | 97.26 | +5.26% | -10.14% | -5.04% |
| [J](https://stockanalysis.com/stocks/j/history/) | 160.24 | +3.63% | +8.90% | +15.55% |
| [ACM](https://stockanalysis.com/stocks/acm/history/) | 65.68 | +3.69% | +8.17% | +9.91% |
| [PWR](https://stockanalysis.com/stocks/pwr/history/) | 621.18 | +0.07% | +10.15% | -9.11% |
| [STRL](https://stockanalysis.com/stocks/strl/history/) | 335.45 | -3.02% | -7.01% | -35.90% |
| [TT](https://stockanalysis.com/stocks/tt/history/) | 413.33 | +0.81% | -9.16% | -12.20% |
| [OTIS](https://stockanalysis.com/stocks/otis/history/) | 78.37 | +3.46% | +4.12% | +18.96% |
| [WM](https://stockanalysis.com/stocks/wm/history/) | 237.71 | +1.82% | -1.37% | +15.02% |
| [RSG](https://stockanalysis.com/stocks/rsg/history/) | 245.97 | +0.79% | +1.93% | +15.57% |
| [FAST](https://stockanalysis.com/stocks/fast/history/) | 52.55 | +1.23% | +0.15% | +3.67% |
| [R](https://stockanalysis.com/stocks/r/history/) | 285.58 | +1.07% | +1.23% | +21.04% |
| [OSIS](https://stockanalysis.com/stocks/osis/history/) | 198.90 | -0.27% | +0.41% | +0.52% |
| [HII](https://stockanalysis.com/stocks/hii/history/) | 313.70 | -1.00% | +11.62% | +17.72% |

##### DOV｜Dover

- **事件核查**：11/2公司8-K确认完成8亿欧元、票息4.350%、2030到期债券发行；这是融资进展，不是新增经营利润或现金转换改善。
- **具名评级与缺项**：本轮未核到11/2新动作。最近表列10/26 Goldman Sachs Joe Ritchie维持Buy，235→237；10/23 Baird Michael Halloran仍Buy但270→258，须保留分歧。
- **经营支持／持续风险**：Q3收入22.34亿美元+8%、有机+7%；持续经营GAAP EPS2.50+14%、调整2.88+10%。五部门订单均增且超过出货，公司FCF3.833亿，部分积压在2027交付。 风险：工业需求与客户capex周期仍在；全年GAAP EPS8.93–9.08与调整10.60–10.75不可混用，处置/收购/重组与普通SBC须逐项核。订单增长不是全部已到账现金。
- **本轮现金核查**：按公司FY26调整EPS10.60–10.75，215.91对应约20.08–20.37倍；此为价格/指引比，不是现金验证或公平价值。
- **下一验证**：跟踪债券所得、旧债回购与融资后利息；复核Q3后普通股现金、2027积压交付与估值。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.dovercorporation.com/news-releases/news-release-details/dover-reports-third-quarter-2026-results) · [来源2](https://stockanalysis.com/stocks/dov/history/) · [来源3](https://stockanalysis.com/stocks/dov/forecast/) · [来源4](https://dovercorporation.gcs-web.com/static-files/5998a64b-6fe7-4a9a-892a-95be94365f3e)

##### ROP｜Roper Technologies

- **事件核查**：11/2 07:55ET子公司PowerPlan发布ELEVATE会议及AI产品路线；尚未披露可量化新增集团收入、利润或现金。Q3有机收入+7%、调整净利+5%和调整每股+15%的区别继续保留。
- **具名评级与缺项**：未核到11/2新评级。公开表将JPMorgan Samik Chatterjee上调至Hold、目标490列10/30，新闻列表相对日期暗示10/26；动作日期有冲突，不能当11/2催化。
- **经营支持／持续风险**：Q3收入21.72亿美元+8%、有机+7%，调整净利润+5%、调整EPS+15%；全年调整EPS22.35–22.40上调。关键工作流与经常收入有当前经营依据。 风险：调整EPS+15%不可冒充总利润+15%；GAAP含Indicor投资影响，收到12亿美元处置相关款项非可重复经营现金；并购支出、回购及普通SBC需归因。AI替代风险仍需实际续约证据。
- **本轮现金核查**：479.54/FY26调整EPS22.35–22.40约21.41–21.46倍；20日价格涨约31.97%，较前期研究时安全边际已收窄，不能沿用旧区间直接买。
- **下一验证**：核经营现金、SBC、回购与并购现金的桥接及AI续约；不把已收12亿美元Indicor款重计成永续经营现金。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.ropertech.com/node/19501/html) · [来源2](https://stockanalysis.com/stocks/rop/history/) · [来源3](https://stockanalysis.com/stocks/rop/forecast/) · [来源4](https://rss.globenewswire.com/news-release/2026/11/02/3393061/0/en/ai-innovation-takes-center-stage-at-powerplan-elevate-2026.html)

##### ITW｜Illinois Tool Works

- **事件核查**：最新列表仍以10/30派息和10/27Q3为主，本轮未核到11/2新增重大经营公告；股价+4.13%不是盈利预测自动提高4.13%。
- **具名评级与缺项**：未核到11/2新动作；10/28 Truist Jamie Cook维持Hold、297→293，Citi Andrew Kaplowitz Hold、317→310；10/27 Goldman Joe Ritchie仍Sell、267→270。
- **经营支持／持续风险**：Q3收入42.4亿美元+4.4%、有机+3.8%，经营利润+5.9%、利润率27.8%，GAAP EPS3.00+6.8%；CFO9.53亿、公司FCF8.51亿。全年GAAP EPS指引11.45–11.55上调。 风险：部分capex业务强而汽车/建筑需求仍有分化；公司100%现金转换按CFO减capex定义，仍需扣普通SBC检验owner cash；保险补偿及回购对每股增长要拆分。原JPM降级日期10/12转述与新表10/9冲突，不能无据定日。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核等口径有机增长、分部门价格/成本及股东现金，比较盈利增长与估值；下一官方财报日未核。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.itw.com/news-and-events/news/news-details/2026/ITW-Reports-Third-Quarter-2026-Results/default.aspx) · [来源2](https://stockanalysis.com/stocks/itw/history/) · [来源3](https://stockanalysis.com/stocks/itw/forecast/)

##### EMR｜Emerson

- **事件核查**：11/4盘前FY26Q4/全年结果及08:30ET电话会由10/14公司公告确认，尚未公布新年度结果。
- **具名评级与缺项**：11/2 BofA Andrew Obin维持Buy，目标价未在可读表披露；不擅填目标。10/19 Morgan Stanley Christopher Snyder Sell、135→145是旧反方。
- **经营支持／持续风险**：官方確認FY26第四季及全年業績11/4盤前發布；公告目錄截至截止時仍以10/14財報安排為最新公司公告，未查得10/22以後新的盈利指引。Q3有機訂單增7%、有機銷售增6%仍是已公布經營基礎。 风险：前版風險（歷史底稿，保留追蹤）：大型收購後槓桿、軟件整合及工業項目延遲；中東風險不能忽略。 本輪更新：收購槓桿、軟件整合和工業項目延遲風險延續；即將發布的全年現金流及2027指引尚未核實，不能以舊Q3推定新年度表現。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：11/4盘前全年结果、08:30ET电话会（北京21:30）；核订单、FY27指引、现金与收购后杠杆。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.emerson.com/en/corporate/news/2026/q4-2026-webcast-advisory) · [来源2](https://stockanalysis.com/stocks/emr/history/) · [来源3](https://stockanalysis.com/stocks/emr/forecast/)

##### ETN｜Eaton

- **事件核查**：11/3盘前Q3、11:00ET电话会已读公司发稿确认。另补核9/24旧公告：拟以企业价值8.10亿欧元购COL Group，目标2027Q1交割、须审批；预测2027销售2.50亿欧元不是已实现利润。
- **具名评级与缺项**：11/2 Bernstein Chad Dillard维持Buy、目标534；并非上调。公开新闻一处把Citi旧目标485误写185，采用具日期评级表485→498，不采异常数字。
- **经营支持／持续风险**：官方確認11/3盤前發布Q3。10/27派息、10/28 A380燃油泵升級為最新官方新聞，並非盈利指引上調；Q2有機收入增14%和電力訂單底稿尚待Q3更新。 风险：前版風險（歷史底稿，保留追蹤）：AI與電網資本開支共同因子、擴產和交付壓力；Mobility分拆交易尚有執行風險。 本輪更新：AI/電網資本開支共同因子、交付擴產及Mobility分拆執行風險延續；11/3財報前不能把訂單直接視為普通股自由現金。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：11/3盘前Q3（北京当晚盘前），11:00ET电话会为北京11/4 00:00；核电力订单、现金、COL融资与Mobility分拆。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-to-announce-third-quarter-2026-earnings-on-november-3--202.html) · [来源2](https://stockanalysis.com/stocks/etn/history/) · [来源3](https://stockanalysis.com/stocks/etn/forecast/) · [来源4](https://www.businesswire.com/news/home/20261020762951/en/Eaton-to-announce-third-quarter-2026-earnings-on-November-3-2026) · [来源5](https://www.businesswire.com/news/home/20260924967260/en/Eaton-signs-agreement-to-acquire-COL-Group-expanding-manufacturing-capacity-and-capabilities-for-data-center-and-utility-markets-in-EMEA)

##### HUBB｜Hubbell

- **事件核查**：本轮未核到11/2新的公司盈利公告，原Q3有机增长11%、调整EPS5.91的经营基础仍有效。已重读9M现金与NSI融资原文。
- **具名评级与缺项**：11/2 Bernstein维持Buy、目标560，公开表未披露分析师姓名，不补猜；10/28 Evercore Alexander Virgo Buy但630→585为旧下修。
- **经营支持／持续风险**：10/27 Q3收入增25%（有機11%、收購13%），調整EPS5.91增14%；全年調整EPS20.40–20.60。Utility有機增5%，Electrical增22%；成長並非全由收購。 风险：前版風險（歷史底稿，保留追蹤）：調整營業利潤率同比下降50基點；收購、通脹和電力資本開支周期可能抵消高收入增長。 本輪更新：9M CFO659m，扣capex119.8m、SBC30m及31m一次性已收關稅退款後為478.2m，尚未扣少數股東現金權益；NSI收購後長債4.506bn，不能把調整EPS直接等同普通股現金。
- **本轮现金核查**：433.74/FY26调整EPS20.40–20.60约21.06–21.26倍；调整EPS不是owner cash。
- **下一验证**：核NSI整合与营运资金回收；659.0−119.8−30.0−31.0=478.2m为9M现金代理，仍需处理NCI、税务与全年季节性。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://hubbell.gcs-web.com/node/32291) · [来源2](https://stockanalysis.com/stocks/hubb/history/) · [来源3](https://stockanalysis.com/stocks/hubb/forecast/) · [来源4](https://www.sec.gov/Archives/edgar/data/48898/000162828026067729/hubb-20260930.htm)

##### IR｜Ingersoll Rand

- **事件核查**：11/2公司发稿确认收购IVEK，约新增4000万美元年收入，价格为协同前2025调整EBITDA低双位数倍数；不是新增已生效4000万美元客户订单，具体买价/股东现金回报尚未完整披露。
- **具名评级与缺项**：11/2 Stifel Nathan Jones Buy、93→95；Baird Michael Halloran Buy但109→107，观点分歧不能只挑上调。
- **经营支持／持续风险**：10/29 Q3有機訂單增18%、有機收入增4%；調整EPS1.07，剔除IEEPA退款為1.01、增17%。Q3 CFO648m、公司FCF623m；訂單轉強但含約195m大型長周期項目。 风险：前版風險（歷史底稿，保留追蹤）：主要工業板塊有機訂單約持平、調整利潤率下降180基點；總收入增長部分來自收購。 本輪更新：退款令調整利潤看起來更強；IT&S剔退款EBITDA利潤率27.8%、同比降120bp，短中期需求與單筆長單須分開。公司FCF尚非扣SBC、收購及少數權益後普通股現金。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核IVEK实际对价、资本占用和整合；原Q3退款、约1.95亿美元长周期大单及剔退款毛利压力继续带入。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1699150/000162828026068260/ir2026q3ex991.htm) · [来源2](https://stockanalysis.com/stocks/ir/history/) · [来源3](https://stockanalysis.com/stocks/ir/forecast/) · [来源4](https://www.businesswire.com/news/home/20261102029102/en/Ingersoll-Rand-Expands-Life-Sciences-Solutions-with-Acquisition-of-IVEK-Corporation)

##### XYL｜Xylem

- **事件核查**：11/1律师招揽调查消息仍在新闻列表，不能等同监管正式立案或法院认定。10/27全年指引下修、项目延迟及出售重组尚未核到解除；+5.26%反弹不恢复新增资格。
- **具名评级与缺项**：未核到11/2新动作；最近10/29 UBS Joshua Spector Hold、112→99；10/28 Barclays William Grippin降至Hold、139→104。
- **经营支持／持续风险**：10/27 Q3有機訂單增10%，但有機收入持平；調整EPS1.44增5%。全年有機收入指引2–3%下調至持平、調整EPS5.55–5.70降至5.40–5.45。擬出售Applied Water International/Specialty Flow Control，2027改三分部。 风险：前版風險（歷史底稿，保留追蹤）：Q2有機收入僅增1%，全年有機收入指引從2–4%縮至2–3%；不可只報訂單與盈利改善。 本輪更新：項目延遲和客戶審慎支出已傳導至全年收入/EPS下修；FCF margin指引由10.2–11.0%收窄至約10.2%。出售及重組仍是計劃，不應計入已完成收益；現金流表期間標題存在June30字樣，未據此自行標作9M owner cash。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核10-Q正確期間、訂單延遲向收入/回款轉化、出售條款與重組現金成本，再重建普通股現金及估值。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1524472/000152447226000146/xyl10272026ex991.htm) · [来源2](https://stockanalysis.com/stocks/xyl/history/) · [来源3](https://stockanalysis.com/stocks/xyl/forecast/)

##### J｜Jacobs Solutions

- **事件核查**：最新列表仍是10/29 AEP服务、10/28旧金山约10亿美元JV项目及10/26业绩安排，本轮未核到11/2新的集团盈利或现金指引。MMSD合同争议仍须承接。
- **具名评级与缺项**：未核到11/2新动作；10/27 Bernstein Chad Dillard Buy、163，10/26 Citi Andrew Kaplowitz Buy、181→188。
- **经营支持／持续风险**：10/26官方確認FY26Q4/全年11/23盤後。MMSD仍是獲選進入談判、待Veolia法律挑戰解決才簽約；10/22行業報道續述暫停定案，不能當作已簽收入。 风险：前版風險（歷史底稿，保留追蹤）：Milwaukee客戶明確等Veolia法律挑戰解決才簽約，預計2028年啟動；Qatar舊民事訴訟也需持續帶入，不能以獲選等同生效訂單。 本輪更新：Milwaukee合同未定案、Qatar舊訴訟和PA收購債務風險延續；本輪未取得案件完整最新卷宗，亦無新業績可證實現金改善。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：11/23盘后FY26Q4/全年、16:30ET电话会；另核MMSD正式签约和诉讼，PA收购后现金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.jacobs.com/newsroom/press-release/jacobs-hold-its-fiscal-fourth-quarter-and-full-year-2026-earnings-conference) · [来源2](https://stockanalysis.com/stocks/j/history/) · [来源3](https://stockanalysis.com/stocks/j/forecast/)

##### ACM｜AECOM

- **事件核查**：公司原文确认11/16盘后FY26Q4/全年、11/17 08:00ET电话会；本轮未核到11/2解除大项目费用/现金回收风险的新公告。
- **具名评级与缺项**：未核到11/2新动作；10/26 Citi Andrew Kaplowitz维持Buy、84→79，不能把降低后的目标仍高当作事件已解决。
- **经营支持／持续风险**：10/26官方確認FY26Q4/全年11/16盤後、11/17 08:00 ET電話會。截止時未有新季度業績推翻FYQ3項目費用337m、GAAP虧損及CFO下降的原風險。 风险：前版風險（歷史底稿，保留追蹤）：FYQ3確認3.37億美元項目費用、GAAP虧損，經營現金流下降66%；全年指引已更新反映損失和更低NSR增長。 本輪更新：Construction Management項目成本/追償和現金回收仍未解除；backlog增長不能直接抵銷大額費用與營運現金受壓，須承接原事件閘門。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：2026-11-16盤後財報、11/17電話會；先查項目費用是否擴大、可追償現金及全年CFO，再重建估值。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://aecom.gcs-web.com/news-releases/news-release-details/aecom-announces-planned-dates-fourth-quarter-and-full-year-0) · [来源2](https://stockanalysis.com/stocks/acm/history/) · [来源3](https://stockanalysis.com/stocks/acm/forecast/)

##### PWR｜Quanta Services

- **事件核查**：未核到11/2新的集团业绩，10/29Q3大额订单和业绩上修仍是旧依据；继续区分RPO、总积压和当期现金。
- **具名评级与缺项**：11/2 Bernstein Chad Dillard Buy、775→804，Oppenheimer Brent Thielman Buy但835→800，Guggenheim Joseph Osha Buy、800；同日非一面倒上修。
- **经营支持／持续风险**：10/29 Q3收入12.01bn、GAAP EPS4.55/調整6.06；CFO約1.5bn、公司FCF約1.2bn；RPO41.8bn、總backlog63.7bn，全年財務預期上調。 风险：前版風險（歷史底稿，保留追蹤）：大額積壓不等於當期利潤；收購整合、技工產能及數據中心資本開支共振增加風險。 本輪更新：收入增幅仍需拆有機/收購；總backlog不同於RPO或當期現金。人力、交付、收購整合及AI/電網capex共同因子延續；尚未完成扣SBC與少數權益的普通股現金橋。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核Q3有機/收購貢獻、RPO轉換、預收/營運資金及收購融資；下次財報日期未官方核實。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.quantaservices.com/_assets/_01c9c3f1ac58364ad0eaebaeeddaa06e/quantaservices/news/2026-10-29_QUANTA_SERVICES_REPORTS_THIRD_QUARTER_2026_407.pdf) · [来源2](https://stockanalysis.com/stocks/pwr/history/) · [来源3](https://stockanalysis.com/stocks/pwr/forecast/)

##### STRL｜Sterling Infrastructure

- **事件核查**：11/2新增的是Cantor目标下修而非新季度财报；Q3已于10/28公布。SEC再核generally available现金16.807m、JV现金200.130m，但循环贷款可用约1.4bn并守契约；不能由低母公司现金直接判定违约。
- **具名评级与缺项**：11/2 Cantor Manish Somaiya维持Overweight，目标742→565（约−23.9%）；公开转述理由为容量及执行限制比需求更重要。目标仍高不能绕过现金/JV审核，也不能证明当日跌幅由该动作单独造成。
- **经营支持／持续风险**：公司新季報頁面日期為10/28。Q3收入1.56bn增127%、GAAP EPS6.92、調整7.58；9M CFO427.1m。已簽backlog4.14bn、combined6.14bn內含未簽2bn；Q3已簽book-to-burn0.9。 风险：前版風險（歷史底稿，保留追蹤）：Q2收入增90%含2.508億美元收購貢獻；AI建設周期、項目集中和回款風險，需估值壓力測試。 本輪更新：9M CFO扣capex115.458m/SBC26.796m後284.841m仍未扣NCI現金；總現金216.937m中JV200.130m、generally available僅16.807m。營運資金耗用203.734m是9M而非Q3；必須核回款和JV現金可用性。 本轮平衡补核：9/30循环贷款尚可用约1.4bn且守契约，低generally available现金不等于违约；9M已付NCI分配0.980m、归NCI利润35.362m，不可只扣已付金额即称完成股东归属。
- **本轮现金核查**：335.45/FY26调整EPS21.70–21.96约15.28–15.46倍，仅为指引倍数；当前新增/加仓仍观察，不能只因跌幅与低倍数放行。
- **下一验证**：追踪应收、合同资产和JV归母现金转移；9M扣capex/SBC代理284.841m尚未完成NCI归属，实际NCI分配0.980m与归NCI利润35.362m不可混同。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.strlco.com/news/sterling-reports-record-third-quarter-results-and-raises-full-year-2026-guidance/) · [来源2](https://stockanalysis.com/stocks/strl/history/) · [来源3](https://stockanalysis.com/stocks/strl/forecast/) · [来源4](https://www.tipranks.com/news/the-fly/sterling-infrastructure-price-target-lowered-to-565-from-742-at-cantor-fitzgerald-thefly-news) · [来源5](https://www.sec.gov/Archives/edgar/data/874238/000087423826000125/strl-20260930.htm)

##### TT｜Trane Technologies

- **事件核查**：本轮未核到11/2新公司经营指引；10/29订单增长和分部利润率压力仍同时有效。
- **具名评级与缺项**：11/2 Bernstein Varun Govindaraj Buy、575→555；Citi Andrew Kaplowitz Buy、566→549；Baird Timothy Wojs Hold、528→498。反弹与目标下修并存。
- **经营支持／持续风险**：10/29 Q3有機訂單增20%、有機收入增16%，backlog12.5bn增73%；調整EPS4.86增25%。9M CFO3.060bn/FCF2.828bn，全年收入預期上調，調整EPS15.20–15.30維持。 风险：前版風險（歷史底稿，保留追蹤）：Q2調整營業利潤率下降60基點；產能、產品組合及數據中心需求預期可能壓縮安全邊際。 本輪更新：整體調整營業利潤率20.2%、同比降40bp；EMEA/APAC分部利潤率下降較大，供應鏈/通脹與數據中心冷卻共同因子延續。FCF尚需扣SBC後估普通股收益。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核各區利潤率、訂單交付和現金正常化，估值不依賴倍數擴張；下季財報日期未官方核實。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2026/Trane-Technologies-Reports-Strong-Third-Quarter-Results-Raises-Full-Year-Revenue-Guidance-Reaffirms-Full-Year-EPS-Guidance/default.aspx) · [来源2](https://stockanalysis.com/stocks/tt/history/) · [来源3](https://stockanalysis.com/stocks/tt/forecast/)

##### OTIS｜Otis Worldwide

- **事件核查**：最新列表仍是10/29派息和10/28Q3；本轮未核到11/2盈利修复新证据。新梯中国收入下滑、成本与现金压力不因+3.46%反弹消失。
- **具名评级与缺项**：未核到11/2新动作；10/29 Bernstein Varun Govindaraj Buy、90→94，与Wells Fargo Stephen Tusa Sell、77→75并存。
- **经营支持／持续风险**：10/28 Q3有機銷售增6%，服務增7%、現代化訂單增10%；調整EPS1.05持平。服務margin24.2%環比修復100bp，但同比降130bp；全年EPS4.01–4.05維持。 风险：前版風險（歷史底稿，保留追蹤）：全年調整EPS指引下調至4.01–4.05美元（此前4.20–4.24）；勞工成本、新梯尤其中國需求承壓。 本輪更新：新梯中國收入降逾20%、整體調整margin16.0%同比降110bp。Q3 CFO337m/調整FCF272m；全年調整FCF由1.50–1.55bn收窄至約1.5bn，成本和現金修復仍未完成。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核服務價格能否覆蓋工資、全年現金達標及中國新梯收縮；保留事件觀察，未確認下季日期。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://otisinvestors.com/news/news-details/2026/OTIS-REPORTS-THIRD-QUARTER-2026-RESULTS/default.aspx) · [来源2](https://stockanalysis.com/stocks/otis/history/) · [来源3](https://stockanalysis.com/stocks/otis/forecast/)

##### WM｜Waste Management

- **事件核查**：本轮未核到11/2新的重大公司经营公告。Q3现金、Healthcare修复及量能偏弱继续承接，公司FCF定义含资产出售，须独立归一化。
- **具名评级与缺项**：未核到11/2新动作；10/30 UBS Jon Windham Buy、270→280；10/29 Morgan Stanley Toni Kaplan Hold、220是应保留的反方。
- **经营支持／持续风险**：10/27 Q3收入6.846bn增6.3%、調整EPS2.15；Healthcare收入增3.7%、EBITDA增逾30%。9M CFO4.867bn增12%、公司FCF3.01bn增逾42%；全年FCF預計3.75–3.85bn高端。 风险：前版風險（歷史底稿，保留追蹤）：收集處置量下降1.8%；低毛利業務退出、燃料成本及醫療業務整合可能影響現金兑现。 本輪更新：Collection/Disposal量仍降0.4%（工作日調整降0.5%），回收商品/能源價格及Stericycle整合風險延續；公司FCF含資產出售收入，普通股現金估值須另核SBC及維持性capex。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：追蹤量能、價格成本差、Healthcare整合及公司FCF口徑；下季日期未官方核實。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://wastemanagement.gcs-web.com/news-releases/news-release-details/wm-announces-third-quarter-2026-earnings) · [来源2](https://stockanalysis.com/stocks/wm/history/) · [来源3](https://stockanalysis.com/stocks/wm/forecast/)

##### RSG｜Republic Services

- **事件核查**：本轮未核到11/2新公司业绩；10/29全年指引上修是11/2多家改价的旧经营背景，但没有识别其价格因果份额。
- **具名评级与缺项**：11/2 Citi Bryan Burgmeier Buy、259→281；Wells Fargo Jerry Revich Buy、234→270；Barclays William Grippin Hold、240→254；Bernstein Connor Cerniglia Hold、227→230，后者目标低于收盘。
- **经营支持／持续风险**：10/29 Q3收入增8.2%（回收/廢物有機4.8pp、環境解決方案2.1pp、收購1.3pp）；調整EPS1.94增2.1%。9M CFO3.52bn/調整FCF2.28bn，全年收入、EBITDA和調整FCF指引上調。 风险：前版風險（歷史底稿，保留追蹤）：總量拖累收入1.6%、環境解決方案收入下降；併購、環保責任與勞工成本仍需核查。 本輪更新：volume對收入影響仍−0.6%，調整EPS增長落後收入；再生商品價格、收購和環境解決方案風險延續。調整FCF須核剔除項和SBC後再估普通股現金。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核環境解決方案改善能否持續、量能恢復及全年調整FCF2.565–2.585bn；下季日期未官方核實。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.republicservices.com/news-releases/news-release-details/republic-services-inc-reports-third-quarter-2026-results) · [来源2](https://stockanalysis.com/stocks/rsg/history/) · [来源3](https://stockanalysis.com/stocks/rsg/forecast/)

##### FAST｜Fastenal

- **事件核查**：本轮未核到11/2新月销售或经营指引；10月销售尚待11/5，不能以股价或旧Q3提前填结果。
- **具名评级与缺项**：未核到11/2新动作；10/29 Morgan Stanley Christine Yao维持Hold、52；10/21 Argus Kristina Ruggeri Buy、55→59为旧消息。
- **经营支持／持续风险**：10/14已報Q3，銷售增15.5%、營業margin21.5%，Q3 CFO422m約為淨利105%；10/22以後本輪未核得新重大盈利公告。官方日曆10月銷售於11/5 06:00 CT發布，尚未公布。 风险：前版風險（歷史底稿，保留追蹤）：大客戶組合壓毛利，價格成本仍拖累；關稅退款與供應商返利含時點效應，高增長需要估值補償。 本輪更新：大客戶/產品組合壓低毛利率，需核價格成本、關稅退款/供應商返利及營運資金時點；原Q3現金不能代替尚未發布10月銷售趨勢。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：2026-11-05 06:00 CT月銷售；看日均銷售、有機需求/價格及客戶組合。下次季度日期未官方核實。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.fastenal.com/news/news-details/2026/Fastenal-Company-Reports-2026-Third-Quarter-Earnings/default.aspx) · [来源2](https://stockanalysis.com/stocks/fast/history/) · [来源3](https://stockanalysis.com/stocks/fast/forecast/) · [来源4](https://investor.fastenal.com/overview/default.aspx)

##### R｜Ryder System

- **事件核查**：11/2公开公司稿确认已于11/1完成Efficiency Enterprises收购，增加6处网点、约50名技师、约1200台设备，预计2027收入约5000万美元；财务条款未披露，不能据此算已实现股东利润。BusinessWire URL含20261103，但同稿带时间转载标11/2 12:30ET；保留此时间/URL差异。
- **具名评级与缺项**：未核到11/2新评级；10/27 Susquehanna Harrison Bauer Buy、280→318；旧评级不能作11/2新催化。
- **经营支持／持续风险**：10/22已發布Q3，GAAP EPS4.16/可比4.33增21%，營運收入增6%；全年可比EPS上調14.85–15.05。CFO2.6bn、公司FCF700–800m全年指引維持。 风险：前版風險（歷史底稿，保留追蹤）：貨運及二手車價格週期；Q2專用運輸營運收入降3%，供應鏈稅前利潤降7%；10月22日財報可能改變舊指引。 本輪更新：DTS營運收入仍降1%，二手車殘值/租賃周期、資本密集性延續；公司FCF包含售車收益，與輕資產股不能直接同口徑。Q4約4.30/share養老金結算是預計非現金費用，不應誤判為經營崩塌。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：核收购对价、营运资本与车队capex；原Q4养老金非现金结算、DTS及二手车风险继续带入。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://newsroom.ryder.com/news/news-details/2026/Ryder-Reports-Third-Quarter-2026-Results/default.aspx) · [来源2](https://stockanalysis.com/stocks/r/history/) · [来源3](https://stockanalysis.com/stocks/r/forecast/) · [来源4](https://www.businesswire.com/news/home/20261103373781/en/Ryder-Acquires-Efficiency-Enterprises-Expands-East-Coast-Fleet-Network) · [来源5](https://www.stockwatch.com/News/Item/U-b20261103373781-U%21R-20261102/U/R) · [来源6](https://finviz.com/news/413400/ryder-acquires-efficiency-enterprises-expands-east-coast-fleet-network)

##### OSIS｜OSI Systems

- **事件核查**：本轮未核到11/2新的经营公告；最新是10/29 FY27Q1及旧评级。政府验收、交付和回款依赖继续存在。
- **具名评级与缺项**：未核到11/2新动作；10/30 Roth MKM Jeff Martin Buy、274；10/8 Oppenheimer Christopher Glynn Buy、300→265是旧降目标。
- **经营支持／持续风险**：10/29 FY27Q1收入403.5m增5%、GAAP EPS1.51增28%、調整1.66增17%；book-to-bill1.4、backlog2.1bn；CFO37.088m、capex7.655m。全年收入1.875–1.930bn維持，調整EPS11.13–11.49提高至11.28–11.64。 风险：前版風險（歷史底稿，保留追蹤）：中東衝突已令交付延後，FY2026Q4收入降4%；政府採購、驗收及收款使季度收入和現金流波動。 本輪更新：Security收入組合壓margin、Healthcare偏弱，地緣/中東交付風險未消失；EPS改善須拆利息和回購，CFO-capex29.433m尚非扣SBC後普通股現金。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：看Security交付/服務組合及Healthcare修復，對照backlog回款與全年指引；下季日期未官方核實。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.osi-systems.com/node/25006) · [来源2](https://stockanalysis.com/stocks/osis/history/) · [来源3](https://stockanalysis.com/stocks/osis/forecast/)

##### HII｜Huntington Ingalls Industries

- **事件核查**：本轮未核到11/2新的集团业绩或回款公告。重读10/29Q3与10-Q：强积压/盈利与营运现金后置并存，不因一天−1.00%认定基本面突然恶化。
- **具名评级与缺项**：11/2 Wells Fargo David Strauss重申Hold、340；不是评级上调。10/30 TD Cowen Gautam Khanna Buy、340，同目标而评级不同。
- **经营支持／持续风险**：10/29 Q3收入約3.5bn、EPS5.48；新合同32.4bn，造船收入指引上調，margin/FCF指引維持。10/30人資主管任命非財務指引變更。 风险：前版風險（歷史底稿，保留追蹤）：訂單能否轉化為現金；Q2自由現金流為負1.50億美元，造船人力、交付和成本執行仍需檢查。 本輪更新：EPS含1.52有利累計完工估計調整。9M CFO99m/FCF−182m，淨合同資產538→1345m；FY26 FCF500–600m需Q4大額回款，不能把造船積壓等同現金。
- **本轮现金核查**：本轮未完成新增完整独立现金估值及全局同额替换比较。
- **下一验证**：跟踪Q4里程碑账单与现金；9M CFO99m、公司FCF−182m，达全年500–600m需Q4约682–782m；合同净资产1.345bn较年初0.538bn上升及EAC盈利须继续拆。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.hii.com/news/hii-reports-third-quarter-2026-results) · [来源2](https://stockanalysis.com/stocks/hii/history/) · [来源3](https://stockanalysis.com/stocks/hii/forecast/) · [来源4](https://www.sec.gov/Archives/edgar/data/1501585/000150158526000056/hii-20260930.htm)

#### 科技（22股）

| 代码／历史来源 | 11/2 Close | 1日 | 5日 | 20日 |
|---|---:|---:|---:|---:|
| [GOOGL](https://stockanalysis.com/stocks/googl/history/) | 278.99 | -0.30% | -11.93% | -19.48% |
| [AMZN](https://stockanalysis.com/stocks/amzn/history/) | 245.63 | +2.20% | -1.39% | -2.30% |
| [MSFT](https://stockanalysis.com/stocks/msft/history/) | 507.12 | -2.83% | -4.78% | -3.44% |
| [META](https://stockanalysis.com/stocks/meta/history/) | 606.73 | -1.34% | -3.78% | -18.22% |
| [ORCL](https://stockanalysis.com/stocks/orcl/history/) | 119.22 | -8.76% | -5.43% | -16.33% |
| [CRM](https://stockanalysis.com/stocks/crm/history/) | 226.18 | -1.30% | -8.65% | -1.57% |
| [ADBE](https://stockanalysis.com/stocks/adbe/history/) | 251.47 | +0.50% | -2.76% | +5.31% |
| [INTU](https://stockanalysis.com/stocks/intu/history/) | 352.10 | +3.23% | +3.59% | +23.68% |
| [ADP](https://stockanalysis.com/stocks/adp/history/) | 298.78 | +1.68% | -0.78% | +14.80% |
| [PAYX](https://stockanalysis.com/stocks/payx/history/) | 115.49 | +3.01% | -0.18% | +15.74% |
| [CSCO](https://stockanalysis.com/stocks/csco/history/) | 101.61 | -2.77% | -7.83% | -9.94% |
| [ANET](https://stockanalysis.com/stocks/anet/history/) | 164.14 | -2.80% | -7.39% | -20.67% |
| [TXN](https://stockanalysis.com/stocks/txn/history/) | 302.02 | +0.39% | +1.31% | +2.41% |
| [ADI](https://stockanalysis.com/stocks/adi/history/) | 412.85 | -1.02% | +1.21% | -1.49% |
| [QCOM](https://stockanalysis.com/stocks/qcom/history/) | 162.08 | -1.64% | -9.76% | -10.35% |
| [AMAT](https://stockanalysis.com/stocks/amat/history/) | 374.53 | -3.99% | -3.37% | -30.93% |
| [LRCX](https://stockanalysis.com/stocks/lrcx/history/) | 227.56 | -4.83% | -4.19% | -34.19% |
| [KLAC](https://stockanalysis.com/stocks/klac/history/) | 153.11 | -3.04% | +2.61% | -25.98% |
| [TSM](https://stockanalysis.com/stocks/tsm/history/) | 398.63 | -1.85% | -6.07% | -17.94% |
| [CDNS](https://stockanalysis.com/stocks/cdns/history/) | 329.51 | +0.49% | +2.28% | -6.78% |
| [DOX](https://stockanalysis.com/stocks/dox/history/) | 63.54 | +1.13% | +1.37% | +8.69% |
| [G](https://stockanalysis.com/stocks/g/history/) | 40.52 | +2.27% | +0.10% | +20.88% |

##### GOOGL｜Alphabet

- **事件核查**：11/2 SEC提交七系列欧元高级无抵押债初步募集说明书，金额、利率和到期日仍留空；Reuters援引承销行材料称规模60亿欧元，不将媒体规模当作已完成到账。Q3单季FCF负而TTM仍正的原判断不变。
- **具名评级与缺项**：11/2公开表列Jefferies Brent Thill Buy 445→400、Cantor Deepak Mathivanan Buy 420→350、BMO Brian Pitz Buy 480→425。Wells Fargo同日目标存在来源冲突：表列417→371，另一具名报道列371→365；须取得原研报才确定修订顺序。
- **经营支持／持续风险**：10/28 Q3收入127.577bn增25%，Search增12%、Cloud增103%至30.7bn（含TPU系統銷售）；營業利益40.576bn增30%，普通股淨利26.17bn/GAAP EPS2.12下降，受投資損失影響。 本轮新增：11/2提出七系列欧元债融资；尚未读到已完成交割证据。 风险：前版風險（歷史底稿，保留追蹤）：美国广告技术补救措施及欧盟监管可能改变数据共享和收费；投资重估与AI资本开支会扭曲表面PE。 本輪更新：Q3 CFO42.290bn−capex51.355bn=FCF−9.065bn；TTM FCF仍+19.747bn，非TTM負現金。Q3普通股發行12.371bn/發債28.996bn及SBC8.630bn提示融資/稀釋；反壟斷救濟與AI搜尋變現風險延續。
- **下一验证**：核Cloud/TPU可重複性、AI搜尋廣告變現、扣SBC及優先股股息後普通股現金；監察司法救濟執行，下一財報日期未官方核實。 核欧元债最终金额/票息/交割、融资后普通股价值及评级修订顺序。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm) · [来源2](https://www.sec.gov/Archives/edgar/data/1652044/000119312526442515/d125079d424b5.htm) · [来源3](https://live.euronext.com/en/financial-news/alphabet-kicks-eu6-billion-bond-sale-tests-appetite-tech-debt) · [来源4](https://ca.investing.com/news/stock-market-news/wells-fargo-cuts-alphabet-stock-price-target-on-ai-overviews-impact-93CH-4921285) · [来源5](https://stockanalysis.com/stocks/googl/ratings/) · [来源6](https://stockanalysis.com/stocks/googl/history/)

##### AMZN｜Amazon

- **事件核查**：11/2未核到新的公司季度财报或经营指引；市场评论聚焦AWS增长及AI投资，具名评级有新变化。原Q3现金表再核后，重资本开支及融资需要仍是重点，不以股价上涨解除。
- **具名评级与缺项**：11/2 CMB Saiyi He维持Buy、301→300；Phillip Helena Wang Buy、320→330，聚合表标Reiterates，Barron报道称Accumulate→Buy，评级动作类别未取得原研报复核。
- **经营支持／持续风险**：10/29 Q3收入201.944bn增12%，營業利益28.1bn；AWS約46bn增39.3%、營業利益17.8bn。Prime Day由2025Q3移至2026多數市場Q2，剔時點影響Q3增速約高400bp，不宜只以總收入斷言核心需求轉弱。 风险：前版風險（歷史底稿，保留追蹤）：TTM自由现金流为负，利润含巨额投资收益；FTC电商垄断诉讼持续，不能用GAAP低PE直接判断便宜。 本輪更新：TTM CFO168.3bn、淨現金capex210.657bn，公司FCF−42.357bn；2026現金capex約220bn，扣SBC後普通股現金更低。FTC反壟斷、AWS競爭/產能及投資收益波動風險延續。
- **本轮现金核查**：本轮复读Q3 SEC现金表：42.422bn−(77.259−1.381)bn=−33.456bn公司简式FCF；再扣SBC5.406bn、融资租赁本金0.433bn及融资义务本金0.107bn，约−39.402bn。TTM公司口径FCF仍−42.357bn，季度与TTM不混用。
- **下一验证**：核AWS收入轉現金和產能投資回報、租賃本金與SBC；FTС案件及後續指引；下季日期未官方核實。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx) · [来源2](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000038/amzn-20260930xex991.htm) · [来源3](https://www.barrons.com/articles/amazon-web-services-stock-earnings-c4f9ea8a) · [来源4](https://stockanalysis.com/stocks/amzn/ratings/) · [来源5](https://stockanalysis.com/stocks/amzn/history/)

##### MSFT｜Microsoft

- **事件核查**：11/2官方与Lumen扩展企业AI网络联合销售合作，但未披露能直接量化的合同金额、净利润或现金承诺。新补读10-Q融资租赁本金，扣SBC及该本金后的季度现金代理仍为正。
- **具名评级与缺项**：11/2 Jefferies Brent Thill Buy650、Barclays Raimo Lenschow Buy610；Phillip Alif Fahmi Hold515，观点分歧仍在。均为公开聚合记录，未取得券商原研报。
- **经营支持／持续风险**：10/28 FY27Q1收入92.279bn增19%、營業利益45.915bn增21%；Azure增48%、commercial RPO677bn增73%。GAAP EPS4.92、剔OpenAI投資影響4.89增18%。 风险：CFO58.000bn−现金capex39.367bn−SBC3.134bn−融资租赁本金1.000bn=14.499bn，为指定扣项现金代理；旧“尚未扣租赁本金”缺项本轮已补。该季Other investing现金流出12.949bn、未开始租赁承诺364.6bn（部分有条件，并非即期债务）、组件供应商应收与受限投资仍须核；AI投入、OpenAI关联风险和CMA拟议SMS事项延续，未完成owner cash归一化。
- **本轮现金核查**：本轮从FY27Q1官方现金表及10-Q租赁附注重算：CFO58.000bn−现金PPE39.367bn=公司简式FCF18.633bn；再扣SBC3.134bn及融资租赁本金1.000bn=14.499bn，仍为正。经营租金和租赁利息已在CFO中，不再重复扣；新增非现金融资租赁资产5.192bn代表未来义务，并非当期再扣一次的现金。不是正常化全年预测。
- **下一验证**：核現金capex/租賃、Azure回報與關聯客戶回款；CMA諮詢11/13截止，最終決定時間仍待監察；下季財報日未官方核實。 跟踪Lumen联合销售能否兑现实际收入与现金，不将合作意向直接资本化。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) · [来源2](https://news.microsoft.com/source/2026/11/02/lumen-and-microsoft-expand-collaboration-to-co-sell-enterprise-ai-ready-networks/) · [来源3](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm) · [来源4](https://stockanalysis.com/stocks/msft/ratings/) · [来源5](https://stockanalysis.com/stocks/msft/history/)

##### META｜Meta Platforms

- **事件核查**：11/2 Reuters转述Bloomberg匿名知情人士称公司考虑至少200亿美元跨境发债；报道明确尚未最终决定。属融资线索而非已交割事实，旧增发/强制可转优先股、AI现金投入及New Mexico判决风险继续。
- **具名评级与缺项**：11/2未核到新具名动作；可核表最新10/28 TD Cowen John Blackledge Buy850等。10/30 S&P展望转负属信用观点，不是11/2股票评级。
- **经营支持／持续风险**：10/26–27新增融资：25bn美元Class A普通股forward出售、12.5bn美元6.5%强制可转优先股；官方定价页10/27、正文电讯日期10/26。不能把forward全写成现金已到账。 风险：承接10/21 New Mexico25bn判决、AI资本开支和现金流压力。10/30 Reuters报道S&P展望Stable→Negative；完整S&P评级原报告未取得。优先股分配与未来转换会影响普通股股东收益。 11/2媒体另报考虑至少200亿美元跨境债券，未最终决定；仅作待核融资线索，不能当成已发行。
- **下一验证**：核forward实际结算、优先股现金/股份股息、Class C/ATM授权与稀释；法院上诉/现金支付。下一季度正式财报日期本轮未取得公司确认，不填写猜测日。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Pricing-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx) · [来源2](https://www.reuters.com/business/meta-eyes-least-20-billion-potential-bond-offerings-bloomberg-news-reports-2026-11-02/) · [来源3](https://stockanalysis.com/stocks/meta/ratings/) · [来源4](https://stockanalysis.com/stocks/meta/history/)

##### ORCL｜Oracle

- **事件核查**：11/2 SEC初步文件正式提出100亿美元普通股和同步100亿美元高级票据发行；两项交割互不构成前提，文件未证明已经到账。由先前融资上限目标进入具体融资阶段，需审最终定价、稀释和资金使用。
- **具名评级与缺项**：11/2 Stephens Brett Huff由Hold升Buy、185→213；高目标价不解除负FCF、融资稀释和项目兑现风险。
- **经营支持／持续风险**：10/28 Investor Day重申FY27收入至少90bn、调整EPS8.10；设FY30收入225bn+、调整经营利润率40%+和调整EPS21+目标。 本轮新增：11/2正式提交100亿美元普通股及同步100亿美元票据发行，尚不等于到账。 风险：FCF转正仍是FY28下半年目标、FY29至少30bn目标，尚未实现；FY27–28资本开支高峰。新增融资目标上限20bn不含再融资，且是在Q1已完成20bn ATM之外。非GAAP剔SBC，须恢复普通股成本。 融资进入具体发行阶段；普通股稀释、最终定价与付息义务须重算，不因Stephens上调评级解除。
- **下一验证**：核FY27–28项目交付、预付款/客户硬件/供应商融资与资本开支匹配；下一财报公司未确认，12/14仅第三方估计。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Investor-Day-2026-Accelerating-Value-Creation/default.aspx) · [来源2](https://www.sec.gov/Archives/edgar/data/1341439/000119312526442729/d181425d424b5.htm) · [来源3](https://stockanalysis.com/stocks/orcl/ratings/) · [来源4](https://stockanalysis.com/stocks/orcl/history/)

##### CRM｜Salesforce

- **事件核查**：11/2定向查询未核到新的季度结果、Braze完成交割或指引改变；当日跌幅是价格事实，不作为AI替代或并购失败的证明。Braze签约及收购后现金缺项继续。
- **具名评级与缺项**：11/2未核到新具名动作；公开表最新10/26 BofA Tal Liani Buy、无目标价，不能编造缺失目标。
- **经营支持／持续风险**：窗口内未核到新季度财报或Braze交易完成公告；承接10/20已签约以约5.66bn企业价值收购Braze，普通股对价47.50美元现金/股。 风险：并购支出、Informatica并表与有机增长、SBC以及AI替代席位收费的旧风险未消除。不要把签约写成交割，亦未完成收购后普通股现金模型。
- **下一验证**：核Braze融资/审批/交割和每股现金影响；下一财报12/2有第三方估计/确认标记冲突，本轮未得公司日期公告。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Braze/default.aspx) · [来源2](https://www.benzinga.com/quote/crm) · [来源3](https://stockanalysis.com/stocks/crm/ratings/) · [来源4](https://stockanalysis.com/stocks/crm/history/)

##### ADBE｜Adobe

- **事件核查**：11/2定向查询未核到新财务指引；可核公司新闻仍为10/22 Alpine合作、10/15 NVIDIA合作等旧事项，不能称11/2新催化。现价附近并未完成无倍数扩张替代比较。
- **具名评级与缺项**：11/2未核到新动作；10/13 HSBC Stephen Bersey降Hold、310→267及10/12 Wells Fargo Michael Turrin降Sell、270→225仍是最强反方。
- **经营支持／持续风险**：10/22至截止未核到新的财务指引；9/10Q3收入6.76bn、GAAP EPS4.62；AI免费用户付费转化仍须实际季度验证。10/15 NVIDIA协作是窗口前消息。 风险：AI竞争、免费策略、CEO12/1交接承接；不能用含SBC剔除的调整EPS直接和GAAP比较。9M CFO7.646bn−PPE0.180bn−SBC1.582bn=5.884bn规模锚，未经季节性/并购正常化，非FY27承诺。
- **下一验证**：核新增ARR、付费转化/流失、收购现金与净股数；下一财报12/9仅第三方估计，未取得公司确认。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm) · [来源2](https://markets.financialcontent.com/stocks/quote/news?ChannelType=PRESSRELEASES&Symbol=NQ%3AADBE) · [来源3](https://stockanalysis.com/stocks/adbe/ratings/) · [来源4](https://stockanalysis.com/stocks/adbe/history/)

##### INTU｜Intuit

- **事件核查**：11/2官方IR新闻目录仍列10/29财报日程、10/27 Intelligence扩展、10/20 Credit Karma Tax及10/15 Sequence收购。未核到11/2新增指引；股价强势不等于已兑现新产品利润。
- **具名评级与缺项**：11/2未核到新具名动作；公开表最新10/12 Morgan Stanley Adam Wood Hold315，10/7 Citi Steve Enders Buy416。表本身更新/检查日期滞后，不能据此穷尽全部11/2研报。
- **经营支持／持续风险**：10/27 Intuit Intelligence横跨QuickBooks、Enterprise Suite、Accountant Suite推出更新，含行业版本、月结和应收工具；部分为beta/即将推出，不能作已兑现利润。10/29确认11/19财报。 风险：承接Sequence收购、Mailchimp弱势和AI竞争；FY27非GAAP已保留SBC，不应再扣5.81/股。FY27收入+9–10%、GAAP EPS20.12–20.36为公司指引，非已实现。
- **下一验证**：11/19盘后FY27Q1，核GBS真实增长/付费、Mailchimp、Sequence财务贡献及普通股现金。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.intuit.com/news-events/press-releases/detail/1329/intuit-expands-intelligence-platform-to-power-the-next-era-of-accounting-firm-and-business-growth) · [来源2](https://investors.intuit.com/news-events) · [来源3](https://stockanalysis.com/stocks/intu/ratings/) · [来源4](https://stockanalysis.com/stocks/intu/history/)

##### ADP｜Automatic Data Processing

- **事件核查**：11/2定向查询未核到新财务指引；承接10/28FY27Q1经营增长与现金转化差异。官方新闻目录存在加载/检索覆盖限制，不将检索无新增当作无风险证明。
- **具名评级与缺项**：11/2未核到新动作；10/29 Stifel David Grossman Hold285→305、Citi Bryan Keane Hold287→295。Morgan Stanley目标变动方向跨来源冲突，暂不把方向作为本轮事实。
- **经营支持／持续风险**：10/28FY27Q1收入5.491bn增长6%（有机固定汇率6%），GAAP EPS2.83增长14%；全年收入增速提高至约6%，GAAP EPS增长12–14%、调整EPS增长10–12%。 风险：利润增长与现金增长不同：本季CFO651m对642.3m；扣PPE52.7m、无形资产资本化117.1m、SBC67.2m后约414m，对上年442.8m。客户资金/限制现金不能作普通股自由现金。就业、客户资金利率风险承接。
- **下一验证**：核新签约、留存、每客户人数、资本化软件和客户资金收益；下一季1/27/2027只是第三方估计，未有公司确认。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/8670/000000867026000033/q1fy27exhibit99.htm) · [来源2](https://investors.adp.com/news/default.aspx) · [来源3](https://stockanalysis.com/stocks/adp/ratings/) · [来源4](https://stockanalysis.com/stocks/adp/history/)

##### PAYX｜Paychex

- **事件核查**：11/2公司IR金融新闻目录最新仍10/15股息与9/23Q1；公司10/26行业奖项属窗口内旧新闻，不是新订单。未核到11/2新经营指引。
- **具名评级与缺项**：11/2未核到新动作；10/29 UBS Kevin McVeigh Hold120为最新可核表记录。
- **经营支持／持续风险**：官方财务新闻目录最新10/15股息、9/23Q1结果；窗口内未核到新季度或全年指引变化。承接Q1收入约+6%、PEO/保险增长和Paycor整合观察。 风险：中小企业就业、客户流失、整合支出及客户资金利率敏感性继续。10/29评级维持不解决现金流和有机增速问题。
- **下一验证**：核Paycor整合后有机收入/保留率/每股现金；下一财报公司未确认，第三方12/17、12/18、12/21–23冲突，不指定确切日。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.paychex.com/news-events/press-releases/detail/850/paychex-reports-first-quarter-fiscal-2027-results) · [来源2](https://investor.paychex.com/news-events/press-releases) · [来源3](https://investor.paychex.com/news-events) · [来源4](https://stockanalysis.com/stocks/payx/ratings/) · [来源5](https://stockanalysis.com/stocks/payx/history/)

##### CSCO｜Cisco Systems

- **事件核查**：11/2新增检索结果多为机构持仓披露及旧业务综述，未核到足以解除10/28 ASA/FTD漏洞补救风险的新公司公告；持仓披露日期不等于当日买卖。
- **具名评级与缺项**：11/2未核到新动作；10/26 Bernstein Daniel Zhu Hold110为最新可核表记录。
- **经营支持／持续风险**：10/28官方新增CVE-2026-76418：特定ASA/FTD SSLVPN和secondary authentication配置可被未认证攻击导致重启DoS，官方称10月已主动利用，已有修补。10/27 Node.js跨产品调查亦在进行。 风险：承接10/14邮件网关漏洞及客户影响；补丁不证明赔付/声誉影响已核清。Node.js公告未确认被恶意用于Cisco产品；不可把所有在调查产品写成已受害。媒体10/30重述ISE76460，原始首发9/16，不作新案件。
- **下一验证**：核客户损害/修复成本、订单和毛利；下一财报11/12有第三方confirmed与原电话会转述，11/11系另一第三方估计；本轮未取得独立公司日期公告，保留冲突。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75) · [来源2](https://www.marketbeat.com/stocks/NASDAQ/CSCO/%5C/news/) · [来源3](https://stockanalysis.com/stocks/csco/ratings/) · [来源4](https://stockanalysis.com/stocks/csco/history/)

##### ANET｜Arista Networks

- **事件核查**：11/2新评级重申但没有新季度结果；11/3美东盘后Q3、16:30电话会由公司确认。VeloCloud漏洞与客户损失未量化的旧风险继续，不扩大为全部交换机受害。
- **具名评级与缺项**：11/2 J.P.Morgan Joseph Cardoso重申Buy250；Evercore Amit Daryanani重申Outperform250另有当日04:25EST具名公开转述。
- **经营支持／持续风险**：10/22官方VeloCloud Orchestrator CVE-2026-114625被主动利用；10/23政府通报列入CISA KEV。Hosted版本已修补，Onprem受影响版本须升级；EOS交换机等明确不受影响。 风险：承接云客户集中、高预期估值风险；新增VCO补救/客户损失未量化，不能把VCO漏洞扩大成所有交换机受害。
- **下一验证**：11/3盘后Q3、16:30EST电话会已由10/6公司公告确认；核订单、毛利、库存和VCO客户影响。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199) · [来源2](https://www.arista.com/zh/company/news/press-release/24817-pr-20261006) · [来源3](https://new.streetinsider.com/Analyst%2BComments/Evercore%2BISI%2BReiterates%2BOutperform%2BRating%2Bon%2BArista%2BNetworks%2B%28ANET%29/27268253.html) · [来源4](https://stockanalysis.com/stocks/anet/ratings/) · [来源5](https://stockanalysis.com/stocks/anet/history/)

##### TXN｜Texas Instruments

- **事件核查**：11/2公司IR目录最新为10/26发行20亿美元投资级票据、10/21Q3结果，未核到新财务指引。旧现金补助及资本开支归一化要求继续。
- **具名评级与缺项**：11/2未核到新动作；10/28 DZ Bank Ingo Wermann升Hold300，BofA Vivek Arya Buy370；评级分歧不能用均值掩盖。
- **经营支持／持续风险**：承接10/21Q3，本轮补读原文：收入6.055bn同比+28%，GAAP EPS2.62；工业、汽车和数据中心广泛增长；Q4收入5.8–6.3bn、EPS2.45–2.79指引。 风险：TTM headlineFCF8.422bn含1.104bn CHIPS补助；CFO9.896bn亦含469m投资税抵免减税，不能把补助全部作永续业务现金。仍需扣SBC并检验300mm资本开支周期。
- **下一验证**：核库存/利用率、工业汽车终端需求、SBC及正常资本开支；下一财报1/26/2027为第三方估计，未有公司确认。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.ti.com/news-releases/news-release-details/ti-reports-third-quarter-2026-financial-results-and-shareholder) · [来源2](https://ti.gcs-web.com/investor-news) · [来源3](https://stockanalysis.com/stocks/txn/ratings/) · [来源4](https://stockanalysis.com/stocks/txn/history/)

##### ADI｜Analog Devices

- **事件核查**：11/2官方新闻/日程检索未核到新指引；10/22确认11/24财报，10/21公司拒绝Tutanota mini-tender是旧事项。机构减持文章不证明经营恶化。
- **具名评级与缺项**：11/2未核到新动作；10/26 Bernstein Stacy Rasgon维持Buy465。
- **经营支持／持续风险**：10/22公司确认11/24 FY26Q4，07:00EST发布、10:00电话会；窗口内未核到新季度结果/指引。承接数据中心和工业复苏。 风险：承接补库与真实需求混淆、汽车/出口风险；AI合作新闻不等于新增盈利，Alif收购影响须另审，未由本轮完成并购现金估值。
- **下一验证**：11/24财报核终端订单、毛利、营运资本和收购现金分配。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.analog.com/news-releases/news-release-details/analog-devices-report-fourth-quarter-fiscal-year-2026-financial) · [来源2](https://investor.analog.com/press-releases) · [来源3](https://analogdevices.gcs-web.com/news-releases/news-release-details/analog-devices-report-fourth-quarter-fiscal-year-2026-financial) · [来源4](https://stockanalysis.com/stocks/adi/ratings/) · [来源5](https://stockanalysis.com/stocks/adi/history/)

##### QCOM｜Qualcomm

- **事件核查**：11/2 Bernstein下调目标价并指出手机需求/内存环境及近端预测风险；这是分析师判断，不是公司撤回指引。官方仍定11/4盘后出FY26Q4，16:45EST电话会。
- **具名评级与缺项**：11/2 Bernstein Stacy Rasgon维持Market Perform/Hold、165→155；重点反方是手机仍占销售大头及近端预测或需下修，不用远年数据中心空间抵销。
- **经营支持／持续风险**：10/22官方确认11/4盘后FY26Q4及全年结果，16:45EST电话会。窗口内未核到新财务指引；不要把2025/10 AI200/AI250发布当2026新催化。 风险：承接Q3手机收入−20%、QCT−5%，汽车/IoT增长尚须抵消；客户自研、中国和许可风险仍在。10/30大跌不独立证明基本面变坏或值得抄底，未以AI新闻摘要替代原始业绩。
- **下一验证**：11/4核手机/Apple收入缺口、汽车/IoT利润和数据中心商业收入/现金投入。 另核11/2 Bernstein近端手机预测下修反方，与公司FY27展望对照。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx) · [来源2](https://www.qualcomm.com/news/releases/2026/10/qualcomm-schedules-fourth-quarter-and-fiscal-2026-earnings-relea) · [来源3](https://price-target.com/2026/11/02/176573/) · [来源4](https://stockanalysis.com/stocks/qcom/ratings/) · [来源5](https://stockanalysis.com/stocks/qcom/history/)

##### AMAT｜Applied Materials

- **事件核查**：11/2新UBS评级维持；公司新闻目录最新经营资本事项仍10/26 Besi增持协议，11/2报道回顾的是10/30跌幅。未核到Besi交付完成或新财务指引。
- **具名评级与缺项**：11/2 UBS Timothy Arcuri维持Buy695；未读原研报，不能以高目标价替代出口与资金成本核查。
- **经营支持／持续风险**：10/26签加速购股协议拟把Besi股权提高至约20%，扩展先进封装/混合键合协作；仍有HSR等待条件，未确认交付完成，官方未披露本次支出金额。 风险：旧BIS案2月已解决，不重写成新未决案；中国出口、资本开支周期延续。Besi增持是现金资本配置，不能把预期协同直接记利润。
- **下一验证**：11/12 16:30EST FY26Q4电话会已由10/22官方确认；核Besi资金成本、先进工艺/服务现金和出口许可。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.appliedmaterials.com/us/en/newsroom/press-releases/102626-increase-investment-besi-semiconductor.html) · [来源2](https://www.appliedmaterials.com/us/en/newsroom/press-releases.html) · [来源3](https://stockanalysis.com/stocks/amat/ratings/) · [来源4](https://stockanalysis.com/stocks/amat/history/)

##### LRCX｜Lam Research

- **事件核查**：11/2新Bernstein评级维持；定向查询未核到新的公司季报或指引，10/21强业绩、营运资本流入和出口风险继续。板块下跌不能直接证明设备订单取消。
- **具名评级与缺项**：11/2 Bernstein Stacy Rasgon维持Buy350；不是新的目标上调，原10/26降至350仍保留历史。
- **经营支持／持续风险**：承接10/21九月季原文：收入8.219bn环比+22%、GAAP EPS2.19、经营利润率40%；十二月季收入8.6bn±0.4bn、GAAP EPS2.33±0.15。 风险：本季CFO3.498bn−资本开支/无形257.697m−SBC114.696m约3.125bn，含535m营运资本流入不能全季年化。中国占收入35%；出口许可和存储资本开支风险继续。
- **下一验证**：核下季供应约束、CSBG增长、客户存储预算及中国收入；下一季公司未确认，第三方1/20与1/27/2027冲突，不写确定日。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://newsroom.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026) · [来源2](https://chartexchange.com/symbol/nasdaq-lrcx/news/) · [来源3](https://stockanalysis.com/stocks/lrcx/ratings/) · [来源4](https://stockanalysis.com/stocks/lrcx/history/)

##### KLAC｜KLA

- **事件核查**：11/2查询未核到新的公司结果/指引或具名新评级；承接10/28FY27Q1及10/30 Argus重申，股价下降与行业压力一致但未识别独立因果。
- **具名评级与缺项**：11/2未核到新动作；10/30 Argus Jim Kelleher Buy225，均按10拆1后价格口径。
- **经营支持／持续风险**：10/28FY27Q1收入4.136bn、GAAP EPS1.18（10拆1后），均超过指引中位；下季收入4.7bn±0.2bn、GAAP EPS1.41±0.11。 风险：季度CFO1.531bn−PPE194.756m−SBC84.073m约1.252bn；headlineFCF1.336bn未扣SBC。库存433.839m、应收179.196m占款；客户集中、出口风险和拆股口径继续。
- **下一验证**：核检测强度、服务、库存/应收回款、中国许可；下季正式公司日尚未核得，1/27或1/28/2027仅第三方预测。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/319201/000031920126000032/exhibit991earningsrelease0.htm) · [来源2](https://www.marketbeat.com/stocks/NASDAQ/KLAC/news/) · [来源3](https://stockanalysis.com/stocks/klac/ratings/) · [来源4](https://stockanalysis.com/stocks/klac/history/)

##### TSM｜Taiwan Semiconductor Manufacturing

- **事件核查**：11/2定向查询未核到新公司月营收或财务指引；官方日历下一10月营收11/10 13:30台北时间。台海、出口合规与海外成本风险继续，不把匿名旧罚款传闻当新执法。
- **具名评级与缺项**：11/2未核到新动作；10/16 D.A.Davidson Gil Luria Buy500、Bernstein Mark Li Buy430→554为窗口前承接，不能写成本轮上调。
- **经营支持／持续风险**：10/22 Reuters称公司寻求工厂设备稀土替代，属于匿名来源供应链风险线索，尚未确认产量损失；10/15Q3官方资料继续为业绩基准。 风险：承接台海集中、海外成本和旧出口合规调查，未取得正式结案依据；不把2025传闻罚款当新罚款。稀土替代不代表已供应中断。
- **下一验证**：官方日历下一经营数据11/10 13:30台北时间10月营收；下一季度财报本轮未核到确定公司日期。核先进节点/封装利用率与海外成本。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.tsmc.com/english/quarterly-results/2026/q3) · [来源2](https://investor.tsmc.com/english/financial-calendar) · [来源3](https://www.marketbeat.com/stocks/NYSE/TSM/news/) · [来源4](https://stockanalysis.com/stocks/tsm/ratings/) · [来源5](https://stockanalysis.com/stocks/tsm/history/)

##### CDNS｜Cadence Design Systems

- **事件核查**：11/2财经文章回顾10/26已发布Q3与上调全年收入指引，不是再次上调；10/29加入DOE Genesis Mission联盟是新补纳的合作线索，没有可量化新增订单/现金。
- **具名评级与缺项**：11/2未核到新动作；10/27 Goldman James Schneider Buy470、Rosenblatt Blair Abernethy Buy420→425承接。
- **经营支持／持续风险**：10/26Q3收入1.633bn同比+22%、重复收入+18%、backlog8.2bn；全年收入增长指引提高至约21%。GAAP EPS1.05同比持平，不能只报调整EPS2.11增长。 10/29加入DOE Genesis Mission联盟仅为合作线索，不等于已兑现新增订单。 风险：GAAP经营利润率26.2%对31.8%，SBC、并购摊销和重组形成差异；9M CFO1.414bn−PPE163.254m−无形6.975m−SBC429.836m约814.371m；并购现金2.143bn须另审。出口/2025和解持续义务承接。
- **下一验证**：核订单转收入、整合毛利和普通股现金。下一季公司未确认，2/23/2027仅第三方估计。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Third-Quarter-2026-Financial-Results/default.aspx) · [来源2](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr-ir/2026/cadence-reports-third-quarter-2026-financial-results.html) · [来源3](https://wkow.marketminute.com/quote/NQ%3ACDNS/pressReleases) · [来源4](https://stockanalysis.com/stocks/cdns/ratings/) · [来源5](https://stockanalysis.com/stocks/cdns/history/)

##### DOX｜Amdocs

- **事件核查**：11/2未核到FY26Q4新结果；官方索引仍确认11/3 17:00EST电话会，第三方11/10估计与官方冲突，不采用该估计。11/1晚间预告是本次窗口内新增二手材料，只是预期，不能当作FY27指引。
- **具名评级与缺项**：11/2未核到新动作；最新可核表8/7 Stifel Shlomo Rosenbaum Buy71，6/29 KeyBanc Devin Au首次Hold；表更新滞后，未核到不等于不存在。
- **经营支持／持续风险**：窗口内未核到新公司财务指引；公司日历FY26Q4 11/3 17:00EST，日期在10/22旧档已存在。10/8出售Vubiquity的净经常盈利影响仍未量化。11/1晚间财报预告发生在晨报截止之后，不纳入。 风险：承接收入+2.7%、Q3重组106m和剥离。SEC确认9M GAAP EPS3.33，剔重组影响1.07后4.40；9M普通股现金518.983−78.769−83.692−3.113=353.409m。不能把710–730m排重组FCF指引当实际普通股现金。 本轮另识别37.260m并购递延/或有支付，资本配置现金单列；353.409m桥不等于包括全部收购支付后的余额。
- **本轮现金核查**：本轮复读旧6-K现金表：9M CFO518.983m−PPE78.769m−SBC83.692m−NCI分配3.113m=353.409m。另有并购或有/递延对价37.260m，作为资本配置义务单列，若扣后为316.149m，不自动当经常营运费用。处置Vubiquity净EPS、持续重组仍待新财报验证。
- **下一验证**：11/3盘后/17:00EST核FY27剥离后收入、GAAP、持续重组支出与现金。d为处置净EPS影响，与重组R分开。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1062579/000119312526355408/6k_q3_26.htm) · [来源2](https://investors.amdocs.com/events-presentations/ir-event-calendar) · [来源3](https://finance.yahoo.com/markets/stocks/articles/amdocs-dox-reports-q3-everything-030936240.html) · [来源4](https://stockanalysis.com/stocks/dox/ratings/) · [来源5](https://stockanalysis.com/stocks/dox/history/)

##### G｜Genpact

- **事件核查**：11/2官方新闻目录最新仍10/28行业称号；未核到新季度指引。11/5盘后Q3、17:00EST电话会由官方确认。H1回款和普通股现金弱项仍未被新资料解除。
- **具名评级与缺项**：11/2未核到新动作；可核10/22 Susquehanna James Friedman Hold37→40，TipRanks另一页标10/21，日期存在一天差异，沿用较明确表但保留冲突。
- **经营支持／持续风险**：10/28官方NelsonHall F&A Transformation Leader称号是行业认可，不是新增订单/利润。Q2总收入+7.1%、ATS+24.1%承接；未见窗口内新财报。 风险：CBS占73%、Q3预期持平至微降；H1 CFO48.908m，扣PPE37.855m/内部无形16.093m/SBC48.632m约−53.672m，含资产处置后仍−49.955m；回款风险未解除。 本轮补扣融资租赁本金3.826m，H1经营现金代理−57.498m；如单列加入资产处置3.717m则−53.781m，不把处置当永续现金。
- **本轮现金核查**：本轮复读H1官方现金表：48.908m−PPE37.855m−资本化无形16.093m−SBC48.632m=−53.672m；进一步扣融资租赁本金3.826m为−57.498m。资产处置收入3.717m单列，若含入则−53.781m，不能把处置收入作永续经营现金。季节性不能单凭半年度判定长期失败。
- **下一验证**：11/5盘后Q3、17:00EST电话会官方确认；核应收/回款、CBS、ATS收费和普通股现金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://media.genpact.com/2026-08-06-Genpact-Reports-Second-Quarter-2026-Results) · [来源2](https://media.genpact.com/news-releases) · [来源3](https://media.genpact.com/2026-10-08-Genpact-to-Report-Third-Quarter-2026-Results) · [来源4](https://stockanalysis.com/stocks/g/ratings/) · [来源5](https://stockanalysis.com/stocks/g/history/)

#### 消費與能源（21股）

| 代码／历史来源 | 11/2 Close | 1日 | 5日 | 20日 |
|---|---:|---:|---:|---:|
| [TJX](https://stockanalysis.com/stocks/tjx/history/) | 141.00 | +0.49% | -1.88% | +4.90% |
| [ROST](https://stockanalysis.com/stocks/rost/history/) | 230.59 | +1.01% | -1.50% | +1.86% |
| [ULTA](https://stockanalysis.com/stocks/ulta/history/) | 637.57 | -0.45% | +1.96% | +17.48% |
| [LOW](https://stockanalysis.com/stocks/low/history/) | 218.15 | +4.34% | +10.05% | +21.53% |
| [HD](https://stockanalysis.com/stocks/hd/history/) | 341.15 | +3.63% | +6.82% | +21.34% |
| [ORLY](https://stockanalysis.com/stocks/orly/history/) | 90.70 | +2.93% | -0.38% | +8.10% |
| [AZO](https://stockanalysis.com/stocks/azo/history/) | 3253.01 | +2.62% | +1.97% | +15.86% |
| [CMG](https://stockanalysis.com/stocks/cmg/history/) | 32.91 | +3.20% | +15.84% | +6.68% |
| [HLT](https://stockanalysis.com/stocks/hlt/history/) | 364.71 | +2.18% | +3.64% | +15.37% |
| [LNG](https://stockanalysis.com/stocks/lng/history/) | 311.67 | -5.65% | +3.69% | +13.36% |
| [EOG](https://stockanalysis.com/stocks/eog/history/) | 157.89 | -4.62% | -3.54% | +9.58% |
| [XOM](https://stockanalysis.com/stocks/xom/history/) | 179.67 | -4.05% | -2.64% | +9.55% |
| [CVX](https://stockanalysis.com/stocks/cvx/history/) | 227.77 | -3.29% | -1.83% | +10.32% |
| [FANG](https://stockanalysis.com/stocks/fang/history/) | 199.74 | -5.82% | -3.57% | +8.51% |
| [NEE](https://stockanalysis.com/stocks/nee/history/) | 85.03 | +1.58% | +3.64% | +11.47% |
| [DUK](https://stockanalysis.com/stocks/duk/history/) | 128.38 | +0.78% | +3.17% | +12.77% |
| [AEP](https://stockanalysis.com/stocks/aep/history/) | 130.33 | +0.09% | +0.86% | +8.85% |
| [CEG](https://stockanalysis.com/stocks/ceg/history/) | 257.25 | -1.96% | +1.89% | -3.87% |
| [VST](https://stockanalysis.com/stocks/vst/history/) | 134.61 | -2.72% | -5.02% | -7.10% |
| [PRDO](https://stockanalysis.com/stocks/prdo/history/) | 29.66 | -0.50% | -9.32% | -5.96% |
| [BKNG](https://stockanalysis.com/stocks/bkng/history/) | 153.75 | +3.79% | +0.40% | -2.89% |

##### TJX｜TJX Companies

- **事件核查**：11/2可见13F持仓转述并非当日买卖、不是公司盈利新催化。
- **具名评级与缺项**：11/2未核到新具名动作；承接10/27 BofA Lorraine Hutchinson Buy、175→170。
- **经营支持／持续风险**：窗口内未核到新季度财报或公司利润指引更新；官方日历预计11/18 FY27Q3。承接Q2同店+4%、调整EPS+11%的业务基础。 风险：承接Marmaxx较弱、关税退款抬高GAAP收益；本轮没有依据把退款年化或把分析师Buy当估值已通过。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：11/18 Q3（官方expected、日期可变）核Marmaxx同店、退款剔除后毛利、库存与普通股现金。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/109198/000010919826000045/tjxq2fy27earningspressrele.htm) · [来源2](https://stockanalysis.com/stocks/tjx/history/) · [来源3](https://stockanalysis.com/stocks/tjx/ratings/)

##### ROST｜Ross Stores

- **事件核查**：11/2出现UBS10/26升评的再次报道，事件日期不前移。
- **具名评级与缺项**：补旧记录遗漏：10/27 BofA Lorraine Hutchinson Buy、265→258；10/26 UBS Jay Sole升Buy、239→315，11/2转载不是新升评。
- **经营支持／持续风险**：最新正式業績仍為8/20 Q2：同店+10%、總收入+13%，主要由客流推動。10/26 UBS認為新CEO可透過商品、營運與營銷縮小對TJX的門店生產率差距；這是分析師假說，非新財報。 风险：Q2 EPS2.66包含約0.60關稅退款，不能把報告EPS全部視作經常盈利；客流強但下一季與估值尚待驗。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：Q3官方日期本輪未確認：資料商11/12與11/19估計不一致，均不當已核日期；等公司正式公告，再驗客流及扣退款利潤率。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.rossstores.com/node/23266/pdf) · [来源2](https://www.ad-hoc-news.de/boerse/news/corporate-news/ross-stores-stock-gets-ubs-boost-as-ceo-targets-productivity-gap/70446622) · [来源3](https://stockanalysis.com/stocks/rost/history/) · [来源4](https://stockanalysis.com/stocks/rost/ratings/)

##### ULTA｜Ulta Beauty

- **事件核查**：11/2行业媒体报道KSECRET进入500多门店，未取得可量化公司盈利影响，作为商品线线索不作上修。
- **具名评级与缺项**：11/2未核新动作；10/23 Jefferies Sydney Wagner Buy、670→730承接。
- **经营支持／持续风险**：正式最新Q2仍為8/27。門店／線上與Space NK整合支持研究；Q2截止8/1，不能驗證8月結束Target合作後的客流。 风险：促銷、併購與回購融資、Target退出後客流轉移均須留在風險；分析師升目標未證明股東現金改善。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：官方IR日曆確認12/3 Q3電話會；核Target合作結束後的同店、毛利、Space NK及淨現金／借款。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.ulta.com/investor/news-events/press-releases/detail/234/ulta-beauty-announces-second-quarter-fiscal-2026-results) · [来源2](https://massmarketretailers.com/ksecret-expands-u-s-retail-presence-via-ulta-beauty-launch/) · [来源3](https://stockanalysis.com/stocks/ulta/history/) · [来源4](https://stockanalysis.com/stocks/ulta/ratings/)

##### LOW｜Lowe's

- **事件核查**：11/2未核到公司新利润指引；房屋装修需求、收购融资风险继续。
- **具名评级与缺项**：11/2未核新动作；10/30 Stifel W. Andrew Carter Hold195，不能把价格上涨当研究上修。
- **经营支持／持续风险**：最新正式Q2為8/19；專業客戶與FBM／ADG可拓展分銷，但8月同店／全年指引收窄後仍待新季驗證。 风险：高房貸利率、大額裝修需求弱；收購後利息與整合支出不能被調整EPS遮蓋。未核得10/22後新的公司盈利指引。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：公司日曆列11/18 Q3電話會但明標tentative，故僅暫定；核同店、收購有機分拆、利息與全額capex現金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://corporate.lowes.com/newsroom/press-releases/lowes-reports-second-quarter-2026-sales-and-earnings-results-08-19-26) · [来源2](https://stockanalysis.com/stocks/low/history/) · [来源3](https://stockanalysis.com/stocks/low/ratings/)

##### HD｜Home Depot

- **事件核查**：11/2未核到公司新利润指引；AI/营销或零售专题不是新季度盈利。
- **具名评级与缺项**：11/2未核新动作；10/30 Stifel W. Andrew Carter Hold322承接。
- **经营支持／持续风险**：最新正式Q2為8/18：收入47.9bn、+5.7%，同店+1.7%。SRS／GMS增加規模，但住宅大項目需求與有機修復仍待Q3。 风险：收購收入不能等同有機增長；房貸利率、大額裝修、整合成本與債務仍是實質風險。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：官方日曆確認11/17 09:00 ET Q3業績活動；核大額交易、同店、SRS/GMS現金轉換及淨債。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/354950/000035495026000145/hd_exhibit991x08022026.htm) · [来源2](https://stockanalysis.com/stocks/hd/history/) · [来源3](https://stockanalysis.com/stocks/hd/ratings/)

##### ORLY｜O'Reilly Automotive

- **事件核查**：11/2未核到新财报或公司盈利指引；重新核10/28 Q3及现金表：同店+7.2%、净利润+8%、EPS+14%，含3900万美元关税退款。
- **具名评级与缺项**：11/2未核新动作；10/30 UBS Michael Lasser Buy120→122；Barclays Seth Sigman Hold98，分歧保留。
- **经营支持／持续风险**：10/28 Q3同店+7.2%、收入5.12bn/+9%、EPS0.97/+14%；專業業務雙位數增長、DIY中單位數增長。全年同店上調5.5–6.5%，EPS3.25–3.35。 风险：Q3有39m關稅退款；淨利+8%低於EPS+14%，回購放大每股增長。FY26公司FCF1.9–2.2bn、capex1.3–1.4bn，仍須扣持續SBC並核債務，不能只看EPS。 本轮现金补核：Q3 CFO558.743m减capex308.223m=250.520m，较去年304.437m降约17.7%；9M扣capex/SBC简化代理1711.593m仍未归一化退款和营运资金。9M回购3467.904m、新发债2446.149m。
- **本轮现金核查**：9M CFO25.98155亿−capex8.60273亿−SBC0.26289亿＝17.11593亿美元简化现金代理，尚未正常化退款/营运资金与租赁；9M回购34.67904亿明显高于同期该代理，融资不能忽略。Q3 CFO5.58743亿−capex3.08223亿＝2.50520亿，同比3.04437亿下降约17.7%，不能只强调9M现金改善。
- **下一验证**：核10-Q租赁/退款全额和正常化现金，估值与最强替换对象同额比较；下一官方季报日未核。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/898173/000089817326000050/orly-ex99d1.htm) · [来源2](https://stockanalysis.com/stocks/orly/history/) · [来源3](https://stockanalysis.com/stocks/orly/ratings/)

##### AZO｜AutoZone

- **事件核查**：CFO11/25离任仍待接续，未核11/2新增会计/业绩分歧；不能自行当财务造假。
- **具名评级与缺项**：11/2未核新动作；10/26 TD Cowen Max Rakhlenko Buy3400、BofA Christopher Nardone Buy3800承接。
- **经营支持／持续风险**：10/26公告CFO Jamere Jackson將11/25離職，已展開外部接任搜尋；過渡期由Controller J. Scott Murphy擔任主要財務主管。公司稱離任與業績或會計分歧無關，不能自行推論財務問題。 风险：承接Q4國內同店僅+1.6%、商業客戶銷售+8.6%；需核配送投資、槓桿回購與管理層交接，未把CFO離職當盈利下修。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：11/25財務主管交接、接任公告；下一次FY27Q1官方業績日期本輪未核，不把資料商12月估計當確認。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/866787/000117184326006805/f8k_102326.htm) · [来源2](https://stockanalysis.com/stocks/azo/history/) · [来源3](https://stockanalysis.com/stocks/azo/ratings/)

##### CMG｜Chipotle Mexican Grill

- **事件核查**：11/2促销报道主要重述10/13–11/10家庭餐活动，不作新财报，客流与利润率仍是验证核心。
- **具名评级与缺项**：11/2未核新动作；10/29 Telsey Sarang Vora Buy48→40、JPM John Ivankoe Buy37→36，目标下调不能漏。
- **经营支持／持续风险**：10/28 Q3收入+9.6%至3.3bn、同店+2.1%；交易量+0.8%、客單+1.3%。新店推動主要增長，全年同店仍低單位數，不把正客流說成高增長全面恢復。 风险：營業利潤率15.9→13.7%、餐廳層級24.5→23.3%，GAAP及調整EPS均0.27/-6.9%；食品、人工成本與客流恢復仍是反方。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：刪除等10/28財報的過期提醒；下次官方日期未核。核11月客流、促銷與利潤率回升，及2027新店340–360家美加的投資回報。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000103/cmg-20261028xex991.htm) · [来源2](https://www.foodservice.news/article/chipotle-cmg-launches-oversized-bag-lto-to-drive-family-meal-orders) · [来源3](https://stockanalysis.com/stocks/cmg/history/) · [来源4](https://stockanalysis.com/stocks/cmg/ratings/)

##### HLT｜Hilton Worldwide

- **事件核查**：11/2未核新业绩，10/27 RevPAR和新开店支持经营，但地区需求、回购融资与债务继续。
- **具名评级与缺项**：补旧记录遗漏：10/30 Argus John Staszak Buy400→410；10/28 Mizuho Benjamin Chaiken升Buy329→421；11/2未核新动作。
- **经营支持／持续风险**：10/27 Q3可比RevPAR+5.8%，管理／特許費收入+9.5%；淨單位增長6.0%、管線543100間。GAAP EPS2.37、調整2.45，需求與開房均有實際進展。 风险：管線不是已開業收入；全年資本回報預計3.5bn仍須核回購融資／淨債，不能單靠EPS或淨開房估值。旅遊周期與匯率仍影響RevPAR。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：Q3已發布，刪除10/27待驗提醒；下次Q4官方日期未核。核管理費增長與開房轉換、客房資助成本及每股股東現金。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1585689/000158568926000049/q32026earningsrelease.htm) · [来源2](https://www.reuters.com/business/retail-consumer/hilton-raises-annual-room-revenue-growth-forecast-steady-us-travel-demand-2026-10-27/) · [来源3](https://stockanalysis.com/stocks/hlt/history/) · [来源4](https://stockanalysis.com/stocks/hlt/ratings/)

##### LNG｜Cheniere Energy

- **事件核查**：11/2 08:31 EST拟发行2037年票据，16:40 EST宣布12亿美元已定价，票息5.8%、发行价99.313%，预计11/17交割。不是已完成发行，也不是利润或FCF。
- **具名评级与缺项**：11/2 Citi Spiro M. Dounis维持Buy、330→377。公开转述，未取得原研报。
- **经营支持／持续风险**：10/29 Q3收入6.17bn、調整EBITDA1.90bn、公司DCF1.23bn；全年EBITDA由7.90–8.40升8.75–9.25bn、DCF由5.30–5.80升6.05–6.55bn。Stage3最後一列車8月完成已帶來出口量提升。 风险：公司DCF非扣全部成長capex的標準FCF；9M GAAP利潤與調整盈利分歧受衍生品影響，不能互換。Stage4未核最終批覆；舊事故調查未核結束。
- **本轮现金核查**：拟用于一般公司用途，包括再融资、capex及营运资金；公司DCF继续不等于扣全部成长capex后的股东现金。
- **下一验证**：11/17发行是否交割、再融资用途和全额capex现金桥。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://lngir.cheniere.com/news-events/press-releases/detail/349/cheniere-reports-third-quarter-2026-results-raises-full) · [来源2](https://lngir.cheniere.com/news-events/press-releases/detail/351/cheniere-announces-pricing-of-1-2-billion-of-senior-notes) · [来源3](https://stockanalysis.com/stocks/lng/history/) · [来源4](https://stockanalysis.com/stocks/lng/ratings/)

##### EOG｜EOG Resources

- **事件核查**：11/2未核新公司业绩；13F与财报预览不代替Q3结果，11/6电话会前待正式结果。
- **具名评级与缺项**：11/2未核新动作；10/20 Susquehanna Charles Minervino Buy170→187承接。
- **经营支持／持续风险**：最新已核業績仍8/4 Q2；成本效率與Encino整合提供研究理由。公司已排11/6 Q3電話會，截止前未發布Q3，不能把油價上漲視作公司新指引。 风险：油氣價格、收購基數及服務成本影響FCF；需用正常化油氣價與全額capex衡量，不能年化高油價季度。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：官方確認11/6 10:00 ET Q3電話會；發布的精確時刻本輪未另核。核Encino產量／單位成本、資本預算與淨債。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.eogresources.com/2026-08-04-EOG-Resources-Reports-Second-Quarter-2026-Results) · [来源2](https://stockanalysis.com/stocks/eog/history/) · [来源3](https://stockanalysis.com/stocks/eog/ratings/)

##### XOM｜ExxonMobil

- **事件核查**：11/2可见Q3旧业绩解读和莫桑比克项目二手报道；未核到新的公司财报指引，不据未验证项目消息改现金模型。
- **具名评级与缺项**：11/2 Bernstein Bob Brackett Buy182→193、UBS Manav Gupta Buy199→213、JPM Arun Jayaram Buy186→199、MS Devin McDermott Buy185→187。目标上调与当日下跌并存。
- **经营支持／持续风险**：10/30 Q3 GAAP EPS3.72、調整4.23；CFO25.7bn、公司FCF19.1bn，煉油利用率及高優勢產量改善。公司另宣布2027回購20bn，屬計劃而非已實施回報。 风险：高油價及煉油價差形成順風；公司FCF口徑與普通股owner cash需再調節，不能把季度乘四作永續盈利。PNG／Guyana與新增LNG投資仍需資本。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：Q3已出，刪除等10/30財報提醒；Q4官方日期未核。核正常化油價／裂解價差、Pioneer協同、全額capex及SBC後現金。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.exxonmobil.com/sec-filings/all-sec-filings/content/0002115436-26-000018/livef8k3q26991.htm) · [来源2](https://stockanalysis.com/stocks/xom/history/) · [来源3](https://stockanalysis.com/stocks/xom/ratings/)

##### CVX｜Chevron

- **事件核查**：11/2官方任命Siva Barnwell Adams为corporate secretary/chief governance officer，2027/1/1生效；不是新盈利上修。
- **具名评级与缺项**：11/2 DBS Pei Hwa Ho Buy222→240、Bernstein Bob Brackett Hold209→248、UBS Manav Gupta Buy235→265、MS Devin McDermott Buy226→230、Barclays Betty Jiang Hold208→244。评级仍有分歧。
- **经营支持／持续风险**：10/30 Q3 GAAP盈利9.9bn／EPS5.06、調整EPS5.28；CFO16.0bn，剔營運資金16.6bn。美國產量較兩年前+27%，Hess／Guyana與煉油執行提供增量。 风险：季度Brent均價97美元、煉油價差順風仍強；同比高增長不能全部歸有機改善。法律準備160m及減值110m需分開，CFO也非扣全部capex後股東現金。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：Q3已出；下次官方日期未核。核Hess協同、正常油價下全額capex／SBC後現金、淨債及回購的可持續性。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm) · [来源2](https://chevroncorp.gcs-web.com/news-releases/news-release-details/siva-barnwell-adams-named-corporate-secretary-and-chief) · [来源3](https://stockanalysis.com/stocks/cvx/history/) · [来源4](https://stockanalysis.com/stocks/cvx/ratings/)

##### FANG｜Diamondback Energy

- **事件核查**：11/2盘后已发布Q3，原‘结果待公布’过时。油产量525千桶/日、全年产量指引上调；现金capex全年由约39亿升39.5–40亿美元。GAAP EPS5.69、调整5.86。
- **具名评级与缺项**：公开评级页仍停10/17 JPM Arun Jayaram Buy233→253；新Q3之后的具名动作本窗口未核到，不能当已更新财报后目标。
- **经营支持／持续风险**：11/2盘后已发布Q3，原‘结果待公布’过时。油产量525千桶/日、全年产量指引上调；现金capex全年由约39亿升39.5–40亿美元。GAAP EPS5.69、调整5.86。 Q3 CFO25.99亿−cash capex10.26亿＝15.73亿美元；公司FCF21.48亿剔除了5.75亿营运资金流出。CFO仍为合并口径，须另核Viper非控股现金、SBC及收购付款，不能直接称普通股现金。 风险：油价与收购整合风险仍在；全年cash capex上调至39.5–40亿美元。公司FCF剔营运资金、合并CFO含Viper，普通股现金归属/SBC/收购支付仍须桥接。原“Q3未公布”已由11/2盘后结果替换，不再沿用。
- **本轮现金核查**：Q3 CFO25.99亿−cash capex10.26亿＝15.73亿美元；公司FCF21.48亿剔除了5.75亿营运资金流出。CFO仍为合并口径，须另核Viper非控股现金、SBC及收购付款，不能直接称普通股现金。
- **下一验证**：11/3 09:00 EST（北京22:00）电话会；核营运资金回收、Viper现金归属、油价正常化、全年capex上调和收购付款。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.diamondbackenergy.com/news-releases/news-release-details/diamondback-energy-inc-announces-second-quarter-2026-financial) · [来源2](https://ir.diamondbackenergy.com/node/18161) · [来源3](https://stockanalysis.com/stocks/fang/history/) · [来源4](https://stockanalysis.com/stocks/fang/ratings/)

##### NEE｜NextEra Energy

- **事件核查**：11/2媒体重述3.7GW积压与数据中心潜力，原Q3已披露；不把旧项目当11/2新增生效订单。
- **具名评级与缺项**：11/2未核新动作；10/28 Argus Marie Ferguson Buy102→96、10/23 Barclays Nicholas Campanella Hold84→79承接。
- **经营支持／持续风险**：10/21 Q3調整EPS1.24、同比+9.7%；FPL監管資本同比+9.2%，新增可再生／儲能項目3.7GW。Dominion交易仍待州／聯邦批准，預期2027下半年，不當已合併盈利。 风险：大型交易融資、電價可負擔性與許可風險；非現金／對沖調整及高capex使GAAP與調整盈利不同。Q3超預期不能解除合併風險。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：Q3已於10/21出；下次官方日期未核。持續核Dominion審批、融資、費率承諾、合約項目投產與自由現金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/37634/000075330826000077/neeq32026exhibit99.htm) · [来源2](https://stockanalysis.com/stocks/nee/history/) · [来源3](https://stockanalysis.com/stocks/nee/ratings/)

##### DUK｜Duke Energy

- **事件核查**：11/2官方节能教育及学生参观稿属于一般企业新闻，未形成新增盈利或合同证据。
- **具名评级与缺项**：11/2未核新动作；10/26 RBC Stephen D'Ambrisi Hold127承接。
- **经营支持／持续风险**：最新已核Q2為8/4，調整EPS1.43；人口與負荷增長可擴大費率基礎。10/27天然氣安全教育等一般公司消息不當盈利催化。 风险：Q2法律披露中的Mooresville煤灰集體訴訟風險承接；未核10/22後重大終局。NTE案於2026年3月已和解，不能混為新訴訟。高capex、利率、費率及風災回收另核。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：官方確認11/5 07:00 ET發布Q3、10:00 ET電話會；核費率案、capex融資及煤灰法律責任更新。
- **研究状态**：常規觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/1326160/000132616026000037/er-20260630xearningsreleas.htm) · [来源2](https://news.duke-energy.com/releases/duke-energy-ohio-kentucky-share-tips-for-warding-off-energy-vampires-saving-money) · [来源3](https://stockanalysis.com/stocks/duk/history/) · [来源4](https://stockanalysis.com/stocks/duk/ratings/)

##### AEP｜American Electric Power

- **事件核查**：11/2媒体再述Jacobs输电项目，原公告为10/29，不把370亿美元五年计划当当年利润。
- **具名评级与缺项**：11/2 Barclays Michael Lonegan维持Hold、120→132；升目标不是升评级。
- **经营支持／持续风险**：10/28 Q3 GAAP EPS2.18、經營2.23；FY26經營EPS預期達原6.25–6.55高端或以上。公布100bn五年資本計劃、2027–2031經營盈利年增9–11%。84GW增量負荷至2031僅計已簽ESA或LOA。 风险：84GW不是即期售電；100bn capex仍須融資與監管回收，不能把合約量或費率基礎CAGR當股東FCF。舊SEC2025處分不當新調查。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：Q3已出，刪除Q2沿用的69GW與舊capex錨；下次官方日期未核。核負荷接入時點、保障條款、資金來源與股本攤薄。
- **研究状态**：估值觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://www.sec.gov/Archives/edgar/data/4904/000000490426000069/a3q20268kpressreleaseex991.htm) · [来源2](https://stockanalysis.com/stocks/aep/history/) · [来源3](https://stockanalysis.com/stocks/aep/ratings/)

##### CEG｜Constellation Energy

- **事件核查**：11/2媒体再述10/27 DOE有条件贷款，不是新拨款，未核最终融资文件/提款。
- **具名评级与缺项**：11/2未核新动作；10/30 MS David Arcaro Buy378→391；10/28 CIBC Mark Jarvi Buy358→343与Wells Fargo Shahriar Pourreza Buy362→352承接。
- **经营支持／持续风险**：10/27公司取得最高5bn DOE有條件貸款承諾，支持核電增容；未到放款或最終項目投資決定。承接10/6 Google 20年協議890MW新增核電，首批增容預期2028，非即期2026盈利。 风险：貸款仍需盡調、最終融資文件及條件；不是5bn補助或現金收入。Calpine整合、核電停機、項目capex與對沖／電價風險未解除。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：官方確認11/9 09:00 ET Q3電話會；核DOE最終條件／提款、Google項目投產、Calpine債務及全額capex現金。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investors.constellationenergy.com/node/10291/pdf) · [来源2](https://stockanalysis.com/stocks/ceg/history/) · [来源3](https://stockanalysis.com/stocks/ceg/ratings/)

##### VST｜Vistra

- **事件核查**：11/2媒体再述10/30 Cogentrix交割，风险转为整合与债务，不重复算新交割。
- **具名评级与缺项**：11/2未核新动作；10/30 MS David Arcaro Buy226→224、JPM Jeremy Tonet Buy228承接；收购完成不消除整合风险。
- **经营支持／持续风险**：10/30官方宣布完成Cogentrix收購：10座現代燃氣電廠、約5500MW，所需監管批准已取得；公司總發電能力近50000MW。不能再寫交易待交割。 风险：風險由交割轉為整合、融資及實際盈利轉換；Moss Landing事故善後與法律風險未因收購完成解除。承接10/5 DOE最高4.2bn有條件貸款，亦非已放款。
- **本轮现金核查**：原盈利业务基础承接；本轮未重算完整普通股现金/估值。
- **下一验证**：官方確認11/6 10:00 ET Q3電話會；核Cogentrix併表／債務、全額成長capex、Moss Landing責任與DOE最終條件。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://investor.vistracorp.com/2026-10-30-Vistra-Completes-Acquisition-of-Cogentrix-Energy%2C-Expanding-Diverse-Generation-Fleet) · [来源2](https://investor.vistracorp.com/news?l=100) · [来源3](https://stockanalysis.com/stocks/vst/history/) · [来源4](https://stockanalysis.com/stocks/vst/ratings/)

##### PRDO｜Perdoceo Education

- **事件核查**：重新读取FSA 10/30更新：该次新增明确是自然医学学位范围；大多数RISE条款及Grad PLUS取消、新年度/累计贷款限额仍生效。未核11/2新的公司业绩或政策解除。
- **具名评级与缺项**：StockAnalysis评级页404；定向检索仍未取得11/2新具名动作或可靠最新完整评级，评级资料缺项保留，不把数月前42目标当最新。
- **经营支持／持续风险**：最新正式Q2仍8/6：收入+1.8%、學生總量+0.7%、經營利潤+6.8%。10/30 FSA更新主要是自然醫學N.D./N.M.D.，非當天新增PRDO護理/PT/OT豁免；法院暫令期professional名單仍列PT/OT/SLP等。 风险：同一官方頁明言Grad PLUS取消與新年／總貸款限額等RISE主要部分仍生效，不能因professional暫令當融資風險解除。South收購仍需批准／付款，淨現金不可全數加值。
- **本轮现金核查**：South现金对价及递延/或有付款承接；未把账面现金全额当过剩现金。最新Q3尚待11/5发布，缺招生/融资新验证。
- **下一验证**：11/5盘后Q3、17:00 EST电话会（北京11/6 06:00）；核招生/留存、学生融资、South批准及付款。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-06-29/update-list-professional-degree-programs-due-court-order-updated-oct-30-2026) · [来源2](https://www.businesswire.com/news/home/20261022931505/en/Perdoceo-Education-Corporation-Schedules-Third-Quarter-Earnings-Conference-Call-for-November-5th) · [来源3](https://stockanalysis.com/stocks/prdo/history/) · [来源4](https://stockanalysis.com/stocks/prdo/ratings/)

##### BKNG｜Booking Holdings

- **事件核查**：11/2 09:00 EST官方重申11/3约16:00 EST发布Q3、16:30电话会；北京11/4约05:00/05:30，尚不是已发布业绩。DSA正式调查原文仍可核，未查到解除证据。
- **具名评级与缺项**：11/2未核新动作；10/27 Baird Michael Bellisario Buy230→223、Wells Fargo Ken Gawrelski Hold220→190；10/26 BofA Justin Post Buy234→232承接。
- **经营支持／持续风险**：最新正式財報仍Q2；10/21歐盟已開DSA正式調查，涉及假房源、釣魚及付費排名標示。11/3 Q3尚未公布，不能用股價回彈或高目標視作監管事件解除。 风险：Q2 10-Q已披露FTC人員擬建議對Priceline及合作方採取訴訟；本輪未核最終起訴／和解新文件，不把建議寫成已判違法。營銷效率、中東／航空成本與監管成本另核。
- **本轮现金核查**：监管影响及新Q3股东现金待核；高目标价和本日反弹不解除新增资金冻结。
- **下一验证**：11/3盘后Q3：间夜/预订、营销效率、DSA/FTC合规成本和指引。
- **研究状态**：事件觀察；定向基础筛查，完整估值/同额比较未完成；新增资金资格未升级。
- **来源**：[来源1](https://digital-strategy.ec.europa.eu/en/news/commission-investigate-how-bookingcom-combats-scams-and-fraud-under-digital-services-act) · [来源2](https://www.prnewswire.com/news-releases/booking-holdings-to-make-third-quarter-2026-earnings-press-release-available-on-companys-investor-relations-website-on-november-3-302921908.html) · [来源3](https://stockanalysis.com/stocks/bkng/history/) · [来源4](https://stockanalysis.com/stocks/bkng/ratings/)

### 本轮候选资料变更台账

| 代码 | 更新性质 | 新判断及资格影响 |
|---|---|---|
| VRTX | 资料更新，非成员调整 | 11/2盘后Q3收入34.408亿美元、同比+12%；GAAP净利6.536亿（去年10.829亿），nonGAAP净利约12亿基本持平。全年收入指引升至131.5–132.5亿，同时nonGAAP综合费用升至约60亿（原56.5–57.5亿）；不能只称盈利增长。；新增资格未升级 |
| FANG | 资料更新，非成员调整 | opportunity/source_date/source_url/next_check/risk；新增资格未升级 |
| REGN | 资料更新，非成员调整 | 11/2未核到新一轮公司业绩修订；重读10/30原稿：Dupixent增长及开发余额还清支持利润分成提升。9M CFO36.753亿减capex7.710亿＝公司FCF29.043亿（同比约−8.05%，尚未扣SBC）；总应收75.786亿较年末57.411亿上升。10月Sanofi十亿美元upfront已收到，Q4确认收入，非经常。；新增资格未升级 |
| MSFT | 资料更新，非成员调整 | 11/2官方与Lumen扩展企业AI网络联合销售合作，但未披露能直接量化的合同金额、净利润或现金承诺。新补读10-Q融资租赁本金，扣SBC及该本金后的季度现金代理仍为正。；新增资格未升级 |
| AMZN | 资料更新，非成员调整 | 11/2未核到新的公司季度财报或经营指引；市场评论聚焦AWS增长及AI投资，具名评级有新变化。原Q3现金表再核后，重资本开支及融资需要仍是重点，不以股价上涨解除。；新增资格未升级 |
| DOX | 资料更新，非成员调整 | 11/2未核到FY26Q4新结果；官方索引仍确认11/3 17:00EST电话会，第三方11/10估计与官方冲突，不采用该估计。11/1晚间预告是本次窗口内新增二手材料，只是预期，不能当作FY27指引。；新增资格未升级 |
| G | 资料更新，非成员调整 | 11/2官方新闻目录最新仍10/28行业称号；未核到新季度指引。11/5盘后Q3、17:00EST电话会由官方确认。H1回款和普通股现金弱项仍未被新资料解除。；新增资格未升级 |
| STRL | 资料更新，非成员调整 | 新增11/2Cantor下修；补充循环贷款1.4bn可用缓冲和NCI现金/利润桥，不把合并现金当全部归母现金，也不把现金低误作新增违约警报。；新增资格未升级 |
| HII | 资料更新，非成员调整 | 新增11/2具名维持Hold动作；保留现金回款门槛，未形成替换或卖出充分证据。；新增资格未升级 |
| HUBB | 资料更新，非成员调整 | 补11/2评级；保留真实现金桥、收购杠杆及一次关税退款；未满足新增资金完整审核。；新增资格未升级 |
| ROP | 资料更新，非成员调整 | 补11/2子公司AI会议消息及评级日期冲突；保留Indicor非经常处置款。；新增资格未升级 |
| DOV | 资料更新，非成员调整 | 新增11/2发债已完成事实，补融资成本及用途跟踪；不改买入资格。；新增资格未升级 |
| MRK | 资料更新，非成员调整 | 11/2 06:45 EST公司公告将于11/8–11/11 HIV Glasgow发表口服HIV治疗/预防资料，包括ISL/LEN三期亚组及患者报告结果；这是研发推进，未量化为新收入。；新增资格未升级 |
| ORLY | 资料更新，非成员调整 | risk/opportunity/valuation_status补现金季/累计差异；新增资格未升级 |
| ORCL | 资料更新，非成员调整 | 11/2 SEC初步文件正式提出100亿美元普通股和同步100亿美元高级票据发行；两项交割互不构成前提，文件未证明已经到账。由先前融资上限目标进入具体融资阶段，需审最终定价、稀释和资金使用。；新增资格未升级 |
| GOOGL | 资料更新，非成员调整 | 11/2 SEC提交七系列欧元高级无抵押债初步募集说明书，金额、利率和到期日仍留空；Reuters援引承销行材料称规模60亿欧元，不将媒体规模当作已完成到账。Q3单季FCF负而TTM仍正的原判断不变。；新增资格未升级 |
| IBKR | 资料更新，非成员调整 | 加入10月经营数据，下一验证改为交易收费、保证金/客户现金与利率影响；不因单日跌幅恢复买入资格。；新增资格未升级 |
| AXS | 资料更新，非成员调整 | 更新两条具名目标价；保留底层综合成本率/准备金/法定资本下一验证，不引入同名PTSB噪声。；新增资格未升级 |
| SCHW | 资料更新，非成员调整 | 增加融资/NII反方及姓名冲突，保留旧记录；这属于研究补核，不包装为11/2突发利空。；新增资格未升级 |
| V | 资料更新，非成员调整 | 新增Cantor500但保留日期冲突；不因目标价或涨幅解除事件观察。；新增资格未升级 |
| MA | 资料更新，非成员调整 | 加入目标765及首次日期待核；聚合共识值口径不同，不混算高低均值。；新增资格未升级 |
| BKNG | 资料更新，非成员调整 | other_sources/next_check；冻结不解除；新增资格未升级 |
| PRDO | 资料更新，非成员调整 | 保留原主要风险；other_sources补官方财报日；评级仍待核；新增资格未升级 |

其余77股当前新闻、评级与价格复核状态亦已写入CSV本轮字段；没有把保留旧主来源日期视作缺少本轮阅读，也没有把读取日伪装成新事件日期。完整原始深度仍按上表计数。

### 基金与市场原始补充来源

- [Vanguard9/30事实页](https://workplace.vanguard.com/iippdf/pdfs/FS5487.pdf)
- [Vanguard共同基金定价](https://investor.vanguard.com/investor-resources-education/online-trading/buying-selling-mutual-funds)
- [Apple11/2盘后原始业绩](https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/)
- [PLTR11/2盘后原始材料](https://investors.palantir.com/files/Palantir%20-%20Q3%202026%20Business%20Update.pdf)

AAPL/PLTR盘后材料只用于后续风险和池外观察，不能解释此前已结束的常规时段价格。


## 基金产品与分散配置补核 OP-20261102-05

实际记录时间：2026-11-03T04:22:32.303Z（UTC；北京时间加8小时）。本段在OP-04之后追加，保留此前产品资料未齐时的结论及其时间，不把新证据倒写为早先已知。

本轮补齐产品范围与份额费用的研究证据，使分散化基金方案可以由产品待核进入具体比较。私人可用菜单、账户身份、配置比例、金额及执行记录不公开。

| 通用研究对象 | 功能与已核事实 | 关键限制 |
|---|---|---|
| VINIX | 标普500美国大盘核心，当前所核份额经营费0.035% | 仍含较高大型科技敞口；指数不保证低估或短期上涨 |
| VTIAX | 美国以外发达和新兴市场股票，费用0.09% | 外汇、区域与新兴市场风险；不是美国风险的完全对冲 |
| VBTLX | 广泛美国投资级债券，费用0.04% | 中等久期及信用风险；不能当保本现金或即时支出准备金 |
| VFFVX | 自动再平衡的全球股债替代，费用0.08%；9/30约91.5%股票、8.5%债券 | 随目标日期逐步趋保守，须核实际取款期限；出生年份不独立决定适用性 |

研究判断：以低费率美国宽基、美国以外股票及适量投资级债券构建核心，可降低单一科技行业依赖；是否额外保留科技行业基金，须有主动超配理由及全账户风险预算。选择依据为经营覆盖、分散、费用和维护方式，不根据年初至今赢家切换行业，也不承诺近期比科技基金收益更高。普通/Roth已有美国股票敞口时，还应按全部可见资产重算股票/债券和行业暴露。

本轮独立反方：更少基金的目标日期方案可降低维护负担；保留行业基金可能带来更多上涨参与，但也继续集中。自行组合有再平衡责任；债券仍可能下跌。个人执行方案和通用研究分开，资料确认不等同成交证据。

执行方法研究：现有余额基金转换与未来供款比例是两件事；计划内exchange适用计划确认页显示的时点和NAV，不机械套普通股票的先卖后买/限价规则。尚未取得具体线上确认页的截止与频繁交易条款，不预设立即成交；不进行计划外提款。

- [VINIX 2026官方招募书](https://www.sec.gov/Archives/edgar/data/862084/000086208426000057/f45033d1.htm)
- [VTIAX官方摘要招募书](https://www.sec.gov/Archives/edgar/data/736054/000119312526077508/f44037d1.htm)
- [VBTLX官方摘要招募书](https://www.sec.gov/Archives/edgar/data/794105/000079410526000113/f44825d1.htm)
- [VFFVX 9/30官方事实页](https://workplace.vanguard.com/iippdf/pdfs/FS1487.pdf)
- [Vanguard雇主计划余额转换说明](https://retirementplans.vanguard.com/web/pdf/pdf/WrittenExchangeRequestT38104.pdf)


## 基金转换时点复核 OP-20261102-06

实际记录：2026-11-03T04:36:46.285Z（UTC；北京时间加8小时）。本段解释OP-05分散方案的执行时点，配置目标与证据标准不变；公开版不含私人比例、金额或交易状态。

当前研究建议可以推进以降低单行业集中的基金转换，不把“先反弹到某价”作为必要条件。现有证据未支持转出基金在等待期间必定跑赢目标组合；等待的交换价值应比较两端相对回报，而不是只看转出基金绝对是否上涨。已发生的价格回撤、之后的风险敞口及交易成本分别处理。科技若短期强劲反弹，较分散的组合也可能落后行业基金，这属于明确的取舍，不能承诺转换立刻带来更高收益。

操作采用计划内现有余额转换/重配。历史NAV仅作参考，不锁定为成交价；应按计划确认页列出的卖出/买入生效日、适用NAV、截止及交易限制执行。Vanguard一般说明：截止前受理对应当日NAV、收市后受理通常对应下一交易日NAV；这不是对具体雇主计划截止或两端同日成交的保证。

- [Vanguard共同基金定价说明](https://investor.vanguard.com/investor-resources-education/online-trading/buying-selling-mutual-funds)
- [雇主计划基金转换与现有余额重配说明](https://retirementplans.vanguard.com/web/pdf/pdf/WrittenExchangeRequestT38104.pdf)
