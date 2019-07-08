
/***
  --创建数据库 jqdata
 */
CREATE SCHEMA `jqdata` CHARACTER SET utf8mb4 ;

/***
  --创建用户 jqdata
 */
CREATE USER 'jqdata'@'%' IDENTIFIED BY 'jqdata';

grant all privileges on jqdata.* to 'jqdata'@'%' IDENTIFIED BY 'jqdata';

flush privileges;


/***
  --股票信息表
 */
CREATE TABLE `jqdata`.`t_all_securities` (
  `security` VARCHAR(20) NOT NULL COMMENT '股票代码',
  `display_name` VARCHAR(20) NULL COMMENT '中文名称',
  `name` VARCHAR(50) NULL COMMENT '缩写简称',
  `start_date` DATE NULL COMMENT '上市日期',
  `end_date` DATE NULL COMMENT '退市日期，如果没有退市则为2200-01-01',
  PRIMARY KEY (`security`))
COMMENT = '所有股票信息';

/***
  --日线行情数据：
--分表规则：股票代码模5取余x
--表名 t_kline_day_x
--索引 股票代码，日期
 */
CREATE TABLE `jqdata`.`t_kline_day_0` (
  `security` VARCHAR(20) NOT NULL COMMENT '股票代码',
  `kday` DATE NOT NULL COMMENT '日期',
  `open` DECIMAL(10,2) NULL COMMENT '时间段开始时价格',
  `close` DECIMAL(10,2) NULL COMMENT '时间段结束时价格',
  `low` DECIMAL(10,2) NULL COMMENT '最低价',
  `high` DECIMAL(10,2) NULL COMMENT '最高价',
  `volume` BIGINT NULL COMMENT '成交的股票数量',
  `money` DECIMAL(20,2) NULL COMMENT '成交的金额',
  `factor` DECIMAL(15,8) NULL COMMENT '前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor',
  `high_limit` DECIMAL(10,2) NULL COMMENT '涨停价',
  `low_limit` DECIMAL(10,2) NULL COMMENT '跌停价',
  `avg` DECIMAL(10,2) NULL COMMENT '这段时间的平均价, 等于money/volume',
  `pre_close` DECIMAL(10,2) NULL COMMENT '前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格',
  `paused` TINYINT NULL COMMENT '布尔值, 这只股票是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0',
  PRIMARY KEY (`security`, `kday`))
COMMENT = '日线行情数据——股票代码模5余0';

CREATE TABLE `jqdata`.`t_kline_day_1` (
  `security` VARCHAR(20) NOT NULL COMMENT '股票代码',
  `kday` DATE NOT NULL COMMENT '日期',
  `open` DECIMAL(10,2) NULL COMMENT '时间段开始时价格',
  `close` DECIMAL(10,2) NULL COMMENT '时间段结束时价格',
  `low` DECIMAL(10,2) NULL COMMENT '最低价',
  `high` DECIMAL(10,2) NULL COMMENT '最高价',
  `volume` BIGINT NULL COMMENT '成交的股票数量',
  `money` DECIMAL(20,2) NULL COMMENT '成交的金额',
  `factor` DECIMAL(15,8) NULL COMMENT '前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor',
  `high_limit` DECIMAL(10,2) NULL COMMENT '涨停价',
  `low_limit` DECIMAL(10,2) NULL COMMENT '跌停价',
  `avg` DECIMAL(10,2) NULL COMMENT '这段时间的平均价, 等于money/volume',
  `pre_close` DECIMAL(10,2) NULL COMMENT '前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格',
  `paused` TINYINT NULL COMMENT '布尔值, 这只股票是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0',
  PRIMARY KEY (`security`, `kday`))
COMMENT = '日线行情数据——股票代码模5余1';

CREATE TABLE `jqdata`.`t_kline_day_2` (
  `security` VARCHAR(20) NOT NULL COMMENT '股票代码',
  `kday` DATE NOT NULL COMMENT '日期',
  `open` DECIMAL(10,2) NULL COMMENT '时间段开始时价格',
  `close` DECIMAL(10,2) NULL COMMENT '时间段结束时价格',
  `low` DECIMAL(10,2) NULL COMMENT '最低价',
  `high` DECIMAL(10,2) NULL COMMENT '最高价',
  `volume` BIGINT NULL COMMENT '成交的股票数量',
  `money` DECIMAL(20,2) NULL COMMENT '成交的金额',
  `factor` DECIMAL(15,8) NULL COMMENT '前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor',
  `high_limit` DECIMAL(10,2) NULL COMMENT '涨停价',
  `low_limit` DECIMAL(10,2) NULL COMMENT '跌停价',
  `avg` DECIMAL(10,2) NULL COMMENT '这段时间的平均价, 等于money/volume',
  `pre_close` DECIMAL(10,2) NULL COMMENT '前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格',
  `paused` TINYINT NULL COMMENT '布尔值, 这只股票是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0',
  PRIMARY KEY (`security`, `kday`))
