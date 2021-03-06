from django.shortcuts import render

def post_list(request):
    return render(request,'blog/post_list.html',{})  # template(htmlファイル)にcontext({})の値を書き込んでHTMLにする