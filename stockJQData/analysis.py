#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-14 16:57
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    :
# @File    : jqdata.py
# @Software: PyCharm

from jqdatasdk import *
from jqdatasdk.technical_analysis import *
auth('18620668927', 'minpeng123')


# 定义股票池列表
security_list1 = '000001.XSHE'
security_list2 = ['000001.XSHE', '000002.XSHE', '601211.XSHG', '603177.XSHG']


def kjd():
    """
    KDJ-随机指数
    :return:
    """
    # 计算并输出 security_list1 的 KDJ 值
    K1, D1, J1 = KDJ(security_list1, check_date='2017-01-04', N=9, M1=3, M2=3)
    print(K1[security_list1])
    print(D1[security_list1])
    print(J1[security_list1])

    # 输出 security_list2 的 KDJ 值
    K2, D2, J2 = KDJ(security_list2, check_date='2017-01-04', N=9, M1=3, M2=3)
    for stock in security_list2:
        print(K2[stock])
        print(D2[stock])
        print(J2[stock])


def mtm():
    """
    MTM-动量线
    :return:
    """
    # 计算并输出 security_list1 的 MTM 值
    MTM1 = MTM(security_list1, check_date='2017-01-04', timeperiod=12)
    print(MTM1[security_list1])

    # 输出 security_list2 的 MTM 值
    MTM2 = MTM(security_list2, check_date='2017-01-04', timeperiod=12)
    for stock in security_list2:
        print(MTM2[stock])


def rsi():
    """
    RSI-相对强弱指标
    :return:
    """
    # 计算并输出 security_list1 的 RSI 值
    RSI1 = RSI(security_list1, check_date='2017-01-04', N1=6)
    print(RSI1[security_list1])

    # 输出 security_list2 的 RSI 值
    RSI2 = RSI(security_list2, check_date='2017-01-04', N1=6)
    for stock in security_list2:
        print(RSI2[stock])



def vpt():
    """
    VPT-量价曲线
    :return:
    """
    VPT1 = VPT(security_list1, check_date='2017-01-04', N=51, M=6)
    print(VPT1[security_list1])

    # 输出 security_list2 的 VPT 值
    VPT2 = VPT(security_list2, check_date='2017-01-04', N=51, M=6)
    for stock in security_list2:
        print(VPT2[stock])


def cry():
    """
    CYR-市场强弱
    :return:
    """
    # 计算并输出 security_list1 的 CYR 值
    CYR1, MACYR1 = CYR(security_list1, check_date='2017-01-04', N=13, M=5)
    print(CYR1[security_list1])
    print(MACYR1[security_list1])

    # 输出 security_list2 的 CYR 值
    CYR2, MACYR2 = CYR(security_list2, check_date='2017-01-04', N=13, M=5)
    for stock in security_list2:
        print(CYR2[stock])
        print(MACYR2[stock])


def hsl():
    """
    HSL-换手线
    :return:
    """
    # 计算并输出 security_list1 的 HSL 值
    HSL1, MAHSL1 = HSL(security_list1, check_date='2017-01-04', N=5)
    print(HSL1[security_list1])
    print(MAHSL1[security_list1])

    # 输出 security_list2 的 HSL 值
    HSL2, MAHSL2 = HSL(security_list2, check_date='2017-01-04', N=5)
    for stock in security_list2:
        print(HSL2[stock])
        print(MAHSL2[stock])


def amv():
    """
    AMV-成本价均线
    :return:
    """
    # 计算并输出 security_list1 的 AMV 值
    AMV1 = AMV(security_list1, check_date='2017-01-04', timeperiod=13)
    print(AMV1[security_list1])

    # 输出 security_list2 的 AMV 值
    AMV2 = AMV(security_list2, check_date='2017-01-04', timeperiod=13)
    for stock in security_list2:
        print(AMV2[stock])


def ma():
    """
    MA-均线
    :return:
    """
    # 计算并输出 security_list1 的 MA 值
    MA1 = MA(security_list1, check_date='2017-01-04', timeperiod=5)
    print(MA1[security_list1])

    # 输出 security_list2 的 MA 值
    MA2 = MA(security_list2, check_date='2017-01-04', timeperiod=5)
    for stock in security_list2:
        print(MA2[stock])


def boll():
    """
    BOLL-布林线
    :return:
    """
    # 计算并输出 security_list1 的 BOLL 值
    upperband, middleband, lowerband = Bollinger_Bands(
        security_list1, check_date='2017-01-04', timeperiod=20, nbdevup=2, nbdevdn=2)
    print(upperband[security_list1])
    print(middleband[security_list1])
    print(lowerband[security_list1])

    # 输出 security_list2 的 BOLL 值
    upperband, middleband, lowerband = Bollinger_Bands(
        security_list2, check_date='2017-01-04', timeperiod=20, nbdevup=2, nbdevdn=2)
    for stock in security_list2:
        print(upperband[stock])
        print(middleband[stock])
        print(lowerband[stock])


