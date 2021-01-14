#! /bin/python
# -*- conding: utf-8 -*-

import random

data = [
        {"name":"杏奈", "weight":0.002117},
        {"name":"真步", "weight":0.002117},
        {"name":"璃乃", "weight":0.002117},
        {"name":"初音", "weight":0.002118},
        {"name":"依绪", "weight":0.002118},
        {"name":"咲恋", "weight":0.002118},
        {"name":"望", "weight":0.002118},
        {"name":"妮侬", "weight":0.002118},
        {"name":"秋乃", "weight":0.002118},
        {"name":"真琴", "weight":0.002118},
        {"name":"静流", "weight":0.002118},
        {"name":"莫妮卡", "weight":0.002118},
        {"name":"姬塔", "weight":0.002118},
        {"name":"纯", "weight":0.002118},
        {"name":"亚里莎", "weight":0.002118},
        {"name":"镜华", "weight":0.002118},
        {"name":"伊利亚", "weight":0.002118},
        {"name":"珠希", "weight":0.014}
        ]
data_weight = sum(map(lambda d : d['weight'], data))

data2 = [
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009474},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473},
        {"name":"二星", "weight":0.009473}
        ]
data2_weight = sum(map(lambda d : d['weight'], data2))

data3 = [
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077},
        {"name":"一星", "weight":0.077}
        ]

def pcr(times):
    result = []
    for i in range(times):
        rd = random.random()
        if rd < data_weight:
            weight = 0
            for i in data:
                weight += i['weight']
                if rd < weight:
                    result.append([format(rd, '.6f'), i['name']])
                    break
        elif i % 10 == 9 or rd < data2_weight + data_weight:
            result.append([format(rd, '.6f'), random.choice(data2)['name']])
        else:
            result.append([format(rd, '.6f'), random.choice(data3)['name']])

    return result


if __name__ == "__main__":
    pcr_record = [0, [0, 0], [0, 0], [0, 0]]
    while True:
        inpt = input("Input (number for chou and 'q' for quit) : ")
        if inpt == 'q':
            break
        elif inpt == '':
            continue
        
        times = int(inpt)
        result = pcr(times)
        for i in result:
            pcr_record[0] += 1
            if i[1] == '一星':
                pcr_record[1][0] += 1
                pcr_record[1][1] = format(pcr_record[1][0] / pcr_record[0], '.6f')
            elif i[1] == '二星':
                pcr_record[2][0] += 1
                pcr_record[2][1] = format(pcr_record[2][0] / pcr_record[0], '.6f')
            else:
                pcr_record[3][0] += 1
                pcr_record[3][1] = format(pcr_record[3][0] / pcr_record[0], '.6f')
            print(i)
        print(pcr_record)
