RemssNetCDF4toCsv
=================
*   [在windows上使用RemssNetCDF4toCsv轉檔程式](#在windows上使用remssnetcdf4tocsv轉檔程式)
*   [安裝Python3及相關套件](#安裝python3及相關套件)
*   [安裝Jupyter](#安裝jupyter)
*   [執行RemssNetCDF4toCsv](#執行remssnetcdf4tocsv)
    *   [在命令提示字元(Command line)上執行](#在命令提示字元(command line)上執行)
    *   [在Jupyter上執行](#在jupyter上執行)
*   [問題排除](#問題排除)

* * *

## 在windows上使用RemssNetCDF4toCsv轉檔程式

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

* * *

## 安裝Python3及相關套件

### 步驟一：安裝Python3
首先我們至Python官網([https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/))上下載windows版本的Python主程式。在官網上可以看到諸多版本的主程式，如果您的電腦作業系統為win10，您可以選擇python3.6的最後版本，若作業系統為win7或電腦較舊，則可以試試看python3.4版本。這裡並沒有建議用python3.7是因為此版本過新，穩定性還不如python3.6。

// 01.png
在下載之前請至`控制台`>`系統及安全性`>`系統`中確認電腦的系統類型為32位元作業系統或是64位元作業系統。若為32位元作業系統，請下載該版本的`Windows x86 executable installer`；若為64位元作業系統，則請下載`Windows x86-64 executable installer`。下載後開啟執行檔，請勾選`Add Python 3.x to PATH`，記下安裝路徑(以下圖為例便是C:\Users\w.y.h\AppData\Local\Programs\Python)，並按下`Install Now`執行至完成。

// 002.png

### 步驟二：更改系統參數
Python安裝完成後，請至`控制台`>`系統及安全性`>`系統`中點選`進階系統設定`，在`進階`標籤中進入環境變數設定。在環境變數的視窗中點選系統變數中的`Path`並按修改。將`path\to\python`與`path\to\python\Scripts`以分號分隔接續在原本的數值之後。以[圖?]為例
於`C:\ ... ;C:\Windows`後加上 `;C:\Users\w.y.h\AppData\Local\Programs\Python;C:\Users\w.y.h\AppData\Local\Programs\Python\Scripts`。設定完成後按下確定離開。

// 05.png

### 步驟三：安裝相關套件
此步驟將安裝本程式有用到的外部套件，分別為**numpy**、**pandas**、以及**netcdf4**。安裝方法如下：

1. 打開命令提示字元
2. 在游標後輸入
   ````
   > pip3 install numpy
   ````
   並按下`Enter`，另外兩個亦然。
   ````
   > pip3 install pandas
   ````
   ````
   > pip3 install netcdf4
   ````
   
// 03.png
// 06.png

基本上這邊結束後就算是安裝完成了。在安裝的過程中你可能會遇到一些問題使得安裝失敗(出現紅字)，請參考[問題排除](#problem)的解法。


* * *

## 安裝Jupyter

安裝Jupyter並不是必要的，它只是另一個python的使用介面，讓第一次接觸python的人比較容易上手。Jupyter的介紹及使用方法可以參考[官方網站](http://jupyter.org/)或是去google輸入Jupyter notebook就會有一堆介紹文章甚至是影片出來。
Jupyter的安裝方法與上一節安裝相關套件的方法是相同的：

1. 打開命令提示字元
2. 在游標後輸入
   ````
   > pip3 install jupyter
   ````
   並按下`Enter`

安裝完成後，只要在命令提示字元輸入
````
> jupyter notebook
````
Jupyter Notebook便會從瀏覽器開啟。



* * *

## 執行RemssNetCDF4toCsv

這邊提供兩種在windows上執行RemssNetCDF4toCsv的方法。以下皆以單一檔案轉檔為例。


### 在命令提示字元(Command line)上執行

1. 打開命令提示字元
2. 先移動到RemssNetCDF4toCsv資料夾的位置
   ````
   > cd path\to\RemssNetCDF4toCsv
   ````
3. 以python執行RemssNetCDF4toCsv.py
   ````
   > python RemssNetCDF4toCsv.py input/file/name output/file/name <options>
   ````
   
想知道RemssNetCDF4toCsv.py的參數輸入規則亦可輸入
````
> python RemssNetCDF4toCsv.py -h
````
查看。

### 在Jupyter上執行

首先開啟Jupyter
1. 打開命令提示字元
2. 先移動到RemssNetCDF4toCsv資料夾的位置
   ````
   > cd path\to\RemssNetCDF4toCsv
   ````
3. 輸入Jypyter notebook，並按下enter鍵執行
   ````
   > jupyter notebook
   ````
4. 這時候Jupyter notebook會用你的瀏覽器開啟，並看到這個畫面
   // 12.png
   直接點選範例檔`RemssNetCDF4toCsv.execute.ipynb`便會看到以下兩行
   // 13.png
   上面那行是RemssNetCDF4toCsv.py的使用說明，下面的則是轉檔的範例。
   ```
   run -i RemssNetCDF4toCsv.py REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_20140819_20140830\20140819002744-REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_v04_095451.dat-v02.0-fv01.0.nc REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_20140819_20140830\testout.csv --lon_min 115 --lon_max 130 --lat_min 15 --lat_max 35
   ```
   這個範例將`REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_20140819_20140830`資料夾裡的檔案`SSTsubskin-TMI-L2b_v04_095451.dat-v02.0-fv01.0.nc`轉檔至同資料夾中，分別產生出test.csv以及test.csv.info兩個文字檔，除此之外，這個範例還指定了經緯度的範圍：東經115度至東經130度，北緯15度至北緯35度。選擇適當的範圍會縮短許多轉檔時間。
   
5. 其他
   每一個`In []:`稱為**cell**，你可以在一個cell中打上複數行數的python3指令，並按下`Run`執行。若想新開一個cell，可以直接按`+`新增。若想開一個新的notebook，則可以按左上角的`File>New Notebook>Python3`。

* * *

## 問題排除
