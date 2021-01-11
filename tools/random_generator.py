# -*- coding: utf-8 -*-
import random

'''
按权重随机抽取
tickets_map为权重表，权重为int值，越大代表抽取概率越大。
'''
tickets_map = {
  'name_1': 2,
  'name_2': 1,
  'name_3': 1,
  'name_4': 1,
  'name_5': 2,
  'name_6': 1,
}

pool = []
for name in tickets_map:
  for i in range(tickets_map[name]):
    pool.append(name)

random.shuffle(pool)
print("Initial pool: ", pool)

for i in range(2):
  print("Round ", i)
  choose_name = random.sample(pool, 1)
  print("Choose: ", choose_name)
  for j in range(tickets_map[choose_name[0]]):
    pool.remove(choose_name[0])
  random.shuffle(pool)
  print("Current pool: ", pool)
