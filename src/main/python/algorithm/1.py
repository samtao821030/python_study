def func1(startNum,endNum):
    count=0;
    for x in range(startNum,endNum):
        numberStr=str(x)
        count+=numberStr.count('7')
    print(str('%s到%s中，7的总个数为%d'%(startNum,endNum,count)))

#func1(0,10000)


def func2():
    #获取只有1位7的所有数中的7的总和
    count1=4*pow(9,3)*1
    #获取只有2位7的所有数中的7的总和
    count2=6*pow(9,2)*2
    #获取只有3位7的所有数中的7的总和
    count3=4*pow(9,1)*3
    #获取只有3位7的所有数中的7的总和
    count4=4

    totalCount=count1+count2+count3+count4
    print(totalCount)

func2()