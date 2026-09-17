# 飞书笔记｜Day 9–Day 15

## Day 9｜期望与方差

### 期望

离散型：

$$E[g(X)]=\sum g(x_i)p_i$$

连续型：

$$E[g(X)]=\int g(x)f_X(x)\,dx$$

### 方差

$$D(X)=E(X^2)-[E(X)]^2$$

因此：

$$E(X^2)=D(X)+[E(X)]^2$$

以及：

$$E[(X-a)^2]=D(X)+[E(X)-a]^2$$

### 线性性质

$$E(aX+b)=aE(X)+b$$

$$D(aX+b)=a^2D(X)$$

若 $X,Y$ 独立：

$$D(aX+bY)=a^2D(X)+b^2D(Y)$$

### 八大分布期望方差

0-1：

$$E(X)=p$$

$$D(X)=p(1-p)$$

二项：

$$E(X)=np$$

$$D(X)=np(1-p)$$

泊松：

$$E(X)=D(X)=\lambda$$

几何：

$$E(X)=\frac1p$$

$$D(X)=\frac{1-p}{p^2}$$

均匀：

$$E(X)=\frac{a+b}{2}$$

$$D(X)=\frac{(b-a)^2}{12}$$

指数：

$$E(X)=\frac1\lambda$$

$$D(X)=\frac1{\lambda^2}$$

正态：

$$E(X)=\mu$$

$$D(X)=\sigma^2$$

### 易错点

- 指数分布的参数与均值不要写反。
- 方差中常数系数必须平方。

---

## Day 10｜特殊期望、矩与分布数字特征

若 $Z\sim N(0,1)$：

$$E|Z|=\sqrt{\frac2\pi}$$

$$D(|Z|)=1-\frac2\pi$$

若 $X\sim N(0,\sigma^2)$：

$$E|X|=\sigma\sqrt{\frac2\pi}$$

$$D(|X|)=\sigma^2\left(1-\frac2\pi\right)$$

### 标准正态矩

奇数阶矩为 0：

$$E(Z^{2k+1})=0$$

常用偶数阶：

$$E(Z^2)=1$$

$$E(Z^4)=3$$

$$E(Z^6)=15$$

一般形式：

$$E(Z^{2k})=(2k-1)!!$$

若 $X\sim N(\mu,\sigma^2)$：

$$E[(X-\mu)^4]=3\sigma^4$$

$$E[(X-\mu)^6]=15\sigma^6$$

### Pascal 分布

第 n 次成功发生时的总试验次数可看成 n 个独立几何变量之和：

$$E(X)=\frac np$$

$$D(X)=\frac{n(1-p)}{p^2}$$

### 对称性

若多个变量在分母中地位完全对称，例如：

$$\frac{X_i^2}{\sum_jX_j^2}$$

在对称条件下常有：

$$E\left(\frac{X_i^2}{\sum_jX_j^2}\right)=\frac1n$$

---

## Day 11｜协方差、相关系数、独立与不相关

### 协方差

$$\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)$$

$$\operatorname{Cov}(X,X)=D(X)$$

$$\operatorname{Cov}(X,Y)=\operatorname{Cov}(Y,X)$$

线性性质：

$$\operatorname{Cov}(aX+b,cY+d)=ac\operatorname{Cov}(X,Y)$$

### 相关系数

$$\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}}$$

$$|\rho|\le1$$

非退化情形下，$|\rho|=1$ 对应严格线性关系。

### 和差方差

$$D(X+Y)=D(X)+D(Y)+2\operatorname{Cov}(X,Y)$$

$$D(X-Y)=D(X)+D(Y)-2\operatorname{Cov}(X,Y)$$

### 独立与不相关

一般：

$$X,Y\text{ 独立}\Rightarrow\operatorname{Cov}(X,Y)=0$$

反过来一般不成立。

二维正态中：

$$\operatorname{Cov}(X,Y)=0\Longleftrightarrow X,Y\text{ 独立}$$

若 $U=X+Y,V=X-Y$：

$$\operatorname{Cov}(U,V)=D(X)-D(Y)$$

---

## Day 12｜切比雪夫、大数定律、中心极限定理

### 切比雪夫不等式

$$P(|X-\mu|\ge\varepsilon)\le\frac{\sigma^2}{\varepsilon^2}$$

等价地：

$$P(|X-\mu|<\varepsilon)\ge1-\frac{\sigma^2}{\varepsilon^2}$$

### 依概率收敛

$$X_n\xrightarrow{P}a$$

含义是：任意固定 $\varepsilon>0$，都有：

$$P(|X_n-a|\ge\varepsilon)\to0$$

### 大数定律

独立同分布且期望存在时：

$$\overline X\xrightarrow{P}\mu$$

伯努利频率依概率收敛到 $p$。

### 中心极限定理

$$\frac{S_n-n\mu}{\sigma\sqrt n}\approx N(0,1)$$

$$S_n\approx N(n\mu,n\sigma^2)$$

样本均值：

$$\frac{\overline X-\mu}{\sigma/\sqrt n}\approx N(0,1)$$

$$\overline X\approx N\left(\mu,\frac{\sigma^2}{n}\right)$$

二项分布正态近似：

$$\frac{X-np}{\sqrt{np(1-p)}}\approx N(0,1)$$

### 易错点

标准化必须先“减均值，再除标准误”，不能把原始误差直接当 z 值。

---

## Day 13｜统计基础 + 三大抽样分布

### 总体、样本、统计量

简单随机样本 $X_1,\dots,X_n$：相互独立，且与总体同分布。

