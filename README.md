RemssNetCDF4toCsv
=================
*   [在windows上使用RemssNetCDF4toCsv轉檔程式](#introduction)
*   [安裝Python3及相關套件](#python3)
*   [安裝Jupyter](#jupyter)
*   [執行RemssNetCDF4toCsv](#execute)
    *   [在命令提示字元(Command line)上執行](#cmd)
    *   [在Jupyter上執行](#exejupyter)

* * *

<h1 id="introduction">在windows上使用RemssNetCDF4toCsv轉檔程式</h1>

本轉檔程式用於將NetCDF4格式(.nc檔)的[GHRSST Level 2P Global Subskin Sea Surface Temperature from TRMM Microwave Imager (TMI) onboard Tropical Rainfall Measurement Mission (TRMM) satellite](https://podaac.jpl.nasa.gov/dataset/TMI-REMSS-L2P-v4) 數據轉存為適宜以excel開啟的逗號分隔檔(.csv)。

本程式包含：

一個主程式
*   [RemssNetCDF4toCsv.py](./RemssNetCDF4toCsv.py)

四個函式
*   [printData.py](./printData.py)
*   [printGroupInfo.py](./printGroupInfo.py)
*   [printTopInfo.py](./printTopInfo.py)
*   [printVariableInfo.py](./printVariableInfo.py)

兩個應用範例程式
*   [run_RemssNetCDF4toCsv.sh](./run_RemssNetCDF4toCsv.sh)
    可在linux的bash下執行的批次檔
*   [RemssNetCDF4toCsv.execute.ipynb](./RemssNetCDF4toCsv.execute.ipynb)
    可在jupyter上執行的使用範例

一個含有數據檔範例的資料夾
*   [REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_20140819_20140830](./REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_20140819_20140830/)
    裡面包含了一個.nc檔，本資料夾為範例中程式輸入及輸出檔案存放的位置
    
以及本說明檔
*   [README.md](./README.md)

本程式主要使用Python3語言設計，因此需要用python3執行。以下幾個主題將介紹如何在windows下(主要針對win7以及win10)[安裝Python3與相關套件](#python3)、[安裝Jupyter](#jupyter)、以及[如何使用本程式](#execute)。

**注意：** 以下所提及的版本或是作法並不是唯一的，有興趣的話亦歡迎去google看看其他人都怎麼做。


<h2 id="python3">安裝Python3及相關套件</h2>

## 步驟一：安裝Python3
首先我們至Python官網([https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/))上下載windows版本的Python主程式。在官網上可以看到諸多版本的主程式，如果您的電腦作業系統為win10，您可以選擇python3.6的最後版本，若作業系統為win7或電腦較舊，則可以試試看python3.4版本。這裡並沒有建議用python3.7是因為此版本過新，穩定性還不如python3.6。

// 001.png

在下載之前請至`控制台>系統及安全性>系統`中確認電腦的系統類型為32位元作業系統或是64位元作業系統。若為32位元作業系統，請下載該版本的`Windows x86 executable installer`；若為64位元作業系統，則請下載`Windows x86-64 executable installer`。下載後開啟執行檔，請勾選`Add Python 3.x to PATH`，記下安裝路徑(以下圖為例便是C:\Users\w.y.h\AppData\Local\Programs\Python)，並按下`Install Now`執行至完成。

// 002.png

## 步驟二：更改系統參數

<h3 id="jupyter">安裝Jupyter</h3>
123


<h4 id="execute">執行RemssNetCDF4toCsv</h4>

123


<h5 id="cmd">在命令提示字元(Command line)上執行</h5>

123


<h6 id="exejupyter">在Jupyter上執行</h6>

123