COMMENT = '日线行情数据——股票代码模5余2';

CREATE TABLE `jqdata`.`t_kline_day_3` (
  `security` VARCHAR(20) NOT NULL COMMENT '股票代码',
  `kday` DATE NOT NULL COMMENT '日期',
  `open` DECIMAL(10,2) NULL COMMENT '时间段开始时价格',
  `close` DECIMAL(10,2) NULL COMMENT '时间段结束时价格',
  `low` DECIMAL(10,2) NULL COMMENT '最低价',
  `high` DECIMAL(10,2) NULL COMMENT '最高价',
  `volume` BIGINT NULL COMMENT '成交的股票数量',
  `money` DECIMAL(20,2) NULL COMMENT '成交的金额',
  `factor` DECIMAL(15,8) NULL COMMENT '前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor',
  `high_limit` DECIMAL(10,2) NULL COMMENT '涨停价',
  `low_limit` DECIMAL(10,2) NULL COMMENT '跌停价',
  `avg` DECIMAL(10,2) NULL COMMENT '这段时间的平均价, 等于money/volume',
  `pre_close` DECIMAL(10,2) NULL COMMENT '前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格',
  `paused` TINYINT NULL COMMENT '布尔值, 这只股票是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0',
  PRIMARY KEY (`security`, `kday`))
COMMENT = '日线行情数据——股票代码模5余3';

CREATE TABLE `jqdata`.`t_kline_day_4` (
  `security` VARCHAR(20) NOT NULL COMMENT '股票代码',
  `kday` DATE NOT NULL COMMENT '日期',
  `open` DECIMAL(10,2) NULL COMMENT '时间段开始时价格',
  `close` DECIMAL(10,2) NULL COMMENT '时间段结束时价格',
  `low` DECIMAL(10,2) NULL COMMENT '最低价',
  `high` DECIMAL(10,2) NULL COMMENT '最高价',
  `volume` BIGINT NULL COMMENT '成交的股票数量',
  `money` DECIMAL(20,2) NULL COMMENT '成交的金额',
  `factor` DECIMAL(15,8) NULL COMMENT '前复权因子, 我们提供的价格都是前复权后的, 但是利用这个值可以算出原始价格, 方法是价格除以factor, 比如: close/factor',
  `high_limit` DECIMAL(10,2) NULL COMMENT '涨停价',
  `low_limit` DECIMAL(10,2) NULL COMMENT '跌停价',
  `avg` DECIMAL(10,2) NULL COMMENT '这段时间的平均价, 等于money/volume',
  `pre_close` DECIMAL(10,2) NULL COMMENT '前一个单位时间结束时的价格, 按天则是前一天的收盘价, 按分钟这是前一分钟的结束价格',
  `paused` TINYINT NULL COMMENT '布尔值, 这只股票是否停牌, 停牌时open/close/low/high/pre_close依然有值,都等于停牌前的收盘价, volume=money=0',
  PRIMARY KEY (`security`, `kday`))
COMMENT = '日线行情数据——股票代码模5余4';


CREATE TABLE `jqdata`.`t_valuation_0` (
  `code` VARCHAR(20) NOT NULL COMMENT '股票代码  带后缀.XSHE/.XSHG',
  `day` DATE NOT NULL COMMENT '取数据的日期',
  `capitalization` DECIMAL(20,4) NULL COMMENT '总股本(万股)     公司已发行的普通股股份总数(包含A股，B股和H股的总股本)',
  `circulating_cap` DECIMAL(20,4) NULL COMMENT '流通股本(万股)     公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)',
  `market_cap` DECIMAL(20,10) NULL COMMENT '总市值(亿元)     A股收盘价*已发行股票总股本（A股+B股+H股）',
  `circulating_market_cap` DECIMAL(20,10) NULL COMMENT '流通市值(亿元)     流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。     A股市场的收盘价*A股市场的流通股数',
  `turnover_ratio` DECIMAL(10,4) NULL COMMENT '换手率(%)     指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。     换手率=[指定交易日成交量(手)100/截至该日股票的自由流通股本(股)]100%',
  `pe_ratio` DECIMAL(15,4) NULL COMMENT '市盈率(PE, TTM)     每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险     市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 当日人民币外汇挂牌价 * 截止当日公司总股本）/归属于母公司股东的净利润TTM。',
  `pe_ratio_lyr` DECIMAL(15,4) NULL COMMENT '以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS     市盈率（PE）=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的净利润。',
  `pb_ratio` DECIMAL(15,4) NULL COMMENT '市净率(PB)     每股股价与每股净资产的比率     市净率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的权益。',
  `ps_ratio` DECIMAL(15,4) NULL COMMENT '市销率(PS, TTM)     市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。     市销率TTM=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/营业总收入TTM',
  `pcf_ratio` DECIMAL(15,4) NULL COMMENT '市现率(PCF, 现金净流量TTM)     每股市价为每股现金净流量的倍数     市现率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM',
  PRIMARY KEY (`code`, `day`))
