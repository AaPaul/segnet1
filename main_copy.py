import tensorflow as tf
import model

FLAGS = tf.app.flags.FLAGS

# 这里还需要定义个testing、finetune以及training？
# 不用，这里直接把下面判断时候打非空，其他不要的过程得要注释掉

#tf.app.flags.DEFINE_string('testing', 'aa', """ checkpoint file """)
tf.app.flags.DEFINE_string('testing', "E:/workspace/mystoreroom/segnet1/SegNet/Logs/model.ckpt-19999", """checkfile""")  # 若需要运行train，注释掉这个
# tf.app.flags.DEFINE_string('testing', "", """checkfile""")

tf.app.flags.DEFINE_string('finetune', '', """ finetune checkpoint file """)
tf.app.flags.DEFINE_integer('batch_size', "5", """ batch_size """)
tf.app.flags.DEFINE_float('learning_rate', "1e-3", """ initial lr """)
tf.app.flags.DEFINE_string('log_dir', "E:/workspace/mystoreroom/segnet1/SegNet/Logs", """ dir to store ckpt """)
tf.app.flags.DEFINE_string('image_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/train.txt", """ path to CamVid image """)

tf.app.flags.DEFINE_string('test_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/test.txt", """ path to CamVid test image """)
# tf.app.flags.DEFINE_string('test_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/t1.txt", """ path to CamVid test image """)

tf.app.flags.DEFINE_string('val_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/val.txt", """ path to CamVid val image """)
tf.app.flags.DEFINE_integer('max_steps', "20000", """ max_steps """)
tf.app.flags.DEFINE_integer('image_h', "360", """ image height """)
tf.app.flags.DEFINE_integer('image_w', "480", """ image width """)
tf.app.flags.DEFINE_integer('image_c', "3", """ image channel (RGB) """)
tf.app.flags.DEFINE_integer('num_class', "11", """ total class number """)
tf.app.flags.DEFINE_boolean('save_image', True, """ whether to save predicted image """)

# 测试分割函数的，上为该项目原函数
# tf.app.flags.DEFINE_string('log_dir', "D:/segnet/Train_Log", """ dir to store ckpt """)
# tf.app.flags.DEFINE_string('image_dir', "D:/segnet/data_set/train.txt", """ path to CamVid image """)
# tf.app.flags.DEFINE_string('val_dir', "D:/segnet/data_set/val.txt", """ path to CamVid val image """)
# tf.app.flags.DEFINE_integer('image_h', "480", """ image height """)




def checkArgs():
    if FLAGS.testing != '':
        print('The model is set to Testing')
        print("check point file: %s"%FLAGS.testing)
        print("CamVid testing dir: %s"%FLAGS.test_dir)
    elif FLAGS.finetune != '':
        print('The model is set to Finetune from ckpt')
        print("check point file: %s"%FLAGS.finetune)
        print("CamVid Image dir: %s"%FLAGS.image_dir)
        print("CamVid Val dir: %s"%FLAGS.val_dir)
    else:
        print('The model is set to Training')
        print("Max training Iteration: %d"%FLAGS.max_steps)
        print("Initial lr: %f"%FLAGS.learning_rate)
        print("CamVid Image dir: %s"%FLAGS.image_dir)
        print("CamVid Val dir: %s"%FLAGS.val_dir)

    print("Batch Size: %d"%FLAGS.batch_size)
    print("Log dir: %s"%FLAGS.log_dir)



def main(args):
    checkArgs()
    # if FLAGS.testing:
    if FLAGS.testing != '':
        model.test(FLAGS)
    # elif FLAGS.finetune:
    elif FLAGS.finetune == '1':
        model.training(FLAGS, is_finetune=True)
    else:
        model.training(FLAGS, is_finetune=False)

if __name__ == '__main__':
  tf.app.run()
