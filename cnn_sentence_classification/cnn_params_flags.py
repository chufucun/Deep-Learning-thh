#!/usr/bin/env python
# -*- coding:utf-8 -*
import tensorflow as tf
from cnn_sentence_classification.app_root import get_root_path
import os
'''
    tf.app.flags.FLAGS 使用全局变量
    python train.py --positive_data_file "./data/en_polaritydata/rt-polarity.pos"
    --negative_data_file "./data/en_polaritydata/rt-polarity.neg"
    如果不传参数,采用默认设置
'''
project_root_path = get_root_path()
model_log_path = os.path.join(project_root_path,'model_log')

FLAGS = tf.app.flags.FLAGS
tf.flags.DEFINE_string("model_log",model_log_path,"model_log")
tf.flags.DEFINE_float("dev_sample_percentage", .1, "Percentage of the training data to use for validation")
tf.flags.DEFINE_string("positive_data_file", project_root_path + "/data/en_polaritydata/rt-polarity.pos",
                       "positive data file path")
tf.flags.DEFINE_string("negative_data_file", project_root_path + "/data/en_polaritydata/rt-polarity.neg",
                       "negative data file path")
# 模型超参数
# Model Hyperparameters
tf.flags.DEFINE_integer("embedding_dims",128,"Dimensionality of character embedding (default: 128)")
tf.flags.DEFINE_float("dropout_keep_prob",0.5,"Dropout keep probability (default: 0.5)")
tf.flags.DEFINE_string("filter_size","3,4,5","Comma-separated filter sizes (default:'3、4、5')")
tf.flags.DEFINE_integer("num_filter_per_region",128,"Number of filters per region size (default: 128)")
tf.flags.DEFINE_float("l2_reg_lambda",0.0,"L2 regularization lambda (default: 0.0)")

# 训练参数
# Training parameters



# 杂项
# Misc Parameters
tf.flags.DEFINE_boolean("allow_soft_placement",True,"Allow device soft device placement")
tf.flags.DEFINE_boolean("log_device_placement",True,"Log placement of ops on devices")

# create the directory for Tensorboard variable if there is not
if not os.path.exists(FLAGS.model_log):
    os.makedirs(FLAGS.model_log)

def test_params():
    positive_data_file = FLAGS.positive_data_file
    negative_data_file = FLAGS.negative_data_file
    print("positive_data_file %s" % positive_data_file)
    print("negative_data_file %s" % negative_data_file)


if __name__ == "__main__":
    test_params()