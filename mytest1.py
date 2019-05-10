import tensorflow as tf
import model
import get_pic_name

import sys,base64
from io import BytesIO
import time
from flask import Flask, jsonify, request
from PIL import Image

FLAGS = tf.app.flags.FLAGS
app = Flask(__name__)



def checkArgs():
    print('The model is set to Testing')
    print("check point file: %s" % FLAGS.testing)
    print("CamVid testing dir: %s" % FLAGS.test_dir)
    print("Batch Size: %d" % FLAGS.batch_size)
    print("Log dir: %s" % FLAGS.log_dir)


@app.route('/test', methods=['post'])
def test():
    start = time.clock()
    if (request):
        print("concept")
        # 将图片保存到本地
        # dict = request.files.to_dict()
        # name = dict['file'].filename
        # print(name)
        file = request.files['file']
        name = file.filename
        file.save("E:/workspace/mystoreroom/segnet1/test_pic/"+name)

        # data_files = BytesIO(base64.b64decode(request.data))
        # img = Image.open(data_files)
        # img.show()
        # img.save("E:/workspace/mystoreroom/segnet1/test_pic/test.png")
        '''
        file = open('test.png','wb')
        file.write(data_files)
        file.close()
        '''
        # 得到文件名
        get_pic_name.get_name()
        # 这里还需要定义个testing、finetune以及training？
        # 不用，这里直接把下面判断时候打非空，其他不要的过程得要注释掉

        tf.app.flags.DEFINE_string('testing', "E:/workspace/mystoreroom/segnet1/SegNet/Logs/model.ckpt-19999",
                                   """checkfile""")  # 若需要运行train，注释掉这个

        tf.app.flags.DEFINE_string('finetune', '', """ finetune checkpoint file """)
        tf.app.flags.DEFINE_integer('batch_size', "5", """ batch_size """)
        tf.app.flags.DEFINE_float('learning_rate', "1e-3", """ initial lr """)
        tf.app.flags.DEFINE_string('log_dir', "E:/workspace/mystoreroom/segnet1/SegNet/Logs", """ dir to store ckpt """)
        # tf.app.flags.DEFINE_string('image_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/train.txt", """ path to CamVid image """)

        tf.app.flags.DEFINE_string('test_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/t1.txt",
                                   """ path to CamVid test image """)

        tf.app.flags.DEFINE_string('val_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/val.txt",
                                   """ path to CamVid val image """)
        # tf.app.flags.DEFINE_integer('max_steps', "20000", """ max_steps """)
        tf.app.flags.DEFINE_integer('image_h', "360", """ image height """)
        tf.app.flags.DEFINE_integer('image_w', "480", """ image width """)
        tf.app.flags.DEFINE_integer('image_c', "3", """ image channel (RGB) """)
        tf.app.flags.DEFINE_integer('num_class', "11", """ total class number """)
        tf.app.flags.DEFINE_boolean('save_image', True, """ whether to save predicted image """)

        checkArgs()
        model.test(FLAGS)
    else:
        print("no files")
        sys.exit(1)


if __name__ == '__main__':
    # tf.app.run()
    app.run(host='0.0.0.0', port=8802)



