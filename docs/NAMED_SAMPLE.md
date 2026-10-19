# 具名分析師私人研究樣本

存取與授權核閱日期：**2026-10-19（Asia/Shanghai）**。這批資料用來檢查具名事件、修訂接合與價格窗口；尚未完成 Buy/Hold/Sell 相關性或目標價到達時間回測。

## 來源與使用範圍

分析師事件來自 AnaChart 的 [AAPL 免費樣本頁](https://anachart.store/free-sample/)及其[官方 100 筆 CSV](https://anachart.store/wp-content/uploads/2026/09/AnaChart_AAPL_sample_100_rows.csv)。樣本頁允許內部載入、測試及與自行取得的價格核對；[條款 §4](https://anachart.store/terms-of-service/)區分內部研究、衍生分析及禁止公開的原始記錄。本專案將 CSV、逐筆轉換、修訂配對與價格接合全部留在受 Git 忽略的 `.local-data/`，公開倉庫只存程式、文件、彙總品質報告及來源 manifest。來源並未授予本專案公開再分發此 CSV 的權利。

日價格使用 EODHD [官方 quick-start 所列 AAPL.US demo 介面](https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis)。其[條款](https://eodhd.com/financial-apis/terms-conditions)允許符合非專業用戶定義者為私人、非商業用途保存及分析，限制再分發、展示或供他人存取原始或重包裝資訊。因此價格原始檔、逐日表及逐筆接合仍只存本機。demo 可公開呼叫不等於資料屬開放授權；這裡不保證其他用途均獲授權。

ExAnte 未納入這批樣本：上傳者的 MIT 標記未解決上游 MarketBeat 的權利疑問，詳見 [SOURCES.md](SOURCES.md)。

## 實際樣本與缺口

以下是本次實際重建的品質計數；完整彙總見 `reports/named_coverage.json`。空值保留，不以券商或推測內容補填。

| 項目 | 本次結果 |
| --- | --- |
| 原始／完全去重後筆數 | 100／90；10 筆完全重複 |
| ticker 與事件日期 | AAPL；2025-09-09 至 2026-04-14 |
| 非空具名分析師 | 28 個來源姓名值；不公開姓名清單 |
| 去重後具姓名、評級及數字新目標價 | 75 筆 |
| 原始新評級 | Buy 64、Hold 19、Sell 7、空白 10 |
| 原始缺少姓名／券商 ID | 1／3 筆 |
| 原始缺少舊／新評級 | 43／10 筆 |
| 原始缺少舊／新目標價 | 29／8 筆 |
| 原始具數字前後目標價／數值有變 | 71／62 筆 |

ticker 由官方 AAPL 樣本頁及檔名確定，原始 CSV 沒有 ticker 欄。`analyst` 是來源提供的標準化姓名，`broker_number` 是內部券商 ID；免費樣本沒有券商名稱、逐筆新聞網址或發布時刻。姓名尚未經本專案逐人獨立核實，日期也不能證明當時已可取得此筆資料。

修訂配對按 **ticker、來源分析師姓名及來源券商 ID** 分組，只比較不同日期的觀測。數字券商 ID 統一小數格式後有 25 個值。17 組身份在多日出現，產生 50 組相鄰日期候選：27 組前後數值銜接、1 組不一致、13 組缺可比較目標價、9 組涉及同日多筆而順序不明。順序不明者不任意挑一筆串接；不能把所有缺口都當成改價。這些是樣本內的可觀測配對，**不是完整或獨立核實的修訂鏈**。

去重後有 55 筆記錄的前後目標價不同，75 筆同時具姓名、評級和新目標價（75/90，83.33%）。個別列是否提供舊目標價，與是否在樣本中直接觀察到前一筆事件，是兩種不同的證據。

EODHD 價格請求窗口為 **2025-01-01 至 2026-10-16**，實際取得 **449 個交易日（2025-01-02 至 2026-10-16）**，另抓到該窗口 7 筆股息、0 筆拆股。90 筆唯一事件均有下一交易日及至少 28 曆日窗口；40 個不同事件日期的名目收盤價全部在 0.02 美元容許差內與另一來源一致。這是來源交叉核對及覆蓋，不是預測命中率。

來源含原始 OHLC、拆股及股息調整的 `adjusted_close`，成交量已作拆股調整。每日端點沒有股息／拆股欄，不能填零冒充觀測；公司行動另存原始回應。不能把休市日當成缺漏。調整後價格可能因後續公司行動而回溯變更，必須保留擷取版本。AnaChart 的 `close_price_adj` 沒有在此被假定為與 EODHD 相同的股息調整尺度，交叉核對使用名目收盤價。

## 供應商結果欄的隔離

AnaChart CSV 另帶 `target_direction`、`target_met`、`date_met`、`days_to_hit`。這些是**供應商事後標籤**，獨立保存於 `anachart_vendor_outcomes.csv`，不進入事件預測欄或當作本專案回測結果。初步樣本的 `date_met` 最晚至 2026-07-16，44 筆晚於事件集合截止日 2026-04-14，顯示事件日期截止不等於結果觀察截止。

價格接合先確認事件與未來窗口是否可用；不據此宣稱已觀測完整修訂、取得無前視偏差的交易訊號或完成四週報酬檢定。未來研究還須明確規定進場時點、同日事件處理、停止追蹤／改價規則，以及拆股後目標價與價格的一致基準；未調整目標不能直接和包含股息調整的價格比較。

## 重現流程與檔案

在倉庫根目錄依序執行：

```text
python -m scripts.named_sample fetch-analysts
python -m scripts.eodhd_prices fetch
python -m scripts.named_sample build
python -m scripts.named_sample validate
python -m scripts.named_sample report
python -m scripts.named_sample check-public
```

下載來源可能更新；manifest 記錄網址、擷取時間、內容雜湊及授權範圍。相同程式重抓不保證得到相同上游版本，重現特定結果應使用已保存且雜湊一致的本機快照。

| 位置 | 內容 |
| --- | --- |
| `data/manifests/analysts_anachart.json` | 公開來源、抓取及授權 metadata，不含逐筆事件 |
| `data/manifests/prices_aapl_eodhd.json` | 公開價格來源與品質 metadata，不含日價格 |
| `.local-data/processed/named_events.csv` | 私人正規化事件 |
| `.local-data/processed/named_revision_pairs.csv` | 私人樣本內修訂配對及缺口標記 |
| `.local-data/processed/named_price_windows.csv` | 私人事件與價格窗口接合 |
| `.local-data/processed/anachart_vendor_outcomes.csv` | 隔離的供應商事後標籤 |
| `.local-data/processed/eodhd_prices_daily.csv` | 私人日價格表 |

`check-public` 用來攔截受限資料、逐筆衍生資料或私人路徑被誤追蹤；通過檢查不構成法律授權或資料正確性保證。

來源署名：**Analyst sample: AnaChart / VADJ Inc.; daily prices: EODHD**。本文僅列彙總品質資訊，沒有公開原始個別記錄或分析師名單。
