#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-22 15:46
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : factorforindex.py
# @Software: PyCharm

"""
##      因子说明
###     KDJ-随机指数
        MTM-动量线
        RSI-相对强弱指标
        VPT-量价曲线
        CYR-市场强弱
        HSL-换手线
        AMV-成本价均线
        MA-均线
        BOLL-布林线
        ENE-轨道线

        CCL-持仓量（适用于期货）
        WVAD-威廉变异离散量
        OBV-累积能量线
        PSY-心理线
        KD-随机指标KD
        WR-威廉指标
        ROC-变动率指标
        MACD-平滑异同平均
参考    https://www.joinquant.com/help/api/help?name=technicalanalysis#%E5%9B%A0%E5%AD%90%E8%AF%B4%E6%98%8E
"""

from jqdatasdk import *
from jqdatasdk.technical_analysis import *
auth('18620668927', 'minpeng123')

def uu_kdj():
    """
    KDJ-随机指标
    :param security_list：股票列表
            check_date：要查询数据的日期
            N：统计的天数 N
            M1：统计的天数 M1
            M2：统计的天数 M2
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :param stockTuShare:
    :rtype :dict
    :return:K，D和J 的值
    :用法 :  1.指标>80 时，回档机率大；指标<20时，反弹机率大；
            2.K在20左右向上交叉D时，视为买进信号；
            3.K在80左右向下交叉D时，视为卖出信号；
            4.J>100 时，股价易反转下跌；J<0 时，股价易反转上涨；
            5.KDJ 波动于50左右的任何信号，其作用不大。
    """
    kdj = KDJ('000001.XSHE', check_date='2019-05-13', N=9, M1=3, M2=3)
    return kdj

def uu_mtm():
    """
    MTM-动量线
    :param :security_list：股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数 N
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:MTM的值
    :用法 :MTM线　:当日收盘价与N日前的收盘价的差； MTMMA线:对上面的差值求N日移动平均； 参数：N 间隔天数，也是求移动平均的天数，一般取6用法：
                1.MTM从下向上突破MTMMA，买入信号；
                2.MTM从上向下跌破MTMMA，卖出信号；
                3.股价续创新高，而MTM未配合上升，意味上涨动力减弱；
                4.股价续创新低，而MTM未配合下降，意味下跌动力减弱；
                5.股价与MTM在低位同步上升，将有反弹行情；反之，从高位同步下降，将有回落走势
    """
    mtm = MTM('000001.XSHE',check_date='2017-01-04', timeperiod=12)
    return mtm

def uu_rsi():
    """
    RSI-相对强弱指标
    :param :security_list：股票列表
            check_date：要查询数据的日期
            N1：统计的天数N1
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:RSI 的值
    : 用法 :1.RSI>80 为超买，RSI<20 为超卖；
            2.RSI 以50为中界线，大于50视为多头行情，小于50视为空头行情；
            3.RSI 在80以上形成Ｍ头或头肩顶形态时，视为向下反转信号；
            4.RSI 在20以下形成Ｗ底或头肩底形态时，视为向上反转信号；
            5.RSI 向上突破其高点连线时，买进；RSI 向下跌破其低点连线时，卖出
    """
    rsi = RSI('000001.XSHE', check_date='2017-01-04', N1=6)
    return rsi

def uu_vpt():
    """
    VPT-量价曲线
    :param :security_list: 股票列表
            check_date: 要查询数据的日期
            N: 统计的天数 N
            M: 统计的天数 M
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:VPT 和 MAVPT 的值
    : 用法 :1.VPT 由下往上穿越0 轴时，为买进信号；
            2.VPT 由上往下穿越0 轴时，为卖出信号；
            3.股价一顶比一顶高，VPT 一顶比一顶低时，暗示股价将反转下跌；
            4.股价一底比一底低，VPT 一底比一底高时，暗示股价将反转上涨；
            5.VPT 可搭配EMV 和WVAD指标使用效果更佳
    """
    vpt = VPT('000001.XSHE',context.previous_date, N= 51, M = 6)
    return vpt

def uu_cyr():
    """
    CYR-市场强弱
    :param :security_list：股票列表
            check_date：要查询数据的日期
            N：统计的天数 N
            M：统计的天数 M
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:CYR 和 MACYR 的值
    : 用法 :CYR是成本均线派生出的指标,是13日成本均线的升降幅度;
            使用CYR可以对股票的强弱进行排序,找出其中的强势和弱势股票
    """
    cyr = CYR('000001.XSHE', check_date='2017-01-04', N = 13, M = 5)
    return cyr


