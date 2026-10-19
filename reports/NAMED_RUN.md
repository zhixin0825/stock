# 具名樣本蒐集執行紀錄

日期：2026-10-19（Asia/Shanghai）。此輪補充具名分析師與前後目標價資料，並實抓同一 ticker 的調整後日價；沒有執行回測。

## 實際資料

- AnaChart 官方 AAPL 100 筆 CSV：HTTP 200；SHA-256 `7fecd71e47c681c3bece604d2e4b62722ea204ac5b633e19eff04986cfb449ab`。原始與正規化均保留 100 筆，標記 10 筆重複後 90 筆唯一事件。28 位來源具名分析師，75 筆唯一事件具姓名、評級及新目標價，55 筆提供有變動的前後目標價。
- EODHD 官方 demo：三個端點均 HTTP 200；449 筆 AAPL 日價、7 筆股息、0 筆拆股。請求範圍 2025-01-01 至 2026-10-16；實際日價從 2025-01-02 起。逐端點 URL、抓取時間及 SHA-256 見公開 manifest，數值均保留本機。
- 50 組相鄰日期候選中，27 組前後目標價銜接、1 組不一致、13 組缺目標價、9 組涉及同日多筆。不能據此宣稱完整修訂鏈。90 筆唯一事件皆有後續與至少 28 曆日窗口；40 個事件日期的名目收盤價交叉核對全部在 0.02 美元差內。

## 執行及驗證

```text
python -m scripts.named_sample fetch-analysts
python -m scripts.eodhd_prices fetch
python -m scripts.named_sample build
python -m scripts.named_sample validate
python -m scripts.named_sample report
python -m unittest discover -s tests -v
python -m scripts.named_sample check-public
git diff --cached --check
```

本機 5 個逐筆衍生檔均與原始快照重建逐位元組相同；日期、來源值、有限正數、重複、姓名與券商分組、同日歧義、API 錯誤訊息、價格與公司行動、雜湊及 metadata 的檢查通過。全倉庫 43 項離線測試通過；合成測試輸入僅存在測試程式及臨時測試目錄，沒有混入研究資料。

`target_direction`、`target_met`、`date_met`、`days_to_hit` 隔離在本機供應商結果檔，沒有進入事件內容識別碼、配對判斷或本專案績效結果。來源的事件截止日不能當作結果觀察截止日。

原始檔、正規化事件、修訂配對、窗口清單及逐日價格全部受 `.local-data/` Git 忽略保護；公開檔只含程式、來源、schema、雜湊和彙總。來源姓名不列入公開報告。這些檢查不等於法律保證、身份獨立核實、完整交易日曆或已驗證的 point-in-time 研究資料庫。
