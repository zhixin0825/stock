# 100隻美股機會觀察池

> **当前入口：2026-11-13 盘前复核。** [当晚研究](reviews/2026-11-13_EVENING_OPERATION_PLAN.md)及逐股 CSV 的 `evening_20261113_*` 列；[11/12 正式收盘及盘后复盘](journal/2026-11-12_OPERATION_REASON_LOG.md)及其历史列保留。

> **当前入口：2026-11-12 正式收盘及盘后复盘。** 见[操作理由日志](journal/2026-11-12_OPERATION_REASON_LOG.md)及逐股 CSV 的 `afterclose_20261112_*` 列；[晚间事前方案](reviews/2026-11-12_EVENING_OPERATION_PLAN.md)与此前盘前列保留。

版本：2026年11月3日补做美股11月2日收盘复盘；新闻截止2026-11-02 20:00 EST／北京2026-11-03 09:00；实际编写2026-11-03T09:17:29+08:00。100个唯一代码，原名册基准2026年10月22日。公开池不标示个人持仓，基金另列。

本輪沒有新增完成全部買入資格的股票；這不是宣稱所有企業都不值得投資。現為29隻常規觀察、47隻事件觀察、24隻估值觀察。類型表示研究方向，不是收益排名；新增資金資格和現持操作結論分開，待覆核不能冒充繼續持有建議。

[完整逐股CSV](../data/watchlists/universe_100_20261022.csv)保留機會、風險、驗證點、來源日期和資料缺口。`new_money_action`僅描述新增或加倉推薦資格，取代容易被誤解為全持倉操作的`current_action`。持倉覆核須按[完整流水線](STOCK_SELECTION_PIPELINE.md)與[逐次模板](STOCK_REVIEW_TEMPLATE.md)另作結論。

## 每日維護要求（2026-11-02補充）

每日報告不以有沒有交易為條件：全部已核實持倉及100隻池均須檢查走勢、重要新事件與下一驗證點，基金另列並納入共同風險。詳見[投資研究與操作日誌模板](INVESTMENT_JOURNAL_TEMPLATE.md)的每日研究章節。

區分兩類更新：一是逐股資料更新，包括行情、財報、分析師動作、來源、風險、事件日期、資格及最後核查時間；二是成員調整，須有經營、估值或研究覆蓋理由，移出者保留備選檔，不為追漲、隱去下跌或湊更新次數而換名單。凍結新增資格不等於刪除，舊風險持續承接。

每輪明示100隻中實際完成行情、新聞及深入基本面覆核的數量與缺項；已核實變化須回填本頁和現行CSV相應欄位，不能只寫在摘要裡。維持100個唯一代碼，全部已核實現股不得遺漏；公開資料不標記個人持倉。未核實資料保留原來源日期並標待更新，不以當日日期冒充新研究。

上一轮11月2日晚間已實際完成100隻的歷史行情、定向事件與公開分析師動作回溯篩查，並更新全部100行CSV及本頁；64行主來源日期有變化，其餘保留原主來源日期，沒有把讀取日當發佈日。這不等於100家公司全部完成現金歸一化、完整估值、券商原研報及同額替代盡調。詳見[完整晨報與100隻逐股明細](journal/2026-11-02_MORNING_RESEARCH_BACKFILL.md)。11月2日盤前的另一輪決策見[晚間覆核](reviews/2026-11-02_PREOPEN_FIXED_STANDARD_REVIEW.md)，不可倒寫成早上已發佈。

## 覆蓋與機會成本比較

1. 每輪從私人持倉快照做代碼集合核對，現持個股零遺漏；記錄價格日期、未同步交易與缺項。基金另列，仍納入全帳戶風險。
2. 持有只保證研究覆蓋。每隻現股都要以今天價格說明繼續配置資金的正面理由，與最強合格替代者做同額、同期限比較，計入稅費、下行情景和集中度。
3. 替代方案扣除成本後有穩健淨改善，才提出換出及換入方案。排名落後不自動賣出；未完成比較標為待覆核，不能默認繼續持有。
4. 重大未核清風險凍結新增資金推薦，事件台帳持續承接。已持有不能解除限制，凍結也不機械推出賣出。
5. 不宣稱100隻已完成全部新聞、估值與分析師研究，也不宣稱證明全市場最優。記錄維護方法不等於已設定自動監控。

## 歷史成員修訂（2026-10-22）

為修正研究覆蓋而調整12個名額；這是研究範圍修訂，沒有完成原成員與新增成員的投資優劣排序。原12隻保留於[備選留檔CSV](../data/watchlists/reserve_20261022.csv)：BLK、AJG、SPGI、AME、PH、MTZ、AON、KKR、NDAQ、AMGN、EW、CPRT。六隻原為資料待核，另六隻保留事件追蹤。任何有效風險不因移出基礎池而解除。

## 本輪成員維護（2026-11-02）

本輪100個代碼不變，資料及觀察類型已更新；不是每天都必須換成員。XYL、STRL、ANET新增事件核查，AZO、FANG、CEG、PRDO及LNG、AEP的觀察類型亦按最新事項調整。這些是研究分類，不自動等同賣出或買入。MEDP三案已撤訴但可重提、VST收購已交割、ICE的HSR條件已滿足等實質變化均已回填。

池外初篩新增APH為研究線索；有機增長與訂單有原始經營證據，但稅率、收購資金、SBC及估值尚未完整核對，不直接擠掉現池成員。備選留檔中的PH以11月5日官方財報為下一驗證點。本輪尚未完成池外與現池最弱成員的同尺度比較，不能宣稱名單已最優或沒有值得增補的公司。來源及限制見晨報。

## 研究進度與共同風險

本輪100隻行情均已取得四個收盤日期並重算1/5/20交易日價格回報；100隻均有定向事件、公開評級及日程檢索記錄。主文標明已核、未核到、原文未取得或日程衝突，不將公開評級摘要當作完整券商模型。新增可執行買入為零：尚未新完成全局同額比較，不是用缺資料推論每隻應繼續持有。原始股價庫未作公開批量鏡像，晨報僅列有來源的研究摘錄及自行計算回報；行情不是即時成交指令。

行業不同不代表風險獨立。資料中心與電網資本開支、金融市場資產價格、政府預算及醫療政策等共同因素須合併評估。

## 逐股觀察

