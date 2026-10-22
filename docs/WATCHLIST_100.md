# 100隻美股機會觀察池

版本：2026年10月22日，北京時間，覆蓋修訂。100個獨立個股代碼。所有已核實的現持個股必須在池內，其餘名額供替代候選；個人持倉核對、基金及帳戶資料僅見私人記錄，公開池不標示持倉。

本池尚無通過完整新增資金審查的股票。33隻常規觀察、40隻事件觀察、26隻估值觀察、1隻資料待核。類型表示研究方向，不是收益排名；新增資金資格和現持操作結論分開，待覆核不能冒充繼續持有建議。

[完整逐股CSV](../data/watchlists/universe_100_20261022.csv)保留機會、風險、驗證點、來源日期和資料缺口。`new_money_action`僅描述新增或加倉推薦資格，取代容易被誤解為全持倉操作的`current_action`。持倉覆核須按[完整流水線](STOCK_SELECTION_PIPELINE.md)與[逐次模板](STOCK_REVIEW_TEMPLATE.md)另作結論。

## 覆蓋與機會成本比較

1. 每輪從私人持倉快照做代碼集合核對，現持個股零遺漏；記錄價格日期、未同步交易與缺項。基金另列，仍納入全帳戶風險。
2. 持有只保證研究覆蓋。每隻現股都要以今天價格說明繼續配置資金的正面理由，與最強合格替代者做同額、同期限比較，計入稅費、下行情景和集中度。
3. 替代方案扣除成本後有穩健淨改善，才提出換出及換入方案。排名落後不自動賣出；未完成比較標為待覆核，不能默認繼續持有。
4. 重大未核清風險凍結新增資金推薦，事件台帳持續承接。已持有不能解除限制，凍結也不機械推出賣出。
5. 不宣稱100隻已完成全部新聞、估值與分析師研究，也不宣稱證明全市場最優。記錄維護方法不等於已設定自動監控。

## 本次成員修訂

為修正研究覆蓋而調整12個名額；這是研究範圍修訂，沒有完成原成員與新增成員的投資優劣排序。原12隻保留於[備選留檔CSV](../data/watchlists/reserve_20261022.csv)：BLK、AJG、SPGI、AME、PH、MTZ、AON、KKR、NDAQ、AMGN、EW、CPRT。六隻原為資料待核，另六隻保留事件追蹤。任何有效風險不因移出基礎池而解除。

## 研究進度與共同風險

每行如實保留深度和缺項。未逐一完成全部10-K、案卷、近30日新聞、券商原研報和估值情景；舊有88條資料沿用上一版來源，本次未冒充已重新全面更新。新增12條補做官方經營來源和事件初核，仍需估值及替代比較。價格快照與財報發布時點分開，私人表新增成員價格空白表示未補取，不能推算即時收益或下單價。

行業不同不代表風險獨立。資料中心與電網資本開支、金融市場資產價格、政府預算及醫療政策等共同因素須合併評估。

## 逐股觀察

