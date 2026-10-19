# 資料字典與適用範圍

CSV 空字串表示缺失，不是零，也不是 Hold。正規化檔為 UTF-8；原始 CSV 保留提供者位元組，透過 manifest 的 SHA-256 核對。`scripts/phase1.py` 的 `EVENT_FIELDS`、`PRICE_FIELDS` 為完整欄位清單。

## 事件表 `data/processed/analyst_events.csv`

| 欄位 | 含義 |
| --- | --- |
| `event_id` | 本專案對券商、ticker、新聞日期、目標價及來源網址計算的穩定雜湊識別碼；不是供應者原始事件 ID |
| `ticker`, `company`, `analyst_firm` | 來源原值，未作證券主檔或券商別名合併 |
| `analyst_name`, `analyst_identity_level` | 姓名空白，層級固定 `firm_only`；不可當作個人分析師事件 |
| `publication_date` | Dalsna `said_date`，新聞的紐約日期；不保證原始研究報告發布日 |
| `published_at_utc`, `timing_precision`, `availability_timestamp_known` | 精確時間空白，精度 `date`，歷史可見時間是否已知為 `false` |
| `rating_raw`, `rating_normalized`, `rating_mapping_version` | 原始評級、研究用 Buy/Hold/Sell 或空白、映射版本 `research-v1` |
| `price_target`, `previous_price_target`, `target_currency` | 來源數字目標價；前目標價及幣別空白，不擅自補 USD |
| `due_date`, `horizon_note` | 提供者的目標期限；保留其明示期限或預設 12 個月的區別，預設值不是原分析師的明示承諾 |
| `source_status` | 提供者狀態 `open/hit/miss/retracted`；非本研究回測結果，後續分析應排除撤回值 |
| `source_name`, `source_url` | 提供者引用的新聞及網址；部分為 Google News 轉址，未逐篇獨立核實 |
| `dataset_source_url`, `fetched_at_utc`, `raw_snapshot_path`, `raw_sha256`, `data_license` | 資料集出處、本次 UTC 抓取時間、原始檔路徑、位元組雜湊及資料授權 |

映射約定：Buy / Strong Buy / Outperform / Overweight / Market Outperform / Sector Outperform / Overweight／Buy → Buy；Hold / Neutral / Equal Weight / Market Perform / Sector Perform / In Line → Hold；Sell / Strong Sell / Underweight / Underperform / Market Underperform / Sector Underperform / Reduce → Sell。忽略大小寫、連字號及多餘空格，`Equalweight` 另作相同處理。未列出的文字保持未映射；`Positive`、`Perform` 不擅自歸類。這只是後續研究可修改的約定，不能證明各券商制度相同。

## 私人價格表 `.local-data/processed/prices_daily.csv`

| 欄位 | 含義 |
| --- | --- |
| `provider`, `ticker`, `date`, `currency`, `exchange_timezone` | Alpha Vantage，官方 IBM 範例，美國市場日，USD（IBM 普通股的報價單位），來源時區 `US/Eastern` |
| `open`, `high`, `low`, `close`, `volume` | API 的原始日 OHLCV；與調整後收盤價分開保留 |
| `adjusted_close` | 提供者依拆股及股息調整的收盤價，基準是本次抓取版本 |
| `adjustment_factor` | `adjusted_close / close`，使用十進位計算，沒有自行重建公司行動因子 |
| `dividend_amount`, `split_coefficient` | API 原始股息及拆股係數；股息可為零，拆股係數須為正 |
| `adjustment_basis`, `fetched_at_utc`, `raw_snapshot_path`, `raw_sha256` | 調整方法標記及快照來源資訊 |

價格欄位沒有公開再授權。不能把 IBM 代入其他 ticker，也不能把缺失價格轉成零報酬。

## 覆蓋及驗證報告

`coverage_public.json` 只使用公開事件；`coverage_local.json` 是本次本機價格配對結果。`price_window_inventory.csv` 只含事件 ID、ticker、日期及布林值，不含價格或報酬。窗口檢查找發布日後首個可用交易日（最多 7 曆日），再找該日起至少 28 曆日的觀察值；這是檔案覆蓋盤點，不是精確成交規則或四週績效。缺正式交易日曆時不判定中途交易日是否完整；也未計算截尾到達時間。

`validation_public.json` 可由公開 clone 離線重現；`validation_local.json` 需本機價格，記錄本次實際檢查。檢查時間可能變，原始快照及正規化資料的重建則須一致。缺失欄位不會令資料格式驗證失敗；通過驗證表示結構與來源一致，**不代表符合個人分析師研究條件或已由第二供應者核實**。

若沒有具名、完整修訂與可信首次發布時間，目前無法辨識「同一分析師在達標前改價」，也不能從歷史新聞快照排除前視或倖存者偏差。後續研究需另定價格尺度、成交時點、樣本母體、截尾及競爭風險，這一階段未計算任何回測結果。
