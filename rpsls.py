#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��޳���
���ڣ�2020��4��3��
"""

import random
comp_number=random.randrange(0,5)



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
	    name_to_number=0
    elif name=="ʷ����":
	    name_to_number=1
    elif name=="ֽ":
	    name_to_number=2
    elif name=="����":
        name_to_number=3
    elif name=="����":
	    name_to_number=4
		
    else:
	    print("Error: No Correct Name")
		
    return name_to_number

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
	    number_to_name="ʯͷ"
    elif number==1:
	    number_to_name="ʷ����"
    elif number==2:
	    number_to_name="ֽ"
    elif number==3:
	    number_to_name="����" 
    else:
	    number_to_name="����" 
		
    return number_to_name

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    # pass #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice_number=name_to_number(player_choice)
    
    if player_choice_number==0 and (comp_number==3 or comp_number== 4):
        print("��Ӯ��") 
    elif player_choice_number==1 and (comp_number==0 or comp_number==4):
        print("��Ӯ��")
    elif player_choice_number==2 and (comp_number==0 or comp_number==1):
        print("��Ӯ��")
    elif player_choice_number==3 and (comp_number==1 or comp_number==2):
        print("��Ӯ��")
    elif player_choice_number==4 and (comp_number==2 or comp_number==3):
        print("��Ӯ��")
    elif player_choice_number==comp_number:
	    print("���ͼ��������һ����")
    else:
	    print("�����Ӯ��")
	


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    # pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
choice_name=input("����������ѡ��:")
print("----------------")
print("����ѡ��Ϊ��%s"%choice_name)
b=number_to_name(comp_number)
print("�������ѡ��Ϊ:"+str(b))
y=rpsls(choice_name)


