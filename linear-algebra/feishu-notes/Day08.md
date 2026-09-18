# 线性代数 Day 8 飞书笔记

## 1. 线性表示

若存在常数 $k_1,\ldots,k_n$，使

$$\beta=k_1\alpha_1+\cdots+k_n\alpha_n$$

则称 $\beta$ 可由 $\alpha_1,\ldots,\alpha_n$ 线性表示。

令

$$A=(\alpha_1,\ldots,\alpha_n)$$

则线性表示问题等价于：

$$Ax=\beta$$

有解。

充要条件：

$$\beta\text{ 可由 }A\text{ 线性表示}\Longleftrightarrow r(A)=r(A,\beta)$$

## 2. 线性相关与线性无关

若：

$$k_1\alpha_1+\cdots+k_n\alpha_n=0$$

存在不全为 0 的系数，则向量组线性相关。

若只有：

$$k_1=\cdots=k_n=0$$

则线性无关。

令：

$$A=(\alpha_1,\ldots,\alpha_n)$$

则：

$$r(A)=n\Longleftrightarrow\alpha_1,\ldots,\alpha_n\text{ 线性无关}$$

$$r(A)<n\Longleftrightarrow\alpha_1,\ldots,\alpha_n\text{ 线性相关}$$

## 3. 快速判断

向量个数大于空间维数：

$$m>n\quad(m\text{ 个 }n\text{ 维向量})$$

则必线性相关。

若某个子向量组已经线性相关，则整个向量组线性相关。

若整个向量组线性无关，则任意子向量组都线性无关。

若某个向量可以由其余向量线性表示，则整个向量组线性相关。

## 4. 向量组之间的线性表示

若向量组 $B$ 中每个向量都能由 $A$ 线性表示，则：

$$r(B)\le r(A)$$

逆命题一般不成立。

## 5. 向量组等价

若：

$$A\text{ 能由 }B\text{ 线性表示}$$

并且：

$$B\text{ 能由 }A\text{ 线性表示}$$

则 $A,B$ 等价。

此时：

$$r(A)=r(B)$$

注意：秩相等本身不能推出向量组等价。

## 6. 线性表示唯一性

若：

$$Ax=\beta$$

有解，且 $A$ 有 $n$ 列，则：

$$r(A)=n\Rightarrow\text{表示唯一}$$

$$r(A)<n\Rightarrow\text{表示不唯一}$$

自由变量个数：

$$n-r(A)$$

## Day 8 易错点

- 写线性相关的非零系数组合时注意正负号。
- 判断相关 / 无关要比较 $r(A)$ 与向量个数 $n$。
- “能表示”只说明方程有解；是否唯一还要继续看自由变量。
