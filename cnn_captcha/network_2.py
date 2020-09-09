import tensorflow as tf
import numpy as np
import os
from PIL import Image
import random



class CNN(object):
    def __init__(self, image_height, image_width, max_captcha, char_set, model_save_dir):
        # ��ʼֵ
        self.image_height = image_height
        self.image_width = image_width
        self.max_captcha = max_captcha
        self.char_set = char_set
        self.char_set_len = len(char_set)
        self.model_save_dir = model_save_dir  # ģ��·��
        with tf.compat.v1.name_scope('parameters'):
            self.w_alpha = 0.01
            self.b_alpha = 0.1
        # tf��ʼ��ռλ��
        with tf.compat.v1.name_scope('data'):
            self.X = tf.compat.v1.placeholder(tf.float32, [None, self.image_height * self.image_width])  # ��������
            self.Y = tf.compat.v1.placeholder(tf.float32, [None, self.max_captcha * self.char_set_len])  # ��ǩ
            self.keep_prob = tf.compat.v1.placeholder(tf.float32)  # dropoutֵ

    @staticmethod
    def convert2gray(img):
        """
        ͼƬתΪ�Ҷ�ͼ�������3ͨ��ͼ����㣬��ͨ��ͼ��ֱ�ӷ���
        :param img:
        :return:
        """
        if len(img.shape) > 2:
            r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
            gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
            return gray
        else:
            return img

    def text2vec(self, text):
        """
        ת��ǩΪoneHot����
        :param text: str
        :return: numpy.array
        """
        text_len = len(text)
        if text_len > self.max_captcha:
            raise ValueError('��֤���{}���ַ�'.format(self.max_captcha))

        vector = np.zeros(self.max_captcha * self.char_set_len)

        for i, ch in enumerate(text):
            idx = i * self.char_set_len + self.char_set.index(ch)
            vector[idx] = 1
        return vector

    def model(self):
        x = tf.reshape(self.X, shape=[-1, self.image_height, self.image_width, 1])
        print(">>> input x: {}".format(x))

        # �����1
        wc1 = tf.compat.v1.get_variable(name='wc1', shape=[3, 3, 1, 32], dtype=tf.float32,
                              initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))
        bc1 = tf.Variable(self.b_alpha * tf.random.normal([32]))
        conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(input=x, filters=wc1, strides=[1, 1, 1, 1], padding='SAME'), bc1))
        conv1 = tf.nn.max_pool2d(input=conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv1 = tf.nn.dropout(conv1, 1 - (self.keep_prob))

        # �����2
        wc2 = tf.compat.v1.get_variable(name='wc2', shape=[3, 3, 32, 64], dtype=tf.float32,
                              initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))
        bc2 = tf.Variable(self.b_alpha * tf.random.normal([64]))
        conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(input=conv1, filters=wc2, strides=[1, 1, 1, 1], padding='SAME'), bc2))
        conv2 = tf.nn.max_pool2d(input=conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv2 = tf.nn.dropout(conv2, 1 - (self.keep_prob))

        # �����3
        wc3 = tf.compat.v1.get_variable(name='wc3', shape=[3, 3, 64, 128], dtype=tf.float32,
                              initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))
        bc3 = tf.Variable(self.b_alpha * tf.random.normal([128]))
        conv3 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(input=conv2, filters=wc3, strides=[1, 1, 1, 1], padding='SAME'), bc3))
        conv3 = tf.nn.max_pool2d(input=conv3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
        conv3 = tf.nn.dropout(conv3, 1 - (self.keep_prob))
        print(">>> convolution 3: ", conv3.shape)
        next_shape = conv3.shape[1] * conv3.shape[2] * conv3.shape[3]

        # ȫ���Ӳ�1
        wd1 = tf.compat.v1.get_variable(name='wd1', shape=[next_shape, 1024], dtype=tf.float32,
                              initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))
        bd1 = tf.Variable(self.b_alpha * tf.random.normal([1024]))
        dense = tf.reshape(conv3, [-1, wd1.get_shape().as_list()[0]])
        dense = tf.nn.relu(tf.add(tf.matmul(dense, wd1), bd1))
        dense = tf.nn.dropout(dense, 1 - (self.keep_prob))

        # ȫ���Ӳ�2
        wout = tf.compat.v1.get_variable('name', shape=[1024, self.max_captcha * self.char_set_len], dtype=tf.float32,
                               initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))
        bout = tf.Variable(self.b_alpha * tf.random.normal([self.max_captcha * self.char_set_len]))

        with tf.compat.v1.name_scope('y_prediction'):
            y_predict = tf.add(tf.matmul(dense, wout), bout)

        return y_predict
