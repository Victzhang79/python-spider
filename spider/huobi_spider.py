# coding:utf8
import json
from datetime import datetime

import pymysql
import requests

huoBi_url = 'https://www.huobipro.com/-/x/hb/p/api/contents/pro/list_notice?page=1&limit=325&language=zh-cn'
huoBi_detail_url = 'https://www.huobipro.com/-/x/hb/p/api/contents/pro/notice/{}'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 ' \
            'Safari/537.36'
headers = {'User-Agent': userAgent}

if __name__ == '__main__':
    db = pymysql.connect(
        host='101.201.140.96',
        port=3306,
        user='root',
        password='Galaxy@91',
        db='coin',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()

    insert_sql = 'insert into notice' \
                 '(market_id, market_notice_id, title, created, source, content, top_notice, weight)values' \
                 '(%d, %d, "%s", "%s", "%s", "%s", "%s", %d)'

    # response = requests.request('GET', huoBi_url, headers=headers)
    # content = response.content.decode('utf-8')
    # data = json.loads(content)['data']['items']

    notice_list = {
        "success": True,
        "status": 0,
        "message": "success",
        "data": {
            "start": 0,
            "limit": 325,
            "totalCount": 325,
            "pages": 1,
            "items": [{
                "id": 1622,
                "title": "火币全球专业站5月23日发布火币主力指数（HUOBI 10）",
                "created": 1527043265000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站已于新加坡时间5月23日发布了火币主力指数。该指数选取了火币全球专业站上线币种中市值高、规模大、流通性好的10种数字资产，采用资产分层、成交量派许加权等先进技术编制，以综合反映火币……",
                "topNotice": True,
                "weight": 71
            }, {
                "id": 1616,
                "title": "LBA交易排名赛 TOP20瓜分250万LBA",
                "created": 1526967006000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间5月22日16:00 Libra Credit (LBA)充值业务。5月23日16:00在创新区开放LBA/BTC, LBA/ETH交易。5月28日16:00开放 L……",
                "topNotice": True,
                "weight": 70
            }, {
                "id": 1611,
                "title": "火币全球专业站5月21日15:30全球首发KAN (KAN)",
                "created": 1526887830000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间5月21日20:00 KAN (KAN)充值业务。5月25日11:00在新创区开放KAN/BTC, KAN/ETH交易。5月27日20:00开放 KAN提现业务。 点……",
                "topNotice": True,
                "weight": 69
            }, {
                "id": 1596,
                "title": "CDC交易排名赛 日榜 TOP3 周榜TOP10瓜分888万CDC",
                "created": 1526876844000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间2018年5月21日12:00-5月27日12:00期间，成功报名且累计CDC交易量（买入量+卖出量且不含自成交） 日榜TOP3 周榜TOP10 实名用户可获如下奖励： 点此报名: h……",
                "topNotice": True,
                "weight": 67
            }, {
                "id": 1569,
                "title": "BKBT交易排名赛 TOP10000瓜分1800万BKBT",
                "created": 1526452746000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所(Huobi HADAX)将定于新加坡时间5月16日14:30开放 币快报 (BKBT)充值业务。5月17日14:00在HADAX开放BKBT/BTC和BKBT/ETH交易……",
                "topNotice": True,
                "weight": 63
            }, {
                "id": 1556,
                "title": "PORTAL交易排名赛 TOP20瓜分60万PORTAL+10000HT",
                "created": 1526442466000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间2018年5月16日12:00-5月22日 12:00期间，成功报名且累计PORTAL交易量（买入量+卖出量且不含自成交）TOP20名实名用户可获如下奖励： 点此报名: https:/……",
                "topNotice": True,
                "weight": 61
            }, {
                "id": 1312,
                "title": "火币全球专业站拉新返佣项目全面上线",
                "created": 1523439463000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站拉新返佣项目全面上线。通过专属邀请码/链接邀请好友注册火币全球专业站。好友接受邀请后，交易扣除手续费的同时，会产生相应比例的返佣。返佣的形式以USDT或点卡的形式返佣到您的交易账户……",
                "topNotice": True,
                "weight": 7
            }, {
                "id": 1634,
                "title": "火币全球专业站暂停EduCoin(EDU)充提币和交易业务",
                "created": 1527096801000,
                "source": "1",
                "content": "尊敬的用户： 由于EduCoin(EDU)官方智能合约升级，火币全球专业站暂停EduCoin(EDU)的充提币和交易业务。待EduCoin官方升级完成，我们将在第一时间恢复充提币业务，后续将以公告形式告知。为……",
                "topNotice": False,
                "weight": 72
            }, {
                "id": 1632,
                "title": "火币Pro暂停EduCoin (EDU)充提币业务和交易的公告",
                "created": 1527089262000,
                "source": "1",
                "content": "尊敬的用户： 应EduCoin (EDU)项目方的要求，火币Pro暂停EDU充提币业务，并同时暂停EDU/BTC和EDU/ETH的交易，具体开放时间另行通知。火币Pro会随时与项目方保持联络，待项目方有最新进……",
                "topNotice": False,
                "weight": 71
            }, {
                "id": 1603,
                "title": "HADAX第三期第四轮投票上币结果公布和下一轮投票上币的安排",
                "created": 1526882183000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第三期第四轮投票上币已于新加坡标准时间5月21日13:00结束，经过后台数据处理确认所有投票数据有效，最终胜出项目为Sharex Exchange Coin（……",
                "topNotice": False,
                "weight": 68
            }, {
                "id": 1591,
                "title": "火币全球专业站关于暂停NAS提币业务的公告",
                "created": 1526872538000,
                "source": "1",
                "content": "尊敬的用户： 因NAS智能合约的容错机制正在升级完善，火币全球专业站现已暂停NAS提币业务，恢复时间将以公告另行通知。暂停期间为此带来的不便，敬请谅解！ 火币全球专业站 2018年5月21日",
                "topNotice": False,
                "weight": 67
            }, {
                "id": 1588,
                "title": "火币全球专业站暂停BTG充值业务的公告",
                "created": 1526708916000,
                "source": "1",
                "content": "尊敬的用户： 因BTG区块链网络不稳定，火币全球专业站已暂停BTG充值业务，待其网络稳定后恢复。恢复时间将以公告另行通知，暂停期间为此带来的不便，敬请谅解！ 火币全球专业站 2018年5月19日",
                "topNotice": False,
                "weight": 67
            }, {
                "id": 1564,
                "title": "HADAX第三期第三轮投票上币结果公布和下一轮投票上币的安排",
                "created": 1526450071000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第三期第三轮投票上币已于新加坡标准时间5月16日13:00结束，经过后台数据处理确认所有投票数据有效，最终胜出项目为Globalvillage Ecosyst……",
                "topNotice": False,
                "weight": 66
            }, {
                "id": 1580,
                "title": "火币全球专业站关于5月12日部分杠杆价格异常的处理办法",
                "created": 1526549363000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间5月12日下午14时左右，火币Pro平台上的 DTA\\ONT\\BTM\\IOST 四个交易盘面出现剧烈行情波动，导致部分用户爆仓，对此我们做了深入调查。 火币Pro的杠杆一直有爆仓熔断……",
                "topNotice": False,
                "weight": 63
            }, {
                "id": 1554,
                "title": "火币全球专业站5月16日11:00恢复BCH充提业务",
                "created": 1526440783000,
                "source": "1",
                "content": "尊敬的用户： 因BCH完成硬分叉，火币全球专业站已于新加坡时间5月16日11:00恢复BCH充提业务。暂停期间造成的不便，敬请谅解。 火币全球专业站 2018年5月16日",
                "topNotice": False,
                "weight": 60
            }, {
                "id": 1549,
                "title": "火币全球专业站暂停BCH充提业务",
                "created": 1526395671000,
                "source": "1",
                "content": "尊敬的用户： 据BCH官方消息，BCH将于北京时间5月16日0:00左右执行硬分叉，将区块大小从8MB增加至32MB。因此，火币全球专业站现已暂停BCH充提币业务，待硬分叉完成后恢复。恢复时间以公告另行通知。……",
                "topNotice": False,
                "weight": 58
            }, {
                "id": 1516,
                "title": "火币全球专业站将于5月13日10:00-11:00期间进行系统维护的公告",
                "created": 1526033534000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间5月13日10:00-11:00期间进行系统维护，在此期间，Huobi Pro和HADAX网站和APP将无法交易，API暂停提供数据，OTC将无法划转至PRO站。如维……",
                "topNotice": False,
                "weight": 58
            }, {
                "id": 1539,
                "title": "Huobi HADAX将于5月15日14:30上线 Aeternity (AE)",
                "created": 1526366300000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所(Huobi HADAX)将定于新加坡时间5月15日14:30开放Aeternity (AE)充值业务。5月16日14:00在HADAX开放AE/BTC和AE/ETH交易。……",
                "topNotice": False,
                "weight": 57
            }, {
                "id": 1546,
                "title": "PC交易排名赛 TOP20瓜分2000万PC",
                "created": 1526376081000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间2018年5月15日18:00 - 5月22日18:00 期间，成功报名且累计PC交易量（买入量+卖出量且不含自成交）TOP20名实名用户可获如下奖励： 点此报名: https://j……",
                "topNotice": False,
                "weight": 56
            }, {
                "id": 1534,
                "title": "火币全球专业站完成eosDAC糖果发放",
                "created": 1526294110000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站已根据新加坡时间2018年4月15日9:00:00全站EOS资产（不含借贷部分）快照持仓数据按照1:1比例分发了eosDAC糖果（包括持仓小于100EOS的用户），您可至HADAX……",
                "topNotice": False,
                "weight": 56
            }, {
                "id": 1532,
                "title": "火币全球专业站上线点卡抵扣借贷利息功能",
                "created": 1526284329000,
                "source": "1",
                "content": "尊敬的用户： 为了增加火币点卡使用场景，让更多持有点卡的用户切实享有更多手续费优惠，火币全球专业站现已上线点卡抵扣借贷利息功能，如您有未还借贷，每日计息时，如系统检测到您的账户中有可用的点卡，将自动抵扣未偿还……",
                "topNotice": False,
                "weight": 56
            }, {
                "id": 1528,
                "title": "Huobi HADAX将于5月14日14:30上线 Republic Protocol(REN)",
                "created": 1526279570000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所(Huobi HADAX)将定于新加坡时间5月14日14:30开放 Republic Protocol (REN)充值业务。5月15日14:00在HADAX开放REN/BT……",
                "topNotice": False,
                "weight": 56
            }, {
                "id": 1522,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于5月14日11:30上线 推广链",
                "created": 1526268864000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所(Huobi HADAX)将定于新加坡时间5月14日11:30开放 推广链（PromotionChain）充值业务。5月15日11:00在HADAX开放PC/BTC和PC/……",
                "topNotice": False,
                "weight": 55
            }, {
                "id": 1508,
                "title": "SOC交易排名赛 TOP20都有奖",
                "created": 1526020039000,
                "source": "1",
                "content": "尊敬的用户： 因All Sports Blockchain (SOC)符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于5月11日18:00上线SOC/USDT交易。 【SOC交易排名赛 T……",
                "topNotice": False,
                "weight": 54
            }, {
                "id": 1502,
                "title": "SMT新用户福利和交易排名赛",
                "created": 1525924178000,
                "source": "1",
                "content": "尊敬的用户： 因SmartMesh合约漏洞问题，应SMT项目方要求，火币全球专业站于4月25日暂停了SMT交易。现SMT官方已更换了新的智能合约，更换智能合约后的SMT将不再存在安全漏洞。因此火币全球专业站将……",
                "topNotice": False,
                "weight": 53
            }, {
                "id": 1506,
                "title": "​HADAX第三期第二轮投票上币结果公布和下一轮投票上币的安排",
                "created": 1526018128000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第三期第二轮投票上币已于新加坡标准时间5月11日13:00结束，经过后台数据处理确认所有投票数据有效，最终胜出项目为影链（INC）、ZJL Distribut……",
                "topNotice": False,
                "weight": 52
            }, {
                "id": 1498,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于5月9日14:30上线 Themis",
                "created": 1525847512000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所(Huobi HADAX)将定于新加坡时间5月9日14:30开放 Themis (GET)充值业务。5月10日14:00在HADAX开放GET/BTC和GET/ETH交易。……",
                "topNotice": False,
                "weight": 52
            }, {
                "id": 1492,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于5月9日11:30上线 Matrix(MAN)",
                "created": 1525836752000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所(Huobi HADAX)将定于新加坡时间5月9日11:30开放 MATRIX (MAN)充值业务。5月10日11:00在HADAX开放MAN/BTC和MAN/ETH交易。……",
                "topNotice": False,
                "weight": 51
            }, {
                "id": 1484,
                "title": "火币全球专业站将于5月8日17:00 IOTA 开盘交易",
                "created": 1525763828000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将定于新加坡时间5月8日17:00在主区开放IOTA/BTC, IOTA/ETH和IOTA/USDT交易。对此开盘延迟而造成的不便，敬请谅解。 【IOTA交易排名赛 TOP20都有……",
                "topNotice": False,
                "weight": 48
            }, {
                "id": 1474,
                "title": "火币全球专业站关于开放NAS新币提币业务的公告",
                "created": 1525662060000,
                "source": "1",
                "content": "尊敬的用户 火币全球专业站将于新加坡时间5月7日11:00开启NAS新币的提币业务。NAS主链已上线，火币全球专业站将不再支持NAS旧币的提币，您只能提现NAS新币，请您务必使用NAS主链的提币地址进行提币。……",
                "topNotice": False,
                "weight": 47
            }, {
                "id": 1480,
                "title": "HADAX投票上币-超级投票节点专场活动第二轮开启",
                "created": 1525758891000,
                "source": "1",
                "content": "尊敬的用户： HADAX于4月19日举办的“超级节点专场上币活动”，取得了业界的广泛好评。超级节点凭借专业能力和行业经验，有效地选出了不少优质项目。因此，我们决定持续开展“超级节点专场上币活动”。第二轮活动将……",
                "topNotice": False,
                "weight": 46
            }, {
                "id": 1460,
                "title": "HADAX第三期第一轮投票上币结果公布及HT返还处理的公告",
                "created": 1525410645000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第三期第一轮投票上币已于新加坡标准时间5月4日13:00结束，经过后台数据处理确认所有投票数据有效，最终胜出项目为推广链（PC）、Themis（GET）、MA……",
                "topNotice": False,
                "weight": 45
            }, {
                "id": 1452,
                "title": "火币全球专业站关于IOTA开盘延迟的公告",
                "created": 1525404229000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站原计划于新加坡时间5月4日16:00开盘的IOTA/BTC, IOTA/ETH和IOTA/USDT交易将延迟，具体开放时间将以公告形式另行通知。对此造成的不便，敬请谅解。 火币全球……",
                "topNotice": False,
                "weight": 44
            }, {
                "id": 1466,
                "title": "火币OTC全球商家招募",
                "created": 1525439103000,
                "source": "1",
                "content": "尊敬的用户： 火币OTC致力于为全球有数字资产兑换需求的用户提供一个可信赖的第三方媒介平台。 什么是全球商家： 全球商家是具备发布特定法币广告资格的专业团队。 成为商家好处: 商家可以通过提供发布法币广告赚取……",
                "topNotice": False,
                "weight": 43
            }, {
                "id": 1454,
                "title": "火币全球专业站关于恢复DBC、RPX、ONT充币业务的公告",
                "created": 1525404253000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站现已恢复DBC、RPX、ONT充币业务，为此造成的不便，敬请谅解！ 火币全球专业站 2018年5月4日",
                "topNotice": False,
                "weight": 43
            }, {
                "id": 1444,
                "title": "IOTA交易排名赛 TOP20都有奖",
                "created": 1525334409000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间5月3日16:00 IOTA (IOTA)充值业务。5月4日16:00在主区开放IOTA/BTC, IOTA/ETH和IOTA/USDT交易。5月6日16:00开放I……",
                "topNotice": False,
                "weight": 43
            }, {
                "id": 1440,
                "title": "火币全球专业站5月3日11:00上线 Wanchain (WAN)",
                "created": 1525316454000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间5月3日11:00 Wanchain (WAN)充值业务。5月4日11:00在创新区开放WAN /BTC, WAN/ETH交易。5月6日11:00开放 WAN提现业务……",
                "topNotice": False,
                "weight": 42
            }, {
                "id": 1437,
                "title": "火币全球专业站将于5月3日12:00-20:00期间暂停亦来云（ELA）充提业务的公告",
                "created": 1525315773000,
                "source": "1",
                "content": "尊敬的用户： 因ELA进行技术升级，火币全球专业站将于新加坡时间5月3日12:00-20:00期间暂停ELA充提业务。为此造成的不便，敬请谅解！ 亦来云官方升级公告： https://www.elastos.……",
                "topNotice": False,
                "weight": 39
            }, {
                "id": 1448,
                "title": "HADAX第三期第一轮投票上币结果公布后的处理和下一轮投票上币的安排",
                "created": 1525345430000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第三期第一轮投票上币将于新加坡标准时间5月4日13:00结束，下面是对本轮投票结果公布后的处理和下一轮投票上币的安排： 一、第三期第一轮投票上币： 1、 本轮……",
                "topNotice": False,
                "weight": 38
            }, {
                "id": 1433,
                "title": "火币全球专业站关于恢复NAS充值业务并开启NAS换币通道的公告",
                "created": 1525273084000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站已恢复NAS充值业务，并同时开启NAS换币通道，即NAS的充币地址将有两个。如您持有NAS旧币（基于以太坊ERC20技术形成的“星云币”），您需点击“旧地址充币”查看充币地址；如您……",
                "topNotice": False,
                "weight": 36
            }, {
                "id": 1430,
                "title": "火币全球专业站5月2日15:00上线 BnkToTheFuture(BFT)",
                "created": 1525244408000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间5月2日15:00 BnkToTheFuture (BFT)充值业务。5月3日15:00在创新区开放BFT /BTC, BFT/ETH交易。5月4日15:00开放 B……",
                "topNotice": False,
                "weight": 34
            }, {
                "id": 1427,
                "title": "火币全球专业站关于支持星云币(NAS)主网上线后换币的公告",
                "created": 1525226569000,
                "source": "1",
                "content": "尊敬的用户： 星云币（NAS）主网已于2018年3月30日上线，并将于近期正式开启主网星云币换币工作，火币全球专业站作为NAS官方推荐的换币平台，将在同一时间开启换币通道。届时，您可以在火币全球专业站将NAS……",
                "topNotice": False,
                "weight": 33
            }, {
                "id": 1414,
                "title": "火币全球专业站将于4月28日12:00 Steem(STEEM)开盘交易",
                "created": 1524844532000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将定于新加坡时间4月28日12:00在主区开放STEEM/BTC, STEEM/ETH和STEEM/USDT交易。对此开盘延迟而造成的不便，敬请谅解。 火币全球专业站 2018年4……",
                "topNotice": False,
                "weight": 31
            }, {
                "id": 1408,
                "title": "关于取消HADAX投资者准入门槛的公告",
                "created": 1524747175000,
                "source": "1",
                "content": "尊敬的用户： HADAX是火币Pro推出的全新子品牌火币自主数字资产交易所（Huobi Autonomous Digital Asset eXchange，简称HADAX）。成立之初，我们旨在服务于专业数字资……",
                "topNotice": False,
                "weight": 30
            }, {
                "id": 1416,
                "title": "火币全球专业站关于暂停DBC、RPX、ONT充币业务的公告",
                "created": 1524844574000,
                "source": "1",
                "content": "尊敬的用户： 由于NEO节点前后版本的兼容问题，火币全球专业站已暂停DBC、RPX、ONT充币业务，预计将于5月初恢复。如提前恢复，我们将以公告形式告知。为此造成的不便，敬请谅解！ 火币全球专业站 2018年……",
                "topNotice": False,
                "weight": 28
            }, {
                "id": 1423,
                "title": "火币全球专业站将于4月28日24:00恢复Propy(PROPY)充提业务",
                "created": 1524915650000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间4月28日24:00恢复Propy(PROPY)充提币业务，暂停期间造成的不便，敬请谅解。 火币全球专业站 2018年4月28日",
                "topNotice": False,
                "weight": 27
            }, {
                "id": 1401,
                "title": "火币全球专业站关于恢复ERC20币种充提的公告",
                "created": 1524716639000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站现已恢复除Propy(PROPY）和Smartmesh(SMT)外其他所有ERC20币种的充提业务，暂停期间的充值将陆续上账，其中PROPY和SMT的充提业务恢复时间将以公告形式另……",
                "topNotice": False,
                "weight": 27
            }, {
                "id": 1399,
                "title": "火币全球专业站关于STEEM开盘",
                "created": 1524715878000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月26日13:00开盘的STEEM/BTC, STEEM/ETH和STEEM/USDT交易将延迟，将以公告形式另行通知。对此造成的不便，敬请谅解。 火币全球专业站 ……",
                "topNotice": False,
                "weight": 26
            }, {
                "id": 1393,
                "title": "火币全球专业站4月25日13:00上线 Steem",
                "created": 1524632404000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月25日13:00 Steem (STEEM)充值业务。4月26日13:00在主区开放STEEM/BTC, STEEM/ETH和STEEM/USDT交易。4月28日……",
                "topNotice": False,
                "weight": 25
            }, {
                "id": 1391,
                "title": "火币全球专业站关于恢复非ERC20币种充提的公告",
                "created": 1524628458000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站现已恢复非ERC20币种的充提业务，ERC20币种充提恢复时间将以公告形式另行通知。暂停期间为您带来的不便，敬请谅解！ 火币全球专业站 2018年4月25日",
                "topNotice": False,
                "weight": 24
            }, {
                "id": 1387,
                "title": "火币Pro暂停SMT交易的公告",
                "created": 1524624162000,
                "source": "1",
                "content": "尊敬的用户： 应SmartMesh (SMT)项目方的要求，火币Pro暂停SMT/USDT、SMT/BTC和SMT/ETH的交易，具体开放时间另行通知。火币Pro会随时与项目方保持联络，待项目方有最新进展我们……",
                "topNotice": False,
                "weight": 24
            }, {
                "id": 1382,
                "title": "关于火币Pro暂停所有币种充提币业务的通知",
                "created": 1524618613000,
                "source": "1",
                "content": "尊敬的用户： SmartMesh(SMT)项目方反馈今日凌晨发现其交易存在异常问题，经初步排查，SMT的以太坊智能合约存在漏洞。火币Pro也同期检测到TXID为0x0775e55c402281e8ff24cf……",
                "topNotice": False,
                "weight": 23
            }, {
                "id": 1380,
                "title": "HADAX投票上币第三期规则发布及第二期第四轮投票处理的公告",
                "created": 1524575715000,
                "source": "1",
                "content": "尊敬的用户： HT（火币全球通用积分）是构建火币生态的核心，发行至今我们正在有序推进各项基于HT的应用场景逐步落地，而HT持有者作为火币生态的参与者也将会获得越来越多的价值回馈。HADAX投票上币是基于HT的……",
                "topNotice": False,
                "weight": 23
            }, {
                "id": 1374,
                "title": "火币全球专业站将于4月24日18:00上线CTXC/USDT交易",
                "created": 1524549605000,
                "source": "1",
                "content": "尊敬的用户： 因 Cortex (CTXC)符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于4月24日18:00上线CTXC/USDT交易。 【CTXC再次空投HT持有者】 3月29日16……",
                "topNotice": False,
                "weight": 23
            }, {
                "id": 1372,
                "title": "杠杆免息 喜迎五一",
                "created": 1524542113000,
                "source": "1",
                "content": "亲爱的用户： 新加坡时间4月24日12:00 - 5月8日12:00，成功报名且参与杠杆交易的全站所有用户，活动期间USDT和BTC区的杠杆利息全免！ 点此报名：https://jinshuju.net/f/……",
                "topNotice": False,
                "weight": 22
            }, {
                "id": 1365,
                "title": "ACT交易赛 赢韩国两日游",
                "created": 1524456031000,
                "source": "1",
                "content": "尊敬的用户： 因 Achain (ACT)符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于4月23日18:00上线ACT/USDT交易。 【ACT交易赛 赢韩国两日游】 新加坡时间2018……",
                "topNotice": False,
                "weight": 18
            }, {
                "id": 1363,
                "title": "HADAX投票上币-超级投票节点专场活动投票结果公布",
                "created": 1524450718000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第一期超级投票节点专场活动于昨日新加坡标准时间4月22日13:00结束，参加本次专场活动的超级投票节点18家，30个项目共投出98票，其中第一名Hydro P……",
                "topNotice": False,
                "weight": 17
            }, {
                "id": 1350,
                "title": "HADAX投票上币-超级投票节点专场活动",
                "created": 1524127506000,
                "source": "1",
                "content": "尊敬的用户： HADAX投票上币上线以来，得到广大用户、项目方和合作伙伴的鼎力支持，至今已经成功举行5轮投票，特别感谢给予我们帮助和鞭策的各位伙伴。HADAX投票上币是社区化业务运作的首次尝试，特别是第二期引……",
                "topNotice": False,
                "weight": 16
            }, {
                "id": 1347,
                "title": "公链知识大奖赛 答题交易领大奖",
                "created": 1524042945000,
                "source": "1",
                "content": "尊敬的用户： 活动时间： 新加坡时间4月18日17:00 - 4月25日17:00 活动规则： 1. 活动期间参与EOS、ELF、IOST、ONT、ELA、ZIL、NAS其中任意一个知识小测试答题得分不低于6……",
                "topNotice": False,
                "weight": 15
            }, {
                "id": 1344,
                "title": "BTM交易赛 TOP20都有奖",
                "created": 1524024261000,
                "source": "1",
                "content": "尊敬的用户： 因 Bytom（BTM）符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于4月18日18:00上线BTM/USDT交易。 【BTM交易赛 TOP20都有奖】 新加坡时间2018……",
                "topNotice": False,
                "weight": 13
            }, {
                "id": 1339,
                "title": "Huobi HADAX定于4月17日14:30上线 DATx (DATX)",
                "created": 1523947183000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）定于新加坡时间4月17日14:30开放 DATx (DATX)充值业务。4月18日14:00在HADAX开放DATX/BTC和DATX/ETH交易……",
                "topNotice": False,
                "weight": 12
            }, {
                "id": 1252,
                "title": "超级火伴和火币火伴全球招募",
                "created": 1522545191000,
                "source": "1",
                "content": "火币全球区域负责人——超级火伴招募 什么是超级火伴？ 超级火伴，是火币在国家、重点区域的当地业务的重要合作伙伴，是火币在关键地区及国家的区域负责人，未来有机会发展成像韩国交易所类似的独立自营交易所。为火币在当……",
                "topNotice": False,
                "weight": 12
            }, {
                "id": 1335,
                "title": "YEE交易排名赛 TOP20都有奖",
                "created": 1523944507000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间2018年4月17日14:00 - 4月22日14:00期间，成功报名且累计YEE交易量（买入量+卖出量且不含自成交）TOP20名实名用户可获如下奖励： 点此报名： https://j……",
                "topNotice": False,
                "weight": 11
            }, {
                "id": 1331,
                "title": "火币全球专业站4月16日14:30上线 卡尔达诺 (ADA)",
                "created": 1523860222000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月16日14:30开放卡尔达诺 (ADA)充值业务。4月17日14:00在主区开放ADA/BTC, ADA/ETH和ADA/USDT交易。4月19日14:30开放A……",
                "topNotice": False,
                "weight": 10
            }, {
                "id": 1329,
                "title": "Huobi Token（HT）第一季度回购信息披露",
                "created": 1523850986000,
                "source": "1",
                "content": "尊敬的用户： 火币全球通用积分（Huobi Token）自从上线以来，备受关注，也得到了广大用户的支持和认可，火币全球专业站承诺拿出收入的20%来进行回购（收入折合USDT以3月31日收盘价格计算），同时按每……",
                "topNotice": False,
                "weight": 9
            }, {
                "id": 1326,
                "title": "OTC买币 免币币交易手续费",
                "created": 1523843074000,
                "source": "1",
                "content": "尊敬的用户： 活动时间： 新加坡时间4月16日10:00 - 4月23日18:00 活动规则： 活动期间在法币交易区买入BTC、ETH、USDT任意币种，即可获得币币交易区等额交易免手续费资格。 OTC交易用……",
                "topNotice": False,
                "weight": 8
            }, {
                "id": 1472,
                "title": "火币全球专业站关于开放NAS新币提币业务的公告",
                "created": 1525661764000,
                "source": "47",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间5月7日11:00开启NAS新币的提币业务。NAS主链已上线，火币全球专业站将不再支持NAS旧币的提币，您只能提现NAS新币，请您务必使用NAS主链的提币地址进行提币……",
                "topNotice": False,
                "weight": 1
            }, {
                "id": 1272,
                "title": "杠杆免息周 点卡疯狂送",
                "created": 1523238770000,
                "source": "1",
                "content": "尊敬的用户： 活动时间： 新加坡时间4月9日10:00 - 4月16日18:00 活动规则： 一、杠杆免息礼 活动期间参与杠杆交易的实名用户，活动期间杠杆利息全免！活动期间杠杆手续费贡献TOP10用户还可有机……",
                "topNotice": False,
                "weight": 1
            }, {
                "id": 1359,
                "title": "Huobi Token(HT)锁仓地址公示",
                "created": 1524311257000,
                "source": "1",
                "content": "尊敬的用户： Huobi Token(HT)第一季度回购信息已于新加坡时间4月16日披露，截至目前，投资者保护基金共有3,835.99万HT。超级节点，超级火伴及OTC商家，项目方保证金等共计锁仓：3,209……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1323,
                "title": "火币全球专业站将于4月15日18:00上线BTS/USDT交易",
                "created": 1523764833000,
                "source": "1",
                "content": "尊敬的用户： 因 比特股 (BTS)符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于4月15日18:00上线BTS/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年4月15日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1316,
                "title": "HADAX第二期第三轮投票上币结果公布及第四轮投票开启通知",
                "created": 1523525419000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期第三轮投票上币已于新加坡标准时间4月9日13:00结束，经过3个工作日的数据清洗和人工回访，最终胜出项目为Portal（PTC）和Game.com To……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1315,
                "title": "关于法币交易区国际化上线及系统更新的通知",
                "created": 1523514671000,
                "source": "1",
                "content": "尊敬的用户： 法币交易区将于新加坡时间4月13日上午06:00 进行系统更新，预计更新时间2小时，系统更新期间WEB、Android/iOS APP均无法使用。 建议您提前做好资产安排，以免行情波动造成资产损……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1308,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于4月11日14:30上线 18区(18T)",
                "created": 1523428203000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）将于新加坡时间4月11日14:30开放18区(18T)充值业务。4月12日14:00在HADAX开放18T/BTC和18T/ETH交易。4月13日……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1305,
                "title": "火币全球专业站将于4月11日18:00上线ZRX/ETH交易",
                "created": 1523419220000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月11日18:00在创新区开放ZRX/ETH交易。 祝您交易愉快！ 火币全球专业站 2018年4月11日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1302,
                "title": "火币全球专业站将为EOS用户空投eosDAC的公告",
                "created": 1523359194000,
                "source": "1",
                "content": "尊敬的用户： 根据eosDAC官方说明，将在新加坡时间2018年4月15日09:00:00为区块链上持有超过100EOS的用户按照1:1空投eosDAC代币。 火币全球专业站将支持eosDAC的空投计划，将在……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1295,
                "title": "HADAX第二期投票上币第三轮投票结果处理及未能入围项目退票时间安排的公告",
                "created": 1523346577000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期投票上币第三轮投票于昨日新加坡标准时间4月9日13:00结束，现对投票结果处理及本轮用户自主退票的安排如下： 本轮投票结果处理： 1、根据本轮投票规定，……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1290,
                "title": "火币全球专业站将于4月10日18:00上线AST/ETH交易",
                "created": 1523332803000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月10日18:00在创新区开放AST/ETH交易。 祝您交易愉快！ 火币全球专业站 2018年4月10日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1285,
                "title": "火币全球专业站将于4月9日17:00恢复CoinMeet(MEET)充提业务",
                "created": 1523263783000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间4月9日17:00恢复CoinMeet(MEET)充提币业务，暂停期间造成的不便，敬请谅解。 CoinMeet(MEET)已完成更名的公告：https://www.h……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1278,
                "title": "火币全球专业站关于CoinMeet更名的公告",
                "created": 1523254271000,
                "source": "1",
                "content": "尊敬的用户： CoinMeet官方智能合约完成升级，火币全球专业站将在新加坡时间2018年4月9日16:00左右完成CoinMeet更名，原CoinMeet币种代码MEE更名为MEET，原有MEE资产将同步映……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1276,
                "title": "火币全球专业站将于4月9日18:00上线ONT/USDT交易",
                "created": 1523253605000,
                "source": "1",
                "content": "尊敬的用户： 因 本体Ontology（ONT）符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于4月9日18:00上线ONT/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年4月……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1274,
                "title": "火币全球专业站将于4月9日16:00上线KNC/ETH交易",
                "created": 1523246404000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月9日16:00在创新区开放KNC/ETH交易。 祝您交易愉快！ 火币全球专业站 2018年4月9日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1269,
                "title": "火币全球专业站关于4月3日17:00-18:00暂停提币审核的公告",
                "created": 1522744131000,
                "source": "1",
                "content": "尊敬的用户： 因火币全球专业站系统维护，我们将在新加坡时间4月3日17:00起暂停提币审核，预计1小时内恢复，如系统维护提前完成，我们将会在第一时间恢复提币审核。为此造成的不便，敬请谅解！ 火币全球专业站 2……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1266,
                "title": "LET交易&持仓前十 赢澳门双日游",
                "created": 1522727725000,
                "source": "1",
                "content": "尊敬的用户： LET交易&持仓前十名用户均可获LET项目方组织的澳门双日游。 活动规则： 1. 交易前十：成功报名且新加坡时间4月3日12:00-4月10日12:00累计LET交易量（买入量+卖出量且不含自成……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1263,
                "title": "火币全球专业站4月2日14:30上线 比特股 (BTS)",
                "created": 1522650665000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间4月2日14:30开放比特股 (BTS)充值业务。4月3日14:00在创新区开放BTS/BTC和BTS/ETH交易。4月5日14:30开放BTS提现业务。 点此查看 ……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1260,
                "title": "火币全球专业站暂停CoinMeet(MEE)充提币业务",
                "created": 1522638927000,
                "source": "1",
                "content": "尊敬的用户： 由于CoinMeet官方智能合约升级，我们暂时暂停CoinMeet（MEE）的充提币业务。待CoinMeet官方升级完成，我们将第一时间恢复充提币业务，预计24-48小时内恢复，如提前恢复，我们……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1254,
                "title": "HADAX第二期第二轮投票上币结果公布及第三轮投票开启通知",
                "created": 1522554922000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期第二轮投票上币已于新加坡标准时间3月27日13:00结束，经过3个工作日的数据清洗和人工回访，最终胜出项目为BitUP（BUT）和18区（18T），我们……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1245,
                "title": "HADAX将于3月30日14:30上线消费链 (CDC)",
                "created": 1522391367000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）将定于新加坡时间3月30日14:30开放CDC充值业务。4月1日15:00在HADAX开放CDC/BTC和CDC/ETH交易。4月2日14:30开……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1243,
                "title": "火币矿池：全球首家数字货币开采与交易一体化的矿池平台上线",
                "created": 1522389625000,
                "source": "1",
                "content": "尊敬的用户： 火币致力于打造安全可信赖的比特币交易平台，以用户体验为核心，提供专业、极致的数字货币基础服务。为满足广大用户对于矿池业务的需求，将于2018年3月30日正式上线火币矿池。 火币矿池采用FPPS等……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1240,
                "title": "火币将于2018年3月30日正式进军韩国市场",
                "created": 1522375210000,
                "source": "1",
                "content": "尊敬的用户： 全球领先的数字资产交易平台火币将于2018年3月30日正式进军韩国市场。届时，将正式开放经过严格的交易所上线审核过程的99种数字资产及201个交易对的充值交易服务。感谢所有用户一直以来对火币的大……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1235,
                "title": "火币全球专业站关于ERC20暂停充币的公告",
                "created": 1522289822000,
                "source": "1",
                "content": "尊敬的用户： 因系统升级维护，当前所有ERC20币种现已暂停充币，预计将在6个小时内恢复正常。如提前完成维护，我们将会第一时间公告通知。维护期间为您带来的不便，敬请谅解！ 火币全球专业站 2018年3月29日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1232,
                "title": "火币全球专业站3月28日20:00全球首发Cortex (CTXC)",
                "created": 1522238255000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间3月28日20:00开放Cortex (CTXC)充值业务。3月29日16:00在创新区开放CTXC/BTC和CTXC/ETH交易。4月3日20:00开放CTXC 提……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1229,
                "title": "火币全球专业站关于3月27日系统升级的再次通知",
                "created": 1522137740000,
                "source": "1",
                "content": "尊敬的用户： 为了更好地提升我们的服务质量，火币全球专业站将于新加坡时间3月27日22:00-3月28日2:00期间进行系统升级，升级期间您将无法进行Huobi Pro和HADAX的币币交易和杠杆交易、无法进……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1222,
                "title": "HADAX第二期投票上币第二轮投票结果处理及未能胜出项目退票时间安排的公告",
                "created": 1522127756000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期投票上币第二轮投票于今天新加坡标准时间3月27日13:00结束，现对投票结果处理及本轮用户自主退票的安排如下： 本轮投票结果处理： 1、我们会在投票结束……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1219,
                "title": "火币全球专业站系统升级通知",
                "created": 1522062282000,
                "source": "1",
                "content": "尊敬的用户： 为了更好地提升我们的服务质量，火币全球专业站将于新加坡时间3月27日22:00-3月28日2:00期间进行系统升级，期间Huobi Pro和Huobi HADAX将停止交易，请您提前做好准备。系……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1217,
                "title": "火币全球专业站系统维护通知",
                "created": 1521955458000,
                "source": "1",
                "content": "尊敬的用户： 为了优化提高火币全球专业站的网络可访问性，火币全球专业站定于新加坡时间3月25日14:00-16:00期间进行系统维护，维护期间部分地区将会出现短时访问延时、访问不稳定等情况，请您提前做好准备。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1214,
                "title": "火币火伴全球招募第二期",
                "created": 1521544643000,
                "source": "1",
                "content": "火币火伴是火币官方的社群组织，享受HT激励和多种火币官方福利，汇聚热爱区块链和数字资产的火币用户，参与火币全球化，共享火币增值！ 火币的影响力从亚洲开始已快速渗透到了全球，从火币火伴上线招募至今： 共收到 3……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1211,
                "title": "火币全球专业站恢复XEM充值业务",
                "created": 1521534877000,
                "source": "1",
                "content": "尊敬的用户, 火币全球专业站现已恢复XEM的充值业务，暂停期间为您带来的不便，敬请谅解！ 火币全球专业站 2018年3月20日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1205,
                "title": "关于延长HADAX第二期第一轮投票上币未入选项目退票时间的通知",
                "created": 1521518872000,
                "source": "1",
                "content": "尊敬的用户： HADAX第二期第一轮投票上币未入选项目SEXC、REN、MUSK、PRA、PXC、CAF、IOTX、AE、HOT、GTC、LRC、FOTA、SHOW、DDD、FAIR、JNT、GTO、RFR、……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1200,
                "title": "HT持有者专享Zilla(ZLA)空投福利",
                "created": 1521451731000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间3月20日14:00对用户账户中持有的HT资产进行快照，对HT持有者空投480000个ZLA。 根据用户HT持有量占比可以瓜分480000个ZLA，快照结束后七个工作……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1196,
                "title": "HADAX第二期第一轮投票结果公布及第二轮投票开启通知",
                "created": 1521447190000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期第一轮投票上币已于新加坡标准时间3月15日13:00结束，经过3个工作日的数据清洗和人工回访，最终胜出项目为消费链(CDC)、DATx(DATX)和LI……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1190,
                "title": "关于HADAX和Pro的定位、HADAX到Pro的转板规则、HADAX和Pro的下线币种规则征求用户建议",
                "created": 1521183971000,
                "source": "1",
                "content": "尊敬的用户： HADAX是Pro的推出的服务于专业数字资产投资者及早期的创新型数字资产的全新子品牌火币自主数字资产交易所。Pro是审核制上币模式，HADAX是投票上币模式。以下是关于HADAX和Pro的定位、……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1183,
                "title": "HADAX第二期第一轮投票结果处理及下一轮投票注意事项说明",
                "created": 1521084906000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期第一轮投票上币将于今天新加坡标准时间3月15日13:00结束，由于本期投票规则较上一期变化较大，在投票结束前对本期规则以及下一轮投票可能的变化做如下说明……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1180,
                "title": "火币全球专业站3月14日11:00恢复ZEC提币业务",
                "created": 1520997264000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站已于新加坡时间3月14日11:00恢复ZEC提币业务，暂停期间造成的不便，敬请谅解。 火币全球专业站 2018年3月14日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1177,
                "title": "火币全球专业站3月13日14:00-3月14日14:00暂停ZEC提币业务",
                "created": 1520923587000,
                "source": "1",
                "content": "尊敬的用户： 因ZEC官方进行系统升级，火币全球专业站定于新加坡时间3月13日14:00到3月14日14:00期间暂停ZEC提币业务，充币业务不受影响，到账时间可能会延迟。对此造成的不便，敬请谅解。 ZEC官……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1174,
                "title": "火币全球专业站关于支持EOS主网映射的公告",
                "created": 1520856708000,
                "source": "1",
                "content": "尊敬的用户： 根据EOS官网消息，EOS测试网络已上线，并已经开始准备将EOS ERC20代币映射到主网络的测试工作。点击这里查看EOS官方关于测试网络和映射方案的公告：https://medium.com/……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1168,
                "title": "火币自主数字资产交易所（HADAX）第二期投票上币正式开启",
                "created": 1520831267000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（HADAX）第二期投票上币已经正式开启。 经历了一周的紧张筹备，我们正式于新加坡标准时间3月12日13:00正式开启第二期投票上币，在此感谢广大用户、项目方和超级节点的鼎……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1164,
                "title": "火币全球专业站已于3月9日23:00起恢复NEO、DBC、GAS、RPX充提业务",
                "created": 1520609064000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站已于新加坡时间3月9日23:00起恢复NEO、DBC、GAS、RPX的充提业务，其中ONT充值业务也同时恢复，提现业务将在3月14日14:00开放。暂停充提期间所有未到账的充值将会……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1160,
                "title": "火币全球专业站将于3月9日16:00起暂停NEO、DBC、GAS、ONT、RPX充提业务",
                "created": 1520581665000,
                "source": "1",
                "content": "尊敬的用户: 因NEO官方节点问题导致数据不同步，火币全球专业站将于新加坡时间3月9日16:00起暂停NEO、DBC、GAS、ONT、RPX的充提业务，预计24-48小时内恢复，如提前恢复，我们将以公告形式告……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1155,
                "title": "EDU交易排名赛 TOP30都有奖",
                "created": 1520573347000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间2018年3月9日14:00-3月15日14:00期间，累计EDU交易量（买入量+卖出量且不含自成交）TOP30名实名用户可获如下奖励： TOP1 200万EDU TOP2-3 100……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1152,
                "title": "火币全球专业站将于3月09日18:00上线TRX/USDT交易",
                "created": 1520568002000,
                "source": "1",
                "content": "尊敬的用户： 因 波场TRON (TRX)符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于3月9日18:00上线TRX/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年3月9日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1150,
                "title": "火币全球专业站将于3月8日21:00-3月9日3:00暂停ELA提币业务",
                "created": 1520507314000,
                "source": "1",
                "content": "因ELA官方将于新加坡时间3月8日22:00到3月9日2:00进行升级，所以火币全球专业站定于3月8日21:00到3月9日3:00暂停ELA提币业务。对此造成的不便，敬请谅解。 ELA官方公告地址： http……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1138,
                "title": "本体Ontology（ONT）充值开放时间延迟至18:00",
                "created": 1520496411000,
                "source": "1",
                "content": "尊敬的用户： 原定于新加坡时间3月8日14:00开放充值的Ontology（ONT），因临时调整，将延迟至3月8日18:00。对此造成的不便，敬请谅解。 火币全球专业站 2018年3月8日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1132,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于3月8日14:30上线UUU",
                "created": 1520490687000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）现已正式上线，并定于新加坡时间3月8日14:30开放U Network (UUU)充值业务。3月9日14:00在HADAX开放UUU/BTC和UU……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1130,
                "title": "超级火伴：火币全球区域合作火伴招募",
                "created": 1520489071000,
                "source": "1",
                "content": "什么是超级火伴？ 为拓展火币的全球业务落地，打造成为全球第一大数字资产交易平台，启动“火币全球区域合作火伴”招募计划，即：超级火伴。 超级火伴，是火币在国家、重点区域的当地业务的重要合作伙伴，是火币在关键地区……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1127,
                "title": "HADAX第一期投票上币退出项目公示",
                "created": 1520488265000,
                "source": "1",
                "content": "尊敬的用户： 自HADAX第二期投票规则（超级节点初审+保证金+用户投票）公布以来得到了众多项目方的积极反馈和支持，其中IPC、AIT、PC、IDC、True、BANCA、GCS、MDT、STB、ZIP和CD……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1124,
                "title": "火币全球专业站将于3月08日18:00上线MDS/USDT交易",
                "created": 1520481611000,
                "source": "1",
                "content": "尊敬的用户： 因 MediShares（MDS）符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于3月8日18:00上线MDS/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年3月……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1113,
                "title": "CNN交易排位赛 大奖20BTC等你拿",
                "created": 1520395086000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间3月7日15:00-3月14日15:00期间，累计CNN 交易量（买入量+卖出量且不含自成交）TOP10000名实名用户可获得如下奖励： TOP1 20BTC TOP2 1000000……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1111,
                "title": "HADAX第二期投票上币规则定稿",
                "created": 1520347462000,
                "source": "1",
                "content": "尊敬的用户： HADAX第二期投票规则终于在几天的忙碌和辩论中诞生，特别感谢给予我们帮助的项目方、用户和合作伙伴，感谢大家的理解和支持。HADAX投票上币是社区化业务运作的首次尝试，我们相信，每一次尝试，每一……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1105,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于3月6日14:30上线CNN, AAC",
                "created": 1520317868000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）现已正式上线，并定于新加坡时间3月6日14:30开放Content Neutrality Network (CNN)、锐角云(AAC)充值业务。3……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1102,
                "title": "关于HADAX投票上币第二期规则完善（第三版）征求意见",
                "created": 1520253176000,
                "source": "1",
                "content": "尊敬的用户： 基于收到的最新用户反馈，我们修改和完善了上一版的规则，再一次征求广大用户建议： 一、投票周期： 1、 第二期投票开始时间：新加坡标准时间2018-03-12 13:00； 2、 每轮投票周期调整……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1091,
                "title": "Huobi HADAX将于3月5日14:30上线 未来版权 (UIP)",
                "created": 1520231457000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）现已正式上线，并定于新加坡时间3月5日14:30开放未来版权 (UIP)充值业务。3月6日14:00在HADAX开放UIP/BTC和UIP/ETH……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1087,
                "title": "火币全球专业站将于3月05日18:00上线ELA/USDT交易",
                "created": 1520222410000,
                "source": "1",
                "content": "尊敬的用户： 因 亦来云（ELA）符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于3月5日18:00上线ELA/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年3月5日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1084,
                "title": "HADAX第二期投票上币延期至3月12日",
                "created": 1520175000000,
                "source": "1",
                "content": "尊敬的用户： HADAX自从推出第二期投票规则征求稿之后，收到了来自各方的建议，基于对用户和项目方都负责任的角度，我们将对第二期投票上币规则继续完善，近期我们会发出第三版征求意见稿，同时第二期投票规则中还需要……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1082,
                "title": "火币自主数字资产交易所（Huobi HADAX）将于3月4日14:30上线GSC、UC",
                "created": 1520145138000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所（Huobi HADAX）将定于新加坡时间3月4日14:30开放全球社交链(GSC)、YouLive (UC)充值业务。3月7日14:30开放GSC、UC提现业务。 3月5……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1074,
                "title": "关于HADAX投票上币第二期规则完善（第二版）征求意见",
                "created": 1519990963000,
                "source": "1",
                "content": "尊敬的用户： 基于收到的最新用户反馈，我们修改和完善了上一版的规则，再一次征求广大用户建议： 一、投票周期： 1、每轮投票周期调整为72小时，每轮投票选出得分最高的前三名项目。每轮投票间隔24小时，以做系统准……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1070,
                "title": "ONT交易排名赛 TOP100都有奖",
                "created": 1519970412000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间3月8日全球首发本体Ontology（ONT）。3月8日14:00开放充值业务。3月9日15:00在创新区开放ONT/BTC和ONT/ETH交易。3月14日14:00……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1066,
                "title": "火币全球专业站对2月26、27日交易用户空投308000ABT",
                "created": 1519903818000,
                "source": "1",
                "content": "尊敬的用户： 由于2月26日ArcBlock (ABT)交易过于火爆，导致2月26日-2月27日火币专业站访问量过大，行情出现短时无法加载情况，我们对此深表歉意。同时ArcBlock团队为了感谢火币交易用户对……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1062,
                "title": "关于HADAX投票上币第二期规则完善的征求意见",
                "created": 1519884310000,
                "source": "1",
                "content": "尊敬的用户： HADAX投票上币功能的推出初衷是火币全球专业站让交易所业务去中心化决策及社区自治方面的首次尝试，让上币过程变得公开透明，减少中间环节，我们期待能将区块链技术的理念真正植入到实际业务过程中。 同……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1060,
                "title": "火币全球专业站3月1日16:00-20:00期间暂停LTC充值提现业务",
                "created": 1519872407000,
                "source": "1",
                "content": "尊敬的用户, 因钱包系统升级，火币全球专业站将于新加坡时间3月1日16:00-20:00期间暂停莱特币LTC的充值、提现业务。请您提前做好准备，为您带来的不便敬请谅解！ 火币全球专业站 2018年3月1日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1056,
                "title": "HADAX第一期投票上币新增退出机制及第二期延迟的公告",
                "created": 1519813179000,
                "source": "1",
                "content": "尊敬的用户： HADAX投票上币是我们将交易所业务社区化运作的一个尝试，在这个过程中，我们征集了大量用户和项目方的反馈，感谢广大用户和项目方对HADAX的支持，我们也会竭尽全力为HADAX项目方和用户提供好服……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1052,
                "title": "Huobi HADAX第一期投票结果公示",
                "created": 1519792111000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站全新子品牌火币自主数字资产交易所HADAX第一期投票自2月12日上线以来，得到了众多项目方和用户的支持，感谢广大用户和项目方对HADAX的认可和支持，也感谢大家对HADAX提出的宝……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1049,
                "title": "关于法币交易区系统更新及大宗交易上线、发布广告调整及费率的公告",
                "created": 1519784460000,
                "source": "1",
                "content": "尊敬的用户： 法币交易区将于2018年3月1日上午6时进行升级维护，预计更新时间2小时，请您提前做好资产安排，以免因行情波动造成损失。 本次系统升级后，将更新以下内容： 一、大宗交易正式上线 大宗交易上线后，……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1047,
                "title": "火币全球专业站支持ONT空投",
                "created": 1519733456000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将支持本体Ontology（ONT）团队的NEO空投计划，于NEO区块高度1,974,823进行快照（预计新加坡时间2018年3月1日21:00，具体时间以实际出块时间为准），空投……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1045,
                "title": "关于火币全球专业站系统维护的公告",
                "created": 1519646261000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站正在进行系统维护，维护预计30分钟，维护期间，开通谷歌验证的用户无法登录，无法添加或修改谷歌验证，为您带来的不便敬请谅解！ 火币全球专业站 2018年2月26日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1042,
                "title": "ArcBlock (ABT)首发火币送礼啦！50000 ABT先到先得",
                "created": 1519609861000,
                "source": "1",
                "content": "尊敬的用户： 新加坡时间2月26日10:00-2月27日10:00，ABT累计交易量（买入量+卖出量且不含自成交）不低于100ABT的实名用户即可获得10ABT。届时将根据交易时间顺序发放奖励，50000AB……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1037,
                "title": "火币全球专业站全球首发区块基石ArcBlock (ABT)，并将于2月25日11:00开放充值业务",
                "created": 1519354107000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月25日11:00开放区块基石ArcBlock (ABT)充值业务。2月26日10:00在创新区开放ABT/BTC和ABT/ETH交易。2月27日11:00开放ABT……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1036,
                "title": "Huobi HADAX第一期投票规则补充和第二期投票规则更新的公告",
                "created": 1519307394000,
                "source": "1",
                "content": "尊敬的用户： 火币自主数字资产交易所HADAX第一期投票自2月12日上线以来，得到了数百项目方和数万用户的支持，截止2月20日16点，75个项目得到了来自近10万用户近‪4000万‬张投票，感谢广大用户和项目……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1034,
                "title": "火币全球专业站2月22日14:00上线 Bluzelle (BLZ)",
                "created": 1519279204000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月22日14:00开放Bluzelle (BLZ)充值业务。2月23日18:00在创新区开放BLZ/BTC和BLZ/ETH交易。2月24日14:00开放BLZ提现业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1032,
                "title": "火币全球专业站将于2月22日18:00上线ITC/USDT交易",
                "created": 1519272006000,
                "source": "1",
                "content": "尊敬的用户： 因 万物链 (ITC) 符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于2月22日18:00上线ITC/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年2月22日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1030,
                "title": "火币全球专业站2月22日11:00全球首发EduCoin  (EDU)",
                "created": 1519268405000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月22日11:00开放EduCoin (EDU) 充值业务。2月23日15:00在创新区开放EDU/BTC和EDU/ETH交易。2月24日15:00开放EDU 提现业……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1027,
                "title": "火币全球专业站XEM暂停充币，提币不受影响",
                "created": 1519113531000,
                "source": "1",
                "content": "尊敬的用户, 由于 NEM.io Foundation Ltd 社区相关事宜影响, 为保护用户资产，我们即刻起暂停XEM的充值，提币不受影响，待NEM官方处理完后恢复充币。同时XEM的提币不受影响。若有新进展……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1026,
                "title": "欢庆中国年 · 我的火币赞",
                "created": 1518746272000,
                "source": "1",
                "content": "新年到，福运到！ 火币同火伴们一起共贺新春，“欢庆中国年”系列活动持续进行。微信朋友圈集赞大比拼，1,000HT免费拿。 活动时间： 新加坡时间（UTC+8）2月16日16:00-2月20日24:00 活动规……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1025,
                "title": "6,666HT头彩，欢庆中国年，除夕夜交易HT送HT",
                "created": 1518571959000,
                "source": "1",
                "content": "尊敬的火币全球专业站用户： 为了与全球火伴一起共庆中国年，在2018年春节来临之际，火币全球专业站特推出“欢庆中国年，交易HT送HT”活动，用户可在活动期间完成活动要求获取抽奖资格。 活动时间：新加坡时间（U……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1020,
                "title": "火币全球专业站关于购手续费点卡套餐送HT活动结束的公告",
                "created": 1518532448000,
                "source": "1",
                "content": "尊敬的用户： 自1月24日火币全球专业站开启抢购手续费点卡套餐送火币全球通用积分HT（Huobi Token）以来，市场反馈持续热烈，截止目前，我们已全部送出3亿HT。 HT发行总量限定5亿，100%用于赠送……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1018,
                "title": "Huobi HADAX第一期投票项目列表和规则更新的公告",
                "created": 1518509159000,
                "source": "1",
                "content": "尊敬的用户： 1、项目更新： 由于第一期投票项目方报名十分火爆，评审时间十分紧张，所以部分项目在信息搜集和理解上有些遗漏和偏差。经过与项目方的再次沟通，本着对每个项目都负责任的原则，我们紧急组织了二次审核，现……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1016,
                "title": "火币全球专业站2月12日14:00上线 Enigma(ENG)",
                "created": 1518415195000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月12日14:00开放Enigma(ENG)充值业务。2月13日18:00在创新区开放ENG/BTC和ENG/ETH交易。2月14日14:00开放ENG提现业务。 点……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1014,
                "title": "火币全球专业站将于2月12日18:00上线NAS/USDT交易",
                "created": 1518407981000,
                "source": "1",
                "content": "尊敬的用户： 因星云币（NAS）符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于2月12日18:00上线NAS/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年2月12日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1012,
                "title": "Huobi HADAX（海达克斯）第一期投票上币正式开启",
                "created": 1518404382000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站全新子品牌火币自主数字资产交易所——Huobi HADAX（海达克斯）将于2月12日起正式开启第一期投票上币，第一期有60个项目参与投票，我们将根据投票结果选择10个项目作为首批上……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1010,
                "title": "火币自主数字资产交易所HADAX投票开启时间更新至2月12日",
                "created": 1518190976000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站全新子品牌火币自主数字交易所HADAX因项目方报名情况火爆，HADAX需要较多时间进行项目真实性和合法性的审核，因此HADAX将延迟第一期投票至2月12日，具体安排请您关注后续公告……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1008,
                "title": "火币全球专业站将于2月9日18:00上线RUFF/USDT交易",
                "created": 1518148691000,
                "source": "1",
                "content": "尊敬的用户： 因Ruff Chain(RUFF)符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于2月9日18:00上线RUFF/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年2……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1006,
                "title": "火币全球专业站将于2月8日16:00恢复NEM(XEM) 充值",
                "created": 1518076849000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡时间2月8日16:00起恢复NEM(XEM)充值业务，暂停充值期间所有未到账的充值将会自动上账。 火币全球专业站 2018年2月8日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1004,
                "title": "火币全球专业站2月8日14:30全球首发 WePower Network (WPR)",
                "created": 1518071370000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月8日14:30开放WePower Network (WPR)充值业务。2月9日14:00在创新区开放WPR/BTC和WPR/ETH交易。2月10日14:00开放WP……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 1002,
                "title": "火币全球专业站将于2月8日18:00上线ZIL/USDT交易",
                "created": 1518062386000,
                "source": "1",
                "content": "尊敬的用户： 因Zilliqa(ZIL) 符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于2月8日18:00上线ZIL/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年2月8日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 999,
                "title": "火币全球专业站将于2月8日0:00-2:00期间进行系统维护",
                "created": 1517987634000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于新加坡时间2月8日0:00-2:00期间进行系统维护，在此期间您可正常登录及交易，仅无法使用新用户注册、修改密码、账号安全相关安全策略变更、身份认证、API管理等功能，请您提前……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 997,
                "title": "火币全球专业站将于2月7日10点开启点卡套餐全民狂欢活动",
                "created": 1517922294000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于新加坡标准时间2月7日10点开启全民狂欢，届时所有用户均可抢购点卡套餐。其中今日点卡套餐将于24:00下线，剩余额度将会计入第二天全民狂欢的点卡套餐额度中。 新加坡标准时间2月……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 995,
                "title": "火币全球专业站2月6日16:10全球首发Matryx (MTX)",
                "created": 1517904722000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月6日16:10开放Matryx (MTX)充值业务。2月7日15:00在创新区开放MTX/BTC和MTX/ETH交易。2月9日14:00开放MTX 提现业务。 点此……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 993,
                "title": "火币全球专业站2月6日10点老用户专场活动预告",
                "created": 1517821304000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于2月2日-2月6日开放老用户回馈专场活动，并将在2月7日开启全民狂欢，所有新老用户均可抢购套餐。其中2月5日赠送额度25秒内发送完毕，共赠送HT 1512万枚。 新加坡标准时间……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 991,
                "title": "火币全球专业站关于设立平台安全备付金的公告",
                "created": 1517819024000,
                "source": "1",
                "content": "尊敬的用户： 2018年1月火币推出投资者保护基金（平台20%收入用于回购HT计提进入投资者保护基金），获得了很多用户的支持和响应。今天，火币全球专业站正式推出另一项用户资金保护机制——“安全备付金机制”，给……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 989,
                "title": "火币全球专业站2月5日~2月7日连续3天空投新币给HT持有者",
                "created": 1517760575000,
                "source": "1",
                "content": "尊敬的用户： 为了感谢HT持有者对火币贡献，火币全球专业站将于北京时间2月5日~2月7日每天10:30对用户账户中的持有的HT资产进行快照，每天对HT持有者空投价值人民币500万的新币。 包括但不限于 NAS……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 987,
                "title": "火币全球专业站2月5日10点老用户专场活动预告",
                "created": 1517753725000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于2月2日-2月6日开放老用户回馈专场活动，并将在2月7日开启全民狂欢，所有新老用户均可抢购套餐。其中2月4日赠送额度10秒内发送完毕，共赠送HT 1209.6万枚。 新加坡标准……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 985,
                "title": "火币全球专业站2月4日11:00全球首发Medicalchain(MTN)",
                "created": 1517713205000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月4日11:00开放Medicalchain(MTN)充值业务。2月5日11:00在创新区开放MTN/BTC和MTN/ETH交易。2月7日11:00开放MTN 提现业……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 983,
                "title": "火币全球专业站设立火币自主数字资产交易所HADAX并开启投票上币功能",
                "created": 1517672035000,
                "source": "1",
                "content": "尊敬的用户： 当前全球数字资产市场规模日益扩张，创新型数字资产的种类和规模都日新月异。火币全球专业站现有的中心化的审核上币运营模式，保持着对数字资产的严格评审，虽然能在一定程度上帮助用户甄选优质资产，降低用户……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 982,
                "title": "火币全球专业站2月4日10点老用户专场活动预告",
                "created": 1517646762000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于2月2日-2月6日开放老用户回馈专场活动，并将在2月7日开启全民狂欢，所有新老用户均可抢购套餐。其中2月3日赠送额度11秒内发送完毕，共赠送HT 907.2万枚。 新加坡标准时……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 979,
                "title": "火币全球专业站将于2月3日18:00上线DTA/USDT交易",
                "created": 1517630412000,
                "source": "1",
                "content": "尊敬的用户： 因DATA (DTA) 符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于2月3日18:00上线DTA/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年2月3日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 977,
                "title": "火币全球专业站2月3日10点老用户专场活动预告",
                "created": 1517567922000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将在2月2日-2月6日开放老用户回馈专场活动，并将在2月7日开启全民狂欢，所有新老用户均可抢购套餐。其中2月2日赠送额度44秒内发送完毕，共赠送HT 600万枚。 新加坡标准时间2……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 975,
                "title": "火币全球专业站2月2日16:00上线 SunContract (SNC)",
                "created": 1517558388000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月2日16:00开放SunContract (SNC)充值业务。2月3日16:00在创新区开放SNC/BTC和SNC/ETH交易。2月6日16:00开放SNC提现业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 973,
                "title": "火币全球专业站2月2日14:30上线LISK(LSK)",
                "created": 1517553391000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2月2日14:30开放LISK(LSK)充值业务。2月3日15:00在创新区开放LSK/BTC和LSK/ETH交易。2月6日14:30开放LSK提现业务。 点此查看LS……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 971,
                "title": "火币全球专业站将于2月2日18:00上线LET/USDT交易",
                "created": 1517544015000,
                "source": "1",
                "content": "尊敬的用户： 因LinkEye (LET) 符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于2月2日18:00上线LET/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年2月2日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 969,
                "title": "火币全球专业站将于2月2日10点开启老用户回馈专场活动",
                "created": 1517507262000,
                "source": "1",
                "content": "尊敬的用户： 火币全球通用积分（HT）上线以来，市场反馈越来越热烈，其中2月1日赠送额度14秒内发送完毕，共赠送HT 1070.5万枚。 自2013年9月成立以来，火币的每一步发展和成长都离不开一路相伴的用户……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 967,
                "title": "火币全球专业站将于2月10日12:00恢复WAX充值",
                "created": 1517493033000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站与项目方进行了积极的沟通，一直进行着对WAX持有者的相关补偿措施，我们已于1月31日前完成所有赔付，并定于北京时间2月10日12:00起恢复WAX充值业务。 火币全球专业站 201……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 965,
                "title": "火币全球专业站将于2月1日10点继续HT抢购，并于14点开放HT交易",
                "created": 1517399958000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于2月1日10点继续HT抢购，并于14点在创新区开放HT/USDT、HT/BTC 和HT/ETH交易，同时开放HT充值和提现。 自1月24日火币全球通用积分（HT）上线以来，市场……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 963,
                "title": "【首发豪送1500000STK】火币全球专业站1月31日全球首发STK Token(STK)",
                "created": 1517383568000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月31日22:00开放STK Token(STK)充值业务。2月1日16:00在创新区开放STK /BTC和STK /ETH交易。2月6日15:00开放STK Tok……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 961,
                "title": "火币全球专业站将于1月31日18:00上线THETA/USDT交易",
                "created": 1517370841000,
                "source": "1",
                "content": "尊敬的用户： 因THETA符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于1月31日18:00上线THETA/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月31日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 959,
                "title": "火币全球专业站明日点卡套餐详情预告，1月31日10点正式开抢！",
                "created": 1517314327000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站1月24日火币全球通用积分（HT）官方上线，并于1月24日-2月7日每日10点开始赠送，近几日市场反馈越来越热烈。其中1月30日赠送额度19秒内发送完毕，共赠送HT 1510万枚。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 956,
                "title": "【Sirin Labs(SRN)百万大奖赛】火币全球专业站1月30日15:10上线SRN",
                "created": 1517294429000,
                "source": "1",
                "content": "尊敬的用户， 火币全球专业站定于北京时间1月30日15:10开放Sirin Labs(SRN)充值业务。1月31日16:00在创新区开放SRN/BTC和SRN/ETH交易。2月1日15:10开放Sirin L……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 953,
                "title": "【ZLA交易送百万】火币全球专业站1月30日14:30全球首发Zilla (ZLA)",
                "created": 1517293887000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月30日14:30开放Zilla (ZLA)充值业务。1月31日15:00在创新区开放ZLA/BTC和ZLA/ETH交易。2月2日14:30开放Zilla (ZLA)……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 951,
                "title": "【亦来云首发三重惊喜】火币全球专业站1月30日12:00全球首发亦来云（ELA）",
                "created": 1517284870000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月30日12:00开放亦来云 (ELA)充值业务。2月1日10:30在创新区开放ELA/BTC和ELA/ETH交易。2月5日12:00开放ELA提现业务。 惊喜一：【……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 949,
                "title": "火币全球专业站明日点卡套餐详情预告，1月30日10点正式开抢！",
                "created": 1517231788000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站1月24日火币全球通用积分（HT）官方上线，并于1月24日-2月7日每日10点开始赠送，近几日市场反馈越来越热烈。其中1月29日赠送额度28秒内发送完毕，共赠送HT 2454万枚。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 946,
                "title": "火币全球专业站1月29日17:30全球首发Odyssey (OCN)",
                "created": 1517217741000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月29日17:30开放Odyssey (OCN)充值业务。1月30日17:00在创新区开放OCN/BTC和OCN/ETH交易。1月31日17:30开放OCN 提现业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 945,
                "title": "火币全球专业站HT老用户回馈专场活动",
                "created": 1517217533000,
                "source": "1",
                "content": "尊敬的用户： 火币自2013年成立以来，已近5年，我们深知过往每一步的成绩和发展都离不开老用户的关心和支持，可以说，没有几百万火币老用户，就没有今天的火币。在火币过去不同的发展阶段，都是靠着老用户的支持才能一……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 943,
                "title": "【LUN百万红包拜早年】火币全球专业站1月29日16:00上线Lunyr (LUN)",
                "created": 1517212895000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月29日16:00开放Lunyr (LUN)充值业务。1月30日15:00在创新区开放LUN/BTC和LUN/ETH交易。1月31日16:00开放Lunyr (LUN……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 941,
                "title": "火币全球专业站1月29日15:30上线 Tron (TRX)",
                "created": 1517210865000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月29日15:30开放Tron (TRX)充值业务。1月30日19:30在创新区开放TRX/BTC和TRX/ETH交易。1月31日15:30开放TRX提现业务。 点此……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 939,
                "title": "火币全球专业站明日点卡套餐详情预告，1月29日10点正式开抢！",
                "created": 1517136078000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站1月24日火币全球通用积分（HT）官方上线，并于1月24日-2月7日每日10点开始赠送，近几日市场反馈越来越热烈。其中1月28日赠送额度22秒内发送完毕，共赠送HT 2542万枚。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 937,
                "title": "火币全球专业站XEM暂停充币，提币不受影响",
                "created": 1517132736000,
                "source": "1",
                "content": "亲爱的用户， 由于 NEM.io Foundation Ltd 官方发出公告，对日本交易平台 Coincheck丢失的XEM进行追踪和标记。在处理完成之前，NEM的区块链网络会受到影响。为保护用户资产，我们即……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 935,
                "title": "RUFF豪送250万 交易多少送多少",
                "created": 1517122801000,
                "source": "1",
                "content": "尊敬的用户： 【RUFF豪送250万 交易多少送多少】 北京时间2018年1月28日15:00-2月3日15:00期间，凡交易RUFF的实名用户，活动期间累计RUFF交易量（买入量+卖出量且不含自成交）均可获……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 934,
                "title": "火币全球专业站法币交易区手续费优惠及广告发布的说明",
                "created": 1517043851000,
                "source": "1",
                "content": "尊敬的用户： 为了答谢大家对法币交易区业务的支持，继本月免除交易手续费结束后，法币交易区现有业务将继续免除交易手续费，免除时间：2018年2月1日 - 2月28日（如有新增业务，收费标准另行通知）。 广告发布……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 932,
                "title": "火币全球专业站明日点卡套餐详情预告，1月28日10点正式开抢！",
                "created": 1517037653000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站1月24日火币全球通用积分（HT）官方上线，并于1月24日-2月7日每日10点开始赠送，近几日市场反馈越来越热烈。其中1月27日赠送额度28秒内发送完毕，共赠送HT 2735万枚。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 928,
                "title": "火币全球专业站明日点卡套餐详情预告，1月27日10点正式开抢！",
                "created": 1516969196000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站1月24日火币全球通用积分（HT）官方上线，并于1月24日-2月7日每日10点开始赠送，近几日市场反馈越来越热烈。其中1月26日赠送额度32秒内发送完毕，共赠送HT 2856万枚。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 926,
                "title": "火币全球专业站将于1月26日19:00开放BTG的充值",
                "created": 1516964510000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将定于1月26日19:00开放BTG的充值。 感谢您的理解与支持！ 火币全球专业站 2018年1月26日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 921,
                "title": "火币全球专业站开通BTC交易区杠杆交易",
                "created": 1516953837000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站现已支持BTC/USDT杠杆交易借贷BTC。 同时开放BTC交易区的杠杆交易，做多做空均可。支持币种如下： ETH、BCH、XRP、LTC、DASH、EOS、ETC、OMG、ZEC……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 918,
                "title": "火币全球专业站1月26日14:30全球首发Ruff (RUFF)",
                "created": 1516948430000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月26日14:30开放Ruff (RUFF)充值业务。1月28日15:00在创新区开放RUFF/BTC和RUFF/ETH交易。1月30日14:30开放RUFF提现业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 916,
                "title": "火币全球专业站将于1月26日18:00上线XEM/USDT交易",
                "created": 1516939140000,
                "source": "1",
                "content": "尊敬的用户： 因XEM符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于1月26日18:00上线XEM/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月26日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 914,
                "title": "火币全球专业站明日点卡套餐详情预告，1月26日10点正式开抢！",
                "created": 1516879356000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站1月24日火币全球通用积分（HT）官方上线，并于1月24日-2月7日每日10点开始赠送，近两日市场反馈越来越热烈。其中1月25日赠送额度1分40秒内发送完毕，共赠送HT 2999万……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 912,
                "title": "火币全球专业站将于1月25日19:00开放RPX、DBC提现业务",
                "created": 1516877996000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将定于1月25日19:00开放RPX、DBC提现业务。 感谢您的理解与支持！ 火币全球专业站 2018年1月25日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 910,
                "title": "火币全球专业站1月25日16:00全球首发SOC",
                "created": 1516867258000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月25日16:00开放SOC充值业务。1月26日13:00在创新区开放SOC/BTC和SOC/ETH交易。1月28日16:00开放SOC提现业务。 风险提示： 数字资……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 908,
                "title": "DTA交易排名赛 TOP10000都有奖",
                "created": 1516863502000,
                "source": "1",
                "content": "尊敬的用户： 点此查看DTA币种资料：https://www.huobipro.com/zh-cn/assetintro/#dta 【DTA交易排名赛 TOP10000都有奖】 北京时间1月25日15:00-……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 906,
                "title": "火币全球专业站1月25日14:30全球首发Zilliqa (ZIL)",
                "created": 1516861807000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月25日14:30开放Zilliqa (ZIL) 充值业务。1月26日15:00在创新区开放ZIL/BTC和ZIL/ETH交易。1月31日14:30开放Zilliqa……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 904,
                "title": "火币全球专业站将于1月25日18:00上线ELF/USDT交易",
                "created": 1516853017000,
                "source": "1",
                "content": "尊敬的用户： 因ELF符合了火币专业站USDT交易区的上线标准，因此火币专业站将于1月25日18:00上线ELF/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月25日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 902,
                "title": "火币全球专业站明日点卡套餐详情预告，新加坡标准时间1月25日上午10点正式开抢！",
                "created": 1516787108000,
                "source": "1",
                "content": "2018年1月24日火币全球通用积分（HT）在火币全球专业站官方上线，已于今日上午10点整正式开始赠送，由于市场反馈非常热烈，火币点卡销售形成了抢购的局面，今天赠送的额度在2分26秒内发送完毕，共赠送HT31……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 900,
                "title": "火币全球专业站将于1月24日18:00上线SMT/USDT交易",
                "created": 1516766370000,
                "source": "1",
                "content": "尊敬的用户： 因SMT符合了火币全球专业站USDT交易区的上线标准，因此火币全球专业站将于1月24日18:00上线SMT/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月24日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 898,
                "title": "火币全球通用积分（HT）官方上线，1月24日10点准时开抢！",
                "created": 1516730808000,
                "source": "1",
                "content": "火币全球专业站将于1月24日10:00发布点卡套餐并赠送火币全球通用积分（HT），HT发行总量限定5亿，本次购买点卡套餐赠送3亿HT。 1月24日-2月7日期间，每日10:00开始抢购，届时将可以通过购买点卡……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 896,
                "title": "火币全球专业站1月23日14:30上线CoinMeet (MEE)",
                "created": 1516689011000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月23日14:30开放CoinMeet (MEE)充值业务。1月24日15:00在创新区开放MEE/BTC和MEE/ETH交易。1月29日14:30开放CoinMee……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 894,
                "title": "火币全球专业站将于1月23日18:00上线IOST/USDT交易",
                "created": 1516680031000,
                "source": "1",
                "content": "尊敬的用户： 因IOST符合了火币专业站USDT交易区的上线标准，因此火币专业站将于1月23日18:00上线IOST/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月23日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 890,
                "title": "火币全球专业站将于1月24日10:00发布点卡套餐并赠送火币全球通用积分（HT）",
                "created": 1516628909000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将定于北京时间1月24日发布火币全球通用积分（HT）。1月24日-2月7日期间，每日10:00开始抢购，届时将可以通过购买点卡套餐获赠火币全球通用积分（HT）。 同时，将在2月1日……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 887,
                "title": "火币全球专业站将于1月22日14:30开放NEM（XEM）提现业务",
                "created": 1516602687000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于1月22日14:30开放NEM（XEM）提现业务，但目前Nem（XEM）提币到Poloniex、Bittrex可能无法到账，请不要尝试提现至该交易所。 感谢您的理解与支持！ 火……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 885,
                "title": "火币全球专业站1月22日14:00上线EchoLink(EKO)",
                "created": 1516601041000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月22日14:00开放EchoLink(EKO)充值业务。1月23日15:00在创新区开放EKO/BTC和EKO/ETH交易。1月26日14:00开放EchoLink……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 883,
                "title": "火币全球专业站将于1月22日18:00上线VEN/USDT交易",
                "created": 1516593560000,
                "source": "1",
                "content": "尊敬的用户： 因VEN符合了火币专业站USDT交易区的上线标准，因此火币专业站将于1月22日18:00上线VEN/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月22日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 881,
                "title": "火币全球专业站1月19日14:30上线ChainLink(LINK)",
                "created": 1516343331000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月19日14:30开放ChainLink(LINK)充值业务。1月21日14:00在创新区开放LINK/BTC和LINK/ETH交易。1月22日14:30开放Chai……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 879,
                "title": "火币全球专业站1月18日14:30上线EVX、ADX",
                "created": 1516257040000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月18日上线EVX、ADX。充值业务已于1月18日14:30开放。 1月19日14:00在创新区开放EVX/BTC和EVX/ETH交易。 1月19日15:00在创新区……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 878,
                "title": "火币官方唯一社群入口：telegram",
                "created": 1516246920000,
                "source": "1",
                "content": "Telegram因安全私密，且群聊人数无上限，和快速成为币圈首选。所有国内外的项目都可以在Telegram上面轻松找到官方项目方的运营发声群，让币圈讨论无国界，更加私密匿名便利。 1月16日起，火币pro的T……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 876,
                "title": "火币全球专业站1月17日14:30全球首发DTA，同时上线UTK",
                "created": 1516171157000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月17日全球首发DATA(DTA)，并同时上线UTRUST(UTK)。充值业务已于1月17日14:30开放。 1月18日14:00在创新区开放DTA/BTC和DTA/……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 874,
                "title": "【LET首发豪送200万】火币全球专业站1月16日19:00全球首发LinkEye(LET)",
                "created": 1516100391000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月16日19:00开放LET充值业务。1月17日14:00在创新区开放LET/BTC和LET/ETH交易。1月22日19:00开放LET提现业务。 【LET首发豪送2……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 872,
                "title": "火币全球专业站1月16日12:00全球首发Theta(THETA)",
                "created": 1516075217000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月16日12:00开放Theta(THETA)充值业务。1月17日12:00在创新区开放THETA/BTC和THETA/ETH交易。1月22日12:00开放THETA……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 870,
                "title": "火币全球专业站1月15日14:30上线NEM(XEM)",
                "created": 1515997821000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月15日14:30开放NEM(XEM)充值业务。1月16日14:00在创新区开放XEM/BTC交易。 【答题送XEM】 1月15日14:30-1月18日14:30期间……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 868,
                "title": "【交易瓜分18888APPC】火币全球专业站1月14日14:30上线AppCoins (APPC）",
                "created": 1515911411000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月14日14:30开放AppCoins (APPC）充值业务。1月15日15:00在创新区开放APPC/BTC和APPC/ETH交易。1月17日14:30开放AppC……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 867,
                "title": "【立即下载】火币Pro桌面客户端 更安全、更轻快、更专业",
                "created": 1515823975000,
                "source": "火币全球专业站",
                "content": "火币Pro桌面客户端 更安全、更轻快、更专业 MAC版下载： https://huobi-1252264550.file.myqcloud.com/bit/ops/app/mac/111/huobi-0.dm……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 865,
                "title": "火币全球专业站1月12日20:30全球首发YEE",
                "created": 1515760188000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月12日20:30开放YEE充值业务。1月14日15:00在创新区开放YEE/BTC和YEE/ETH交易。1月18日20:30开放YEE提现业务。 点此查看YEE币种……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 863,
                "title": "火币全球专业站1月12日16:00上线BeeChat(CHAT)",
                "created": 1515744085000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月12日16:00开放BeeChat(CHAT)充值业务。1月14日14:00在创新区开放CHAT/BTC和CHAT/ETH交易。1月15日16:00开放BeeCha……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 861,
                "title": "火币全球专业站1月12日15:00上线Datum (DAT)",
                "created": 1515740460000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月12日15:00开放Datum (DAT)充值业务，1月12日19:00在创新区开放DAT/BTC和DAT/ETH交易，1月15日15:00开放提现业务。 点此查看……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 859,
                "title": "【IOST首发豪礼人人有】火币全球专业站1月12日14:30全球首发IOST",
                "created": 1515738568000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月12日14:30开放IOST充值业务。1月15日14:00在创新区开放IOST/BTC和IOST/ETH交易。1月18日14:30开放IOST提现业务。 点此查看I……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 855,
                "title": "火币全球专业站1月12日15:00上线DBC/ETH交易",
                "created": 1515656167000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月12日15:00上线DBC/ETH交易。 祝您交易愉快！ 火币全球专业站 2018月1月11日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 853,
                "title": "火币全球专业站将于1月11日18:00上线CVC/USDT交易",
                "created": 1515643196000,
                "source": "1",
                "content": "尊敬的用户： 因CVC 符合了火币专业站USDT交易区的上线标准，因此火币专业站将于1月11日18:00上线CVC/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月11日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 852,
                "title": "火币Pro关于WAX项目补偿的二次通知",
                "created": 1515638697000,
                "source": "1",
                "content": "尊敬的用户： 火币Pro关于WAX项目的补偿工作正在持续进行中，本次补偿以BTC进行支付。 为了方便用户提交补偿申请，我们提供了在线表格和电子邮件两种方式。 还没有申请补偿的用户，您可以点击链接填写表格：ht……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 850,
                "title": "火币全球专业站1月10日14:30全球首发QUN、AIDOC，同时上线OST",
                "created": 1515565790000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月10日全球首发QunQun(QUN)、天医(AIDOC)，并同时上线Simple Token (OST)。QunQun(QUN)、天医(AIDOC)、Simple ……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 848,
                "title": "火币全球专业站1月9日18:30全球首发拓扑链（TOPC）",
                "created": 1515493826000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月9日18:30开放拓扑链 (TOPC)充值业务。1月10日16:00在创新区开放TOPC/BTC和TOPC/ETH交易。1月15日18:30开放拓扑链（TOPC）提……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 846,
                "title": "火币全球专业站1月9日18:30上线Achain(ACT)",
                "created": 1515493740000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月9日18:30开放Achain(ACT)充值业务。1月10日15:00在创新区开放ACT/BTC和ACT/ETH交易。1月11日18:30开放Achain(ACT)……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 844,
                "title": "火币全球专业站1月9日14:30上线DeepBrainChain(DBC)",
                "created": 1515479266000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月9日14:30开放DeepBrainChain(DBC)充值业务。1月10日14:00在创新区开放DBC/BTC交易。DeepBrainChain(DBC)提现业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 842,
                "title": "火币全球专业站将于1月9日18:00上线STORJ/USDT交易",
                "created": 1515470402000,
                "source": "1",
                "content": "尊敬的用户： 因STORJ符合了火币专业站USDT交易区的上线标准，因此火币专业站将于1月9日18:00上线STORJ/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月9日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 840,
                "title": "【100000个RPX送不停】火币全球专业站1月8日14:30上线Red Pulse (RPX)",
                "created": 1515392958000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月8日14:30开放RPX充值业务。1月9日14:00在创新区开放RPX/BTC交易。RPX提现业务开放时间另行通知。 【100000个RPX送不停】 北京时间1月9……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 837,
                "title": "火币新年买卖ELF送币活动1月7日名单公示",
                "created": 1515340756000,
                "source": "1",
                "content": "亲爱的火币用户： 今天的ELF秒杀活动已经结束，随着活动的推进，每天活动参与人数与日俱增。ELF秒杀活动火爆情形给本次元旦秒杀送币活动画上了圆满的句号。火币新年活动项目组在此宣布，2018年元旦七天抢币活动也……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 836,
                "title": "火币新年买卖PROPY送币活动1月6日名单公示",
                "created": 1515252326000,
                "source": "1",
                "content": "亲爱的火币用户： 今天的PROPY秒杀活动已经结束，本次元旦七天抢币活动已进入到尾声阶段，感谢大家对火币的支持。今日PROPY的获奖名单已于火币官方微博@火币网 全部公示，本公告的底部也将对获奖名单进行公示。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 834,
                "title": "火币全球专业站1月6日14:30上线Power Ledger (POWR)",
                "created": 1515220190000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月6日14:30开放Power Ledger (POWR)充值业务。1月7日14:00在创新区开放POWR/BTC和POWR/ETH交易。1月8日14:30开放Pow……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 833,
                "title": "火币新年交易送币活动奖励机制公示",
                "created": 1515205427000,
                "source": "1",
                "content": "亲爱的火币用户： 昨天的SMT秒杀活动已经结束，感谢大家对火币的支持。SMT的获奖名单已于火币官方微博@火币网 官网微信进行公示，本公告的底部也会对昨天SMT的获奖名单进行公示。 近期有用户反馈对本次火币元旦……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 831,
                "title": "火币全球专业站1月6日10:00上线Request Network (REQ)",
                "created": 1515203998000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月6日10:00开放Request Network (REQ) 充值业务。1月6日18:00在创新区开放REQ/BTC和REQ/ETH交易。1月8日10:00开放Re……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 829,
                "title": "火币全球专业站1月5日16:30上线维基链(WICC)",
                "created": 1515141027000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月5日16:30开放维基链(WICC)充值业务。1月5日21:00在创新区开放WICC/BTC和WICC/ETH交易。1月9日16:30开放维基链(WICC)提现业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 827,
                "title": "火币全球专业站将于1月5日16:00开放NEO/USDT杠杆交易",
                "created": 1515134060000,
                "source": "1",
                "content": "尊敬的用户： 火币专业站将于1月5日16:00开放NEO/USDT杠杆交易。 祝您交易愉快！ 火币全球专业站 2018年1月5日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 825,
                "title": "【SWFTC交易排名赛】火币全球专业站1月5日14:30上线SwftCoin(SWFTC)",
                "created": 1515133730000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月5日14:30开放SwftCoin(SWFTC)充值业务，1月8日14:00在创新区开放SWFTC/BTC和SWFTC/ETH交易，1月9日14:00开放提现业务。……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 823,
                "title": "火币全球专业站将于1月5日18:00上线SNT/USDT交易",
                "created": 1515124788000,
                "source": "1",
                "content": "尊敬的用户： 因SNT符合了火币专业站USDT交易区的上线标准，因此火币专业站将于1月5日18:00上线SNT/USDT交易。 祝您交易愉快！ 火币全球专业站 2018年1月5日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 822,
                "title": "火币新年买卖MDS送币活动1月4日名单公示",
                "created": 1515078655000,
                "source": "1",
                "content": "亲爱的火币用户： 今天的MDS秒杀活动已经结束，感谢大家对火币的支持。MDS的获奖名单已于火币官网微博@火币网全部公示。目前火币网官方微博已公示1月4日MDS全天秒杀奖励名单。MDS的奖励我们将在详细审核确认……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 820,
                "title": "火币全球专业站1月4日14:30上线PROPY(PRO)",
                "created": 1515047386000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月4日14:30开放PROPY(PRO)充值业务，1月5日14:00在创新区开放PROPY/BTC和PROPY/ETH交易，1月6日14:00开放提现业务。 点此查看……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 819,
                "title": "火币新年买卖GNX送币活动1月3日名单公示",
                "created": 1515032008000,
                "source": "1",
                "content": "亲爱的火币用户： 今天的GNX秒杀活动已经结束，感谢大家对火币的支持。GNX的获奖名单已于火币官网微博@火币网全部公示。关于今天活动奖励公布以及参与活动的相关规则，现公告如下： 一、公平的规则发放机制： 基于……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 817,
                "title": "火币全球专业站将于1月4日14:00上线NEO/USDT交易",
                "created": 1514966230000,
                "source": "1",
                "content": "尊敬的用户： 因NEO全球市值排名较高，流动性较好，因此火币专业站将于1月4日14:00上线NEO/USDT交易，但NEO仍属于创新区交易品种。 作为一种智能经济分布式网络，NEO基于区块链技术，将现实中的资……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 816,
                "title": "火币新年买卖QTUM送币活动1月2日名单公示",
                "created": 1514936127000,
                "source": "1",
                "content": "亲爱的火币用户： 今天的QTUM秒杀活动已经结束，感谢大家对火币的支持。QTUM的获奖名单已于火币官网微博@火币网全部公示，首先，很抱歉今天QTUM的奖励告示发的比预期要晚，但是本着公平公正为大家服务的理念，……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 814,
                "title": "火币全球专业站1月2日14:30上线MediShares (MDS)",
                "created": 1514874614000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间1月2日14:30开放MediShares (MDS)充值业务，1月3日14:00在创新区开放MDS/BTC和MDS/ETH交易，1月4日14:00开放提现业务。 点此……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 813,
                "title": "火币新年买卖HSR送币活动1月1日名单公示",
                "created": 1514822220000,
                "source": "1",
                "content": "亲爱的火币用户： 今天的HSR秒杀活动已经结束，感谢大家对火币的支持。关于活动获奖规则及活动奖励结果，现公告如下： 一、公平的规则发放机制： 基于今天的活动产生的结果，为避免大家错失获奖机会，以及为了保证活动……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 812,
                "title": "火币新年7日交易送币活动",
                "created": 1514789549000,
                "source": "1",
                "content": "尊敬的火币用户： 火币庆祝品牌升级的新年庆典，交易送30,000,000活动已经开始。1月1日至1月7日期间，火币选择了7个项目进行交易送币活动。每天用户可以在火币官网Huobi.pro看到活动入口（广告位）……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 810,
                "title": "火币全球专业站1月1日14:00上线Genaro Network (GNX)",
                "created": 1514786404000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间2018年1月1日14:00开放Genaro Network (GNX) 充值业务，1月2日14:00在创新区开放GNX/BTC和GNX/ETH交易，1月3日14:00……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 809,
                "title": "火币全球专业站元旦活动：七天不间断 狂送3000万",
                "created": 1514622977000,
                "source": "1",
                "content": "尊敬的用户： 火币庆祝元旦的狂送30,000,000活动即将开始。 你看到这个公告，你就已经先人一步知道了这次活动的信息！ 为庆祝火币全球专业站官网即将从 huobi.pro 升级为顶级域名 huobi.co……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 808,
                "title": "火币全球专业站关于Segwit2x分叉币BT2、B2X的处理方案",
                "created": 1514545698000,
                "source": "1",
                "content": "尊敬的用户： 近期，火币全球专业站收到大量用户咨询有关BT2资产处置方案，现答复如下： BT2和B2X是两个完全不同的数字资产，分叉高度、分叉方案、项目团队都不同。 火币全球专业站只是下线了BT2与BTC的交……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 806,
                "title": "火币全球专业站12月28日16:00上线ICON(ICX)",
                "created": 1514448002000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月28日16:00开放ICON(ICX)充值业务。12月29日14:00在创新区开放ICX/BTC和ICX/ETH交易。12月29日16:00开放ICON(ICX)……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 805,
                "title": "火币全球专业站关于法币交易区手续费再次优惠及产品服务升级的通知",
                "created": 1514431385000,
                "source": "1",
                "content": "尊敬的用户： 自火币全球专业站法币交易区业务开通以来，业务发展迅猛，为答谢大家支持，继本月免除交易手续费结束后，法币交易区现有业务将继续免除交易手续费，免除时间：2018年1月1日——1月31日（如有新增业务……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 802,
                "title": "火币全球专业站发放完毕Bitcoin File (BIFI)并上线BIFI交易",
                "created": 1514388583000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站已按1:1000的比例完成比特币分叉资产Bitcoin File (BIFI)的发放，并将于北京时间12月27日23:40在分叉区开放BIFI/BTC交易。 待分叉链稳定后，我们将……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 800,
                "title": "【100万元GAS等你拿】火币全球专业站12月27日14:00上线NEO、GAS",
                "created": 1514354445000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月27日14:00开放NEO、GAS充值业务。12月28日14:00在创新区开放NEO/BTC和GAS/BTC、GAS/ETH交易。12月29日14:00开放NEO……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 798,
                "title": "火币全球专业站关于Wax项目的用户补偿方案",
                "created": 1514272315000,
                "source": "1",
                "content": "尊敬的用户： 火币Pro已就Wax项目临时扩量事件，与项目发行方团队进行了积极的沟通。Wax发行方团队表示，有意愿联合火币Pro对因Wax项目临时扩量受到资产损失的用户，做出一定的补偿。 由于美国正处于圣诞假……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 796,
                "title": "火币全球专业站12月26日15:00上线星云币（NAS）",
                "created": 1514271592000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月26日15:00开放星云币（NAS）充值业务。12月27日14:00在创新区开放NAS/BTC和NAS/ETH交易。12月29日15:00开放提现业务。 点此查看……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 794,
                "title": "火币Pro关于Wax临时扩量事件的声明",
                "created": 1514120467000,
                "source": "1",
                "content": "尊敬的火币Pro用户： 日前Wax项目因临时拆分导致用户资产出现严重波动，经火币与Wax项目方沟通了解后，现公告如下： Wax项目是一个去中心化的全球虚拟资产交易所，是面向网络游戏虚拟财产交易的通用去中心化平……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 792,
                "title": "欢迎老火伴回家 火币送出1亿红包",
                "created": 1513954027000,
                "source": "huobipro",
                "content": "尊敬的用户： 即日起至12月31日，火币网老用户（2017年９月15日前在火币网注册，且从未在火币Pro有任何交易的用户）可以领到价值50元人民币的红包，快来瞧瞧! 活动规则 1. 完成实名认证 2. 绑定手……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 789,
                "title": "【交易送HSR】火币全球专业站上线HSR/USDT交易及HSR杠杆交易",
                "created": 1513859756000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月22日16:00在创新区上线HSR/USDT交易，并开通HSR杠杆交易。 【HSR杠杆交易 多借礼多多】 2017年12月22日16:00-12月31日24:00……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 788,
                "title": "火币全球专业站关于上调USDT和BTC最小充值额度的通知",
                "created": 1513856480000,
                "source": "1",
                "content": "尊敬的用户： 因比特币持续受到全球投资者的青睐，越来越多的人关注和使用比特币，导致近期比特币网络转账手续费持续增高，为了为用户提供更高效便捷的服务，火币专业站决定即刻起上调USDT最小充值额度至100USDT……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 786,
                "title": "【200万元ELF送不停】火币全球专业站12月21日9:50全球首发ælf (ELF)",
                "created": 1513821016000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月21日9:50开放充值业务，并同时在创新区开放ELF/BTC和ELF/ETH交易。12月25日9:50开放ELF提现业务。 【200万元ELF送不停】 北京时间1……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 785,
                "title": "火币全球专业站声明：请警惕冒用火币名义的虚假赠币活动",
                "created": 1513816262000,
                "source": "1",
                "content": "尊敬的用户： 近日，我们监测到社交媒体、数字货币社群中出现了假冒火币集团名义发送的“Huobi系统免费注册赠送4000火币”的虚假邀请链接。 火币集团郑重声明，火币集团及旗下所有平台，并未以任何形式发行官方代……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 783,
                "title": "火币全球专业站关于USDT钱包升级的说明",
                "created": 1513773306000,
                "source": "1",
                "content": "尊敬的用户： 由于近期比特币网络转账手续费持续增高，比特币区块网络上的未确认交易数已达到近期峰值，为了更好的提升我们的服务质量，火币专业站需升级USDT钱包（USDT是在比特币区块链上发布的数字资产），USD……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 781,
                "title": "火币全球专业站关于ERC20充提币延迟处理的公告",
                "created": 1513756861000,
                "source": "1",
                "content": "尊敬的用户： 由于近期业务量暴涨，为了更好的提升我们的服务质量，火币全球专业站正在进行钱包升级，当前所有ERC20币种充值和提现均需延迟处理，预计12月20日18:30恢复正常，根据实际情况，升级可能会提前或……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 779,
                "title": "【100万元BTM等你拿】12月20日14:00上线比原链(BTM)",
                "created": 1513749630000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月20日14:00开放BTM充值业务，12月20日18:00开放提现业务，12月21日14:00在创新区开放BTM/BTC和BTM/ETH交易。 【100万元BTM……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 777,
                "title": "【豪送100万元WAX】12月20日10:00全球首发WAX",
                "created": 1513735185000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月20日10:00开放WAX充值业务，并同时在创新区开放WAX/BTC和WAX/ETH交易。12月22日10:00开放WAX提现业务。 【首发豪礼人人有 豪送100……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 776,
                "title": "关于火币全球专业站法币交易区系统升级维护的公告",
                "created": 1513676244000,
                "source": "1",
                "content": "尊敬的用户： 火币全球交易站法币交易区将于20日凌晨2:00进行升级维护，预计升级时间5小时，恢复时间20日7:00。 升级期间将暂停法币交易区的服务，请您务必提前做好交易安排，非常感谢您的理解！ 本次更新内……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 774,
                "title": "火币全球专业站12月19日14:00上线HSR",
                "created": 1513663119000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月19日14:00开放HSR充值业务，12月19日18:00开放提现业务，12月20日14:00在创新区开放HSR/BTC和HSR/ETH交易。 【空投价值5000……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 772,
                "title": "700万元达世邀你嗨",
                "created": 1513651657000,
                "source": "1",
                "content": "一、达世空投 12月19日11:00-12月25日11:00期间，参与DASH/USDT和DASH/BTC交易的实名用户可均分价值百万元的DASH，奖励于活动结束后三个工作日内发放。 二、答题送达世 12月1……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 770,
                "title": "Ethereum Fog（ETF）已完成发放",
                "created": 1513597661000,
                "source": "1",
                "content": "尊敬的用户： ETF资产已发放至您火币专业站账户中，请您至资产页面查看。由于以太坊是一款能够在区块链上实现智能合约、开源的底层系统，上面已经产生了几百个ERC20代币，一旦以太坊被分叉，那么所有的ERC20代……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 768,
                "title": "杠杆交易领红包，火币狂撒百万元",
                "created": 1513595439000,
                "source": "1",
                "content": "尊敬的用户： 您好，火币全球专业站定于北京时间12月18日19时-24日24时期间，联合唯链（VEN）和QTUM（量子链）推出红包大礼，在此期间，所有参与杠杆交易的用户均有机会分享百万元的红包奖励。 活动一：……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 766,
                "title": "【500万元大礼来袭】12月18日14:00上线唯链 (VEN)、SALT",
                "created": 1513576793000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月18日14:00开放VEN、SALT充值业务，12月18日18:00开放提现业务，12月19日14:00在创新区开放VEN/BTC、VEN/ETH、SALT/BT……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 764,
                "title": "火币全球专业站关于糖果分发的说明",
                "created": 1513522800000,
                "source": "1",
                "content": "尊敬的用户： 因近期比特币、莱特币、以太坊等都可能会产生分叉，越来越多的用户咨询火币专业站是否支持相关分叉资产的发放。作为交易平台，火币专业站会切实保护好用户的每一份已有的和应得的资产，将用户应得的资产都分给……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 762,
                "title": "关于恢复USDT充值、提现业务的公告",
                "created": 1513260820000,
                "source": "1",
                "content": "尊敬的用户： 目前火币全球专业站已完成USDT钱包升级，USDT充值、提现业务即刻起立即恢复。 感谢您的理解与支持！ 火币全球专业站 2017年12月14日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 760,
                "title": "关于暂停USDT充值提现业务的公告",
                "created": 1513242981000,
                "source": "1",
                "content": "尊敬的用户： USDT钱包升级维护，升级期间暂停USDT充值和提现业务，恢复时间，另行公告通知，给您带来不便敬请谅解。 火币全球专业站 2017年12月14日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 758,
                "title": "火币全球专业站12月14日14:00上线Civic (CVC)",
                "created": 1513231194000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月14日14:00开放Civic (CVC)充值业务，12月14日18:00开放提现业务，12月15日14:00开放CVC/BTC和CVC/ETH交易。 点此查看C……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 756,
                "title": "关于SBTC和BCX发放及上线交易的公告",
                "created": 1513176407000,
                "source": "1",
                "content": "尊敬的用户： SBTC和BCX已于区块高度498888（北京时间2017年12月12日18:29:53）分叉成功。火币专业站已按1BTC:1SBTC和1BTC:10000BCX的比例发放SBTC和BCX资产至……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 754,
                "title": "火币全球专业站12月13日14:00上线Decentraland (MANA)",
                "created": 1513144800000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月13日14:00开放Decentraland (MANA)充值业务，12月13日18:00开放提现业务，12月14日14:00开放MANA/BTC和MANA/ET……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 752,
                "title": "关于比特币现金简写BCC变更为BCH的公告",
                "created": 1513136713000,
                "source": "1",
                "content": "尊敬的用户： 随着数字资产行业的蓬勃发展，出现了很多写法相近的数字资产英文名称缩写。为了更准确地区分数字资产，与业界普遍缩写方式保持同步，火币专业站将于2017年12月19日15:00对系统进行升级，同时将比……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 750,
                "title": "火币全球专业站12月13日10:30全球首发SmartMesh (SMT)",
                "created": 1513131849000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月13日10:30开放SmartMesh (SMT)充值业务，并同时上线SMT/BTC和SMT/ETH交易。12月15日10:30开放SMT提现业务。 【SMT首发……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 748,
                "title": "火币全球专业站关于领取BCX的公告",
                "created": 1512995856000,
                "source": "1",
                "content": "尊敬的用户： 由于比特无限(BCX)将于区块高度498888进行分叉，火币Pro将于区块高度到达498888前（预计北京时间2017年12月13日）对用户账户中的BTC资产进行快照，并于当日以1: 10000……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 746,
                "title": "火币全球专业站12月12日上线QTUM/USDT交易",
                "created": 1512993961000,
                "source": "1",
                "content": "尊敬的用户： 因QTUM全球市值排名较高，流动性较好，因此火币专业站将于12月12日12:00上线QTUM/USDT交易，但QTUM仍属于创新区交易品种。 与主区交易的区块链资产相比，除火币专业站《用户协议》……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 744,
                "title": "火币全球专业站12月11日上线注意力币 (BAT)",
                "created": 1512972007000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月11日14:00开放注意力币 (BAT)充值提现业务，12月12日14:00在创新区上线BAT/BTC和BAT/ETH交易。 什么是注意力币（BAT）？ BAT(……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 742,
                "title": "火币全球专业站12月8日上线杠杆交易",
                "created": 1512737568000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站现已正式上线杠杆交易，当前USDT交易区的所有币种均将支持杠杆交易（BTC、BCC、ETH、LTC、ETC、DASH、XRP、EOS、OMG、ZEC），BTC和ETH交易区暂不支持……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 740,
                "title": "火币全球专业站关于领取SBTC的公告",
                "created": 1512650984000,
                "source": "1",
                "content": "尊敬的用户： 由于超级比特币(SBTC)将于区块高度498888进行分叉，火币Pro将于区块高度到达498888前（预计北京时间2017年12月13日）对用户账户中的BTC资产进行快照，并于当日以1:1的比例……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 738,
                "title": "火币全球专业站12月7日上线量子链（QTUM）",
                "created": 1512647976000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月7日20:00开放量子链（QTUM）充值提现业务，12月8日14:00上线QTUM/BTC和QTUM/ETH交易。 什么是量子链？ Qtum Blockchain……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 736,
                "title": "火币专业站12月7日0:00进行系统维护",
                "created": 1512545357000,
                "source": "1",
                "content": "尊敬的用户： 火币专业站将于北京时间12月7日0:00-0:40进行系统维护，维护期间，网站和APP将有一段时间无法访问，API暂停提供数据，请您提前做好准备，感谢您的理解与支持！ 火币专业站 2017年12……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 734,
                "title": "火币专业站12月6日上线Zcash (ZEC)",
                "created": 1512539949000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月6日14:00开放Zcash (ZEC)充值提现业务，12月7日14:00上线ZEC/BTC和ZEC/USDT交易。 什么是Zcash？ Zcash是一种去中心化……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 732,
                "title": "火币专业站12月5日上线CyberMiles (CMT)",
                "created": 1512453573000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月5日14:00开放CyberMiles (CMT）充值提现业务，12月6日14:00上线CMT/BTC和CMT/ETH交易。 什么是CyberMiles？ Cyb……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 730,
                "title": "火币专业站12月5日上线EOS/USDT和OMG/USDT交易",
                "created": 1512384442000,
                "source": "1",
                "content": "尊敬的用户： 因EOS和OMG符合火币专业站主区上币标准，因此火币专业站将于12月5日10:00上线EOS/USDT和OMG/USDT交易，并将EOS和OMG划分至主区。 主区： 交易品种： 经过市场充分验证……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 728,
                "title": "12月4日上线Monaco (MCO)【价值400万元福利等你拿】",
                "created": 1512367216000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月4日14:00开放Monaco (MCO) 充值提现业务，12月5日14:00上线MCO/BTC和MCO/ETH交易。 【四波福利 价值400万元 狂嗨一周】 第……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 727,
                "title": "关于点对点交易平台开通认证商家及手续费优惠的通知",
                "created": 1512186206000,
                "source": "1",
                "content": "尊敬的用户： 为促进市场的健康稳定发展，更好的服务用户，点对点交易平台于12月2日上线了“认证商家”功能模块。 认证商家会显示专属认证标识、享有一对一客服和优质广告位展示等服务。 认证商家需要缴纳一定的保证金……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 725,
                "title": "关于www.huobibtc.com网站盗用火币专业站logo和资料的声明",
                "created": 1512118617000,
                "source": "1",
                "content": "尊敬的用户： 火币专业站在此明确提示，一家网址为http://www.huobibtc.com/的网站在未经火币专业站许可的情况下，盗用火币专业站logo、介绍，冒充火币网站。火币专业站从未与之建立任何合作关……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 723,
                "title": "火币全球专业站12月1日10:00全球首发万物链IoT Chain（ITC）",
                "created": 1512093521000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间12月1日10:00开放万物链IoT Chain（ITC）充值提现业务，12月1日12:00上线ITC/BTC和ITC/ETH交易。 ITC（万物链）项目介绍： ITC……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 721,
                "title": "火币专业站11月30日18:00上线QASH",
                "created": 1512035954000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月30日18:00开放QASH充值提现业务，11月30日21:00上线QASH/BTC和QASH/ETH交易。 QASH介绍： QASH（QUOINE LIQUID……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 719,
                "title": "火币专业站11月28日上线TenX (PAY), DigixDAO (DGD)和Golem (GNT)",
                "created": 1511841507000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月28日14:00开放TenX (PAY), DigixDAO (DGD)和Golem (GNT)充值提现业务，11月29日14:00上线PAY/BTC和PAY/E……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 717,
                "title": "火币全球专业站11月27日12:00全球首发M.I.T（TNB）",
                "created": 1511750472000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月27日12:00开放M.I.T（TNB）充值提现业务，并同时上线TNB/BTC和TNB/ETH交易。 【TNB首发豪礼人人有 交易多少送多少】 2017年11月2……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 715,
                "title": "火币专业站关于BT1、BT2、BTG和BCD处理方案的公告",
                "created": 1511719103000,
                "source": "火币网",
                "content": "尊敬的用户： 原定于区块高度494784发生比特币Segwit2x硬分叉，由于区块高度494784（2017年11月17日 20:48:03）后至今仍没有Segwit2x的区块产生，且Segwit2x失去了社……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 713,
                "title": "火币专业站关于比特币钻石BCD快照时间的公告",
                "created": 1511510556000,
                "source": "1",
                "content": "尊敬的用户： 火币专业站将于区块高度到达495866前对用户账户中的BTC和BT1资产进行快照，即区块高度到达495865后进行快照，预计为北京时间2017年11月24日18:00-20:00期间，具体时间由……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 711,
                "title": "火币全球专业站关于恢复USDT充值、提现业务的公告",
                "created": 1511495336000,
                "source": "1",
                "content": "尊敬的用户： 目前火币Pro已完成USDT钱包升级，USDT充值、提现业务即刻起立即恢复。 感谢您的理解与支持！ 火币全球专业站 2017年11月24日",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 709,
                "title": "火币全球专业站11月23日上线Ripple (XRP)",
                "created": 1511416807000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月23日14:00开放Ripple (XRP)充值提现业务，11月24日14:00上线XRP/BTC和XRP/USDT交易。 Ripple项目介绍： 瑞波（Ripp……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 707,
                "title": "火币全球专业站关于BTC和BT1领取BCD的公告",
                "created": 1511346712000,
                "source": "1",
                "content": "尊敬的用户： 由于Segwit2x声明的分叉起始区块高度494784已于北京时间2017年11月17日20:48:03出块，但是目前仍未成功稳定地挖出Segwit2x区块，且Segwit2x没有动态难度调整机……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 705,
                "title": "火币全球专业站11月22日上线Tierion (TNT)",
                "created": 1511330405000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月22日14:00开放Tierion (TNT)充值提现业务，11月23日14:00上线TNT/BTC和TNT/ETH交易。 Tierion项目介绍： Tierio……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 702,
                "title": "火币全球专业站关于比特币各种分叉（BTG、BCD等）的态度及处理方案",
                "created": 1511320671000,
                "source": "1",
                "content": "尊敬的用户： 随着近期比特币分叉事件的逐渐增多，越来越多的用户询问火币全球专业站对于近期已产生的分叉币（如BTG）和未来将要产生的分叉币（如BCD等）的态度和处理方案。火币Pro声明如下： 1. 火币Pro认……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 699,
                "title": "火币全球专业站关于暂停USDT充值、提现的公告",
                "created": 1511235766000,
                "source": "1",
                "content": "尊敬的用户： 由于收到Tether官方通知，USDT钱包需要升级。为了保证用户资产的绝对安全，火币全球专业站（包括点对点交易平台）暂停USDT充值、提现业务（点对点交易平台和火币Pro的平台划转功能不受影响）……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 697,
                "title": "火币全球专业站11月21日全球首发Quantstamp (QSP)",
                "created": 1511227258000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月21日9:30开放Quantstamp (QSP)充值提现业务，11月21日12:30上线QSP/BTC和QSP/ETH交易。 Quantstamp项目介绍： Q……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 695,
                "title": "火币全球专业站11月20日上线Status (SNT)",
                "created": 1511157572000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月20日14:00开放Status (SNT)充值提现业务，11月22日14:00上线SNT/BTC交易。 Status项目介绍： Status是一款基于以太坊客户……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 693,
                "title": "【豪掷百万】新用户注册充值就送1MTL",
                "created": 1511153856000,
                "source": "1",
                "content": "尊敬的用户： 火币Pro联合Metal豪掷百万活动第一弹： 2017年11月20日-11月26日 期间，注册并成功充值比特币或USDT的用户即送1MTL，奖励于11月27日统一发放。 更多活动，敬请期待…… ……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 691,
                "title": "火币全球专业站11月21日0:00进行系统维护",
                "created": 1511149966000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于北京时间11月21日0:00-0:15进行系统维护，在此期间，网站和APP将无法访问，API暂停提供数据，请您提前做好准备，感谢您的理解与支持！ 火币全球专业站 2017年11……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 689,
                "title": "火币全球专业站11月18日上线EOS",
                "created": 1510972474000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站现已开放EOS充值提现业务，11月18日14:00上线EOS/BTC和EOS/ETH交易。 EOS项目介绍： EOS (Enterprise Operation System)是由……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 687,
                "title": "火币全球专业站11月16日上线Metal (MTL)",
                "created": 1510813490000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月16日14:00开放Metal (MTL)充值提现业务，11月17日14:00上线MTL/BTC交易。 【5000个MTL等你拿】 11月16日14:00-11月……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 685,
                "title": "火币全球专业站11月15日上线Storj (STORJ)",
                "created": 1510727192000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月15日14:00开放Storj (STORJ)充值提现业务，11月16日14:00上线STORJ/BTC交易。 Storj介绍： Storj是一个致力于成为免审查……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 683,
                "title": "火币全球专业站11月14日上线雷电网络Raiden Network(RDN)",
                "created": 1510640958000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月14日14:00开放Raiden Network(RDN)充值提现业务，11月15日14:00上线RDN/BTC和RDN/ETH交易。 Raiden Networ……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 680,
                "title": "Pro狂撒USDT回馈老用户第二波",
                "created": 1510567643000,
                "source": "1",
                "content": "尊敬的用户： 火币Pro狂撒USDT回馈老用户第二波福利来啦！ 活动日期： 2017年11月14日-11月30日 活动对象： 火币用户（www.huobi.com的注册用户） 活动规则： 1. 未在火币Pro……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 679,
                "title": "火币全球专业站11月13日上线OmiseGO（OMG）",
                "created": 1510552624000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月13日14:00开放OmiseGO（OMG）充值提现业务，11月14日14:00上线OMG/BTC和OMG/ETH交易。 【天降大礼，5000个OMG等你瓜分】 ……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 676,
                "title": "火币全球专业站11月10日22:00进行钱包系统维护，交易正常",
                "created": 1510305161000,
                "source": "1",
                "content": "尊敬的用户： 因11月10日22:00至次日5:00期间，火币全球专业站需处理火币网（www.huobi.com）用户资产迁移事宜，在此期间： 1. 火币全球专业站的BTC、LTC、BCC和USDT充值提现业……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 672,
                "title": "火币全球专业站11月9日正式上线达世币DASH",
                "created": 1510192603000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于北京时间11月9日10:00开放达世币DASH充值提现业务，11月10日10:00上线DASH/BTC和DASH/USDT交易。 达世币DASH介绍： 达世币是一款支持即时交易……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 669,
                "title": "关于火币全球专业站11月7日上线Ripio（RCN）的公告",
                "created": 1510023038000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于北京时间2017年11月7日14:00开放Ripio代币RCN的充值提现业务，并于11月8日14:00正式上线RCN/BTC和RCN/ETH交易。 火币全球专业站是第一个上线R……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 667,
                "title": "关于火币全球专业站上线点对点交易平台的公告",
                "created": 1509786389000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站11月4日正式上线点对点交易平台，提供比特币和USDT的点对点交易服务，支持人民币买卖，支持提币。上线首月（11月4日-12月4日），交易手续费全免！立即体验： https://o……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 665,
                "title": "火币Pro狂撒USDT回馈老用户",
                "created": 1509621953000,
                "source": "1",
                "content": "亲爱的用户， 正值火币Pro站新版上线之际，给大家发福利了！登录Pro就送USDT，连续登录送更多！ 活动日期： 2017年11月3日-11月12日 活动对象： 火币用户（www.huobi.com的注册用户……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 663,
                "title": "火币全球专业站11月1日上线KyberNetwork(KNC), AirSwap(AST)和0x(ZRX)",
                "created": 1509506547000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站将于北京时间2017年11月1日14:00开放KNC,AST和ZRX的充值提现业务，并于当日20:00正式上线KNC/BTC,AST/BTC和ZRX/BTC交易。 KyberNet……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 661,
                "title": "关于火币全球专业站10月31日上线BCC/USDT和ETC/USDT的公告",
                "created": 1509356229000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于10月31日12:00上线BCC/USDT和ETC/USDT交易。 上Pro打新 充币送壕礼 10月26日-11月9日期间，凡在Huobi Pro充值USDT等新上线的数字资产……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 653,
                "title": "关于火币全球专业站10月27日上线LTC/USDT的公告",
                "created": 1509023499000,
                "source": "1",
                "content": "尊敬的用户： 火币全球专业站定于10月27日12:00上线LTC/USDT交易。 上Pro打新 充币送壕礼 10月26日-11月9日期间，凡在Huobi Pro充值USDT等新上线的数字资产（10月26日-1……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 651,
                "title": "关于火币全球专业站10月24日上线Tether（简称USDT）的公告",
                "created": 1508838301000,
                "source": "火币全球专业站",
                "content": "尊敬的用户： 火币全球专业站定于10月24日18:00开放USDT充值提现业务，10月26日12:00开放BTC/USDT和ETH/USDT交易。 USDT介绍： USDT是Tether公司推出的基于稳定价值……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 650,
                "title": "火币全球专业站关于分叉币的态度及处理方案",
                "created": 1508824385000,
                "source": "火币全球专业站",
                "content": "尊敬的用户： 随着近期比特币及其它币种分叉事件的逐渐增多，越来越多的用户询问火币全球专业站对各种分叉的态度和处理方案。火币全球专业站一直以保障用户利益为中心，坚持守护用户的每一份资产，永远把用户的权益放在首位……",
                "topNotice": False,
                "weight": 0
            }, {
                "id": 648,
                "title": "火币全球专业站（Huobi.pro）关于比特币Segwit2x分叉处理方案的公告",
                "created": 1508222122000,
                "source": "1",
                "content": "尊敬的用户： 2017年5月23日，来自全球22个国家58家知名区块链公司共同签署了纽约共识（Segwit2x，即隔离验证+2M），纽约共识获得了全网83.28%的算力签字支持，总量超过每月51亿美元交易额的……",
                "topNotice": False,
                "weight": 0
            }],
            "currentPage": 1,
            "orderColumn": "weight DESC, created DESC"
        }
    }

    data = notice_list['data']['items']

    try:
        for item in data:
            print(item)
            market_id = 1
            market_notice_id = int(item['id'])
            title = item['title']
            created = datetime.fromtimestamp(item['created'] / 1000).strftime("%Y-%m-%d %H:%M:%S")
            source = item['source']
            content = item['content']
            top_notice = bool(item['topNotice'])
            weight = item['weight']
            exec_sql = insert_sql % (market_id, market_notice_id, title, created, source, content, top_notice, weight)
            cursor.execute(exec_sql)
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        cursor.close()
        db.close()
