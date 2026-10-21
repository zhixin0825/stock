# 分析師預測研究：第一階段資料蒐集

## 选股与换股规则

2026-10-21（Asia/Shanghai）新增执行规范。进行具体选股或持仓建议前，先完成重大新闻准入审查，再比较盈利、估值与机会成本；关键项未完成时允许零推荐。

- [完整选股流水线与BKNG事件复盘](docs/STOCK_SELECTION_PIPELINE.md)
- [每次推荐的复核记录模板](docs/STOCK_REVIEW_TEMPLATE.md)
- [仓库执行规则](AGENTS.md)

2026-10-19（Asia/Shanghai）。已取得真實來源樣本、建立可重現轉換並完成基本驗證；**尚未進行回測、相關性或到達時間研究**。目前仍未取得能公開再分發、包含個人分析師姓名與完整修訂歷史的資料。

## 新增：具名分析師及歷史改價樣本

已依明確的內部研究許可，實抓 **AnaChart AAPL 100 筆**，涵蓋 2025-09-09 至 2026-04-14；其中 10 筆完全重複，保留並標記後為 **90 筆唯一事件、28 位具名分析師**。75 筆唯一事件同時有姓名、評級與新目標價，55 筆提供有變動的前後目標價。100 筆原始與逐筆衍生資料全部留在本機，沒有公開上傳。

按來源姓名、券商 ID 及 ticker，比較相鄰不同日期：27 組前後目標價可銜接、1 組不一致、13 組缺目標價、9 組涉及同日順序不明。這是樣本內觀測，**不代表取得完整、無遺漏的修訂鏈**。來源缺逐筆新聞連結、發布時刻及券商名稱；評級為來源簡化類別，身份未逐人獨立驗證。

對應價格另從 **EODHD 官方免註冊 AAPL.US demo** 取得 **449 筆調整後日價（2025-01-02 至 2026-10-16）**、7 筆股息及 0 筆拆股。全部 90 筆唯一事件均有後續及至少 28 曆日窗口，40 個不同事件日期的名目收盤價在 0.02 美元容許差內全部交叉吻合。這些是資料核對，沒有計算預測勝率或報酬。

AnaChart 和 EODHD 均有再分發限制；原始、正規化、配對與價格檔全部受 `.local-data/` 的 Git 忽略規則保護，公開只放程式、來源 manifest 和彙總報告。供應商事後到價標籤獨立隔離，沒有作為本專案的研究結果。

- [新樣本來源與重現方法](docs/NAMED_SAMPLE.md)
- [具名樣本覆蓋與缺失](reports/named_coverage.json)、[本機重建驗證](reports/named_validation.json)、[全部資料集盤點](reports/dataset_inventory.json)
- [本次執行紀錄](reports/NAMED_RUN.md)、[公開／私人邊界檢查](reports/named_public_boundary.json)

```text
python -m scripts.named_sample fetch-analysts
python -m scripts.eodhd_prices fetch
python -m scripts.named_sample build
python -m scripts.named_sample validate
python -m scripts.named_sample report
python -m unittest discover -s tests -v
python -m scripts.named_sample check-public
```

公開 clone 可執行離線單元測試及原有 Dalsna 重建；要重建新增私人資料的彙總，需先按上述許可重新下載。上游可能修訂，因此重抓時應核對 manifest 雜湊，不保證動態下載永遠不變。原始評級與目標價、名目值與調整值分開保留；未知欄位不補猜測。

## 首批公開樣本及 IBM 介面驗證

| 項目 | 觀察樣本 | 公開範圍 |
| --- | --- | --- |
| Dalsna 券商目標價事件 | 1,735 筆、578 個 ticker、56 家券商；新聞日 2026-02-20 至 2026-10-18 | 原始 CSV、正規化 CSV、來源與雜湊；CC BY 4.0 |
| IBM 調整後日價格 | 6,781 筆；1999-11-01 至 2026-10-16；原始 OHLCV、adjusted close、股息、拆股係數 | 僅本機私人研究；公開取得程式、manifest、覆蓋及驗證結果，沒有逐日價格 |
| 價格窗口接合 | 14 筆 IBM 事件有發布日後 7 曆日內的價格；其中 11 筆在首個後續交易日至少有 28 曆日追蹤 | 只記錄日期窗口是否存在，沒有計算報酬或達標時間 |