def ene():
    """
    ENE-轨道线
    :return:
    """
    # 计算并输出 security_list1 的 ENE 值
    up1, low1, ENE1 = ENE(
        security_list1, check_date='2017-01-04', N=25, M1=6, M2=6)
    print(up1[security_list1])
    print(low1[security_list1])
    print(ENE1[security_list1])

    # 输出 security_list2 的 ENE 值
    up2, low2, ENE2 = ENE(
        security_list2, check_date='2017-01-04', N=25, M1=6, M2=6)
    for stock in security_list2:
        print(up2[stock])
        print(low2[stock])
        print(ENE2[stock])


def wvad():
    """
    WVAD-威廉变异离散量
    :return:
    """
    # 计算并输出 security_list1 的 WVAD 值
    wvad_wvad, wvad_mawvad = WVAD(
        security_list1, check_date='2017-01-04', N=24, M=6)
    print(wvad_wvad[security_list1])
    print(wvad_mawvad[security_list1])

    # 输出 security_list2 的 WVAD 值
    wvad_wvad, wvad_mawvad = WVAD(
        security_list2, check_date='2017-01-04', N=24, M=6)
    for stock in security_list2:
        print(wvad_wvad[stock])
        print(wvad_mawvad[stock])


def obv():
    """
    OBV-累积能量线
    :return:
    """
    # 计算并输出 security_list1 的 OBV 值
    OBV1 = OBV(security_list1, check_date='2017-01-04', timeperiod=30)
    print(OBV1[security_list1])

    # 输出 security_list2 的 OBV 值
    OBV2 = OBV(security_list2, check_date='2017-01-04', timeperiod=30)
    for stock in security_list2:
        print(OBV2[stock])


def psy():
    """
    PSY-心理线
    :return:
    """
    # 计算并输出 security_list1 的 PSY 值
    PSY1 = PSY(security_list1, check_date='2017-01-04', timeperiod=14)
    print(PSY1[security_list1])

    # 输出 security_list2 的 PSY 值
    PSY2 = PSY(security_list2, check_date='2017-01-04', timeperiod=14)
    for stock in security_list2:
        print(PSY2[stock])


def kd():
    """
    KD-随机指标KD
    :return:
    """
    # 计算并输出 security_list1 的 KD值
    K1, D1 = KD(security_list1, check_date='2017-01-04', N=9, M1=3, M2=3)
    print(K1[security_list1])
    print(D1[security_list1])

    # 输出 security_list2 的 KD 值
    K2, D2 = KD(security_list2, check_date='2017-01-04', N=9, M1=3, M2=3)
    for stock in security_list2:
        print(K2[stock])
        print(D2[stock])


def wr():
    """
    WR-威廉指标
    :return:
    """
    # 计算并输出 security_list1 的 WR 值
    WR1, MAWR1 = WR(security_list1, check_date='2017-01-04', N=10, N1=6)
    print(WR1[security_list1])
    print(MAWR1[security_list1])

    # 输出 security_list2 的 WR 值
    WR2, MAWR2 = WR(security_list2, check_date='2017-01-04', N=10, N1=6)
    for stock in security_list2:
        print(WR2[stock])
        print(MAWR2[stock])


def roc():
    """
    ROC-变动率指标
    :return:
    """
    # 计算并输出 security_list1 的 ROC 值
    ROC1 = ROC(security_list1, check_date='2017-01-04', timeperiod=12)
    print(ROC1[security_list1])

    # 输出 security_list2 的 ROC 值
    ROC2 = ROC(security_list2, check_date='2017-01-04', timeperiod=12)
    for stock in security_list2:
        print(ROC2[stock])


def macd():
    """
    MACD-平滑异同平均
    :return:
    """
    # 计算并输出 security_list1 的 MACD 值
    macd_dif, macd_dea, macd_macd = MACD(
        security_list1, check_date='2017-01-04', SHORT=12, LONG=26, MID=9)
    print(macd_dif[security_list1])
    print(macd_dea[security_list1])
    print(macd_macd[security_list1])

    # 输出 security_list2 的 MACD 值
    macd_dif, macd_dea, macd_macd = MACD(
        security_list2, check_date='2017-01-04', SHORT=12, LONG=26, MID=9)
    for stock in security_list2:
        print(macd_dif[stock])
        print(macd_dea[stock])
        print(macd_macd[stock])

macd()