### 金融

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [JPM JPMorgan Chase](https://jpmorganchaseco.gcs-web.com/static-files/71d42762-a4d9-435b-9486-b7327e378dca) | 常規觀察 | Q3净利息收入同比增长13%，贷款、支付和资本市场业务可共同提供盈利来源；观察存款与信贷质量能否支持持续回报。 下一步：下一次经营更新核净息差、存款成本、坏账与资本回报；用ROTCE和有形净资产估值比较。 | 信贷与资本市场周期；Q3报告EPS与剔除显著项目后EPS不同，不能把一次性项目正常化错配。 |
| [BAC Bank of America](https://investor.bankofamerica.com/regulatory-and-other-filings/select-sec-filings/content/0000070858-26-000481/bac09302026ex991.htm) | 事件觀察 | 固定利率资产重定价与净利息收入恢复提供经营改善线索，但必须先评估新监管处罚和整改。 下一步：先核OCC整改范围、持续成本与业务限制；重算正常化盈利后再做估值。 | OCC于10月13日就BSA/AML缺陷处以7.5亿美元民事罚款，2024停止令仍要求整改；新监管影响未量化。 |
| [GS Goldman Sachs](https://www.sec.gov/Archives/edgar/data/886982/000088698226000529/a3q26gsearningsresults.htm) | 常規觀察 | Q3投行费用同比增长21%，并购与股权融资恢复可提供经营杠杆，资产管理提高经常性收入占比。 下一步：核投行积压订单、费用收入和资产管理经常收益，避免把高交易季度直接年化。 | 投行与交易周期波动；公司Q3投行费用积压订单较Q2下降，盈利强不代表后续订单继续加速。 |
| [MS Morgan Stanley](https://www.sec.gov/Archives/edgar/data/895421/000089542126000288/a3q26msearningsrelease.htm) | 常規觀察 | Q3财富管理与机构业务共同带动收入增长，观察客户资产转为收费资产及持续利润率的能力。 下一步：核净新增资产、收费型资产流入和财富管理利润率；与交易收入波动分开。 | 权益市场下跌会影响资产管理收费和交易活动；高股价不能仅靠单季ROTCE外推。 |
| [IBKR Interactive Brokers Group](https://ndcdyn.interactivebrokers.com/mkt/getFileNew.php?file=2026Q3_Earnings_Release.pdf) | 常規觀察 | Q3客户账户同比增长35%、佣金收入增长12%，全球低成本平台的新增客户有待转为长期利润。 下一步：按月看账户、客户资产与DARTs；核降息下利息收入和保证金融资风险。 | 利息收入占比高、保证金贷款增长快；交易量和监管费用转嫁影响收入质量，需检查系统与合规风险。 |
| [AMP Ameriprise Financial](https://www.sec.gov/Archives/edgar/data/820027/000082002726000038/q22026er.htm) | 常規觀察 | Q2调整经营EPS同比增长22%，收费型财富业务与资产增长带来经营杠杆。 下一步：10月29日Q3经营资料核净流入、顾问生产力及资产管理净流出；另核当前估值。 | 市场下跌会压低收费资产；保险及衍生品估值使GAAP与调整经营利润存在差异。 |
| [BNY The Bank of New York Mellon](https://www.bny.com/content/dam/bnymellon/documents/pdf/investor-relations/earnings/earnings-press-release-3q-2026.pdf) | 常規觀察 | Q3收费收入同比增长12%，托管规模与平台效率改善可支持经常性盈利增长。 下一步：看托管收费、有机客户拓展、费用增长和资本比率；核增长是否依赖市场价格上涨。 | 市场水平、利率和客户资产变动影响收费；Q3杠杆及CET1资本比率同比下降，需要检查资本缓冲。 |
| [TROW T. Rowe Price](https://www.troweprice.com/en/us/press/2026/press-release--t--rowe-price-group-reports-month-end-assets-unde6) | 事件觀察 | 若退休金与主动管理资金流出稳定，费用控制和现有资产规模可能带来修复机会；目前尚未见流出拐点。 下一步：10月29日Q3核净流出结构、目标日期基金及费用率，不以市场上涨掩盖净流出。 | 9月净流出122亿美元、Q3净流出283亿美元；主动管理份额流失和收费压力持续。 |
| [CB Chubb](https://news.chubb.com/2026-10-20-Chubb-Reports-Third-Quarter-Per-Share-Net-Income-and-Record-Core-Operating-Income-of-7-30-and-7-66,-Respectively,-Up-4-4-and-0-8-Consolidated-Net-Premiums-Written-of-15-1-Billion,-Up-1-9-,-with-P-C-and-Life-Insurance-Up-1-9-and-1-4-P-C-Combined) | 估值觀察 | 承保纪律、投资收入及地域分散支持防守型中线观察，重点是有形账面价值长期复利。 下一步：核费率软化、灾损和准备金释放后可持续ROE；按重述后核心盈利及账面价值估值。 | Q3承保利润下降、灾损增加；Q3起核心盈利定义排除部分购入无形资产摊销，前期已重述，不能错配同比。 |
| [CME CME Group](https://www.cmegroup.com/media-room/press-releases/2026/10/21/cme_group_inc_reportshighestq3revenueonrecordforq32026.html) | 估值觀察 | 利率、外汇、商品避险需求转为交易与清算收费，Q3收入与净利双位数增长。 下一步：核交易量与每合约收入、费用，以及perpetual futures竞争和对CFTC诉讼最新裁定；估值给足补偿。 | 成交量可能由异常波动拉动而非永久增长；新永续合约竞争与诉讼边界未完整核清，CME是原告而非被调查方。 |
| [ICE Intercontinental Exchange](https://ir.theice.com/press/news-details/2026/Intercontinental-Exchange-to-Acquire-MarketAxess-Creating-a-Premier-Fixed-Income-Marketplace/default.aspx) | 事件觀察 | 债券电子化与MarketAxess数据协同有扩张潜力，现有数据订阅可降低纯交易量依赖。 下一步：核MarketAxess审批及10月29日HSR等待期进展，按收购后债务、利息与协同重算。 | 现金收购约60亿美元股权价值、约57亿美元EV，计划新增债融资；HSR重报不等于审批已完成。 |
| [V Visa](https://s1.q4cdn.com/050606653/files/doc_financials/2026/q3/Q3-2026-Earnings-Release_vF.pdf) | 事件觀察 | 支付电子化、跨境和增值服务提供长期量价增长，FYQ3净收入增长14%；先核核心反垄断案件影响。 下一步：10月27日财报核支付量、跨境、客户激励及诉讼情景；法律风险未核清不进入买入排名。 | DOJ借记卡垄断诉讼仍需持续承接；费率、激励和网络排他条款变化可能影响核心业务。 |
| [MA Mastercard](https://s25.q4cdn.com/479285134/files/doc_financials/2026/q2/2Q26-Mastercard-Earnings-Release.pdf) | 事件觀察 | Q2收入增长14%，跨境支付与数据、安全增值服务扩展，值得跟踪增长质量。 下一步：核交易量、跨境与服务增长，以及BVNK等资本配置；先量化核心商户费率诉讼边界。 | 持续商户交换费反垄断诉讼、网络规则与监管变化；现有材料未完成责任及费率影响测算。 |
| [MCO Moody's](https://www.sec.gov/Archives/edgar/data/1059556/000162828026066594/a3q26earningsrelease.htm) | 估值觀察 | Q3 Analytics有机恒汇率收入增长8%、ARR增长8%，订阅分析业务可部分平滑债券评级周期。 下一步：核Ratings交易收入恢复、Analytics续约与现金增长；按10月21日重申全年指引估值。 | Q3总收入仅增1%、评级交易收入降5%，调整EPS增长仅6%；不能沿用Q2高增长叙事。 |
| [DFIN Donnelley Financial Solutions](https://investor.dfinsolutions.com/press-releases/news-details/2026/DFIN-Reports-Second-Quarter-2026-Results/default.aspx) | 事件觀察 | 由印刷向軟體轉型；Q2軟體收入增7.8%，佔總收入44.3%，ActiveDisclosure約增29%，現金流改善。 下一步：10月29日盤前Q3；核對軟體有機增長、訂閱續約、交易收入及印刷萎縮能否抵銷，再比較ADP、PAYX或其他軟體服務的前瞻回報。 | 總收入僅增2.8%，印刷收入降15%；交易業務依賴IPO及併購環境，回購使EPS增長快於淨利。 |
| [AXS AXIS Capital Holdings](https://www.sec.gov/Archives/edgar/data/1214816/000121481626000201/q22026pressrelease.htm) | 事件觀察 | 專業險承保及每股帳面值增長；Q2帳面值每股80.67美元、同比增14.7%。 下一步：2026-10-28盤後Q3財報及10-29電話會議：剔除災害的承保質量、準備金變動、費率和每股帳面值。 | Q2營運收益同比下降19%、承保收益下降24%，綜合成本率93.1%；災害、戰爭承保、準備金及保費競爭可能壓縮回報。 |
| [SCHW The Charles Schwab Corporation](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Schwab-Delivers-Record-Net-New-Assets--Earnings/default.aspx) | 估值觀察 | 客戶資產、淨流入及財富管理規模增長；Q3核心淨新增資產1904億美元，調整EPS1.69美元。 下一步：把Q3淨息差3.04%、存款和融資結構、正常化EPS與同額替代者估值比較。 | 利率、存款遷移、淨息差、融資與市場活躍度；好財報不自動代表現價比IBKR、AMP等更值得持有。 |
| [BRK.B Berkshire Hathaway Class B](https://www.berkshirehathaway.com/qtrly/2ndqtr26.pdf) | 估值觀察 | 保險浮存金與多元經營現金流、資本配置；Q2營運收益129.83億美元，並回購約45億美元股票。 下一步：核對Q3公告日、正常化營運收益、GEICO損失率、資本部署及相對估值。 | Q2保險承保和投資收益同比下降；GEICO理賠頻率與嚴重程度上升。須分離未實現投資收益、匯率及其他項目，不能按表面EPS倍增推論核心盈利倍增。 |

### 醫療

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [JNJ Johnson & Johnson](https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q3-2026-results-raises-2026-guidance/default.aspx) | 事件觀察 | Tremfya等新药增长及骨科业务重组有望改善业务组合，适合观察新产品能否覆盖专利到期压力。 下一步：核滑石粉拟和解的批准、剩余责任和骨科分拆后现金流；再验证创新药与MedTech增长。 | 10月13日Q3含滑石粉拟解决方案特别费用；拟和解未等于全部诉讼责任消失，海外MedTech增长偏弱。 |
| [MRK Merck & Co.](https://www.merck.com/news/merck-highlights-key-regulatory-and-clinical-milestones-across-broad-diverse-pipeline/) | 常規觀察 | Keytruda QLEX皮下注射剂与Winrevair等新品可延长核心肿瘤业务的现金创造，并提供专利到期前的产品替代路径。 下一步：核QLEX采用率、新品销售和研发结果对2028年后现金流的覆盖；剔除收购IPR&D后统一盈利口径。 | Keytruda专利集中度高，Gardasil需求与临床结果存在波动；大额收购费用使表面EPS不可直接估值。 |
| [ABBV AbbVie](https://news.abbvie.com/2026-07-31-AbbVie-Reports-Second-Quarter-2026-Financial-Results) | 常規觀察 | Skyrizi和Rinvoq已成为接替Humira的实际销售增长来源，神经科学产品也可扩大盈利基础。 下一步：核两大新药增量、Apogee收购后的研发支出及资金占用，再测可持续EPS与现金流。 | Humira仍衰退；Apogee收购新增资金及临床兑现风险，不能把并购费用造成的指引变动当纯经营恶化或全部忽略。 |
| [GILD Gilead Sciences](https://www.gilead.com/news/news-details/2026/gilead-sciences-announces-second-quarter-2026-financial-results) | 常規觀察 | HIV基本盘、长效lenacapavir预防用药及肝病产品可支持增长；观察新药实际可及性如何转为收入。 下一步：核HIV新品处方和支付覆盖、收购后资金回报及细胞治疗业务是否止跌。 | Arcellx等收购产生巨额IPR&D，GAAP和调整后利润均需逐项重建；细胞治疗受竞争挤压，长效HIV药的定价及可及性受关注。 |
| [REGN Regeneron Pharmaceuticals](https://investor.regeneron.com/news-releases/news-release-details/regeneron-reports-second-quarter-2026-financial-and-operating) | 常規觀察 | Dupixent增长、Eylea HD替代与Libtayo扩张提供多条商业化路径，可观察高剂量眼科产品是否稳定总眼科收入。 下一步：核Eylea新旧剂量合计销售、Dupixent分成与新适应证、产品供应和审批进展。 | 眼科竞争、生物类似药及供应链审批旧问题仍需持续核；合作方确认的全球销售不能直接当REGN营收。 |
| [VRTX Vertex Pharmaceuticals](https://investors.vrtx.com/news-releases/news-release-details/vertex-reports-second-quarter-2026-financial-results) | 常規觀察 | 囊性纤维化现金流可为Journavx、Casgevy及肾病管线商业化提供资金，观察非CF收入占比提升。 下一步：核非CF产品实际收入与付费患者、肾病审批/试验数据，以及Crinetics交易最新状态和资金成本。 | 新产品销售起步及支付渠道兑现有不确定性；CF集中度仍高，不能把管线潜在市场算成当期收入。 |
| [LLY Eli Lilly](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-second-quarter-2026-financial-results-raises-full) | 估值觀察 | Mounjaro和Zepbound销量扩张及口服/下一代产品可扩大可服务人群，已有商业销售支撑增长逻辑。 下一步：核销量、净售价、产能利用率及医保覆盖后的净利润增量，等待与持续盈利相称的价格。 | Q2强劲销量同时伴随实现价格下滑；估值、支付政策、竞品和安全标签均可使增长股回撤。第三方调配药召回不能误归为Lilly原厂药召回。 |
| [NVO Novo Nordisk](https://www.sec.gov/Archives/edgar/data/353278/000035327826000023/caq22026.htm) | 事件觀察 | Wegovy和Ozempic已有大规模业务，若价格、处方和新品竞争改善，有利润修复机会。 下一步：核剔除340B与减值后的同口径销售、美国净价/份额及全年指引执行，确认修复再估值。 | 竞争与净价压力明显；调整后增长与报告利润受340B比较基数及管线减值影响，不能以低表面倍数跳过修复验证。 |
| [MDT Medtronic](https://news.medtronic.com/2026-09-01-Medtronic-reports-first-quarter-fiscal-2027-results-delivers-broad-based-portfolio-performance-and-raises-fiscal-2027-guidance) | 常規觀察 | 心脏消融PFA和较新产品驱动心血管增长，若收入结构升级能改善利润，可成为器械复苏候选。 下一步：核FY2027新指引兑现、PFA份额及毛利、机器人投资回报；增长比较要剔除53周额外周。 | 关税与退款、器械召回和新平台竞争；大额机器人投资尚非确定利润。 |
| [SYK Stryker](https://s22.q4cdn.com/857738142/files/doc_financials/2026/q2/Q2-26-Earnings-Press-Release-07-30-2026.pdf) | 事件觀察 | 骨科手术、机器人与MedSurg产品可支持量增；网络事件后运营修复提供跟踪窗口。 下一步：核网络攻击后的生产、供应与订单恢复、额外费用和责任边界，再验证有机增长与现金回款。 | 3月网络攻击有持续恢复事项；Q2反弹不能等同所有客户及财务损失已结清。 |
| [BSX Boston Scientific](https://news.bostonscientific.com/2026-07-29-Boston-Scientific-announces-results-for-second-quarter-2026) | 事件觀察 | FARAPULSE与Watchman的长期渗透仍可扩张，若增长重置后趋稳，有重新评估空间。 下一步：核Watchman独立手术及联合手术需求、竞争与利润指引是否止降；估值以重置后持续盈利计算。 | 7月再次下调全年销售/盈利指引，Watchman及电生理需求受压；重组成本和诉讼调整不能省略。 |
| [ISRG Intuitive Surgical](https://isrg.intuitive.com/news-releases/news-release-details/intuitive-announces-third-quarter-earnings-6) | 事件觀察 | da Vinci 5升级、耗材及租赁装机基础可形成持续收入，Ion也有手术量增长。 下一步：核4.5亿美元反垄断拟和解获批及禁令救济条款对售后经济性的影响，再看手术增速与资本开支。 | 10月20日Q3披露新拟和解费用且待法院批准，财报明确还含关税退款；不能只看22%收入增速。 |
| [DHR Danaher](https://investors.danaher.com/2026-10-21-Danaher-Reports-Third-Quarter-2026-Results?asPDF=) | 事件觀察 | 生物工艺需求恢复及诊断业务可支持中期增长，需观察耗材需求的持续性。 下一步：先核Abcam抗体验证数据争议及整改；再验证剔除呼吸道收入后的增长与并购后现金回报。 | Abcam在抗体验证图片公开质疑中被涉及，仍需原始数据/独立核验；Q4总体核心增长约3%也不支持忽略估值。 |
| [TMO Thermo Fisher Scientific](https://ir.thermofisher.com/investors/news-events/news/news-details/2026/Thermo-Fisher-Scientific-Reports-Third-Quarter-2026-Results/default.aspx) | 事件觀察 | 实验耗材、仪器和药物研发服务的多元收入及Q3有机复苏，提供中期业务研究价值。 下一步：先取得可复核抗体验证原始数据、整改/独立核验与客户影响边界；解除风险后再看价格及现金流。 | 抗体验证图片存在具体公开质疑，公司否认操纵/造假但仍审查与重新标注；Q3强劲和价格下跌都不解除门槛。 |
| [ABT Abbott Laboratories](https://www.sec.gov/Archives/edgar/data/1800/000162828026066601/abt-2026q3xexhibitx991.htm) | 事件觀察 | Libre糖尿病监测、结构性心脏器械和癌症诊断可形成增长组合，分拆后或改善业务聚焦。 下一步：按10月21日新销售增速指引重算盈利，并厘清营养业务分拆中的法律责任、债务及现金流。 | 最新销售增速下修；营养业务拟分拆及重大诉讼责任分配尚待核，不因低倍数直接加仓。 |
| [ZTS Zoetis](https://investor.zoetis.com/news/news-details/2026/Zoetis-Announces-Second-Quarter-2026-Results/default.aspx) | 事件觀察 | 宠物长期医疗需求与新药平台仍有业务基础，若客流和产品需求恢复，可观察盈利修复。 下一步：核下调指引后美国宠物客流、Librela需求、安全信息和经营收入是否见底，再重估。 | Q2大幅下调全年营收与EPS指引，宠物业务、价格敏感和竞争承压；不能把跌价当解冻。 |
| [MEDP Medpace Holdings](https://investor.medpace.com/node/13171/pdf) | 事件觀察 | 生物科技融资和药企研发可转成临床订单，观察净新增订单与取消率能否支撑未来收入。 下一步：核取消率、订单口径及相关披露诉讼最新公司/法院材料；再验证积压订单转收入和盈利质量。 | 持续的取消率/订单披露证券诉讼指控未核清，不能当已证实造假；新季度增长放缓及估值要求也需重算。 |
| [IQV IQVIA Holdings](https://ir.iqvia.com/press-releases/press-release-details/2026/IQVIA-Reports-Second-Quarter-2026-Results/default.aspx) | 事件觀察 | 医药数据、商业分析和临床服务具有客户持续使用价值，若数据来源合法性与临床订单改善，可重新比较。 下一步：先核意大利受影响数据集、客户收入、120日整改和其他地区外溢影响，再估值。 | 意大利监管认定健康数据并非真正匿名，罚700万欧元并要求整改，GP数据传输已暂停；关键是商业化持续性。 |
| [CVS CVS Health](https://www.cvshealth.com/news/company-news/aetna-2027-star-ratings-reflect-strong-clinical-quality-and-member-experience.html) | 事件觀察 | Aetna保險盈利修復及藥房現金流；Q2上調全年指引，醫療福利比率87.4%。 下一步：2026-11-04 08:00ET Q3電話會議：醫療利用率、2027會員與定價、星級獎金影響及修復指引。 | 醫療成本、PBM政策、Medicare重定價與星級獎金；2027年4星以上計劃會員比例為逾69%，須量化相對前期下降及對未來獎金的影響。 |

### 工業與服務

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [DOV Dover](https://www.dovercorporation.com/china/in-the-news/post/2026/07/23/dover-reports-second-quarter-2026-results) | 常規觀察 | Q2有機收入增5%、調整EPS增12%，五個板塊均有機增長；訂單轉收入可提供中線盈利催化。 下一步：10月22日美股盤前新財報，核訂單轉收入、現金回款與全年指引；依新數據重估。 | 工業需求與客戶資本開支放緩；今晚新數據尚未發布，不能沿用7月指引直接買入。 |
| [ROP Roper Technologies](https://www.ropertech.com/node/19171/html) | 常規觀察 | Q2有機收入增5%、調整自由現金流增11%；關鍵行業工作流程與經常性收入值得持續觀察。 下一步：10月22日盤前財報及08:00美東電話會；核有機增長、續約、AI競爭和每股現金流。 | Indicor投資重估抬高GAAP盈利；調整EPS受回購影響，不能把低表面PE當便宜證據。 |
| [ITW Illinois Tool Works](https://investor.itw.com/news-and-events/news/news-details/2026/ITW-Reports-Second-Quarter-2026-Results-and-Raises-Full-Year-2026-Guidance/default.aspx) | 常規觀察 | Q2有機增長4.5%、營業利潤率26.7%，分散的利基工業業務適合觀察定價及現金韌性。 下一步：新季度驗證有機增長、各板塊利潤率及自由現金流；重新比較價格與盈利增速。 | 周期需求與估值；10月12日JPMorgan降至Neutral的具名轉述提供反方，不能只看上調全年指引。 |
| [EMR Emerson](https://ir.emerson.com/news-events/press-releases/detail/642/emerson-reports-third-quarter-2026-results-raises-2026-outlook) | 常規觀察 | FYQ3基礎訂單增7%、自由現金流增36%；軟件與系統訂單及自動化投資可支持盈利。 下一步：核新年度有機增長、軟件整合後現金流與去槓桿，區分收購收入和持續增長。 | 大型收購後槓桿、軟件整合及工業項目延遲；中東風險不能忽略。 |
| [ETN Eaton](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000027/etn06302026exhibit99.htm) | 估值觀察 | Q2有機收入增14%，電氣板塊訂單及積壓快速增長；電網與數據中心電力設備有真實交付需求。 下一步：核訂單取消條款、交付與現金回款，並以保守增長重新檢驗當前估值。 | AI與電網資本開支共同因子、擴產和交付壓力；Mobility分拆交易尚有執行風險。 |
| [HUBB Hubbell](https://hubbell.gcs-web.com/news-releases/news-release-details/hubbell-reports-second-quarter-2026-results) | 估值觀察 | Q2有機收入增10%，公用電網現代化與負載增加支持需求；耗材及關鍵零件比單一機房項目分散。 下一步：核新增產能的收入及現金兑现、價格成本差與收購融資，再定估值補償。 | 調整營業利潤率同比下降50基點；收購、通脹和電力資本開支周期可能抵消高收入增長。 |
| [IR Ingersoll Rand](https://investors.irco.com/news/news-details/2026/Ingersoll-Rand-Reports-Second-Quarter-2026-Results/default.aspx) | 常規觀察 | Q2收入增9%，工業技術服務有機收入增4%；壓縮機、服務和流體設備提供工業復甦觀察點。 下一步：驗證有機訂單由持平轉強，價格能否抵消通脹，以及併購後現金回收。 | 主要工業板塊有機訂單約持平、調整利潤率下降180基點；總收入增長部分來自收購。 |
| [XYL Xylem](https://www.xylem.com/en-al/resources/press-releases/xylem-reports-second-quarter-2026-results/) | 常規觀察 | Q2有機訂單增41%、調整EPS增16%；水務、工業用水與效率升級可提供長周期需求。 下一步：核高訂單是否按期轉收入；比較上調EPS與下調收入指引能否同時成立。 | Q2有機收入僅增1%，全年有機收入指引從2–4%縮至2–3%；不可只報訂單與盈利改善。 |
| [J Jacobs Solutions](https://www.sec.gov/Archives/edgar/data/52988/000162828026052563/jfy2026q3earningsrelease.htm) | 事件觀察 | FYQ3調整淨收入增8.3%、調整EPS增13.6%；水務、交通、能源與先進設施業務值得保留研究。 下一步：先排除Milwaukee未簽項目，核法律進展、PA收購後負債和FY2027現金轉換。 | Milwaukee客戶明確等Veolia法律挑戰解決才簽約，預計2028年啟動；Qatar舊民事訴訟也需持續帶入，不能以獲選等同生效訂單。 |
| [ACM AECOM](https://investors.aecom.com/news-releases/news-release-details/aecom-reports-third-quarter-fiscal-2026-results) | 事件觀察 | FYQ3積壓增13%、設計業務淨服務收入增長；若工程損失邊界清晰，核心設計业务有重新估值可能。 下一步：先核建造管理項目剩餘成本、追索與現金流，再依新指引重算；風險未清前不進買入比較。 | FYQ3確認3.37億美元項目費用、GAAP虧損，經營現金流下降66%；全年指引已更新反映損失和更低NSR增長。 |
| [PWR Quanta Services](https://www.prnewswire.com/news-releases/quanta-services-reports-second-quarter-2026-results-302838646.html) | 估值觀察 | Q2積壓達534億美元、經營現金流約11億美元；輸配電及能源工程有可見訂單。 下一步：拆開有機與收購增長，核RPO轉收入、項目毛利與現金回款，再按保守訂單周期估值。 | 大額積壓不等於當期利潤；收購整合、技工產能及數據中心資本開支共振增加風險。 |
| [STRL Sterling Infrastructure](https://www.prnewswire.com/news-releases/sterling-reports-record-second-quarter-results-and-raises-full-year-2026-guidance-302841538.html) | 估值觀察 | Q2收入與盈利高速增長，數據中心配套施工與整合平台提供訂單兑现機會。 下一步：把收購貢獻與有機增長分開，核客戶集中度、訂單取消與營運資金，避免靠表面高增長追價。 | Q2收入增90%含2.508億美元收購貢獻；AI建設周期、項目集中和回款風險，需估值壓力測試。 |
| [TT Trane Technologies](https://www.sec.gov/Archives/edgar/data/1466258/000162828026050743/exhibit991-q22026earningsr.htm) | 估值觀察 | Q2有機訂單增37%、有機收入增9%；商用HVAC、節能改造與冷卻需求提供盈利動力。 下一步：核高訂單向交付、持續利潤率與現金回收轉化；另檢驗當前估值對增長預期的容忍度。 | Q2調整營業利潤率下降60基點；產能、產品組合及數據中心需求預期可能壓縮安全邊際。 |
| [OTIS Otis Worldwide](https://s203.q4cdn.com/227649559/files/doc_financials/2026/q2/2Q26-Otis-Earnings-Release.pdf) | 事件觀察 | Q2服務有機銷售增9%、現代化訂單增9%；存量電梯維修升級有經常性收入。 下一步：先核全年盈利下修後的服務投資與成本、價格傳導，等待利潤率和現金流證明修復。 | 全年調整EPS指引下調至4.01–4.05美元（此前4.20–4.24）；勞工成本、新梯尤其中國需求承壓。 |
| [WM Waste Management](https://mediaroom.wm.com/2026-07-28-WM-Announces-Second-Quarter-2026-Earnings) | 常規觀察 | Q2收入增4%、自由現金流增34.5%；定價、自動化、醫療廢物整合和再生能源項目帶來現金改善。 下一步：核剔除能源附加費及去年山火清理基數後的量價、醫療業務協同及債務下降。 | 收集處置量下降1.8%；低毛利業務退出、燃料成本及醫療業務整合可能影響現金兑现。 |
| [RSG Republic Services](https://investor.republicservices.com/news-releases/news-release-details/republic-services-inc-reports-second-quarter-2026-results) | 常規觀察 | Q2收入增4.6%，定價超成本、上調全年指引；路線密度與定價可支撐較穩定現金。 下一步：核量價、收購後現金回報、勞工與環境成本，並與WM同口徑比較估值及增長。 | 總量拖累收入1.6%、環境解決方案收入下降；併購、環保責任與勞工成本仍需核查。 |
| [FAST Fastenal](https://investor.fastenal.com/news/news-details/2026/Fastenal-Company-Reports-2026-Third-Quarter-Earnings/default.aspx) | 估值觀察 | 10月14日Q3收入增15.5%、營業利潤率升至21.5%；大客戶、現場供應與自動售貨帶動份額提升。 下一步：逐月日均銷售驗證製造業量增，核新增據點資本開支後現金回報及大客戶組合。 | 大客戶組合壓毛利，價格成本仍拖累；關稅退款與供應商返利含時點效應，高增長需要估值補償。 |
| [R Ryder System](https://newsroom.ryder.com/news/news-details/2026/Ryder-Reports-Second-Quarter-2026-Results/default.aspx) | 事件觀察 | 合約型車隊及供應鏈收入增加，二手車市場改善；2026Q2營運收入增3%，可比EPS增12%。 下一步：先核對10月22日盤前Q3正式業績及全年指引，再看二手車售價、租賃利用率、供應鏈利潤與正常化自由現金流。 | 貨運及二手車價格週期；Q2專用運輸營運收入降3%，供應鏈稅前利潤降7%；10月22日財報可能改變舊指引。 |
| [OSIS OSI Systems](https://investors.osi-systems.com/news-releases/news-release-details/osi-systems-reports-fiscal-2026-fourth-quarter-and-fiscal-year) | 事件觀察 | FY2026年底訂單積壓約19億美元；FY2027公司預期收入增5.0%至8.1%，醫療部門盈利改善。 下一步：10月29日16:30 ET FY2027Q1會議；核對延遲訂單交付、應收款、現金流、FY2027指引及估值安全邊際。 | 中東衝突已令交付延後，FY2026Q4收入降4%；政府採購、驗收及收款使季度收入和現金流波動。 |
| [HII Huntington Ingalls Industries](https://www.sec.gov/Archives/edgar/data/1501585/000150158526000045/hii2026q2earningsrelease.htm) | 事件觀察 | 海軍造船訂單積壓及產能改善；Q2上調全年造船收入和利潤率指引。 下一步：2026-10-29 Q3財報：吞吐量改善、造船利潤率、現金流及全年指引。 | 訂單能否轉化為現金；Q2自由現金流為負1.50億美元，造船人力、交付和成本執行仍需檢查。 |

### 科技

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [GOOGL Alphabet](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/googexhibit991q22026.htm) | 事件觀察 | Google Cloud与订阅业务增长，观察AI搜索能否在广告之外形成可持续利润。 下一步：10月28日财报核搜索变现、云利润、资本开支与剔除投资重估后的现金回报。 | 美国广告技术补救措施及欧盟监管可能改变数据共享和收费；投资重估与AI资本开支会扭曲表面PE。 |
| [AMZN Amazon](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/) | 事件觀察 | Q2 AWS收入增长37%，零售效率和广告业务可与云业务共同提升经营利润。 下一步：10月29日财报验证AWS增长、经营利润及资本开支后的自由现金流。 | TTM自由现金流为负，利润含巨额投资收益；FTC电商垄断诉讼持续，不能用GAAP低PE直接判断便宜。 |
| [MSFT Microsoft](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) | 事件觀察 | Azure与企业软件订阅形成重复收入，Q4经营利润同比增长18%；观察Copilot付费转化。 下一步：10月28日财报核Azure订单兑现、AI投入后的自由现金流和折旧。 | CMA 10月16日拟将商业软件生态认定为战略市场地位，捆绑和互操作可能受约束；AI资本开支和OpenAI敞口。 |
| [META Meta Platforms](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) | 事件觀察 | Q3广告收入仍强，AI推荐与广告工具可能提高变现效率。 下一步：先核10月21日新财报、New Mexico判决及上诉、法律现金支出和新股类别安排。 | 10月21日报道250亿美元隐私判决；Q3还含重大法律费用、自由现金流压力和高AI资本开支。 |
| [ORCL Oracle](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx) | 事件觀察 | FY2027 Q1云基础设施收入三位数增长，数据库客户迁云及AI合同可形成未来收入。 下一步：核RPO交付、客户集中度、客户预付款、资本开支与债务融资的匹配。 | 订单不是利润；巨额资本开支与现金流缺口、少数AI客户偿付能力可能削弱股东回报。 |
| [CRM Salesforce](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/default.aspx) | 事件觀察 | cRPO增长与Agentforce收费可能提高现有客户价值，观察增长能否转为每股现金流。 下一步：更新Braze收购后的债务、稀释和协同假设，区分Informatica并表与有机增长。 | 10月20日新收购尚未完成独立测算；股权薪酬和AI替代传统席位收费会影响收益。 |
| [ADBE Adobe](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm) | 常規觀察 | AI-first ARR和庞大创意用户群提供变现空间，观察免费用户能否升级付费。 下一步：核新增ARR、付费转化、流失率和管理层交接后的指引兑现。 | AI竞争与免费策略可能压低定价；10月12日Wells Fargo双重降级，不能以低倍数盖过增长疑问。 |
| [INTU Intuit](https://investors.intuit.com/news-events/press-releases/detail/1327/intuit-to-acquire-ai-native-revenue-management-platform-sequence) | 常規觀察 | QuickBooks在线生态的客户增长、定价与支付工资服务交叉销售，提供重复收入扩张机会。 下一步：核FY2027有机增长、Mailchimp修复和Sequence收购条款，检查新增产品是否挤压原税务业务。 | 10月15日Sequence收购对价及贡献需核；AI竞争、税务免费服务变化和Credit Karma周期影响利润。 |
| [ADP Automatic Data Processing](https://investors.adp.com/news/news-details/2026/ADP-Reports-Fourth-Quarter-and-Fiscal-2026-Results/default.aspx) | 常規觀察 | 云端HCM升级、客户留存和工资处理的重复收入，提供较稳定的企业服务观察方向。 下一步：10月28日FY2027 Q1核新签约、留存、每客户员工数与客户资金收益。 | 就业走弱拖累工资处理量，利率下降影响客户资金收益；较高估值可能吞噬经营增长。 |
| [PAYX Paychex](https://investor.paychex.com/news-events/press-releases/detail/850/paychex-reports-first-quarter-fiscal-2027-results) | 常規觀察 | Q1 FY2027收入增长6%，PEO与保险收入增长12%；交叉销售可提高每客户收入。 下一步：验证收入增长能否持续、客户流失与就业量、Paycor整合及每股现金流。 | 增长低于前季且全年指引未提高；中小企业就业、整合费用和客户资金利率敏感。 |
| [CSCO Cisco Systems](https://investor.cisco.com/news/news-details/2026/CISCO-REPORTS-FOURTH-QUARTER-AND-FISCAL-YEAR-2026-EARNINGS/default.aspx) | 事件觀察 | AI网络、园区更新与订阅安全业务可带来增长，观察硬件订单转收入。 下一步：先核10月14日邮件网关漏洞的入侵范围、修复及客户/财务影响，再核FY2027订单和毛利。 | 公司披露Critical邮件网关漏洞且发现疑似客户入侵；已发布软件修复不代表影响已核清。 |
| [ANET Arista Networks](https://investors.arista.com/Communications/Press-Releases-and-Events/Press-Release-Detail/2026/Arista-Networks-Inc--Reports-Second-Quarter-2026-Financial-Results/default.aspx) | 估值觀察 | Q2收入增长37.7%，1.6Tbps等交换平台可受益于高速网络升级与以太网AI互连。 下一步：11月3日财报验证云客户订单、AI与非AI增长、毛利和库存/预收款。 | 大客户资本开支高度集中，交付确认与高增长预期可能使估值回撤放大。 |
| [TXN Texas Instruments](https://investor.ti.com/news-releases/news-release-details/ti-reports-third-quarter-2026-financial-results-and-shareholder) | 常規觀察 | 工业/汽车模拟芯片库存周期恢复及300mm产能成本优势，可在利用率提升时改善盈利。 下一步：阅读10月21日新Q3后核工业和汽车订单、库存、利用率及资本开支后FCF。 | 新产能折旧与低利用率可使营收复苏不转成现金；中国市场和出口规则持续影响。 |
| [ADI Analog Devices](https://investor.analog.com/news-releases/news-release-details/analog-devices-reports-record-fiscal-third-quarter-2026) | 估值觀察 | FY2026 Q3数据中心和工业需求带动收入，观察周期恢复与高现金转换是否延续。 下一步：验证工业与汽车补库、终端真实需求、毛利和营运资本。 | 周期反弹可能被重复下单和库存夸大；汽车需求、出口限制与估值需同时核。 |
| [QCOM Qualcomm](https://www.sec.gov/Archives/edgar/data/804328/000080432826000085/qcom062826erex991.htm) | 常規觀察 | FY2026 Q3汽车收入增长61%、IoT增长9%，提供降低手机依赖的业务路径。 下一步：核汽车设计赢单转收入、IoT利润及手机客户流失能否被新业务抵消。 | 同季手机收入下降20%，总QCT下降5%；客户自研芯片、许可争议和中国销售风险持续。 |
| [AMAT Applied Materials](https://ir.appliedmaterials.com/static-files/425ac634-4ee7-4c41-a07f-fa9e3c42b797) | 常規觀察 | Q3先进晶体管、先进封装与工艺复杂度提高带来设备及服务需求。 下一步：核先进工艺收入、服务续约、出口许可后的可服务市场和自由现金流。 | 中国出口限制与客户资本开支周期；旧BIS案已于2月和解、DOJ/SEC结案，不能误作新增未决调查。 |
| [LRCX Lam Research](https://newsroom.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026) | 估值觀察 | 先进存储、HBM和器件复杂度提升带动刻蚀沉积强度，9月季度经营增长值得跟踪。 下一步：核10月21日新财报的下季订单、存储投资和中国受限客户收入；重新估正常周期现金流。 | 新财报强增长未必超过高预期；存储资本开支周期、出口限制及售后服务可得性。 |
| [KLAC KLA](https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full) | 估值觀察 | 先进制程良率与封装复杂度提升带来检测需求，服务收入提供重复现金来源。 下一步：10月28日FY2027 Q1核检测强度、服务增长、毛利及中国收入许可风险。 | 先进制程投资集中于少数客户，出口限制可能收窄市场；拆股后每股数据口径需一致。 |
| [TSM Taiwan Semiconductor Manufacturing](https://investor.tsmc.com/english/quarterly-results/2026/q3) | 事件觀察 | 先进制程、先进封装与AI客户需求带来产能扩张机会，Q3官方结果已发布可作验证基准。 下一步：核先进节点/封装实际利用率、海外厂成本、资本开支与月度营收兑现。 | 台海集中度、美国海外扩产成本和涉华出口合规调查旧线索的最新状态待核。 |
| [CDNS Cadence Design Systems](https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Second-Quarter-2026-Financial-Results/default.aspx) | 估值觀察 | Q2订单积压和系统设计工具需求增长，芯片复杂度增加可扩张重复软件收入。 下一步：10月26日财报核订单转收入、现金回款、AI产品付费和受限地区收入。 | 高增长估值及中国EDA出口限制；2025年出口案认罪和解须跟踪合规义务，不能当今年新案件。 |
| [DOX Amdocs](https://investors.amdocs.com/news-releases/news-release-details/third-quarter-results-fiscal-2026) | 事件觀察 | FY2026Q3託管服務佔收入67%，12個月訂單積壓42.6億美元；aOS轉型可能增加長期合約價值。 下一步：11月3日17:00 ET FY2026Q4會議；先重建剝離Vubiquity後FY2027收入、GAAP盈利及扣重組支出的自由現金流，再比較其他服務股。 | Q3收入僅增2.7%，1.06億美元重組費壓低GAAP盈利；Vubiquity於10月8日出售，交易金額未披露，舊收入與現金流基準須重算。 |
| [G Genpact](https://media.genpact.com/2026-08-06-Genpact-Reports-Second-Quarter-2026-Results) | 事件觀察 | Q2先進技術方案收入增24.1%，佔總收入27%；總收入增7.1%，公司上調全年調整後EPS增長預期。 下一步：11月5日盤後Q3；核對核心業務下滑、AI簽約轉收入、經營現金流回升、應收款及GAAP與調整後差異。 | 佔收入73%的核心商業服務Q2僅增1.9%，Q3預期持平至微降；Q2經營現金流7200萬美元，低於去年1.77億美元；AI新產品未等於已兌現盈利。 |

### 消費與能源

| 股票與公司 | 觀察類型 | 機會與下一驗證點 | 主要風險 |
| --- | --- | --- | --- |
| [TJX TJX Companies](https://www.sec.gov/Archives/edgar/data/109198/000010919826000045/tjxq2fy27earningspressrele.htm) | 估值觀察 | 折扣消费与全球门店扩张；Q2 FY27同店增长4%，调整EPS增长11%。 下一步：验证Marmaxx同店改善、FY28门店增长计划与剔除关税退款后的利润；下一财报前更新估值。 | Marmaxx增速弱于集团；关税退款抬高GAAP盈利，不可把一次性收益年化。 |
| [ROST Ross Stores](https://investors.rossstores.com/node/23266/) | 估值觀察 | Q2同店增长10%主要由客流推动，新增门店可扩大低价零售覆盖。 下一步：验证下半年高基数下的客流、无退款利润率及新店生产率；重新评估当前价格。 | Q2 EPS含约0.60美元关税退款；需求强劲已否被价格充分反映仍待估值核验。 |
| [ULTA Ulta Beauty](https://www.ulta.com/investor/news-events/press-releases/detail/234/ulta-beauty-announces-second-quarter-fiscal-2026-results) | 常規觀察 | Q2同店、营业利润和EPS恢复，Space NK与门店/线上渠道提供增量。 下一步：等美东12月3日Q3电话会验证Target合作8月终止后的客流、利润率、回购资金及全年指引。 | 截至8月1日的Q2不能验证合作退出影响；竞争促销、并购与回购借款需核。 |
| [LOW Lowe's](https://corporate.lowes.com/newsroom/press-releases/lowes-reports-second-quarter-2026-sales-and-earnings-results-08-19-26) | 事件觀察 | 专业客户与维修需求，以及FBM/ADG并购整合，构成住宅修缮复苏时的经营杠杆。 下一步：先用8月下修后的指引重算下行情景，验证同店恢复、收购后利息和现金流。 | 全年同店预期已下修至持平、调整EPS预期收窄至低端；不能靠低倍数跳过重估。 |
| [HD Home Depot](https://www.sec.gov/Archives/edgar/data/354950/000035495026000145/hd_exhibit991x08022026.htm) | 常規觀察 | Q2同店恢复增长，小型维修需求与SRS/GMS专业分销网络可带来份额提升。 下一步：核住宅交易与大额装修是否恢复、SRS/GMS并购协同、债务和含退款指引。 | 大项目需求仍受房贷利率制约；收购增长不等于有机增长，利润也有退款与成本抵消。 |
| [ORLY O'Reilly Automotive](https://www.sec.gov/Archives/edgar/data/898173/000089817326000042/orly-20260729xex99d1.htm) | 估值觀察 | 专业维修与DIY双渠道执行强；Q2同店增长6%，营业利润增长8%。 下一步：核专业客户份额、配送投资回报、同店持续性及扣回购贡献后的利润增长，再评估价格。 | 进口成本与工资压力、同店高基数；回购使EPS增长快于净利润，不能只看EPS。 |
| [AZO AutoZone](https://investors.autozone.com/news-releases/news-release-details/autozone-4th-quarter-total-company-same-store-sales-increase-15) | 常規觀察 | FY26 Q4商业客户销售增长8.6%，商业服务项目覆盖扩大，专业维修份额可继续提升。 下一步：验证同店减速是否稳定、专业配送投资利润、海外汇率与债务回购。 | Q4国内同店仅增长1.6%，显著低于商业销售增幅；杠杆回购不可当营业改善。 |
| [CMG Chipotle Mexican Grill](https://ir.chipotle.com/2026-07-29-CHIPOTLE-RAISES-FULL-YEAR-COMPARABLE-SALES-GUIDANCE-ON-STRONG-Q2-MOMENTUM) | 事件觀察 | Chipotlane与新店扩张；Q2交易量恢复正增长，若客流修复可带来利润率杠杆。 下一步：10月28日财报先验证10月客流、食品成本和同店指引，处理新近负面渠道检查。 | 10月21日TD Cowen降至Hold并下调目标，指出10月需求弱；直营模式放大客流和成本压力。 |
| [HLT Hilton Worldwide](https://ir.hilton.com/news-events/investor-news/detail/85/hilton-reports-second-quarter-results) | 估值觀察 | 轻资产收费与净开房增长；Q2净增客房21,600间，管线规模支撑未来管理费。 下一步：10月27日Q3验证RevPAR、净单位增长、费用增长和杠杆后的每股现金流。 | 酒店需求与旅游周期；管线不是已开业客房，Q2部分非RevPAR收益由下半年提前确认。 |
| [LNG Cheniere Energy](https://lngir.cheniere.com/news-events/press-releases/detail/343/cheniere-reports-second-quarter-2026-results-and-raises) | 常規觀察 | CCL Stage3已于8月28日完成，新增产能可转为出口量与合同现金收入。 下一步：10月29日Q3核新增产能产量、扩建后现金余量、债务与事故调查是否限制运营。 | DCF不是扣全部扩建资本开支的标准FCF；Stage4未批，7月承包工死亡调查不能自动视作结束。 |
| [EOG EOG Resources](https://investors.eogresources.com/2026-08-04-EOG-Resources-Reports-Second-Quarter-2026-Results) | 估值觀察 | 高效率钻井、气油资源组合与成本控制；Q2成本低于指引中点，现金回报能力可跨周期验证。 下一步：以正常化油气价格重算FCF，核Encino整合、产量和资本开支，而非单季乘四。 | 近期高油价抬高现金流；并购基数、天然气价格与服务成本影响可持续收益。 |
| [XOM ExxonMobil](https://investor.exxonmobil.com/company-information/press-releases/detail/1208/exxonmobil-announces-second-quarter-2026-results) | 估值觀察 | Permian、Guyana新增产能及结构性降本，提供油价之外的量与成本改善。 下一步：10月30日财报剥离战争造成炼油高利润，验证正常化盈利、Guyana投产与资本纪律。 | 油价与炼油价差高度周期；Q2超强FCF和Q3炼油顺风不可作为永续盈利。 |
| [CVX Chevron](https://www.sec.gov/Archives/edgar/data/93410/000009341026000162/a06302026ex9918-k.htm) | 估值觀察 | Hess/Guyana资产整合和降本协同；Q2偿债增强资本灵活性，长期产量扩张可验证。 下一步：核正常化油价下的Hess协同、资本开支和股东回报，按投产时间而非能源AI标题估值。 | Q2高油价、炼油价差及营运资金顺风不可年化；Hess资产增长不等于有机增速。 |
| [FANG Diamondback Energy](https://www.diamondbackenergy.com/news-releases/news-release-details/diamondback-energy-inc-announces-second-quarter-2026-financial) | 估值觀察 | Permian规模与钻井效率、资产整合有望降低单位成本并增强正常油价下现金回报。 下一步：核整合后单位成本、净债务、收购/资产出售与资本预算，再用正常化油价估值。 | 油价敞口集中且有较大净债务；高价现金流和回购授权不等于未来实际回报。 |
| [NEE NextEra Energy](https://www.sec.gov/Archives/edgar/data/37634/000075330826000077/neeq32026exhibit99.htm) | 事件觀察 | FPL费率基础增长、储能与可再生签约；10月21日Q3调整EPS增长9.7%，已有真实项目积压。 下一步：先核Dominion合并的州/联邦批准、承诺的电价补贴及融资；将真实签约负荷与潜在管线分开。 | Dominion大型合并尚待监管批准，电价可负担性政治压力可能改变回报；不能用Q3超预期抵消交易风险。 |
| [DUK Duke Energy](https://www.sec.gov/Archives/edgar/data/1326160/000132616026000037/er-20260630xearningsreleas.htm) | 常規觀察 | 人口与工业负荷增长地区的电网投资，通过监管资本回收转为较稳定盈利。 下一步：核费率案回报、真实大客户接入与融资、极端天气成本回收，并复核煤灰诉讼责任。 | 高资本开支与利率、费率政治压力；Mooresville煤灰诉讼仍须核，不把已解决NTE案当新利空。 |
| [AEP American Electric Power](https://www.sec.gov/Archives/edgar/data/4904/000000490426000055/a2q20268kpressreleaseex991.htm) | 常規觀察 | 输电与已签大负荷需求可扩大费率基础；Q2上调全年经营EPS指引，支持跟踪资本回收。 下一步：核每项数据中心负荷的约束性合同、接入日期、担保和用户承担成本；核资本开支融资与监管回报。 | 69GW等负荷规划不等于即期售电；新核能/燃料电池项目的许可、造价和股东融资均需单独测算。 |
| [CEG Constellation Energy](https://www.constellationenergy.com/news/2026/08/constellation-reports-second-quarter-2026-results.html) | 估值觀察 | 真实长期PPA与核电资产利用率；Q2新签920MW长期售电协议，Calpine整合增加业务范围。 下一步：核Calpine后净债务与剥离义务、核电停机和Crane重启进度；按签约电价与生效年份估值。 | 高估值与电价周期、核电停机、并购整合；补救性剥离达成不等于所有交易成本消失。 |
| [VST Vistra](https://investor.vistracorp.com/2026-08-07-Vistra-Reports-Second-Quarter-2026-Results) | 事件觀察 | 现有核电/燃气与零售业务可承接更高电力需求，长期PPA能改善未来现金流可见性。 下一步：11月6日财报核PPA实际收费、Cogentrix交易审批与融资、扩张后现金流和Moss Landing责任。 | Moss Landing事故善后及法律责任、Cogentrix仍待交割、能源对冲公允价值使GAAP利润噪音大。 |
| [PRDO Perdoceo Education](https://www.sec.gov/Archives/edgar/data/1046568/000119312526337919/prdo-ex99_1.htm) | 資料待核 | 健康科學教育及現金產生能力值得研究；Q2營業利潤增6.8%，USAHS學生人數增6.0%。 下一步：先確認Q3官方公布日期；核對最新訴訟、學生資助規則、Grad PLUS替代融資、招生及留存，再作正常化盈利估值。 | 整體學生人數僅增0.7%、收入增1.8%；AIUS學生減少，聯邦學生資助、Grad PLUS取消及法律監管風險直接影響投資假設。 |
| [BKNG Booking Holdings](https://digital-strategy.ec.europa.eu/en/news/commission-investigate-how-bookingcom-combats-scams-and-fraud-under-digital-services-act) | 事件觀察 | 全球旅遊平台、直接預訂與成本效率；僅構成繼續研究理由。 下一步：立即核對DSA程序、FTC進展和公司回應，再於11-03 Q3財報量化預訂、營銷效率、合規成本與指引；完成前不得升格買入。 | 2026-10-21歐盟委員會正式啟動DSA程序，涉及虛假房源、釣魚詐騙和付費排名廣告標示；Q2 10-Q已披露FTC人員擬建議起訴Priceline及合作方。另有中東衝突、長途旅行和航班成本影響。 |

## 延續的重大事件

BKNG已在本池，2026年10月21日歐盟正式DSA程序仍凍結新增或加倉推薦，未因納入而解除。現持處置須獨立覆核。[事件復盤](STOCK_SELECTION_PIPELINE.md)。原池TMO、DHR、IQV等事件及備選NDAQ的舊歐盟調查、CPRT的DOJ調查均繼續承接，沒有新證據不得視作已結案。
