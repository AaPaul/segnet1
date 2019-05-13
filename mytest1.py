import tensorflow as tf
import model
import get_pic_name

import sys,base64,os
from io import BytesIO
import time
from flask import Flask, jsonify, request, url_for
from PIL import Image


FLAGS = tf.app.flags.FLAGS
# 这里还需要定义个testing、finetune以及training？
# 不用，这里直接把下面判断时候打非空，其他不要的过程得要注释掉

# tf.app.flags.DEFINE_string('testing', "E:/workspace/mystoreroom/segnet1/SegNet/Logs/model.ckpt-19999",
#                            """checkfile""")
tf.app.flags.DEFINE_string('testing', "E:/workspace/mystoreroom/segnet1/SegNet/model.ckpt-19999",
                           """checkfile""")

tf.app.flags.DEFINE_string('finetune', '', """ finetune checkpoint file """)
tf.app.flags.DEFINE_integer('batch_size', "5", """ batch_size """)
tf.app.flags.DEFINE_float('learning_rate', "1e-3", """ initial lr """)
tf.app.flags.DEFINE_string('log_dir', "E:/workspace/mystoreroom/segnet1/SegNet/Logs", """ dir to store ckpt """)
tf.app.flags.DEFINE_string('test_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/t1.txt",
                           """ path to CamVid test image """)
tf.app.flags.DEFINE_string('val_dir', "E:/workspace/mystoreroom/segnet1/SegNet/CamVid/val.txt",
                           """ path to CamVid val image """)
tf.app.flags.DEFINE_integer('image_h', "360", """ image height """)
tf.app.flags.DEFINE_integer('image_w', "480", """ image width """)
tf.app.flags.DEFINE_integer('image_c', "3", """ image channel (RGB) """)
tf.app.flags.DEFINE_integer('num_class', "11", """ total class number """)
tf.app.flags.DEFINE_boolean('save_image', True, """ whether to save predicted image """)
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
        files = os.listdir("E:/workspace/mystoreroom/segnet1/test_pic")
        for file in files:
            if (os.path.isdir(file) == False):
                os.remove(os.path.join("E:/workspace/mystoreroom/segnet1/test_pic", file))


        path = 'E:/workspace/mystoreroom/segnet1/static/return_pics'
        files = os.listdir(path)
        if (files):
            for file in files:
                f = os.path.join(path, file)
                os.remove(f)
                print(f+"Deleted.")
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


        checkArgs()
        model.test(FLAGS)
        # sys.stdout.flush()
        tf.reset_default_graph()
        # return_file = os.listdir(path)
        # img = Image.open('E:/workspace/mystoreroom/segnet1/static/return_pics/testing_image0.png')
        # dict = 'static/return_pics'
        # return jsonify(dict)

        # 传base64图片
        with open('E:/workspace/mystoreroom/segnet1/static/return_pics/testing_image0.png', 'rb') as f:
            img = f.read()
            img64 = base64.b64encode(img)
            url = jsonify(img64)
            url.headers['Access-Control-Allow-Origin'] = '*'
        return url


    # 传静态地址
        # str = '/static/return_pics/testing_image0.png'
        # # url = make_response(str)
        # # url.headers['Access-Control-Allow-Origin'] = '*'
        # url = jsonify(str)
        # url.headers['Access-Control-Allow-Origin'] = '*'
        # return url

    else:
        print("no files")
        sys.exit(1)
        return 1


#测试访问静态数据
# @app.route('/show_pic', methods=['get'])
# def show_pic():
#     demoCSS = url_for("static", filename="0001TP_008700.png")
#     return demoCSS



if __name__ == '__main__':
    # tf.app.run()
    app.run(host='0.0.0.0', port=8802)



