---
name: excel-vba
description: Excel VBA 開發的專業技能。用於建立 VBA 巨集、Excel 操作自動化及活頁簿處理。
---

# Excel VBA 開發技能

## 基本方針
- 必須使用 Option Explicit
- 必須進行錯誤處理（On Error GoTo）
- 透過控制畫面更新與計算來優化效能
- 變數須明確宣告類型

## 標準範本

### Sub 程序
```vba
Option Explicit

Public Sub ProcessData()
    On Error GoTo ErrorHandler

    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    ' 處理主體

CleanUp:
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
    Exit Sub

ErrorHandler:
    MsgBox "錯誤: " & Err.Description, vbExclamation
    Resume CleanUp
End Sub
```

## 命名規則
- 模組：mod_功能名稱
- 程序：動詞_受詞
- 變數：小駝峰式命名（帶前綴：str, lng, rng 等）

## 常用模式
- 取得最後一行：`Cells(Rows.Count, 1).End(xlUp).Row`
- 範圍迴圈：`For Each cell In Range(...)`
- 陣列處理：大量數據應讀入陣列後再處理

## 效能優化
```vba
' 處理開始時
Application.ScreenUpdating = False
Application.Calculation = xlCalculationManual
Application.EnableEvents = False

' 處理結束時
Application.ScreenUpdating = True
Application.Calculation = xlCalculationAutomatic
Application.EnableEvents = True
```

## 錯誤處理模式
```vba
On Error GoTo ErrorHandler
' 處理

Exit Sub

ErrorHandler:
    Dim errMsg As String
    errMsg = "錯誤代碼: " & Err.Number & vbCrLf & _
             "錯誤內容: " & Err.Description
    MsgBox errMsg, vbCritical, "錯誤"
    ' 視需要輸出日誌
End Sub
```

## 範例

- 「想要彙總 Excel 銷售數據」→ 提供工作表操作 + 彙總邏輯的範本
- 「想要合併多個 Excel 檔案」→ 提供 FileSystemObject 與活頁簿操作模式
- 「巨集執行很慢」→ 套用效能優化模式（如 ScreenUpdating 等）
- 「巨集因錯誤停止」→ 提供錯誤處理範本

## 指引

- 必須宣告 `Option Explicit` 以禁止隱含變數宣告
- 在所有程序中實作 `On Error GoTo ErrorHandler`
- 處理大量數據時，應先讀入陣列再進行迴圈處理
- 在處理前後控制 `ScreenUpdating` 與 `Calculation`
- 變數名稱應加上表示類型的接頭辭（str, lng, rng, ws 等）
- 將過長的程序依功能分割以確保可讀性
