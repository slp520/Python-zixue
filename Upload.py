import flask,os,time
from flask import request,send_from_directory,jsonify
app = flask.Flask(__name__)#创建一个app，代表这个web服务
@app.route('/get_file',methods=['get'])
def get_file():
    #下载文件接口
    filename = request.values.get('fname',None)
    #获取需要下载的文件名
    if filename:#如果获取到的文件名话
        if os.path.isfile(filename):#判断是否是一个文件
            #返回要下载的文件
            return send_from_directory('.',filename,as_attachment=True)
        else:
            return jsonify({"msg":"文件不存在!"})
    else:
        return jsonify({'msg':'文件名不能为空'})
@app.route('/files',methods=['get'])
def file_list():
    #获取文件列表接口
    files = os.listdir('.')#获取当前目录下所有文件
    new_files = [f for f in files if os.path.isfile(f)]
    #三元运算符，把是文件的放到list中
    return jsonify({"files":new_files})
@app.route('/upload',methods=['post'])
def upload():
    #上传文件接口
    f = request.files.get('file_name',None)
    if f:
        t = time.strftime('%Y%m%d%H%M%S')#获取当前时间
        new_file_name = t+f.filename#给文件重命名，防止有重复文件覆盖
        f.save(new_file_name)#保存文件
        return jsonify({"code":"ok"})
    else:
        return jsonify({"msg":"请上传文件！"})
app.run(debug=True,port=8018)#启动这个web服务