COMMENT = '市值数据-股票代码模5余0';

CREATE TABLE `jqdata`.`t_valuation_1` (
  `code` VARCHAR(20) NOT NULL COMMENT '股票代码  带后缀.XSHE/.XSHG',
  `day` DATE NOT NULL COMMENT '取数据的日期',
  `capitalization` DECIMAL(20,4) NULL COMMENT '总股本(万股)     公司已发行的普通股股份总数(包含A股，B股和H股的总股本)',
  `circulating_cap` DECIMAL(20,4) NULL COMMENT '流通股本(万股)     公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)',
  `market_cap` DECIMAL(20,10) NULL COMMENT '总市值(亿元)     A股收盘价*已发行股票总股本（A股+B股+H股）',
  `circulating_market_cap` DECIMAL(20,10) NULL COMMENT '流通市值(亿元)     流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。     A股市场的收盘价*A股市场的流通股数',
  `turnover_ratio` DECIMAL(10,4) NULL COMMENT '换手率(%)     指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。     换手率=[指定交易日成交量(手)100/截至该日股票的自由流通股本(股)]100%',
  `pe_ratio` DECIMAL(15,4) NULL COMMENT '市盈率(PE, TTM)     每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险     市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 当日人民币外汇挂牌价 * 截止当日公司总股本）/归属于母公司股东的净利润TTM。',
  `pe_ratio_lyr` DECIMAL(15,4) NULL COMMENT '以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS     市盈率（PE）=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的净利润。',
  `pb_ratio` DECIMAL(15,4) NULL COMMENT '市净率(PB)     每股股价与每股净资产的比率     市净率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的权益。',
  `ps_ratio` DECIMAL(15,4) NULL COMMENT '市销率(PS, TTM)     市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。     市销率TTM=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/营业总收入TTM',
  `pcf_ratio` DECIMAL(15,4) NULL COMMENT '市现率(PCF, 现金净流量TTM)     每股市价为每股现金净流量的倍数     市现率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM',
  PRIMARY KEY (`code`, `day`))
COMMENT = '市值数据-股票代码模5余1';

CREATE TABLE `jqdata`.`t_valuation_2` (
  `code` VARCHAR(20) NOT NULL COMMENT '股票代码  带后缀.XSHE/.XSHG',
  `day` DATE NOT NULL COMMENT '取数据的日期',
  `capitalization` DECIMAL(20,4) NULL COMMENT '总股本(万股)     公司已发行的普通股股份总数(包含A股，B股和H股的总股本)',
  `circulating_cap` DECIMAL(20,4) NULL COMMENT '流通股本(万股)     公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)',
  `market_cap` DECIMAL(20,10) NULL COMMENT '总市值(亿元)     A股收盘价*已发行股票总股本（A股+B股+H股）',
  `circulating_market_cap` DECIMAL(20,10) NULL COMMENT '流通市值(亿元)     流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。     A股市场的收盘价*A股市场的流通股数',
  `turnover_ratio` DECIMAL(10,4) NULL COMMENT '换手率(%)     指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。     换手率=[指定交易日成交量(手)100/截至该日股票的自由流通股本(股)]100%',
  `pe_ratio` DECIMAL(15,4) NULL COMMENT '市盈率(PE, TTM)     每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险     市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 当日人民币外汇挂牌价 * 截止当日公司总股本）/归属于母公司股东的净利润TTM。',
  `pe_ratio_lyr` DECIMAL(15,4) NULL COMMENT '以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS     市盈率（PE）=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的净利润。',
  `pb_ratio` DECIMAL(15,4) NULL COMMENT '市净率(PB)     每股股价与每股净资产的比率     市净率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的权益。',
  `ps_ratio` DECIMAL(15,4) NULL COMMENT '市销率(PS, TTM)     市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。     市销率TTM=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/营业总收入TTM',
  `pcf_ratio` DECIMAL(15,4) NULL COMMENT '市现率(PCF, 现金净流量TTM)     每股市价为每股现金净流量的倍数     市现率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM',
  PRIMARY KEY (`code`, `day`))
COMMENT = '市值数据-股票代码模5余2';

