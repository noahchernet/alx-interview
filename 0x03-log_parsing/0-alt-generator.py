#!/usr/bin/python3
import sys


test_strings = [r'51.77.161.67 - [2022-07-06 18:14:58.342379] "GET /projects/260 HTTP/1.1" 301 963',
                r'195.18.136.144 - [2022-07-06 18:14:59.266149] "GET /projects/260 HTTP/1.1" 404 194',
                r'121.101.83.103 - [2022-07-06 18:14:59.389852] "GET /projects/260 HTTP/1.1" 401 909',
                r'230.88.229.93 - [2022-07-06 18:15:00.298044] "GET /projects/260 HTTP/1.1" 404 549',
                r'36.140.69.180 - [2022-07-06 18:15:00.444834] "GET /projects/260 HTTP/1.1" 404 870',
                r'146.136.162.139 - [2022-07-06 18:15:00.703781] "GET /projects/260 HTTP/1.1" 403 938',
                r'170.160.225.89 - [2022-07-06 18:15:01.330753] "GET /projects/260 HTTP/1.1" 400 167',
                r'64.111.134.65 - [2022-07-06 18:15:01.343489] "GET /projects/260 HTTP/1.1" 401 486',
                r'104.132.140.146 - [2022-07-06 18:15:01.850779] "GET /projects/260 HTTP/1.1" 500 733',
                r'107.245.150.43 - [2022-07-06 18:15:02.849368] "GET /projects/260 HTTP/1.1" 401 86',
                r'92.130.238.230 - [2022-07-06 18:15:03.426959] "GET /projects/260 HTTP/1.1" 405 329',
                r'2.34.247.54 - [2022-07-06 18:15:04.296281] "GET /projects/260 HTTP/1.1" 405 622',
                r'72.168.179.94 - [2022-07-06 18:15:04.624704] "GET /projects/260 HTTP/1.1" 404 499',
                r'169.56.201.128 - [2022-07-06 18:15:05.545586] "GET /projects/260 HTTP/1.1" 500 78',
                r'1.127.68.193 - [2022-07-06 18:15:06.386802] "GET /projects/260 HTTP/1.1" 403 736',
                r'149.87.6.51 - [2022-07-06 18:15:07.164808] "GET /projects/260 HTTP/1.1" 405 239',
                r'103.168.139.240 - [2022-07-06 18:15:07.860694] "GET /projects/260 HTTP/1.1" 301 204',
                r'90.64.210.33 - [2022-07-06 18:15:08.451991] "GET /projects/260 HTTP/1.1" 200 805',
                r'112.15.203.123 - [2022-07-06 18:15:09.029097] "GET /projects/260 HTTP/1.1" 403 247',
                r'147.67.109.138 - [2022-07-06 18:15:09.629821] "GET /projects/260 HTTP/1.1" 200 570',
                r'71.87.39.9 - [2022-07-06 18:15:09.686142] "GET /projects/260 HTTP/1.1" 400 151',
                r'206.175.13.80 - [2022-07-06 18:15:10.356547] "GET /projects/260 HTTP/1.1" 404 225',
                r'85.245.176.223 - [2022-07-06 18:15:10.383993] "GET /projects/260 HTTP/1.1" 405 413',
                r'181.30.210.150 - [2022-07-06 18:15:11.151577] "GET /projects/260 HTTP/1.1" 500 525',
                r'95.13.105.77 - [2022-07-06 18:15:11.350646] "GET /projects/260 HTTP/1.1" 403 696',
                r'210.234.194.200 - [2022-07-06 18:15:12.248429] "GET /projects/260 HTTP/1.1" 401 984',
                r'122.33.131.226 - [2022-07-06 18:15:12.880711] "GET /projects/260 HTTP/1.1" 200 74',
                r'198.139.56.3 - [2022-07-06 18:15:13.848617] "GET /projects/260 HTTP/1.1" 200 832',
                r'153.57.81.203 - [2022-07-06 18:15:14.527555] "GET /projects/260 HTTP/1.1" 200 852',
                r'125.11.57.41 - [2022-07-06 18:15:15.389559] "GET /projects/260 HTTP/1.1" 404 856',
                r'167.120.76.51 - [2022-07-06 18:15:15.578348] "GET /projects/260 HTTP/1.1" 403 738',
                r'65.79.42.54 - [2022-07-06 18:15:16.534967] "GET /projects/260 HTTP/1.1" 404 100',
                r'247.143.254.210 - [2022-07-06 18:15:17.321184] "GET /projects/260 HTTP/1.1" 301 887',
                r'252.227.155.254 - [2022-07-06 18:15:18.172766] "GET /projects/260 HTTP/1.1" 403 931',
                r'166.137.178.7 - [2022-07-06 18:15:18.182404] "GET /projects/260 HTTP/1.1" 405 207',
                r'255.176.222.136 - [2022-07-06 18:15:18.412847] "GET /projects/260 HTTP/1.1" 500 324',
                r'2.46.219.68 - [2022-07-06 18:15:18.613972] "GET /projects/260 HTTP/1.1" 404 379',
                r'146.87.171.170 - [2022-07-06 18:15:19.552963] "GET /projects/260 HTTP/1.1" 301 706',
                r'197.253.42.245 - [2022-07-06 18:15:20.029888] "GET /projects/260 HTTP/1.1" 200 993',
                r'129.215.96.90 - [2022-07-06 18:15:20.368719] "GET /projects/260 HTTP/1.1" 404 621',
                r'139.221.226.100 - [2022-07-06 18:15:21.065015] "GET /projects/260 HTTP/1.1" 403 938',
                r'155.27.138.185 - [2022-07-06 18:15:21.853517] "GET /projects/260 HTTP/1.1" 404 786',
                r'208.170.44.97 - [2022-07-06 18:15:22.781824] "GET /projects/260 HTTP/1.1" 401 968',
                r'122.242.44.77 - [2022-07-06 18:15:23.462015] "GET /projects/260 HTTP/1.1" 404 973',
                r'62.252.223.30 - [2022-07-06 18:15:24.059345] "GET /projects/260 HTTP/1.1" 401 184',
                r'129.131.101.181 - [2022-07-06 18:15:24.205091] "GET /projects/260 HTTP/1.1" 404 1008',
                r'108.235.159.221 - [2022-07-06 18:15:24.857327] "GET /projects/260 HTTP/1.1" 301 124',
                r'93.1.176.51 - [2022-07-06 18:15:25.172010] "GET /projects/260 HTTP/1.1" 405 803',
                r'95.88.30.59 - [2022-07-06 18:15:25.744574] "GET /projects/260 HTTP/1.1" 403 915',
                r'34.216.192.253 - [2022-07-06 18:15:26.316353] "GET /projects/260 HTTP/1.1" 400 520',
                r'14.180.32.27 - [2022-07-06 18:15:26.906528] "GET /projects/260 HTTP/1.1" 301 449',
                r'104.71.139.231 - [2022-07-06 18:15:27.461125] "GET /projects/260 HTTP/1.1" 400 593',
                r'220.149.206.14 - [2022-07-06 18:15:28.299483] "GET /projects/260 HTTP/1.1" 405 1014',
                r'194.249.189.106 - [2022-07-06 18:15:29.171160] "GET /projects/260 HTTP/1.1" 405 216',
                r'53.242.176.216 - [2022-07-06 18:15:29.220082] "GET /projects/260 HTTP/1.1" 404 711',
                r'111.71.100.76 - [2022-07-06 18:15:30.173673] "GET /projects/260 HTTP/1.1" 401 304',
                r'206.151.195.251 - [2022-07-06 18:15:30.655010] "GET /projects/260 HTTP/1.1" 400 749',
                r'10.42.22.236 - [2022-07-06 18:15:31.426706] "GET /projects/260 HTTP/1.1" 405 828',
                r'28.13.188.75 - [2022-07-06 18:15:31.493797] "GET /projects/260 HTTP/1.1" 403 611',
                r'33.109.184.26 - [2022-07-06 18:15:32.205011] "GET /projects/260 HTTP/1.1" 400 99',
                r'236.163.185.86 - [2022-07-06 18:15:32.760244] "GET /projects/260 HTTP/1.1" 301 563',
                r'202.101.41.238 - [2022-07-06 18:15:32.809323] "GET /projects/260 HTTP/1.1" 200 539',
                r'70.124.68.80 - [2022-07-06 18:15:33.291998] "GET /projects/260 HTTP/1.1" 404 17',
                r'233.148.226.37 - [2022-07-06 18:15:33.846682] "GET /projects/260 HTTP/1.1" 405 663',
                r'193.135.192.219 - [2022-07-06 18:15:34.074883] "GET /projects/260 HTTP/1.1" 500 537',
                r'177.5.93.243 - [2022-07-06 18:15:34.580099] "GET /projects/260 HTTP/1.1" 301 530',
                r'6.22.49.110 - [2022-07-06 18:15:35.517444] "GET /projects/260 HTTP/1.1" 500 807',
                r'166.29.17.223 - [2022-07-06 18:15:35.564135] "GET /projects/260 HTTP/1.1" 404 664',
                r'14.183.2.125 - [2022-07-06 18:15:35.873916] "GET /projects/260 HTTP/1.1" 400 733',
                r'38.182.247.253 - [2022-07-06 18:15:36.439263] "GET /projects/260 HTTP/1.1" 500 207',
                r'113.83.127.145 - [2022-07-06 18:15:37.165052] "GET /projects/260 HTTP/1.1" 404 779',
                r'229.4.93.88 - [2022-07-06 18:15:37.193025] "GET /projects/260 HTTP/1.1" 403 812',
                r'47.31.149.145 - [2022-07-06 18:15:37.890288] "GET /projects/260 HTTP/1.1" 200 70',
                r'87.116.255.19 - [2022-07-06 18:15:38.123219] "GET /projects/260 HTTP/1.1" 200 227',
                r'227.1.195.99 - [2022-07-06 18:15:38.540291] "GET /projects/260 HTTP/1.1" 400 360',
                r'134.149.117.99 - [2022-07-06 18:15:39.287970] "GET /projects/260 HTTP/1.1" 401 910',
                r'234.131.8.217 - [2022-07-06 18:15:40.031515] "GET /projects/260 HTTP/1.1" 403 587',
                r'8.208.85.123 - [2022-07-06 18:15:40.434961] "GET /projects/260 HTTP/1.1" 301 810',
                r'56.59.11.167 - [2022-07-06 18:15:40.503527] "GET /projects/260 HTTP/1.1" 500 137',
                r'103.82.90.221 - [2022-07-06 18:15:40.675173] "GET /projects/260 HTTP/1.1" 403 757',
                r'234.175.18.23 - [2022-07-06 18:15:40.817013] "GET /projects/260 HTTP/1.1" 403 781',
                r'239.7.76.145 - [2022-07-06 18:15:41.268898] "GET /projects/260 HTTP/1.1" 403 690',
                r'2.223.13.209 - [2022-07-06 18:15:41.588795] "GET /projects/260 HTTP/1.1" 200 1013',
                r'224.220.216.246 - [2022-07-06 18:15:42.555397] "GET /projects/260 HTTP/1.1" 403 984',
                r'191.11.91.158 - [2022-07-06 18:15:42.789272] "GET /projects/260 HTTP/1.1" 301 56',
                r'246.13.7.126 - [2022-07-06 18:15:43.130757] "GET /projects/260 HTTP/1.1" 401 191',
                r'38.50.254.150 - [2022-07-06 18:15:43.957811] "GET /projects/260 HTTP/1.1" 405 1014',
                r'24.218.160.136 - [2022-07-06 18:15:43.989218] "GET /projects/260 HTTP/1.1" 400 914',
                r'207.133.46.227 - [2022-07-06 18:15:44.967782] "GET /projects/260 HTTP/1.1" 404 698',
                r'186.80.1.124 - [2022-07-06 18:15:45.349144] "GET /projects/260 HTTP/1.1" 500 914',
                r'217.214.65.187 - [2022-07-06 18:15:45.422304] "GET /projects/260 HTTP/1.1" 301 223',
                r'218.210.42.47 - [2022-07-06 18:15:45.475795] "GET /projects/260 HTTP/1.1" 301 80',
                r'238.171.245.185 - [2022-07-06 18:15:45.960027] "GET /projects/260 HTTP/1.1" 404 876',
                r'198.245.22.160 - [2022-07-06 18:15:46.217778] "GET /projects/260 HTTP/1.1" 405 307',
                r'167.185.110.178 - [2022-07-06 18:15:46.927734] "GET /projects/260 HTTP/1.1" 401 258',
                r'30.206.81.22 - [2022-07-06 18:15:47.010501] "GET /projects/260 HTTP/1.1" 500 89',
                r'70.202.78.238 - [2022-07-06 18:15:47.081636] "GET /projects/260 HTTP/1.1" 403 842',
                r'211.237.207.76 - [2022-07-06 18:15:47.638937] "GET /projects/260 HTTP/1.1" 404 20',
                r'154.252.75.79 - [2022-07-06 18:15:48.499793] "GET /projects/260 HTTP/1.1" 301 125',
                r'63.56.18.187 - [2022-07-06 18:15:48.551674] "GET /projects/260 HTTP/1.1" 301 865',
                r'219.111.201.243 - [2022-07-06 18:15:48.964815] "GET /projects/260 HTTP/1.1" 405 412',
                r'140.5.39.32 - [2022-07-06 18:15:49.378908] "GET /projects/260 HTTP/1.1" 400 922',
                r'157.173.1.129 - [2022-07-06 18:15:49.650435] "GET /projects/260 HTTP/1.1" 403 53',
                r'232.241.245.220 - [2022-07-06 18:15:50.461033] "GET /projects/260 HTTP/1.1" 200 357',
                r'222.99.95.129 - [2022-07-06 18:15:51.117345] "GET /projects/260 HTTP/1.1" 401 555',
                r'16.74.232.84 - [2022-07-06 18:15:51.832852] "GET /projects/260 HTTP/1.1" 200 269',
                r'244.128.56.34 - [2022-07-06 18:15:51.933025] "GET /projects/260 HTTP/1.1" 403 936',
                r'148.145.96.227 - [2022-07-06 18:15:52.656279] "GET /projects/260 HTTP/1.1" 500 922',
                r'165.133.139.232 - [2022-07-06 18:15:53.313835] "GET /projects/260 HTTP/1.1" 500 386',
                r'163.63.237.180 - [2022-07-06 18:15:53.790455] "GET /projects/260 HTTP/1.1" 401 341',
                r'19.42.138.112 - [2022-07-06 18:15:53.976765] "GET /projects/260 HTTP/1.1" 500 716',
                r'75.108.142.28 - [2022-07-06 18:15:54.591177] "GET /projects/260 HTTP/1.1" 401 306',
                r'248.192.34.10 - [2022-07-06 18:15:55.030414] "GET /projects/260 HTTP/1.1" 200 944',
                r'138.247.22.4 - [2022-07-06 18:15:55.612943] "GET /projects/260 HTTP/1.1" 400 89',
                r'137.201.112.139 - [2022-07-06 18:15:56.228266] "GET /projects/260 HTTP/1.1" 401 176',
                r'33.73.30.175 - [2022-07-06 18:15:57.085308] "GET /projects/260 HTTP/1.1" 404 772',
                r'48.63.184.113 - [2022-07-06 18:15:57.376781] "GET /projects/260 HTTP/1.1" 301 731',
                r'69.186.206.197 - [2022-07-06 18:15:57.800320] "GET /projects/260 HTTP/1.1" 500 560',
                r'78.236.97.178 - [2022-07-06 18:15:58.541100] "GET /projects/260 HTTP/1.1" 401 141',
                r'189.19.178.39 - [2022-07-06 18:15:59.122025] "GET /projects/260 HTTP/1.1" 400 611',
                r'203.214.223.75 - [2022-07-06 18:15:59.809595] "GET /projects/260 HTTP/1.1" 400 546',
                r'245.45.207.117 - [2022-07-06 18:16:00.497384] "GET /projects/260 HTTP/1.1" 401 709',
                r'200.126.199.171 - [2022-07-06 18:16:00.968759] "GET /projects/260 HTTP/1.1" 401 827',
                r'179.42.2.231 - [2022-07-06 18:16:01.854656] "GET /projects/260 HTTP/1.1" 200 801',
                r'23.157.231.209 - [2022-07-06 18:16:02.636699] "GET /projects/260 HTTP/1.1" 500 572',
                r'50.150.196.203 - [2022-07-06 18:16:02.655302] "GET /projects/260 HTTP/1.1" 400 135',
                r'157.19.22.197 - [2022-07-06 18:16:03.556671] "GET /projects/260 HTTP/1.1" 404 268',
                r'110.125.3.104 - [2022-07-06 18:16:03.731650] "GET /projects/260 HTTP/1.1" 401 358',
                r'142.52.146.87 - [2022-07-06 18:16:03.902992] "GET /projects/260 HTTP/1.1" 500 793',
                r'180.253.12.44 - [2022-07-06 18:16:04.516568] "GET /projects/260 HTTP/1.1" 404 192',
                r'182.136.27.26 - [2022-07-06 18:16:04.737980] "GET /projects/260 HTTP/1.1" 200 916',
                r'174.203.23.98 - [2022-07-06 18:16:05.138140] "GET /projects/260 HTTP/1.1" 301 591',
                r'60.67.49.22 - [2022-07-06 18:16:05.683923] "GET /projects/260 HTTP/1.1" 405 377',
                r'88.135.125.160 - [2022-07-06 18:16:05.810868] "GET /projects/260 HTTP/1.1" 405 597',
                r'15.158.254.69 - [2022-07-06 18:16:05.957195] "GET /projects/260 HTTP/1.1" 400 333',
                r'149.128.68.46 - [2022-07-06 18:16:06.305218] "GET /projects/260 HTTP/1.1" 403 200',
                r'252.212.248.182 - [2022-07-06 18:16:06.977990] "GET /projects/260 HTTP/1.1" 404 636',
                r'196.84.20.194 - [2022-07-06 18:16:07.835081] "GET /projects/260 HTTP/1.1" 500 567',
                r'241.168.60.19 - [2022-07-06 18:16:08.007160] "GET /projects/260 HTTP/1.1" 500 625',
                r'115.72.118.138 - [2022-07-06 18:16:08.959715] "GET /projects/260 HTTP/1.1" 200 4',
                r'132.87.206.194 - [2022-07-06 18:16:09.298810] "GET /projects/260 HTTP/1.1" 200 678',
                r'235.137.56.78 - [2022-07-06 18:16:09.427291] "GET /projects/260 HTTP/1.1" 400 781',
                r'248.118.85.237 - [2022-07-06 18:16:10.378906] "GET /projects/260 HTTP/1.1" 405 494',
                r'72.177.68.44 - [2022-07-06 18:16:10.648690] "GET /projects/260 HTTP/1.1" 403 666',
                r'238.244.132.94 - [2022-07-06 18:16:11.285923] "GET /projects/260 HTTP/1.1" 401 829',
                r'171.243.237.84 - [2022-07-06 18:16:12.267072] "GET /projects/260 HTTP/1.1" 405 198',
                r'151.239.32.159 - [2022-07-06 18:16:12.344975] "GET /projects/260 HTTP/1.1" 200 289',
                r'14.215.71.204 - [2022-07-06 18:16:12.433419] "GET /projects/260 HTTP/1.1" 401 349',
                r'128.141.164.46 - [2022-07-06 18:16:13.372837] "GET /projects/260 HTTP/1.1" 500 910',
                r'82.153.66.3 - [2022-07-06 18:16:13.381629] "GET /projects/260 HTTP/1.1" 401 259',
                r'13.47.5.199 - [2022-07-06 18:16:13.558347] "GET /projects/260 HTTP/1.1" 403 730',
                r'192.19.36.42 - [2022-07-06 18:16:14.522784] "GET /projects/260 HTTP/1.1" 401 966',
                r'172.94.95.153 - [2022-07-06 18:16:14.733759] "GET /projects/260 HTTP/1.1" 403 264',
                r'205.10.121.95 - [2022-07-06 18:16:15.668046] "GET /projects/260 HTTP/1.1" 403 558',
                r'46.16.36.83 - [2022-07-06 18:16:15.994517] "GET /projects/260 HTTP/1.1" 200 64',
                r'191.29.150.12 - [2022-07-06 18:16:16.442727] "GET /projects/260 HTTP/1.1" 400 825',
                r'52.234.69.63 - [2022-07-06 18:16:17.009806] "GET /projects/260 HTTP/1.1" 200 797',
                r'183.173.21.76 - [2022-07-06 18:16:17.196552] "GET /projects/260 HTTP/1.1" 401 106',
                r'103.2.251.13 - [2022-07-06 18:16:17.459028] "GET /projects/260 HTTP/1.1" 404 962',
                r'36.66.116.191 - [2022-07-06 18:16:17.675593] "GET /projects/260 HTTP/1.1" 301 382']

for i in test_strings:
    sys.stdout.write("{}\n".format(i))
    sys.stdout.flush()
