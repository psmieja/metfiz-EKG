# Metody Fizyczne w Biologii i Medycynie - Badanie przebiegów EKG - Projekt Zaliczeniowy

Piotr Śmieja, 2020

Wydział Fizyki, Uniwersytet Warszawski

## Cel

Celem projektu było stworzenie programu odczytującego zapisy EKG, obliczającego puls i zapisującego odpowiedni wykres EKG i pulsu w funkcji czasu.

## Uruchomienie

Program uruchamia się jako argument podając ścieżkę pliku. Przykładowe dane znajdują się w folderze **data**

`$ python 1.py ./data/sample2.csv `

Programy uruchamiane były w **Python3.8.0**, wersje wykorzystanych pakietów znajdują się w **requirements.txt**. Przykładowe dane znajdują się w folderze **data**. Po pobraniu pełnego repozytorium i zainstalowaniu odpowiednich bibliotek programy nie wymagają dodatkowej instalacji. Można wykorzystać programy na innych rekordach z odpowiednich baz danych, choć nie były one na nich testowane, wymaga to jednak indywidualnego pobrania ich i zapisania w csv z użyciem odpowiedniego oprogramownania z **WFDB** opisanego poniżej zgodnie z instrukcjami dostępnymi na załączonych stronach internetowych.

## Programy wykorzystane do odczytu danych

#### WFDB

https://archive.physionet.org/physiotools/wfdb-linux-quick-start.shtml

Pakiet oprogramowania do konwersji plików z PhysioNet

#### rdsamp

https://archive.physionet.org/physiotools/wag/rdsamp-1.htm

Program z **WFDB** do odczytu plików PhysioNet

**rdsamp -c** - produce output in csv
https://archive.physionet.org/physiotools/wag/rdsamp-1.htm

#### LightWave

https://physionet.org/lightwave/

Wyświetlanie przebiegów czasowych w przeglądarce

#### PhysioBank ATM

https://archive.physionet.org/cgi-bin/atm/ATM

Wyświetlanie danych w przeglądarce i eksport krótkich fragmentów do CSV (max 10s)

## Wykorzystane Bazy Danych

Wszyskie bazy danych pochodzą z 

https://physionet.org

Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. 
C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, 
PhysioToolkit, and PhysioNet: Components of a new research resource for 
complex physiologic signals. Circulation [Online]. 101 (23), pp. 
e215–e220.

i udostępnione są na licencji Open Data Commons Attribution Licence v1.0

https://opendatacommons.org/licenses/by/index.html

#### QT Database

https://physionet.org/content/qtdb/1.0.0/

Laguna P, Mark RG, Goldberger AL, Moody GB. A Database for Evaluation of 
Algorithms for Measurement of QT and Other Waveform Intervals in the 
ECG. Computers in Cardiology 24:673-676 (1997).

https://physionet.org/physiobank/database/qtdb/doc/index.shtml

15m fragmenty EKG

Pliki pochodzące z bazy

- `./data2/sample2.csv`

#### Motion Artifact Contaminated ECG Database

https://physionet.org/content/macecgdb/1.0.0/

Vahid Behravan, Neil E. Glover, Rutger Farry, Mohammed Shoaib, Patrick Y. Chiang. Rate-Adaptive Compressed-Sensing and Sparsity Variance of Biomedical Signals. Body Sensor Networks (BSN) 2015 IEEE International Conference in June 2015.

http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=7299419&tag=1

Pliki pochodzące z bazy

- **./data/**
  
  - `sample3_1.csv`
  
  - `sample3_2.csv`
  
  - `sample3_3.csv`

## Pliki i Foldery

- **proj**
  
  - **metfiz_venv** - virtual environment directory
  
  - **wfdb-10.6.2** - WFDB software directory
  
  - **data1** - pliki z ECG_ID test data
  
  - **data2** - pliki z QT DB data
  
  - **data3** - pliki z Motion Artifact Contaminated ECG Database
  
  - 0_1.py - pierwszy test na danych z ECG-ID
  
  - 0_2.py - test odczytu większego pliku z wykorzystaniem QT Database
  
  - 0_3.py - próby z zaburzeniami sygnału pochodzącymi z ruchu badanego