统计量是样本的函数，不能含未知参数。

### 样本均值与样本方差

$$\overline X=\frac1n\sum_{i=1}^nX_i$$

$$S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\overline X)^2$$

### 卡方分布

若 $Z_i$ 独立且：

$$Z_i\sim N(0,1)$$

则：

$$\sum_{i=1}^nZ_i^2\sim\chi^2(n)$$

正态总体样本方差：

$$\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$$

### F 分布

若独立：

$$U\sim\chi^2(m)$$

$$V\sim\chi^2(n)$$

则：

$$\frac{U/m}{V/n}\sim F(m,n)$$

### t 分布

若独立：

$$Z\sim N(0,1)$$

$$V\sim\chi^2(n)$$

则：

$$\frac{Z}{\sqrt{V/n}}\sim t(n)$$

### t 与 F

$$T\sim t(n)\Rightarrow T^2\sim F(1,n)$$

### 正态总体样本均值

$$\overline X\sim N\left(\mu,\frac{\sigma^2}{n}\right)$$

并且正态总体下：

$$\overline X\perp S^2$$

未知方差时：

$$\frac{\overline X-\mu}{S/\sqrt n}\sim t(n-1)$$

两独立正态总体：

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F(n_1-1,n_2-1)$$

---

## Day 14｜六大统计量 + 抽样分布关系

### 单正态总体

$$\overline X\sim N\left(\mu,\frac{\sigma^2}{n}\right)$$

$$\frac{\sqrt n(\overline X-\mu)}{\sigma}\sim N(0,1)$$

$$\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)$$

$$\frac{\sqrt n(\overline X-\mu)}{S}\sim t(n-1)$$

### 双正态总体

方差已知，比较均值：

$$\frac{(\overline X-\overline Y)-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}}\sim N(0,1)$$

共同方差未知但相等时，先合并：

$$S_w^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}$$

再构造：

$$\frac{(\overline X-\overline Y)-(\mu_1-\mu_2)}{S_w\sqrt{1/n_1+1/n_2}}\sim t(n_1+n_2-2)$$

比较两个总体方差：

$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F(n_1-1,n_2-1)$$

### 四类用途地图

$$\text{均值 + 方差已知}\Rightarrow N$$

$$\text{均值 + 方差未知}\Rightarrow t$$

$$\text{单个正态总体方差}\Rightarrow\chi^2$$

$$\text{两个正态总体方差之比}\Rightarrow F$$

### 分布关系

$$N(0,1)\xrightarrow{\text{平方和}}\chi^2$$

$$\frac{N(0,1)}{\sqrt{\chi^2/df}}\rightarrow t$$

$$\frac{\chi^2/df}{\chi^2/df}\rightarrow F$$

$$t(r)^2\rightarrow F(1,r)$$

$$F(m,n)^{-1}\rightarrow F(n,m)$$

### 视觉直觉

- 标准正态与 t：可正可负，关于 0 对称；t 的尾部更厚，自由度增大时更接近标准正态。
- 卡方与 F：只在正半轴；常表现为右偏。

### 关键纠错

- `N(0,2σ²)` 的标准差是 `sqrt(2)σ`。
- 标准化式平方后，分母也必须平方。
- 标准样本方差是除以 `n-1`。
- `t(n-1)^2` 对应 `F(1,n-1)`。

---

## Day 15｜矩估计 + 最大似然 + 估计量评价

### 矩

k 阶原点矩：

$$E(X^k)$$

一阶原点矩就是期望：

$$E(X)$$

二阶中心矩就是方差：

$$E[(X-E(X))^2]=D(X)$$

### 矩估计

核心思想：

$$\text{总体矩}=\text{样本对应矩}$$

最常用：

$$E(X)=\overline X$$

若：

$$E(X)=g(\theta)$$

则令：

$$g(\theta)=\overline X$$

再解出 $\hat\theta$。

### 最大似然估计

若样本独立：

$$L(\theta)=\prod_{i=1}^nf(X_i;\theta)$$

常规流程：

$$\text{写似然}\rightarrow\text{取对数}\rightarrow\text{求导}\rightarrow\text{找最大值}$$

多总体时：把所有组、所有样本对应的密度全部乘起来。

### 单调似然

若 $X\sim U(0,\theta)$：

要求：

$$\theta\ge X_{(n)}$$

其中：

$$X_{(n)}=\max(X_1,\dots,X_n)$$

因为：

$$L(\theta)=\theta^{-n}$$

随 $\theta$ 增大而减小，因此：

$$\hat\theta=X_{(n)}$$

### 两组指数样本共同估计参数

一组均值为 $\theta$，另一组均值为 $2\theta$ 时，得到：

$$\hat\theta=\frac{\sum_{i=1}^nX_i+\frac12\sum_{j=1}^mY_j}{n+m}$$

并且：

$$D(\hat\theta)=\frac{\theta^2}{n+m}$$

### 无偏性

若：

$$E(\hat\theta)=\theta$$

则称 $\hat\theta$ 是 $\theta$ 的无偏估计量。

偏差：

$$\operatorname{Bias}(\hat\theta)=E(\hat\theta)-\theta$$

### 两个无偏估计量比较

在都无偏时，方差更小的估计量波动更小、通常更稳定。

### 一致性直觉

$$\hat\theta_n\xrightarrow{P}\theta$$

若：

$$E(\hat\theta_n)=\theta$$

且：

$$D(\hat\theta_n)\to0$$

则估计量会越来越集中在真实参数附近。
