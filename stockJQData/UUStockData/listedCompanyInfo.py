#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 17:07
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : listedCompanyInfo.py
# @Software: PyCharm

"""
##   获取上市公司概况
###  上市公司员工情况
     上市公司基本信息
     上市公司状态变动
     股票上市信息
     股票简称变更
     公司管理人员任职情况
参考 https://www.joinquant.com/help/api/help?name=JQData#%E8%8E%B7%E5%8F%96%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E6%A6%82%E5%86%B5
"""
from jqdatasdk import *
auth('18620668927', 'minpeng123')   # 账号密码认证

def uu_query_STK_EMPLOYEE_INFO():
    """
    上市公司员工情况
    获取上市公司在公告中公布的员工情况，包括员工人数、学历等信息
    :param :query(finance.STK_EMPLOYEE_INFO)：表示从finance.STK_EMPLOYEE_INFO这张表中查询上市公司员工情况的字段信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用逗号分隔进行提取；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_EMPLOYEE_INFO：代表上市公司员工情况表，收录了上市公司在公告中公布的员工情况，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            code	证券代码	varchar(12)	'600276.XSHG'，'000001.XSHE'
            name	证券名称	varchar(64)
            end_date	报告期截止日	date	统计截止该报告期的员工信息
            pub_date	公告日期	date
            employee	在职员工总数	int	人
            retirement	离退休人员	int	人
            graduate_rate	研究生以上人员比例	decimal(10,4)	%
            college_rate	大学专科以上人员比例	decimal(10,4)	%
            middle_rate	中专及以下人员比例	decimal(10,4)	%
            filter(finance.STK_EMPLOYEE_INFO.code==code)：指定筛选条件，通过finance.STK_EMPLOYEE_INFO.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_EMPLOYEE_INFO.pub_date>='2015-01-01'，表示公告日期大于2015年1月1日上市公司公布的员工信息；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的员工信息且公告日期大于2015年1月1日，限定返回条数为10
    q = query(finance.STK_EMPLOYEE_INFO).filter(finance.STK_EMPLOYEE_INFO.code == '600276.XSHG',
                                                finance.STK_EMPLOYEE_INFO.pub_date >= '2015-01-01').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_COMPANY_INFO(stock):
    """
    上市公司基本信息
    获取上市公司最新公布的基本信息，包含注册资本，主营业务，行业分类等
    :param :query(finance.STK_COMPANY_INFO)：表示从finance.STK_COMPANY_INFO这张表中查询上市公司最新公布的基本信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_COMPANY_INFO：代表上市公司基本信息表，收录了上市公司最新公布的基本信息，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            code	证券代码	varchar(12)	多证券代码的优先级：A股>B股
            full_name	公司名称	varchar(100)
            short_name	公司简称	varchar(40)
            a_code	A股股票代码	varchar(12)
            b_code	B股股票代码	varchar(12)
            h_code	H股股票代码	varchar(12)
            fullname_en	英文名称	varchar(100)
            shortname_en	英文简称	varchar(40)
            legal_representative	法人代表	varchar(40)
            register_location	注册地址	varchar(100)
            office_address	办公地址	varchar(150)
            zipcode	邮政编码	varchar(10)
            register_capital	注册资金	decimal(20,4)	单位：万元
            currency_id	货币编码	int
            currency	货币名称	varchar(32)
            establish_date	成立日期	date
            website	机构网址	varchar(80)
            email	电子信箱	varchar(80)
            contact_number	联系电话	varchar(60)
            fax_number	联系传真	varchar(60)
            main_business	主营业务	varchar(500)
            business_scope	经营范围	varchar(4000)
            description	机构简介	varchar(4000)
            tax_number	税务登记号	varchar(50)
            license_number	法人营业执照号	varchar(40)
            pub_newspaper	指定信息披露报刊	varchar(120)
            pub_website	指定信息披露网站	varchar(120)
            secretary	董事会秘书	varchar(40)
            secretary_number	董秘联系电话	varchar(60)
            secretary_fax	董秘联系传真	varchar(60)
            secretary_email	董秘电子邮箱	varchar(80)
            security_representative	证券事务代表	varchar(40)
            province_id	所属省份编码	varchar(12)
            province	所属省份	varchar(60)
            city_id	所属城市编码	varchar(12)
            city	所属城市	varchar(60)
            industry_id	行业编码	varchar(12)	证监会行业分类
            industry_1	行业一级分类	varchar(60)
            industry_2	行业二级分类	varchar(60)
            cpafirm	会计师事务所	varchar(200)
            lawfirm	律师事务所	varchar(200)
            ceo	总经理	varchar(100)
            comments	备注	varchar(300)
            filter(finance.STK_COMPANY_INFO.code==code)：指定筛选条件，通过finance.STK_COMPANY_INFO.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_COMPANY_INFO.city=='北京市'，表示所属城市为北京市；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的上市公司基本信息，限定返回条数为10
    q = query(finance.STK_COMPANY_INFO).filter(finance.STK_COMPANY_INFO.code == stock).limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_STATUS_CHANGE():
    """
    上市公司状态变动
    获取上市公司已发行未上市、正常上市、实行ST、*ST、暂停上市、终止上市的变动情况等
    :param :query(finance.STK_STATUS_CHANGE)：表示从finance.STK_STATUS_CHANGE这张表中查询上市公司的状态变动信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_STATUS_CHANGE：代表上市公司状态变动表，收录了上市公司已发行未上市、正常上市、实行ST、*ST、暂停上市、终止上市的变动情况等，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	机构ID	int
            code	股票代码	varchar(12)
            name	股票名称	varchar(40)
            pub_date	公告日期	date
            change_date	变更日期	date
            public_status_id	上市状态编码	int	如下上市状态编码
            public_status	上市状态	varchar(32)
            change_reason	变更原因	varchar(500)
            change_type_id	变更类型编码	int	如下变更类型编码
            change_type	变更类型	varchar(60)
            comments	备注	varchar(255)
            上市状态编码

            上市状态编码	上市状态
            301001	正常上市
            301002	ST
            301003	*ST
            301004	暂停上市
            301005	进入退市整理期
            301006	终止上市
            301007	已发行未上市
            301008	预披露
            301009	未过会
            301010	发行失败
            301011	暂缓发行
            301012	暂缓上市
            301013	停止转让
            301014	正常转让
            301015	实行投资者适当性管理表示
            301099	其他
            变更类型编码
            变更类型编码	变更类型
            303001	恢复上市
            303002	摘星
            303003	摘帽
            303004	摘星摘帽
            303005	披星
            303006	戴帽
            303007	戴帽披星
            303008	拟上市
            303009	新股上市
            303010	发行失败
            303011	暂停上市
            303012	终止上市
            303013	退市整理
            303014	暂缓发行
            303015	暂缓上市
            303016	实行投资者适当性管理标识
            303017	未过会
            303018	预披露
            303019	正常转让
            303020	停止转让
            303021	重新上市
            303099	其他
            filter(finance.STK_STATUS_CHANGE.code==code)：指定筛选条件，通过finance.STK_STATUS_CHANGE.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_STATUS_CHANGE.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的上市公司状态变动，限定返回条数为10
    q = query(finance.STK_STATUS_CHANGE).filter(finance.STK_STATUS_CHANGE.code == '600276.XSHG').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_LIST(stock):
    """
    股票上市信息
    获取沪深A股的上市信息，包含上市日期、交易所、发行价格、初始上市数量等
    :param :query(finance.STK_LIST)：表示从STK_LIST这张表中查询沪深A股的上市信息，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_LIST：代表股票上市信息表，收录了沪深A股的上市信息，包含上市日期、交易所、发行价格、初始上市数量等，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            code	证券代码	varchar(12)
            name	证券简称	varchar(40)
            short_name	拼音简称	varchar(20)
            category	证券类别	varchar(4)	A/B
            exchange	交易所	varchar(12)	XSHG/XSHE
            start_date	上市日期	date
            end_date	终止上市日期	date
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            ipo_shares	初始上市数量	decimal(20,2)	股
            book_price	发行价格	decimal(20,4)	元
            par_value	面值	decimal(20,4)	元
            state_id	上市状态编码	int
            state	上市状态	varchar(32)
            filter(finance.STK_LIST.code==code)：指定筛选条件，通过finance.STK_LIST.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_LIST.start_date>='2015-01-01'，表示筛选上市日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的上市信息，限定返回条数为10
    q = query(finance.STK_LIST).filter(finance.STK_LIST.code == stock).limit(10)
    df = finance.run_query(q)
    return df



