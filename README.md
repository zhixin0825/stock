# 分析師預測研究：第一階段資料蒐集

2026-10-19（Asia/Shanghai）。已取得真實來源樣本、建立可重現轉換並完成基本驗證；**尚未進行回測、相關性或到達時間研究**。目前仍未取得能公開再分發、包含個人分析師姓名與完整修訂歷史的資料。

## 本次實際取得

| 項目 | 觀察樣本 | 公開範圍 |
| --- | --- | --- |
| Dalsna 券商目標價事件 | 1,735 筆、578 個 ticker、56 家券商；新聞日 2026-02-20 至 2026-10-18 | 原始 CSV、正規化 CSV、來源與雜湊；CC BY 4.0 |
| IBM 調整後日價格 | 6,781 筆；1999-11-01 至 2026-10-16；原始 OHLCV、adjusted close、股息、拆股係數 | 僅本機私人研究；公開取得程式、manifest、覆蓋及驗證結果，沒有逐日價格 |
| 價格窗口接合 | 14 筆 IBM 事件有發布日後 7 曆日內的價格；其中 11 筆在首個後續交易日至少有 28 曆日追蹤 | 只記錄日期窗口是否存在，沒有計算報酬或達標時間 |

這是下載樣本內的覆蓋，分母不是全市場。578 個 ticker 尚未逐一確認交易所、證券身分或美元報價；不可直接稱為完整美股樣本。

本機價格 ticker 覆蓋為 1/578（0.17%），有發布日後價格的事件為 14/1,735（0.81%），具至少 28 曆日窗口為 11/1,735（0.63%）；具名個人覆蓋為 0%。這些是可用資料窗口，不是策略命中率。

評級映射後 Buy 1,135、Hold 419、Sell 63、未映射 118。未映射包含 111 筆來源空白，以及 6 筆 `Positive`、1 筆 `Perform`；沒有把未知值填成 Hold。Overweight/Outperform 等歸組屬研究約定，原文保留，並不代表不同券商的定義完全等價。

**關鍵缺口：1,735 筆全部缺個人姓名、前目標價、日內發布時間與目標價幣別。** 這些欄位保持空白，個人分析師及修訂鏈合格筆數均為零。不能用同一家券商的兩筆記錄證明是同一人的修訂。來源日期是新聞發布日，歷史首次可見時間未知；目前快照不是已驗證的 point-in-time 資料庫。來源採新聞選樣，並非逐份原始分析師報告獨立核驗。

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

下一階段需取得具適當權利的個人姓名、原始報告時間與完整修訂歷史，以及更廣股票的價格。在計算 50%／75% 價差進度或四週報酬前，還需決定成交時點、交易日曆、拆股／股息尺度及截尾規則。名目目標價不可直接與今日回溯調整的股價比較。

Data: [Dalsna Finance](https://dalsnafin.com/analysts), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。本專案加入欄位、評級映射及統計；不包含來源新聞全文或第三方市場價格的再授權。
