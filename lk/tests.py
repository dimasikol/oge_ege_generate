
"""27 задания с лаборатории МЭШ"""
#задание №1
# date = [[5,3],33,41,19,22,40]
# s=0
# count=0
# for i in range(date[0][0]):
#     s+=date[i+1]
#     if s%date[0][1]==0:
#        count+=1
# print(count)

#задание №2
# date = [[5,2],2,-2,2,-2,2]
# s=0
# repeat=0
# maxx=-100000
# for i in range(date[0][0]):
#     s+=date[i+1]
#     if s>=maxx:
#         if s==maxx:
#             repeat+=1
#         else:
#             repeat=1
#             maxx=s
# print(maxx,repeat)

#задание № 3
#
# date = [[5,3],33,41,19,22,40]
# s=0
# len_date=0
# for i in range(date[0][0]):
#     s+=date[i+1]
#     if s%date[0][1]==0:
#         len_date=i
# print(i-1)

#задание № 4
# date  = [[5,3],33,41,19,22,40]
# s_ost=sum(date[1:])%date[0][1]
# len_date=0
# date2=[0*len(date)-1]
# for i in range(date[0][0]):
#     date2=date[i+1]%date[0][1]
