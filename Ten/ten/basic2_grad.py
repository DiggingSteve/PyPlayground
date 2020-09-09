import tensorflow as tf

#在机器学习中，我们经常需要计算函数的导数。TensorFlow 提供了强大的 自动求导机制 来计算导数。在即时执行模式下，TensorFlow 引入了 tf.GradientTape() 这个 “求导记录器” 来实现自动求导。以下代码展示了如何使用 tf.GradientTape() 计算函数 y(x) = x^2 在 x = 3 时的导数：
x = tf.Variable(initial_value =3.)
with tf.GradientTape() as tape:     # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
    y = tf.square(x)
y_grad = tape.gradient(y, x)        # 计算y关于x的导数
print(y, y_grad)