### 金融

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [JPM JPMorgan Chase](https://jpmorganchaseco.gcs-web.com/static-files/71d42762-a4d9-435b-9486-b7327e378dca) | 常規觀察 | Q3净利息收入同比增长13%，贷款、支付和资本市场业务可共同提供盈利来源；观察存款与信贷质量能否支持持续回报。 本轮事件：11/2定向新闻检索未核到改变核心盈利指引的新公司公告；新增为券商目标价动作，不能把市场评论当公司盈利上修。 下一步：11/5行业会议及2027-01-14 Q4官方结果；核NII、费用、坏账、资本缓冲，按ROTCE/TBV同尺度估值。 | 信贷与资本市场周期；Q3报告EPS与剔除显著项目后EPS不同，不能把一次性项目正常化错配。 |
| [BAC Bank of America](https://investor.bankofamerica.com/regulatory-and-other-filings/select-sec-filings/content/0000070858-26-000481/bac09302026ex991.htm) | 事件觀察 | 固定利率资产重定价与净利息收入恢复提供经营改善线索，但必须先评估新监管处罚和整改。 本轮事件：11/2未核到监管整改完成或经营指引新上调；10/30员工仲裁诉讼仍为最近新增风险，不能和10/13反洗钱处罚混为同一事件。 下一步：11/5行业会议、2027-01-15 Q4；先核监管整改、持续开支与正常化可分配资本。 | 10/13 FinCEN12亿美元处罚已抵扣OCC7.5亿，另OFAC1160万；2024停止令及回溯/独立审查仍在，持续整改成本和影响未量化。 |
| [GS Goldman Sachs](https://www.sec.gov/Archives/edgar/data/886982/000088698226000529/a3q26gsearningsresults.htm) | 常規觀察 | Q3投行费用同比增长21%，并购与股权融资恢复可提供经营杠杆，资产管理提高经常性收入占比。 本轮事件：11/2定向公司/评级检索未核到新的盈利指引或资本返还公告；强投行季度不能推出积压订单持续加速。 下一步：核投行积压订单和费用可持续性；2027-01-19官方Q4结果，避免年化高交易季度。 | 投行与交易周期波动；公司Q3投行费用积压订单较Q2下降，盈利强不代表后续订单继续加速。 |
| [MS Morgan Stanley](https://www.sec.gov/Archives/edgar/data/895421/000089542126000288/a3q26msearningsrelease.htm) | 常規觀察 | Q3财富管理与机构业务共同带动收入增长，观察客户资产转为收费资产及持续利润率的能力。 本轮事件：11/2新增可核为UBS评级条目；Morgan Stanley策略师对大盘的评论不属于MS本身新盈利指引。 下一步：会议实录及2027-01-14官方Q4；核净新增资产、收费资产转化、财富利润率和资本回报。 | 权益市场下跌会影响资产管理收费和交易活动；高股价不能仅靠单季ROTCE外推。 |
| [IBKR Interactive Brokers Group](https://ndcdyn.interactivebrokers.com/mkt/getFileNew.php?file=2026Q3_Earnings_Release.pdf) | 常規觀察 | Q3客户账户同比增长35%、佣金收入增长12%，全球低成本平台的新增客户有待转为长期利润。 本轮事件：11/2 12:01 ET公布10月月报：DARTs430.6万，同比−4%/环比+5%；客户账户567.8万，同比+34%；客户权益9286亿美元，同比+19%但环比−4%；保证金贷款1068亿美元，同比+31%。账户增长与交易活跃度出现分化，不把规模增长直接当利润增长。 下一步：等下一份官方月度经纪数据，核账户/DARTs/保证金贷款及利息收入；Q4正式财报日未核到。 | 利息收入占比高、保证金贷款增长快；交易量和监管费用转嫁影响收入质量，需检查系统与合规风险。 |
| [AMP Ameriprise Financial](https://www.sec.gov/Archives/edgar/data/820027/000082002726000054/amp-20260930.htm) | 常規觀察 | Q3扣除unlocking后EPS12.07，利润同比+14%；财富流量剔除Comerica后净流入53亿美元。 本轮事件：定向检索及当前新闻页未核到11/2新的公司经营指引；承接10/29 Q3及顾问留存、财富管理有机流量问题。合并CFO或EPS转换率不能替代独立上游可分配资本。 下一步：核迁移后财富净流量、资产管理留存、母公司资本桥及RBC压力；下一正式财报日未核到。 | 财富报告流出受Comerica影响；资产管理仍净流出93.17亿美元；9M净上游资本25亿美元，不可用EPS×90%替代独立可分配资本验证。 |
| [BNY The Bank of New York Mellon](https://www.bny.com/content/dam/bnymellon/documents/pdf/investor-relations/earnings/earnings-press-release-3q-2026.pdf) | 常規觀察 | Q3收费收入同比增长12%，托管规模与平台效率改善可支持经常性盈利增长。 本轮事件：11/2检索及新闻页未核到新的核心经营公告；10/27宣布参加11/5 BMO Financials Conference仍为下一验证，不把旗下封闭式基金分红当上市母公司盈利上调。 下一步：核有机托管收费、NII、资本缓冲及新客户；未来正式财报日未核到。 | 市场水平、利率和客户资产变动影响收费；Q3杠杆及CET1资本比率同比下降，需要检查资本缓冲。 |
| [TROW T. Rowe Price](https://www.sec.gov/Archives/edgar/data/1113169/000111316926000003/earningsreleaseq32026.htm) | 事件觀察 | Q3调整EPS2.86、收入同比+5.9%；ETF/SMA/模型组合扩展有潜力，未见持续净流出拐点。 本轮事件：11/2定向检索未核到新的公司经营指引；Q3资产管理规模增长和主动权益产品净流出并存，不能用资产价格上涨掩盖客户流失。 下一步：下一月AUM与净流量、目标日期基金/ETF及费用；下一正式季度日期未核到。 | Q3净流出283亿美元；调整费用同比+5.8%，不能把市场抬升AUM当作资金流入。 |
| [CB Chubb](https://news.chubb.com/2026-10-20-Chubb-Reports-Third-Quarter-Per-Share-Net-Income-and-Record-Core-Operating-Income-of-7-30-and-7-66,-Respectively,-Up-4-4-and-0-8-Consolidated-Net-Premiums-Written-of-15-1-Billion,-Up-1-9-,-with-P-C-and-Life-Insurance-Up-1-9-and-1-4-P-C-Combined) | 估值觀察 | 承保纪律、投资收入及地域分散支持防守型中线观察，重点是有形账面价值长期复利。 本轮事件：11/2 10:00 ET公司发布J.D. Power小商业保险客户满意度消息：整体第2、数字渠道第1。它支持渠道/服务质量描述，但不提供保费、承保利润或股东现金的量化上修。 下一步：看剔灾当年承保、准备金、费率和法定资本；下一正式财报日未核到。 | Q3承保利润下降、灾损增加；Q3起核心盈利定义排除部分购入无形资产摊销，前期已重述，不能错配同比。 |
| [CME CME Group](https://www.cmegroup.com/media-room/press-releases/2026/10/21/cme_group_inc_reportshighestq3revenueonrecordforq32026.html) | 估值觀察 | 利率、外汇、商品避险需求转为交易与清算收费，Q3收入与净利双位数增长。 本轮事件：11/2定向检索和新闻页未核到10月正式月度ADV报告；9月31.8m/三季度29.4m是10/2旧公告，不能改名为11月最新。10/27巴西雷亚尔合约成交纪录也是旧事件。 下一步：下一月ADV/RPC及数据收入；核永续合约竞争与法院新裁定，未来正式财报日未核到。 | 成交量可能由异常波动拉动而非永久增长；新永续合约竞争与诉讼边界未完整核清，CME是原告而非被调查方。 |
| [ICE Intercontinental Exchange](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-Reports-Third-Quarter-2026/default.aspx) | 事件觀察 | Q3净收入同比+15%、调整EPS+18%；9M CFO45亿美元，交易与数据业务支持增长。 本轮事件：11/2定向检索未核到公司级新盈利指引或MarketAxess交易完成；继续按10/29 Q3及HSR等待期已提前终止、其他审批尚待核的阶段研究。 下一步：核其他审批、2027Q1交割及新增融资；统一调整FCF与股东现金口径。 | HSR已于10/21提前终止，但其他审批仍需取得；9月底债务233亿美元，MarketAxess收购融资及协同需重算。 |
| [V Visa](https://www.sec.gov/Archives/edgar/data/1403161/000140316126000126/q42026earningsrelease.htm) | 事件觀察 | FYQ4净收入同比+13%、调整EPS+17%；支付量+9%、跨境剔除欧洲内+14%。 本轮事件：11/2行业展望/评级转载为主要新检索线索，未核到改变法律责任或公司指引的正式新公告；FY26法律计提与DOJ借记卡诉讼仍须单独审查。 下一步：审FY26 10-K和法院进展，核客户激励现金、FY27增长及估值；下一正式财报日期未核到。 | FY26法律计提17亿美元；DOJ借记卡反垄断风险未核到解除，激励、费率和诉讼现金需继续审。 |
| [MA Mastercard](https://www.sec.gov/Archives/edgar/data/1141391/000114139126000122/ma09302026-exx991xearnings.htm) | 事件觀察 | Q3收入同比+14%、调整EPS+21%，跨境量+11%；支付网络及服务增长持续。 本轮事件：11/2主要为Q3后分析师/行业评论，未核到新的公司财报或解除商户诉讼的正式公告；9M现金及激励预付款问题继续承接。 下一步：审Q3法律附注、激励现金、BVNK/债务及SBC后现金；下一正式财报日未核到。 | 9M CFO118.59亿美元低于去年126.46亿，激励预付款与法律支付增加；商户诉讼及收购债务未清关。 |
| [MCO Moody's](https://www.sec.gov/Archives/edgar/data/1059556/000162828026066594/a3q26earningsrelease.htm) | 估值觀察 | Q3 Analytics有机恒汇率收入增长8%、ARR增长8%，订阅分析业务可部分平滑债券评级周期。 本轮事件：11/2定向检索及新闻索引未核到新的经营指引；最近核心事件仍10/21 Q3，评级发行周期走弱与Analytics经常收入增长并存。 下一步：看Ratings发行与Analytics续约，核SBC后现金和回购融资；下一正式财报日未核到。 | Q3总收入仅增1%、评级交易收入降5%，调整EPS增长仅6%；不能沿用Q2高增长叙事。 |
| [DFIN Donnelley Financial Solutions](https://www.sec.gov/Archives/edgar/data/1669811/000119312526436951/dfin-ex99_1.htm) | 事件觀察 | Q3总收入同比+5.5%，软件+5%、占比51.5%，ActiveDisclosure约+24%；9M现金转换改善。 本轮事件：11/2‘目标72/共识提高’等转载主要回顾10/29财报和10/30 Needham动作，不是11/2新财报。ActiveDisclosure高增长与整体软件仅约5%增长必须同时保留。 下一步：下一季软件续约、有机增长、交易收入与SBC后现金；下次正式财报日期未核到。 | 交易收入仍依赖资本市场周期，整体软件增速仅5%；调整EPS排除SBC，需看扣SBC后现金；Q3印刷已转为同比+9.4%，勿延用Q2下降结论。 |
| [AXS AXIS Capital Holdings](https://www.globenewswire.com/news-release/2026/10/28/3390766/0/en/axis-capital-reports-third-quarter-net-income-available-to-common-shareholders-of-202-million-or-2-75-per-diluted-common-share-and-operating-income-of-229-million-or-3-12-per-dilut.html) | 事件觀察 | Q3剔AOCI每股账面84.33、同比+14.4%，但不能据此忽略承保盈利下降。 本轮事件：11/2新增主要为Q3后券商评估。Q3经营净利同比−10%、剔灾/天气当年综合成本率90.3%对比87.7%的底层承保压力仍在；网上关于爱尔兰顾问Axis Capital考虑PTSB收购属于同名异实体，排除于NYSE:AXS事件。 下一步：核承保基础、准备金三角、费率及法定可分配资本；下一正式财报日未核到。 | Q3经营净利同比−10%，综合成本率94%；剔灾/天气当年综合成本率90.3% vs87.7%，费率软化与竞争并非纯灾损一次性。 |
| [SCHW The Charles Schwab Corporation](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Delivers-Record-Net-New-Assets--Earnings/default.aspx) | 估值觀察 | 客戶資產、淨流入及財富管理規模增長；Q3核心淨新增資產1904億美元，調整EPS1.69美元。 本轮事件：11/2定向新闻检索未核到新的公司盈利预警；较新的风险解释仍来自10/28券商对资金成本、可生息资产扩张及NIM的重新估计，不能把一切归因于大盘。Q3净流入等经营正面仍在。 下一步：月度流量、存款/现金迁移、NIM与AI成本收益；下一正式季度财报日未核到。 | 利率、存款遷移、淨息差、融資與市場活躍度；好財報不自動代表現價比IBKR、AMP等更值得持有。 |
| [BRK.B Berkshire Hathaway Class B](https://www.berkshirehathaway.com/qtrly/2ndqtr26.pdf) | 估值觀察 | 保險浮存金與多元經營現金流、資本配置；Q2營運收益129.83億美元，並回購約45億美元股票。 本轮事件：11/2官方新闻目录未出现Q3正式发布时间；不能以第三方11/7或11/13当公司确认。另本轮补核10/29 Bending Spoons原始公告/SEC：新增3.3亿美元投资已交割，总持股4%，此前6亿美元IPO投资；这是10/14宣布事项的完成，不是11/2新投资。 下一步：等待官方Q3日程/公告；核正常化经营收益、GEICO、资本部署及回购。聚合日期冲突，不采用为确认日。 | Q2保險承保和投資收益同比下降；GEICO理賠頻率與嚴重程度上升。須分離未實現投資收益、匯率及其他項目，不能按表面EPS倍增推論核心盈利倍增。 |

### 醫療

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [JNJ Johnson & Johnson](https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q3-2026-results-raises-2026-guidance/default.aspx) | 事件觀察 | Tremfya等新药增长及骨科业务重组有望改善业务组合，适合观察新产品能否覆盖专利到期压力。 本轮事件：11/2定向检索未核到新的集团业绩修订；补核11/1 Shockwave Javelin冠脉IVL的30日研究结果。属美国研究性器械与单臂试验，不等于新增商业销售或利润。 下一步：司法批准/参与条件及支付日程、MedTech地区增长和创新药替代；下一正式财报日未核到。 本轮下一验证：核器械批准与真实销售转化；滑石粉拟和解的法院程序仍须继续跟踪。 | 10月13日Q3含滑石粉拟解决方案特别费用；拟和解未等于全部诉讼责任消失，海外MedTech增长偏弱。 |
| [MRK Merck & Co.](https://www.merck.com/news/merck-co-inc-rahway-n-j-usa-announces-third-quarter-2026-financial-results-highlights-multiple-milestones-advancing-broad-diverse-pipeline/) | 常規觀察 | Q3销售同比+5%；QLEX销售8.30亿美元、Winrevair6.94亿美元且同比+93%，新品采用获得实际收入支持。 本轮事件：11/2 06:45 EST公司公告将于11/8–11/11 HIV Glasgow发表口服HIV治疗/预防资料，包括ISL/LEN三期亚组及患者报告结果；这是研发推进，未量化为新收入。 下一步：核QLEX/Winrevair现金、管线节点与收购现金/债务；未来正式财报日期未核到。 本轮下一验证：11/8–11/11会议资料及IDVYNSO补充申请2027/4/22目标日期；仍先核Keytruda集中度和并购后股东现金。 | Keytruda专利集中度仍在；FY26调整EPS2.77–2.82含大额收购/许可一次费用，估值需统一剔除费用与收购现金/债务，不能只修EPS。 |
| [ABBV AbbVie](https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm) | 常規觀察 | Q3收入174.04亿美元+10.3%；Skyrizi+22.7%、Rinvoq+23.9%、神经科学+19.4%，真实商业收入继续接替Humira；全年调整EPS指引上调至13.95–13.99。 本轮事件：11/2 09:00 EST Brise更新2024年已签的两项临床前偏头痛授权，潜在总额7.57亿美元加版税；不是11/2新增7.57亿美元收入。另11/2 16:05 SEC接收8-K：董事Jennifer L. Davis因任Align CEO离任，公司称无分歧。 下一步：重建并购后普通股现金、债务和持续EPS；下一财报日期尚未获公司确认，不填估计日期。 本轮下一验证：区分临床前里程碑支出与现有Skyrizi/Rinvoq现金，重建收购后的债务及可持续普通股现金。 | Humira收入仍−31.2%；Apogee已完成并购，资金占用与临床兑现仍须核。GAAP EPS2.37与调整3.82差异大，IPR&D和或有对价不能一概抹去；税率比较也影响盈利增幅。 |
| [GILD Gilead Sciences](https://www.sec.gov/Archives/edgar/data/882095/000088209526000037/exhibit991earningspressrel.htm) | 常規觀察 | Q3产品销售83亿美元+13%，剔除Veklury+16%，HIV+18%；Q3经营现金50亿美元，已有业务仍有盈利和现金基础。 本轮事件：11/2官方索引确认HIV Glasgow数据展示公告，会议为11/8–11/11；未将新摘要当作已实现收入。官方页面正文打开失败，本轮仅核官方检索摘要及公司原稿转述线索。 下一步：核新增HIV预防产品真实收入/支付、并购回报及细胞治疗；下一季官方日期未确认。 本轮下一验证：11/8–11/11核新数据，继续核HIV净价/库存、Biktarvy医保定价与并购现金义务。 | 细胞治疗销售−18%；HIV增长含净价和库存因素。全年GAAP及nonGAAP指引均为亏损，含并购IPR&D约每股9.88；不能直接使用单季2.55调整EPS年化。9个月收购现金113亿、现金证券降至64亿，须重建债务及股东现金。 |
| [REGN Regeneron Pharmaceuticals](https://investor.regeneron.com/news-releases/news-release-details/regeneron-reports-third-quarter-2026-financial-and-operating) | 常規觀察 | Q3收入51.2亿美元+36%、nonGAAP EPS20.07+70%；Dupixent全球销售+35%、Libtayo+51%，偿还Sanofi开发余额后首个完整季度分成改善有真实经营依据。 本轮事件：11/2未核到新一轮公司业绩修订；重读10/30原稿：Dupixent增长及开发余额还清支持利润分成提升。9M CFO36.753亿减capex7.710亿＝公司FCF29.043亿（同比约−8.05%，尚未扣SBC）；总应收75.786亿较年末57.411亿上升。10月Sanofi十亿美元upfront已收到，Q4确认收入，非经常。 下一步：核Sanofi应收款回款、EYLEA合计下滑及后续研发费用；下一季官方财报日未确认。 本轮下一验证：用最新估值与独立股东现金重算；EYLEA+HD全球合计−11%仍需跟踪，不将连续上涨作为加仓依据。 | EYLEA与HD全球合计销售−11%（美国合计−1%，不能混口径）；Sanofi应收款回收和普通股现金需继续核。Q4十亿美元Sanofi upfront不属经常盈利；原审批/竞争事项未以一季增长自动解除。 本轮补核：9M公司FCF低于去年且应收增加，需核Sanofi应收的收款周期、SBC与持续研发开支；不能把October已收的一次upfront与应收回收混为一谈。 |
| [VRTX Vertex Pharmaceuticals](https://investors.vrtx.com/node/35101/pdf) | 常規觀察 | Q3收入34.408亿美元+12%，新产品开始贡献；全年收入升至131.5–132.5亿美元。Crinetics已完成收购，PALSONIFY纳入报表；但nonGAAP净利约12亿美元基本持平，费用增长抵消收入改善。 本轮事件：11/2盘后Q3收入34.408亿美元、同比+12%；GAAP净利6.536亿（去年10.829亿），nonGAAP净利约12亿基本持平。全年收入指引升至131.5–132.5亿，同时nonGAAP综合费用升至约60亿（原56.5–57.5亿）；不能只称盈利增长。 下一步：11/2盘后核Q3非CF实际收入、Crinetics会计/现金支出、可持续利润；11/30 povetacicept审批节点仍需届时官方复核。 本轮下一验证：11/30 povetacicept FDA目标日期；核CF以外收入兑现与费用/债务，财报后评级待更新。 | CF收入集中、新产品付费/渠道兑现和Crinetics约88亿美元扣现金后交易额需核；公司预计并购至2029才增厚nonGAAP经营利润，潜在峰值销售不是当前盈利。 本轮补核：Q3 GAAP净利下降，费用及并购资金占用上升；9/30现金证券98亿美元、公司新借款45亿美元。需读现金流全表、SBC/租赁/整合现金义务，未完成股东现金和现价估值。 |
| [LLY Eli Lilly](https://www.sec.gov/Archives/edgar/data/59478/000005947826000104/q326lillysalesandearningsp.htm) | 估值觀察 | Q3收入243.97亿美元+39%，GAAP EPS7.22+16%、nonGAAP7.48+7%；全年收入指引850–870亿上调至910–920亿美元，已有销量支撑。 本轮事件：11/2定向检索未核到新一轮公司业绩修订，沿用10/29Q3及已记录的收入、IPR&D和费用口径；本轮新增为财报后的具名目标调整。 下一步：核销量、净价、产能投入后股东现金，以及并购后持续EPS；未来官方财报日期未确认。 本轮下一验证：维持销量、净价、产能投入及并购后股东现金复核，不能由目标价上调代替安全边际。 | 销量扩张同时净价压力；Q3含每股4.57的并购IPR&D。全年nonGAAP EPS实际由35.50–36.50降至35–36，经营改善与并购费用须分开；资本开支、药价政策和估值不能忽略。 |
| [NVO Novo Nordisk](https://www.novonordisk-us.com/media/press-releases/awiqli-fda-approval-pediatric-type-2-diabetes.html) | 事件觀察 | 10/23公司公告Awiqli获FDA批准用于10岁以上2型糖尿病儿童；11/4九个月业绩日期由公司确认，电话会07:00–08:00EST。 本轮事件：11/2定向检索未核到新的集团业绩修订；10/28、10/29会议数据预告及11/4业绩节点继续跟踪，不写成11/2已经公布Q3。 下一步：11/4核美国处方/净价、剔除340B与减值后的可比增长、指引与自由现金；批准适应证的商业贡献另跟踪。 本轮下一验证：11/4核九个月结果与指引，剔一次性340B/减值影响，检验美国处方、净价及现金。 | 新适应证批准不等于已兑现销售。原有肥胖药竞争、净价压力、340B基数及减值影响未解除；不能以新产品利好或低表面PE跳过利润修复。 |
| [MDT Medtronic](https://news.medtronic.com/2026-10-22-Medtronic-announces-positive-results-from-real-world-registries-for-the-Sphere-9-TM-catheter-and-PulseSelect-TM-PFA-System-at-APHRS-2026) | 常規觀察 | 10/22公布Sphere-9与PulseSelect真实世界登记结果，支持心脏消融产品商业路径；10/15 MiniMed分拆完成是原台账遗漏的资本结构事项，需按新口径研究。 本轮事件：11/2定向检索未核到新增集团盈利指引；产品/获奖及激励安排线索未获得足够时间与影响验证，不当作新盈利催化。MiniMed分拆后的持续业务口径仍待核。 下一步：先核MiniMed分拆后持续业务盈利/债务和PFA收入利润；第三方给11/17 FY27Q2，但本轮未取得公司确认，日期列待核。 本轮下一验证：先核分拆后的债务、可比季度与股东现金；下次季度业绩日期仍待公司原文确认。 | 登记研究不是新增订单/利润；Sphere-9的VT用途美国尚属研究用途。FY27Q1有额外一周，13.7%有机增长不能直接当等长季度增速；召回、机器人投入和分拆后现金责任仍待核。 |
| [SYK Stryker](https://www.sec.gov/Archives/edgar/data/310764/000031076426000059/sykex991earningsq32026.htm) | 事件觀察 | Q3收入65亿美元+7.7%、有机+7.7%；调整EPS3.52+10.3%、调整经营利润率26.2%，但公司承认低于自身预期。全年有机增长新范围6.5–7%、调整EPS14.80–14.90。 本轮事件：11/2未核到新的公司盈利修订；10/29低于公司预期的新指引仍是经营基准，不能因单日反弹当作业绩修复。律师招揽不是监管认定。 下一步：核增长低于预期的产品/地区、网络恢复成本、GAAP到现金差异和回购资金；下一官方季度日期未核。 本轮下一验证：核产品/地区增长不足、网络事件恢复成本与现金，重算14.80–14.90全年调整EPS对应估值。 | GAAP净利7.53亿美元−12.3%、EPS1.96−11.7%；收购整合、重组、召回/法律等调整仍须审。原3月网络事件仍在财报风险中，未见结案及全部成本证明。 |
| [BSX Boston Scientific](https://news.bostonscientific.com/2026-10-28-Boston-Scientific-announces-results-for-third-quarter-2026) | 事件觀察 | Q3销售51.38亿美元仅+1.5%，GAAP EPS0.40低于去年0.51，调整EPS0.73低于0.75；全年调整EPS新指引3.16–3.18，Q4销售预计−3%至−1%。 本轮事件：11/2未核到新的盈利指引；10/28网络事件、心脏器械需求与2027压力继续有效。新律所调查招揽不等于已经正式立案或认定违规。 下一步：核网络恢复与实际损失、Watchman/FARAPULSE份额、2027收入/盈利低基数及并购资金；下一官方财报日未核。 本轮下一验证：核网络恢复、实际损失、2027增长及现金；11/11会议若有新增经营披露再评估。 | 8月网络事件造成运营压力；Watchman/电生理竞争、增长重置与调整项仍需核。不能以目标价高于股价或股价下跌恢复新增资金资格。 |
| [ISRG Intuitive Surgical](https://isrg.intuitive.com/news-releases/news-release-details/intuitive-announces-third-quarter-earnings-6) | 事件觀察 | 沿用10/20 Q3原始业绩：手术机器人、耗材/服务业务增长；10/21 10Q再次明确4.5亿美元反垄断拟和解需法院初步及最终批准。 本轮事件：11/2定向检索未核到法院初步/最终批准的新证据。10/21 10-Q仍写反垄断拟和解需批准，4.5亿美元和禁令救济风险继续有效；不能写已结案。 下一步：核法院批准及禁令细则、手术量和装机/租赁现金回报；下次官方财报日期未确认。 本轮下一验证：法院批准/禁令细则，手术量及装机/租赁真实现金回报；未完成新估值不新增。 | 4.5亿美元现金和禁令救济对售后经济性的影响未解除；原Q3还含关税退款，不把全部EPS当正常利润。未查到法院批准的新证据，不能宣称已结案。 |
| [DHR Danaher](https://investors.danaher.com/2026-10-21-Danaher-Reports-Third-Quarter-2026-Results?asPDF=) | 事件觀察 | 10/21 Q3收入66亿美元+8.5%，剔除呼吸道核心增长5.5%、整体核心3%；公司FCF16亿美元。全年调整EPS指引8.57–8.62，业务恢复有经营依据。 本轮事件：11/2定向检索未核到Abcam验证争议独立解除的新证据；检索到的持仓申报/旧业绩不当新经营催化。争议是公开指控，未当监管造假认定。 下一步：先核Abcam原始验证资料、独立检查/客户损失，再验证非呼吸道需求和普通股现金；未来财报日期未官方确认。 本轮下一验证：先取得原始验证图及独立核验/客户影响；再审非呼吸道需求及SBC后现金。 | Abcam抗体验证图片仍有具体公开质疑，未取得独立核验/整改解除证明；这是指控及验证门槛，不等于监管已认定造假。Q4整体核心增长约3%，现金仍需扣正常SBC并核并购回报。 |
| [TMO Thermo Fisher Scientific](https://www.sec.gov/Archives/edgar/data/97745/000009774526000173/q32026earnings8kex99_1.htm) | 事件觀察 | 10/21 Q3收入121.4亿美元+9%、有机+6%，GAAP EPS4.64+9%、调整6.68+15%。10/30提交8K说明10/27宣布EVP Michael Shafer于12/31退休，未见改变盈利指引。 本轮事件：11/2定向检索未核到抗体图片争议独立解除的新证据；10/30 10-Q及高增长旧财报不能证明争议已解决。 下一步：先核原始图、独立审查/客户影响，再核股东现金；后续季度公司日期未确认。 本轮下一验证：核原始图、审查结论及客户影响，再统一股东现金与估值；事件观察不解除。 | 公司FAQ否认伪造并称正在审查/标注Western blot图片、可提供部分raw图；未取得足够可复核的独立验证解除。强业绩、评级及价格都不替代该门槛。 |
| [ABT Abbott Laboratories](https://www.sec.gov/Archives/edgar/data/1800/000162828026066601/abt-2026q3xexhibitx991.htm) | 事件觀察 | 10/21 Q3报告销售+14.5%，含Exact Sciences并购后的可比销售+7%；全年可比销售增长约6%，调整EPS缩窄至5.50–5.55。营养业务拟分拆，尚非完成。 本轮事件：11/2 09:00 EST公布Amulet 360 VERITAS一年结果，资料实际11/1 TCT展示；TEE评估完全闭合96.3%。美国仍为研究用途，CE已于8月取得；不可称新增FDA批准或直接当利润。 下一步：核分拆法律责任/融资、器械需求和新指引后股东现金，再估值；未来官方财报日未确认。 本轮下一验证：核器械美国审批及商业化、营养分拆债务/诉讼与现金责任，不能以研究数据解除旧风险。 | 营养诉讼责任、分拆债务及现金分配仍待核；GAAP EPS0.53与调整1.42差异明显。报告销售增长不可直接当有机增长；评级偏多也不解除分拆责任门槛。 |
| [ZTS Zoetis](https://investor.zoetis.com/news/news-details/2026/Zoetis-Announces-Second-Quarter-2026-Results/default.aspx) | 事件觀察 | 截至截止未公布Q3，沿用8/6下调后的经营基准；公司9/24公告确认11/5 08:30ET电话会。不能把临近财报预期当新盈利。 本轮事件：11/2定向检索未核到Q3已发布或利润指引新修订；官方11/5电话会仍是下一验证点。单日反弹不等于美国宠物需求及Librela风险已修复。 下一步：11/5核美国宠物收入、Librela、净价/销量、全年指引及现金；必要时跟FDA安全原文。 本轮下一验证：11/5 08:30 ET电话会：核美国宠物销量/价格、Librela、全年指引和现金。 | 美国宠物就诊/价格敏感、Librela需求与安全线索、全年收入及利润下修仍未解除；价格跌幅和历史毛利率不能证明修复。 |
| [MEDP Medpace Holdings](https://www.sec.gov/Archives/edgar/data/1668397/000166839726000034/medp-20261021exx991.htm) | 事件觀察 | Q3收入7.16亿美元+8.5%，净新增业务8.734亿+10.6%，backlog31.672亿+5.6%；GAAP EPS4.84、CFO2.166亿，实际订单和盈利仍增长。 本轮事件：11/2定向检索未核到新的公司业绩或已验证重提诉讼材料；沿用最新10-Q自愿without prejudice撤诉的事实，不倒退为已经确认仍在诉，也不升级为披露完全无误。 下一步：核后续重提案卷、取消率和net book-to-bill（本季约1.22）口径、现金是否含预收；未来官方财报日期未核。 本轮下一验证：取消率、net book-to-bill、backlog转收入与预收款；继续核重提案卷，不靠现金单季强劲自动解冻。 | 最新10Q明确Durbin证券案10/12、Bushansky与Mary派生案10/20均自愿without prejudice撤诉；可再提、不等于法院认定披露无误。原‘持续诉讼未核清’须修正；取消率、backlog转化及成长放缓仍需核。 |
| [IQV IQVIA Holdings](https://ir.iqvia.com/press-releases/press-release-details/2026/IQVIA-Reports-Third-Quarter-2026-Results/default.aspx) | 事件觀察 | Q3收入44.28亿美元+8%，净新订单32亿+15%、book-to-bill1.2；GAAP EPS2.10，公司FCF6.67亿，并上调全年收入/调整EPS指引。12/1 Investor Day已在官方业绩稿宣布。 本轮事件：11/2定向检索未核到新的集团业绩修订或意大利数据整改获解除原文；近期回购/AI新闻线索不替代数据合法性与backlog验证。 下一步：核意大利数据合法化和客户影响、backlog减记/取消率、真实收入转化及债务/普通股现金；12/1 Investor Day。 本轮下一验证：意大利120日整改、backlog核减/取消与债务，12/1 Investor Day。 | 因复核不活跃试验，backlog核减约21亿美元，剩326亿；公司称不影响历史业绩、当年指引或未来12月转收入，仍须验证。意大利数据违法处理700万欧元罚款和120日整改未获解除；净债务138.18亿美元、3.45倍杠杆，FCF同比7.72亿降至6.67亿。 |
| [CVS CVS Health](https://www.cvshealth.com/news/company-news/aetna-2027-star-ratings-reflect-strong-clinical-quality-and-member-experience.html) | 事件觀察 | 截至截止Q3尚未公布；公司确认11/4 08:00ET电话会。沿用Q2修复与10/8星级资料，2027四星以上计划会员比例逾69%仍需量化收益影响。 本轮事件：11/2定向检索未核到Q3已经发布或原指引新修订；公司10/5原文确认11/4 08:00 ET电话会（北京11/4 21:00）。这是电话会时间，不能当精确财报发布时间。 下一步：11/4核医疗福利比率、2027会员/定价、星级奖金净影响、经营现金及修复指引。 本轮下一验证：11/4核医疗福利比率、2027会员/定价、准备金及经营现金；财报前不因低估值预期新增。 | 医疗利用率、Medicare重定价、PBM盈利模式及未来星级奖金影响未解除；不能把预期EPS或分析师目标当已实现收益。 |

### 工業與服務

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [DOV Dover](https://investors.dovercorporation.com/news-releases/news-release-details/dover-reports-third-quarter-2026-results) | 常規觀察 | Q3收入22.34亿美元+8%、有机+7%；持续经营GAAP EPS2.50+14%、调整2.88+10%。五部门订单均增且超过出货，公司FCF3.833亿，部分积压在2027交付。 本轮事件：11/2公司8-K确认完成8亿欧元、票息4.350%、2030到期债券发行；这是融资进展，不是新增经营利润或现金转换改善。 下一步：跟踪债券所得、旧债回购与融资后利息；复核Q3后普通股现金、2027积压交付与估值。 | 工业需求与客户capex周期仍在；全年GAAP EPS8.93–9.08与调整10.60–10.75不可混用，处置/收购/重组与普通SBC须逐项核。订单增长不是全部已到账现金。 |
| [ROP Roper Technologies](https://investors.ropertech.com/node/19501/html) | 常規觀察 | Q3收入21.72亿美元+8%、有机+7%，调整净利润+5%、调整EPS+15%；全年调整EPS22.35–22.40上调。关键工作流与经常收入有当前经营依据。 本轮事件：11/2 07:55ET子公司PowerPlan发布ELEVATE会议及AI产品路线；尚未披露可量化新增集团收入、利润或现金。Q3有机收入+7%、调整净利+5%和调整每股+15%的区别继续保留。 下一步：核经营现金、SBC、回购与并购现金的桥接及AI续约；不把已收12亿美元Indicor款重计成永续经营现金。 | 调整EPS+15%不可冒充总利润+15%；GAAP含Indicor投资影响，收到12亿美元处置相关款项非可重复经营现金；并购支出、回购及普通SBC需归因。AI替代风险仍需实际续约证据。 |
| [ITW Illinois Tool Works](https://investor.itw.com/news-and-events/news/news-details/2026/ITW-Reports-Third-Quarter-2026-Results/default.aspx) | 常規觀察 | Q3收入42.4亿美元+4.4%、有机+3.8%，经营利润+5.9%、利润率27.8%，GAAP EPS3.00+6.8%；CFO9.53亿、公司FCF8.51亿。全年GAAP EPS指引11.45–11.55上调。 本轮事件：最新列表仍以10/30派息和10/27Q3为主，本轮未核到11/2新增重大经营公告；股价+4.13%不是盈利预测自动提高4.13%。 下一步：核等口径有机增长、分部门价格/成本及股东现金，比较盈利增长与估值；下一官方财报日未核。 | 部分capex业务强而汽车/建筑需求仍有分化；公司100%现金转换按CFO减capex定义，仍需扣普通SBC检验owner cash；保险补偿及回购对每股增长要拆分。原JPM降级日期10/12转述与新表10/9冲突，不能无据定日。 |
| [EMR Emerson](https://www.emerson.com/en/corporate/news/2026/q4-2026-webcast-advisory) | 常規觀察 | 官方確認FY26第四季及全年業績11/4盤前發布；公告目錄截至截止時仍以10/14財報安排為最新公司公告，未查得10/22以後新的盈利指引。Q3有機訂單增7%、有機銷售增6%仍是已公布經營基礎。 本轮事件：11/4盘前FY26Q4/全年结果及08:30ET电话会由10/14公司公告确认，尚未公布新年度结果。 下一步：11/4盘前全年结果、08:30ET电话会（北京21:30）；核订单、FY27指引、现金与收购后杠杆。 | 前版風險（歷史底稿，保留追蹤）：大型收購後槓桿、軟件整合及工業項目延遲；中東風險不能忽略。 本輪更新：收購槓桿、軟件整合和工業項目延遲風險延續；即將發布的全年現金流及2027指引尚未核實，不能以舊Q3推定新年度表現。 |
| [ETN Eaton](https://www.eaton.com/us/en-us/company/news-insights/news-releases/2026/eaton-to-announce-third-quarter-2026-earnings-on-november-3--202.html) | 估值觀察 | 官方確認11/3盤前發布Q3。10/27派息、10/28 A380燃油泵升級為最新官方新聞，並非盈利指引上調；Q2有機收入增14%和電力訂單底稿尚待Q3更新。 本轮事件：11/3盘前Q3、11:00ET电话会已读公司发稿确认。另补核9/24旧公告：拟以企业价值8.10亿欧元购COL Group，目标2027Q1交割、须审批；预测2027销售2.50亿欧元不是已实现利润。 下一步：11/3盘前Q3（北京当晚盘前），11:00ET电话会为北京11/4 00:00；核电力订单、现金、COL融资与Mobility分拆。 | 前版風險（歷史底稿，保留追蹤）：AI與電網資本開支共同因子、擴產和交付壓力；Mobility分拆交易尚有執行風險。 本輪更新：AI/電網資本開支共同因子、交付擴產及Mobility分拆執行風險延續；11/3財報前不能把訂單直接視為普通股自由現金。 |
| [HUBB Hubbell](https://hubbell.gcs-web.com/node/32291) | 估值觀察 | 10/27 Q3收入增25%（有機11%、收購13%），調整EPS5.91增14%；全年調整EPS20.40–20.60。Utility有機增5%，Electrical增22%；成長並非全由收購。 本轮事件：本轮未核到11/2新的公司盈利公告，原Q3有机增长11%、调整EPS5.91的经营基础仍有效。已重读9M现金与NSI融资原文。 下一步：核NSI整合与营运资金回收；659.0−119.8−30.0−31.0=478.2m为9M现金代理，仍需处理NCI、税务与全年季节性。 | 前版風險（歷史底稿，保留追蹤）：調整營業利潤率同比下降50基點；收購、通脹和電力資本開支周期可能抵消高收入增長。 本輪更新：9M CFO659m，扣capex119.8m、SBC30m及31m一次性已收關稅退款後為478.2m，尚未扣少數股東現金權益；NSI收購後長債4.506bn，不能把調整EPS直接等同普通股現金。 |
| [IR Ingersoll Rand](https://www.sec.gov/Archives/edgar/data/1699150/000162828026068260/ir2026q3ex991.htm) | 常規觀察 | 10/29 Q3有機訂單增18%、有機收入增4%；調整EPS1.07，剔除IEEPA退款為1.01、增17%。Q3 CFO648m、公司FCF623m；訂單轉強但含約195m大型長周期項目。 本轮事件：11/2公司发稿确认收购IVEK，约新增4000万美元年收入，价格为协同前2025调整EBITDA低双位数倍数；不是新增已生效4000万美元客户订单，具体买价/股东现金回报尚未完整披露。 下一步：核IVEK实际对价、资本占用和整合；原Q3退款、约1.95亿美元长周期大单及剔退款毛利压力继续带入。 | 前版風險（歷史底稿，保留追蹤）：主要工業板塊有機訂單約持平、調整利潤率下降180基點；總收入增長部分來自收購。 本輪更新：退款令調整利潤看起來更強；IT&S剔退款EBITDA利潤率27.8%、同比降120bp，短中期需求與單筆長單須分開。公司FCF尚非扣SBC、收購及少數權益後普通股現金。 |
| [XYL Xylem](https://www.sec.gov/Archives/edgar/data/1524472/000152447226000146/xyl10272026ex991.htm) | 事件觀察 | 10/27 Q3有機訂單增10%，但有機收入持平；調整EPS1.44增5%。全年有機收入指引2–3%下調至持平、調整EPS5.55–5.70降至5.40–5.45。擬出售Applied Water International/Specialty Flow Control，2027改三分部。 本轮事件：11/1律师招揽调查消息仍在新闻列表，不能等同监管正式立案或法院认定。10/27全年指引下修、项目延迟及出售重组尚未核到解除；+5.26%反弹不恢复新增资格。 下一步：核10-Q正確期間、訂單延遲向收入/回款轉化、出售條款與重組現金成本，再重建普通股現金及估值。 | 前版風險（歷史底稿，保留追蹤）：Q2有機收入僅增1%，全年有機收入指引從2–4%縮至2–3%；不可只報訂單與盈利改善。 本輪更新：項目延遲和客戶審慎支出已傳導至全年收入/EPS下修；FCF margin指引由10.2–11.0%收窄至約10.2%。出售及重組仍是計劃，不應計入已完成收益；現金流表期間標題存在June30字樣，未據此自行標作9M owner cash。 |
| [J Jacobs Solutions](https://www.jacobs.com/newsroom/press-release/jacobs-hold-its-fiscal-fourth-quarter-and-full-year-2026-earnings-conference) | 事件觀察 | 10/26官方確認FY26Q4/全年11/23盤後。MMSD仍是獲選進入談判、待Veolia法律挑戰解決才簽約；10/22行業報道續述暫停定案，不能當作已簽收入。 本轮事件：最新列表仍是10/29 AEP服务、10/28旧金山约10亿美元JV项目及10/26业绩安排，本轮未核到11/2新的集团盈利或现金指引。MMSD合同争议仍须承接。 下一步：11/23盘后FY26Q4/全年、16:30ET电话会；另核MMSD正式签约和诉讼，PA收购后现金。 | 前版風險（歷史底稿，保留追蹤）：Milwaukee客戶明確等Veolia法律挑戰解決才簽約，預計2028年啟動；Qatar舊民事訴訟也需持續帶入，不能以獲選等同生效訂單。 本輪更新：Milwaukee合同未定案、Qatar舊訴訟和PA收購債務風險延續；本輪未取得案件完整最新卷宗，亦無新業績可證實現金改善。 |
| [ACM AECOM](https://aecom.gcs-web.com/news-releases/news-release-details/aecom-announces-planned-dates-fourth-quarter-and-full-year-0) | 事件觀察 | 10/26官方確認FY26Q4/全年11/16盤後、11/17 08:00 ET電話會。截止時未有新季度業績推翻FYQ3項目費用337m、GAAP虧損及CFO下降的原風險。 本轮事件：公司原文确认11/16盘后FY26Q4/全年、11/17 08:00ET电话会；本轮未核到11/2解除大项目费用/现金回收风险的新公告。 下一步：2026-11-16盤後財報、11/17電話會；先查項目費用是否擴大、可追償現金及全年CFO，再重建估值。 | 前版風險（歷史底稿，保留追蹤）：FYQ3確認3.37億美元項目費用、GAAP虧損，經營現金流下降66%；全年指引已更新反映損失和更低NSR增長。 本輪更新：Construction Management項目成本/追償和現金回收仍未解除；backlog增長不能直接抵銷大額費用與營運現金受壓，須承接原事件閘門。 |
| [PWR Quanta Services](https://investors.quantaservices.com/_assets/_01c9c3f1ac58364ad0eaebaeeddaa06e/quantaservices/news/2026-10-29_QUANTA_SERVICES_REPORTS_THIRD_QUARTER_2026_407.pdf) | 估值觀察 | 10/29 Q3收入12.01bn、GAAP EPS4.55/調整6.06；CFO約1.5bn、公司FCF約1.2bn；RPO41.8bn、總backlog63.7bn，全年財務預期上調。 本轮事件：未核到11/2新的集团业绩，10/29Q3大额订单和业绩上修仍是旧依据；继续区分RPO、总积压和当期现金。 下一步：核Q3有機/收購貢獻、RPO轉換、預收/營運資金及收購融資；下次財報日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：大額積壓不等於當期利潤；收購整合、技工產能及數據中心資本開支共振增加風險。 本輪更新：收入增幅仍需拆有機/收購；總backlog不同於RPO或當期現金。人力、交付、收購整合及AI/電網capex共同因子延續；尚未完成扣SBC與少數權益的普通股現金橋。 |
| [STRL Sterling Infrastructure](https://www.strlco.com/news/sterling-reports-record-third-quarter-results-and-raises-full-year-2026-guidance/) | 事件觀察 | 公司新季報頁面日期為10/28。Q3收入1.56bn增127%、GAAP EPS6.92、調整7.58；9M CFO427.1m。已簽backlog4.14bn、combined6.14bn內含未簽2bn；Q3已簽book-to-burn0.9。 本轮事件：11/2新增的是Cantor目标下修而非新季度财报；Q3已于10/28公布。SEC再核generally available现金16.807m、JV现金200.130m，但循环贷款可用约1.4bn并守契约；不能由低母公司现金直接判定违约。 下一步：追踪应收、合同资产和JV归母现金转移；9M扣capex/SBC代理284.841m尚未完成NCI归属，实际NCI分配0.980m与归NCI利润35.362m不可混同。 | 前版風險（歷史底稿，保留追蹤）：Q2收入增90%含2.508億美元收購貢獻；AI建設周期、項目集中和回款風險，需估值壓力測試。 本輪更新：9M CFO扣capex115.458m/SBC26.796m後284.841m仍未扣NCI現金；總現金216.937m中JV200.130m、generally available僅16.807m。營運資金耗用203.734m是9M而非Q3；必須核回款和JV現金可用性。 本轮平衡补核：9/30循环贷款尚可用约1.4bn且守契约，低generally available现金不等于违约；9M已付NCI分配0.980m、归NCI利润35.362m，不可只扣已付金额即称完成股东归属。 |
| [TT Trane Technologies](https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2026/Trane-Technologies-Reports-Strong-Third-Quarter-Results-Raises-Full-Year-Revenue-Guidance-Reaffirms-Full-Year-EPS-Guidance/default.aspx) | 估值觀察 | 10/29 Q3有機訂單增20%、有機收入增16%，backlog12.5bn增73%；調整EPS4.86增25%。9M CFO3.060bn/FCF2.828bn，全年收入預期上調，調整EPS15.20–15.30維持。 本轮事件：本轮未核到11/2新公司经营指引；10/29订单增长和分部利润率压力仍同时有效。 下一步：核各區利潤率、訂單交付和現金正常化，估值不依賴倍數擴張；下季財報日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：Q2調整營業利潤率下降60基點；產能、產品組合及數據中心需求預期可能壓縮安全邊際。 本輪更新：整體調整營業利潤率20.2%、同比降40bp；EMEA/APAC分部利潤率下降較大，供應鏈/通脹與數據中心冷卻共同因子延續。FCF尚需扣SBC後估普通股收益。 |
| [OTIS Otis Worldwide](https://otisinvestors.com/news/news-details/2026/OTIS-REPORTS-THIRD-QUARTER-2026-RESULTS/default.aspx) | 事件觀察 | 10/28 Q3有機銷售增6%，服務增7%、現代化訂單增10%；調整EPS1.05持平。服務margin24.2%環比修復100bp，但同比降130bp；全年EPS4.01–4.05維持。 本轮事件：最新列表仍是10/29派息和10/28Q3；本轮未核到11/2盈利修复新证据。新梯中国收入下滑、成本与现金压力不因+3.46%反弹消失。 下一步：核服務價格能否覆蓋工資、全年現金達標及中國新梯收縮；保留事件觀察，未確認下季日期。 | 前版風險（歷史底稿，保留追蹤）：全年調整EPS指引下調至4.01–4.05美元（此前4.20–4.24）；勞工成本、新梯尤其中國需求承壓。 本輪更新：新梯中國收入降逾20%、整體調整margin16.0%同比降110bp。Q3 CFO337m/調整FCF272m；全年調整FCF由1.50–1.55bn收窄至約1.5bn，成本和現金修復仍未完成。 |
| [WM Waste Management](https://wastemanagement.gcs-web.com/news-releases/news-release-details/wm-announces-third-quarter-2026-earnings) | 常規觀察 | 10/27 Q3收入6.846bn增6.3%、調整EPS2.15；Healthcare收入增3.7%、EBITDA增逾30%。9M CFO4.867bn增12%、公司FCF3.01bn增逾42%；全年FCF預計3.75–3.85bn高端。 本轮事件：本轮未核到11/2新的重大公司经营公告。Q3现金、Healthcare修复及量能偏弱继续承接，公司FCF定义含资产出售，须独立归一化。 下一步：追蹤量能、價格成本差、Healthcare整合及公司FCF口徑；下季日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：收集處置量下降1.8%；低毛利業務退出、燃料成本及醫療業務整合可能影響現金兑现。 本輪更新：Collection/Disposal量仍降0.4%（工作日調整降0.5%），回收商品/能源價格及Stericycle整合風險延續；公司FCF含資產出售收入，普通股現金估值須另核SBC及維持性capex。 |
| [RSG Republic Services](https://investor.republicservices.com/news-releases/news-release-details/republic-services-inc-reports-third-quarter-2026-results) | 常規觀察 | 10/29 Q3收入增8.2%（回收/廢物有機4.8pp、環境解決方案2.1pp、收購1.3pp）；調整EPS1.94增2.1%。9M CFO3.52bn/調整FCF2.28bn，全年收入、EBITDA和調整FCF指引上調。 本轮事件：本轮未核到11/2新公司业绩；10/29全年指引上修是11/2多家改价的旧经营背景，但没有识别其价格因果份额。 下一步：核環境解決方案改善能否持續、量能恢復及全年調整FCF2.565–2.585bn；下季日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：總量拖累收入1.6%、環境解決方案收入下降；併購、環保責任與勞工成本仍需核查。 本輪更新：volume對收入影響仍−0.6%，調整EPS增長落後收入；再生商品價格、收購和環境解決方案風險延續。調整FCF須核剔除項和SBC後再估普通股現金。 |
| [FAST Fastenal](https://investor.fastenal.com/news/news-details/2026/Fastenal-Company-Reports-2026-Third-Quarter-Earnings/default.aspx) | 估值觀察 | 10/14已報Q3，銷售增15.5%、營業margin21.5%，Q3 CFO422m約為淨利105%；10/22以後本輪未核得新重大盈利公告。官方日曆10月銷售於11/5 06:00 CT發布，尚未公布。 本轮事件：本轮未核到11/2新月销售或经营指引；10月销售尚待11/5，不能以股价或旧Q3提前填结果。 下一步：2026-11-05 06:00 CT月銷售；看日均銷售、有機需求/價格及客戶組合。下次季度日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：大客戶組合壓毛利，價格成本仍拖累；關稅退款與供應商返利含時點效應，高增長需要估值補償。 本輪更新：大客戶/產品組合壓低毛利率，需核價格成本、關稅退款/供應商返利及營運資金時點；原Q3現金不能代替尚未發布10月銷售趨勢。 |
| [PEP PepsiCo](https://www.sec.gov/Archives/edgar/data/77476/000007747626000048/pep-20260905.htm) | 观察 | 2026-11-06 纳入消费必需品覆盖。36周 CFO 7,950m，扣 capex 2,182m 及 SBC 240m，指定现金代理 5,528m。 | 北美销量、促销、外汇、负债及再投资；当前不开放新增。 |
| [OSIS OSI Systems](https://investors.osi-systems.com/node/25006) | 事件觀察 | 10/29 FY27Q1收入403.5m增5%、GAAP EPS1.51增28%、調整1.66增17%；book-to-bill1.4、backlog2.1bn；CFO37.088m、capex7.655m。全年收入1.875–1.930bn維持，調整EPS11.13–11.49提高至11.28–11.64。 本轮事件：本轮未核到11/2新的经营公告；最新是10/29 FY27Q1及旧评级。政府验收、交付和回款依赖继续存在。 下一步：看Security交付/服務組合及Healthcare修復，對照backlog回款與全年指引；下季日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：中東衝突已令交付延後，FY2026Q4收入降4%；政府採購、驗收及收款使季度收入和現金流波動。 本輪更新：Security收入組合壓margin、Healthcare偏弱，地緣/中東交付風險未消失；EPS改善須拆利息和回購，CFO-capex29.433m尚非扣SBC後普通股現金。 |
| [HII Huntington Ingalls Industries](https://www.hii.com/news/hii-reports-third-quarter-2026-results) | 事件觀察 | 10/29 Q3收入約3.5bn、EPS5.48；新合同32.4bn，造船收入指引上調，margin/FCF指引維持。10/30人資主管任命非財務指引變更。 本轮事件：本轮未核到11/2新的集团业绩或回款公告。重读10/29Q3与10-Q：强积压/盈利与营运现金后置并存，不因一天−1.00%认定基本面突然恶化。 下一步：跟踪Q4里程碑账单与现金；9M CFO99m、公司FCF−182m，达全年500–600m需Q4约682–782m；合同净资产1.345bn较年初0.538bn上升及EAC盈利须继续拆。 | 前版風險（歷史底稿，保留追蹤）：訂單能否轉化為現金；Q2自由現金流為負1.50億美元，造船人力、交付和成本執行仍需檢查。 本輪更新：EPS含1.52有利累計完工估計調整。9M CFO99m/FCF−182m，淨合同資產538→1345m；FY26 FCF500–600m需Q4大額回款，不能把造船積壓等同現金。 |

### 科技

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [GOOGL Alphabet](https://www.sec.gov/Archives/edgar/data/1652044/000119312526442515/d125079d424b5.htm) | 事件觀察 | 10/28 Q3收入127.577bn增25%，Search增12%、Cloud增103%至30.7bn（含TPU系統銷售）；營業利益40.576bn增30%，普通股淨利26.17bn/GAAP EPS2.12下降，受投資損失影響。 本轮新增：11/2提出七系列欧元债融资；尚未读到已完成交割证据。 本轮事件：11/2 SEC提交七系列欧元高级无抵押债初步募集说明书，金额、利率和到期日仍留空；Reuters援引承销行材料称规模60亿欧元，不将媒体规模当作已完成到账。Q3单季FCF负而TTM仍正的原判断不变。 下一步：核Cloud/TPU可重複性、AI搜尋廣告變現、扣SBC及優先股股息後普通股現金；監察司法救濟執行，下一財報日期未官方核實。 核欧元债最终金额/票息/交割、融资后普通股价值及评级修订顺序。 | 前版風險（歷史底稿，保留追蹤）：美国广告技术补救措施及欧盟监管可能改变数据共享和收费；投资重估与AI资本开支会扭曲表面PE。 本輪更新：Q3 CFO42.290bn−capex51.355bn=FCF−9.065bn；TTM FCF仍+19.747bn，非TTM負現金。Q3普通股發行12.371bn/發債28.996bn及SBC8.630bn提示融資/稀釋；反壟斷救濟與AI搜尋變現風險延續。 |
| [AMZN Amazon](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx) | 事件觀察 | 10/29 Q3收入201.944bn增12%，營業利益28.1bn；AWS約46bn增39.3%、營業利益17.8bn。Prime Day由2025Q3移至2026多數市場Q2，剔時點影響Q3增速約高400bp，不宜只以總收入斷言核心需求轉弱。 本轮事件：11/2未核到新的公司季度财报或经营指引；市场评论聚焦AWS增长及AI投资，具名评级有新变化。原Q3现金表再核后，重资本开支及融资需要仍是重点，不以股价上涨解除。 下一步：核AWS收入轉現金和產能投資回報、租賃本金與SBC；FTС案件及後續指引；下季日期未官方核實。 | 前版風險（歷史底稿，保留追蹤）：TTM自由现金流为负，利润含巨额投资收益；FTC电商垄断诉讼持续，不能用GAAP低PE直接判断便宜。 本輪更新：TTM CFO168.3bn、淨現金capex210.657bn，公司FCF−42.357bn；2026現金capex約220bn，扣SBC後普通股現金更低。FTC反壟斷、AWS競爭/產能及投資收益波動風險延續。 |
| [MSFT Microsoft](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) | 事件觀察 | 10/28 FY27Q1收入92.279bn增19%、營業利益45.915bn增21%；Azure增48%、commercial RPO677bn增73%。GAAP EPS4.92、剔OpenAI投資影響4.89增18%。 本轮事件：11/2官方与Lumen扩展企业AI网络联合销售合作，但未披露能直接量化的合同金额、净利润或现金承诺。新补读10-Q融资租赁本金，扣SBC及该本金后的季度现金代理仍为正。 下一步：核現金capex/租賃、Azure回報與關聯客戶回款；CMA諮詢11/13截止，最終決定時間仍待監察；下季財報日未官方核實。 跟踪Lumen联合销售能否兑现实际收入与现金，不将合作意向直接资本化。 | CFO58.000bn−现金capex39.367bn−SBC3.134bn−融资租赁本金1.000bn=14.499bn，为指定扣项现金代理；旧“尚未扣租赁本金”缺项本轮已补。该季Other investing现金流出12.949bn、未开始租赁承诺364.6bn（部分有条件，并非即期债务）、组件供应商应收与受限投资仍须核；AI投入、OpenAI关联风险和CMA拟议SMS事项延续，未完成owner cash归一化。 |
| [META Meta Platforms](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Pricing-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx) | 事件觀察 | 10/26–27新增融资：25bn美元Class A普通股forward出售、12.5bn美元6.5%强制可转优先股；官方定价页10/27、正文电讯日期10/26。不能把forward全写成现金已到账。 本轮事件：11/2 Reuters转述Bloomberg匿名知情人士称公司考虑至少200亿美元跨境发债；报道明确尚未最终决定。属融资线索而非已交割事实，旧增发/强制可转优先股、AI现金投入及New Mexico判决风险继续。 下一步：核forward实际结算、优先股现金/股份股息、Class C/ATM授权与稀释；法院上诉/现金支付。下一季度正式财报日期本轮未取得公司确认，不填写猜测日。 | 承接10/21 New Mexico25bn判决、AI资本开支和现金流压力。10/30 Reuters报道S&P展望Stable→Negative；完整S&P评级原报告未取得。优先股分配与未来转换会影响普通股股东收益。 11/2媒体另报考虑至少200亿美元跨境债券，未最终决定；仅作待核融资线索，不能当成已发行。 |
| [ORCL Oracle](https://www.sec.gov/Archives/edgar/data/1341439/000119312526442729/d181425d424b5.htm) | 事件觀察 | 10/28 Investor Day重申FY27收入至少90bn、调整EPS8.10；设FY30收入225bn+、调整经营利润率40%+和调整EPS21+目标。 本轮新增：11/2正式提交100亿美元普通股及同步100亿美元票据发行，尚不等于到账。 本轮事件：11/2 SEC初步文件正式提出100亿美元普通股和同步100亿美元高级票据发行；两项交割互不构成前提，文件未证明已经到账。由先前融资上限目标进入具体融资阶段，需审最终定价、稀释和资金使用。 下一步：核FY27–28项目交付、预付款/客户硬件/供应商融资与资本开支匹配；下一财报公司未确认，12/14仅第三方估计。 | FCF转正仍是FY28下半年目标、FY29至少30bn目标，尚未实现；FY27–28资本开支高峰。新增融资目标上限20bn不含再融资，且是在Q1已完成20bn ATM之外。非GAAP剔SBC，须恢复普通股成本。 融资进入具体发行阶段；普通股稀释、最终定价与付息义务须重算，不因Stephens上调评级解除。 |
| [CRM Salesforce](https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Braze/default.aspx) | 事件觀察 | 窗口内未核到新季度财报或Braze交易完成公告；承接10/20已签约以约5.66bn企业价值收购Braze，普通股对价47.50美元现金/股。 本轮事件：11/2定向查询未核到新的季度结果、Braze完成交割或指引改变；当日跌幅是价格事实，不作为AI替代或并购失败的证明。Braze签约及收购后现金缺项继续。 下一步：核Braze融资/审批/交割和每股现金影响；下一财报12/2有第三方估计/确认标记冲突，本轮未得公司日期公告。 | 并购支出、Informatica并表与有机增长、SBC以及AI替代席位收费的旧风险未消除。不要把签约写成交割，亦未完成收购后普通股现金模型。 |
| [ADBE Adobe](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm) | 常規觀察 | 10/22至截止未核到新的财务指引；9/10Q3收入6.76bn、GAAP EPS4.62；AI免费用户付费转化仍须实际季度验证。10/15 NVIDIA协作是窗口前消息。 本轮事件：11/2定向查询未核到新财务指引；可核公司新闻仍为10/22 Alpine合作、10/15 NVIDIA合作等旧事项，不能称11/2新催化。现价附近并未完成无倍数扩张替代比较。 下一步：核新增ARR、付费转化/流失、收购现金与净股数；下一财报12/9仅第三方估计，未取得公司确认。 | AI竞争、免费策略、CEO12/1交接承接；不能用含SBC剔除的调整EPS直接和GAAP比较。9M CFO7.646bn−PPE0.180bn−SBC1.582bn=5.884bn规模锚，未经季节性/并购正常化，非FY27承诺。 |
| [INTU Intuit](https://investors.intuit.com/news-events/press-releases/detail/1329/intuit-expands-intelligence-platform-to-power-the-next-era-of-accounting-firm-and-business-growth) | 常規觀察 | 10/27 Intuit Intelligence横跨QuickBooks、Enterprise Suite、Accountant Suite推出更新，含行业版本、月结和应收工具；部分为beta/即将推出，不能作已兑现利润。10/29确认11/19财报。 本轮事件：11/2官方IR新闻目录仍列10/29财报日程、10/27 Intelligence扩展、10/20 Credit Karma Tax及10/15 Sequence收购。未核到11/2新增指引；股价强势不等于已兑现新产品利润。 下一步：11/19盘后FY27Q1，核GBS真实增长/付费、Mailchimp、Sequence财务贡献及普通股现金。 | 承接Sequence收购、Mailchimp弱势和AI竞争；FY27非GAAP已保留SBC，不应再扣5.81/股。FY27收入+9–10%、GAAP EPS20.12–20.36为公司指引，非已实现。 |
| [ADP Automatic Data Processing](https://www.sec.gov/Archives/edgar/data/8670/000000867026000033/q1fy27exhibit99.htm) | 常規觀察 | 10/28FY27Q1收入5.491bn增长6%（有机固定汇率6%），GAAP EPS2.83增长14%；全年收入增速提高至约6%，GAAP EPS增长12–14%、调整EPS增长10–12%。 本轮事件：11/2定向查询未核到新财务指引；承接10/28FY27Q1经营增长与现金转化差异。官方新闻目录存在加载/检索覆盖限制，不将检索无新增当作无风险证明。 下一步：核新签约、留存、每客户人数、资本化软件和客户资金收益；下一季1/27/2027只是第三方估计，未有公司确认。 | 利润增长与现金增长不同：本季CFO651m对642.3m；扣PPE52.7m、无形资产资本化117.1m、SBC67.2m后约414m，对上年442.8m。客户资金/限制现金不能作普通股自由现金。就业、客户资金利率风险承接。 |
| [PAYX Paychex](https://investor.paychex.com/news-events/press-releases/detail/850/paychex-reports-first-quarter-fiscal-2027-results) | 常規觀察 | 官方财务新闻目录最新10/15股息、9/23Q1结果；窗口内未核到新季度或全年指引变化。承接Q1收入约+6%、PEO/保险增长和Paycor整合观察。 本轮事件：11/2公司IR金融新闻目录最新仍10/15股息与9/23Q1；公司10/26行业奖项属窗口内旧新闻，不是新订单。未核到11/2新经营指引。 下一步：核Paycor整合后有机收入/保留率/每股现金；下一财报公司未确认，第三方12/17、12/18、12/21–23冲突，不指定确切日。 | 中小企业就业、客户流失、整合支出及客户资金利率敏感性继续。10/29评级维持不解决现金流和有机增速问题。 |
| [CSCO Cisco Systems](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75) | 事件觀察 | 10/28官方新增CVE-2026-76418：特定ASA/FTD SSLVPN和secondary authentication配置可被未认证攻击导致重启DoS，官方称10月已主动利用，已有修补。10/27 Node.js跨产品调查亦在进行。 本轮事件：11/2新增检索结果多为机构持仓披露及旧业务综述，未核到足以解除10/28 ASA/FTD漏洞补救风险的新公司公告；持仓披露日期不等于当日买卖。 下一步：核客户损害/修复成本、订单和毛利；下一财报11/12有第三方confirmed与原电话会转述，11/11系另一第三方估计；本轮未取得独立公司日期公告，保留冲突。 | 承接10/14邮件网关漏洞及客户影响；补丁不证明赔付/声誉影响已核清。Node.js公告未确认被恶意用于Cisco产品；不可把所有在调查产品写成已受害。媒体10/30重述ISE76460，原始首发9/16，不作新案件。 |
| [ANET Arista Networks](https://www.arista.com/en/support/advisories-notices/security-advisory/24838-security-advisory-0199) | 事件觀察 | 10/22官方VeloCloud Orchestrator CVE-2026-114625被主动利用；10/23政府通报列入CISA KEV。Hosted版本已修补，Onprem受影响版本须升级；EOS交换机等明确不受影响。 本轮事件：11/2新评级重申但没有新季度结果；11/3美东盘后Q3、16:30电话会由公司确认。VeloCloud漏洞与客户损失未量化的旧风险继续，不扩大为全部交换机受害。 下一步：11/3盘后Q3、16:30EST电话会已由10/6公司公告确认；核订单、毛利、库存和VCO客户影响。 | 承接云客户集中、高预期估值风险；新增VCO补救/客户损失未量化，不能把VCO漏洞扩大成所有交换机受害。 |
| [TXN Texas Instruments](https://investor.ti.com/news-releases/news-release-details/ti-reports-third-quarter-2026-financial-results-and-shareholder) | 常規觀察 | 承接10/21Q3，本轮补读原文：收入6.055bn同比+28%，GAAP EPS2.62；工业、汽车和数据中心广泛增长；Q4收入5.8–6.3bn、EPS2.45–2.79指引。 本轮事件：11/2公司IR目录最新为10/26发行20亿美元投资级票据、10/21Q3结果，未核到新财务指引。旧现金补助及资本开支归一化要求继续。 下一步：核库存/利用率、工业汽车终端需求、SBC及正常资本开支；下一财报1/26/2027为第三方估计，未有公司确认。 | TTM headlineFCF8.422bn含1.104bn CHIPS补助；CFO9.896bn亦含469m投资税抵免减税，不能把补助全部作永续业务现金。仍需扣SBC并检验300mm资本开支周期。 |
| [ADI Analog Devices](https://investor.analog.com/news-releases/news-release-details/analog-devices-report-fourth-quarter-fiscal-year-2026-financial) | 估值觀察 | 10/22公司确认11/24 FY26Q4，07:00EST发布、10:00电话会；窗口内未核到新季度结果/指引。承接数据中心和工业复苏。 本轮事件：11/2官方新闻/日程检索未核到新指引；10/22确认11/24财报，10/21公司拒绝Tutanota mini-tender是旧事项。机构减持文章不证明经营恶化。 下一步：11/24财报核终端订单、毛利、营运资本和收购现金分配。 | 承接补库与真实需求混淆、汽车/出口风险；AI合作新闻不等于新增盈利，Alif收购影响须另审，未由本轮完成并购现金估值。 |
| [QCOM Qualcomm](https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-Schedules-Fourth-Quarter-and-Fiscal-2026-Earnings-Release-and-Conference-Call/default.aspx) | 常規觀察 | 10/22官方确认11/4盘后FY26Q4及全年结果，16:45EST电话会。窗口内未核到新财务指引；不要把2025/10 AI200/AI250发布当2026新催化。 本轮事件：11/2 Bernstein下调目标价并指出手机需求/内存环境及近端预测风险；这是分析师判断，不是公司撤回指引。官方仍定11/4盘后出FY26Q4，16:45EST电话会。 下一步：11/4核手机/Apple收入缺口、汽车/IoT利润和数据中心商业收入/现金投入。 另核11/2 Bernstein近端手机预测下修反方，与公司FY27展望对照。 | 承接Q3手机收入−20%、QCT−5%，汽车/IoT增长尚须抵消；客户自研、中国和许可风险仍在。10/30大跌不独立证明基本面变坏或值得抄底，未以AI新闻摘要替代原始业绩。 |
| [AMAT Applied Materials](https://www.appliedmaterials.com/us/en/newsroom/press-releases/102626-increase-investment-besi-semiconductor.html) | 常規觀察 | 10/26签加速购股协议拟把Besi股权提高至约20%，扩展先进封装/混合键合协作；仍有HSR等待条件，未确认交付完成，官方未披露本次支出金额。 本轮事件：11/2新UBS评级维持；公司新闻目录最新经营资本事项仍10/26 Besi增持协议，11/2报道回顾的是10/30跌幅。未核到Besi交付完成或新财务指引。 下一步：11/12 16:30EST FY26Q4电话会已由10/22官方确认；核Besi资金成本、先进工艺/服务现金和出口许可。 | 旧BIS案2月已解决，不重写成新未决案；中国出口、资本开支周期延续。Besi增持是现金资本配置，不能把预期协同直接记利润。 |
| [LRCX Lam Research](https://newsroom.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026) | 估值觀察 | 承接10/21九月季原文：收入8.219bn环比+22%、GAAP EPS2.19、经营利润率40%；十二月季收入8.6bn±0.4bn、GAAP EPS2.33±0.15。 本轮事件：11/2新Bernstein评级维持；定向查询未核到新的公司季报或指引，10/21强业绩、营运资本流入和出口风险继续。板块下跌不能直接证明设备订单取消。 下一步：核下季供应约束、CSBG增长、客户存储预算及中国收入；下一季公司未确认，第三方1/20与1/27/2027冲突，不写确定日。 | 本季CFO3.498bn−资本开支/无形257.697m−SBC114.696m约3.125bn，含535m营运资本流入不能全季年化。中国占收入35%；出口许可和存储资本开支风险继续。 |
| [KLAC KLA](https://www.sec.gov/Archives/edgar/data/319201/000031920126000032/exhibit991earningsrelease0.htm) | 估值觀察 | 10/28FY27Q1收入4.136bn、GAAP EPS1.18（10拆1后），均超过指引中位；下季收入4.7bn±0.2bn、GAAP EPS1.41±0.11。 本轮事件：11/2查询未核到新的公司结果/指引或具名新评级；承接10/28FY27Q1及10/30 Argus重申，股价下降与行业压力一致但未识别独立因果。 下一步：核检测强度、服务、库存/应收回款、中国许可；下季正式公司日尚未核得，1/27或1/28/2027仅第三方预测。 | 季度CFO1.531bn−PPE194.756m−SBC84.073m约1.252bn；headlineFCF1.336bn未扣SBC。库存433.839m、应收179.196m占款；客户集中、出口风险和拆股口径继续。 |
| [TSM Taiwan Semiconductor Manufacturing](https://investor.tsmc.com/english/quarterly-results/2026/q3) | 事件觀察 | 10/22 Reuters称公司寻求工厂设备稀土替代，属于匿名来源供应链风险线索，尚未确认产量损失；10/15Q3官方资料继续为业绩基准。 本轮事件：11/2定向查询未核到新公司月营收或财务指引；官方日历下一10月营收11/10 13:30台北时间。台海、出口合规与海外成本风险继续，不把匿名旧罚款传闻当新执法。 下一步：官方日历下一经营数据11/10 13:30台北时间10月营收；下一季度财报本轮未核到确定公司日期。核先进节点/封装利用率与海外成本。 | 承接台海集中、海外成本和旧出口合规调查，未取得正式结案依据；不把2025传闻罚款当新罚款。稀土替代不代表已供应中断。 |
| [CDNS Cadence Design Systems](https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Third-Quarter-2026-Financial-Results/default.aspx) | 估值觀察 | 10/26Q3收入1.633bn同比+22%、重复收入+18%、backlog8.2bn；全年收入增长指引提高至约21%。GAAP EPS1.05同比持平，不能只报调整EPS2.11增长。 10/29加入DOE Genesis Mission联盟仅为合作线索，不等于已兑现新增订单。 本轮事件：11/2财经文章回顾10/26已发布Q3与上调全年收入指引，不是再次上调；10/29加入DOE Genesis Mission联盟是新补纳的合作线索，没有可量化新增订单/现金。 下一步：核订单转收入、整合毛利和普通股现金。下一季公司未确认，2/23/2027仅第三方估计。 | GAAP经营利润率26.2%对31.8%，SBC、并购摊销和重组形成差异；9M CFO1.414bn−PPE163.254m−无形6.975m−SBC429.836m约814.371m；并购现金2.143bn须另审。出口/2025和解持续义务承接。 |
| [DOX Amdocs](https://www.sec.gov/Archives/edgar/data/1062579/000119312526355408/6k_q3_26.htm) | 事件觀察 | 窗口内未核到新公司财务指引；公司日历FY26Q4 11/3 17:00EST，日期在10/22旧档已存在。10/8出售Vubiquity的净经常盈利影响仍未量化。11/1晚间财报预告发生在晨报截止之后，不纳入。 本轮事件：11/2未核到FY26Q4新结果；官方索引仍确认11/3 17:00EST电话会，第三方11/10估计与官方冲突，不采用该估计。11/1晚间预告是本次窗口内新增二手材料，只是预期，不能当作FY27指引。 下一步：11/3盘后/17:00EST核FY27剥离后收入、GAAP、持续重组支出与现金。d为处置净EPS影响，与重组R分开。 | 承接收入+2.7%、Q3重组106m和剥离。SEC确认9M GAAP EPS3.33，剔重组影响1.07后4.40；9M普通股现金518.983−78.769−83.692−3.113=353.409m。不能把710–730m排重组FCF指引当实际普通股现金。 本轮另识别37.260m并购递延/或有支付，资本配置现金单列；353.409m桥不等于包括全部收购支付后的余额。 |
| [G Genpact](https://media.genpact.com/2026-08-06-Genpact-Reports-Second-Quarter-2026-Results) | 事件觀察 | 10/28官方NelsonHall F&A Transformation Leader称号是行业认可，不是新增订单/利润。Q2总收入+7.1%、ATS+24.1%承接；未见窗口内新财报。 本轮事件：11/2官方新闻目录最新仍10/28行业称号；未核到新季度指引。11/5盘后Q3、17:00EST电话会由官方确认。H1回款和普通股现金弱项仍未被新资料解除。 下一步：11/5盘后Q3、17:00EST电话会官方确认；核应收/回款、CBS、ATS收费和普通股现金。 | CBS占73%、Q3预期持平至微降；H1 CFO48.908m，扣PPE37.855m/内部无形16.093m/SBC48.632m约−53.672m，含资产处置后仍−49.955m；回款风险未解除。 本轮补扣融资租赁本金3.826m，H1经营现金代理−57.498m；如单列加入资产处置3.717m则−53.781m，不把处置当永续现金。 |

### 消費與能源

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [TJX TJX Companies](https://www.sec.gov/Archives/edgar/data/109198/000010919826000045/tjxq2fy27earningspressrele.htm) | 估值觀察 | 窗口内未核到新季度财报或公司利润指引更新；官方日历预计11/18 FY27Q3。承接Q2同店+4%、调整EPS+11%的业务基础。 本轮事件：11/2可见13F持仓转述并非当日买卖、不是公司盈利新催化。 下一步：11/18 Q3（官方expected、日期可变）核Marmaxx同店、退款剔除后毛利、库存与普通股现金。 | 承接Marmaxx较弱、关税退款抬高GAAP收益；本轮没有依据把退款年化或把分析师Buy当估值已通过。 |
| [ROST Ross Stores](https://investors.rossstores.com/node/23266/pdf) | 估值觀察 | 最新正式業績仍為8/20 Q2：同店+10%、總收入+13%，主要由客流推動。10/26 UBS認為新CEO可透過商品、營運與營銷縮小對TJX的門店生產率差距；這是分析師假說，非新財報。 本轮事件：11/2出现UBS10/26升评的再次报道，事件日期不前移。 下一步：Q3官方日期本輪未確認：資料商11/12與11/19估計不一致，均不當已核日期；等公司正式公告，再驗客流及扣退款利潤率。 | Q2 EPS2.66包含約0.60關稅退款，不能把報告EPS全部視作經常盈利；客流強但下一季與估值尚待驗。 |
| [ULTA Ulta Beauty](https://www.ulta.com/investor/news-events/press-releases/detail/234/ulta-beauty-announces-second-quarter-fiscal-2026-results) | 常規觀察 | 正式最新Q2仍為8/27。門店／線上與Space NK整合支持研究；Q2截止8/1，不能驗證8月結束Target合作後的客流。 本轮事件：11/2行业媒体报道KSECRET进入500多门店，未取得可量化公司盈利影响，作为商品线线索不作上修。 下一步：官方IR日曆確認12/3 Q3電話會；核Target合作結束後的同店、毛利、Space NK及淨現金／借款。 | 促銷、併購與回購融資、Target退出後客流轉移均須留在風險；分析師升目標未證明股東現金改善。 |
| [LOW Lowe's](https://corporate.lowes.com/newsroom/press-releases/lowes-reports-second-quarter-2026-sales-and-earnings-results-08-19-26) | 事件觀察 | 最新正式Q2為8/19；專業客戶與FBM／ADG可拓展分銷，但8月同店／全年指引收窄後仍待新季驗證。 本轮事件：11/2未核到公司新利润指引；房屋装修需求、收购融资风险继续。 下一步：公司日曆列11/18 Q3電話會但明標tentative，故僅暫定；核同店、收購有機分拆、利息與全額capex現金。 | 高房貸利率、大額裝修需求弱；收購後利息與整合支出不能被調整EPS遮蓋。未核得10/22後新的公司盈利指引。 |
| [HD Home Depot](https://www.sec.gov/Archives/edgar/data/354950/000035495026000145/hd_exhibit991x08022026.htm) | 常規觀察 | 最新正式Q2為8/18：收入47.9bn、+5.7%，同店+1.7%。SRS／GMS增加規模，但住宅大項目需求與有機修復仍待Q3。 本轮事件：11/2未核到公司新利润指引；AI/营销或零售专题不是新季度盈利。 下一步：官方日曆確認11/17 09:00 ET Q3業績活動；核大額交易、同店、SRS/GMS現金轉換及淨債。 | 收購收入不能等同有機增長；房貸利率、大額裝修、整合成本與債務仍是實質風險。 |
| [ORLY O'Reilly Automotive](https://www.sec.gov/Archives/edgar/data/898173/000089817326000050/orly-ex99d1.htm) | 估值觀察 | 10/28 Q3同店+7.2%、收入5.12bn/+9%、EPS0.97/+14%；專業業務雙位數增長、DIY中單位數增長。全年同店上調5.5–6.5%，EPS3.25–3.35。 本轮事件：11/2未核到新财报或公司盈利指引；重新核10/28 Q3及现金表：同店+7.2%、净利润+8%、EPS+14%，含3900万美元关税退款。 下一步：核10-Q租赁/退款全额和正常化现金，估值与最强替换对象同额比较；下一官方季报日未核。 | Q3有39m關稅退款；淨利+8%低於EPS+14%，回購放大每股增長。FY26公司FCF1.9–2.2bn、capex1.3–1.4bn，仍須扣持續SBC並核債務，不能只看EPS。 本轮现金补核：Q3 CFO558.743m减capex308.223m=250.520m，较去年304.437m降约17.7%；9M扣capex/SBC简化代理1711.593m仍未归一化退款和营运资金。9M回购3467.904m、新发债2446.149m。 |
| [AZO AutoZone](https://www.sec.gov/Archives/edgar/data/866787/000117184326006805/f8k_102326.htm) | 事件觀察 | 10/26公告CFO Jamere Jackson將11/25離職，已展開外部接任搜尋；過渡期由Controller J. Scott Murphy擔任主要財務主管。公司稱離任與業績或會計分歧無關，不能自行推論財務問題。 本轮事件：CFO11/25离任仍待接续，未核11/2新增会计/业绩分歧；不能自行当财务造假。 下一步：11/25財務主管交接、接任公告；下一次FY27Q1官方業績日期本輪未核，不把資料商12月估計當確認。 | 承接Q4國內同店僅+1.6%、商業客戶銷售+8.6%；需核配送投資、槓桿回購與管理層交接，未把CFO離職當盈利下修。 |
| [CMG Chipotle Mexican Grill](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000103/cmg-20261028xex991.htm) | 事件觀察 | 10/28 Q3收入+9.6%至3.3bn、同店+2.1%；交易量+0.8%、客單+1.3%。新店推動主要增長，全年同店仍低單位數，不把正客流說成高增長全面恢復。 本轮事件：11/2促销报道主要重述10/13–11/10家庭餐活动，不作新财报，客流与利润率仍是验证核心。 下一步：刪除等10/28財報的過期提醒；下次官方日期未核。核11月客流、促銷與利潤率回升，及2027新店340–360家美加的投資回報。 | 營業利潤率15.9→13.7%、餐廳層級24.5→23.3%，GAAP及調整EPS均0.27/-6.9%；食品、人工成本與客流恢復仍是反方。 |
| [HLT Hilton Worldwide](https://www.sec.gov/Archives/edgar/data/1585689/000158568926000049/q32026earningsrelease.htm) | 估值觀察 | 10/27 Q3可比RevPAR+5.8%，管理／特許費收入+9.5%；淨單位增長6.0%、管線543100間。GAAP EPS2.37、調整2.45，需求與開房均有實際進展。 本轮事件：11/2未核新业绩，10/27 RevPAR和新开店支持经营，但地区需求、回购融资与债务继续。 下一步：Q3已發布，刪除10/27待驗提醒；下次Q4官方日期未核。核管理費增長與開房轉換、客房資助成本及每股股東現金。 | 管線不是已開業收入；全年資本回報預計3.5bn仍須核回購融資／淨債，不能單靠EPS或淨開房估值。旅遊周期與匯率仍影響RevPAR。 |
| [LNG Cheniere Energy](https://lngir.cheniere.com/news-events/press-releases/detail/349/cheniere-reports-third-quarter-2026-results-raises-full) | 估值觀察 | 10/29 Q3收入6.17bn、調整EBITDA1.90bn、公司DCF1.23bn；全年EBITDA由7.90–8.40升8.75–9.25bn、DCF由5.30–5.80升6.05–6.55bn。Stage3最後一列車8月完成已帶來出口量提升。 本轮事件：11/2 08:31 EST拟发行2037年票据，16:40 EST宣布12亿美元已定价，票息5.8%、发行价99.313%，预计11/17交割。不是已完成发行，也不是利润或FCF。 下一步：11/17发行是否交割、再融资用途和全额capex现金桥。 | 公司DCF非扣全部成長capex的標準FCF；9M GAAP利潤與調整盈利分歧受衍生品影響，不能互換。Stage4未核最終批覆；舊事故調查未核結束。 |
| [EOG EOG Resources](https://investors.eogresources.com/2026-08-04-EOG-Resources-Reports-Second-Quarter-2026-Results) | 估值觀察 | 最新已核業績仍8/4 Q2；成本效率與Encino整合提供研究理由。公司已排11/6 Q3電話會，截止前未發布Q3，不能把油價上漲視作公司新指引。 本轮事件：11/2未核新公司业绩；13F与财报预览不代替Q3结果，11/6电话会前待正式结果。 下一步：官方確認11/6 10:00 ET Q3電話會；發布的精確時刻本輪未另核。核Encino產量／單位成本、資本預算與淨債。 | 油氣價格、收購基數及服務成本影響FCF；需用正常化油氣價與全額capex衡量，不能年化高油價季度。 |
| [XOM ExxonMobil](https://investor.exxonmobil.com/sec-filings/all-sec-filings/content/0002115436-26-000018/livef8k3q26991.htm) | 估值觀察 | 10/30 Q3 GAAP EPS3.72、調整4.23；CFO25.7bn、公司FCF19.1bn，煉油利用率及高優勢產量改善。公司另宣布2027回購20bn，屬計劃而非已實施回報。 本轮事件：11/2可见Q3旧业绩解读和莫桑比克项目二手报道；未核到新的公司财报指引，不据未验证项目消息改现金模型。 下一步：Q3已出，刪除等10/30財報提醒；Q4官方日期未核。核正常化油價／裂解價差、Pioneer協同、全額capex及SBC後現金。 | 高油價及煉油價差形成順風；公司FCF口徑與普通股owner cash需再調節，不能把季度乘四作永續盈利。PNG／Guyana與新增LNG投資仍需資本。 |
| [CVX Chevron](https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm) | 估值觀察 | 10/30 Q3 GAAP盈利9.9bn／EPS5.06、調整EPS5.28；CFO16.0bn，剔營運資金16.6bn。美國產量較兩年前+27%，Hess／Guyana與煉油執行提供增量。 本轮事件：11/2官方任命Siva Barnwell Adams为corporate secretary/chief governance officer，2027/1/1生效；不是新盈利上修。 下一步：Q3已出；下次官方日期未核。核Hess協同、正常油價下全額capex／SBC後現金、淨債及回購的可持續性。 | 季度Brent均價97美元、煉油價差順風仍強；同比高增長不能全部歸有機改善。法律準備160m及減值110m需分開，CFO也非扣全部capex後股東現金。 |
| [FANG Diamondback Energy](https://ir.diamondbackenergy.com/node/18161) | 事件觀察 | 11/2盘后已发布Q3，原‘结果待公布’过时。油产量525千桶/日、全年产量指引上调；现金capex全年由约39亿升39.5–40亿美元。GAAP EPS5.69、调整5.86。 Q3 CFO25.99亿−cash capex10.26亿＝15.73亿美元；公司FCF21.48亿剔除了5.75亿营运资金流出。CFO仍为合并口径，须另核Viper非控股现金、SBC及收购付款，不能直接称普通股现金。 本轮事件：11/2盘后已发布Q3，原‘结果待公布’过时。油产量525千桶/日、全年产量指引上调；现金capex全年由约39亿升39.5–40亿美元。GAAP EPS5.69、调整5.86。 下一步：11/3 09:00 EST（北京22:00）电话会；核营运资金回收、Viper现金归属、油价正常化、全年capex上调和收购付款。 | 油价与收购整合风险仍在；全年cash capex上调至39.5–40亿美元。公司FCF剔营运资金、合并CFO含Viper，普通股现金归属/SBC/收购支付仍须桥接。原“Q3未公布”已由11/2盘后结果替换，不再沿用。 |
| [NEE NextEra Energy](https://www.sec.gov/Archives/edgar/data/37634/000075330826000077/neeq32026exhibit99.htm) | 事件觀察 | 10/21 Q3調整EPS1.24、同比+9.7%；FPL監管資本同比+9.2%，新增可再生／儲能項目3.7GW。Dominion交易仍待州／聯邦批准，預期2027下半年，不當已合併盈利。 本轮事件：11/2媒体重述3.7GW积压与数据中心潜力，原Q3已披露；不把旧项目当11/2新增生效订单。 下一步：Q3已於10/21出；下次官方日期未核。持續核Dominion審批、融資、費率承諾、合約項目投產與自由現金。 | 大型交易融資、電價可負擔性與許可風險；非現金／對沖調整及高capex使GAAP與調整盈利不同。Q3超預期不能解除合併風險。 |
| [DUK Duke Energy](https://www.sec.gov/Archives/edgar/data/1326160/000132616026000037/er-20260630xearningsreleas.htm) | 常規觀察 | 最新已核Q2為8/4，調整EPS1.43；人口與負荷增長可擴大費率基礎。10/27天然氣安全教育等一般公司消息不當盈利催化。 本轮事件：11/2官方节能教育及学生参观稿属于一般企业新闻，未形成新增盈利或合同证据。 下一步：官方確認11/5 07:00 ET發布Q3、10:00 ET電話會；核費率案、capex融資及煤灰法律責任更新。 | Q2法律披露中的Mooresville煤灰集體訴訟風險承接；未核10/22後重大終局。NTE案於2026年3月已和解，不能混為新訴訟。高capex、利率、費率及風災回收另核。 |
| [AEP American Electric Power](https://www.sec.gov/Archives/edgar/data/4904/000000490426000069/a3q20268kpressreleaseex991.htm) | 估值觀察 | 10/28 Q3 GAAP EPS2.18、經營2.23；FY26經營EPS預期達原6.25–6.55高端或以上。公布100bn五年資本計劃、2027–2031經營盈利年增9–11%。84GW增量負荷至2031僅計已簽ESA或LOA。 本轮事件：11/2媒体再述Jacobs输电项目，原公告为10/29，不把370亿美元五年计划当当年利润。 下一步：Q3已出，刪除Q2沿用的69GW與舊capex錨；下次官方日期未核。核負荷接入時點、保障條款、資金來源與股本攤薄。 | 84GW不是即期售電；100bn capex仍須融資與監管回收，不能把合約量或費率基礎CAGR當股東FCF。舊SEC2025處分不當新調查。 |
| [CEG Constellation Energy](https://investors.constellationenergy.com/node/10291/pdf) | 事件觀察 | 10/27公司取得最高5bn DOE有條件貸款承諾，支持核電增容；未到放款或最終項目投資決定。承接10/6 Google 20年協議890MW新增核電，首批增容預期2028，非即期2026盈利。 本轮事件：11/2媒体再述10/27 DOE有条件贷款，不是新拨款，未核最终融资文件/提款。 下一步：官方確認11/9 09:00 ET Q3電話會；核DOE最終條件／提款、Google項目投產、Calpine債務及全額capex現金。 | 貸款仍需盡調、最終融資文件及條件；不是5bn補助或現金收入。Calpine整合、核電停機、項目capex與對沖／電價風險未解除。 |
| [VST Vistra](https://investor.vistracorp.com/2026-10-30-Vistra-Completes-Acquisition-of-Cogentrix-Energy%2C-Expanding-Diverse-Generation-Fleet) | 事件觀察 | 10/30官方宣布完成Cogentrix收購：10座現代燃氣電廠、約5500MW，所需監管批准已取得；公司總發電能力近50000MW。不能再寫交易待交割。 本轮事件：11/2媒体再述10/30 Cogentrix交割，风险转为整合与债务，不重复算新交割。 下一步：官方確認11/6 10:00 ET Q3電話會；核Cogentrix併表／債務、全額成長capex、Moss Landing責任與DOE最終條件。 | 風險由交割轉為整合、融資及實際盈利轉換；Moss Landing事故善後與法律風險未因收購完成解除。承接10/5 DOE最高4.2bn有條件貸款，亦非已放款。 |
| [PRDO Perdoceo Education](https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-06-29/update-list-professional-degree-programs-due-court-order-updated-oct-30-2026) | 事件觀察 | 最新正式Q2仍8/6：收入+1.8%、學生總量+0.7%、經營利潤+6.8%。10/30 FSA更新主要是自然醫學N.D./N.M.D.，非當天新增PRDO護理/PT/OT豁免；法院暫令期professional名單仍列PT/OT/SLP等。 本轮事件：重新读取FSA 10/30更新：该次新增明确是自然医学学位范围；大多数RISE条款及Grad PLUS取消、新年度/累计贷款限额仍生效。未核11/2新的公司业绩或政策解除。 下一步：11/5盘后Q3、17:00 EST电话会（北京11/6 06:00）；核招生/留存、学生融资、South批准及付款。 | 同一官方頁明言Grad PLUS取消與新年／總貸款限額等RISE主要部分仍生效，不能因professional暫令當融資風險解除。South收購仍需批准／付款，淨現金不可全數加值。 |
| [BKNG Booking Holdings](https://digital-strategy.ec.europa.eu/en/news/commission-investigate-how-bookingcom-combats-scams-and-fraud-under-digital-services-act) | 事件觀察 | 最新正式財報仍Q2；10/21歐盟已開DSA正式調查，涉及假房源、釣魚及付費排名標示。11/3 Q3尚未公布，不能用股價回彈或高目標視作監管事件解除。 本轮事件：11/2 09:00 EST官方重申11/3约16:00 EST发布Q3、16:30电话会；北京11/4约05:00/05:30，尚不是已发布业绩。DSA正式调查原文仍可核，未查到解除证据。 下一步：11/3盘后Q3：间夜/预订、营销效率、DSA/FTC合规成本和指引。 | Q2 10-Q已披露FTC人員擬建議對Priceline及合作方採取訴訟；本輪未核最終起訴／和解新文件，不把建議寫成已判違法。營銷效率、中東／航空成本與監管成本另核。 |

## 延續的重大事件

BKNG已在本池，2026年10月21日歐盟正式DSA程序仍凍結新增或加倉推薦，未因納入而解除。現持處置須獨立覆核。[事件復盤](STOCK_SELECTION_PIPELINE.md)。原池TMO、DHR、IQV等事件及備選NDAQ的舊歐盟調查、CPRT的DOJ調查均繼續承接，沒有新證據不得視作已結案。


## 本轮收盘维护（2026-11-03补做美国11月2日）

实际编写2026-11-03T09:17:29+08:00；新闻截止2026-11-02 20:00 EST／北京2026-11-03 09:00。行情100/100、定向新闻基础筛查100/100、公开评级材料99/100（PRDO最新可靠评级未取得，检索已尝试）；14只重点原始经营/现金补核，完整估值及同额替换比较0/100。价格、新闻、现金深化分别计数，不将读页等同完整尽调。

本轮成员不调整，仍100个唯一代码。已更新100行当前走势/事件/评级及复核状态；VRTX、FANG新季报替换旧“待公布”，MSFT租赁扣项、REGN已收一次付款、STRL循环额度、ORLY季度现金反方及跨来源冲突均保留。池外检查延续APH与留档PH，并新增核AAPL/PLTR盘后原始业绩；未完成与现池较弱成员的同尺度估值，暂不因高增长或单日涨跌换名额。

[本轮完整100股收盘日志](journal/2026-11-02_OPERATION_REASON_LOG.md#收盘后补做复盘-op-20261102-04)含逐项来源、已核新资料及未完成项。旧晨报补录继续保留，不把它重标为本轮收盘成果。


## 晚间增量维护 EV-20261103-01（2026-11-03 20:01北京）

对应美国11/3盘前。本段追加，保留晨间原判断及来源日期。新字段以CSV的evening_*列区分，不把旧资料改日期当新研究。全池昨收重新读取100/100（与11/2锚一致）、盘前快照96/100（G、DFIN、R、OSIS未取得）、聚合新闻/公开评级索引基础阅读100/100。新增或补录实质资料核实5/100，完整现金归一化/估值/指定替换深度比较本轮新完成0/100；全部代码该深度仍未完成，状态逐行保留。聚合标题不等于已核公司事实，精确报价延迟、价差与完整券商原研报未核。

[完整晚间方案、覆盖表及变更台账](reviews/2026-11-03_EVENING_OPERATION_PLAN.md)；[现行逐股CSV](../data/watchlists/universe_100_20261022.csv)。本轮零新增可执行买入，旧配对不自动恢复；这不证明现股全部合格。

|代码|本轮已核资料更新|资格及下一验证|
|---|---|---|
|ORCL|新增原始公告：11/2 22:09 EST已定价约8621万股、每股116美元及100亿美元票据；票息7%–8.65%，预期11/4交割，尚非已到账。相对晨间20:00EST截止新增定价事实；稀释、利息与capex现金回报须重算。 [来源](https://www.prnewswire.com/news-releases/oracle-announces-pricing-of-20-billion-of-common-stock-and-senior-notes-302927244.html)|未升级新增资格；核FY27–28项目交付、预付款/客户硬件/供应商融资与资本开支匹配；下一财报公司未确认，12/14仅第三方估计。 本轮追加：11/4核两项融资分别是否交割、实际净额、稀释、利息及AI资本开支现金回报。|
|HII|11/3公司与Thales公布无人水雷对抗全流程演示；技术进展不是披露新增量化合同、利润或回款，Q4现金兑现门槛不变。 [来源](https://www.hii.com/news/hii-and-thales-successfully-demonstrate-expeditionary-pathmasters-ability-to-deliver-an-end-to-end-autonomous-mine-countermeasure-mission)|未升级新增资格；跟踪Q4里程碑账单与现金；9M CFO99m、公司FCF−182m，达全年500–600m需Q4约682–782m；合同净资产1.345bn较年初0.538bn上升及EAC盈利须继续拆。|
|REGN|补录11/2 16:05 ET公司投资者会议安排：11/17 09:00 ET Jefferies，12/1及12/2另有会议；该公告在晨间截止前已可得但未写入原next_check，属于遗漏补录而非新的盈利上修。 [来源](https://www.globenewswire.com/news-release/2026/11/02/3393740/0/en/regeneron-announces-investor-conference-presentations.html)|未升级新增资格；核Sanofi应收款回款、EYLEA合计下滑及后续研发费用；下一季官方财报日未确认。 本轮下一验证：用最新估值与独立股东现金重算；EYLEA+HD全球合计−11%仍需跟踪，不将连续上涨作为加仓依据。 本轮补录：11/17 09:00 ET Jefferies，12/1 13:45 ET及12/2 09:40 ET投资者会议。|
|MRK|11/3公开转述DZ Bank Elmar Kraus将Buy降至Hold，目标153；公司盈利未因此被改写。原研报及动作精确发布时间未取得；不同平台Cantor评级/目标存在冲突，保留原记录不混算。 [来源](https://www.tipranks.com/news/the-fly/merck-downgraded-to-hold-from-buy-at-dz-bank-thefly-news)|未升级新增资格；核QLEX/Winrevair现金、管线节点与收购现金/债务；未来正式财报日期未核到。 本轮下一验证：11/8–11/11会议资料及IDVYNSO补充申请2027/4/22目标日期；仍先核Keytruda集中度和并购后股东现金。|
|DOV|补读10/30原始债券回购安排：上限由2.3亿升3亿美元，截止11/5 17:00纽约、预计11/9结算；这是旧事实补录，融资与债务回购不当新增经营利润。 [来源](https://www.globenewswire.com/news-release/2026/10/30/3392597/0/en/dover-announces-upsize-of-its-tender-cap-and-extension-of-expiration-date-of-previously-announced-offer-to-purchase-for-cash-certain-of-its-outstanding-debt-securities.html)|未升级新增资格；跟踪债券所得、旧债回购与融资后利息；复核Q3后普通股现金、2027积压交付与估值。 补录10/30原公告：11/5 17:00纽约回购截止、预计11/9结算。|

研究Top5顺序维持HUBB、ROP、DOV、MRK、ORLY，均非今晚买单；HUBB/ROP盘前更高没有增加安全边际，MRK新增降级纳入反方。ETN索引出现新业绩线索，但本轮未完成原始结果/现金表核实，不能以标题数字升级资格。完整旧事件/风险不因本轮索引没有新条目而解除。

本轮没有实际调整成员，仍100个唯一代码并覆盖私人已核个股集合，基金另列且不公开私人标记。已检查备选PH和池外APH/AAPL/PLTR新闻索引，但未完成与拟移出对象的同尺度估值，尚不足以判断是否应调整成员。原备选档及旧风险继续保留，不宣称名单已经最优。公开仅派生盘前变化/时间及研究摘录，不批量镜像盘前原始报价。


## 盘前新候选发现要求（2026-11-03新增）

按[选股流水线的盘前主动搜寻新候选章节](STOCK_SELECTION_PIPELINE.md)执行。每日先主动搜寻现行100只及备选名单以外的新线索，同时推进前日有价值对象的原始经营、独立现金/资本和估值缺口；现池例行更新不能替代新候选发现。跨行业轮换覆盖，不把旧Top5或重复几个池外名字改日期当新发现。

晚间既定20点流程前段执行，目标21点前交付主要结论，不等提醒或拖到22点。每日脱敏研究台账须列首次发现、旧线索实质推进、淘汰及理由，保留首次发现日、来源/事件时间、盈利与现金证据状态、估值缺项、最强反方和下一验证。认真初筛数量与搜索命中数分开；研究Top5与可买名单分开。零交易/零推荐仍须搜寻并报告完成深度，不能将比较未完当作没有更好对象。

候选资料维护不自动改成员；有充分证据才替换，保留移出档及有效风险，保持100个唯一代码并覆盖私人已核个股，基金另列。公开不标记个人持仓。本次仅新增流程要求，没有新增候选事实、买入资格或成员调整，不把规则更新算作已完成候选搜寻。


## 池外新候选实际搜寻 DISC-20261103-01（11/3约20:54北京）

本轮于20:46后补做，不能倒写成20:05方案前已完成。新登记池外重点研究LDOS、FSS、HCA；次级观察WCC、CACI、WAY。六只均非正式100只成员新增，也非今晚买入推荐。APH此前已提出，不重复算新发现。

[本轮完整发现/现金/风险/淘汰记录](reviews/2026-11-03_NEW_CANDIDATE_DISCOVERY.md)及[14项结构化池外台账](../data/watchlists/discovery_20261103.csv)已单独维护。11只完成定向经营/事件初筛，另3只只到检索线索；8只核算独立现金项目，完整正常化估值及指定替换比较0只，未以标题/目标价冒充通过。

|新纳入层次|代码|理由与未完成项|
|---|---|---|
|重点研究|LDOS|新季报盈利/现金指引上调但收入因转JV调低；核税率、正常化回款与政府预算|
|重点研究|FSS|销售/经营利润/订单增长有原始证据；22倍左右调整盈利并非自动便宜，核并购和季节性|
|重点研究|HCA|就诊量、既有盈利与现金支持研究；医疗政策、税款时点、负债和回购须核|
|次级观察|WCC、CACI、WAY|分别有增长/订单/订阅依据，但预收现金、应收保理、SBC/软件资本化及估值缺项保留|
|事件/暂缓|UHS、FIS、ESAB、CI、AFL|分别保留和解/法律、新财报、杠杆、监管资本及网络等风险|
|仅检索线索|PFE、GRAB、NOV|原文/现金/估值或持续盈利未充分验证，未升级研究优先级|

正式100只成员本轮不调整，仍100个唯一代码；新线索与现池成员分开计数，原池及备选资料/风险均保留。没有形成新的同额替换方案，不能将本轮研究纳入说成已证明应换出某成员。

## 22:29北京增量资料复核

本次补读LDOS公司Q3演示（有机收入+0.6%、Health收入−11.7%、季度CFO下降）及CACI11/3空军五年1.08亿美元合同；六只新研究对象的盘前源时间与待核状态追加到[发现记录](reviews/2026-11-03_NEW_CANDIDATE_DISCOVERY.md)及[池外CSV](../data/watchlists/discovery_20261103.csv)，首次发现字段和此前判断保留。LDOS不能仅据盈利标题上修/盘前下跌放行；CACI多年合同不当当季现金。FSS/HCA/WCC/WAY旧反方保留，六只完整正常化/指定换股比较仍未完成。正式100只成员本次不调整；这次范围仅六只池外资料及相关通用覆盖，未重做全池，不足以断言成员结构无需调整。原逐股CSV/备选资料未改日期。

## 23:01北京：重点决策与模型补完，成员不变

[同日方案追加的决策补核](reviews/2026-11-03_EVENING_OPERATION_PLAN.md)完整保存旧判断、本轮现金/资本模型、同额一年基准/下行/无倍数扩张以及改判条件。研究选择不再一律停在待复核：BKNG优先降低事件敞口、现金保留；STRL减仓方向排后；HII/G/DOX保留并冻结新增，旧HII→AMP、DOX→ADBE暂停。SCHW/REGN/INTU/AXS/PRDO和BRK.B/MSFT/AMZN/CVS形成当次有条件判断；AMP/ADBE/HUBB为指定比较对象。共17个池内代码新增decision_repair字段，全部其余原列、旧新闻/价格、风险和研究保留，研究深度不同不称17份完整DCF。池外LDOS等6只未因此升级可买。

实质资料：HII实际Q3现金恢复、BKNG预收与TTM现金、G170m预付/保理及迁册草案、STRL NCI/完整再投资/FCFE、DOX/ADBE重组与现金比较。迁册最终日期及个体税务未知；STRL模型含息现金不再扣净债。原100只价格/新闻统计仍按原时间，未重标本轮全量更新。成员无增删，CSV仍100个唯一代码；与Markdown链接保持一致。未把私人账户、数量、成本或订单写入资料。

## 23:44北京：池外LDOS资料推进

[发现记录](reviews/2026-11-03_NEW_CANDIDATE_DISCOVERY.md)及[池外CSV](../data/watchlists/discovery_20261103.csv)新增LDOS实际税款现金项目：9M CFO税款应收/应付正贡献239m，1423m现金代理归零该贡献后敏感度1184m；不可机械年化，不宣称239全部永久不可持续。持续现金/剥离和Health仍未形成可执行替换优势，新增资格不升级。其他池外资料及正式100成员本次未改，保留所有旧列/判断，仍100个唯一代码。主方案减仓所得现金不变；部分减仓不腾出新代码名额。

## 11/4 00:14北京：执行建议纠错，成员与基本面判断不变

既定卖出须配合买入规则已写入AGENTS/流水线/模板；[11/3方案最新追加](reviews/2026-11-03_EVENING_OPERATION_PLAN.md)撤回BKNG/STRL独立卖出留现金的执行资格，待明确合格买入端与完整比较后再启动。原风险、现金模型和研究历史保留，不把执行撤回说成公司风险解除。现行CSV对BKNG/STRL另增execution_rule_override字段，优先于旧独立减仓执行判断，原资料不删除。候选资格未因此放宽；本次为规则一致性核对，不冒充全100新研究，无成员增删，仍100个唯一代码。

## 11/4 00:24北京：四组指定比较与资料推进

[当晚方案追加](reviews/2026-11-03_EVENING_OPERATION_PLAN.md)完成BKNG对ADBE/LDOS/HCA/INTU四组同额一年决策比较，统一C1年现金口径。INTU/ADBE基准略优但易被合理误差逆转、风险和集中度未支持放行；LDOS/HCA当前现金补偿未显示稳健升级。不能声称100只都不如BKNG；本次没有重复全100价格/新闻深审。主方案仍不启动无合格买入端的卖出，不恢复旧暂停配对。

资料新增/纠错：ADBE TTM营运资金归一与英国CMA3/19取消费旧案仍Open（不是美国和解全部解除）；INTU FY26实际277m稀释股及R&D递延税现金范围；LDOS融资租赁/SES41.5%权益与Health持续现金；HCA TTM跨窗税款/NCI和11/2公司拟发票据。研究深度与模型假设在正文分开。现行100 CSV仅BKNG/ADBE/INTU新增direct_bkng字段，池外LDOS/HCA在[池外CSV](../data/watchlists/discovery_20261103.csv)及[发现记录](reviews/2026-11-03_NEW_CANDIDATE_DISCOVERY.md)对应更新。原历史列、首次发现和未解除风险保留；成员无增删，100唯一代码/原链接一致。

## 11/4 08:10北京：DOX重大事件置顶，旧持有模型失效

[美国11/3方案盘后追加](reviews/2026-11-03_EVENING_OPERATION_PLAN.md)记录已核公司Q4/FY27原文、T-Mobile违约/潜在终止及仲裁、报告与proforma收入下修、盈利/FCF、EIS/融资和现金归属。DOX新增/加仓冻结，旧445–520m持续现金模型撤回，新owner范围170–347m为明确情景；不将62.43常规收盘混作约35的盘后报价。旧DOX→ADBE不恢复。

DOX→SCHW作为美国11/4常规盘前须重新核准的条件配对：DOX≥35、SCHW≤90为研究界限，不是当前盘后实时可成交价，先卖后买、实际净款决定买入，价格/新公告变化整对重算。SCHW盈利与资本支持和NIM/金融集中反方均已列出，不声称严格收益支配。未核实际订单/成交，不把研究计划记为执行。

FY25已披露T-Mobile19.9%、AT&T25.9%、前十大约70%的客户集中属于事前可知；具体违约公开时点本次未找到更早正式披露，不能宣称绝无先知信号。旧模型/原理由保留供复盘，不用新解释覆盖历史。本轮仅DOX/SCHW重点更新，未重做100只；DOX退出未确认继续保留强制覆盖，成员仍100唯一代码，无增删。CSV追加material_event字段，优先于旧持有判断而不删除旧列。

## 11/4 11:50北京：有限增量补核，原记录与成员保持

本段记录实际读取时间，标识LIMITED-20261104-1150。本轮仅PRDO原始法律／并购／现金及财报节点补读，以及DOX、SCHW两只公开旧盘后报价刷新，不是全池更新。行情2/100（DOX、SCHW）；定向原始事件补核1/100（PRDO）；现金项目深入补核1/100（PRDO，尚未正常化）；完整正常化估值及指定替换深审新完成0/100。其余97只本轮未重新核查；PRDO未新查行情，DOX/SCHW本轮未重新深审原始经营。全部代码的旧字段、来源日期和研究保留，未把旧资料改成今日发布。

|代码|本轮已核资料及新旧判断|下一验证与限制|
|---|---|---|
|PRDO|补读[Q2 10-Q](https://www.sec.gov/Archives/edgar/data/1046568/000119312526337926/prdo-20260630.htm)：Fiorisce/Peters涉及核心Title IV合规的FCA诉讼未核到终局解除，DOJ拒绝介入不等于结案，指控不是已认定违法，公司无法估损。[法院自身10/13活动记录](https://www.cod.uscourts.gov/Seal.aspx?FileID=5205)仍见Fiorisce原告motion；第三方summary judgment motion标题不当裁定。维持观察，新增／加仓暂冻结待核；本轮未完成现股退出判断。|[公司公告](https://www.businesswire.com/news/home/20261022931505/en/Perdoceo-Education-Corporation-Schedules-Third-Quarter-Earnings-Conference-Call-for-November-5th)核实美11/5盘后Q3、17:00EST电话会＝北京11/6 06:00；核招生、学生融资、法律最新裁定及现金。原FSA贷款风险继续承接，不因本轮未重读而解除。|
|PRDO现金／资本|[FY25原始年报](https://www.sec.gov/Archives/edgar/data/1046568/000119312526149817/prdo-ars-april_2026.pdf)与Q2拼接TTM：CFO225.353−capex7.373−SBC12.435−融租本金5.213＝200.332m；1H26同式131.916m。为独立报表指定扣项代理，未完成税款／营运资金正常化，不能半年乘二或冒充永续现金。|6/30现金／短投734.824m含受限0.820m，融租8.887m及failed sale leaseback57.178m另列；[9/14 South原稿](https://www.sec.gov/Archives/edgar/data/1046568/000119312526389857/d61984dex991.htm)需130–150m交割、18m递延、最高56m earnout，仍须批准，最快2027/4。不能全额加账面现金，也不把新South利润提前并入；本轮未产生精确买价。|
|DOX|[行情页](https://stockanalysis.com/stocks/dox/)常规62.43@美11/3 16:00EST＝北京11/4 05:00；盘后34.58@19:59EST＝北京08:59，较常规收盘−44.61%。相对08:10记录的34.97为随后盘后成交变化；原重大事件冻结及旧持有模型失效判断未解除。|只是旧盘后成交快照，不是美国11/4盘前或实时bid/ask。延迟／价差／流动性未独立验证；本轮不重新批准旧配对条件，价格变化后需盘前整组重算。|
|SCHW|[行情页](https://stockanalysis.com/stocks/schw/)常规89.28@美11/3 16:00EST＝北京11/4 05:00；盘后89.07@19:58EST＝北京08:58，较常规−0.24%。保留08:10的盈利／资本正面及NIM／资金成本反方。|本轮仅报价刷新，未重算金融资本和独立加仓资格；不同时间报价不当同步成交条件。美国11/4盘前重核，不把一般企业CFO机械当金融可分配现金。|

本轮更新现行CSV的limited_20261104_*九个追踪字段，仅PRDO、DOX、SCHW有本轮事实，其余97行新字段留空。原63列内容逐格保留；旧判断和旧条件不删除，当前限制以实际最新复核为准。[现行逐股CSV](../data/watchlists/universe_100_20261022.csv)链接不变。正式成员没有增删，仍100个唯一代码；有限检查不足以断言全池已最优或无需调整，池外及备选未在本轮新增深审。没有披露个人持有标识或私人财务／交易安排。

## 11/4 11:57北京：BKNG新Q3／FTC应计与前景有限更新

本段编号BKNG-Q3-20261104-1157；原各时点事前判断保留。本次只完成BKNG一只的最新原始Q3／准备发言及未解除事件补核，现金为指定报表扣项代理，尚非完整正常化DCF或新两端执行方案；没有重新核其余99只，不把这一项补核称为全池更新。

|新资料与已核事实|对判断的影响／下一验证|
|---|---|
|[11/3盘后SEC原始业绩稿](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000044/q3-26bkngearningsrelease.htm)：FTC事项计收入减少900m及损失准备100m，合计1bn；从调整收入／利润／EBITDA中剔除。|相对旧Q2只知工作人员拟建议起诉，这是新的量化应计事实，须提高后续退出／替换比较优先。调查相关损失不能因“调整EPS仍增长”被忽略，也不能把应计写成已付款或最终和解。|
|[新10-Q原文定位](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000045/bkng-20260930.htm)／[SEC索引](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000045/0001075531-26-000045-index.htm)：11/3 17:09:41 EST接受。原文相关负债列9/30流动应计负债，披露尚未达成和解、可能超额处罚／赔偿及经营整改。|10-Q HTML本轮直取失败，索引可读；事件细节通过逐字转载辅助核对，900m／100m及报表数字以成功读取的SEC原始业绩稿交叉确认。不能假定1bn是上限、不能作每年固定损失。|
|Q3间夜+7%、gross bookings+10%、调整收入+9%、调整EPS+17%；GAAP收入8.893bn、净利2.717bn各约−1%。实际业务仍增长，股数减少也推动每股增速。|不能宣称平台盈利已崩坏；也不能把预订额当利润。9/30 issued1618m减treasury872m约746m期末普通股（报表整数），与加权稀释753m不同，原751m旧股数不直接覆盖新估值。|
|Q3 CFO1.137bn、公司FCF1.069bn，同比−21%／−22%；9M CFO8.071−PPE0.251−SBC0.427=7.393bn。|指定扣项现金不是归一化永续股东现金。预收、应付及应计负债不能全当过剩现金；旧Q2／TTM约8.1bn及7%收益模型需更新。将同一FTC应计影响剔出营运资金后再扣同一1bn，会造成重复扣减，须统一现金／价值桥。|
|[公司准备发言](https://s25.q4cdn.com/383369491/files/content_files/Q3_26-Prepared-Remarks-for-Website.pdf)：Q3现金受季节性merchant预收回吐约3.6bn影响；Q4间夜增长1–3%、调整收入0–2%、调整EBITDA约持平，包含中东冲突及国际需求放缓假设。|Q3现金下降不能凭时间顺序全部归因于FTC“已付罚款”；Q4增长降档是新增经营风险，不能线性延用Q3或旧模型增速。|
|[欧委会10/21 DSA正式调查](https://digital-strategy.ec.europa.eu/en/news/commission-investigate-how-bookingcom-combats-scams-and-fraud-under-digital-services-act)涉及假房源／钓鱼与付费排名披露。|本轮未核解除，正式调查不等于违法认定；未来支付／整改、佣金及平台转化影响需跟踪。|

**当前通用研究判定：新增／加仓继续观察冻结，提高后续退出或替换比较优先；不凭1bn应计单独发卖出指令。** 旧现金与估值条件须据新资料重算；原盈利基础和最强持有反方保留，不因新负面机械清空研究。具体买入端仍需独立合格并完成同额同期限比较；本段无个人账户、持有标识、数量、成本、目标比例、订单或成交资料。

本次CSV仅BKNG新增bkng_q3_20261104_*九列，其余99行新列为空；原72列逐格／原文保留。正式100成员不增删，备选及既有风险保留，链接不变。研究资料更新与成员调整分开；没有新完成全池价格／评级筛查，不把旧来源日期改成今日公告。

## 2026-11-04午间：全100基础资料补做与当次模型更正

本轮实际13:40后逐股读取100份常规行情/新闻及具名评级索引，均保留源日期；常规行情100/100、旧盘后92/100（缺BNY/CB/AXS/IQV/DOV/ITW/OTIS/RSG），不是今日盘前。原始经营/现金/资本或重大事件重点补核18/100；完整新正常化估值0/100，深度和未完成项如实写明。1/5/20价格窗口样本14个，含息/拆股差异及市场行业参照在[补做日志](journal/2026-11-03_OPERATION_REASON_LOG.md)及[本轮100行CSV](../data/reviews/2026-11-03_CLOSE_REASSESSMENT_100.csv)；本轮补做不倒写成定时任务已完成。

[当日主方案追加](reviews/2026-11-04_EVENING_OPERATION_PLAN.md)补完DOX→INTU及INTU/SCHW同尺度比较，当前优先买入研究端更正为INTU，旧DOX→SCHW不再自动有效。INTU优越性有合理增长/倍数反例，不宣称严格收益支配；独立现金与金融资本各自校验，不再混历史/前瞻PE或重复加经济现金。BKNG新TTM及PRDO核心息税/收购预留完成到本轮有条件判定，未冒称法律损失均量化。原判断/股数例子/条件保留并标被后续版本替代，不代表实际订单已撤销或成交。

现行逐股CSV原81列逐格保留，新增18个daily_latest_*通用当次字段为最新基础资料，旧列按其旧时点解释。每轮覆盖latest前另保存对应完整快照；不能将旧历史结论冒充当前。正式100无增删，仍100行/100唯一；全部已核个人覆盖仅私人集合核对，不在公开表标记。

本轮补核新Q3提高ETN/ANET深研优先，次轮核其普通股现金与估值；池外[ENSG/FOXA新登记、EME旧推进及LUMN事件线索](reviews/2026-11-04_NEW_CANDIDATE_DISCOVERY.md)已留档。研究优先不是即时买单，FOXA事件冻结不解除；本轮未完成足以增删成员的指定比较，维持成员不等于已证明无需调整。通用基金用官方9/30构成重核，NAV/执行缺项不编造。公开没有个人持有标识、账户、数量、成本、目标比例、余额、订单或收益。


## 2026-11-04 17:02–17:11北京：全池基础复取与盘前续记

[本轮日志](journal/2026-11-04_OPERATION_REASON_LOG.md)及[100行固定快照](../data/reviews/2026-11-04_1700_REASSESSMENT_100.csv)记录本次实际工作。纽约归档日11/4，常规终点11/3，不能称11/4已收市。100只均重新取四个收盘日期并计算1/5/20价格回报、市场与行业对照；100只新闻头部索引重读，99只具名表及PRDO替代源合计100只基础复核。不是全量新闻全文/券商原研报/全100现金审计。PRDO评级日期/动作有跨源冲突，未解除。

本轮定向有限经营重核4只：INTU/ANET原文、DOX/NVO原始索引（后两者正文直取失败），新完整DCF0/100；午间18只重点补核和原模型按原时点保留。新NVO结果、ANET业绩和CVS分拆报道提高事件优先；AT&T与DOX八年合作，不应被误写成AT&T也发生T-Mobile相同争议。DOX→INTU仍仅条件研究；不同步盘前/旧盘后报价不能当可执行配对，旧SCHW90示例不恢复。全部新资料、资格、下一点、缺项与来源写入现行CSV的run_20261104_*列，原99列逐格保留。

本轮新增登记池外FIX的盈利/原始现金表初筛：9M CFO减PPE约2.039bn，预收/超额开票余额增长、SBC/并购及必要投资正常化未闭合；不等于可持续普通股派现。没有新完成其当前估值/指定替换，不是买单。旧EME/ENSG/FOXA保留原记录，不重复算新发现。研究Top5：INTU、CVS、NVO、ANET、FIX，分别为配对/事件/现金估值工作优先；当次可执行新增名单为空。

正式成员不增删，100行/100唯一，资料更新与成员调整分开。全池基础索引加一个池外初筛仍不足以判断是否应换成员，不宣称名册最优。基金VITAX行业集中仍有效，最新可读NAV仅11/2，非11/3正式成交证明。公开不含个人持有标识、账户、规模、比例、成本、余额或实际交易。


## 2026-11-04约20:01–20:20：全池晚间更新与税现金纠错

[当日主方案最新追加](reviews/2026-11-04_EVENING_OPERATION_PLAN.md)、[100行固定快照](../data/reviews/2026-11-04_2000_PREOPEN_100.csv)：实际新读100/100常规价/新闻头部索引、94/100盘前（缺DFIN/AXS/MEDP/R/OSIS/PRDO）、100/100具名评级索引（PRDO替代源）。1/5/20及行业/市场对照承接17点已重算相同11/3终点，本轮逐股核收盘全部相同，不制造新交易日收益。关键现金/资本深核4/100（DOX/INTU/SCHW/CVS），新完整全财报/归一及DCF0/100，其余96只未新完成这一层；旧研究保留。

**当前判断优先读取evening_20261104_*14个新列，午间daily_latest与17点run_*为历史；原119列逐格保留。** INTU早已披露FY27现金税2bn，本轮才充分纳入：新桥4.886–5.086bn，旧6.074bn和345–350买入现金依据停用，这是研究遗漏/模型纠错，非今日公司新下修。新条件配对DOX>=36→SCHW<=90；当前90.28不符，不先单边卖出、不恢复旧订单或股数。收益反例、资本留存与共同风险取舍保留，不称严格收益支配。

CVS新报/正式拆分意向已原文确认，改为结果后有条件持有不新增；DOX财报后具名降级、BKNG降目标等逐股记录。客户/单点依赖风险字段有证据则填，精确比例未新取得者明确留缺。CROX新初筛、FIX旧缺口未实质闭合的检索尝试写入[发现记录](reviews/2026-11-04_NEW_CANDIDATE_DISCOVERY.md)及[发现CSV](../data/watchlists/discovery_20261104.csv)，不包装为可买或每日必须换成员。100行/100唯一仍不增删，尚不足以判断成员是否应调换。基金NAV更新不证明实际交换。公开无个人持有标识、账户、数量、成本、余额、目标比例或订单。

## 北京2026-11-05晨间：美11/4收市实际补跑

实际更新时间2026-11-05T06:58:36+08:00，本轮100/100四个收盘锚点及1/5/20价格收益、100/100新闻及具名评级索引新读；89/100盘后快照，完整现金估值深度另计，不冒称全100尽调。当前判断优先读取`morning_20261105_*`21个新字段，保留原133列和旧判断。固定明细见[11/4收市100只](../data/reviews/2026-11-04_CLOSE_REVIEW_100.csv)，正文及更正在[11/4操作日志晨间追加](journal/2026-11-04_OPERATION_REASON_LOG.md)。

资料实质变化包括：DOV独立现金补完后暂停旧210新增建议；STRL新价进入旧260–290重审区但不恢复330新增；G/PRDO形成11/5财报前明确保留、不新增判断，保留融资/法律尾险；QCOM/EMR新财报、BRK周末官方节点、VST与V等具名评级变化、ORCL可信报道未公司核实的线索，均分列原文/索引深度。冻结不会因上涨或未见新坏消息自动解除。

MCK/VRSK为本轮池外新登记，CROX为旧线索实质推进，详见[发现记录](reviews/2026-11-04_NEW_CANDIDATE_DISCOVERY.md)。三者均未被包装为即时买入。成员无增删，仍100个唯一代码；覆盖并未证明名单最优，不以单日涨跌换成员或移除失败对象。基金官方构成及NAV缺项另列，无个人财务信息。

## 北京 2026-11-05 17 时段：11/4 收盘复核与 STRL 后续

重取四个常规价格锚 100/100，重算相同终点的 1/5/20，92 个收盘值与晨间版存在差异，保留两版及时间。新闻头部 100/100，具名日期表 99/100 加 PRDO 替代索引（冲突未解），本轮盘后 74/100、早盘 12/100。26 个代码追加定向事件或旧模型复用状态，STRL 完成受影响现金估值重算，完整新正常化估值 0/100。现行 CSV 新增 followup_20261105_* 16 列，旧 154 列逐格保留。以 TCEQ、ERCOT 及公司实际积压区分已执行、待开工和未签项目，旧 330 条件仍暂停。G/PRDO 财报时间、BRK 周末节点及 QCOM/EMR 已核深度在[后续日志](journal/2026-11-05_OPERATION_REASON_LOG.md)。

### 池外研究变更台账

|代码|登记及来源日期|经营、现金与主要反方|当前资格及下一验证|
|---|---|---|---|
|ARDT|2026-11-05 登记；[11/4 公司 Q3](https://www.businesswire.com/news/home/20261104366372/en/Ardent-Health-Reports-Third-Quarter-2026-Results)|医院量增长、归母盈利；9M 扣资本开支、SBC、NCI 分派约 50.3m，支付方和补助影响需分离。|未通过新增；核按州补贴、债务及正常化现金后估值。|
|SEI|2026-11-05 登记；[11/4 公司 Q3](https://www.businesswire.com/news/home/20261104636686/en/Solaris-Energy-Infrastructure-Announces-Third-Quarter-2026-Results-Additional-Power-Contracts-and-Increased-Guidance)|已披露新电力合同及普通股盈利，债务和受限现金约束明显；与数据中心建设高度同因子。|未通过新增；核投产、维护资本、可转债及税款后普通股现金。|
|VRSK|旧线索；公司正式确认 11/5 盘前|业绩尚未纳入；交易与现金模型缺项保留。|待实报、收购进展和估值。|

现行成员仍 100 个唯一代码，与现行 CSV 链接一致。两只新池外线索和旧备选均保留，独立估值与成员替换证据不足，暂无调整。研究优先和即时新增名单分开，当前未放行新增。

## 北京 2026-11-05 20 时段：盘前资料与池外台账

[晚间方案](reviews/2026-11-05_EVENING_OPERATION_PLAN.md)及[现行逐股 CSV](../data/watchlists/universe_100_20261022.csv)已追加本轮资料。原170列逐格保留，新增 preopen_20261105_* 九列；仍为100个唯一代码。100只重新读取常规终点与新闻头部，盘前98只（缺 DFIN、R），具名日期表99只另 PRDO 替代源冲突。本轮19只定向更新、完整全新估值0只。增补事实与资格分开：STRL 许可、回款情景未解除；G/PRDO 等财报；BKNG 监管现金及配对待核；QCOM、CSCO 新具名评级已入逐股表。DUK 季报索引已见，原文现金回报待核；ZTS、FAST 结果缺项保留。

|对象|日期与变化|估值和下一点|
|---|---|---|
|MUR，新线索|11/5 公司三季度经营现金上升；9M 扣资本支出、非现金薪酬与少数权益分派的代理约 122.5m。|现阶段不进新增队列，核油价敏感度、维持资本、退役义务与债务。[发行人稿转载](https://www.stocktitan.net/news/MUR/murphy-oil-corporation-announces-third-quarter-wsmnty9rbhw2.html)|
|FIS，旧线索实质推进|11/4 财报的9M现金扣资本开支和SBC约1,238m，分开测试477m处置现金税。|保留观察；核整合、净债与强制还款。[原文](https://www.investor.fisglobal.com/news-releases/news-release-details/fis-reports-third-quarter-2026-results)|
|CI，旧线索实质推进|11/5 原报确认GAAP EPS下降而调整利润指引上修。|独立可分配现金待核；看医疗准备金、PBM与监管资本。[原文](https://newsroom.thecignagroup.com/2026-11-05-The-Cigna-Group-Reports-Strong-Third-Quarter-2026-Results,-Raises-2026-Outlook)|
|VRSK，旧线索待补|未取得当轮结果正文，AccuLynx 阶段继续查。|维持观察，旧估值不作为盘前买入依据。|

本轮正式成员不变，盘前基础覆盖与池外现金初筛仍不足以支持指定成员替换。即时新增名单为空。原备选、风险及早先结论留档。

## 2026-11-06 北京：11/5 收市复盘与覆盖调整

重取100个成员收盘锚与1/5/20收益、100个新闻头部、99个可读具名日期表、89个盘后。新增 close_20261105_* 逐股列。重点重核 G、PRDO、PEP 现金，STRL 按新价重算，完整全新估值0只。详见[操作日志](journal/2026-11-06_OPERATION_REASON_LOG.md)及[现行CSV](../data/watchlists/universe_100_20261022.csv)。

- **纳入 PEP，R 转备选。** PEP 增加消费必需品防御覆盖，R 仍可跟踪但与车队、物流及运输的周期风险重复，且公司自由现金受售车与车队支出影响。现行仍为100个唯一代码；研究席位不表示买卖建议。R 在 [先前逐股完整版本](https://github.com/zhixin0825/stock/blob/27045e126c680eb3f0e7c1b0e0076ca4edc9d585/data/watchlists/universe_100_20261022.csv) 保留全部历史列，本轮收盘270.16、1/5/20日 −4.58/−3.75/+14.87%，仍核收购对价、专用运输及残值。
- **EPAM 新线索**：盈利改善与经营现金下降并存，拟融资回购前需核现金归属和杠杆，不进入新增队列。[公司原报](https://investors.epam.com/news/news-details/2026/EPAM-Reports-Results-for-Third-Quarter-2026/default.aspx)
- **VRSK 旧线索推进**：Q3现金明显下滑，AccuLynx 仍须审查。G 收款风险提升配对复核优先；PRDO 学生资助及诉讼程序（11/6 反对简报）继续跟踪。两者均不新增。[VRSK 公司资料](https://investor.verisk.com/financials/quarterly-results/default.aspx) · [PRDO SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1046568/000119312526449730/prdo-20260930.htm)

### R 转备选时的历史资料行

| 对象 | 旧状态 | 经营证据 | 风险 |
|---|---|---|---|
| [R Ryder System](https://newsroom.ryder.com/news/news-details/2026/Ryder-Reports-Third-Quarter-2026-Results/default.aspx) | 事件觀察 | 10/22已發布Q3，GAAP EPS4.16/可比4.33增21%，營運收入增6%；全年可比EPS上調14.85–15.05。CFO2.6bn、公司FCF700–800m全年指引維持。 本轮事件：11/2公开公司稿确认已于11/1完成Efficiency Enterprises收购，增加6处网点、约50名技师、约1200台设备，预计2027收入约5000万美元；财务条款未披露，不能据此算已实现股东利润。BusinessWire URL含20261103，但同稿带时间转载标11/2 12:30ET；保留此时间/URL差异。 下一步：核收购对价、营运资本与车队capex；原Q4养老金非现金结算、DTS及二手车风险继续带入。 | 前版風險（歷史底稿，保留追蹤）：貨運及二手車價格週期；Q2專用運輸營運收入降3%，供應鏈稅前利潤降7%；10月22日財報可能改變舊指引。 本輪更新：DTS營運收入仍降1%，二手車殘值/租賃周期、資本密集性延續；公司FCF包含售車收益，與輕資產股不能直接同口徑。Q4約4.30/share養老金結算是預計非現金費用，不應誤判為經營崩塌。 |

## 2026-11-06 北京 20 时段：盘前与池外台账

[盘前方案](reviews/2026-11-06_EVENING_OPERATION_PLAN.md)及[现行逐股表](../data/watchlists/universe_100_20261022.csv)已补记 11/5 常规终点、11/6 盘前状态、新闻与日期评级索引。100/100 收盘、96/100 盘前（DFIN、J、ULTA、PRDO 缺）、100/100 新闻头部、99/100 具名日期表（PRDO 缺）。新增 preopen_20261106_* 八列，旧资料保留。15 个代码定向补核，完整新估值 0；G 的应收现金缺口与 PRDO 的 FCA 程序日期未解除。现行成员仍 100 个唯一代码；盘前与池外筛查不足以再替换席位。

- **UBER，新登记（11/6 阅读 11/4 原报）**：9M CFO 扣设备及 SBC 5,999m，剔除含保险应计的营运资金贡献后 5,158m。观察，核保险赔付、司机激励、监管、非控股归属与估值。[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm)
- **EPAM，旧线索推进**：现金与回购融资分开，拟 500m ASR 部分使用信贷，待可分配现金与杠杆重核，未放行。[公司原报](https://investors.epam.com/news/news-details/2026/EPAM-Reports-Results-for-Third-Quarter-2026/default.aspx)


## 2026-11-07 北京20时段：周末、11/6收盘与池外资料更新

[晚间主要方案](reviews/2026-11-07_EVENING_OPERATION_PLAN.md)与[当日日志](journal/2026-11-07_OPERATION_REASON_LOG.md)使用纽约自然日11/7。周六休市，最新常规价格为11/6；不制造周六收益、盘前或新NAV。价格及1/5/20重取100/100，新闻头部100/100，具名日期表99/100（PRDO缺），有效盘后90/100；盘后缺TROW/DFIN/AXS/DHR/DOV/ITW/IR/ACM/CRM/ULTA。日期索引字段95/100，缺ORCL/CRM/ADBE/PAYX/AZO，旧日期不当未来确认。

本轮新增REGN/HII两项SBC扣项现金桥；EOG/VST新结果定向推进，BRK周末事件、CEG/TSM未来节点、STRL旧政策和MSFT合同报道分别记证据级别。17个定向代码不等于17个深入估值；完整全新正常化估值0/100。G合格配对、STRL地域现金、PRDO提交材料、BKNG监管及AMZN/INTU完整现价持有优势尚未闭合。最新状态优先读现行CSV的weekend_20261107_*14列；原196列逐格保留。新列没有批量公开原始价格镜像，只存自行计算回报、索引和通用结论。AMZN主要行业对照改XLY、XLK保留作云业务辅助，属比较口径修正。

|对象/发现与本轮日期|新旧状态及已核资料|资格、最强反方和下一验证|
|---|---|---|
|WEX，本轮首次登记11/7；原报10/28|支付/福利平台盈利，全年调整EPS上修。9M GAAP CFO−419.6m；公司调整FCF502.8m需要银行存款、融资和资本桥，不直接当可派普通股现金。|11/6收182.22；SBC112.4m、银行法定资本/存款、债务及燃油价格需核，未通过新增。[SEC](https://www.sec.gov/Archives/edgar/data/1309108/000130910826000039/wexq32026earningsrelease.htm)|
|HAYW，本轮首次登记11/7；原报10/28|泳池售后业务和实际盈利；9M CFO减设备、软件与SBC184.720m，对去年251.755m；剔营运资本时点约113.997m，不年化。|11/6收16.24；净债约489.5m、住房/渠道与季节性、完整普通股估值待核，未通过新增。[公司](https://investor.hayward.com/investor-news/news-details/2026/Hayward-Holdings-Reports-Third-Quarter-Fiscal-Year-2026-Financial-Results-and-Increases-2026-Guidance/default.aspx)|
|VRSK，旧线索11/7实质推进|Q3 10-Q确认8/14 AccuLynx履约令、3.8m直接成本及利息，10/23上诉维持；旧事件今天补原证，不能再只写交易终止。|不新增；约2.35bn对价/融资、FTC许可和现金模型须纳入。[SEC](https://www.sec.gov/Archives/edgar/data/1442145/000143774926035083/vrsk20260820_10q.htm)|
|UBER/EPAM，旧线索例行承接|未新闭合保险准备与普通股归属、融资回购后估值，未冒称实质推进。|保留观察；下一步补关键现金，不重新包装新发现。|

认真初筛为两个新对象；DLB仅资料/日程检索未完成初筛，不计完成数。研究Top5为BRK.B/G/STRL/PRDO/BKNG，事件时效将BRK移至首位，非买入排名。正式成员本轮不调整，仍100个唯一代码；PEP入池、R备选和旧风险均保留。两项初筛与全池基础更新不足以证明名册最优，不为每天换名字凑次数。通用基金以9/30官方成分及11/6二手NAV更新，科技重叠和债券风险保留，不含私人菜单、比例、金额或执行事实。


## 2026-11-08 周日维护及池外变更台账

读取截止2026-11-08 12:13:04 UTC，北京时间加8小时。纽约11/8休市，价格终点仍11/6；不制造周日收益。[当次完整研究](reviews/2026-11-08_EVENING_OPERATION_PLAN.md) · [同日日志](journal/2026-11-08_OPERATION_REASON_LOG.md)

- 本轮重新取得100/100的四个价格锚及1/5/20收益、新闻头部100/100、具名评级表99/100（PRDO缺），盘后90/100（缺TROW、DFIN、AXS、DHR、DOV、ITW、IR、ACM、CRM、ULTA）。原公司未来财报日期没有逐家官方新确认；不是100份研报/原始新闻尽调。
- 原210列逐格保留，新增14列weekend_20261108_*。原始经营/现金/资本实质新查池内2/100：BRK.B新财报、G融资租赁更正；全新完整正常化估值0/100。其余98只的原模型、未解除事件和下一核验按新列承接，不能改日期冒充新做现金桥。
- BRK.B：11/7实报取代11/7事前“未发布”。9M CFO减资本支出17.777bn，短债收益分类及普通股归属仍未闭合；当前570.89约1.60倍账面，有限承担风险的事件判断更新，不新增。BHE 11/3口头辩论不是终局免责。
- G：TTM融资租赁本金9.029m补扣，原221.939m代理更正212.910m；9M更正−23.408m。原值保留为扣租赁前口径；固定旧倍数重算基准/恢复/下行，不因股价上涨解冻。实收与合格配对仍待核。
- 成员不调整，仍100个唯一代码；新初筛不足以证明席位替换。保留备选和风险，不把“没有买单”当作穷尽机会或现股全通过。

|对象／类别／日期|实际推进与证据|反方、估值/准入、下一验证|
|---|---|---|
|JKHY；本轮首次发现11/8，原报11/3，FY27Q1至9/30|银行核心系统/支付；GAAP EPS2.28对1.97；CFO扣设备、内部软件和资本化开发82.932m，SBC未取得，不年化。[SEC原报](https://www.sec.gov/Archives/edgar/data/779152/000077915226000095/jkhy-20260930xex99pressrel.htm)|11/6收173.23；deconversion收入增加不是续费增长，银行整并流失/季节性。观察暂不买入；下一核SBC/租赁、正常化现金、同一年估值和指定替代比较。|
|ITT；本轮首次发现11/8，原报11/4，9M至10/3|工业流体/运动控制；Q3 GAAP EPS1.38对调整2.26；9M CFO扣capex加补助扣SBC430.9m，不含补助426.0m。[SEC原报](https://www.sec.gov/Archives/edgar/data/216228/000021622826000072/earningsrelease2026q3.htm)|11/6收205.55；收购与新债/票据、协同和利润调整差异。观察暂不买入；下一核收购后稳态现金、债务/租赁/NCI及独立估值；非单季EPS乘四。|
|WEX；旧线索11/7→11/8实质推进|新读10-Q，FDIC2023命令10/15已终止；Tier1/平均资产9.26%、CET1/RWA12.30%、总资本13.01%。[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1309108/000130910826000043/wex-20260930.htm)|不再保留该命令为未解除限制；9M信用损失准备85.5m对57.9m，母公司可分派现金/银行资本/油价与信用正常化仍缺，不能全面解冻新增。|
|HAYW、UBER、EPAM、VRSK；旧线索例行承接|本轮未新增闭合其正常化/保险准备/普通股归属/收购履约现金。|不是首次发现或实质推进，不提高资格，沿原验证点。DLB仅搜索线索，不计完成初筛。|

实际搜寻覆盖银行科技、工业流体/运动控制、支付/福利与泳池旧线索，认真初筛2个；未把检索命中数当完成数。JKHY/ITT在可见项目检索未见旧登记，不能据此声称从未有人研究。两项未通过立即买入门槛，未永久淘汰公司。研究Top5为G、BRK.B、STRL、PRDO、BKNG；可买名单为空。11/9开盘前先补G配对、BRK归属与STRL具名项目，随后PRDO/BKNG尾险与AMZN/INTU现价优势。未完成复核不等于持有结论。


## 2026-11-09 盘前资料及候选变更

复核截止 2026-11-09 09:16:42 UTC，北京加8小时。11/6常规价100/100、同端点1/5/20承接，11/6旧盘后90/100。11/9早盘时间戳25/100，新闻头部100/100、具名评级99/100（PRDO缺）、财报页面日期95/100（ORCL、CRM、ADBE、PAYX、AZO缺）。时间、准入和实际缺项见[日志](journal/2026-11-09_OPERATION_REASON_LOG.md)及[逐股CSV](../data/watchlists/universe_100_20261022.csv)。4个池内定向资本/现金/配对推进，3项另外的公司公告核验，0个新完成完整估值。

- G/SCHW同额一年含息比较完成敏感度更新，回款假设可以逆转排序，双压接近持平，资本准入及净改善仍待核。G前9M扣租赁代理−23.408m，达到原全年350m研究水平需Q4 373.408m，同口径较上年Q4约高58%。继续核实际回款，不把算术阈值当公司指引。
- STRL原始10-Q补了地域和合同营运资金。CEC和Stone Ridge使Texas敞口具体化，Plateau、Petillo另有东南和东北/中大西洋敞口；仍缺当前逐项目许可与开工。9M合同营运资金净流出350.834m，现金扣额后代理283.861m；未扣所有必要融资本金与未来对价。新增冻结，盘前反弹不改准入。
- BRK.B核实两笔收购已执行及现金对价，收购已反映在季度余额；归属资本仍待桥。REGN和JNJ核原始临床公告，未计入商业现金。AMZN新出现的头部源于11/5旧合作，未形成利润估值上调。

|对象|发现、经营现金证据|最强反方、资格和下一验证|
|---|---|---|
|UFPI|本轮初筛11/9，原财报10/28及其后10-Q。79.92，9M实报现金扣全额capex、SBC/授予和已分派NCI约86.461m，对164.432m。|公司自定义FCF有调整。营运资本占用、包装/建筑量价、维持资本及完整估值缺。观察，核收款和现金归属。[10-Q](https://www.sec.gov/Archives/edgar/data/912767/000110465926122507/ufpi-20260926x10q.htm)|
|KNSL|本轮初筛11/9，原报10/22。383.73约4.50倍账面，Q3经营EPS5.70、综合成本率75.4%。|前期准备金有利发展和再保自留、灾害下行及可分派资本缺。观察，核事故年度及母公司分派，未通过新增。[原报](https://ir.kinsalecapitalgroup.com/news/news-details/2026/Kinsale-Capital-Group-Reports-Third-Quarter-2026-Results/default.aspx)|
|WEX、JKHY、ITT|沿11/8核实线索，保留源时点。|本轮未进一步闭合各自现金/资本估值，不提升资格。|

两项新初筛来自包装/木材与特殊险，当前及备选/可见仓库检索未见登记。成员仍100个唯一代码，保留移出备选和旧风险。研究优先顺序G、STRL、BRK.B、PRDO、BKNG，当前可执行新增为空。盘前变化不当作常规收盘收益。


## 2026-11-09晚间资料与候选台账追加

读取截止 2026-11-09 12:04:15 UTC，北京加8小时。11/6常规价100/100，11/9带时间盘前93/100，新闻头部100/100，具名表99/100，日期索引95/100。新增十列，原234列和100个唯一代码保留。盘前缺DFIN、AXS、MEDP、IR、OSIS、PAYX、G。正反依据和逐股深度见[11/9晚间方案](reviews/2026-11-09_EVENING_OPERATION_PLAN.md)。

- 早段已做UFPI、KNSL，后续另有TKR、ATMU、CAH及DFIN推进，均留原日期；晚间实质新初筛为BMRN、MUSA，不混称为今日新财报。两只不加入现行100，未达到新增资金资格。
- ADBE、FANG、TROW用新早盘价和原锚定倍数重算。ADBE与TROW某些情景实质挑战G，但订阅补救、油价/储量投入、主动流失分别限制准入，G回款也能反转排序。不得把暂无可执行配对写成现股最优。
- CEG于06:53 EST提交实报，Q3 GAAP EPS5.19，前9M CFO减资本开支1.518bn对1.469bn。已签Peak+依机组2028起供，条件贷款不能算当期现金。06:35报价早于实报，22:00北京电话会与后续财报后报价待核，不新增。[8-K附件](https://www.sec.gov/Archives/edgar/data/1868275/000186827526000116/ceg-20261109991.htm)
- 另记录GOOGL Waymo补救充分性新调查报道；旧召回范围已核，新案原文及经济影响待核。保留各历史风险，成员不因异步盘前涨跌调整。

|代码|本轮初筛日期与来源|现金、反方及下一点|
|---|---|---|
|BMRN|11/9晚间；11/2原报；56.03收盘、56.68盘前。|9M CFO扣capex及SBC约326.258m对531.538m。并购及IPR&D投资超5bn，核收入协同、债务/租赁、研发现金和归一化估值，观察。[原报](https://investors.biomarin.com/news/news-details/2026/BioMarin-Reports-Third-Quarter-2026-Financial-and-Operating-Results/default.aspx)|
|MUSA|11/9晚间；10/28原报；521.89收盘、523.89盘前。|Q3净利176.0m，9M扣资产投入及营运资本释放408.7m，未完全扣SBC/租赁。核油品毛利、维护与扩店资本、持续现金及一年估值，观察。[10-Q](https://www.sec.gov/Archives/edgar/data/1573516/000157351626000195/musa-20260930.htm)|

本轮跨罕见病药物、便利店与油品零售，并查拍卖平台日程。只有两只取得足够原始材料列为初筛。研究优先为ADBE、FANG、TROW、CEG、DFIN，今晚可买为空。成员仍100只，保留原备选。

### 2026-11-10 盘前核查与11/9收盘复核

- 11/9纽约常规收盘、1／5／20日收盘价格走势100/100，盘后带时间85/100，新闻头部索引100/100，具名评级99/100、财报索引91/100。原始与复权收盘回报分列，源自11/9、11/6、11/2、10/12。11/9人工补记有17个代码的回报与这次原始价格不同，旧值可由Adj Close复现；保留历史。
- G与ADBE复核了同额一年固定倍数情景的相对排序，G需约231–240m的持续滚动现金以追平ADBE 6%–10%现金增长情景；G实收、ADBE CMA和续费未闭合。STRL收盘290.67超过旧基准终值区间，核具名许可、开工及回款，新增资格未通过。TSM 11/10月营收、PEP组织调整分列。
- 本次首次核两条池外经营线索。以下均保留观察，未加入100只，也未通过新增买入。既有MUSA、NRG和BMRN沿前轮台账，未重记为新发现。深度和数据缺项见[复盘日志](journal/2026-11-10_OPERATION_REASON_LOG.md)。

|代码|发现／事件|现金和最强反方|下一核验点与资格|
|---|---|---|---|
|CHD|11/10发现，10/30财报；有机销售+5.1%，Q3 EPS 0.89对0.75|9M CFO扣设备和非现金薪酬689.1m对740.6m；收购现金、关税退款和营运资本影响持续性|核收购对价、退款和归一化现金估值，保留池外观察。[10-Q](https://www.sec.gov/Archives/edgar/data/313927/000119312526441040/chd-20260930.htm)|
|TXRH|11/10发现，11/5财报；Q3 EPS 1.36，Q4首五周同店增速约1.5%|39周扣设备、SBC、NCI后现金代理223.149m对167.998m，收购与维护资本需分列；客流与工资、食品成本可能压利润|核成熟店客流、维护投入、租赁和正常化估值，保留池外观察。[10-Q](https://www.sec.gov/Archives/edgar/data/1289460/000162828026071362/txrh-20260929.htm)|

成员维持100个唯一代码。CHD与TXRH留在本次候选变更记录，现有备选归档继续保留。

### 2026-11-10 晚间候选变更与复核

- **SANM**（首次11/10，11/9盘后财报）。FY26 GAAP EPS $6.85，季末股东经营现金桥先从FY CFO $944.094m减净设备 $403.267m得$540.827m，对上期$478.181m，尚未扣齐SBC、NCI和租赁。净收购现金另有$1.114bn，财年营运资金负贡献约$72.5m，前期为正$189.0m；不能把并购带来的报告增幅当同店增长。06:21 EST $181.00较前收149.64高约21%。需核ZT客户集中、维护投入与交易后常态归属；保留研究，未放行。[原报](https://ir.sanmina.com/news/news-details/2026/Sanmina-Reports-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx)
- **INFU**（首次11/10，11/5财报、11/10电话会）。季度EPS $0.15对$0.11，患者服务+15%与设备服务−17%分化。9M CFO $18.091m扣医疗设备$8.712m、其他设备$0.321m及SBC $3.719m，未加设备出售为$5.339m，对上期$8.423m。11/9收14.68，本轮无可核盘前。核GE Healthcare合同重订和设备再投入，低现金补偿暂留池外观察。[原报](https://ir.infusystem.com/news-events/press-releases/detail/1408/infusystem-announces-financial-results-for-third-quarter)
- **DSGR**（首次11/10，11/5财报）。Q3有机销售+9.2%，9M CFO $20.359m对$66.906m。扣净设备、净租赁设备、SBC及融资租赁本金后约−$6.275m，对上期+$43.549m；未扣收购现金。应收和库存占用、约3.4倍净杠杆及收购回报制约，初筛淘汰本轮新增。11/9收34.95，36.23仅为11/9盘后。等营运资金释放和归属现金转正再复核。[原报](https://www.sec.gov/Archives/edgar/data/703604/000070360426000050/a2026q3pressrelease.htm)

- 早段CHD、TXRH仍保留；晚间FANG公告将融资和归属分派列为新待核，G/ADBE翻转点按新报价调整，STRL按新价确认风险补偿不足。
- 100只成员无增删。晚间盘前95/100、新闻头部100/100、具名评级99/100、财报索引95/100；早段全100收盘与趋势留档。完整新正常化估值0/100。详见[晚间方案](reviews/2026-11-10_EVENING_OPERATION_PLAN.md)及[100行明细](../data/watchlists/universe_100_20261022.csv)。

### 2026-11-11 收盘复核及候选变更

- **ONON**，11/11首次初筛，11/10财报。季度营收9.314亿瑞郎，同比+17.2%，DTC增长25%。前9月CFO 413.3m瑞郎，减有形资产68.5m、无形资产16.1m、租赁付款61.3m、在融资栏列示的利息20.2m及SBC 50.6m，现金代理196.6m，去年约80.9m（按汇总SBC 48.6m）。11/10收34.70美元，19:59盘后34.75。待核营运资金、渠道库存、双股权换算及汇率，保留池外研究。[SEC原报](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000025/a26q3-ex991xpressrelease.htm)
- **AMRC**，11/11首次初筛，11/9财报。前9月经营现金−60.251m，上年经重列+33.323m；两期ITC出售收款已进经营现金，本期剔20.411m后为−80.662m。另有能源项目资本投入334.910m和维护20.203m，融资现金474.244m。11/10收27.62，19:50盘后27.13。待核未开票项目、税抵收款、项目融资和非控股归属，暂不进入新增队列。[SEC原报](https://www.sec.gov/Archives/edgar/data/1488139/000162828026072337/amrc-20260930.htm)
- 已发现线索中，FANG补到交易公告后收盘，下一步仍须出资和交割后分派。ADBE把Google产品合作和可确认现金分开，G/ADBE现金翻转点按同收盘重算。SANM、INFU、DSGR沿前次记录，未计作本次首次发现。现有证据不足以调整100个唯一成员。研究优先ADBE、TROW、FANG、CEG、ONON，执行名单为空。

- 11/10的收盘及1／5／20日100/100，盘后84/100，新闻头部100/100，具名评级99/100，财报索引96/100。收盘与复权回报分列。7只价格情景、另CRWV盘后现金桥与两家池外初筛。100个唯一成员继续沿既有名单。
- STRL、G继续优先研究配对减敞口，项目现金和合格配对仍待核。CoreWeave预计90亿美元预付尚无可验证的STRL项目现金映射。详见[复盘日志](journal/2026-11-11_OPERATION_REASON_LOG.md)及[100只明细](../data/watchlists/universe_100_20261022.csv)。

### 2026-11-11 晚间候选变更与复核

- **CLFD，11/11首次初筛。** 11/10原报，FY26持续营收151.9m，持续净利2.1m对6.3m。持续经营CFO 12.621m减设备及无形3.597m、SBC 4.649m为4.375m，去年17.213m，未加入资产出售。盘前30.13（05:24）。光纤订单和BEAD授标、拨付、收入、回款须分开。毛利与现金走弱，本轮未通过新增。[原报](https://www.sec.gov/Archives/edgar/data/796505/000117184326007330/exh_991.htm)
- **KRMD，11/11首次初筛。** 11/10原报，Q3收入11.6m、净利约0.2m。9M经营现金−0.652m，扣设备0.422m、SBC与权证费用2.067m、融资租赁0.104m后约−3.246m；去年约−2.980m。11/10收3.16，晚间缺当日盘前点。患者基础增长有经营证据，付款方与大客户合同、应收及股东现金转正仍待核，本轮未通过新增。[原报](https://www.sec.gov/Archives/edgar/data/704440/000116169726000244/form_10-q.htm)
- **GIB为早段已发现线索。** 已读11/11公司发布的全年结果，进展和同业比较见正文。ONON、AMRC沿当日早段现金研究，前日SANM等仍保留。研究优先ADBE、GIB、TROW、FANG、ONON，执行名单为空。现有证据不足以换入观察池成员，仍为100个唯一代码。

- GIB财报06:30发布。07:00盘前84.45较发布前点高，全年CFO扣业务投入约C$2.094bn，季度CFO同比回落，下一步核全年租赁及SBC、政府项目收款与汇率。另重算G/ADBE翻转点、STRL情景，PWR补核现金补偿。REGN盘前源冲突，研究暂沿昨收。
- 晚间核昨收100/100、盘前带时间95/100（含REGN冲突）、新闻索引100/100、具名评级99/100及财报索引96/100。100个唯一成员，完整新估值0/100。见[晚间方案](reviews/2026-11-11_EVENING_OPERATION_PLAN.md)及[100只逐股明细](../data/watchlists/universe_100_20261022.csv)。

## 2026-11-12 候选变更与收盘覆盖

北京时间 17:03:45 截止，承接纽约 11/11 时段。100 个唯一代码。常规走势 100/100，11/11 盘后带时间 99/100（缺 DOV），11/12 早盘 1/100（ADBE），新闻头部 100/100，具名索引 99/100（缺 PRDO），财报索引 97/100（缺 ORCL、ADBE、PAYX）。重点复核 23/100，完整新正常化估值 0/100。更新资料与候选台账，成员本轮无变动。[操作理由日志](journal/2026-11-12_OPERATION_REASON_LOG.md) · [逐股CSV](../data/watchlists/universe_100_20261022.csv)

- **ALH，11/12首次入初筛（11/10原报）。** 商用洗衣设备Q3收入4.61亿美元、同比+5%，净利6500万美元。前9月CFO 230.202m扣资本开支23.780m及SBC 7.580m为198.842m，去年同口径84.439m。营运资金占用少约49m，利润有一次性关税退款，设备应收及证券化边界须重做。按全年资本开支约60m的指引，第四季开支明显偏重。核融资相关现金、年末投入和正常化估值后再排买入资格。本轮进入研究，尚未通过买入。[公司原报](https://ir.alliancelaundry.com/news-events/press-releases/detail/149/alliance-laundry-reports-third-quarter-2026-results)
- **USFD，11/12首次入初筛（11/5原报）。** 餐饮配送；前39周CFO 1,160m减现金购置266m、SBC 76m为818m，去年同口径736m，均未扣归在债务偿还的融资租赁本金，未计资产处置。核车队租赁现金、营运资本、杠杆和餐饮需求，随后做无倍数扩张估值。本轮进入研究，尚未通过买入。[SEC原报](https://www.sec.gov/Archives/edgar/data/1665918/000166591826000053/usfd09262026ex991.htm)
- **GIB旧线索实质推进。** 用全年审计的 C$1.851bn 现金代理更新六月TTM比较，扣实际并购后约 C$1.652bn。续约及采购现金、FX和融资仍待核。**TROW**为池内例行跟踪后重算。**CLFD、KRMD**的原结论仍见11/11盘前报告，未取得改变光纤现金走弱或医疗设备股东现金为负的新证据。其余原线索无新增可核资格。研究优先 STRL 项目、G／GIB、ADBE、TROW、ALH／USFD。无经复核可执行新增，100个成员无需按本轮两条初筛线索更换。

## 2026-11-12 早段盘前增量候选

2026-11-12 10:08:28 UTC。100 只逐只复查，收盘及新闻索引 100，具名评级 99，财报索引 97，带时刻盘前点 90。完整新估值 0。成员不变。详见[当日日志](journal/2026-11-12_OPERATION_REASON_LOG.md)。

- **CAE（本轮首次入初筛，11/11 盘后原报）**。FY27 上半年 CFO 扣现金购置固定资产、无形投入、权益结算股权薪酬及租赁本金约 **C$218.1m 对 −C$97.7m**，剔除营运资本变动约 **C$154.0m 对 C$78.9m**，合资与非控股归属待核。第二季民航分部调整利润同比降，国防分部含以前年度税抵，Flightscape 拟售 **US$500m** 有条件，未计入现金。11/11 纽约收 27.39，未取 11/12 盘前点。11/12 08:00 EST 电话会后核续约、交付、合资归属和正常化估值。[公司原报](https://www.prnewswire.com/news-releases/cae-reports-second-quarter-fiscal-2027-results-302936965.html)
- **FNV（本轮首次入初筛，11/11 盘后原报）**。前9月 CFO **US$1,432.1m 对 1,067.2m**，扣股权薪酬、设备及当期实际特许权再投入后约 **US$762.8m 对 −1,099.3m**。并购支出不均匀，此为当期代理。金当量销量下降 6%，现金受金属价格支持。Cobre Panamá 库存加工实际交付约 3,716 GEO，原矿生产仍停，复产不入基准。按 11/11 价格和市值，扣实际特许权再投入的机械年化现金收益率约 2.1%，不支持当前价格下直接新增。11/12 08:00 EST 电话会后核正常化商品价格、再投资和审批。[公司原报](https://www.prnewswire.com/news-releases/franco-nevada-reports-q3-2026-results-812447402.html)
- **USFD、ALH（旧线索实质推进）**。USFD 前39周现金减股权薪酬、资本开支及融资租赁定期付款为 **722m 对 650m**，补齐此前租赁缺项；按指引最后13周现金资本开支约 144–164m。ALH 10-Q 确认信托受限现金 27.882m、证券化应收净额 612.303m、保留权益 62.582m。原 198.842m 是合并口径，仍须拆出实际可分配金额。均保留研究，暂无新增资格。[USFD SEC原报](https://www.sec.gov/Archives/edgar/data/1665918/000166591826000056/usfd-20260926.htm) · [ALH 10-Q](https://ir.alliancelaundry.com/financial-information/all-sec-filings/content/0001628280-26-072698/all-20260930.htm)
- **GIB、TROW（早盘价格更新）**。GIB 续约与季度实收仍待核，现金模型不变；TROW 保留11/11资金流量敏感度，不重复扣减。以上线索均未形成可执行买入；不调整100个池内成员。

## 2026-11-12 晚间候选台账

100 个唯一代码不调整。复核收盘及新闻索引各100，带时刻盘前97，具名评级99，财报索引97，池内定向重算7，完整新独立估值0。

- **BALL，11/12 晚间首次初筛。** 11/3 的原报及 10-Q。三季可比营业收益 451m 对 440m，GAAP 归属亏损 94m。前9月营业现金 20m 对 51m，扣资本开支后为 −439m 对 −253m，均未扣股权薪酬。现金受约 1.23bn 营运资金净流出影响，英养老金结算中的 475m 为非现金项。公司全年约 900m FCF 指引不能直接当作已经收到的普通股现金。晚间核到 65.59（04:00 EST），留研究，核季节性回收和实际资本开支。[SEC 10-Q](https://www.sec.gov/Archives/edgar/data/9389/000110465926121838/ball-20260930x10q.htm) · [公司原报](https://www.ball.com/newswire/article/124291/ball-reports-strong-third-quarter-2026-results)
- **CTVA，11/12 晚间首次初筛。** 11/11 盘后首次按分拆后农化业务发布季度结果，11/12 10:30 EST 电话会。前9月持续业务经营现金 −3.878bn 对 −0.941bn，养老金/OPEB 缴款 1.567bn 对 0.110bn，递延收入和其他负债也占用现金，暂不将缴款全当可逆。独立持续业务现金、分拆后资本结构和报价口径尚需闭合。本轮剔除出新增比较，待补分拆后同口径现金桥。[公司原报](https://investors.corteva.com/static-files/c57b6c4a-d707-4cc1-970d-99f35ed15ef5) · [财报会](https://investors.corteva.com/events/event-details/corteva-agriscience-3q-2026-earnings)
- **旧线索。** USFD 的 10-Q 增量（融资租赁付款扣后 722m 对 650m）及 ALH 的证券化信托归属已在同日早段完成，晚间未取得可核更新报价或进一步现金证据。GIB 续约/实收仍待核，ADBE 与 G 配对按新价重算。CAE、FNV 均为今日早段已发现，FNV 盘前 250.75（06:31），上轮扣当期实际再投入后机械年化收益仍约 2.1%，原矿停产维持基准处理。CAE／FNV 的 08:00 EST 电话会尚未开始，结果不可先入模。100 个成员未变，未用暂未合格的池外对象替换。研究优先 GIB、ADBE、USFD、CAE、BALL，可买名单为空。[同日现金核验](journal/2026-11-12_OPERATION_REASON_LOG.md)

## 2026-11-12 正式收盘后的候选变更

收盘及1／5／20日 100/100，早段盘后93，新闻索引100，具名评级99，财报索引97。CSCO、AMAT各补现金桥，完整新估值0。100个唯一代码不变。[收市复盘](journal/2026-11-12_OPERATION_REASON_LOG.md)。

- **YETI，11/12 收市轮次首次入台账。** 原报第三季经营利润 60.968m 对 54.353m。前九月经营现金 110.219m，扣现金资本开支 38.502m 和股权薪酬 28.425m，现金代理 **43.292m 对 17.657m**；应付款变动及税款有较大贡献，尚未核完整租赁及正常化。全年调整后EPS指引由 2.94–3.00 下调至 2.90–2.95，收 38.30，观察假期销售和回款，不晋级。[SEC原报](https://www.sec.gov/Archives/edgar/data/1670592/000167059226000043/yeti-20261112xex991pressre.htm)
- **EPC，11/12 收市轮次首次初筛。** FY26 现金流 49.6m 扣资本开支 59.6m、股权薪酬 19.0m，得 **−29.0m 对 +16.9m**。均为合并历史现金，未计资产出售及未验证调整；剥离交易和过渡服务收入限制同口径。收 28.74，FY27 公司调整后FCF 100–120m 为指引，待核剥离税款、保理和新业务实收，暂排除新增。[公司原报](https://ir.edgewell.com/news-and-events/press-releases/2026/11-12-2026-110150942?sc_lang=en)
- **旧线索。** CAE 28.15、FNV 247.72 更新到收盘。未取到足以改写 CAE 合资归属或 FNV 矿山复产与正常化再投入的新证据。BALL 的营运资金回收未补，CTVA 分拆后独立现金与资本结构未闭合，均沿当日晚间记录。GIB 重新计价，季度回款继续核。100 个成员无调整。研究优先 CSCO、AMAT、GIB、ADBE、YETI，可执行新增为空。

## 2026-11-13 盘前候选台账

收盘索引及新闻头部各 100/100，具名动作 99/100，财报索引 97/100，带时标盘前 93/100。盘前缺 DFIN、AXS、IQV、IR、J、G、PRDO。定向重价／现金收益率更新 8/100，新增完整独立估值池内 0/100。逐股新增来源时间、研究深度、状态及下次核验字段，历史数据列保留。[当晚比较及来源](reviews/2026-11-13_EVENING_OPERATION_PLAN.md)

- **NU，11/13 首次初筛，拉美零售金融。** 11/12 公司原报第三季 IFRS 净利约 US$1.1bn，汇率中性同比 +31%，存款 US$47.5bn。90 日以上逾期率 7.3%，前季 6.9%。贷款增长有真实盈利，存款为负债；跨实体资本、信用成本、汇率与可分配资本尚未核成统一估值。盘前样本 06:49 EST；留研究，下一次先看巴西等子公司资本、贷款批次和实际拨备。[公司原报](https://nu.com/en/newsroom/company/nu-holdings-ltd-reports-third-quarter-2026-financial-results) · [行情](https://stockanalysis.com/stocks/nu/)
- **CBRS，11/13 首次初筛，AI 计算。** 11/12 10-Q 披露客户协议，Microsoft 条款和现金兑现仍待披露。前三季经营现金 −US$388.9m 对 −US$134.2m，扣现金设备开支后约 −US$1.435bn 对 −US$435.4m，均未额外扣 SBC；同一现金流表的 SBC US$541.7m 对 US$33.8m。收入增长与客户融资风险同在。盘前样本 06:32 EST；本轮排除新增，核已付款、设备投产和稀释。[10-Q](https://investors.cerebras.ai/static-files/9c021f1a-3cc4-44b6-97fa-ef1a4ad2e0d8) · [公司原报](https://investors.cerebras.ai/news-releases/news-release-details/cerebras-systems-delivers-record-revenue-third-quarter-2026) · [行情](https://stockanalysis.com/stocks/cbrs/)
- **旧线索推进。** GIB 新做两档独立现金及折现率敏感度。CSCO 和 AMAT 沿昨晚已做的现金桥按新报价重算收益率。YETI、EPC、BALL、CTVA 仍分别待节日回款、剥离税费、季节性营运资金回收及分拆后的资本结构。全池 100 个唯一代码，未取得足以用 NU 或 CBRS 替换成员的证据。研究顺序 GIB、NU、CSCO、AMAT、ADBE。可执行新增为空。[前次现金桥](journal/2026-11-12_OPERATION_REASON_LOG.md)
