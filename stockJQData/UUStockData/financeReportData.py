#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:09
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : financeReportData.py
# @Software: PyCharm

"""
##   获取报告期财务数据
###  业绩预告
     合并利润表
     母公司利润表
     合并现金流量表
     母公司现金流量表
     合并资产负债表
     母公司资产负债表
     金融类合并利润表
     金融类母公司利润表
     金融类合并现金流量表
     金融类母公司现金流量表
     金融类合并资产负债表
     金融类母公司资产负债表
     财务报表补充科目
参考  https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E6%8A%A5%E5%91%8A%E6%9C%9F%E8%B4%A2%E5%8A%A1%E6%95%B0%E6%8D%AE
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_query_STK_FIN_FORCAST():
    """
    获取上市公司业绩预告等信息
    :param :query(finance.STK_FIN_FORCAST)：表示从finance.STK_FIN_FORCAST这张表中查询上市公司业绩报告的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_FIN_FORCAST：代表上市公司业绩预告表，收录了上市公司的业绩预告信息，表结构和字段信息如下：

            字段	名称	类型	注释
            company_id	公司ID	int
            code	股票代码	varchar(12)
            name	公司名称	varchar(64)
            end_date	报告期	date
            report_type_id	预告期类型编码	int	如下 预告期类型编码
            report_type	预告期类型	varchar(32)
            pub_date	公布日期	date
            type_id	预告类型编码	int	如下 业绩类型编码
            type	预告类型	varchar(32)
            profit_min	预告净利润（下限）	decimal(22,6)
            profit_max	预告净利润（上限）	decimal(22,6)
            profit_last	去年同期净利润	decimal(22,6)
            profit_ratio_min	预告净利润变动幅度(下限)	decimal(10,4)	单位：%
            profit_ratio_max	预告净利润变动幅度(上限)	decimal(10,4)	单位：%
            content	预告内容	varchar(2048)
            预告期类型编码

            预告期编码	预告期类型
            304001	一季度预告
            304002	中报预告
            304003	三季度预告
            304004	四季度预告
            业绩类型编码

            业绩类型编码	业绩类型
            305001	业绩大幅上升
            305002	业绩预增
            305003	业绩预盈
            305004	预计扭亏
            305005	业绩持平
            305006	无大幅变动
            305007	业绩预亏
            305008	业绩大幅下降
            305009	大幅减亏
            305010	业绩预降
            305011	预计减亏
            305012	不确定
            305013	取消预测
            filter(finance.STK_FIN_FORCAST.code==code)：指定筛选条件，通过finance.STK_FIN_FORCAST.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_FIN_FORCAST.pub_date>='2015-01-01'，表示公告日期在2015年1月1日之后发布的业绩预告；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公布的业绩预告信息，限定返回条数为10条
    q = query(finance.STK_FIN_FORCAST).filter(finance.STK_FIN_FORCAST.code == '600519.XSHG',
                                              finance.STK_FIN_FORCAST.pub_date >= '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_INCOME_STATEMENT(stock,pub_date = '2015-01-01'):
    """
    获取上市公司定期公告中公布的合并利润表数据
    :param :query(finance.STK_INCOME_STATEMENT)：表示从finance.STK_INCOME_STATEMENT这张表中查询上市公司定期公告中公布的合并利润表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_INCOME_STATEMENT：代表上市公司合并利润表，收录了上市公司定期公告中公布的合并利润表数据，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0：本期，1：上期
            source_id	报表来源编码	int	如下 报表来源编码
            source	报表来源	varchar(60)	选择时程序自动填入
            total_operating_revenue	营业总收入	decimal(20,4)
            operating_revenue	营业收入	decimal(20,4)
            total_operating_cost	营业总成本	decimal(20,4)
            operating_cost	营业成本	decimal(20,4)
            operating_tax_surcharges	营业税金及附加	decimal(20,4)
            sale_expense	销售费用	decimal(20,4)
            administration_expense	管理费用	decimal(20,4)
            exploration_expense	堪探费用	decimal(20,4)	勘探费用用于核算企业（石油天然气开采）核算的油气勘探过程中发生的地质调查、物理化学勘探各项支出和非成功探井等支出。
            financial_expense	财务费用	decimal(20,4)
            asset_impairment_loss	资产减值损失	decimal(20,4)
            fair_value_variable_income	公允价值变动净收益	decimal(20,4)
            investment_income	投资收益	decimal(20,4)
            invest_income_associates	对联营企业和合营企业的投资收益	decimal(20,4)
            exchange_income	汇兑收益	decimal(20,4)
            other_items_influenced_income	影响营业利润的其他科目	decimal(20,4)
            operating_profit	营业利润	decimal(20,4)
            subsidy_income	补贴收入	decimal(20,4)
            non_operating_revenue	营业外收入	decimal(20,4)
            non_operating_expense	营业外支出	decimal(20,4)
            disposal_loss_non_current_liability	非流动资产处置净损失	decimal(20,4)
            other_items_influenced_profit	影响利润总额的其他科目	decimal(20,4)
            total_profit	利润总额	decimal(20,4)
            income_tax	所得税	decimal(20,4)
            other_items_influenced_net_profit	影响净利润的其他科目	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            np_parent_company_owners	归属于母公司所有者的净利润	decimal(20,4)
            minority_profit	少数股东损益	decimal(20,4)
            eps	每股收益	decimal(20,4)
            basic_eps	基本每股收益	decimal(20,4)
            diluted_eps	稀释每股收益	decimal(20,4)
            other_composite_income	其他综合收益	decimal(20,4)
            total_composite_income	综合收益总额	decimal(20,4)
            ci_parent_company_owners	归属于母公司所有者的综合收益总额	decimal(20,4)
            ci_minority_owners	归属于少数股东的综合收益总额	decimal(20,4)
            interest_income	利息收入	decimal(20,4)
            premiums_earned	已赚保费	decimal(20,4)
            commission_income	手续费及佣金收入	decimal(20,4)
            interest_expense	利息支出	decimal(20,4)
            commission_expense	手续费及佣金支出	decimal(20,4)
            refunded_premiums	退保金	decimal(20,4)
            net_pay_insurance_claims	赔付支出净额	decimal(20,4)
            withdraw_insurance_contract_reserve	提取保险合同准备金净额	decimal(20,4)
            policy_dividend_payout	保单红利支出	decimal(20,4)
            reinsurance_cost	分保费用	decimal(20,4)
            non_current_asset_disposed	非流动资产处置利得	decimal(20,4)
            other_earnings	其他收益	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.STK_INCOME_STATEMENT.code==code)：指定筛选条件，通过finance.STK_INCOME_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_INCOME_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的合并利润表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公告的合并利润表数据，取出合并利润表中本期的营业总收入，归属于母公司的净利润
    q = query(finance.STK_INCOME_STATEMENT.company_name,
              finance.STK_INCOME_STATEMENT.code,
              finance.STK_INCOME_STATEMENT.pub_date,
              finance.STK_INCOME_STATEMENT.start_date,
              finance.STK_INCOME_STATEMENT.end_date,
              finance.STK_INCOME_STATEMENT.total_operating_revenue,
              finance.STK_INCOME_STATEMENT.np_parent_company_owners).filter(
        finance.STK_INCOME_STATEMENT.code == stock, finance.STK_INCOME_STATEMENT.pub_date >= pub_date,
        finance.STK_INCOME_STATEMENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_STK_INCOME_STATEMENT_PARENT():
    """
    获取上市公司母公司利润的信息
    :param :query(finance.STK_INCOME_STATEMENT_PARENT)：表示从finance.STK_INCOME_STATEMENT_PARENT这张表中查询上市公司母公司利润表的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_INCOME_STATEMENT_PARENT：代表上市公司母公司利润表，收录了上市公司母公司的利润信息，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            total_operating_revenue	营业总收入	decimal(20,4)
            operating_revenue	营业收入	decimal(20,4)
            total_operating_cost	营业总成本	decimal(20,4)
            operating_cost	营业成本	decimal(20,4)
            operating_tax_surcharges	营业税金及附加	decimal(20,4)
            sale_expense	销售费用	decimal(20,4)
            administration_expense	管理费用	decimal(20,4)
            exploration_expense	堪探费用	decimal(20,4)	勘探费用用于核算企业（石油天然气开采）核算的油气勘探过程中发生的地质调查、物理化学勘探各项支出和非成功探井等支出。
            financial_expense	财务费用	decimal(20,4)
            asset_impairment_loss	资产减值损失	decimal(20,4)
            fair_value_variable_income	公允价值变动净收益	decimal(20,4)
            investment_income	投资收益	decimal(20,4)
            invest_income_associates	对联营企业和合营企业的投资收益	decimal(20,4)
            exchange_income	汇兑收益	decimal(20,4)
            other_items_influenced_income	影响营业利润的其他科目	decimal(20,4)
            operating_profit	营业利润	decimal(20,4)
            subsidy_income	补贴收入	decimal(20,4)
            non_operating_revenue	营业外收入	decimal(20,4)
            non_operating_expense	营业外支出	decimal(20,4)
            disposal_loss_non_current_liability	非流动资产处置净损失	decimal(20,4)
            other_items_influenced_profit	影响利润总额的其他科目	decimal(20,4)
            total_profit	利润总额	decimal(20,4)
            income_tax	所得税	decimal(20,4)
            other_items_influenced_net_profit	影响净利润的其他科目	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            np_parent_company_owners	归属于母公司所有者的净利润	decimal(20,4)
            minority_profit	少数股东损益	decimal(20,4)
            eps	每股收益	decimal(20,4)
            basic_eps	基本每股收益	decimal(20,4)
            diluted_eps	稀释每股收益	decimal(20,4)
            other_composite_income	其他综合收益	decimal(20,4)
            total_composite_income	综合收益总额	decimal(20,4)
            ci_parent_company_owners	归属于母公司所有者的综合收益总额	decimal(20,4)
            ci_minority_owners	归属于少数股东的综合收益总额	decimal(20,4)
            interest_income	利息收入	decimal(20,4)
            premiums_earned	已赚保费	decimal(20,4)
            commission_income	手续费及佣金收入	decimal(20,4)
            interest_expense	利息支出	decimal(20,4)
            commission_expense	手续费及佣金支出	decimal(20,4)
            refunded_premiums	退保金	decimal(20,4)
            net_pay_insurance_claims	赔付支出净额	decimal(20,4)
            withdraw_insurance_contract_reserve	提取保险合同准备金净额	decimal(20,4)
            policy_dividend_payout	保单红利支出	decimal(20,4)
            reinsurance_cost	分保费用	decimal(20,4)
            non_current_asset_disposed	非流动资产处置利得	decimal(20,4)
            other_earnings	其他收益	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.STK_INCOME_STATEMENT_PARENT.code==code)：指定筛选条件，通过finance.STK_INCOME_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_INCOME_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的母公司利润表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公告的母公司利润表数据，取出母公司利润表中本期的营业总收入，归属于母公司所有者的净利润
    from jqdatasdk import finance
    q = query(finance.STK_INCOME_STATEMENT_PARENT.company_name,
              finance.STK_INCOME_STATEMENT_PARENT.code,
              finance.STK_INCOME_STATEMENT_PARENT.pub_date,
              finance.STK_INCOME_STATEMENT_PARENT.start_date,
              finance.STK_INCOME_STATEMENT_PARENT.end_date,
              finance.STK_INCOME_STATEMENT_PARENT.total_operating_revenue,
              finance.STK_INCOME_STATEMENT_PARENT.np_parent_company_owners,
              finance.STK_INCOME_STATEMENT_PARENT.eps).filter(
        finance.STK_INCOME_STATEMENT_PARENT.code == '600519.XSHG',
        finance.STK_INCOME_STATEMENT_PARENT.pub_date >= '2015-01-01',
        finance.STK_INCOME_STATEMENT_PARENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df


def uu_query_STK_CASHFLOW_STATEMENT(stock,pub_date = '2015-01-01'):
    """
    获取上市公司定期公告中公布的合并现金流量表数据
    :param :query(finance.STK_CASHFLOW_STATEMENT)：表示从finance.STK_CASHFLOW_STATEMENT这张表中查询上市公司定期公告中公布的合并现金流量表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_CASHFLOW_STATEMENT：代表上市公司合并现金流量表，收录了上市公司定期公告中公布的合并现金流量表数据，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            goods_sale_and_service_render_cash	销售商品、提供劳务收到的现金	decimal(20,4)
            tax_levy_refund	收到的税费返还	decimal(20,4)
            subtotal_operate_cash_inflow	经营活动现金流入小计	decimal(20,4)
            goods_and_services_cash_paid	购买商品、接受劳务支付的现金	decimal(20,4)
            staff_behalf_paid	支付给职工以及为职工支付的现金	decimal(20,4)
            tax_payments	支付的各项税费	decimal(20,4)
            subtotal_operate_cash_outflow	经营活动现金流出小计	decimal(20,4)
            net_operate_cash_flow	经营活动现金流量净额	decimal(20,4)
            invest_withdrawal_cash	收回投资收到的现金	decimal(20,4)
            invest_proceeds	取得投资收益收到的现金	decimal(20,4)
            fix_intan_other_asset_dispo_cash	处置固定资产、无形资产和其他长期资产收回的现金净额	decimal(20,4)
            net_cash_deal_subcompany	处置子公司及其他营业单位收到的现金净额	decimal(20,4)
            subtotal_invest_cash_inflow	投资活动现金流入小计	decimal(20,4)
            fix_intan_other_asset_acqui_cash	购建固定资产、无形资产和其他长期资产支付的现金	decimal(20,4)
            invest_cash_paid	投资支付的现金	decimal(20,4)
            impawned_loan_net_increase	质押贷款净增加额	decimal(20,4)
            net_cash_from_sub_company	取得子公司及其他营业单位支付的现金净额	decimal(20,4)
            subtotal_invest_cash_outflow	投资活动现金流出小计	decimal(20,4)
            net_invest_cash_flow	投资活动现金流量净额	decimal(20,4)
            cash_from_invest	吸收投资收到的现金	decimal(20,4)
            cash_from_borrowing	取得借款收到的现金	decimal(20,4)
            cash_from_bonds_issue	发行债券收到的现金	decimal(20,4)
            subtotal_finance_cash_inflow	筹资活动现金流入小计	decimal(20,4)
            borrowing_repayment	偿还债务支付的现金	decimal(20,4)
            dividend_interest_payment	分配股利、利润或偿付利息支付的现金	decimal(20,4)
            subtotal_finance_cash_outflow	筹资活动现金流出小计	decimal(20,4)
            net_finance_cash_flow	筹资活动现金流量净额	decimal(20,4)
            exchange_rate_change_effect	汇率变动对现金的影响	decimal(20,4)
            other_reason_effect_cash	其他原因对现金的影响	decimal(20,4)
            cash_equivalent_increase	现金及现金等价物净增加额	decimal(20,4)
            cash_equivalents_at_beginning	期初现金及现金等价物余额	decimal(20,4)
            cash_and_equivalents_at_end	期末现金及现金等价物余额	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            assets_depreciation_reserves	资产减值准备	decimal(20,4)
            fixed_assets_depreciation	固定资产折旧、油气资产折耗、生产性生物资产折旧	decimal(20,4)
            intangible_assets_amortization	无形资产摊销	decimal(20,4)
            defferred_expense_amortization	长期待摊费用摊销	decimal(20,4)
            fix_intan_other_asset_dispo_loss	处置固定资产、无形资产和其他长期资产的损失	decimal(20,4)
            fixed_asset_scrap_loss	固定资产报废损失	decimal(20,4)
            fair_value_change_loss	公允价值变动损失	decimal(20,4)
            financial_cost	财务费用	decimal(20,4)
            invest_loss	投资损失	decimal(20,4)
            deffered_tax_asset_decrease	递延所得税资产减少	decimal(20,4)
            deffered_tax_liability_increase	递延所得税负债增加	decimal(20,4)
            inventory_decrease	存货的减少	decimal(20,4)
            operate_receivables_decrease	经营性应收项目的减少	decimal(20,4)
            operate_payable_increase	经营性应付项目的增加	decimal(20,4)
            others	其他	decimal(20,4)
            net_operate_cash_flow_indirect	经营活动现金流量净额_间接法	decimal(20,4)
            debt_to_capital	债务转为资本	decimal(20,4)
            cbs_expiring_in_one_year	一年内到期的可转换公司债券	decimal(20,4)
            financial_lease_fixed_assets	融资租入固定资产	decimal(20,4)
            cash_at_end	现金的期末余额	decimal(20,4)
            cash_at_beginning	现金的期初余额	decimal(20,4)
            equivalents_at_end	现金等价物的期末余额	decimal(20,4)
            equivalents_at_beginning	现金等价物的期初余额	decimal(20,4)
            other_reason_effect_cash_indirect	其他原因对现金的影响_间接法	decimal(20,4)
            cash_equivalent_increase_indirect	现金及现金等价物净增加额_间接法	decimal(20,4)
            net_deposit_increase	客户存款和同业存放款项净增加额	decimal(20,4)
            net_borrowing_from_central_bank	向中央银行借款净增加额	decimal(20,4)
            net_borrowing_from_finance_co	向其他金融机构拆入资金净增加额	decimal(20,4)
            net_original_insurance_cash	收到原保险合同保费取得的现金	decimal(20,4)
            net_cash_received_from_reinsurance_business	收到再保险业务现金净额	decimal(20,4)
            net_insurer_deposit_investment	保户储金及投资款净增加额	decimal(20,4)
            net_deal_trading_assets	处置以公允价值计量且其变动计入当期损益的金融资产净增加额	decimal(20,4)
            interest_and_commission_cashin	收取利息、手续费及佣金的现金	decimal(20,4)
            net_increase_in_placements	拆入资金净增加额	decimal(20,4)
            net_buyback	回购业务资金净增加额	decimal(20,4)
            net_loan_and_advance_increase	客户贷款及垫款净增加额	decimal(20,4)
            net_deposit_in_cb_and_ib	存放中央银行和同业款项净增加额	decimal(20,4)
            original_compensation_paid	支付原保险合同赔付款项的现金	decimal(20,4)
            handling_charges_and_commission	支付利息、手续费及佣金的现金	decimal(20,4)
            policy_dividend_cash_paid	支付保单红利的现金	decimal(20,4)
            cash_from_mino_s_invest_sub	子公司吸收少数股东投资收到的现金	decimal(20,4)
            proceeds_from_sub_to_mino_s	子公司支付给少数股东的股利、利润	decimal(20,4)
            investment_property_depreciation	投资性房地产的折旧及摊销	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.STK_CASHFLOW_STATEMENT.code==code)：指定筛选条件，通过finance.STK_CASHFLOW_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_CASHFLOW_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司合并现金流量表数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公告的合并现金流量表数据，取出本期的经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
    q = query(finance.STK_CASHFLOW_STATEMENT.company_name,
              finance.STK_CASHFLOW_STATEMENT.code,
              finance.STK_CASHFLOW_STATEMENT.pub_date,
              finance.STK_CASHFLOW_STATEMENT.start_date,
              finance.STK_CASHFLOW_STATEMENT.end_date,
              finance.STK_CASHFLOW_STATEMENT.net_operate_cash_flow,
              finance.STK_CASHFLOW_STATEMENT.net_invest_cash_flow,
              finance.STK_CASHFLOW_STATEMENT.net_finance_cash_flow).filter(
        finance.STK_CASHFLOW_STATEMENT.code == stock, finance.STK_CASHFLOW_STATEMENT.pub_date >= pub_date,
        finance.STK_CASHFLOW_STATEMENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_STK_CASHFLOW_STATEMENT_PARENT():
    """
    获取上市公司定期公告中公布的母公司现金流量表
    :param :query(finance.STK_CASHFLOW_STATEMENT_PARENT)：表示从finance.STK_CASHFLOW_STATEMENT_PARENT这张表中查询上市公司定期公告中公布的母公司现金流量表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_CASHFLOW_STATEMENT_PARENT：代表上市公司母公司现金流量表，收录了上市公司定期公告中公布的母公司现金流量表数据，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            goods_sale_and_service_render_cash	销售商品、提供劳务收到的现金	decimal(20,4)
            tax_levy_refund	收到的税费返还	decimal(20,4)
            subtotal_operate_cash_inflow	经营活动现金流入小计	decimal(20,4)
            goods_and_services_cash_paid	购买商品、接受劳务支付的现金	decimal(20,4)
            staff_behalf_paid	支付给职工以及为职工支付的现金	decimal(20,4)
            tax_payments	支付的各项税费	decimal(20,4)
            subtotal_operate_cash_outflow	经营活动现金流出小计	decimal(20,4)
            net_operate_cash_flow	经营活动现金流量净额	decimal(20,4)
            invest_withdrawal_cash	收回投资收到的现金	decimal(20,4)
            invest_proceeds	取得投资收益收到的现金	decimal(20,4)
            fix_intan_other_asset_dispo_cash	处置固定资产、无形资产和其他长期资产收回的现金净额	decimal(20,4)
            net_cash_deal_subcompany	处置子公司及其他营业单位收到的现金净额	decimal(20,4)
            subtotal_invest_cash_inflow	投资活动现金流入小计	decimal(20,4)
            fix_intan_other_asset_acqui_cash	购建固定资产、无形资产和其他长期资产支付的现金	decimal(20,4)
            invest_cash_paid	投资支付的现金	decimal(20,4)
            impawned_loan_net_increase	质押贷款净增加额	decimal(20,4)
            net_cash_from_sub_company	取得子公司及其他营业单位支付的现金净额	decimal(20,4)
            subtotal_invest_cash_outflow	投资活动现金流出小计	decimal(20,4)
            net_invest_cash_flow	投资活动现金流量净额	decimal(20,4)
            cash_from_invest	吸收投资收到的现金	decimal(20,4)
            cash_from_borrowing	取得借款收到的现金	decimal(20,4)
            cash_from_bonds_issue	发行债券收到的现金	decimal(20,4)
            subtotal_finance_cash_inflow	筹资活动现金流入小计	decimal(20,4)
            borrowing_repayment	偿还债务支付的现金	decimal(20,4)
            dividend_interest_payment	分配股利、利润或偿付利息支付的现金	decimal(20,4)
            subtotal_finance_cash_outflow	筹资活动现金流出小计	decimal(20,4)
            net_finance_cash_flow	筹资活动现金流量净额	decimal(20,4)
            exchange_rate_change_effect	汇率变动对现金的影响	decimal(20,4)
            other_reason_effect_cash	其他原因对现金的影响	decimal(20,4)
            cash_equivalent_increase	现金及现金等价物净增加额	decimal(20,4)
            cash_equivalents_at_beginning	期初现金及现金等价物余额	decimal(20,4)
            cash_and_equivalents_at_end	期末现金及现金等价物余额	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            assets_depreciation_reserves	资产减值准备	decimal(20,4)
            fixed_assets_depreciation	固定资产折旧、油气资产折耗、生产性生物资产折旧	decimal(20,4)
            intangible_assets_amortization	无形资产摊销	decimal(20,4)
            defferred_expense_amortization	长期待摊费用摊销	decimal(20,4)
            fix_intan_other_asset_dispo_loss	处置固定资产、无形资产和其他长期资产的损失	decimal(20,4)
            fixed_asset_scrap_loss	固定资产报废损失	decimal(20,4)
            fair_value_change_loss	公允价值变动损失	decimal(20,4)
            financial_cost	财务费用	decimal(20,4)
            invest_loss	投资损失	decimal(20,4)
            deffered_tax_asset_decrease	递延所得税资产减少	decimal(20,4)
            deffered_tax_liability_increase	递延所得税负债增加	decimal(20,4)
            inventory_decrease	存货的减少	decimal(20,4)
            operate_receivables_decrease	经营性应收项目的减少	decimal(20,4)
            operate_payable_increase	经营性应付项目的增加	decimal(20,4)
            others	其他	decimal(20,4)
            net_operate_cash_flow_indirect	经营活动现金流量净额_间接法	decimal(20,4)
            debt_to_capital	债务转为资本	decimal(20,4)
            cbs_expiring_in_one_year	一年内到期的可转换公司债券	decimal(20,4)
            financial_lease_fixed_assets	融资租入固定资产	decimal(20,4)
            cash_at_end	现金的期末余额	decimal(20,4)
            cash_at_beginning	现金的期初余额	decimal(20,4)
            equivalents_at_end	现金等价物的期末余额	decimal(20,4)
            equivalents_at_beginning	现金等价物的期初余额	decimal(20,4)
            other_reason_effect_cash_indirect	其他原因对现金的影响_间接法	decimal(20,4)
            cash_equivalent_increase_indirect	现金及现金等价物净增加额_间接法	decimal(20,4)
            net_deposit_increase	客户存款和同业存放款项净增加额	decimal(20,4)
            net_borrowing_from_central_bank	向中央银行借款净增加额	decimal(20,4)
            net_borrowing_from_finance_co	向其他金融机构拆入资金净增加额	decimal(20,4)
            net_original_insurance_cash	收到原保险合同保费取得的现金	decimal(20,4)
            net_cash_received_from_reinsurance_business	收到再保险业务现金净额	decimal(20,4)
            net_insurer_deposit_investment	保户储金及投资款净增加额	decimal(20,4)
            net_deal_trading_assets	处置以公允价值计量且其变动计入当期损益的金融资产净增加额	decimal(20,4)
            interest_and_commission_cashin	收取利息、手续费及佣金的现金	decimal(20,4)
            net_increase_in_placements	拆入资金净增加额	decimal(20,4)
            net_buyback	回购业务资金净增加额	decimal(20,4)
            net_loan_and_advance_increase	客户贷款及垫款净增加额	decimal(20,4)
            net_deposit_in_cb_and_ib	存放中央银行和同业款项净增加额	decimal(20,4)
            original_compensation_paid	支付原保险合同赔付款项的现金	decimal(20,4)
            handling_charges_and_commission	支付利息、手续费及佣金的现金	decimal(20,4)
            policy_dividend_cash_paid	支付保单红利的现金	decimal(20,4)
            cash_from_mino_s_invest_sub	子公司吸收少数股东投资收到的现金	decimal(20,4)
            proceeds_from_sub_to_mino_s	子公司支付给少数股东的股利、利润	decimal(20,4)
            investment_property_depreciation	投资性房地产的折旧及摊销	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.STK_CASHFLOW_STATEMENT_PARENT.code==code)**：指定筛选条件，通过finance.STK_CASHFLOW_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_CASHFLOW_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的母公司现金流量表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公告的母公司现金流量表数据，取出本期的经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
    q = query(finance.STK_CASHFLOW_STATEMENT_PARENT.company_name,
              finance.STK_CASHFLOW_STATEMENT_PARENT.code,
              finance.STK_CASHFLOW_STATEMENT_PARENT.pub_date,
              finance.STK_CASHFLOW_STATEMENT_PARENT.start_date,
              finance.STK_CASHFLOW_STATEMENT_PARENT.end_date,
              finance.STK_CASHFLOW_STATEMENT_PARENT.net_operate_cash_flow,
              finance.STK_CASHFLOW_STATEMENT_PARENT.net_invest_cash_flow,
              finance.STK_CASHFLOW_STATEMENT_PARENT.net_finance_cash_flow).filter(
        finance.STK_CASHFLOW_STATEMENT_PARENT.code == '600519.XSHG',
        finance.STK_CASHFLOW_STATEMENT_PARENT.pub_date >= '2015-01-01',
        finance.STK_CASHFLOW_STATEMENT_PARENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df


def uu_query_STK_BALANCE_SHEET(stock,pub_date = '2015-01-01'):
    """
    合并资产负债表
    获取上市公司定期公告中公布的合并资产负债表
    :param :query(finance.STK_BALANCE_SHEET)：表示从finance.STK_BALANCE_SHEET这张表中查询上市公司定期公告中公布的合并资产负债表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_BALANCE_SHEET：代表上市公司合并资产负债表信息，收录了上市公司定期公告中公布的合并资产负债表数据，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下 报表来源编码
            source	报表来源	varchar(60)
            cash_equivalents	货币资金	decimal(20,4)
            trading_assets	交易性金融资产	decimal(20,4)
            bill_receivable	应收票据	decimal(20,4)
            account_receivable	应收账款	decimal(20,4)
            advance_payment	预付款项	decimal(20,4)
            other_receivable	其他应收款	decimal(20,4)
            affiliated_company_receivable	应收关联公司款	decimal(20,4)
            interest_receivable	应收利息	decimal(20,4)
            dividend_receivable	应收股利	decimal(20,4)
            inventories	存货	decimal(20,4)
            expendable_biological_asset	消耗性生物资产	decimal(20,4)	消耗性生物资产，是指为出售而持有的、或在将来收获为农产品的生物资产，包括生长中的大田作物、蔬菜、用材林，以及存栏代售的牲畜等
            non_current_asset_in_one_year	一年内到期的非流动资产	decimal(20,4)
            total_current_assets	流动资产合计	decimal(20,4)
            hold_for_sale_assets	可供出售金融资产	decimal(20,4)
            hold_to_maturity_investments	持有至到期投资	decimal(20,4)
            longterm_receivable_account	长期应收款	decimal(20,4)
            longterm_equity_invest	长期股权投资	decimal(20,4)
            investment_property	投资性房地产	decimal(20,4)
            fixed_assets	固定资产	decimal(20,4)
            constru_in_process	在建工程	decimal(20,4)
            construction_materials	工程物资	decimal(20,4)
            fixed_assets_liquidation	固定资产清理	decimal(20,4)
            biological_assets	生产性生物资产	decimal(20,4)
            oil_gas_assets	油气资产	decimal(20,4)
            intangible_assets	无形资产	decimal(20,4)
            development_expenditure	开发支出	decimal(20,4)
            good_will	商誉	decimal(20,4)
            long_deferred_expense	长期待摊费用	decimal(20,4)
            deferred_tax_assets	递延所得税资产	decimal(20,4)
            total_non_current_assets	非流动资产合计	decimal(20,4)
            total_assets	资产总计	decimal(20,4)
            shortterm_loan	短期借款	decimal(20,4)
            trading_liability	交易性金融负债	decimal(20,4)
            notes_payable	应付票据	decimal(20,4)
            accounts_payable	应付账款	decimal(20,4)
            advance_peceipts	预收款项	decimal(20,4)
            salaries_payable	应付职工薪酬	decimal(20,4)
            taxs_payable	应交税费	decimal(20,4)
            interest_payable	应付利息	decimal(20,4)
            dividend_payable	应付股利	decimal(20,4)
            other_payable	其他应付款	decimal(20,4)
            affiliated_company_payable	应付关联公司款	decimal(20,4)
            non_current_liability_in_one_year	一年内到期的非流动负债	decimal(20,4)
            total_current_liability	流动负债合计	decimal(20,4)
            longterm_loan	长期借款	decimal(20,4)
            bonds_payable	应付债券	decimal(20,4)
            longterm_account_payable	长期应付款	decimal(20,4)
            specific_account_payable	专项应付款	decimal(20,4)
            estimate_liability	预计负债	decimal(20,4)
            deferred_tax_liability	递延所得税负债	decimal(20,4)
            total_non_current_liability	非流动负债合计	decimal(20,4)
            total_liability	负债合计	decimal(20,4)
            paidin_capital	实收资本（或股本）	decimal(20,4)
            capital_reserve_fund	资本公积	decimal(20,4)
            specific_reserves	专项储备	decimal(20,4)
            surplus_reserve_fund	盈余公积	decimal(20,4)
            treasury_stock	库存股	decimal(20,4)
            retained_profit	未分配利润	decimal(20,4)
            equities_parent_company_owners	归属于母公司所有者权益	decimal(20,4)
            minority_interests	少数股东权益	decimal(20,4)
            foreign_currency_report_conv_diff	外币报表折算价差	decimal(20,4)
            irregular_item_adjustment	非正常经营项目收益调整	decimal(20,4)
            total_owner_equities	所有者权益（或股东权益）合计	decimal(20,4)
            total_sheet_owner_equities	负债和所有者权益（或股东权益）合计	decimal(20,4)
            other_comprehesive_income	其他综合收益	decimal(20,4)
            deferred_earning	递延收益-非流动负债	decimal(20,4)
            settlement_provi	结算备付金	decimal(20,4)
            lend_capital	拆出资金	decimal(20,4)
            loan_and_advance_current_assets	发放贷款及垫款-流动资产	decimal(20,4)
            derivative_financial_asset	衍生金融资产	decimal(20,4)
            insurance_receivables	应收保费	decimal(20,4)
            reinsurance_receivables	应收分保账款	decimal(20,4)
            reinsurance_contract_reserves_receivable	应收分保合同准备金	decimal(20,4)
            bought_sellback_assets	买入返售金融资产	decimal(20,4)
            hold_sale_asset	划分为持有待售的资产	decimal(20,4)
            loan_and_advance_noncurrent_assets	发放贷款及垫款-非流动资产	decimal(20,4)
            borrowing_from_centralbank	向中央银行借款	decimal(20,4)
            deposit_in_interbank	吸收存款及同业存放	decimal(20,4)
            borrowing_capital	拆入资金	decimal(20,4)
            derivative_financial_liability	衍生金融负债	decimal(20,4)
            sold_buyback_secu_proceeds	卖出回购金融资产款	decimal(20,4)
            commission_payable	应付手续费及佣金	decimal(20,4)
            reinsurance_payables	应付分保账款	decimal(20,4)
            insurance_contract_reserves	保险合同准备金	decimal(20,4)
            proxy_secu_proceeds	代理买卖证券款	decimal(20,4)
            receivings_from_vicariously_sold_securities	代理承销证券款	decimal(20,4)
            hold_sale_liability	划分为持有待售的负债	decimal(20,4)
            estimate_liability_current	预计负债-流动负债	decimal(20,4)
            deferred_earning_current	递延收益-流动负债	decimal(20,4)
            preferred_shares_noncurrent	优先股-非流动负债	decimal(20,4)
            pepertual_liability_noncurrent	永续债-非流动负债	decimal(20,4)
            longterm_salaries_payable	长期应付职工薪酬	decimal(20,4)
            other_equity_tools	其他权益工具	decimal(20,4)
            preferred_shares_equity	其中：优先股-所有者权益	decimal(20,4)
            pepertual_liability_equity	永续债-所有者权益	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.STK_BALANCE_SHEET.code==code)：指定筛选条件，通过finance.STK_BALANCE_SHEET.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_BALANCE_SHEET.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的合并资产负债表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公告的合并资产负债表数据，取出本期的货币资金，总资产和总负债
    q = query(finance.STK_BALANCE_SHEET.company_name,
              finance.STK_BALANCE_SHEET.code,
              finance.STK_BALANCE_SHEET.pub_date,
              finance.STK_BALANCE_SHEET.start_date,
              finance.STK_BALANCE_SHEET.end_date,
              finance.STK_BALANCE_SHEET.cash_equivalents,
              finance.STK_BALANCE_SHEET.total_assets,
              finance.STK_BALANCE_SHEET.total_liability
              ).filter(finance.STK_BALANCE_SHEET.code == stock,
                       finance.STK_BALANCE_SHEET.pub_date >= pub_date,
                       finance.STK_BALANCE_SHEET.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_STK_BALANCE_SHEET_PARENT():
    """
    母公司资产负债表
    获取上市公司定期公告中公布的母公司资产负债表
    :param :query(finance.STK_BALANCE_SHEET_PARENT)：表示从finance.STK_BALANCE_SHEET_PARENT这张表中查询上市公司定期公告中公布的母公司资产负债表信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_BALANCE_SHEET_PARENT：代表上市公司母公司资产负债表信息，收录了上市公司定期公告中公布的母公司资产负债表数据，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            cash_equivalents	货币资金	decimal(20,4)
            trading_assets	交易性金融资产	decimal(20,4)
            bill_receivable	应收票据	decimal(20,4)
            account_receivable	应收账款	decimal(20,4)
            advance_payment	预付款项	decimal(20,4)
            other_receivable	其他应收款	decimal(20,4)
            affiliated_company_receivable	应收关联公司款	decimal(20,4)
            interest_receivable	应收利息	decimal(20,4)
            dividend_receivable	应收股利	decimal(20,4)
            inventories	存货	decimal(20,4)
            expendable_biological_asset	消耗性生物资产	decimal(20,4)	消耗性生物资产，是指为出售而持有的、或在将来收获为农产品的生物资产，包括生长中的大田作物、蔬菜、用材林以及存栏代售的牲畜等
            non_current_asset_in_one_year	一年内到期的非流动资产	decimal(20,4)
            total_current_assets	流动资产合计	decimal(20,4)
            hold_for_sale_assets	可供出售金融资产	decimal(20,4)
            hold_to_maturity_investments	持有至到期投资	decimal(20,4)
            longterm_receivable_account	长期应收款	decimal(20,4)
            longterm_equity_invest	长期股权投资	decimal(20,4)
            investment_property	投资性房地产	decimal(20,4)
            fixed_assets	固定资产	decimal(20,4)
            constru_in_process	在建工程	decimal(20,4)
            construction_materials	工程物资	decimal(20,4)
            fixed_assets_liquidation	固定资产清理	decimal(20,4)
            biological_assets	生产性生物资产	decimal(20,4)
            oil_gas_assets	油气资产	decimal(20,4)
            intangible_assets	无形资产	decimal(20,4)
            development_expenditure	开发支出	decimal(20,4)
            good_will	商誉	decimal(20,4)
            long_deferred_expense	长期待摊费用	decimal(20,4)
            deferred_tax_assets	递延所得税资产	decimal(20,4)
            total_non_current_assets	非流动资产合计	decimal(20,4)
            total_assets	资产总计	decimal(20,4)
            shortterm_loan	短期借款	decimal(20,4)
            trading_liability	交易性金融负债	decimal(20,4)
            notes_payable	应付票据	decimal(20,4)
            accounts_payable	应付账款	decimal(20,4)
            advance_peceipts	预收款项	decimal(20,4)
            salaries_payable	应付职工薪酬	decimal(20,4)
            taxs_payable	应交税费	decimal(20,4)
            interest_payable	应付利息	decimal(20,4)
            dividend_payable	应付股利	decimal(20,4)
            other_payable	其他应付款	decimal(20,4)
            affiliated_company_payable	应付关联公司款	decimal(20,4)
            non_current_liability_in_one_year	一年内到期的非流动负债	decimal(20,4)
            total_current_liability	流动负债合计	decimal(20,4)
            longterm_loan	长期借款	decimal(20,4)
            bonds_payable	应付债券	decimal(20,4)
            longterm_account_payable	长期应付款	decimal(20,4)
            specific_account_payable	专项应付款	decimal(20,4)
            estimate_liability	预计负债	decimal(20,4)
            deferred_tax_liability	递延所得税负债	decimal(20,4)
            total_non_current_liability	非流动负债合计	decimal(20,4)
            total_liability	负债合计	decimal(20,4)
            paidin_capital	实收资本（或股本）	decimal(20,4)
            capital_reserve_fund	资本公积	decimal(20,4)
            specific_reserves	专项储备	decimal(20,4)
            surplus_reserve_fund	盈余公积	decimal(20,4)
            treasury_stock	库存股	decimal(20,4)
            retained_profit	未分配利润	decimal(20,4)
            equities_parent_company_owners	归属于母公司所有者权益	decimal(20,4)
            minority_interests	少数股东权益	decimal(20,4)
            foreign_currency_report_conv_diff	外币报表折算价差	decimal(20,4)
            irregular_item_adjustment	非正常经营项目收益调整	decimal(20,4)
            total_owner_equities	所有者权益（或股东权益）合计	decimal(20,4)
            total_sheet_owner_equities	负债和所有者权益（或股东权益）合计	decimal(20,4)
            other_comprehesive_income	其他综合收益	decimal(20,4)
            deferred_earning	递延收益-非流动负债	decimal(20,4)
            settlement_provi	结算备付金	decimal(20,4)
            lend_capital	拆出资金	decimal(20,4)
            loan_and_advance_current_assets	发放贷款及垫款-流动资产	decimal(20,4)
            derivative_financial_asset	衍生金融资产	decimal(20,4)
            insurance_receivables	应收保费	decimal(20,4)
            reinsurance_receivables	应收分保账款	decimal(20,4)
            reinsurance_contract_reserves_receivable	应收分保合同准备金	decimal(20,4)
            bought_sellback_assets	买入返售金融资产	decimal(20,4)
            hold_sale_asset	划分为持有待售的资产	decimal(20,4)
            loan_and_advance_noncurrent_assets	发放贷款及垫款-非流动资产	decimal(20,4)
            borrowing_from_centralbank	向中央银行借款	decimal(20,4)
            deposit_in_interbank	吸收存款及同业存放	decimal(20,4)
            borrowing_capital	拆入资金	decimal(20,4)
            derivative_financial_liability	衍生金融负债	decimal(20,4)
            sold_buyback_secu_proceeds	卖出回购金融资产款	decimal(20,4)
            commission_payable	应付手续费及佣金	decimal(20,4)
            reinsurance_payables	应付分保账款	decimal(20,4)
            insurance_contract_reserves	保险合同准备金	decimal(20,4)
            proxy_secu_proceeds	代理买卖证券款	decimal(20,4)
            receivings_from_vicariously_sold_securities	代理承销证券款	decimal(20,4)
            hold_sale_liability	划分为持有待售的负债	decimal(20,4)
            estimate_liability_current	预计负债-流动负债	decimal(20,4)
            deferred_earning_current	递延收益-流动负债	decimal(20,4)
            preferred_shares_noncurrent	优先股-非流动负债	decimal(20,4)
            pepertual_liability_noncurrent	永续债-非流动负债	decimal(20,4)
            longterm_salaries_payable	长期应付职工薪酬	decimal(20,4)
            other_equity_tools	其他权益工具	decimal(20,4)
            preferred_shares_equity	其中：优先股-所有者权益	decimal(20,4)
            pepertual_liability_equity	永续债-所有者权益	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.STK_BALANCE_SHEET_PARENT.code==code)：指定筛选条件，通过finance.STK_BALANCE_SHEET_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_BALANCE_SHEET_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的母公司资产负债表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询贵州茅台2015年之后公告的母公司资产负债表数据，取出本期的货币资金，总资产和总负债
    q = query(finance.STK_BALANCE_SHEET_PARENT.company_name,
              finance.STK_BALANCE_SHEET_PARENT.code,
              finance.STK_BALANCE_SHEET_PARENT.pub_date,
              finance.STK_BALANCE_SHEET_PARENT.start_date,
              finance.STK_BALANCE_SHEET_PARENT.end_date,
              finance.STK_BALANCE_SHEET_PARENT.cash_equivalents,
              finance.STK_BALANCE_SHEET_PARENT.total_assets,
              finance.STK_BALANCE_SHEET_PARENT.total_liability
              ).filter(finance.STK_BALANCE_SHEET_PARENT.code == '600519.XSHG',
                       finance.STK_BALANCE_SHEET_PARENT.pub_date >= '2015-01-01',
                       finance.STK_BALANCE_SHEET_PARENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_FINANCE_INCOME_STATEMENT():
    """
    金融类合并利润表
    获取金融类上市公司的合并利润表信息
    :param :query(finance.FINANCE_INCOME_STATEMENT)：表示从finance.FINANCE_INCOME_STATEMENT这张表中查询金融类上市公司合并利润表的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_INCOME_STATEMENT：代表金融类上市公司合并利润表，收录了金融类上市公司的合并利润表，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            operating_revenue	营业收入	decimal(20,4)
            interest_net_revenue	利息净收入	decimal(20,4)
            interest_income	利息收入	decimal(20,4)
            interest_expense	利息支出	decimal(20,4)
            commission_net_income	手续费及佣金净收入	decimal(20,4)
            commission_income	手续费及佣金收入	decimal(20,4)
            commission_expense	手续费及佣金支出	decimal(20,4)
            agent_security_income	代理买卖证券业务净收入	decimal(20,4)
            sell_security_income	证券承销业务净收入	decimal(20,4)
            manage_income	委托客户管理资产业务净收入	decimal(20,4)
            premiums_earned	已赚保费	decimal(20,4)
            assurance_income	保险业务收入	decimal(20,4)
            premiums_income	分保费收入	decimal(20,4)
            premiums_expense	分出保费	decimal(20,4)
            prepare_money	提取未到期责任准备金	decimal(20,4)
            investment_income	投资收益	decimal(20,4)
            invest_income_associates	对联营企业和合营企业的投资收益	decimal(20,4)
            fair_value_variable_income	公允价值变动收益	decimal(20,4)
            exchange_income	汇兑收益	decimal(20,4)
            other_income	其他业务收入	decimal(20,4)
            operation_expense	营业支出	decimal(20,4)
            refunded_premiums	退保金	decimal(20,4)
            compensate_loss	赔付支出	decimal(20,4)
            compensation_back	摊回赔付支出	decimal(20,4)
            insurance_reserve	提取保险责任准备金	decimal(20,4)
            insurance_reserve_back	摊回保险责任准备金	decimal(20,4)
            policy_dividend_payout	保单红利支出	decimal(20,4)
            reinsurance_cost	分保费用	decimal(20,4)
            operating_tax_surcharges	营业税金及附加	decimal(20,4)
            commission_expense2	手续费及佣金支出(保险专用)	decimal(20,4)
            operation_manage_fee	业务及管理费	decimal(20,4)
            separate_fee	摊回分保费用	decimal(20,4)
            asset_impairment_loss	资产减值损失	decimal(20,4)
            other_cost	其他业务成本	decimal(20,4)
            operating_profit	营业利润	decimal(20,4)
            subsidy_income	补贴收入	decimal(20,4)
            non_operating_revenue	营业外收入	decimal(20,4)
            non_operating_expense	营业外支出	decimal(20,4)
            other_items_influenced_profit	影响利润总额的其他科目	decimal(20,4)
            total_profit	利润总额	decimal(20,4)
            income_tax_expense	所得税费用	decimal(20,4)
            other_influence_net_profit	影响净利润的其他科目	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            np_parent_company_owners	归属于母公司股东的净利润	decimal(20,4)
            minority_profit	少数股东损益	decimal(20,4)
            eps	每股收益	decimal(20,4)
            basic_eps	基本每股收益	decimal(20,4)
            diluted_eps	稀释每股收益	decimal(20,4)
            other_composite_income	其他综合收益	decimal(20,4)
            total_composite_income	综合收益总额	decimal(20,4)
            ci_parent_company_owners	归属于母公司的综合收益	decimal(20,4)
            ci_minority_owners	归属于少数股东的综合收益	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_INCOME_STATEMENT.code==code)**：指定筛选条件，通过finance.FINANCE_INCOME_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_INCOME_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并利润表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的合并利润表数据,指定只取出本期数据
    q = query(finance.FINANCE_INCOME_STATEMENT).filter(finance.FINANCE_INCOME_STATEMENT.code == '601318.XSHG',
                                                       finance.FINANCE_INCOME_STATEMENT.pub_date >= '2015-01-01',
                                                       finance.FINANCE_INCOME_STATEMENT.report_type == 0).limit(10)
    df = finance.run_query(q)
    return df

def uu_query_FINANCE_INCOME_STATEMENT_PARENT():
    """
    金融类母公司利润表
    获取金融类上市公司的母公司利润表信息
    :param :query(finance.FINANCE_INCOME_STATEMENT_PARENT)：表示从finance.FINANCE_INCOME_STATEMENT_PARENT这张表中查询金融类上市公司母公司利润表的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_INCOME_STATEMENT_PARENT：代表金融类上市公司母公司利润表，收录了金融类上市公司的母公司利润表，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            operating_revenue	营业收入	decimal(20,4)
            interest_net_revenue	利息净收入	decimal(20,4)
            interest_income	利息收入	decimal(20,4)
            interest_expense	利息支出	decimal(20,4)
            commission_net_income	手续费及佣金净收入	decimal(20,4)
            commission_income	手续费及佣金收入	decimal(20,4)
            commission_expense	手续费及佣金支出	decimal(20,4)
            agent_security_income	代理买卖证券业务净收入	decimal(20,4)
            sell_security_income	证券承销业务净收入	decimal(20,4)
            manage_income	委托客户管理资产业务净收入	decimal(20,4)
            premiums_earned	已赚保费	decimal(20,4)
            assurance_income	保险业务收入	decimal(20,4)
            premiums_income	分保费收入	decimal(20,4)
            premiums_expense	分出保费	decimal(20,4)
            prepare_money	提取未到期责任准备金	decimal(20,4)
            investment_income	投资收益	decimal(20,4)
            invest_income_associates	对联营企业和合营企业的投资收益	decimal(20,4)
            fair_value_variable_income	公允价值变动收益	decimal(20,4)
            exchange_income	汇兑收益	decimal(20,4)
            other_income	其他业务收入	decimal(20,4)
            operation_expense	营业支出	decimal(20,4)
            refunded_premiums	退保金	decimal(20,4)
            compensate_loss	赔付支出	decimal(20,4)
            compensation_back	摊回赔付支出	decimal(20,4)
            insurance_reserve	提取保险责任准备金	decimal(20,4)
            insurance_reserve_back	摊回保险责任准备金	decimal(20,4)
            policy_dividend_payout	保单红利支出	decimal(20,4)
            reinsurance_cost	分保费用	decimal(20,4)
            operating_tax_surcharges	营业税金及附加	decimal(20,4)
            commission_expense2	手续费及佣金支出(保险专用)	decimal(20,4)
            operation_manage_fee	业务及管理费	decimal(20,4)
            separate_fee	摊回分保费用	decimal(20,4)
            asset_impairment_loss	资产减值损失	decimal(20,4)
            other_cost	其他业务成本	decimal(20,4)
            operating_profit	营业利润	decimal(20,4)
            subsidy_income	补贴收入	decimal(20,4)
            non_operating_revenue	营业外收入	decimal(20,4)
            non_operating_expense	营业外支出	decimal(20,4)
            other_items_influenced_profit	影响利润总额的其他科目	decimal(20,4)
            total_profit	利润总额	decimal(20,4)
            income_tax_expense	所得税费用	decimal(20,4)
            other_influence_net_profit	影响净利润的其他科目	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            np_parent_company_owners	归属于母公司股东的净利润	decimal(20,4)
            minority_profit	少数股东损益	decimal(20,4)
            eps	每股收益	decimal(20,4)
            basic_eps	基本每股收益	decimal(20,4)
            diluted_eps	稀释每股收益	decimal(20,4)
            other_composite_income	其他综合收益	decimal(20,4)
            total_composite_income	综合收益总额	decimal(20,4)
            ci_parent_company_owners	归属于母公司的综合收益	decimal(20,4)
            ci_minority_owners	归属于少数股东的综合收益	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_INCOME_STATEMENT_PARENT.code==code)**：指定筛选条件，通过finance.FINANCE_INCOME_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_INCOME_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的母公司利润表信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的母公司利润表数据,指定只取出本期数据
    q = query(finance.FINANCE_INCOME_STATEMENT_PARENT).filter(
        finance.FINANCE_INCOME_STATEMENT_PARENT.code == '601318.XSHG',
        finance.FINANCE_INCOME_STATEMENT_PARENT.pub_date >= '2015-01-01',
        finance.FINANCE_INCOME_STATEMENT_PARENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_FINANCE_CASHFLOW_STATEMENT():
    """
    金融类合并现金流量表
    获取金融类上市公司的合并现金流量表信息
    :param :query(finance.FINANCE_CASHFLOW_STATEMENT)：表示从finance.FINANCE_CASHFLOW_STATEMENT这张表中查询金融类上市公司合并现金流量的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_CASHFLOW_STATEMENT：代表金融类上市公司合并现金流量表，收录了金融类上市公司的合并现金流量，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            operate_cash_flow	经营活动产生的现金流量	decimal(20,4)
            net_loan_and_advance_decrease	客户贷款及垫款净减少额	decimal(20,4)
            net_deposit_increase	客户存款和同业存放款项净增加额	decimal(20,4)
            net_borrowing_from_central_bank	向中央银行借款净增加额	decimal(20,4)
            net_deposit_in_cb_and_ib_de	存放中央银行和同业款项净减少额	decimal(20,4)
            net_borrowing_from_finance_co	向其他金融机构拆入资金净增加额	decimal(20,4)
            interest_and_commission_cashin	收取利息、手续费及佣金的现金	decimal(20,4)
            trade_asset_increase	处置交易性金融资产净增加额	decimal(20,4)
            net_increase_in_placements	拆入资金净增加额	decimal(20,4)
            net_buyback	回购业务资金净增加额	decimal(20,4)
            goods_sale_and_service_render_cash	销售商品、提供劳务收到的现金	decimal(20,4)
            tax_levy_refund	收到的税费返还	decimal(20,4)
            net_original_insurance_cash	收到原保险合同保费取得的现金	decimal(20,4)
            insurance_cash_amount	收到再保业务现金净额	decimal(20,4)
            net_insurer_deposit_investment	保户储金及投资款净增加额	decimal(20,4)
            subtotal_operate_cash_inflow	经营活动现金流入小计	decimal(20,4)
            net_loan_and_advance_increase	客户贷款及垫款净增加额	decimal(20,4)
            saving_clients_decrease_amount	客户存放及同业存放款项净减少额	decimal(20,4)
            net_deposit_in_cb_and_ib	存放中央银行和同业款项净增加额	decimal(20,4)
            central_borrowing_decrease	向中央银行借款净减少额	decimal(20,4)
            other_money_increase	向其他金融机构拆出资金净增加额	decimal(20,4)
            purchase_trade_asset_increase	购入交易性金融资产净增加额	decimal(20,4)
            repurchase_decrease	回购业务资金净减少额	decimal(20,4)
            handling_charges_and_commission	支付利息、手续费及佣金的现金	decimal(20,4)
            goods_sale_and_service_render_cash	购买商品、提供劳务支付的现金	decimal(20,4)
            net_cash_re_insurance	支付再保业务现金净额	decimal(20,4)
            reserve_investment_decrease	保户储金及投资款净减少额	decimal(20,4)
            original_compensation_paid	支付原保险合同赔付款项的现金	decimal(20,4)
            policy_dividend_cash_paid	支付保单红利的现金	decimal(20,4)
            staff_behalf_paid	支付给职工以及为职工支付的现金	decimal(20,4)
            tax_payments	支付的各项税费	decimal(20,4)
            subtotal_operate_cash_outflow	经营活动现金流出小计	decimal(20,4)
            net_operate_cash_flow	经营活动现金流量净额	decimal(20,4)
            invest_cash_flow	投资活动产生的现金流量	decimal(20,4)
            invest_withdrawal_cash	收回投资收到的现金	decimal(20,4)
            invest_proceeds	取得投资收益收到的现金	decimal(20,4)
            gain_from_disposal	处置固定资产、无形资产和其他长期资产所收回的现金	decimal(20,4)
            subtotal_invest_cash_inflow	投资活动现金流入小计	decimal(20,4)
            invest_cash_paid	投资支付的现金	decimal(20,4)
            impawned_loan_net_increase	质押贷款净增加额	decimal(20,4)
            fix_intan_other_asset_acqui_cash	购建固定资产、无形资产和其他长期资产支付的现金	decimal(20,4)
            subtotal_invest_cash_outflow	投资活动现金流出小计	decimal(20,4)
            net_invest_cash_flow	投资活动现金流量净额	decimal(20,4)
            finance_cash_flow	筹资活动产生的现金流量	decimal(20,4)
            cash_from_invest	吸收投资收到的现金	decimal(20,4)
            cash_from_bonds_issue	发行债券收到的现金	decimal(20,4)
            cash_from_borrowing	取得借款收到的现金	decimal(20,4)
            subtotal_finance_cash_inflow	筹资活动现金流入小计	decimal(20,4)
            borrowing_repayment	偿还债务支付的现金	decimal(20,4)
            dividend_interest_payment	分配股利、利润或偿付利息支付的现金	decimal(20,4)
            subtotal_finance_cash_outflow	筹资活动现金流出小计	decimal(20,4)
            net_finance_cash_flow	筹资活动产生的现金流量净额	decimal(20,4)
            exchange_rate_change_effect	汇率变动对现金的影响	decimal(20,4)
            other_reason_effect_cash	其他原因对现金的影响	decimal(20,4)
            cash_equivalent_increase	现金及现金等价物净增加额	decimal(20,4)
            cash_equivalents_at_beginning	期初现金及现金等价物余额	decimal(20,4)
            cash_and_equivalents_at_end	期末现金及现金等价物余额	decimal(20,4)
            net_profit_cashflow_adjustment	将净利润调节为经营活动现金流量	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            assets_depreciation_reserves	资产减值准备	decimal(20,4)
            fixed_assets_depreciation	固定资产折旧、油气资产折耗、生产性生物资产折旧	decimal(20,4)
            intangible_assets_amortization	无形资产摊销	decimal(20,4)
            defferred_expense_amortization	长期待摊费用摊销	decimal(20,4)
            fix_intan_other_asset_dispo_loss	处置固定资产、无形资产和其他长期资产的损失	decimal(20,4)
            fixed_asset_scrap_loss	固定资产报废损失	decimal(20,4)
            fair_value_change_loss	公允价值变动损失	decimal(20,4)
            financial_cost	财务费用	decimal(20,4)
            invest_loss	投资损失	decimal(20,4)
            deffered_tax_asset_decrease	递延所得税资产减少	decimal(20,4)
            deffered_tax_liability_increase	递延所得税负债增加	decimal(20,4)
            inventory_decrease	存货的减少	decimal(20,4)
            operate_receivables_decrease	经营性应收项目的减少	decimal(20,4)
            operate_payable_increase	经营性应付项目的增加	decimal(20,4)
            others	其他	decimal(20,4)
            net_operate_cash_flow2	经营活动产生的现金流量净额_间接法	decimal(20,4)
            activities_not_relate_major	不涉及现金收支的重大投资和筹资活动	decimal(20,4)
            debt_to_capital	债务转为资本	decimal(20,4)
            cbs_expiring_in_one_year	一年内到期的可转换公司债券	decimal(20,4)
            financial_lease_fixed_assets	融资租入固定资产	decimal(20,4)
            change_info_cash	现金及现金等价物净变动情况	decimal(20,4)
            cash_at_end	现金的期末余额	decimal(20,4)
            cash_at_beginning	现金的期初余额	decimal(20,4)
            equivalents_at_end	现金等价物的期末余额	decimal(20,4)
            equivalents_at_beginning	现金等价物的期初余额	decimal(20,4)
            other_influence2	其他原因对现金的影响2	decimal(20,4)
            cash_equivalent_increase2	现金及现金等价物净增加额2	decimal(20,4)
            investment_property_depreciation	投资性房地产的折旧及摊销	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_CASHFLOW_STATEMENT.code==code)：指定筛选条件，通过finance.FINANCE_CASHFLOW_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_CASHFLOW_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并现金流量信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的合并现金流量表数据，指定只取出本期数据经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
    q = query(finance.FINANCE_CASHFLOW_STATEMENT.company_name,
              finance.FINANCE_CASHFLOW_STATEMENT.code,
              finance.FINANCE_CASHFLOW_STATEMENT.pub_date,
              finance.FINANCE_CASHFLOW_STATEMENT.start_date,
              finance.FINANCE_CASHFLOW_STATEMENT.end_date,
              finance.FINANCE_CASHFLOW_STATEMENT.net_operate_cash_flow,
              finance.FINANCE_CASHFLOW_STATEMENT.net_invest_cash_flow,
              finance.FINANCE_CASHFLOW_STATEMENT.net_finance_cash_flow).filter(
        finance.FINANCE_CASHFLOW_STATEMENT.code == '601318.XSHG',
        finance.FINANCE_CASHFLOW_STATEMENT.pub_date >= '2015-01-01',
        finance.FINANCE_CASHFLOW_STATEMENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_FINANCE_CASHFLOW_STATEMENT():
    """
    金融类合并现金流量表
    获取金融类上市公司的合并现金流量表信息
    :param :query(finance.FINANCE_CASHFLOW_STATEMENT)：表示从finance.FINANCE_CASHFLOW_STATEMENT这张表中查询金融类上市公司合并现金流量的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_CASHFLOW_STATEMENT：代表金融类上市公司合并现金流量表，收录了金融类上市公司的合并现金流量，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            operate_cash_flow	经营活动产生的现金流量	decimal(20,4)
            net_loan_and_advance_decrease	客户贷款及垫款净减少额	decimal(20,4)
            net_deposit_increase	客户存款和同业存放款项净增加额	decimal(20,4)
            net_borrowing_from_central_bank	向中央银行借款净增加额	decimal(20,4)
            net_deposit_in_cb_and_ib_de	存放中央银行和同业款项净减少额	decimal(20,4)
            net_borrowing_from_finance_co	向其他金融机构拆入资金净增加额	decimal(20,4)
            interest_and_commission_cashin	收取利息、手续费及佣金的现金	decimal(20,4)
            trade_asset_increase	处置交易性金融资产净增加额	decimal(20,4)
            net_increase_in_placements	拆入资金净增加额	decimal(20,4)
            net_buyback	回购业务资金净增加额	decimal(20,4)
            goods_sale_and_service_render_cash	销售商品、提供劳务收到的现金	decimal(20,4)
            tax_levy_refund	收到的税费返还	decimal(20,4)
            net_original_insurance_cash	收到原保险合同保费取得的现金	decimal(20,4)
            insurance_cash_amount	收到再保业务现金净额	decimal(20,4)
            net_insurer_deposit_investment	保户储金及投资款净增加额	decimal(20,4)
            subtotal_operate_cash_inflow	经营活动现金流入小计	decimal(20,4)
            net_loan_and_advance_increase	客户贷款及垫款净增加额	decimal(20,4)
            saving_clients_decrease_amount	客户存放及同业存放款项净减少额	decimal(20,4)
            net_deposit_in_cb_and_ib	存放中央银行和同业款项净增加额	decimal(20,4)
            central_borrowing_decrease	向中央银行借款净减少额	decimal(20,4)
            other_money_increase	向其他金融机构拆出资金净增加额	decimal(20,4)
            purchase_trade_asset_increase	购入交易性金融资产净增加额	decimal(20,4)
            repurchase_decrease	回购业务资金净减少额	decimal(20,4)
            handling_charges_and_commission	支付利息、手续费及佣金的现金	decimal(20,4)
            goods_sale_and_service_render_cash	购买商品、提供劳务支付的现金	decimal(20,4)
            net_cash_re_insurance	支付再保业务现金净额	decimal(20,4)
            reserve_investment_decrease	保户储金及投资款净减少额	decimal(20,4)
            original_compensation_paid	支付原保险合同赔付款项的现金	decimal(20,4)
            policy_dividend_cash_paid	支付保单红利的现金	decimal(20,4)
            staff_behalf_paid	支付给职工以及为职工支付的现金	decimal(20,4)
            tax_payments	支付的各项税费	decimal(20,4)
            subtotal_operate_cash_outflow	经营活动现金流出小计	decimal(20,4)
            net_operate_cash_flow	经营活动现金流量净额	decimal(20,4)
            invest_cash_flow	投资活动产生的现金流量	decimal(20,4)
            invest_withdrawal_cash	收回投资收到的现金	decimal(20,4)
            invest_proceeds	取得投资收益收到的现金	decimal(20,4)
            gain_from_disposal	处置固定资产、无形资产和其他长期资产所收回的现金	decimal(20,4)
            subtotal_invest_cash_inflow	投资活动现金流入小计	decimal(20,4)
            invest_cash_paid	投资支付的现金	decimal(20,4)
            impawned_loan_net_increase	质押贷款净增加额	decimal(20,4)
            fix_intan_other_asset_acqui_cash	购建固定资产、无形资产和其他长期资产支付的现金	decimal(20,4)
            subtotal_invest_cash_outflow	投资活动现金流出小计	decimal(20,4)
            net_invest_cash_flow	投资活动现金流量净额	decimal(20,4)
            finance_cash_flow	筹资活动产生的现金流量	decimal(20,4)
            cash_from_invest	吸收投资收到的现金	decimal(20,4)
            cash_from_bonds_issue	发行债券收到的现金	decimal(20,4)
            cash_from_borrowing	取得借款收到的现金	decimal(20,4)
            subtotal_finance_cash_inflow	筹资活动现金流入小计	decimal(20,4)
            borrowing_repayment	偿还债务支付的现金	decimal(20,4)
            dividend_interest_payment	分配股利、利润或偿付利息支付的现金	decimal(20,4)
            subtotal_finance_cash_outflow	筹资活动现金流出小计	decimal(20,4)
            net_finance_cash_flow	筹资活动产生的现金流量净额	decimal(20,4)
            exchange_rate_change_effect	汇率变动对现金的影响	decimal(20,4)
            other_reason_effect_cash	其他原因对现金的影响	decimal(20,4)
            cash_equivalent_increase	现金及现金等价物净增加额	decimal(20,4)
            cash_equivalents_at_beginning	期初现金及现金等价物余额	decimal(20,4)
            cash_and_equivalents_at_end	期末现金及现金等价物余额	decimal(20,4)
            net_profit_cashflow_adjustment	将净利润调节为经营活动现金流量	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            assets_depreciation_reserves	资产减值准备	decimal(20,4)
            fixed_assets_depreciation	固定资产折旧、油气资产折耗、生产性生物资产折旧	decimal(20,4)
            intangible_assets_amortization	无形资产摊销	decimal(20,4)
            defferred_expense_amortization	长期待摊费用摊销	decimal(20,4)
            fix_intan_other_asset_dispo_loss	处置固定资产、无形资产和其他长期资产的损失	decimal(20,4)
            fixed_asset_scrap_loss	固定资产报废损失	decimal(20,4)
            fair_value_change_loss	公允价值变动损失	decimal(20,4)
            financial_cost	财务费用	decimal(20,4)
            invest_loss	投资损失	decimal(20,4)
            deffered_tax_asset_decrease	递延所得税资产减少	decimal(20,4)
            deffered_tax_liability_increase	递延所得税负债增加	decimal(20,4)
            inventory_decrease	存货的减少	decimal(20,4)
            operate_receivables_decrease	经营性应收项目的减少	decimal(20,4)
            operate_payable_increase	经营性应付项目的增加	decimal(20,4)
            others	其他	decimal(20,4)
            net_operate_cash_flow2	经营活动产生的现金流量净额_间接法	decimal(20,4)
            activities_not_relate_major	不涉及现金收支的重大投资和筹资活动	decimal(20,4)
            debt_to_capital	债务转为资本	decimal(20,4)
            cbs_expiring_in_one_year	一年内到期的可转换公司债券	decimal(20,4)
            financial_lease_fixed_assets	融资租入固定资产	decimal(20,4)
            change_info_cash	现金及现金等价物净变动情况	decimal(20,4)
            cash_at_end	现金的期末余额	decimal(20,4)
            cash_at_beginning	现金的期初余额	decimal(20,4)
            equivalents_at_end	现金等价物的期末余额	decimal(20,4)
            equivalents_at_beginning	现金等价物的期初余额	decimal(20,4)
            other_influence2	其他原因对现金的影响2	decimal(20,4)
            cash_equivalent_increase2	现金及现金等价物净增加额2	decimal(20,4)
            investment_property_depreciation	投资性房地产的折旧及摊销	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_CASHFLOW_STATEMENT.code==code)：指定筛选条件，通过finance.FINANCE_CASHFLOW_STATEMENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_CASHFLOW_STATEMENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并现金流量信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的合并现金流量表数据，指定只取出本期数据经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
    q = query(finance.FINANCE_CASHFLOW_STATEMENT.company_name,
              finance.FINANCE_CASHFLOW_STATEMENT.code,
              finance.FINANCE_CASHFLOW_STATEMENT.pub_date,
              finance.FINANCE_CASHFLOW_STATEMENT.start_date,
              finance.FINANCE_CASHFLOW_STATEMENT.end_date,
              finance.FINANCE_CASHFLOW_STATEMENT.net_operate_cash_flow,
              finance.FINANCE_CASHFLOW_STATEMENT.net_invest_cash_flow,
              finance.FINANCE_CASHFLOW_STATEMENT.net_finance_cash_flow).filter(
        finance.FINANCE_CASHFLOW_STATEMENT.code == '601318.XSHG',
        finance.FINANCE_CASHFLOW_STATEMENT.pub_date >= '2015-01-01',
        finance.FINANCE_CASHFLOW_STATEMENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_FINANCE_CASHFLOW_STATEMENT_PARENT():
    """
    金融类母公司现金流量表
    获取金融类上市公司的母公司现金流量表信息
    :param :query(finance.FINANCE_CASHFLOW_STATEMENT_PARENT)：表示从finance.FINANCE_CASHFLOW_STATEMENT_PARENT这张表中查询金融类上市公司母公司现金流量的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_CASHFLOW_STATEMENT_PARENT：代表金融类上市公司母公司现金流量表，收录了金融类上市公司的母公司现金流量，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            operate_cash_flow	经营活动产生的现金流量	decimal(20,4)
            net_loan_and_advance_decrease	客户贷款及垫款净减少额	decimal(20,4)
            net_deposit_increase	客户存款和同业存放款项净增加额	decimal(20,4)
            net_borrowing_from_central_bank	向中央银行借款净增加额	decimal(20,4)
            net_deposit_in_cb_and_ib_de	存放中央银行和同业款项净减少额	decimal(20,4)
            net_borrowing_from_finance_co	向其他金融机构拆入资金净增加额	decimal(20,4)
            interest_and_commission_cashin	收取利息、手续费及佣金的现金	decimal(20,4)
            trade_asset_increase	处置交易性金融资产净增加额	decimal(20,4)
            net_increase_in_placements	拆入资金净增加额	decimal(20,4)
            net_buyback	回购业务资金净增加额	decimal(20,4)
            goods_sale_and_service_render_cash	销售商品、提供劳务收到的现金	decimal(20,4)
            tax_levy_refund	收到的税费返还	decimal(20,4)
            net_original_insurance_cash	收到原保险合同保费取得的现金	decimal(20,4)
            insurance_cash_amount	收到再保业务现金净额	decimal(20,4)
            net_insurer_deposit_investment	保户储金及投资款净增加额	decimal(20,4)
            subtotal_operate_cash_inflow	经营活动现金流入小计	decimal(20,4)
            net_loan_and_advance_increase	客户贷款及垫款净增加额	decimal(20,4)
            saving_clients_decrease_amount	客户存放及同业存放款项净减少额	decimal(20,4)
            net_deposit_in_cb_and_ib	存放中央银行和同业款项净增加额	decimal(20,4)
            central_borrowing_decrease	向中央银行借款净减少额	decimal(20,4)
            other_money_increase	向其他金融机构拆出资金净增加额	decimal(20,4)
            purchase_trade_asset_increase	购入交易性金融资产净增加额	decimal(20,4)
            repurchase_decrease	回购业务资金净减少额	decimal(20,4)
            handling_charges_and_commission	支付利息、手续费及佣金的现金	decimal(20,4)
            goods_sale_and_service_render_cash	购买商品、提供劳务支付的现金	decimal(20,4)
            net_cash_re_insurance	支付再保业务现金净额	decimal(20,4)
            reserve_investment_decrease	保户储金及投资款净减少额	decimal(20,4)
            original_compensation_paid	支付原保险合同赔付款项的现金	decimal(20,4)
            policy_dividend_cash_paid	支付保单红利的现金	decimal(20,4)
            staff_behalf_paid	支付给职工以及为职工支付的现金	decimal(20,4)
            tax_payments	支付的各项税费	decimal(20,4)
            subtotal_operate_cash_outflow	经营活动现金流出小计	decimal(20,4)
            net_operate_cash_flow	经营活动现金流量净额	decimal(20,4)
            invest_cash_flow	投资活动产生的现金流量	decimal(20,4)
            invest_withdrawal_cash	收回投资收到的现金	decimal(20,4)
            invest_proceeds	取得投资收益收到的现金	decimal(20,4)
            gain_from_disposal	处置固定资产、无形资产和其他长期资产所收回的现金	decimal(20,4)
            subtotal_invest_cash_inflow	投资活动现金流入小计	decimal(20,4)
            invest_cash_paid	投资支付的现金	decimal(20,4)
            impawned_loan_net_increase	质押贷款净增加额	decimal(20,4)
            fix_intan_other_asset_acqui_cash	购建固定资产、无形资产和其他长期资产支付的现金	decimal(20,4)
            subtotal_invest_cash_outflow	投资活动现金流出小计	decimal(20,4)
            net_invest_cash_flow	投资活动现金流量净额	decimal(20,4)
            finance_cash_flow	筹资活动产生的现金流量	decimal(20,4)
            cash_from_invest	吸收投资收到的现金	decimal(20,4)
            cash_from_bonds_issue	发行债券收到的现金	decimal(20,4)
            cash_from_borrowing	取得借款收到的现金	decimal(20,4)
            subtotal_finance_cash_inflow	筹资活动现金流入小计	decimal(20,4)
            borrowing_repayment	偿还债务支付的现金	decimal(20,4)
            dividend_interest_payment	分配股利、利润或偿付利息支付的现金	decimal(20,4)
            subtotal_finance_cash_outflow	筹资活动现金流出小计	decimal(20,4)
            net_finance_cash_flow	筹资活动产生的现金流量净额	decimal(20,4)
            exchange_rate_change_effect	汇率变动对现金的影响	decimal(20,4)
            other_reason_effect_cash	其他原因对现金的影响	decimal(20,4)
            cash_equivalent_increase	现金及现金等价物净增加额	decimal(20,4)
            cash_equivalents_at_beginning	期初现金及现金等价物余额	decimal(20,4)
            cash_and_equivalents_at_end	期末现金及现金等价物余额	decimal(20,4)
            net_profit_cashflow_adjustment	将净利润调节为经营活动现金流量	decimal(20,4)
            net_profit	净利润	decimal(20,4)
            assets_depreciation_reserves	资产减值准备	decimal(20,4)
            fixed_assets_depreciation	固定资产折旧、油气资产折耗、生产性生物资产折旧	decimal(20,4)
            intangible_assets_amortization	无形资产摊销	decimal(20,4)
            defferred_expense_amortization	长期待摊费用摊销	decimal(20,4)
            fix_intan_other_asset_dispo_loss	处置固定资产、无形资产和其他长期资产的损失	decimal(20,4)
            fixed_asset_scrap_loss	固定资产报废损失	decimal(20,4)
            fair_value_change_loss	公允价值变动损失	decimal(20,4)
            financial_cost	财务费用	decimal(20,4)
            invest_loss	投资损失	decimal(20,4)
            deffered_tax_asset_decrease	递延所得税资产减少	decimal(20,4)
            deffered_tax_liability_increase	递延所得税负债增加	decimal(20,4)
            inventory_decrease	存货的减少	decimal(20,4)
            operate_receivables_decrease	经营性应收项目的减少	decimal(20,4)
            operate_payable_increase	经营性应付项目的增加	decimal(20,4)
            others	其他	decimal(20,4)
            net_operate_cash_flow2	经营活动产生的现金流量净额_间接法	decimal(20,4)
            activities_not_relate_major	不涉及现金收支的重大投资和筹资活动	decimal(20,4)
            debt_to_capital	债务转为资本	decimal(20,4)
            cbs_expiring_in_one_year	一年内到期的可转换公司债券	decimal(20,4)
            financial_lease_fixed_assets	融资租入固定资产	decimal(20,4)
            change_info_cash	现金及现金等价物净变动情况	decimal(20,4)
            cash_at_end	现金的期末余额	decimal(20,4)
            cash_at_beginning	现金的期初余额	decimal(20,4)
            equivalents_at_end	现金等价物的期末余额	decimal(20,4)
            equivalents_at_beginning	现金等价物的期初余额	decimal(20,4)
            other_influence2	其他原因对现金的影响2	decimal(20,4)
            cash_equivalent_increase2	现金及现金等价物净增加额2	decimal(20,4)
            investment_property_depreciation	投资性房地产的折旧及摊销	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code==code)：指定筛选条件，通过finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_CASHFLOW_STATEMENT_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的母公司现金流量信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的母公司现金流量表数据，指定只取出本期经营活动现金流量净额，投资活动现金流量净额，以及筹资活动现金流量净额
    q = query(finance.FINANCE_CASHFLOW_STATEMENT_PARENT.company_name,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.pub_date,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.start_date,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.end_date,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.net_operate_cash_flow,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.net_invest_cash_flow,
              finance.FINANCE_CASHFLOW_STATEMENT_PARENT.net_finance_cash_flow).filter(
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.code == '601318.XSHG',
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.pub_date >= '2015-01-01',
        finance.FINANCE_CASHFLOW_STATEMENT_PARENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_FINANCE_BALANCE_SHEET():
    """
    金融类合并资产负债表
    获取金融类上市公司的合并资产负债表信息
    :param :query(finance.FINANCE_BALANCE_SHEET)：表示从finance.FINANCE_BALANCE_SHEET这张表中查询金融类上市公司合并资产负债的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_BALANCE_SHEET：代表金融类上市公司合并资产负债表，收录了金融类上市公司的合并资产负债，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表编码表
            source	报表来源	varchar(60)
            deposit_in_ib	存放同业款项	decimal(20,4)
            cash_equivalents	货币资金	decimal(20,4)
            deposit_client	客户资金存款	decimal(20,4)
            cash_in_cb	现金及存放中央银行款项	decimal(20,4)
            settlement_provi	结算备付金	decimal(20,4)
            settlement_provi_client	客户备付金	decimal(20,4)
            metal	贵金属	decimal(20,4)
            lend_capital	拆出资金	decimal(20,4)
            fairvalue_fianancial_asset	以公允价值计量且其变动计入当期损益的金融资产	decimal(20,4)
            other_grow_asset	衍生金融资产	decimal(20,4)
            bought_sellback_assets	买入返售金融资产	decimal(20,4)
            interest_receivable	应收利息	decimal(20,4)
            insurance_receivables	应收保费	decimal(20,4)
            recover_receivable	应收代位追偿款	decimal(20,4)
            separate_receivable	应收分保帐款	decimal(20,4)
            not_time_fund	应收分保未到期责任准备金	decimal(20,4)
            not_decide_fund	应收分保未决赔款准备金	decimal(20,4)
            response_fund	应收分保寿险责任准备金	decimal(20,4)
            health_fund	应收分保长期健康险责任准备金	decimal(20,4)
            margin_loan	保户质押贷款	decimal(20,4)
            deposit_period	定期存款	decimal(20,4)
            loan_and_advance	发放贷款及垫款	decimal(20,4)
            margin_out	存出保证金	decimal(20,4)
            agent_asset	代理业务资产	decimal(20,4)
            investment_reveiable	应收款项类投资	decimal(20,4)
            advance_payment	预付款项	decimal(20,4)
            hold_for_sale_assets	可供出售金融资产	decimal(20,4)
            hold_to_maturity_investments	持有至到期投资	decimal(20,4)
            longterm_equity_invest	长期股权投资	decimal(20,4)
            finance_out	融出资金	decimal(20,4)
            capital_margin_out	存出资本保证金	decimal(20,4)
            investment_property	投资性房地产	decimal(20,4)
            inventories	存货	decimal(20,4)
            fixed_assets	固定资产	decimal(20,4)
            constru_in_process	在建工程	decimal(20,4)
            intangible_assets	无形资产	decimal(20,4)
            trade_fee	交易席位费	decimal(20,4)
            long_deferred_expense	长期待摊费用	decimal(20,4)
            fixed_assets_liquidation	固定资产清理	decimal(20,4)
            independent_account_asset	独立帐户资产	decimal(20,4)
            deferred_tax_assets	递延所得税资产	decimal(20,4)
            other_asset	其他资产	decimal(20,4)
            total_assets	资产总计	decimal(20,4)
            borrowing_from_centralbank	向中央银行借款	decimal(20,4)
            deposit_in_ib_and_other	同业及其他金融机构存放款项	decimal(20,4)
            shortterm_loan	短期借款	decimal(20,4)
            loan_pledge	其中：质押借款	decimal(20,4)
            borrowing_capital	拆入资金	decimal(20,4)
            fairvalue_financial_liability	以公允价值计量且其变动计入当期损益的金融负债	decimal(20,4)
            derivative_financial_liability	衍生金融负债	decimal(20,4)
            sold_buyback_secu_proceeds	卖出回购金融资产款	decimal(20,4)
            deposit_absorb	吸收存款	decimal(20,4)
            proxy_secu_proceeds	代理买卖证券款	decimal(20,4)
            proxy_sell_proceeds	代理承销证券款	decimal(20,4)
            accounts_payable	应付账款	decimal(20,4)
            notes_payable	应付票据	decimal(20,4)
            advance_peceipts	预收款项	decimal(20,4)
            insurance_receive_early	预收保费	decimal(20,4)
            commission_payable	应付手续费及佣金	decimal(20,4)
            insurance_payable	应付分保帐款	decimal(20,4)
            salaries_payable	应付职工薪酬	decimal(20,4)
            taxs_payable	应交税费	decimal(20,4)
            interest_payable	应付利息	decimal(20,4)
            proxy_liability	代理业务负债	decimal(20,4)
            estimate_liability	预计负债	decimal(20,4)
            compensation_payable	应付赔付款	decimal(20,4)
            interest_insurance_payable	应付保单红利	decimal(20,4)
            investment_money	保户储金及投资款	decimal(20,4)
            not_time_reserve	未到期责任准备金	decimal(20,4)
            not_decide_reserve	未决赔款准备金	decimal(20,4)
            live_reserve	寿险责任准备金	decimal(20,4)
            longterm_reserve	长期健康险责任准备金	decimal(20,4)
            longterm_loan	长期借款	decimal(20,4)
            bonds_payable	应付债券	decimal(20,4)
            independent_account	独立帐户负债	decimal(20,4)
            deferred_tax_liability	递延所得税负债	decimal(20,4)
            other_liability	其他负债	decimal(20,4)
            total_liability	负债合计	decimal(20,4)
            paidin_capital	实收资本(或股本)	decimal(20,4)
            capital_reserve_fund	资本公积	decimal(20,4)
            treasury_stock	减：库存股	decimal(20,4)
            surplus_reserve_fund	盈余公积	decimal(20,4)
            equities_parent_company_owners	归属于母公司所有者权益	decimal(20,4)
            retained_profit	未分配利润	decimal(20,4)
            minority_interests	少数股东权益	decimal(20,4)
            currency_mis	外币报表折算差额	decimal(20,4)
            total_owner_equities	所有者权益合计	decimal(20,4)
            total_liability_equity	负债和所有者权益总计	decimal(20,4)
            perferred_share_liability	优先股-负债	decimal(20,4)
            account_receivable	应收账款	decimal(20,4)
            other_equity_tools	其他权益工具	decimal(20,4)
            perferred_share_equity	优先股-权益	decimal(20,4)
            pep_debt_equity	永续债-权益	decimal(20,4)
            other_comprehesive_income	其他综合收益	decimal(20,4)
            good_will	商誉	decimal(20,4)
            shortterm_loan_payable	应付短期融资款	decimal(20,4)
            accounts_payable	应付账款	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_BALANCE_SHEET.code==code)：指定筛选条件，通过finance.FINANCE_BALANCE_SHEET.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_BALANCE_SHEET.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的合并资产负债信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的合并资产负债表数据，取出本期的货币资金，总资产和总负债
    q = query(finance.FINANCE_BALANCE_SHEET.company_name,
              finance.FINANCE_BALANCE_SHEET.code,
              finance.FINANCE_BALANCE_SHEET.pub_date,
              finance.FINANCE_BALANCE_SHEET.start_date,
              finance.FINANCE_BALANCE_SHEET.end_date,
              finance.FINANCE_BALANCE_SHEET.cash_equivalents,
              finance.FINANCE_BALANCE_SHEET.total_assets,
              finance.FINANCE_BALANCE_SHEET.total_liability
              ).filter(finance.FINANCE_BALANCE_SHEET.code == '601318.XSHG',
                       finance.FINANCE_BALANCE_SHEET.pub_date >= '2015-01-01',
                       finance.FINANCE_BALANCE_SHEET.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df


def uu_query_FINANCE_BALANCE_SHEET_PARENT():
    """
    金融类母公司资产负债表
    获取金融类上市公司的母公司资产负债表信息
    :param :query(finance.FINANCE_BALANCE_SHEET_PARENT)：表示从finance.FINANCE_BALANCE_SHEET_PARENT这张表中查询金融类上市公司母公司资产负债的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.FINANCE_BALANCE_SHEET_PARENT：代表金融类上市公司母公司资产负债表，收录了金融类上市公司的母公司资产负债，表结构和字段信息如下：

            字段名称	中文名称	字段类型	含义
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	公司主证券代码	varchar(12)
            a_code	A股代码	varchar(12)
            b_code	B股代码	varchar(12)
            h_code	H股代码	varchar(12)
            pub_date	公告日期	date
            start_date	开始日期	date
            end_date	截止日期	date
            report_date	报告期	date
            report_type	报告期类型	int	0本期，1上期
            source_id	报表来源编码	int	如下报表来源编码
            source	报表来源	varchar(60)
            deposit_in_ib	存放同业款项	decimal(20,4)
            cash_equivalents	货币资金	decimal(20,4)
            deposit_client	客户资金存款	decimal(20,4)
            cash_in_cb	现金及存放中央银行款项	decimal(20,4)
            settlement_provi	结算备付金	decimal(20,4)
            settlement_provi_client	客户备付金	decimal(20,4)
            metal	贵金属	decimal(20,4)
            lend_capital	拆出资金	decimal(20,4)
            fairvalue_fianancial_asset	以公允价值计量且其变动计入当期损益的金融资产	decimal(20,4)
            other_grow_asset	衍生金融资产	decimal(20,4)
            bought_sellback_assets	买入返售金融资产	decimal(20,4)
            interest_receivable	应收利息	decimal(20,4)
            insurance_receivables	应收保费	decimal(20,4)
            recover_receivable	应收代位追偿款	decimal(20,4)
            separate_receivable	应收分保帐款	decimal(20,4)
            not_time_fund	应收分保未到期责任准备金	decimal(20,4)
            not_decide_fund	应收分保未决赔款准备金	decimal(20,4)
            response_fund	应收分保寿险责任准备金	decimal(20,4)
            health_fund	应收分保长期健康险责任准备金	decimal(20,4)
            margin_loan	保户质押贷款	decimal(20,4)
            deposit_period	定期存款	decimal(20,4)
            loan_and_advance	发放贷款及垫款	decimal(20,4)
            margin_out	存出保证金	decimal(20,4)
            agent_asset	代理业务资产	decimal(20,4)
            investment_reveiable	应收款项类投资	decimal(20,4)
            advance_payment	预付款项	decimal(20,4)
            hold_for_sale_assets	可供出售金融资产	decimal(20,4)
            hold_to_maturity_investments	持有至到期投资	decimal(20,4)
            longterm_equity_invest	长期股权投资	decimal(20,4)
            finance_out	融出资金	decimal(20,4)
            capital_margin_out	存出资本保证金	decimal(20,4)
            investment_property	投资性房地产	decimal(20,4)
            inventories	存货	decimal(20,4)
            fixed_assets	固定资产	decimal(20,4)
            constru_in_process	在建工程	decimal(20,4)
            intangible_assets	无形资产	decimal(20,4)
            trade_fee	交易席位费	decimal(20,4)
            long_deferred_expense	长期待摊费用	decimal(20,4)
            fixed_assets_liquidation	固定资产清理	decimal(20,4)
            independent_account_asset	独立帐户资产	decimal(20,4)
            deferred_tax_assets	递延所得税资产	decimal(20,4)
            other_asset	其他资产	decimal(20,4)
            total_assets	资产总计	decimal(20,4)
            borrowing_from_centralbank	向中央银行借款	decimal(20,4)
            deposit_in_ib_and_other	同业及其他金融机构存放款项	decimal(20,4)
            shortterm_loan	短期借款	decimal(20,4)
            loan_pledge	其中：质押借款	decimal(20,4)
            borrowing_capital	拆入资金	decimal(20,4)
            fairvalue_financial_liability	以公允价值计量且其变动计入当期损益的金融负债	decimal(20,4)
            derivative_financial_liability	衍生金融负债	decimal(20,4)
            sold_buyback_secu_proceeds	卖出回购金融资产款	decimal(20,4)
            deposit_absorb	吸收存款	decimal(20,4)
            proxy_secu_proceeds	代理买卖证券款	decimal(20,4)
            proxy_sell_proceeds	代理承销证券款	decimal(20,4)
            accounts_payable	应付账款	decimal(20,4)
            notes_payable	应付票据	decimal(20,4)
            advance_peceipts	预收款项	decimal(20,4)
            insurance_receive_early	预收保费	decimal(20,4)
            commission_payable	应付手续费及佣金	decimal(20,4)
            insurance_payable	应付分保帐款	decimal(20,4)
            salaries_payable	应付职工薪酬	decimal(20,4)
            taxs_payable	应交税费	decimal(20,4)
            interest_payable	应付利息	decimal(20,4)
            proxy_liability	代理业务负债	decimal(20,4)
            estimate_liability	预计负债	decimal(20,4)
            compensation_payable	应付赔付款	decimal(20,4)
            interest_insurance_payable	应付保单红利	decimal(20,4)
            investment_money	保户储金及投资款	decimal(20,4)
            not_time_reserve	未到期责任准备金	decimal(20,4)
            not_decide_reserve	未决赔款准备金	decimal(20,4)
            live_reserve	寿险责任准备金	decimal(20,4)
            longterm_reserve	长期健康险责任准备金	decimal(20,4)
            longterm_loan	长期借款	decimal(20,4)
            bonds_payable	应付债券	decimal(20,4)
            independent_account	独立帐户负债	decimal(20,4)
            deferred_tax_liability	递延所得税负债	decimal(20,4)
            other_liability	其他负债	decimal(20,4)
            total_liability	负债合计	decimal(20,4)
            paidin_capital	实收资本(或股本)	decimal(20,4)
            capital_reserve_fund	资本公积	decimal(20,4)
            treasury_stock	减：库存股	decimal(20,4)
            surplus_reserve_fund	盈余公积	decimal(20,4)
            equities_parent_company_owners	归属于母公司所有者权益	decimal(20,4)
            retained_profit	未分配利润	decimal(20,4)
            minority_interests	少数股东权益	decimal(20,4)
            currency_mis	外币报表折算差额	decimal(20,4)
            total_owner_equities	所有者权益合计	decimal(20,4)
            total_liability_equity	负债和所有者权益总计	decimal(20,4)
            perferred_share_liability	优先股-负债	decimal(20,4)
            account_receivable	应收账款	decimal(20,4)
            other_equity_tools	其他权益工具	decimal(20,4)
            perferred_share_equity	优先股-权益	decimal(20,4)
            pep_debt_equity	永续债-权益	decimal(20,4)
            other_comprehesive_income	其他综合收益	decimal(20,4)
            good_will	商誉	decimal(20,4)
            shortterm_loan_payable	应付短期融资款	decimal(20,4)
            accounts_payable	应付账款	decimal(20,4)
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(finance.FINANCE_BALANCE_SHEET_PARENT.code==code)：指定筛选条件，通过finance.FINANCE_BALANCE_SHEET_PARENT.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.FINANCE_BALANCE_SHEET_PARENT.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日金融类上市公司公布的母公司资产负债信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 查询中国平安2015年之后公告的母公司资产负债表数据，取出本期的货币资金，总资产和总负债
    q = query(finance.FINANCE_BALANCE_SHEET_PARENT.company_name,
              finance.FINANCE_BALANCE_SHEET_PARENT.code,
              finance.FINANCE_BALANCE_SHEET_PARENT.pub_date,
              finance.FINANCE_BALANCE_SHEET_PARENT.start_date,
              finance.FINANCE_BALANCE_SHEET_PARENT.end_date,
              finance.FINANCE_BALANCE_SHEET_PARENT.cash_equivalents,
              finance.FINANCE_BALANCE_SHEET_PARENT.total_assets,
              finance.FINANCE_BALANCE_SHEET_PARENT.total_liability
              ).filter(finance.FINANCE_BALANCE_SHEET_PARENT.code == '601318.XSHG',
                       finance.FINANCE_BALANCE_SHEET_PARENT.pub_date >= '2015-01-01',
                       finance.FINANCE_BALANCE_SHEET_PARENT.report_type == 0).limit(20)
    df = finance.run_query(q)
    return df

def uu_query_STK_FINANCE_SUPPLEMENT():
    """
    财务报表补充科目
    描述：记录上市公司在财务报表中的补充科目（2018年6月，财政部修订了企业财务报表格式，其中资产负债表主要是合并了应收账款和应收票据、应付账款和应付票据，利润表主要是将研发费用从管理费用中拿出来单列，同时对股东权益变动表做了部分调整，补充数据自2018年9月30号三季报开始公布）
    :param :query(sup.STK_FINANCE_SUPPLEMENT)：表示从sup.STK_FINANCE_SUPPLEMENT这张表中查询财务报表的补充科目，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：query简易教程
            sup.STK_FINANCE_SUPPLEMENT：收录了财务报表补充科目，表结构和字段信息如下：
            字段设计：

            字段名称	字段类型	描述
            company_id	int	公司ID
            company_name	varchar(100)	公司名称
            code	varchar(12)	公司主证券代码
            a_code	varchar(12)	A股代码
            b_code	varchar(12)	B股代码
            h_code	varchar(12)	H股代码
            pub_date	date	公告日期
            start_date	date	开始日期，对应截止日期所在年度-01-01
            end_date	date	截止日期
            report_date	date	报告期
            report_type	int	报告期类型，0本期，1上期
            source_id	int	报表来源编码
            source	varchar(60)	报表来源
            bill_and_account_receivable	decimal(20,2)	应收票据及应收账款
            bill_and_account_payable	decimal(20,2)	应付票据及应付账款
            rd_expenses	decimal（20,2）	研发费用
            报表来源编码

            编码	名称
            321001	招募说明书
            321002	上市公告书
            321003	定期报告
            321004	预披露公告
            321005	换股报告书
            321099	其他
            filter(sup.STK_FINANCE_SUPPLEMENT.end_date==date)：指定筛选条件，通过sup.STK_FINANCE_SUPPLEMENT.end_date==date可以指定你想要查询的报告期对应的截止日期；除此之外，还可以对表中其他字段指定筛选条件；多个筛选条件用英文逗号分隔。
            limit(n)：限制返回的数据条数，n指定返回条数。
    :rtype :dataframe
    :return:
    """
    # 查询上市公司2018年年报公布的财务报表补充科目对应的本期数据。
    df=sup.run_query(query(sup.STK_FINANCE_SUPPLEMENT).filter(sup.STK_FINANCE_SUPPLEMENT.end_date=='2018-12-31',sup.STK_FINANCE_SUPPLEMENT.report_type==0).limit(10))
    return df


# df=sup.run_query(query(sup.STK_FINANCE_SUPPLEMENT).filter(sup.STK_FINANCE_SUPPLEMENT.end_date=='2018-12-31',sup.STK_FINANCE_SUPPLEMENT.report_type==0).limit(10))
# print(df)