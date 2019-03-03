'''Softmax-Classifier for CIFAR-10'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import time
import data_helpers

beginTime = time.time()

# Parameter definitions
batch_size = 100
learning_rate = 0.005
max_steps = 1000

# Uncommenting this line removes randomness
# You'll get exactly the same result on each run
# np.random.seed(1)

# Prepare data
data_sets = data_helpers.load_data()

# -----------------------------------------------------------------------------
# Prepare the TensorFlow graph
# (We're only defining the graph here, no actual calculations taking place)
# -----------------------------------------------------------------------------

# Define input placeholders 定义占位符, shape=none代表可以输入任意多个图像(样本集个数),3072每幅图像的浮点值
images_placeholder = tf.placeholder(tf.float32, shape=[None, 3072])
labels_placeholder = tf.placeholder(tf.int64, shape=[None])

# Define variables (these are the values we want to optimize) weights和biases是我们希望优化的变量,weights是一个3072*10的矩阵
# ,结果是一个10维向量,是10个加权和,表示在10个分类中的得分情况.3072*10这个矩阵中的初始值设为0,经过训练后得出最终结果=>模型参数
# 偏差值保证每个分类的起始值不为0
weights = tf.Variable(tf.zeros([3072, 10]))
biases = tf.Variable(tf.zeros([10]))

# Define the classifier's result=>定义分类的打分值
logits = tf.matmul(images_placeholder, weights) + biases

# Define the loss function=>定义损失函数:比较真实值和预测值,得到损失值.损失值越小,说明预测得越准确
#sparse_softmax_cross_entropy_with_logits()函数的输出就是每幅输入图像的损失值

loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits,
  labels=labels_placeholder))
#但是我们如何调整参数来将损失最小化呢？TensorFlow这时就大发神威了。
# 通过被称作自动分化（auto-differentiation）的技术，它可以计算出相对于参数值，
# 损失值的梯度。这就是说它可以知道每个参数对总的损失的影响，小幅度的加或减参数是否可以降低损失。
# 然后依此调整所有参数值，增加模型的准确性。在完成参数调整之后，整个过程重新开始，新的一组图片被输入到模型中。
#GradientDescentOptimizer=>梯度下降优化器
#learning_rate=>学习率 学习率越大,则参数调整得越快,但是可能导致不能收敛.学习率越小,参数调整得越慢,意味着要
#花很长时间才能找到一个好的参数值
# Define the training operation
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# Operation comparing prediction with true label
#以下两行代码用于比较真实值和预测结果,得到模型的精确度accuracy
#tf.argmax(logits, 1)返回分数最高的分类,
#correct_prediction是一个boolean值,所以需要强转成float,便于数学统计
correct_prediction = tf.equal(tf.argmax(logits, 1), labels_placeholder)

# Operation calculating the accuracy of our predictions
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# -----------------------------------------------------------------------------
# Run the TensorFlow graph
# -----------------------------------------------------------------------------

with tf.Session() as sess:
  # Initialize variables
  sess.run(tf.global_variables_initializer())

  # Repeat max_steps times
  for i in range(max_steps):

    # Generate input data batch
    indices = np.random.choice(data_sets['images_train'].shape[0], batch_size)
    images_batch = data_sets['images_train'][indices]
    labels_batch = data_sets['labels_train'][indices]

    # Periodically print out the model's current accuracy
    if i % 100 == 0:
      train_accuracy = sess.run(accuracy, feed_dict={
        images_placeholder: images_batch, labels_placeholder: labels_batch})
      print('Step {:5d}: training accuracy {:g}'.format(i, train_accuracy))

    # Perform a single training step
    sess.run(train_step, feed_dict={images_placeholder: images_batch,
      labels_placeholder: labels_batch})

  # After finishing the training, evaluate on the test set
  test_accuracy = sess.run(accuracy, feed_dict={
    images_placeholder: data_sets['images_test'],
    labels_placeholder: data_sets['labels_test']})
  print('Test accuracy {:g}'.format(test_accuracy))

endTime = time.time()
print('Total time: {:5.2f}s'.format(endTime - beginTime))
