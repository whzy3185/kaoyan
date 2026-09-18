# 线性代数 Day 1–Day 7 飞书笔记

## Day 1：线代总框架

$$A=(\alpha_1,\ldots,\alpha_n),\quad x=(x_1,\ldots,x_n)^T$$

$$Ax=x_1\alpha_1+\cdots+x_n\alpha_n$$

$$Ax=b\Longleftrightarrow b\text{ 可由 }A\text{ 的列向量线性表示}$$

$$Ax=b\Longleftrightarrow\text{线性方程组}$$

自由变量个数：

$$n-r(A)$$

方阵：

$$|A|\neq0\Longleftrightarrow A\text{ 可逆}$$

---

## Day 2：行列式基础

二阶行列式：

$$\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$$

交换两行：

$$D\rightarrow-D$$

一行乘 $k$：

$$D\rightarrow kD$$

倍加：

$$R_i\rightarrow R_i+kR_j$$

行列式不变。

两行成比例：

$$D=0$$

三角行列式：

$$D=\text{主对角线元素之积}$$

余子式与代数余子式：

$$A_{ij}=(-1)^{i+j}M_{ij}$$

按行展开：

$$D=\sum_j a_{ij}A_{ij}$$

---

## Day 3：行列式进阶

自交：

$$a_{i1}A_{i1}+\cdots+a_{in}A_{in}=D$$

互交：

$$a_{i1}A_{j1}+\cdots+a_{in}A_{jn}=0\quad(i\neq j)$$

余子式求和先转代数余子式：

$$M_{ij}=(-1)^{i+j}A_{ij}$$

同一行的 $A_{ij}$：把对应行替换成系数，构造新行列式。

同一列的 $A_{ij}$：把对应列替换成系数。

---

## Day 4：矩阵基础

矩阵乘法：左行乘右列。

一般：

$$AB\neq BA$$

单位矩阵：

$$AE=EA=A$$

转置：

$$\left(A^T\right)^T=A$$

对称：

$$A^T=A$$

反对称：

$$A^T=-A$$

反对称矩阵主对角线：

$$a_{ii}=0$$

可逆方阵：

$$|A|\neq0\Longleftrightarrow A\text{ 可逆}\Longleftrightarrow r(A)=n$$

二阶逆矩阵：

$$A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$

---

## Day 5：伴随、秩、初等变换

二阶伴随：

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}^*=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$

$$A^{-1}=\frac{1}{|A|}A^*$$

$$A^*=|A|A^{-1}$$

$$AA^*=A^*A=|A|E$$

具体矩阵求秩：

$$\text{初等行变换}\rightarrow\text{阶梯形}\rightarrow\text{非零行数}$$

初等变换不改变秩。

$$\text{左乘初等矩阵}\Rightarrow\text{对应行变换}$$

求逆：

$$(A\mid E)\rightarrow(E\mid A^{-1})$$

---

## Day 6：秩性质、AB=0、分块、正交

$$r(AB)\le\min\{r(A),r(B)\}$$

$$r(A+B)\le r(A)+r(B)$$

$$k\neq0\Rightarrow r(kA)=r(A)$$

可逆矩阵不改变秩：

$$P,Q\text{ 可逆}\Rightarrow r(PAQ)=r(A)$$

如果：

$$A_{m\times n}B_{n\times s}=0$$

那么：

$$r(A)+r(B)\le n$$

且 $B$ 的每一列都是：

$$Ax=0$$

的解。

块对角：

$$\begin{pmatrix}B&0\\0&C\end{pmatrix}^{-1}=\begin{pmatrix}B^{-1}&0\\0&C^{-1}\end{pmatrix}$$

正交矩阵：

$$Q^{-1}=Q^T$$

---

## Day 7：满秩、消去、等价、高次幂

行满秩：

$$r(A)=\text{行数}$$

列满秩：

$$r(A)=\text{列数}$$

列满秩：

$$Ax=0\text{ 只有零解}$$

行满秩：

$$Ax=b\text{ 对任意 }b\text{ 有解}$$

消去律：

$$\text{右消看行满秩}$$

$$\text{左消看列满秩}$$

同型矩阵等价：

$$A\sim B\Longleftrightarrow r(A)=r(B)$$

若：

$$A^2=cA$$

则：

$$A^n=c^{n-1}A\quad(n\ge1)$$
