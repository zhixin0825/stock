# 第一階段資料來源審核

審核及存取日期：**2026-10-19（Asia/Shanghai）**。本頁記錄公開文件、實際存取與本次採用範圍；不保證所有司法管轄區的法律結論。能下載、免費、開源程式或資料卡標示授權，均不等於上游資料可公開再分發。本階段尚未完成回測。

## 來源目錄

| 來源 | 可用欄位及實際存取 | 本次決定與授權限制 |
| --- | --- | --- |
| [Dalsna Finance CSV](https://dalsnafin.com/analysts/data.csv)／[方法與授權](https://dalsnafin.com/analysts/methodology) | CSV GET 200。券商、ticker、原始評級、數字目標價、新聞發布日、來源連結；沒有個人分析師姓名。 | **納入公開樣本**。編纂的目標價及日期等資料標示 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，須署名並註明轉換；不包含新聞全文及第三方市場價格。 |
| [ExAnte 資料卡](https://huggingface.co/datasets/yachuanliu/ExAnte)／[原始資料卡](https://huggingface.co/datasets/yachuanliu/ExAnte/raw/main/README.md) | 公開 analyst CSV 可讀；包含日期、券商、部分分析師姓名、評級與前後目標價。資料卡標示 MIT。 | **排除原始資料再分發**。[論文 §3.1](https://aclanthology.org/2026.eacl-long.72.pdf) 指出分析師預測來源為 MarketBeat；上傳者的 MIT 標籤未解決上游權利。 |
| [MarketBeat 使用條款](https://www.marketbeat.com/terms/) | 條款 GET 200；可見的歷史評級與目標價資訊不構成開放授權。 | 條款限制批量 CSV、Excel 或資料庫向第三方再分發；本次不抓取或上傳其評級資料。 |
| [Alpha Vantage Daily Adjusted 文件](https://www.alphavantage.co/documentation/#dailyadj)／[服務條款](https://www.alphavantage.co/terms_of_service/) | 官方 IBM demo 可作價格介面驗證；日資料提供原始 OHLCV、adjusted close、股息及拆股。實際成功筆數見執行報告。 | **價格只作本機私人研究**。條款 §2–3 的個人、非商業、不可轉授權使用，未授予本倉庫公開再分發價格的權利；價格原始檔及逐日價格表不提交。 |
| [Benzinga Ratings API](https://www.benzinga.com/apis/cloud-product/analyst-ratings-api/)／[官方介面說明](https://www.benzinga.com/apis/blog/mastering-the-ratings-api-analyst-upgrade-signals-for-swing-trading-and-momentum-plays/) | 官方列有日期／時間、個人分析師、券商、ticker、前後評級、前後目標價及來源網址；歷史標示自 2013 年。 | **候選，未取得資料**。需要 API key 及合適合約；公開文件未授予批量公開再分發權，不把文件示例當真實觀測。 |
| [FMP Price Target FAQ](https://site.financialmodelingprep.com/faqs?code=data)／[服務條款](https://site.financialmodelingprep.com/developer/docs/terms-of-service) | 官方確認目標價來自新聞，並提供來源連結；未測試付費資料或確認所需全部欄位及歷史完整性。 | **候選，未取得資料**。條款限制第三方共享及再分發；研究及公開發布範圍須另確認，不購買或冒用 key。 |
| [AnaChart 資料產品與欄位](https://anachart.com/snowflake-nasdaq100-analyst-price-targets-ratings/) | 官方列有日期、個人分析師、券商、ticker、前後評級／目標價及來源連結；本次僅核閱文件。 | **候選，未取得資料**。透過 Snowflake Marketplace，權利依該 listing 合約；未找到允許本倉庫批量再分發的開放授權。 |

## Dalsna 樣本的覆蓋與缺口

審核時下載的 CSV 有 **1,735 筆、578 個 ticker、56 家券商**，新聞日期範圍為 **2026-02-20 至 2026-10-18**。111 筆原始評級空白；券商、ticker、目標價、新聞日期及來源網址均有值。所有記錄當時的來源狀態都是 `open`。這些是檔案內計數，並非全市場覆蓋率或正確率；重抓時以該次快照與驗證報告為準。

- 個人分析師姓名、前目標價、行動、幣別及日內時間均未提供，保持空值，不能用券商名代替個人姓名，也不能證明完整修訂鏈。
- `said_date` 是紐約日期的**新聞發布日**，未必是原始研究報告的發布日；沒有盤前／盤中時間，不能直接當作當日可成交訊號。
- 來源會篩選並審核新聞，也會排除部分重複、無價格或異常目標；這是新聞選樣，存在覆蓋及選擇偏差。
- 760 個來源網址是 Google News RSS 轉址。保留來源原值，不宣稱都已解析或逐篇獨立核實；新聞全文不納入倉庫。
- 這次下載是目前可見的歷史集合，不能證明各筆當時已被此來源收錄。未提供歷史版本及首次可見時間，故**不是已驗證的 point-in-time 資料庫**。保存擷取時間及雜湊只能證明本次快照。

資料署名：**Data: Dalsna Finance, CC BY 4.0 — credit [dalsnafin.com](https://dalsnafin.com/analysts)**。正規化欄位由本專案轉換；原始評級及來源數值保留，Buy/Hold/Sell 映射屬研究假設。

## 價格與後續研究邊界

adjusted close 通常同時反映拆股與股息。未來計算目標價 50%／75% 的到達時間時，必須把當時目標價、起點價格及後續價格調成一致基準；不能把未調整目標直接與今日回溯調整的價格比較。四週報酬還需要明確的進場時點、交易日曆及可用價格窗口。

IBM demo 僅能驗證資料抓取、欄位及接合流程，不能代表全部 ticker 的價格覆蓋。對公開授權、姓名、完整修訂及首次可見時間尚未滿足的部分，應保留缺口；不得據此聲稱已完成個人分析師研究、相關性檢定或到達時間回測。