CREATE TABLE `jqdata`.`t_valuation_3` (
  `code` VARCHAR(20) NOT NULL COMMENT '股票代码  带后缀.XSHE/.XSHG',
  `day` DATE NOT NULL COMMENT '取数据的日期',
  `capitalization` DECIMAL(20,4) NULL COMMENT '总股本(万股)     公司已发行的普通股股份总数(包含A股，B股和H股的总股本)',
  `circulating_cap` DECIMAL(20,4) NULL COMMENT '流通股本(万股)     公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)',
  `market_cap` DECIMAL(20,10) NULL COMMENT '总市值(亿元)     A股收盘价*已发行股票总股本（A股+B股+H股）',
  `circulating_market_cap` DECIMAL(20,10) NULL COMMENT '流通市值(亿元)     流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。     A股市场的收盘价*A股市场的流通股数',
  `turnover_ratio` DECIMAL(10,4) NULL COMMENT '换手率(%)     指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。     换手率=[指定交易日成交量(手)100/截至该日股票的自由流通股本(股)]100%',
  `pe_ratio` DECIMAL(15,4) NULL COMMENT '市盈率(PE, TTM)     每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险     市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 当日人民币外汇挂牌价 * 截止当日公司总股本）/归属于母公司股东的净利润TTM。',
  `pe_ratio_lyr` DECIMAL(15,4) NULL COMMENT '以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS     市盈率（PE）=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的净利润。',
  `pb_ratio` DECIMAL(15,4) NULL COMMENT '市净率(PB)     每股股价与每股净资产的比率     市净率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的权益。',
  `ps_ratio` DECIMAL(15,4) NULL COMMENT '市销率(PS, TTM)     市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。     市销率TTM=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/营业总收入TTM',
  `pcf_ratio` DECIMAL(15,4) NULL COMMENT '市现率(PCF, 现金净流量TTM)     每股市价为每股现金净流量的倍数     市现率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM',
  PRIMARY KEY (`code`, `day`))
COMMENT = '市值数据-股票代码模5余3';

CREATE TABLE `jqdata`.`t_valuation_4` (
  `code` VARCHAR(20) NOT NULL COMMENT '股票代码  带后缀.XSHE/.XSHG',
  `day` DATE NOT NULL COMMENT '取数据的日期',
  `capitalization` DECIMAL(20,4) NULL COMMENT '总股本(万股)     公司已发行的普通股股份总数(包含A股，B股和H股的总股本)',
  `circulating_cap` DECIMAL(20,4) NULL COMMENT '流通股本(万股)     公司已发行的境内上市流通、以人民币兑换的股份总数(A股市场的流通股本)',
  `market_cap` DECIMAL(20,10) NULL COMMENT '总市值(亿元)     A股收盘价*已发行股票总股本（A股+B股+H股）',
  `circulating_market_cap` DECIMAL(20,10) NULL COMMENT '流通市值(亿元)     流通市值指在某特定时间内当时可交易的流通股股数乘以当时股价得出的流通股票总价值。     A股市场的收盘价*A股市场的流通股数',
  `turnover_ratio` DECIMAL(10,4) NULL COMMENT '换手率(%)     指在一定时间内市场中股票转手买卖的频率，是反映股票流通性强弱的指标之一。     换手率=[指定交易日成交量(手)100/截至该日股票的自由流通股本(股)]100%',
  `pe_ratio` DECIMAL(15,4) NULL COMMENT '市盈率(PE, TTM)     每股市价为每股收益的倍数，反映投资人对每元净利润所愿支付的价格，用来估计股票的投资报酬和风险     市盈率（PE，TTM）=（股票在指定交易日期的收盘价 * 当日人民币外汇挂牌价 * 截止当日公司总股本）/归属于母公司股东的净利润TTM。',
  `pe_ratio_lyr` DECIMAL(15,4) NULL COMMENT '以上一年度每股盈利计算的静态市盈率. 股价/最近年度报告EPS     市盈率（PE）=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的净利润。',
  `pb_ratio` DECIMAL(15,4) NULL COMMENT '市净率(PB)     每股股价与每股净资产的比率     市净率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/归属母公司股东的权益。',
  `ps_ratio` DECIMAL(15,4) NULL COMMENT '市销率(PS, TTM)     市销率为股票价格与每股销售收入之比，市销率越小，通常被认为投资价值越高。     市销率TTM=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/营业总收入TTM',
  `pcf_ratio` DECIMAL(15,4) NULL COMMENT '市现率(PCF, 现金净流量TTM)     每股市价为每股现金净流量的倍数     市现率=（股票在指定交易日期的收盘价 * 当日人民币外汇牌价 * 截至当日公司总股本）/现金及现金等价物净增加额TTM',
  PRIMARY KEY (`code`, `day`))
COMMENT = '市值数据-股票代码模5余4';