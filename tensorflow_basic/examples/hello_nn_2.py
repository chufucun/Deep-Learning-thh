#!/usr/bin/env python
# -*- coding:utf-8 -*

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weigths = tf.Variable(tf.truncated_normal(mean=0.0, stddev=0.1, shape=[in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weigths) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


x_data = np.linspace(-1, 1, 300000)[:, np.newaxis]  # 一个":"代表开始,"::"代表结束

# 加入一些噪点,使不完全按二次方的曲线连续分布
noise = np.random.normal(0, 0.01, x_data.shape)  # 正态分布
y_data = np.square(x_data) - 0.5 + noise
# 为了可以 mini-batch
xs = tf.placeholder(tf.float32, shape=(None, 1), name='xs')
ys = tf.placeholder(tf.float32, shape=(None, 1), name='ys')

# 输入层1个神经元  隐层10个  输出层1个
l1 = add_layer(xs, 1, 20, activation_function=tf.nn.relu)
l2 = add_layer(l1, 20, 20, activation_function=tf.nn.relu)

prediction = add_layer(l2, 20, 1, activation_function=None)


# 方差是衡量随机变量或一组数据离散程度的度量, 在概率论中方差用来度量随机变量和其数学期望(均值)之间的偏离程度。
# reduction_indices=1 按行求和
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
# # 定义global_step
# global_step = tf.Variable(0, trainable=False)
# # 通过指数衰减函数来生成学习率
# learing_rate = tf.train.exponential_decay(0.05, global_step, 100, 0.96, staircase=True)

train_step = tf.train.RMSPropOptimizer(0.01).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x_data, y_data)
    plt.ion()

    for i in range(10000):
        session.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if i % 50 == 0:
            # print("prediction %s"%session.run(prediction, feed_dict={xs: x_data, ys: y_data}))
            print(session.run(loss, feed_dict={xs: x_data, ys: y_data}))
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value = session.run(prediction, feed_dict={xs: x_data})
            lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
            plt.pause(0.1)
