#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:08
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : listedCompanyShareholderInfo.py
# @Software: PyCharm

"""
##   获取上市公司股东和股本信息
###  十大股东
     十大流通股东
     股东股份质押
     股东股份冻结
     股东户数
     大股东增减持
     受限股份实际解禁日期
     上市公司股本变动
参考  https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E8%82%A1%E4%B8%9C%E5%92%8C%E8%82%A1%E6%9C%AC%E4%BF%A1%E6%81%AF
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_query_STK_SHAREHOLDER_TOP10():
    """
    十大股东
    获取上市公司前十大股东的持股情况，包括持股数量，所持股份性质，变动原因等
    :param :query(finance.STK_SHAREHOLDER_TOP10)：表示从finance.STK_SHAREHOLDER_TOP10这张表中查询上市公司前十大股东的持股情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_SHAREHOLDER_TOP10：代表上市公司十大股东表，收录了上市公司前十大股东的持股情况，包括持股数量，所持股份性质，变动原因等。表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            company_name	公司名称	varchar(100)	在此是指上市公司的名称
            code	股票代码	varchar(12)
            end_date	截止日期	date	公告中统计的十大股东截止到某一日期的更新情况。
            pub_date	公告日期	date	公告中会提到十大股东的更新情况。
            change_reason_id	变动原因编码	int
            change_reason	变动原因	varchar(120)
            shareholder_rank	股东名次	int
            shareholder_name	股东名称	varchar(200)
            shareholder_name_en	股东名称（英文）	varchar(200)
            shareholder_id	股东ID	int
            shareholder_class_id	股东类别编码	int
            shareholder_class	股东类别	varchar(150)	包括:券商、社保基金、证券投资基金、保险公司、QFII、其它机构、个人等
            share_number	持股数量	decimal(10,4)	股
            share_ratio	持股比例	decimal(10,4)	%
            sharesnature_id	股份性质编码	int
            sharesnature	股份性质	varchar(120)	包括:国家股、法人股、个人股外资股、流通A股、流通B股、职工股、发起人股、转配股等
            share_pledge_freeze	股份质押冻结数量	decimal(10,4)	如果股份质押数量和股份冻结数量任意一个字段有值，则等于后两者之和
            share_pledge	股份质押数量	decimal(10,4)
            share_freeze	股份冻结数量	decimal(10,4)
            filter(finance.STK_SHAREHOLDER_TOP10.code==code)：指定筛选条件，通过finance.STK_SHAREHOLDER_TOP10.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHAREHOLDER_TOP10.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的十大股东情况，限定返回条数为10条
    q = query(finance.STK_SHAREHOLDER_TOP10).filter(finance.STK_SHAREHOLDER_TOP10.code == '600276.XSHG',
                                                    finance.STK_SHAREHOLDER_TOP10.pub_date > '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_SHAREHOLDER_FLOATING_TOP10():
    """
    十大流通股东
    获取上市公司前十大流通股东的持股情况，包括持股数量，所持股份性质，变动原因等
    :param :query(finance.STK_SHAREHOLDER_FLOATING_TOP10)：表示从finance.STK_SHAREHOLDER_FLOATING_TOP10这张表中查询上市公司前十大流通股东的持股情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_SHAREHOLDER_FLOATING_TOP10：代表上市公司十大流通股东表，收录了上市公司前十大流通股东的持股情况，包括持股数量，所持股份性质，变动原因等。表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            end_date	截止日期	date
            pub_date	公告日期	date
            change_reason_id	变动原因编码	int
            change_reason	变动原因	varchar(120)
            shareholder_rank	股东名次	int
            shareholder_id	股东ID	int
            shareholder_name	股东名称	varchar(200)
            shareholder_name_en	股东名称（英文）	varchar(150)
            shareholder_class_id	股东类别编码	int
            shareholder_class	股东类别	varchar(150)
            share_number	持股数量	int	股
            share_ratio	持股比例	decimal(10,4)	%
            sharesnature_id	股份性质编码	int
            sharesnature	股份性质	varchar(120)
            filter(finance.STK_SHAREHOLDER_FLOATING_TOP10.code==code)：指定筛选条件，通过finance.STK_SHAREHOLDER_FLOATING_TOP10.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHAREHOLDER_FLOATING_TOP10.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的十大流通股东情况，返回条数为10条
    q = query(finance.STK_SHAREHOLDER_FLOATING_TOP10).filter(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code == '600276.XSHG',
        finance.STK_SHAREHOLDER_FLOATING_TOP10.pub_date > '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_SHARES_PLEDGE():
    """
    股东股份质押
    获取上市公司股东股份的质押情况
    :param :query(finance.STK_SHARES_PLEDGE)：表示从finance.STK_SHARES_PLEDGE这张表中查询上市公司股东股份的质押情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_SHARES_PLEDGE：代表上市公司股东股份质押表，收录了上市公司股东股份的质押情况。表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            pub_date	公告日期	date
            pledgor_id	出质人ID	int
            pledgor	出质人	varchar(100)	将资产质押出去的人成为出质人
            pledgee	质权人	varchar(100)
            pledge_item	质押事项	varchar(500)	质押原因，记录借款人、借款金额、币种等内容
            pledge_nature_id	质押股份性质编码	int
            pledge_nature	质押股份性质	varchar(120)
            pledge_number	质押数量	int	股
            pledge_total_ratio	占总股本比例	decimal(10,4)	%
            start_date	质押起始日	date
            end_date	质押终止日	date
            unpledged_date	质押解除日	date
            unpledged_number	质押解除数量	int
            unpledged _detail	解除质押说明	varchar(1000)
            is_buy_back	是否质押式回购交易	char(1)
            filter(finance.STK_SHARES_PLEDGE.code==code)：指定筛选条件，通过finance.STK_SHARES_PLEDGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHARES_PLEDGE.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为万科（000002.XSHE)的股东股份质押情况，返回条数为10条
    q = query(finance.STK_SHARES_PLEDGE).filter(finance.STK_SHARES_PLEDGE.code == '000002.XSHE',
                                                finance.STK_SHARES_PLEDGE.pub_date > '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df


def uu_query_STK_SHARES_FROZEN():
    """
    股东股份冻结
    获取上市公司股东股份的冻结情况
    :param :query(finance.STK_SHARES_FROZEN)：表示从finance.STK_SHARES_FROZEN这张表中查询股东股份的冻结情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_SHARES_FROZEN：代表上市公司股东股份冻结表，收录了上市公司股东股份的冻结情况，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            pub_date	公告日期	date
            code	股票代码	varchar(12)
            frozen_person_id	被冻结当事人ID	int
            frozen_person	被冻结当事人	varchar(100)
            frozen_reason	冻结事项	varchar(600)
            frozen_share_nature_id	被冻结股份性质编码	int
            frozen_share_nature	被冻结股份性质	varchar(120)	包括:国家股、法人股、个人股、外资股、流通A股、流通B股、职工股、发起人股、转配股
            frozen_number	冻结数量	int	股
            frozen_total_ratio	占总股份比例	decimal(10,4)	%
            freeze_applicant	冻结申请人	varchar(100)
            freeze_executor	冻结执行人	varchar(100)
            start_date	冻结起始日	date
            end_date	冻结终止日	date
            unfrozen_date	解冻日期	date	分批解冻的为最近一次解冻日期
            unfrozen_number	累计解冻数量	int	原解冻数量
            unfrozen_detail	解冻处理说明	varchar(1000)	冻结过程及结束后的处理结果
            filter(finance.STK_SHARES_FROZEN.code==code)：指定筛选条件，通过finance.STK_SHARES_FROZEN.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHARES_FROZEN.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为文一科技（600520.XSHG)的股东股份冻结情况，返回条数为10条
    q = query(finance.STK_SHARES_FROZEN).filter(finance.STK_SHARES_FROZEN.code == '600520.XSHG',
                                                finance.STK_SHARES_FROZEN.pub_date > '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df


def uu_query_STK_HOLDER_NUM():
    """
    股东户数
    获取上市公司全部股东户数，A股股东、B股股东、H股股东的持股户数
    :param :query(finance.STK_HOLDER_NUM)：表示从finance.STK_HOLDER_NUM这张表中查询上市公司的股东户数，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_HOLDER_NUM：代表上市公司股东户数表，收录了上市公司全部股东户数，A股股东、B股股东、H股股东的持股户数情况，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            code	股票代码	varchar(12)
            pub_date	公告日期	date
            end_date	截止日期	date
            share_holders	股东总户数	int
            a_share_holders	A股股东总户数	int
            b_share_holders	B股股东总户数	int
            h_share_holders	H股股东总户数	int
            filter(finance.STK_HOLDER_NUM.code==code)：指定筛选条件，通过finance.STK_HOLDER_NUM.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_HOLDER_NUM.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为万科（000002.XSHE)的股东户数情况，返回条数为10条
    q = query(finance.STK_HOLDER_NUM).filter(finance.STK_HOLDER_NUM.code == '000002.XSHE',
                                             finance.STK_HOLDER_NUM.pub_date > '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df


def uu_query_STK_SHAREHOLDERS_SHARE_CHANGE():
    """
    大股东增减持
    获取上市公司大股东的增减持情况
    :param :query(finance.STK_SHAREHOLDERS_SHARE_CHANGE)：表示从finance.STK_SHAREHOLDERS_SHARE_CHANGE这张表中查询上市公司大股东的增减持情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_SHAREHOLDERS_SHARE_CHANGE：代表上市公司大股东增减持情况表，收录了大股东的增减持情况，表结构和字段信息如下：

            段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            pub_date	公告日期	date
            end_date	增（减）持截止日	date	变动截止日期
            type	增（减）持类型	int	0--增持;1--减持
            shareholder_id	股东ID	int
            shareholder_name	股东名称	varchar(100)
            change_number	变动数量	int	股
            change_ratio	变动数量占总股本比例	decimal(10,4)	录入变动数量后，系统自动计算变动比例，持股比例可以用持股数量除以股本情况表中的总股本
            price_ceiling	增（减）持价格上限	varchar(100)
            after_change_ratio	变动后占比	decimal(10,4)	%，变动后持股数量占总股本比例
            filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code==code)：指定筛选条件，通过finance.STK_SHAREHOLDERS_SHARE_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为万科（000002.XSHE)的大股东增减持情况，返回条数为10条
    q = query(finance.STK_SHAREHOLDERS_SHARE_CHANGE).filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code == '000002.XSHE',
                                                            finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date > '2015-01-01').limit(
        10)
    df = finance.run_query(q)
    return df


def uu_query_STK_LIMITED_SHARES_UNLIMIT():
    """
    受限股份实际解禁日期
    获取公司已上市的受限股份实际解禁的日期
    :param :query(finance.STK_LIMITED_SHARES_UNLIMIT)：表示从finance.STK_LIMITED_SHARES_UNLIMIT这张表中查询上市公司受限股份实际解禁的日期，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_LIMITED_SHARES_UNLIMIT：代表上市公司受限股份实际解禁表，收录了上市公司受限股份实际解禁的日期信息，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            pub_date	公告日期	date
            shareholder_name	股东名称	varchar(100)
            actual_unlimited_date	实际解除限售日期	date
            actual_unlimited_number	实际解除限售数量	int	股
            actual_unlimited_ratio	实际解除限售比例	decimal(10,4)	实际解除限售数量占总股本比例，单位%
            limited_reason_id	限售原因编码	int
            limited_reason	限售原因	varchar(60)
            actual_trade_number	实际可流通数量	int
            filter(finance.STK_LIMITED_SHARES_UNLIMIT.code==code)：指定筛选条件，通过finance.STK_LIMITED_SHARES_UNLIMIT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_LIMITED_SHARES_UNLIMIT.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的受限股份实际解禁日期，返回条数为10条
    q = query(finance.STK_LIMITED_SHARES_UNLIMIT).filter(finance.STK_LIMITED_SHARES_UNLIMIT.code == '600276.XSHG',
                                                         finance.STK_LIMITED_SHARES_UNLIMIT.pub_date > '2015-01-01').limit(
        10)
    df = finance.run_query(q)
    return df

def uu_query_STK_CAPITAL_CHANGE():
    """
    上市公司股本变动
    获取上市公司的股本变动情况
    :param :query(finance.STK_CAPITAL_CHANGE)：表示从finance.STK_CAPITAL_CHANGE这张表中查询股票简称的变更情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_CAPITAL_CHANGE：代表上市公司的股本变动表，收录了上市公司发生上市、增发、配股，转增等时间带来的股本变动情况。表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            change_date	变动日期	date
            pub_date	公告日期	date
            change_reason_id	变动原因编码	int
            change_reason	变动原因	varchar(120)
            share_total	总股本	decimal(20,4)	未流通股份+已流通股份，单位：万股
            share_non_trade	未流通股份	decimal(20,4)	发起人股份 + 募集法人股份 + 内部职工股 + 优先股+转配股+其他未流通股+配售法人股+已发行未上市股份
            share_start	发起人股份	decimal(20,4)	国家持股 +国有法人持股+境内法人持股 + 境外法人持股 + 自然人持股
            share_nation	国家持股	decimal(20,4)
            share_nation_legal	国有法人持股	decimal(20,4)
            share_instate_legal	境内法人持股	decimal(20,4)
            share_outstate_legal	境外法人持股	decimal(20,4)
            share_natural	自然人持股	decimal(20,4)
            share_raised	募集法人股	decimal(20,4)
            share_inside	内部职工股	decimal(20,4)
            share_convert	转配股	decimal(20,4)
            share_perferred	优先股	decimal(20,4)
            share_other_nontrade	其他未流通股	decimal(20,4)
            share_limited	流通受限股份	decimal(20,4)
            share_legal_issue	配售法人股	decimal(20,4)	战略投资配售股份+证券投资基金配售股份+一般法人配售股份
            share_strategic_investor	战略投资者持股	decimal(20,4)
            share_fund	证券投资基金持股	decimal(20,4)
            share_normal_legal	一般法人持股	decimal(20,4)
            share_other_limited	其他流通受限股份	decimal(20,4)
            share_nation_limited	国家持股（受限）	decimal(20,4)
            share_nation_legal_limited	国有法人持股（受限）	decimal(20,4)
            other_instate_limited	其他内资持股（受限）	decimal(20,4)
            legal of other_instate_limited	其他内资持股（受限）中的境内法人持股	decimal(20,4)
            natural of other_instate_limited	其他内资持股（受限）中的境内自然人持股	decimal(20,4)
            outstate_limited	外资持股（受限）	decimal(20,4)
            legal of outstate_limited	外资持股（受限）中的境外法人持股	decimal(20,4)
            natural of outstate_limited	外资持股（受限）境外自然人持股	decimal(20,4)
            share_trade_total	已流通股份（自由流通股）	decimal(20,4)	人民币普通股 + 境内上市外资股（B股）+ 境外上市外资股（H股）+高管股+ 其他流通股
            share_rmb	人民币普通股	decimal(20,4)
            share_b	境内上市外资股（B股）	decimal(20,4)
            share_b_limited	限售B股	decimal（20,4）
            share_h	境外上市外资股（H股）	decimal(20,4)
            share_h_limited	限售H股	decimal(20,4)
            share_management	高管股	decimal(20,4)
            share_management_limited	限售高管股	decimal(20,4)
            share_other_trade	其他流通股	decimal(20,4)
            control_shareholder_limited	控股股东、实际控制人(受限)	decimal(20,4)
            core_employee_limited	核心员工(受限)	decimal(20,4)
            individual_fund_limited	个人或基金(受限)	decimal(20,4)
            other_legal_limited	其他法人(受限)	decimal(20,4)
            other_limited	其他(受限)	decimal(20,4)
            filter(finance.STK_CAPITAL_CHANGE.code==code)：指定筛选条件，通过finance.STK_CAPITAL_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_CAPITAL_CHANGE.pub_date>='2015-01-01'，表示筛选公布日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的股本变动情况，返回条数为10条
    q = query(finance.STK_CAPITAL_CHANGE).filter(finance.STK_CAPITAL_CHANGE.code == '600276.XSHG',
                                                 finance.STK_CAPITAL_CHANGE.pub_date > '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

#指定查询对象为恒瑞医药（600276.XSHG)的股本变动情况，返回条数为10条
q=query(finance.STK_CAPITAL_CHANGE).filter(finance.STK_CAPITAL_CHANGE.code=='600276.XSHG',finance.STK_CAPITAL_CHANGE.pub_date>'2015-01-01').limit(10)
df=finance.run_query(q)
print(df)