from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import Post
import sqlite3
from contextlib import closing
import random
# Create your views here.
"""def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
"""

class Neta:
    def __init__ (self,id,name,addr,att):
        self.id=id
        self.name=name
        self.addr=addr
        self.att=att
    def set_att(att):
        self.att=att

def post_list(request):
    db_name = 'dbtest.db'
    set_of_data=range(1,89) #ここでリストの値をしゅとく
    quiz_num = 4
    rand_list = random.sample(set_of_data,quiz_num)
    rand_list.append(rand_list[random.randint(0,len(rand_list)-1)])
    #neta_dic[ getdata(num) for num in rand_list]
    template = loader.get_template('blog/quiz.html')
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        #hirake='.table'
        #c.execute(hirake)
        select_sql = 'SELECT id,name,addr FROM master WHERE id is '
        #print(select_sql)
        netas=[]
        for i in range(quiz_num+1):
            sql = select_sql + str(rand_list[i])
            
            #select_sql = select_sql + (' OR 'if i < 3 else '')
            row=[row for row in c.execute(sql)]
            #netas.append(row)
            netas.append(Neta(row[0][0],row[0][1],row[0][2],0))
    nts={'neta0':netas[0],
         'neta1':netas[1],
         'neta2':netas[2],
         'neta3':netas[3],
         'neta4':netas[4],
         'score':0,
         'total':1}
        #print(netas)
    return HttpResponse(template.render(nts,request))
	
	
def output(request):
    db_name = 'dbtest.db'
    template = loader.get_template("blog/output.html")
    result = loader.get_template("blog/result.html")
    input_id = int(request.POST["select"])
    ans_id = int(request.POST["ans"])
    score = int(request.POST["score"])
    total = int(request.POST["total"])
    ret = 'ぴんぽーん！' if input_id is ans_id else 'ぶっぶー！'
    score += 1 if input_id is ans_id else 0
    choices = request.POST["choices"]
    choices= [int(x.strip()) for x in choices.split(',')]
    choices.append(input_id)
    choices.append(ans_id)
    quiz_num = 4
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        #hirake='.table'
        #c.execute(hirake)
        select_sql = 'SELECT id,name,addr FROM master WHERE id is '
        #print(select_sql)
        netas=[]
        for i in range(quiz_num+2):
            sql = select_sql + str(choices[i])
            
            #select_sql = select_sql + (' OR 'if i < 3 else '')
            row=[row for row in c.execute(sql)]
            #netas.append(row)
            netas.append(Neta(row[0][0],row[0][1],row[0][2],0))
    nts={'neta0':netas[0],
         'neta1':netas[1],
         'neta2':netas[2],
         'neta3':netas[3],
         'input':netas[4],
         'ans':netas[5],
         'str':ret,
         'next_button':'eat',
         'score':score,
         'total':total}
        #print(netas)
    if total is 5:
        return HttpResponse(result.render(nts,request))
    else:
        return HttpResponse(template.render(nts, request))

def more(request):
    db_name = 'dbtest.db'
    set_of_data=range(1,89) #ここでリストの値をしゅとく
    quiz_num = 4
    rand_list = random.sample(set_of_data,quiz_num)
    rand_list.append(rand_list[random.randint(0,len(rand_list)-1)])
    #neta_dic[ getdata(num) for num in rand_list]
    score = int(request.POST["score"])
    total = int(request.POST["total"])+1
    template = loader.get_template('blog/quiz.html')
    with closing(sqlite3.connect(db_name)) as conn:
        c = conn.cursor()
        #hirake='.table'
        #c.execute(hirake)
        select_sql = 'SELECT id,name,addr FROM master WHERE id is '
        #print(select_sql)
        netas=[]
        for i in range(quiz_num+1):
            sql = select_sql + str(rand_list[i])
            
            #select_sql = select_sql + (' OR 'if i < 3 else '')
            row=[row for row in c.execute(sql)]
            #netas.append(row)
            netas.append(Neta(row[0][0],row[0][1],row[0][2],0))
    nts={'neta0':netas[0],
         'neta1':netas[1],
         'neta2':netas[2],
         'neta3':netas[3],
         'neta4':netas[4],
         'score':score,
         'total':total}
        #print(netas)
    return HttpResponse(template.render(nts,request))

def result(request):
    result = loader.get_template("blog/result.html")
    score = int(request.POST["score"])
    total = int(request.POST["total"])
    nts={'score':score,
         'total':total}
    return HttpResponse(template.render(nts,request))