def uu_query_STK_NAME_HISTORY():
    """
    股票简称变更
    获取在A股市场和B股市场上市的股票简称的变更情况
    :param :query(finance.STK_NAME_HISTORY)：表示从finance.STK_NAME_HISTORY这张表中查询股票简称的变更情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_NAME_HISTORY：代表股票简称变更表，收录了在A股市场和B股市场上市的股票简称的变更情况，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            code	股票代码	varchar(12)
            company_id	公司ID	int
            new_name	新股票简称	varchar(40)
            new_spelling	新英文简称	varchar(40)
            org_name	原证券简称	varchar(40)
            org_spelling	原证券英文简称	varchar(40)
            start_date	开始日期	date
            pub_date	公告日期	date
            reason	变更原因	varchar(255)
            filter(finance.STK_NAME_HISTORY.code==code)：指定筛选条件，通过finance.STK_NAME_HISTORY.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_NAME_HISTORY.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。

            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    # 指定查询对象为恒瑞医药（600276.XSHG)的股票简称变更信息，限定返回条数为10
    q = query(finance.STK_NAME_HISTORY).filter(finance.STK_NAME_HISTORY.code == '600276.XSHG').limit(10)
    df = finance.run_query(q)
    return df

def uu_query_STK_MANAGEMENT_INFO(stock):
    """
    公司管理人员任职情况
    记录上市公司管理人员的任职情况
    :param :query(finance.STK_MANAGEMENT_INFO)：表示从finance.STK_MANAGEMENT_INFO这张表中查询上市公司管理人员任职情况，还可以指定所要查询的字段名，格式如下：query(库名.表名.字段名1，库名.表名.字段名2），多个字段用英文逗号进行分隔；query函数的更多用法详见：sqlalchemy.orm.query.Query对象

            finance.STK_MANAGEMENT_INFO：代表了公司管理人员任职情况表，收录了上市公司管理人员的任职情况，表结构和字段信息如下：

            字段名称	中文名称	字段类型	备注/示例
            company_id	公司ID	int
            company_name	公司名称	varchar(100)
            code	股票代码	varchar(12)
            pub_date	公告日期	date
            person_id	个人ID	int
            name	姓名	varchar(40)
            title_class_id	职务类别编码	int
            title_class	职务类别	varchar(60)
            title	职务名称	varchar(60)
            start_date	任职日期	date
            leave_date	离职日期	date
            leave_reason	离职原因	varchar(255)
            on_job	是否在职	char(1)	0-否，1-是
            gender	性别	char(1)	F-女；M-男
            birth_year	出生年份	varchar(8)
            highest_degree_id	最高学历编码	int
            highest_degree	最高学历	varchar(60)
            title_level_id	职级编码	int
            titile_level	职级	varchar(120)	职级代表工作的难易程度、责任轻重以及所需的资格条件相同或充分相似的职系的集合。如初级、中级、高级、高级。
            profession_certificate	专业技术资格	varchar(120)
            profession_certificate	专业技术资格	varchar(120)
            nationality	国籍	varchar(60)
            security_career_start_year	从事证券业开始年份	varchar(8)
            resume	个人简历	varchar(3000)
            filter(finance.STK_MANAGEMENT_INFO.code==code)：指定筛选条件，通过finance.STK_MANAGEMENT_INFO.code==code可以指定你想要查询的股票代码；除此之外，还可以对表中其他字段指定筛选条件，如finance.STK_MANAGEMENT_INFO.pub_date>='2015-01-01'，表示筛选公告日期大于等于2015年1月1日之后的数据；多个筛选条件用英文逗号分隔。
            order_by(finance.STK_MANAGEMENT_INFO.pub_date): 将返回结果按公告日期排序
            limit(n)：限制返回的数据条数，n指定返回条数
    :rtype :dataframe
    :return:
    """
    q = query(finance.STK_MANAGEMENT_INFO).filter(finance.STK_MANAGEMENT_INFO.code == stock).order_by(
        finance.STK_MANAGEMENT_INFO.pub_date).limit(10)
    df = finance.run_query(q)
    return df


# df=uu_query_STK_LIST()
# print(df)