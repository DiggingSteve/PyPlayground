# -*- coding: utf-8 -*-
"""
ʶ��ͼ����࣬Ϊ�˿��ٽ��ж��ʶ����Ե��ô�������ķ�����
R = Recognizer(image_height, image_width, max_captcha)
for i in range(10):
    r_img = Image.open(str(i) + ".jpg")
    t = R.rec_image(r_img)
�򵥵�ͼƬÿ�Ż����Ͽ��Դﵽ���뼶��ʶ���ٶ�
"""
import tensorflow as tf
import numpy as np
from PIL import Image
from cnnlib.network import CNN
import json


class Recognizer(CNN):
    def __init__(self, image_height, image_width, max_captcha, char_set, model_save_dir):
        # ��ʼ������
        super(Recognizer, self).__init__(image_height, image_width, max_captcha, char_set, model_save_dir)

        # �½�ͼ�ͻỰ
        self.g = tf.Graph()
        self.sess = tf.compat.v1.Session(graph=self.g)
        # ʹ��ָ����ͼ�ͻỰ
        with self.g.as_default():
            # ����ѭ��ǰ��д�������õ��������ļ�����ʽ�����д��ѭ���У��ᷢ���ڴ�й©������ʶ����ٶ�
            # tf��ʼ��ռλ��
            self.X = tf.compat.v1.placeholder(tf.float32, [None, self.image_height * self.image_width])  # ��������
            self.Y = tf.compat.v1.placeholder(tf.float32, [None, self.max_captcha * self.char_set_len])  # ��ǩ
            self.keep_prob = tf.compat.v1.placeholder(tf.float32)  # dropoutֵ
            # ���������ģ�Ͳ���
            self.y_predict = self.model()
            self.predict = tf.argmax(input=tf.reshape(self.y_predict, [-1, self.max_captcha, self.char_set_len]), axis=2)
            saver = tf.compat.v1.train.Saver()
            with self.sess.as_default() as sess:
                saver.restore(sess, self.model_save_dir)

    # def __del__(self):
    #     self.sess.close()
    #     print("session close")

    def rec_image(self, img):
        # ��ȡͼƬ
        img_array = np.array(img)
        test_image = self.convert2gray(img_array)
        test_image = test_image.flatten() / 255
        # ʹ��ָ����ͼ�ͻỰ
        with self.g.as_default():
            with self.sess.as_default() as sess:
                text_list = sess.run(self.predict, feed_dict={self.X: [test_image], self.keep_prob: 1.})

        # ��ȡ���
        predict_text = text_list[0].tolist()
        p_text = ""
        for p in predict_text:
            p_text += str(self.char_set[p])

        # ����ʶ����
        return p_text


def main():
    with open("conf/sample_config.json", "r", encoding="utf-8") as f:
        sample_conf = json.load(f)
    image_height = sample_conf["image_height"]
    image_width = sample_conf["image_width"]
    max_captcha = sample_conf["max_captcha"]
    char_set = sample_conf["char_set"]
    model_save_dir = sample_conf["model_save_dir"]
    R = Recognizer(image_height, image_width, max_captcha, char_set, model_save_dir)
    r_img = Image.open("./sample/test/2b3n_6915e26c67a52bc0e4e13d216eb62b37.jpg")
    t = R.rec_image(r_img)
    print(t)


if __name__ == '__main__':
    main()