def uu_hsl():
    """
    HSL-换手线
    :param :security_list：股票列表
            check_date：要查询数据的日期
            N：统计的天数 N
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:HSL和MAHSL 的值
    : 用法 :换手线是根据换手率绘制的曲线，使对于成交量的研判
            不受股本变动的影响，更增加了成交量具有可比性。
    """
    hsl = HSL('000001.XSHE', check_date='2017-01-04', N = 5)
    return hsl

def uu_amv():
    """
    AMV-成本价均线
    :param :security_list：股票列表
            check_date: 要查询数据的日期
            timeperiod：统计的天数
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:AMV的值
    : 用法 :成本价均线不同于一般移动平均线系统，成本价均线系统首次将成交量引入均线系统，充分提高均线系统的可靠性。
            同样对于成本价均线可以使用月均线系统(5,10,20,250)和季均线系统(20,40,60,250),另外成本价均线还可
            以使用自身特有的均线系统(5,13,34,250),称为市场平均建仓成本均线，简称成本价均线。在四个均线中参数为250的
            均线为年度均线,为行情支撑均线。成本均线不容易造成虚假信号或骗线，比如某日股价无量暴涨，移动均线会大幅拉升，
            但成本均线却不会大幅上升，因为在无量的情况下市场持仓成本不会有太大的变化。依据均线理论，当短期均线站在长期
            均线之上时叫多头排列，反之就叫空头排列。短期均线上穿长期均线叫金叉，短期均线下穿长期均线叫死叉。均线的多头
            排列是牛市的标志，空头排列是熊市的标志。均线系统一直是市场广泛认可的简单而可靠的分析指标，其使用要点是尽量
            做多头排列的股票，回避空头排列的股票。34日成本线是市场牛熊的重要的分水岭。一旦股价跌破34日成本线，则常常是最后的出逃机会
    """
    amv = AMV('000001.XSHE',check_date='2017-01-04', timeperiod=13)
    return amv

def uu_ma():
    """
    MA-均线
    :param :security_list：股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数timeperiod
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:MA 的值
    : 用法 :1.股价高于平均线，视为强势；股价低于平均线，视为弱势
            2.平均线向上涨升，具有助涨力道；平均线向下跌降，具有助跌力道；
            3.二条以上平均线向上交叉时，买进；
            4.二条以上平均线向下交叉时，卖出；
            5.移动平均线的信号经常落后股价，若以EXPMA 、VMA 辅助，可以改善
    """
    ma = MA('000001.XSHE', check_date='2017-01-04', timeperiod=5)
    return ma

def uu_boll():
    """
    BOLL-布林线
    :param :security_list：股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数timeperiod
            nbdevup：统计的天数 nbdevup
            nbdevdn：统计的天数 nbdevdn
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:上轨线UB 、中轨线MB、下轨线LB 的值
    : 用法 :1.股价上升穿越布林线上限时，回档机率大；
            2.股价下跌穿越布林线下限时，反弹机率大；
            3.布林线震动波带变窄时，表示变盘在即；
            4.BOLL须配合BB 、WIDTH 使用
    """
    boll = Bollinger_Bands('000001.XSHE', check_date='2017-01-04', timeperiod=20, nbdevup=2, nbdevdn=2)
    return boll

def uu_ene():
    """
    ENE-轨道线
    :param :security_list：股票列表
            check_date: 要查询数据的日期
            N：统计的天数
            M1：统计的天数
            M2：统计的天数
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:UPPER LOWER ENE的值
    : 用法 :1.股价上升穿越轨道线上限时，回档机率大；
            2.股价下跌穿越轨道线下限时，反弹机率大；
            3.股价波动于轨道线内时，代表常态行情，此时，超买超卖指标可发挥效用；
            4.股价波动于轨道线外时，代表脱轨行情，此时，应使用趋势型指标
    """
    ene = ENE('000001.XSHE',check_date='2017-01-04',N=25,M1=6,M2=6)
    return ene

def uu_wvad():
    """
    WVAD-威廉变异离散量
    :param :security_list：股票列表
            check_date：要查询数据的日期
            N：统计的天数 N
            M：统计的天数 M
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:WVAD 和 MAWVAD的值
    : 用法 :1.WVAD由下往上穿越0 轴时，视为长期买进信号；
            2.WVAD由上往下穿越0 轴时，视为长期卖出信号；
            3.当ADX 低于±DI时，本指标失去效用；
            4.长期使用WVAD指标才能获得最佳利润；
            5.本指标可与EMV 指标搭配使用
    """
    wvad = WVAD('000001.XSHE',check_date='2017-01-04', N = 24, M = 6)
    return wvad

