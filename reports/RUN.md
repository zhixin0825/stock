# 本次執行紀錄

執行日期：2026-10-19（Asia/Shanghai）。原倉庫為公開空倉庫，預設分支 `main`，無既有研究程式或資料。工作在另建的 Git clone 進行，沒有改動 ChatGPT 同步的 `sources/` 參考檔。

## 抓取結果

| 來源 | HTTP | 實際筆數 | 原始位元組 SHA-256 |
| --- | --- | --- | --- |
| Dalsna `analysts/data.csv` | 200 | 1,735 | `a732c9d468fe3150b7a8e68efee4463c89679c7ecec9308d85e124f6086601a5` |
| Alpha Vantage IBM 官方 daily adjusted demo | 200 | 6,781 | `034606c3b9c33e312228d624c019f6a5f70fe22787190a80d7cb71b8248e5721` |

實際 UTC 抓取時間、URL、HTTP metadata、授權及儲存範圍在 `data/manifests/`。Dalsna 原始 CSV 公開保存；IBM 原始及逐日價格保留在被 Git 忽略的 `.local-data/`，沒有公開價格記錄。`.gitattributes` 對原始快照停用換行轉換，以維持雜湊。

## 已執行的檢查

```text
python scripts/phase1.py fetch-analysts
python scripts/phase1.py fetch-prices
python scripts/phase1.py build --with-private-prices
python scripts/phase1.py validate --with-private-prices
python scripts/phase1.py validate
python scripts/phase1.py report --with-private-prices
python scripts/phase1.py report
python -m unittest discover -s tests -v
git diff --check
git check-ignore .local-data/raw/alpha_vantage/IBM.json .local-data/processed/prices_daily.csv
```

公開及本機驗證均通過；輸入 1,735 筆、輸出 1,735 筆、隔離 0 筆，原始快照及正規化重建一致。IBM 6,781 筆日資料通過價格鍵、日期順序、有限正數、OHLC、股息／成交量及調整係數檢查。20 個離線單元測試全部通過，合成測試資料僅存在測試程式，沒有寫入研究資料或報告。兩個私人價格檔均確認被 Git 忽略。

覆蓋報告另外盤點 578 個 ticker、56 家券商，14 筆 IBM 事件有後續價格，其中 11 筆有至少 28 曆日的觀察窗口。1,735 筆均缺個人分析師姓名、前目標價、精確發布時間與幣別。這些驗證不代表新聞提取已逐篇獨立核實，也不代表研究樣本已符合 point-in-time 或個人修訂研究的要求。

尚未計算報酬、相關係數、50%／75% 到達時間或任何策略回測。後續資料授權及欄位缺口見 README 與來源審核。
