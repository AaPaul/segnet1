import tensorflow as tf

x = tf.constant([1,1,1],[1,1,1])
# x = tf.constant(1)


sess = tf.Session()
with sess.as_default():
    print('结果：',sess.run(x.tf.get_collection()))