def uu_bov():
    """
    OBV-累积能量线
    :param :security_list：股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数 N
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:OBV 的值
    : 用法 :1.股价一顶比一顶高，而OBV 一顶比一顶低，暗示头部即将形成；
            2.股价一底比一底低，而OBV 一底比一底高，暗示底部即将形成；
            3.OBV 突破其Ｎ字形波动的高点次数达5 次时，为短线卖点；
            4.OBV 跌破其Ｎ字形波动的低点次数达5 次时，为短线买点；
            5.OBV 与ADVOL、PVT、WAD、ADL同属一组指标群，使用时应综合研判
    """
    bov = OBV('000001.XSHE',check_date='2017-01-04', timeperiod=30)
    return bov

def uu_psy():
    """
    PSY-心理线
    :param :security_list：股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数 N
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:PSY 的值
    : 用法 :1.PSY>75，形成Ｍ头时，股价容易遭遇压力；
            2.PSY<25，形成Ｗ底时，股价容易获得支撑；
            3.PSY 与VR 指标属一组指标群，须互相搭配使用
    """
    psy = PSY('000001.XSHE',check_date='2017-01-04', timeperiod=14)
    return psy

def uu_kd():
    """
    KD-随机指标KD
    :param :security_list：股票列表
            check_date：要查询数据的日期
            N：统计的天数 N
            M1：统计的天数 M1
            M2：统计的天数 M2
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:K和D 的值
    : 用法 :1.KD的计算公式与SKDJ的不太大，而常见的炒股软件中均没有找到KD的用法注释，所以该处的用法注释使用的是公式SKDJ的；
            2.指标>80 时，回档机率大；指标<20 时，反弹机率大；
            3.K在20左右向上交叉D时，视为买进信号；
            4.K在80左右向下交叉D时，视为卖出信号；
            5.SKDJ波动于50左右的任何讯号，其作用不大
    """
    kd = KD('000001.XSHE', check_date = '2017-01-04', N = 9, M1 = 3, M2 = 3)
    return kd

def uu_wr():
    """
    WR-威廉指标
    :param :security_list：股票列表
            check_date：要查询数据的日期
            N：统计的天数 N
            M：统计的天数 M
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:WR和MAWR 的值
    : 用法 :1.WR波动于0 - 100，100置于顶部，0置于底部。
            2.本指标以50为中轴线，高于50视为股价转强；低于50视为股价转弱
            3.本指标高于20后再度向下跌破20，卖出；低于80后再度向上突破80，买进。
            4.WR连续触底3 - 4次，股价向下反转机率大；连续触顶3 - 4次，股价向上反转机率大
    """
    wr = WR('000001.XSHE', check_date = '2017-01-04', N = 10, N1 = 6)
    return wr

def uu_roc():
    """
    ROC-变动率指标
    :param :security_list：股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数 N
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return: ROC的值
    : 用法 :1.本指标的超买超卖界限值随个股不同而不同，使用者应自行调整；
            2.本指标的超买超卖范围，一般介于±6.5之间；
            3.本指标用法请参考MTM 指标用法；
            4.本指标可设参考线
    """
    roc = ROC('000001.XSHE',check_date='2017-01-04', timeperiod=12)
    return roc

def uu_macd():
    """
    MACD-平滑异同平均
    :param :security_list：股票列表
            check_date：要查询数据的日期
            SHORT：统计的天数 SHORT
            LONG：统计的天数 LONG
            MID：统计的天数 MID
            unit：统计周期，默认为 '1d', 支持如下周期: '1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'. '1w' 表示一周, ‘1M' 表示一月
            include_now：是否包含当前周期，默认为 True
    :rtype :dict
    :return:DIF, DEA和MACD的值
    DIFF线　收盘价短期、长期指数平滑移动平均线间的差 DEA线　
    DIFF线的M日指数平滑移动平均线 MACD线　DIFF线与DEA线的差，彩色柱状线 参数：SHORT(短期)、LONG(长期)、M 天数，一般为12、26、9

    用法： 1.DIFF、DEA均为正，DIFF向上突破DEA，买入信号。
            2.DIFF、DEA均为负，DIFF向下跌破DEA，卖出信号。
            3.DEA线与K线发生背离，行情反转信号。
            4.分析MACD柱状线，由红变绿(正变负)，卖出信号；由绿变红，买入信号
    """
    macd = MACD('000001.XSHE',check_date='2017-01-04', SHORT = 12, LONG = 26, MID = 9)
    return macd