這是下載樣本內的覆蓋，分母不是全市場。578 個 ticker 尚未逐一確認交易所、證券身分或美元報價；不可直接稱為完整美股樣本。

本機價格 ticker 覆蓋為 1/578（0.17%），有發布日後價格的事件為 14/1,735（0.81%），具至少 28 曆日窗口為 11/1,735（0.63%）；具名個人覆蓋為 0%。這些是可用資料窗口，不是策略命中率。

評級映射後 Buy 1,135、Hold 419、Sell 63、未映射 118。未映射包含 111 筆來源空白，以及 6 筆 `Positive`、1 筆 `Perform`；沒有把未知值填成 Hold。Overweight/Outperform 等歸組屬研究約定，原文保留，並不代表不同券商的定義完全等價。

**Dalsna 子集的缺口：1,735 筆全部缺個人姓名、前目標價、日內發布時間與目標價幣別。** 這些欄位保持空白，此子集的個人分析師及修訂鏈合格筆數均為零。不能用同一家券商的兩筆記錄證明是同一人的修訂。來源日期是新聞發布日，歷史首次可見時間未知；目前快照不是已驗證的 point-in-time 資料庫。來源採新聞選樣，並非逐份原始分析師報告獨立核驗。

## 檔案

- [正規化事件 CSV](data/processed/analyst_events.csv)、[原始快照 manifest](data/manifests/analysts_dalsna.json)。CSV 的空欄位表示缺失；JSON 使用明確的筆數。
- [公開覆蓋結果](reports/coverage_public.json)、[本機價格接合覆蓋結果](reports/coverage_local.json)、[逐筆窗口清單](reports/price_window_inventory.csv)。後兩者是本次本機執行留下的統計，從公開 clone 無價格檔時不能重算。
- [公開資料驗證](reports/validation_public.json)、[本次本機價格驗證](reports/validation_local.json)。
- [來源、候選與授權審核](docs/SOURCES.md)、[價格來源限制](docs/PRICE_DATA.md)、[欄位與研究邊界](docs/DATA_DICTIONARY.md)、[資料授權與署名](DATA_LICENSE.md)。

`.local-data/` 被 Git 忽略，包含本次已抓取的 IBM 原始及逐日價格。公開價格筆數為 **0**；不要將本機資料或個人 API key 強行加入 Git。ExAnte/MarketBeat 原始資料未公開提交，原因見來源審核。

## 重現與驗證

需求：Python 3.10+，只用標準函式庫。公開 clone 可離線重建既有快照，無 API key：

```text
python scripts/phase1.py build
python scripts/phase1.py validate
python scripts/phase1.py report
python -m unittest discover -s tests -v
```

取得新的公開分析師快照（動態來源，筆數可能改變），再執行上列指令：

```text
python scripts/phase1.py fetch-analysts
```

對符合 Alpha Vantage 個人、非商業研究條款的本機使用，官方 IBM demo 無需個人 key：

```text
python scripts/phase1.py fetch-prices
python scripts/phase1.py build --with-private-prices
python scripts/phase1.py validate --with-private-prices
python scripts/phase1.py report --with-private-prices
```

抓取程式拒絕將 HTTP 200 的 API 錯誤當成價格，也拒絕覆寫內容不同的既有原始快照。公開事件快照檔名包含日期及雜湊。`build` 不連網，以既存 manifest 與原始位元組重建；相同快照結果應逐位元組一致。API 之後可能更新、改價或停止提供 demo，因此不能保證再次下載的價格雜湊與本次相同；目前固定 IBM 原始檔若已有不同版本會停止，請先在 Git 忽略目錄另存舊版及對應 manifest。

驗證包含輸入輸出筆數、原始值對照、事件／價格唯一性、日期、正數有限值、未知評級、缺失姓名保留、OHLC 關係、調整係數及快照重建一致性。單元測試中的合成資料只用於故障檢查，沒有混入研究 CSV。

下一階段需擴大具適當權利的具名樣本、取得原始報告時間與完整修訂歷史，以及更廣股票的價格。在計算 50%／75% 價差進度或四週報酬前，還需決定成交時點、交易日曆、拆股／股息尺度及截尾規則。名目目標價不可直接與今日回溯調整的股價比較。

Data: [Dalsna Finance](https://dalsnafin.com/analysts), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。本專案加入欄位、評級映射及統計；不包含來源新聞全文或第三方市場價格的再授權。
