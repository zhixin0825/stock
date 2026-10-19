# 資料授權及署名

## 新增的具名樣本與 AAPL 日價

**Analyst sample: AnaChart / VADJ Inc.** [免費樣本頁](https://anachart.store/free-sample/)明確提供內部測試與價格核對權限，[條款 §4](https://anachart.store/terms-of-service/)允許不重現原始記錄的彙總衍生分析。本專案僅公開程式、來源及統計；原始 CSV、正規化事件、供應商事後標籤、逐筆配對與接合全部留在 `.local-data/`。這份樣本沒有套用 Dalsna 的 CC BY 授權。

**Daily prices: EODHD.** [官方 demo](https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis)供試用；[條款](https://eodhd.com/financial-apis/terms-conditions)允許私人非商業保存及分析，限制再分發與展示。AAPL 日價與股息／拆股原始及逐筆資料均不公開，manifest 及覆蓋報告不含市場價格。若用途不符合個人非商業範圍，需另取得適用授權。

詳見 [新增樣本說明](docs/NAMED_SAMPLE.md)。

## 公開的 Dalsna 資料

Data: **Dalsna Finance analyst price-target tracker**, [dalsnafin.com/analysts](https://dalsnafin.com/analysts)，存取日 2026-10-19，依 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 使用。

提供者的[方法及授權聲明](https://dalsnafin.com/analysts/methodology)適用於其編纂的目標價、日期及判定等資料。此倉庫保留原始下載 CSV，另外正規化欄位、加入保守評級映射、缺失標記、來源追蹤及覆蓋統計；這些是本專案的轉換。請保留署名、授權連結及修改說明；不暗示提供者、券商或分析師認可本研究。

授權不延伸到連結文章全文或第三方市場價格。本倉庫沒有納入新聞全文，亦沒有替來源供應者授予不存在的權利。

## 本機的 Alpha Vantage 價格

`.local-data/` 不提交 Git。官方 IBM demo 的本機資料按提供者[服務條款](https://www.alphavantage.co/terms_of_service/)供私人個人、非商業研究使用。本次沒有確認公開再分發權，故只公開程式、檔案雜湊、日期及筆數等覆蓋資訊，**公開逐日價格筆數為零**。程式碼或其他資料的開放授權不能視作該價格的授權。

ExAnte 雖由上傳者標記 MIT，其分析師資料上游為 MarketBeat；因上游批量再分發限制而未公開提交。詳見 [來源審核](docs/SOURCES.md)。本文件只說明採用依據及範圍，不構成適用於所有使用情況的法律保證。
