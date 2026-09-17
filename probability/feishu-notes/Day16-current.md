# 飞书笔记｜Day 16（进行中）

> 当前进度约 30%。本文件将在 Day 16 真正完成后再整理为最终版。

## 1. 置信度与显著性水平

若置信度为：

$$1-\alpha$$

则区间外概率为：

$$\alpha$$

双侧置信区间中，两侧通常各分：

$$\frac{\alpha}{2}$$

例如 95% 置信区间：

$$1-\alpha=0.95$$

所以：

$$\alpha=0.05$$

两边各：

$$\frac{\alpha}{2}=0.025$$

---

## 2. 正态总体，方差已知，求均值的置信区间

设：

$$X\sim N(\mu,\sigma^2)$$

其中 $\sigma^2$ 已知、$\mu$ 未知。

使用统计量：

$$\frac{\overline X-\mu}{\sigma/\sqrt n}\sim N(0,1)$$

对于置信度 $1-\alpha$：

$$P\left(-z_{\alpha/2}<\frac{\overline X-\mu}{\sigma/\sqrt n}<z_{\alpha/2}\right)=1-\alpha$$

解出 $\mu$：

$$\overline X-z_{\alpha/2}\frac{\sigma}{\sqrt n}<\mu<\overline X+z_{\alpha/2}\frac{\sigma}{\sqrt n}$$

所以置信区间：

$$\left(\overline X-z_{\alpha/2}\frac{\sigma}{\sqrt n},\ \overline X+z_{\alpha/2}\frac{\sigma}{\sqrt n}\right)$$

可记为：

**点估计 ± 临界值 × 标准误。**

### 95% 置信区间

常用临界值：

$$z_{0.025}=1.96$$

例：

$$\sigma^2=4$$

$$n=100$$

$$\overline X=10$$

标准误：

$$\frac{\sigma}{\sqrt n}=\frac2{10}=0.2$$

误差范围：

$$1.96\times0.2=0.392$$

所以：

$$\mu\text{ 的 95% 置信区间}=(9.608,10.392)$$

---

## 3. 下一步：方差未知时估计均值

若总体仍为正态总体，但 $\sigma^2$ 未知，则不能再用总体标准差 $\sigma$。

改用：

$$\frac{\overline X-\mu}{S/\sqrt n}\sim t(n-1)$$

因此均值置信区间将使用 t 分布临界值，而不是标准正态临界值。

### 当前断点

当前最后一道待答：

若总体方差未知，样本容量：

$$n=16$$

构造 $\mu$ 的置信区间时，t 分布自由度是多少？

正确续答：

$$15$$

---

## Day 16 后续待学

- 方差未知时均值的 t 置信区间。
- 正态总体方差的卡方置信区间。
- 按考研范围处理双总体区间估计。
- 假设检验基本思想。
- 原假设 $H_0$ 与备择假设 $H_1$。
- 显著性水平与拒绝域。
- 双侧检验与单侧检验。
- 第一类错误与第二类错误。
- 最终综合收尾。
