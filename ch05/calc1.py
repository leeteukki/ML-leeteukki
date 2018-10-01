# Tensorflow 추출하기
import tensorflow as tf

# 상수 정의
a = tf.constant(1234)

b = tf.constant(5000)

# 계산 정의
add_op = a + b

# 세션 시작하기 
sess = tf.Session()
res = sess.run(add_op)
print(res)
