# 日價格來源與公開範圍

後續已新增 **EODHD AAPL.US 官方 demo**，實抓 449 筆調整後日價及獨立公司行動，配對具名分析師樣本。這批也只存本機私人研究；來源許可、欄位尺度、覆蓋與重現見 [NAMED_SAMPLE.md](NAMED_SAMPLE.md) 及 `reports/named_coverage.json`。以下為首批 IBM 來源紀錄。

本階段實際測試並採用 Alpha Vantage 官方 IBM 範例 API，作為**私人、本地研究用**的調整後日價格樣本。未找到足以直接公開再散布這份價格資料的授權，因此價格原始檔與整理後數值留在 Git 忽略目錄；公開倉庫提供抓取程式、來源、雜湊與覆蓋統計。這不是完整股票價格面板，也不是完成回測。

## 可重現的官方樣本

- [TIME_SERIES_DAILY_ADJUSTED 官方文件](https://www.alphavantage.co/documentation/#dailyadj)：說明原始日 OHLCV、調整後收盤價、歷史股息與拆股事件；文件直接列出下方 `demo` 範例。
- [IBM 完整範例請求](https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo)：`demo` 是官方公開的範例值，不是個人密鑰。取得其他股票或未來持續使用，需依提供者當時方案與條款處理；一般調整後日價格端點標為 Premium。
- [Alpha Vantage 使用條款](https://www.alphavantage.co/terms_of_service/)：第 2 節授權範圍為個人、非商業用途，並以私人個人的投資分析、研究、測試等活動界定範圍。第 3 節授權不可再授權、不可轉讓。查閱日為 2026-10-19；未發現向公開 GitHub 提供原始價格下載的明確許可。

在 2026-10-19 的連線檢查，該範例回傳 HTTP 200，包含 6,781 個 IBM 日觀察值，日期由 1999-11-01 至 2026-10-16，來源 metadata 的 `Last Refreshed` 為 2026-10-16。API 是動態來源，之後可能更新或修訂；本次正式執行的實際日期、筆數與 SHA-256 以 `data/manifests/prices_ibm.json` 及產生的覆蓋報告為準。這些統計不是市場數值的公開替代品。

檔案分工：

| 路徑 | 內容與處理 |
| --- | --- |
| `.local-data/raw/alpha_vantage/IBM.json` | 實際下載的來源回應；保留原始位元組供核對；Git 忽略 |
| `.local-data/processed/prices_daily.csv` | 由來源解析的 IBM 日價格；Git 忽略 |
| `data/manifests/prices_ibm.json` | 公開來源 URL、抓取時間、筆數、日期範圍、檔案雜湊及使用限制；不含逐日價格 |

請勿把上述本地檔案另行附入 commit、release 或公開下載。倉庫程式的授權不會改變供應者對資料的使用限制；欲公開原始價格，應先取得適用的再散布權或改用授權已確認的來源。

## 欄位及調整基準

來源每日記錄提供 `open`、`high`、`low`、`close`、`adjusted close`、`volume`、`dividend amount`、`split coefficient`。依官方文件，OHLCV 為當時交易數值，調整後收盤價另列；本研究保留兩者，以及股息與拆股欄位，不把調整後收盤價覆寫成名目收盤價。日期是提供者的美國市場日日期，metadata 時區為 `US/Eastern`；它不是新聞發布的精確時間。

調整後收盤價適合後續建立一致的報酬序列，但不能直接與分析師當日發布的**名目目標價**比較。目標價、事件起點價格與後續價格必須先轉成相同拆股單位；股息調整的總報酬尺度也不等同名目股價觸及某一價格。若研究「走完起始價到目標價差距的 50% / 75%」，必須明訂起點、方向、是否使用盤中高低價、拆股調整及事件何時可交易。現有階段只抓取資料，沒有計算這些達標時間。

供應者今日回傳的歷史調整數值，可能因後來發生的公司行動或資料修訂而改變。本次快照不是當年可取得的歷史版本；雜湊可辨識本次快照，但不能證明其在事件發生日已知。未來若要避免前視偏差，需保存每次擷取版本並另行定義 point-in-time 規則。

## 覆蓋與缺失的解讀

IBM 官方範例僅覆蓋一個 ticker。分析師事件中其他 ticker 缺少此價格來源，必須保留缺失，不能用 IBM 代填、用常數填補或將缺失視為零報酬。事件是否有發布日之後的價格、是否至少有 4 週觀察窗，以及因樣本結束而被截尾，須分別計數。即使 IBM 事件可連接，也不足以推論整體分析師預測表現。

基本資料檢查應涵蓋日期能解析、ticker 與日期唯一、價格為正且有限、成交量非負、拆股係數為正，以及原始 OHLC 的高低關係。市場休市日不代表遺漏；在未取得正式交易日曆前，不能把每個曆日或每個平日都當作應有記錄。通過格式檢查也不等於價格已由第二供應者交叉核實。

## 本階段其他候選來源

| 候選 | 查證結果與未採用原因 |
| --- | --- |
| Yahoo Finance / yfinance | [維護者官方 README](https://github.com/ranaroussi/yfinance/blob/main/README.md) 明確區分套件 Apache 授權與 Yahoo 實際資料權利，提醒 API 供個人用途。未據套件開源授權公開價格。 |
| Nasdaq / Quandl WIKI | 具歷史日 OHLCV、股息、拆股及調整價；[Nasdaq 官方套件文件](https://github.com/Nasdaq/data-link-python/blob/main/FOR_DEVELOPERS.md) 仍列出 `WIKI/AAPL` 用法。本次無帳號直接請求官方 `WIKI/AAPL` API 得到 HTTP 403，未取得樣本。舊 WIKI 可作後續較早期間研究候選；不能當成已取得 2026 年的資料，也不能把現行平台的一般條款或第三方鏡像說明當成完整的歷史授權證據。 |
| Stooq 與 Kaggle 轉存 | 目前未完成上游再散布權及調整方法的原始文件核實。Kaggle 上傳者標示 CC0 本身不足以核實其對上游來源的權利，本階段不公開轉存價格。 |
| Tiingo | [官方產品頁](https://www.tiingo.com/products/end-of-day-stock-price-data) 列出原始與調整 OHLCV、股息及拆股，並把一般方案的 Internal Use Only 與另行提供的 Display Redistribution 方案區分。未使用帳號或付費方案，未抓取或公開其價格。 |

本階段不聲稱找到可無條件公開再散布的完整現代美股價格資料庫。可公開的分析師樣本與價格的本地取得是分開的授權問題；未完成任何目標價達標時間、Buy/Hold/Sell 的 4 週報酬相關性或策略回測。
