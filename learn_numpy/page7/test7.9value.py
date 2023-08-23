# 金融函数

# fv函数计算所谓的终值（future value），即基于一些假设给出的某个金融资产在未来某一时间点的价值。
# pv函数计算现值（present value），即金融资产当前的价值。
# npv函数返回的是净现值（net present value），即按折现率计算的净现金流之和。
# pmt函数根据本金和利率计算每期需支付的金额。
# irr函数计算内部收益率（internal rate of return）。
# 内部收益率是是净现值为0时的有效利率，不考虑通胀因素。
# mirr函数计算修正后内部收益率（modified internal rate of return），
# 是内部收益率的改进版本。
# nper函数计算定期付款的期数。
# rate函数计算利率（rate of interest）。

import numpy as np
import numpy_financial as npf
from matplotlib.pyplot import plot, show

# 我们以利率3%、每季度支付金额10、存款周期5年以及现值1 000为参数，
# 使用NumPy中的fv函数计算了终值

print("Future value", npf.fv(0.03 / 4, 5 * 4, -10, -1000))
fvals = []
for i in range(1, 10):
 fvals.append(npf.fv(.03/4, i * 4, -10, -1000))
plot(fvals, 'bo')
show()

# 现值

print("Present value", npf.pv(0.03 / 4, 5 * 4, -10, 1376.09633204))

# 净现值净现值（net present value）

cashflows = np.random.randint(100, size=5)
cashflows = np.insert(cashflows, 0, -100)
print("Cashflows", cashflows)
print("Net present value", npf.npv(0.03, cashflows))

# 内部收益率
# 内部收益率（internal rate of return）是净现值为0时的有效利率，不考虑通胀因素。
# NumPy中的irr函数根据给定的现金流数据返回对应的内部收益率
print("Internal rate of return", npf.irr([-100, 38, 48, 90, 17, 36]))


# 分期付款
# NumPy中的pmt函数可以根据利率和期数计算贷款每期所需支付的资金。
# 假设你贷款100万，年利率为10%，要用30年时间还完贷款，那么每月你必须支付多少资金呢？
# 使用刚才提到的参数值，调用pmt函数。

print("Payment", npf.pmt(0.07 / 12, 12 * 30, 10000000))

# 付款期数
# NumPy中的nper函数可以计算分期付款所需的期数。所需的参数为贷款利率、固定的月供以及贷款额。
# 考虑贷款9 000，年利率10%，每月固定还款为100的情形。通过nper函数计算出付款期数。

print("Number of payments", npf.nper(0.05/12, -4, 100))
# 为什么很多值都不行

# 计算利率
print("Interest rate", 12 * npf.rate(167, -40000, 10000000, 0))


